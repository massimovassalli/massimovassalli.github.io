# N4M 2027 website project state

## Purpose
This repository contains the static conference website for N4M 2027. The site is generated from a data file rather than a CMS, and the generated HTML files live in the 2027 folder alongside the Python build script.

## Key files
- 2027/content.json — source of truth for texts, sponsor data, speaker data, and program structure.
- 2027/build.py — Python generator that writes the HTML pages.
- 2027/theme.css — custom styling for the static pages.
- 2027/index.html — current teaser landing page for public access.
- 2027/index_tmp.html — private preview page for direct-link access.
- 2027/*.html generated pages (overview_tmp.html, venue_tmp.html, speakers_tmp.html, program_tmp.html, registration_tmp.html) — direct-link preview pages.

## Current layout behavior
- Public teaser page is at 2027/index.html.
- Full private preview pages are created as *_tmp.html files.
- The direct-link preview pages use the full website structure and keep private navigation pointing to the *_tmp pages.
- The gold sponsor banner is displayed in the page header for overview, venue, speakers, and programme.
- The home page remains a teaser-style landing page and is not the full site.

## Build command
Run from the repository root:

python 2027/build.py

## Notes and conventions
- Treat 2027/content.json as the main content source.
- Do not manually edit the generated HTML files if the intent is to keep the generator authoritative.
- If making layout changes, adjust build.py and theme.css rather than editing generated HTML directly.
- The site is static; no server-side framework or database is used.

## Important decisions captured from recent work
- The gold sponsor sits in the title/header region on non-home pages and is separated from the content body to avoid layout compression.
- The programme page has the same header treatment as venue/speakers.
- Overview keeps the same pattern and is not treated as a special case.
- The temporary public/private split is intended for invitation-only previewing before the full site is published.

## Useful context for restarting
- This was built as a data-driven static site, not a React/Vite app.
- The site uses Bootstrap CSS from the root css folder and custom styling from 2027/theme.css.
- The generator writes HTML in the same folder as the source.
