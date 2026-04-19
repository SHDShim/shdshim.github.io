# Add Research News

## Purpose
Add a new research news item in one step while keeping home and research pages synchronized.

## Source Of Truth
- `_data/research.yml`

## What This Skill Updates
- `news.latest` (prepends new item)
- keeps only 2 items in `news.latest`
- moves overflow items into `news.earlier` as archived entries

## Inputs
- `date` in `YYYY.MM` format (example: `2026.04`)
- `text` short news sentence
- `source_label` (example: `Science`)
- `source_url` full link

## Command
```bash
ruby scripts/add_research_news.rb \
  --date "2026.04" \
  --text "Shim has been selected as a Guggenheim Fellow in Astronomy and Astrophysics." \
  --source-label "Guggenheim Foundation" \
  --source-url "https://www.gf.org/stories/announcing-the-2026-guggenheim-fellows"
```

## Verification
```bash
ruby -ryaml -e 'YAML.load_file("_data/research.yml"); puts "research.yml: OK"'
rg -n "news:|latest:|earlier:|Guggenheim|Science" _data/research.yml
```

## Notes
- Do not edit `index.md` or `research.md` for routine news updates; both read from `_data/research.yml`.
- If a `source_url` already exists, the script updates recency by moving it to the top latest slot without duplication.
