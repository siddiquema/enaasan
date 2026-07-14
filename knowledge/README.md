# Enaasan Knowledge Layer

## Purpose

This is the single source of truth for every substantive piece of guidance enaasan produces — the actual written knowledge (guides, workbooks, career profiles, checklists, glossaries), the standards that keep it consistent, and the brand/voice rules that make it recognisably enaasan regardless of which page, PDF, or platform it eventually appears on.

It exists separately from the live website (`index.html`, `after10.html`, `faq.html`, etc.) and from `docs/` (which documents the *repository and engineering setup*, not the *content*). `knowledge/` is the authoring layer; the website is one of several possible delivery formats for what gets authored here.

**This folder does not affect the live site.** Nothing here is linked from, built into, or deployed as part of `enaasan.online`. It is documentation and standards only — no build system, no framework, no website changes.

## Contents

| Folder | What it holds |
|---|---|
| `architecture/` | How the knowledge layer itself is structured — metadata, document IDs, versioning |
| `eos/` | Enaasan Operating System specifications v1.0 (frozen): EOS-001–004, the object model, metadata contract, relationship model |
| `ops/` | Operational Standards: editorial workflow (OPS-001), sprint logs, reuse registry |
| `governance/` | Governance policies defining how Enaasan operates — research standards, IP policy, change log |
| `standards/` | Editorial calibration rules and domain-specific standards |
| `templates/` | Blank skeletons for every publication type — copy, don't improvise a new structure |
| `branding/` | Mission, voice, tone, writing style, visual language |
| `publishing/` | How one Markdown source becomes PDF / DOCX / Google Doc / HTML / website page |
| `publications/` | Where real content eventually lives, organised by domain |
| `assets/` | Logos, diagrams, illustrations, icons used across publications |
| `output/` | Reserved for compiled/rendered artifacts (PDF, DOCX, EPUB, HTML) — build products, not source |

## Naming Convention

- All folder and file names: lowercase, hyphen-separated (`kebab-case`) — matches the convention already used in `docs/`.
- Standards and templates are named `<thing>-standard.md` and `<thing>-template.md` respectively — never mix the two in one file.
- Every folder in this layer carries its own `README.md` explaining that folder specifically; this file only orients you to the layer as a whole.

## Rules

1. Nothing in `knowledge/` is ever referenced by an HTML page, a `<script>` tag, a build step, or a GitHub Action. If a future task wants to *publish* something from here onto the live site, that is a separate, explicit task — this layer does not do it automatically.
2. Standards and templates in this layer are **structure only** — they don't contain real, ready-to-publish enaasan content. Real content lives under `publications/` once it's written, reviewed, and given a Document ID per `architecture/document-id-standard.md`.
3. Every publication, of any type, carries the metadata block defined in `architecture/metadata-standard.md`. No exceptions.
4. Brand and voice rules in `branding/` apply to everything written here — including future website copy, not just PDFs.

## Examples

- A future task "write the Career Roadmap for Data Analysts" would: read `templates/career-profile-template.md` (or a roadmap-specific template, once added), follow `standards/publication-standard.md`, fill in `architecture/metadata-standard.md` fields, write it under `publications/careers/`, and only *then* consider whether/how it gets rendered via `publishing/` into `output/` or embedded on the website.
- The existing `assets/enaasan-90-day-career-clarity-plan.pdf` and `faq.html` predate this layer. They are not retroactively moved or restructured by creating this folder — see `architecture/knowledge-architecture.md` for how they relate to it going forward.

## Future Expansion

- A `knowledge/review/` folder may be added later to track review cycles and due dates in one place, rather than only per-document metadata.
- A `knowledge/localisation/` folder may be added once the Telugu article strategy (see `docs/website-update-spec.md` §17) is decided, to hold translation-specific standards separate from the website's `data-i18n` system.
- `output/` is currently empty by design — it stays empty until the publishing pipeline described in `publishing/publishing-workflow.md` is actually implemented as a separate, explicit task.
