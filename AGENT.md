# AGENT.md

## Purpose

This repository is the static GitHub Pages website for Dan Shim Lab. Treat it as
a design-sensitive academic website, not a generic template site.

The site should communicate:

- planetary science
- high-pressure materials research
- a polished but restrained space aesthetic
- clarity and readability over visual gimmicks

## Core rules

- Do not make visual or structural changes to `index.html` unless the user explicitly asks.
- Use `styles.css` as the shared source of truth for site-wide styling.
- Keep the homepage and the interior pages visually distinct.
- Preserve the current non-home visual direction: dark, space-themed, subdued, readable.
- Avoid introducing bright neon colors, loud gradients, or “sci-fi UI” styling.
- Prefer small, controlled changes over large redesigns.

## Page model

- `index.html` is a special-case landing page and should remain isolated from interior-page theme work.
- All other pages use the shared non-home styling branch via `body:not(.home-page)` in `styles.css`.
- When changing the interior-page theme, scope changes so they do not affect the homepage.

## Design language

### Non-home pages

- Background uses `assets/images/background.png` with a single-tone dark overlay.
- The tone should feel like deep space, but not overly blue.
- Theme colors should stay muted:
  - dark charcoal/slate panels
  - warm off-white text
  - restrained sand/gold accents
- Maintain strong readability and contrast for body text.

### Header / top nav

- Interior-page top nav has a subtle starfield treatment.
- Stars should be soft, dim, and natural-looking, not sharp bright dots.
- A faint nebula/fog effect exists on the right side of the top bar.
- Keep the nav refined and understated.

### Cards and sections

- Use soft glass/dark-panel surfaces with thin light borders.
- Borders should be subtle and consistent across sections.
- Avoid heavy outlines or thick separators.

## Images

### General hero images

- Hero images on interior pages should use a thin light boundary line.
- The line should be visible but restrained.
- Rounded corners should be consistent with surrounding panel styling.

### People page collage

- The Lab community collage is wrapped in `.people-collage-frame`.
- Keep the frame responsible for the visible outer edge.
- The image itself should fill the frame edge-to-edge with rounded clipping.
- If black gaps or padding appear around the collage, fix the frame/image fit first.
- If the problem is baked into the asset, crop or replace the image asset instead of layering more CSS hacks.

### Dan Shim portrait

- The portrait in `dan-shim.html` should use a thin light circular boundary, not a heavy glowing ring.
- Keep it visually aligned with the thin-edge treatment used elsewhere on the site.

## Content and layout guidance

- Preserve the current multi-page static HTML structure.
- Do not introduce a framework unless explicitly requested.
- Prefer semantic HTML and simple maintainable CSS.
- Keep navigation labels and section structure stable unless the user requests content changes.
- Academic content should feel professional and direct, not promotional.

## Editing guidance

- When changing visuals for interior pages, inspect whether the selector also affects `index.html`.
- Before changing shared image styles, check which pages reuse the class.
- If a user asks for “same styling as another page,” reuse the shared class where possible.
- When updating design, prefer adjusting shared tokens and shared classes before page-specific overrides.

## Cache-busting

- If a CSS change is significant and pages use versioned stylesheet query strings, update the non-home pages consistently.
- Do not change the homepage stylesheet version unless the homepage itself needs the new CSS.

## What to avoid

- Do not convert the site into a generic SaaS-style layout.
- Do not add purple-heavy space themes.
- Do not use overly bright cyan accents.
- Do not add animations by default.
- Do not make the interior theme lighter unless explicitly asked.
- Do not “fix” the homepage while working on interior pages.

## Preferred workflow

1. Identify whether the request affects `index.html`, interior pages, or both.
2. Inspect shared selectors in `styles.css` before editing.
3. Keep non-home theme changes inside `body:not(.home-page)` when possible.
4. Reuse existing patterns for borders, hero images, frames, and section cards.
5. If an image-edge issue persists, verify whether the asset itself is the problem before adding more CSS.

## Files of interest

- `index.html`: homepage, preserve unless explicitly asked
- `dan-shim.html`: PI landing page
- `people.html`: lab community and roster
- `research.html`: research overview
- `publications.html`: publication list
- `resources.html`: resources and tools
- `styles.css`: shared styling system
- `assets/images/background.png`: interior-page background

## Success criteria

A good change in this repo should:

- preserve the homepage unless requested
- make interior pages feel cohesive
- keep the planetary/space atmosphere subtle and academic
- improve visual consistency across images, borders, and panels
- remain simple to maintain in plain HTML/CSS
