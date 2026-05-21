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
Use `rbenv` so the project Ruby in `.ruby-version` is used. Initialize
`rbenv` explicitly because Codex and other non-interactive shells may not load
the full `~/.zshrc`.

```zsh
cd /Users/danshim/Git-Workspace/websites/website
eval "$(rbenv init - zsh)"
rbenv local 3.2.4
export BUNDLE_USER_HOME="${TMPDIR:-/tmp}/bundle-home"
rbenv exec ruby -v
rbenv exec bundle exec jekyll serve --host 127.0.0.1 --port 4000
```

Expected Ruby:

```text
ruby 3.2.4
```

If gems are missing, install them with the same Ruby context:

```zsh
cd /Users/danshim/Git-Workspace/websites/website
eval "$(rbenv init - zsh)"
rbenv local 3.2.4
export BUNDLE_USER_HOME="${TMPDIR:-/tmp}/bundle-home"
rbenv exec gem install bundler:4.0.10
rbenv exec bundle install
```

If Jekyll reports native extensions are not built, refresh the local bundle for
Ruby `3.2.4`:

```zsh
cd /Users/danshim/Git-Workspace/websites/website
eval "$(rbenv init - zsh)"
rbenv local 3.2.4
export BUNDLE_USER_HOME="${TMPDIR:-/tmp}/bundle-home"
rbenv exec bundle pristine
rbenv exec bundle install
```

### 2) Open in Safari
Run in another terminal while the server is running.

```zsh
ROUTE="/research.html"
open -a Safari "http://127.0.0.1:4000${ROUTE}"
```

### 3) List candidate pages in this repo
Use this to find routes quickly.

```zsh
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

```zsh
ROUTE="/research.html"
PATTERN="Ava Campbell|NSF Graduate Research Fellowship|research.gov/grfp"
curl -s "http://127.0.0.1:4000${ROUTE}" | rg -n "$PATTERN"
```

## Stop Server
In the terminal running Jekyll, press `Ctrl+C`.

## Notes
- Always run `ruby -v` through `rbenv exec` for this site. Homebrew Ruby 4.x
  resolves `github-pages` to obsolete versions and causes native gem failures
  such as `posix-spawn` or `yajl-ruby`.
- If `bundle exec` fails because of Ruby/Bundler mismatch, use `rbenv exec` as shown above.
- Do not edit generated output inside `_site/`.
