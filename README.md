# Dan Shim Lab Website

This repository now hosts the static GitHub Pages version of the lab website at
`https://shdshim.github.io/`, with content migration underway from
`https://www.danshimlab.info/`.

## Current structure

- `index.html`: homepage
- `dan-shim.html`: PI profile
- `people.html`: lab people page
- `research.html`: research themes and methods
- `publications.html`: publication page scaffold
- `resources.html`: migration strategy for public and private resources
- `opportunities.html`: current opportunity posting
- `styles.css`: shared site styling
- `.nojekyll`: serves the site as plain static files on GitHub Pages

## Preserved old site

The earlier site histories were preserved locally before the reset:

- `archive-dev-2026-03-28`
- `archive-master-2026-03-28`

## Migration approach

The current implementation is a first-pass migration from the Google Site into a
maintainable static multi-page structure. The next upgrades should be:

- migrate the full people roster
- migrate publication entries with DOI links
- migrate public resources and teaching materials
- add real images, figures, and profile photos
- leave members-only material in authenticated systems
