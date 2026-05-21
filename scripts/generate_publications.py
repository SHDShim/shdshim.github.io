#!/usr/bin/env python3
"""Generate website publication data from Zotero exports.

The generated file is intentionally separate from the active website data:

    _data/publications_generated.yml

Review the checker output and diff before replacing _data/publications.yml.
"""

from __future__ import annotations

import html
from collections import defaultdict
from copy import deepcopy
from typing import Any

from publication_utils import (
    GENERATED_PUBLICATIONS,
    WEBSITE_PUBLICATIONS,
    item_record,
    item_tags,
    load_bibtex_articles,
    load_yaml,
    normalize_doi,
    publication_period,
    selected_zotero_items,
    website_entries,
    write_yaml,
)


PERIOD_OPEN_DEFAULTS = {
    "2020-present": True,
    "2014-2019": False,
    "2004-2013": False,
    "1999-2002": False,
    "1994-1996": False,
}


def creator_name(creator: dict[str, Any]) -> str:
    first = (creator.get("firstName") or "").strip()
    last = (creator.get("lastName") or creator.get("name") or "").strip()
    if not first:
        return last
    initials = []
    for part in first.replace("-", " ").split():
        if part.endswith("."):
            initials.append(part)
        elif part:
            initials.append(f"{part[0]}.")
    return f"{' '.join(initials)} {last}".strip()


def apply_people_name(name: str, people: dict[str, Any]) -> str:
    canonical = people.get("canonical_names") or {}
    if "," in name:
        key = name
    else:
        parts = name.split()
        key = f"{parts[-1]}, {' '.join(parts[:-1])}" if len(parts) > 1 else name
    return canonical.get(key, canonical.get(name, name))


def render_authors(item: dict[str, Any], people: dict[str, Any]) -> str:
    names = []
    highlights = set(people.get("highlight_names") or [])
    for creator in item.get("creators") or []:
        if creator.get("creatorType") != "author":
            continue
        display = apply_people_name(creator_name(creator), people)
        if display in highlights:
            display = f"<strong>{html.escape(display)}</strong>"
        else:
            display = html.escape(display)
        names.append(display)
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    if len(names) == 2:
        return f"{names[0]} and {names[1]}"
    return f"{', '.join(names[:-1])}, and {names[-1]}"


def render_entry(record: dict[str, Any], people: dict[str, Any]) -> str:
    item = record["item"]
    authors = render_authors(item, people)
    title = html.escape(record["title"])
    journal = html.escape(record["journal"])
    year = record["year"] or ""
    doi = record["doi"]
    citation = f"{authors}. {title}. {journal}, {year}."
    if doi:
        citation += (
            f' <a class="text-link" href="https://doi.org/{html.escape(doi)}" '
            'target="_blank" rel="noreferrer">DOI</a>'
        )
    return citation


def current_entry_candidates() -> tuple[list[dict[str, Any]], dict[str, list[dict[str, Any]]]]:
    entries = website_entries()
    by_doi = defaultdict(list)
    for entry in entries:
        if entry["doi"]:
            by_doi[entry["doi"]].append(entry)
    return entries, by_doi


def match_current_entry(
    record: dict[str, Any],
    current_by_doi: dict[str, list[dict[str, Any]]],
    used_orders: set[int],
) -> dict[str, Any] | None:
    doi = record["doi"]
    if not doi:
        return None
    candidates = [entry for entry in current_by_doi.get(doi, []) if entry["order"] not in used_orders]
    if not candidates:
        return None
    title_norm = record["title_norm"]
    for candidate in candidates:
        if title_norm and title_norm in candidate["title_norm"]:
            return candidate
    return candidates[0]


def sort_key(row: dict[str, Any]) -> tuple[int, int, str]:
    current_order = row.get("current_order")
    if current_order is not None:
        return (0, current_order, "")
    year = row.get("year") or 0
    return (1, -year, row.get("title") or row.get("entry_html") or "")


def main() -> int:
    current_data = load_yaml(WEBSITE_PUBLICATIONS, {}) or {}
    overrides = load_yaml(__import__("publication_utils").OVERRIDES, {}) or {}
    people = load_yaml(__import__("publication_utils").PUBLICATION_PEOPLE, {}) or {}

    current_entries, current_by_doi = current_entry_candidates()
    used_current_orders: set[int] = set()
    selected_rows = []

    bibtex = load_bibtex_articles()
    bibtex_dois = {
        normalize_doi(entry.get("doi"))
        for entry in bibtex.values()
        if normalize_doi(entry.get("doi"))
    }
    missing_bibtex_dois = []

    for item in selected_zotero_items():
        record = item_record(item)
        if record["doi"] and record["doi"] not in bibtex_dois:
            missing_bibtex_dois.append(record)
        matched = match_current_entry(record, current_by_doi, used_current_orders)
        if matched and overrides.get("reuse_existing_html_by_doi", True):
            used_current_orders.add(matched["order"])
            entry_html = matched["entry_html"]
            current_order = matched["order"]
            period = matched["period"] or publication_period(record["year"])
        else:
            entry_html = render_entry(record, people)
            current_order = None
            period = publication_period(record["year"])
        selected_rows.append(
            {
                "citation_key": record["citation_key"],
                "year": record["year"],
                "period": period,
                "entry_html": entry_html,
                "current_order": current_order,
                "title": record["title"],
                "doi": record["doi"],
                "tags": sorted(item_tags(item)),
            }
        )

    if overrides.get("include_unmatched_current_articles", True):
        for entry in current_entries:
            if entry["order"] in used_current_orders:
                continue
            selected_rows.append(
                {
                    "citation_key": "",
                    "year": entry["year"],
                    "period": entry["period"] or publication_period(entry["year"]),
                    "entry_html": entry["entry_html"],
                    "current_order": entry["order"],
                    "title": "",
                    "doi": entry["doi"],
                    "tags": [],
                }
            )

    selected_rows.sort(key=sort_key)

    period_order = [period.get("label") for period in current_data.get("periods") or []]
    for row in selected_rows:
        if row["period"] not in period_order:
            period_order.append(row["period"])

    grouped = {label: [] for label in period_order}
    for row in selected_rows:
        grouped.setdefault(row["period"], []).append(row["entry_html"])

    generated = {
        "hero": deepcopy(current_data.get("hero") or {}),
        "periods": [
            {
                "label": label,
                "open": PERIOD_OPEN_DEFAULTS.get(label, False),
                "entries_html": grouped[label],
            }
            for label in period_order
            if grouped.get(label)
        ],
    }

    write_yaml(GENERATED_PUBLICATIONS, generated)

    print(f"Wrote {GENERATED_PUBLICATIONS.relative_to(__import__('publication_utils').ROOT)}")
    print(f"Selected Zotero records: {len(selected_zotero_items())}")
    print(f"Generated website entries: {sum(len(p['entries_html']) for p in generated['periods'])}")
    print(f"Reused current website entries: {len(used_current_orders)}")
    if missing_bibtex_dois:
        print("Selected JSON records not found in BibTeX by DOI:")
        for record in missing_bibtex_dois:
            print(f"- {record['citation_key']} | {record['doi']} | {record['title']}")
    else:
        print("Selected JSON DOI values were all found in BibTeX.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
