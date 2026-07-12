# Knowledge Architecture

## What this layer is for

Enaasan produces two different kinds of things:

1. **The website** — HTML pages, i18n strings, CSS, the accordion on `faq.html`, the schema markup, the GitHub Pages deployment. This is presentation and delivery. It's documented in `docs/` (see `docs/project-structure.md`).
2. **The knowledge** — the actual guidance: what to tell a Class 10 student choosing a stream, what the 90-Day Career Clarity Plan says to do in week 4, what a Career Profile for a KPO analyst looks like. This is substance. It's authored, reviewed, and versioned in `knowledge/`.

Before this layer existed, substance was written directly into HTML/JSON files (`faq.html`, `locales/en.json`, the PDF-generation script for the 90-Day Plan) with no separate source of truth, no metadata, no versioning beyond git history, and no standard shape from one piece of content to the next. That worked at small scale. This layer exists so it keeps working as the number of publications grows — comparison pages, career profiles, a glossary, learning paths (see `docs/website-update-spec.md` Phase 2) — without every one of them reinventing its own structure.

## How the pieces fit together

```
architecture/   →  defines HOW content is identified and described (IDs, metadata, versions)
branding/       →  defines HOW content sounds and looks (voice, tone, visual language)
templates/      →  blank skeletons that already follow architecture/ + branding/ rules
standards/      →  the acceptance bar each publication TYPE must meet before being "done"
publications/   →  where real, written, reviewed content actually lives, by audience
publishing/     →  how one publications/ source becomes PDF / DOCX / Google Doc / HTML
output/         →  where the compiled artifacts from publishing/ land
assets/         →  shared visual assets used across publications
```

A publication's life cycle: pick the right `templates/` file → follow the matching `standards/` file → fill in `architecture/metadata-standard.md` fields → write it in `publications/<audience>/` → (later, separately) render it via `publishing/` into `output/`.

## Relationship to existing content

Two real publications already exist and predate this layer:

- **`assets/enaasan-90-day-career-clarity-plan.pdf`** — this is, structurally, a **Workbook** (see `templates/workbook-template.md`). It is not moved or renamed by creating this layer. A future task could give it a formal Document ID and metadata record under `publications/graduates/` that *points to* the existing file, rather than duplicating it.
- **`faq.html`'s 32 Q&As** — structurally, these map closely to the **FAQ template** and, at the individual question level, to **Knowledge Cards** (see `standards/knowledge-card-standard.md`). Same principle: adopting this layer doesn't mean rewriting or moving what's already live.

Retrofitting existing content into this architecture (giving it Document IDs, metadata, etc.) is a distinct future task, not something this layer's creation does automatically.

## What this layer deliberately does not do

- It does not build, render, or deploy anything. `publishing/` describes a *conceptual* pipeline — no scripts exist yet.
- It does not contain real publications yet. `templates/` and `standards/` are structure; `publications/` subfolders are currently empty containers with only a README each.
- It does not change how the website's own i18n system (`js/i18n.js`, `locales/*.json`) works. Long-form knowledge content and short UI strings are different problems with different lifecycles — seeing them as one system would be a mistake. See `docs/website-update-spec.md` §17 for the open question of how future long-form Telugu articles will be handled; this layer's `architecture/` will need to account for whichever answer is chosen, but does not pre-decide it.
