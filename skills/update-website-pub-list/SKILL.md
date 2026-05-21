---
name: update-website-pub-list
description: Update this Jekyll website publication list from the local Zotero exports linked under knowledge/.
---

# Update Website Publication List

Use this repository-local skill to update the website publication list from
Zotero while preserving the current website presentation.

## Sources

- Primary structured source: `knowledge/library.json`
- Independent consistency source: `knowledge/MyLibrary.bib`
- Legacy hand-maintained website source: `_data/publications.yml`
- Active website source: `_data/publications_generated.yml`
- Manual overrides: `_data/publication-overrides.yml`
- Publication name rendering: `_data/publication-people.yml`

Treat all files under `knowledge/` as read-only.

## Selection Rule

Include only Zotero records where:

- `itemType == "journalArticle"`
- tags include `my-article`
- the citation key is not listed in `_data/publication-overrides.yml`

## Workflow

1. Run the checker first:

   ```zsh
   python scripts/check_publications.py
   ```

2. Review missing records, DOI mismatches, title matches, and ordering issues.

3. Generate the active website data file:

   ```zsh
   python scripts/generate_publications.py
   ```

4. Compare the candidate file against the active website data:

   ```zsh
   diff -u _data/publications.yml _data/publications_generated.yml
   ```

5. Review the diff before committing changes. The publication page already
   reads `_data/publications_generated.yml`.

6. Validate the website:

   ```zsh
   bundle exec jekyll build
   ```

## Safety Rules

- Do not edit `knowledge/library.json`.
- Do not edit `knowledge/MyLibrary.bib`.
- Keep generated publication output separate from hand-maintained overrides.
- Preserve current publication-page design and URL behavior.
- Use overrides for website-specific display choices, not Zotero metadata.
