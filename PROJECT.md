# N4M 2027 website project state

## Purpose
This repository contains the 2027 edition of the N4M conference website. The site is a static, data-driven website: content is stored in `2027/content.json`, and the generated HTML files are written by `2027/build.py`.

## Current status
The 2027 site is in a clean public state. The old preview-only `_tmp` pattern has been retired, and the generator creates the standard public pages directly:

- `2027/index.html`
- `2027/overview.html`
- `2027/venue.html`
- `2027/speakers.html`
- `2027/sponsors.html`
- `2027/program.html`
- `2027/registration.html`

The home page is no longer a teaser page; it is the main landing page for the event.

## Key files
- `2027/content.json` — source of truth for conference metadata, organisers, speaker list, overview sessions, and sponsor data.
- `2027/build.py` — generator for all pages; this is the authority for the 2027 edition.
- `2027/theme.css` — all custom styling, including card layout, sponsor presentation, and responsive spacing.
- `2027/index.html` — main public home page.
- `2027/sponsors.html` — sponsor landing page with gold/silver/bronze sections and sponsor detail cards.

## Working convention
- Edit the source files, not the generated HTML, unless a rebuild is intentionally being tested.
- Treat `2027/content.json` and `2027/build.py` as the persistent source of truth.
- Regenerate the site with:

  python 2027/build.py

## Current design decisions captured
- The home page includes the sponsor rail in the top navigation and side sponsor column, but no quick sponsor link under the title.
- The sponsor cards on the dedicated sponsors page behave as a landing page: each logo points to the sponsor page, while the external website is only opened from the sponsor detail card.
- The gold sponsor is not repeated as a floating header banner on the sponsors page to avoid redundancy.
- The organiser cards use the same visual system as the speaker cards for consistency.
- Sponsor entries are represented in `content.json` with fields such as `name`, `level`, `logo`, `description`, and `website`.

## Content workflow for the next person
1. Open `2027/content.json` to update the conference data.
2. Add or replace sponsor entries by editing the `sponsors` array.
3. Add or update speaker entries in the `speakers` array.
4. Update the overview session data in the `overview.sessions` section if required.
5. Update the organiser and institutional supporter data as needed.
6. Run:

   python 2027/build.py

7. Check the generated `2027/*.html` files and the CSS result.

## Known placeholder state
The site is intentionally structured so that placeholders can be replaced one by one as confirmations arrive. The current sponsor list remains partly placeholder-based until the remaining sponsor logos, descriptions, and URLs are confirmed.

## Useful project context
- This is a static website; there is no backend or database.
- The pages are generated locally into the same `2027` folder.
- CSS is custom and lives in `2027/theme.css`; Bootstrap is used only as a base layer from the root CSS assets.
- The repo uses a simple generator-driven workflow rather than a front-end framework.

## Immediate next actions
- Replace remaining sponsor placeholders with confirmed logos and text.
- Finalise any remaining page copy and visual polish for the public release.
- Commit and push once the 2027 edition is approved for publication.
