# Metadata Standard

Every publication in `knowledge/publications/`, regardless of type, carries this metadata block as YAML front matter at the top of its Markdown source. No publication is considered complete without it.

## The block

```yaml
---
document_id: ENA-<TYPE>-<AUDIENCE>-<slug>-v<major>.<minor>
title: "[Full title as it should appear to a reader]"
subtitle: "[Optional one-line subtitle — omit the key entirely if unused]"
version: <major>.<minor>
status: Draft | In Review | Published | Under Revision | Retired
author: "[Person or team responsible for the content]"
audience: Graduates | Schools (10th) | Schools (12th) | Parents | Careers | Workplace | All
reading_level: "[Plain-language description, not a grade number — see below]"
estimated_reading_time: "[e.g. 8 minutes — omit for interactive/workbook types, use estimated_completion_time instead]"
estimated_completion_time: "[e.g. 2 hours across 1 week — for workbooks, checklists, learning paths]"
difficulty: Not applicable | Beginner | Intermediate | Advanced
tags: [kebab-case, free-text, tags]
prerequisites: ["ENA-... document IDs, or 'None'"]
related_documents: ["ENA-... document IDs"]
related_careers: ["Career names, free text for now — see architecture/README.md Future Expansion"]
related_skills: ["Skill names, free text for now"]
last_reviewed: "YYYY-MM-DD"
review_due: "YYYY-MM-DD"
license: "Free to read, download, and share for personal and educational use. Not for resale or republishing without permission. © enaasan.online"
---
```

A ready-to-copy blank version lives at `templates/metadata-template.md`.

## Field-by-field rules

- **`document_id`** — assigned once, per `document-id-standard.md`. Never changes across versions of the same document; only the `-v<major>.<minor>` suffix updates as `version` changes.
- **`title` / `subtitle`** — reader-facing. Not the same as the document ID's slug, which is a short machine-friendly stand-in.
- **`version`** — must exactly match the version embedded in `document_id`. See `versioning-standard.md` for what counts as a major vs. minor change.
- **`status`** —
  - `Draft`: being written, version is 0.x
  - `In Review`: complete draft, awaiting the review described in `standards/publication-standard.md`
  - `Published`: reviewed and live somewhere (as a PDF, on the site, etc.)
  - `Under Revision`: a published document currently being updated — the old version stays available until the new one replaces it
  - `Retired`: no longer maintained; the document should say what (if anything) replaces it
- **`author`** — a name or role, not "AI" alone. Per enaasan's existing public commitment (see `about.html`'s transparency section), AI may assist drafting, but a named human is responsible for what's published — that applies here identically.
- **`audience`** — pick exactly one primary audience. If content genuinely serves two, that's usually a sign it should be two documents, or an `All`-audience document with audience-specific sections called out inline.
- **`reading_level`** — a plain description (e.g. "Plain English — no prior subject knowledge assumed"), not a Flesch-Kincaid score. See `branding/writing-style.md` for what "plain English" means here.
- **`estimated_reading_time` / `estimated_completion_time`** — use reading time for things meant to be read straight through (Guides, Reference Guides, Knowledge Cards); use completion time for things with tasks/worksheets (Workbooks, Checklists, Learning Paths). A document normally has one or the other, not both.
- **`difficulty`** — only meaningful where a reader is building a skill or working through a structured task. A plain informational Guide is usually `Not applicable`.
- **`tags`** — free-text for now (see `architecture/README.md`'s Future Expansion note on a controlled taxonomy).
- **`prerequisites`** — other documents a reader should ideally have read first. Use `"None"` explicitly rather than an empty list, so it's clear the field wasn't just forgotten.
- **`related_documents` / `related_careers` / `related_skills`** — the cross-linking that makes the knowledge layer a web rather than a pile. Keep these accurate as documents are added or retired — a related-document reference to a retired document should be updated to point at its replacement, if any.
- **`last_reviewed` / `review_due`** — every substantive publication gets a review cadence, matching the spirit of the site's existing "Last reviewed" commitment for high-stakes content (`docs/website-update-spec.md` §5–§6). `review_due` is normally 12 months after `last_reviewed` for stable content, and 3–6 months for anything referencing exam dates, fees, cut-offs, or other volatile facts.
- **`license`** — the default text above applies unless a specific publication needs different terms (state so explicitly if it does).
