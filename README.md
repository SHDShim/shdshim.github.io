# Dan Shim Lab Website

This repository hosts the GitHub Pages version of the lab website at
`https://shdshim.github.io/`, with content migration underway from
`https://www.danshimlab.info/`.

## Current structure

This site is now configured for Jekyll so page content can be managed with
Markdown front matter and shared layouts.

- `_config.yml`: Jekyll site configuration
- `_layouts/`: shared page layouts (`default.html`, `home.html`)
- `_includes/`: reusable head and primary navigation includes
- `index.md`, `dan-shim.md`, `dan-shim-cv.md`, `dan-shim-teaching.md`, `dan-shim-talks.md`, `people.md`, `research.md`, `publications.md`, `resources.md`: page templates (Liquid + layout structure)
- `_data/home.yml`: homepage text/content data
- `_data/dan_shim.yml`: PI overview/CV/teaching/talks content data
- `_data/people.yml`: people page content data
- `_data/research.yml`: research page content data
- `_data/publications.yml`: publication periods and entries
- `_data/resources.yml`: resources page content data
- `styles.css`: shared site styling

## Local development (Jekyll)

1. Install dependencies:
   - `bundle install`
2. Serve the site locally:
   - `bundle exec jekyll serve`
3. Open:
   - `http://127.0.0.1:4000`

## Content maintenance

- For routine content updates, edit `_data/*.yml` instead of page templates.
- `index.md` reads from `_data/home.yml`.
- `dan-shim*.md` pages read from `_data/dan_shim.yml`.
- `people.md` reads from `_data/people.yml`.
- `research.md` reads from `_data/research.yml`.
- `publications.md` reads from `_data/publications.yml`.
- `resources.md` reads from `_data/resources.yml`.

## Preserved old site

The earlier site histories were preserved locally before the reset:

- `archive-dev-2026-03-28`
- `archive-master-2026-03-28`

## Migration approach

The current implementation is a migration from the Google Site into a
maintainable multi-page structure. The next upgrades should be:

- migrate the full people roster
- migrate publication entries with DOI links
- migrate public resources and teaching materials
- add real images, figures, and profile photos
- leave members-only material in authenticated systems
