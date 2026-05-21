# Website Publication Pipeline Instructions for Codex

Use these instructions in the website repository to build a Zotero-driven publication list that matches the CV-generated list.

## Goal

Create a reproducible website publication pipeline equivalent to the CV pipeline.

The website publication list should include the same peer-reviewed article set as:

```text
content/research/publications-generated.tex
```

in the CV repository.

The website output format may differ from LaTeX, but the publication identity, ordering, and inclusion rules should match the CV generated list.

## Inputs

Assume the website repository will have a local `knowledge/` directory with read-only links to Zotero exports:

```text
knowledge/library.json
knowledge/MyLibrary.bib
```

Use `knowledge/library.json` as the primary structured source. Use `knowledge/MyLibrary.bib` as an independent consistency check.

Select only Zotero records that satisfy all of the following:

- tag includes `my-article`
- `itemType == "journalArticle"`
- not excluded by local overrides

Do not edit files inside `knowledge/`.

## Expected Website Files

Adapt paths to the website repository after inspecting its structure. Prefer existing conventions.

Suggested files:

```text
scripts/generate_publications.py
scripts/check_publications.py
content/publications-generated.json
content/publication-overrides.yml
content/people.yml
skills/update-website-pub-list/SKILL.md
skills/update-website-pub-list/scripts/check_publications.py
```

If the website uses Markdown, MDX, YAML, or another data format, generate that format instead of JSON. Keep the generated output in a clearly named file and mark it as generated.

## Matching Rules

Match records in this order:

1. normalized DOI
2. normalized title
3. explicit aliases in `publication-overrides.yml`

Normalize DOI by:

- lowercasing
- removing `https://doi.org/`
- removing `http://doi.org/`
- removing `https://dx.doi.org/`
- removing leading `doi:`
- trimming punctuation

Normalize titles by:

- removing HTML tags
- removing LaTeX commands
- removing braces
- converting Unicode accents to plain text where possible
- lowercasing
- collapsing punctuation and whitespace

## Ordering

Sort publications in reverse publication year order:

1. newer year first
2. within the same year, preserve the CV generated order when possible
3. otherwise sort by Zotero date, then title

The website order should match `content/research/publications-generated.tex` from the CV pipeline as closely as possible.

## Overrides

Create `content/publication-overrides.yml` if needed.

Use it for website-specific or CV-specific presentation data that should not be stored in Zotero:

- excluded citation keys
- DOI aliases
- manually preferred display title
- press release links
- note text
- role tags such as `GS`, `PD`, `PI`, `cPI`, `vGS`
- topic tags such as planetary science or technique
- author display overrides
- URL overrides

Suggested structure:

```yaml
exclude_citation_keys:
  - shim2014Postperovskite

include_unmatched_current_articles: true

doi_aliases:
  someCitationKey:
    - 10.xxxx/example

notes:
  someCitationKey:
    press_releases:
      - label: ASU News
        url: https://example.edu/news
    note: Short website note if needed.
```

Keep overrides small and explicit. Do not duplicate Zotero metadata unless it is needed for website display or matching.

## Author Handling

Create `content/people.yml` if the website needs consistent name rendering.

Use it to unify the user’s name and close collaborator/student display names across Zotero variants.

Examples of variants that should render consistently:

```yaml
canonical_names:
  "Shim, Sang-Heon": "S.-H. Shim"
  "Shim, S.-H.": "S.-H. Shim"
  "Shim, Dan": "S.-H. Shim"
```

For the website, decide whether to render the user’s name in bold, with a CSS class, or as plain text. Keep that display decision in the generator or a presentation layer, not in Zotero.

## Generated Output

The generated website publication file should contain structured records, not LaTeX.

Recommended fields:

```yaml
- citation_key:
  year:
  date:
  title:
  authors:
  journal:
  doi:
  url:
  tags:
  role_tags:
  press_releases:
  note:
```

If the website already has a data schema, use that schema instead.

The generated file should not require manual editing. Put manual data in overrides.

## Checker Workflow

Before generating, create and run a checker script.

The checker should compare:

- existing website publication source, if any
- `knowledge/library.json` records tagged `my-article`
- `knowledge/MyLibrary.bib` records tagged `my-article`
- optionally, the CV `publications-generated.tex` if the website repo can access it

Report:

- Zotero `my-article` records missing from the website
- website records missing from Zotero
- BibTeX records missing from JSON
- JSON records missing from BibTeX
- DOI mismatches
- likely title matches with different DOI
- order differences relative to reverse year order
- order differences relative to the CV generated list, if available

Do not rewrite the website publication file until the user approves generation.

## Generator Workflow

After user approval, run:

```zsh
python scripts/generate_publications.py
```

The generator should:

- read `knowledge/library.json`
- select `my-article` journal articles
- apply `publication-overrides.yml`
- apply `people.yml`
- sort recent first
- write the generated website publication data file
- report the number of records written
- report any selected/override DOI values that were not found

## Website Integration

After generation:

1. Find the website page/component that renders publications.
2. Change it to read the generated data file.
3. Preserve the existing visual design and URL behavior.
4. Run the website build/test command.
5. If possible, run a local dev server and visually inspect the publication page.

Do not redesign the publication page unless explicitly requested.

## Local Skill

Create a repository-local skill:

```text
skills/update-website-pub-list/SKILL.md
```

The skill should be local to the website repo, not global.

It should:

- describe the website-specific file paths
- require checking before generation
- use `my-article`
- use `knowledge/library.json` and `knowledge/MyLibrary.bib`
- explain the override and people files
- require approval before replacing generated website data
- include validation commands for the website build

Also place the checker script inside the skill:

```text
skills/update-website-pub-list/scripts/check_publications.py
```

The repo-level generator should remain in:

```text
scripts/generate_publications.py
```

## Safety Rules

- Do not edit `knowledge/library.json`.
- Do not edit `knowledge/MyLibrary.bib`.
- Do not discard existing website-only display fields; move them into overrides.
- Do not replace the current website publication data until the checker output has been reviewed.
- Keep the generated publication output separate from hand-maintained overrides.
- Run the website build/test command before final reporting.

## Suggested First Codex Prompt in the Website Repo

```text
I want to create a Zotero-driven generated publication list for this website.
Use knowledge/library.json and knowledge/MyLibrary.bib.
Select only journalArticle records with the my-article tag.
Make the generated website publication list match the CV file content/research/publications-generated.tex in publication identity and order.
First inspect the existing website publication data/page and report differences.
Then create a local skill named update-website-pub-list, a checker script, an override YAML file if needed, and a generator script.
Do not switch the website page to the generated data until I approve.
```
