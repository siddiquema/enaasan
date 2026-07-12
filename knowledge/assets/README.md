# assets/

## Purpose

Shared visual assets — logos, diagrams, illustrations, icons — used across knowledge-layer publications, kept separate from the website's own `assets/` folder (which holds `og-image.jpg` and the compiled `enaasan-90-day-career-clarity-plan.pdf`) so that source visual assets for authoring don't get confused with the website's own delivery assets.

## Contents

| Folder | Holds |
|---|---|
| `logos/` | Logo lockups and wordmark variants for use in publication covers/headers |
| `diagrams/` | Reusable diagrams (decision trees, process flows) referenced across multiple publications |
| `illustrations/` | Illustration assets, once an illustration style is established (see `branding/visual-language.md`) |
| `icons/` | Icon assets for use in Checklists, Knowledge Cards, and similar structured content |

All four subfolders are currently empty (each holds only a `.gitkeep` placeholder) — no visual assets have been created for this layer yet.

## Naming Convention

Asset filenames: lowercase, hyphen-separated, descriptive (`enaasan-wordmark-gold-on-dark.svg`, not `logo2-final-FINAL.svg`).

## Rules

1. Assets here follow `branding/visual-language.md` exactly — colour values, typography choices, and (for anything used on a printable cover) the print-friendliness rule.
2. A publication references an asset by a stable filename under this folder rather than embedding an absolute path or a copy of the asset inline (see `publishing/markdown-standard.md`'s rule against embedded absolute paths).
3. Don't duplicate an asset that already exists on the live site (`favicon.svg`, `assets/og-image.jpg`) — reference or adapt from those where the use case genuinely overlaps, rather than creating a second, slightly different logo file here.

## Examples

- A future Career Profile needing a simple "growth path" diagram (entry role → next role → senior role) would have that diagram created once under `diagrams/` and referenced from every Career Profile that needs the same visual pattern, rather than each profile getting a bespoke one-off graphic.

## Future Expansion

- This folder stays empty until `branding/visual-language.md`'s illustration style is actually defined with real assets — a deliberate, separate future task, not something to populate speculatively now.
