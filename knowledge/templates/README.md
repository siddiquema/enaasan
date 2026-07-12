# templates/

## Purpose

Blank, ready-to-copy skeletons for every publication type enaasan produces. Starting a new publication means copying the matching template here and filling it in — not improvising a new structure from scratch each time.

## Contents

| File | Type code | For |
|---|---|---|
| `guide-template.md` | `GUIDE` / `REFGUIDE` | A plain-read explanatory document (also used, with notes, for Reference Guides) |
| `workbook-template.md` | `WORKBOOK` | A structured, worksheet-driven plan (like the existing 90-Day Career Clarity Plan) |
| `playbook-template.md` | `PLAYBOOK` | A scenario/decision-driven "if this, then that" document |
| `checklist-template.md` | `CHECKLIST` | A short, standalone checklist |
| `faq-template.md` | `FAQ` | A collection of question/answer pairs on one theme |
| `career-profile-template.md` | `PROFILE` / `ROADMAP` | A single career's profile (also used, with notes, for multi-stage Career Roadmaps) |
| `learning-path-template.md` | `LPATH` | A sequenced set of documents/cards toward a goal |
| `knowledge-card-template.md` | `KCARD` | A single atomic, reusable knowledge unit |
| `metadata-template.md` | *(all types)* | The blank metadata block, ready to paste at the top of any new document |

## Naming Convention

`<type>-template.md`, matching the TYPE codes in `architecture/document-id-standard.md` exactly.

## Rules

1. Templates contain **structure only** — headings, bracketed placeholders, and instructional comments. They must never contain real, ready-to-publish enaasan content. If you find yourself writing a real answer into a template file, stop — that content belongs in `publications/`, using a *copy* of the template.
2. Every template starts with the block from `metadata-template.md` (referenced, not duplicated by value, so a change to the metadata standard doesn't require editing nine template files).
3. A template's placeholder text is written as `[bracketed instructions]`, not as filled-in example prose — this keeps templates from being mistaken for finished content at a glance.
4. If a new publication type is needed that doesn't fit an existing template, add both the template here and its TYPE code in `architecture/document-id-standard.md` in the same change.

## Examples

- Starting a new Career Profile for "Business Analyst": copy `career-profile-template.md` into `publications/careers/`, rename the file to the new document's slug, fill in the metadata block per `architecture/metadata-standard.md`, and replace every bracketed placeholder with real content.

## Future Expansion

- Additional templates likely as the site's content roadmap plays out: a Comparison Page template (see `docs/website-update-spec.md` §12) and a Glossary-entry template (distinct from the whole-glossary document, which is described in `standards/glossary-standard.md`) are the two most likely next additions.
