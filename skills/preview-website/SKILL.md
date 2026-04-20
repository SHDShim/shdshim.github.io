---
name: preview-website
description: Start a local Jekyll preview for this repository, open any page in Safari, and verify that updated content appears on the expected route.
---

# Preview Website

## Purpose
Preview this website locally with Jekyll and open any page in Safari.

## Inputs
- `route` optional page route (examples: `/`, `/research.html`, `/people.html`, `/dan-shim.html`)
- `check_pattern` optional text pattern for verification

## When To Use
- After content or style updates
- Before committing site changes

## Source Of Truth
- `_config.yml`
- `_data/` (content data files)
- page `.md` files in repository root

## Commands

### 1) Start local preview
Use `rbenv` so the project Ruby in `.ruby-version` is used.

```bash
rbenv exec bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

### 2) Open in Safari
Run in another terminal while the server is running.

```bash
ROUTE="/research.html"
open -a Safari "http://127.0.0.1:4000${ROUTE}"
```

### 3) List candidate pages in this repo
Use this to find routes quickly.

```bash
rg --files -g "*.md" -g "*.html" \
| rg -v "^(_|assets/|vendor/|skills/|scripts/)"
```

Typical routes include:
- `/`
- `/dan-shim.html`
- `/people.html`
- `/research.html`
- `/publications.html`
- `/resources.html`

## Verification
Check that expected text is present in any rendered route.

```bash
ROUTE="/research.html"
PATTERN="Ava Campbell|NSF Graduate Research Fellowship|research.gov/grfp"
curl -s "http://127.0.0.1:4000${ROUTE}" | rg -n "$PATTERN"
```

## Stop Server
In the terminal running Jekyll, press `Ctrl+C`.

## Notes
- If `bundle exec` fails because of Ruby/Bundler mismatch, use `rbenv exec` as shown above.
- Do not edit generated output inside `_site/`.
