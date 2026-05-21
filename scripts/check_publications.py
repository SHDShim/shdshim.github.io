#!/usr/bin/env python3
"""Check website publication data against Zotero JSON and BibTeX exports."""

from __future__ import annotations

from collections import defaultdict

from publication_utils import (
    by_doi,
    item_record,
    load_bibtex_articles,
    normalize_doi,
    normalize_title,
    publication_period,
    selected_zotero_items,
    website_entries,
)


def main() -> int:
    website = website_entries()
    zotero = [item_record(item) for item in selected_zotero_items()]
    bibtex = load_bibtex_articles()

    website_by_doi = by_doi(website)
    zotero_by_doi = by_doi(zotero)
    bib_by_doi = {
        normalize_doi(entry.get("doi")): entry
        for entry in bibtex.values()
        if normalize_doi(entry.get("doi"))
    }

    print("Publication check")
    print("=================")
    print(f"Website entries: {len(website)}")
    print(f"Zotero JSON my-article journalArticle records: {len(zotero)}")
    print(f"BibTeX my-article @article records: {len(bibtex)}")
    print()

    missing_from_website = [record for record in zotero if record["doi"] not in website_by_doi]
    missing_from_zotero = [record for record in website if record["doi"] and record["doi"] not in zotero_by_doi]
    json_missing_from_bib = [record for record in zotero if record["doi"] and record["doi"] not in bib_by_doi]
    bib_missing_from_json = [
        entry
        for doi, entry in bib_by_doi.items()
        if doi and doi not in zotero_by_doi
    ]

    title_to_zotero = defaultdict(list)
    for record in zotero:
        title_to_zotero[record["title_norm"]].append(record)

    likely_title_matches = []
    for entry in website:
        if entry["doi"] in zotero_by_doi:
            continue
        for candidate in title_to_zotero.get(entry["title_norm"], []):
            likely_title_matches.append((entry, candidate))

    order_issues = []
    previous_year = None
    for entry in website:
        year = entry.get("year")
        if previous_year is not None and year is not None and year > previous_year:
            order_issues.append(entry)
        if year is not None:
            previous_year = year

    period_issues = []
    for entry in website:
        expected = publication_period(entry.get("year"))
        if entry.get("period") != expected:
            period_issues.append((entry, expected))

    def print_records(title: str, rows: list, formatter) -> None:
        print(title)
        print("-" * len(title))
        if not rows:
            print("None")
        else:
            for row in rows:
                print(formatter(row))
        print()

    print_records(
        "Zotero records missing from website by DOI",
        missing_from_website,
        lambda r: f"{r['citation_key']} | {r['year']} | {r['doi'] or 'NO DOI'} | {r['title']}",
    )
    print_records(
        "Website records missing from Zotero by DOI",
        missing_from_zotero,
        lambda r: f"{r['year']} | {r['doi']} | {r['entry_html'][:160]}",
    )
    print_records(
        "JSON records missing from BibTeX by DOI",
        json_missing_from_bib,
        lambda r: f"{r['citation_key']} | {r['doi']} | {r['title']}",
    )
    print_records(
        "BibTeX records missing from JSON by DOI",
        bib_missing_from_json,
        lambda e: f"{e.get('ID')} | {normalize_doi(e.get('doi'))} | {normalize_title(e.get('title'))[:120]}",
    )
    print_records(
        "Likely title matches with different or missing DOI",
        likely_title_matches,
        lambda pair: (
            f"website DOI={pair[0]['doi'] or 'NO DOI'} <-> "
            f"zotero DOI={pair[1]['doi'] or 'NO DOI'} | {pair[1]['citation_key']}"
        ),
    )
    print_records(
        "Website reverse-year order issues",
        order_issues,
        lambda r: f"order={r['order']} year={r['year']} doi={r['doi'] or 'NO DOI'}",
    )
    print_records(
        "Website period grouping issues",
        period_issues,
        lambda pair: f"year={pair[0]['year']} current={pair[0]['period']} expected={pair[1]} doi={pair[0]['doi'] or 'NO DOI'}",
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
