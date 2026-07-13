# publications/

## Purpose

Where real, written, reviewed enaasan content actually lives — as distinct from `templates/` (blank structure) and `standards/` (acceptance rules). This folder is intentionally empty of content today; it's a set of prepared containers, organised by audience, ready to receive real publications as they're written.

## Contents

> **Amended per KA-1.0 (`architecture/knowledge-architecture-1.0.md`, amendment A3):** this folder now has two kinds of subfolders. **Domain folders** hold Knowledge Cards and domain-natural publications (filed by what they're about). **Audience folders** remain valid for genuinely audience-targeted publications (workbooks, letters written *for* someone). No existing file moves.

**Domain folders (Knowledge Cards + domain-natural publications):**

| Folder | KA-1.0 Domain — Document ID DOMAIN code |
|---|---|
| `pathways/` | Education routes: streams, courses, exams, institutions — `PATH` *(created when first content lands)* |
| `careers/` | The world of work: profiles, sectors, salaries, ladders — `CAREER` |
| `skills/` | Transferable capabilities — `SKILL` *(first real content: `skills/communication/`)* |
| `deciding/` | Frameworks, comparisons, traps, self-assessment — `DECIDE` *(created when first content lands)* |
| `mindset/` | Pressure, family, wellbeing, confidence — `MIND` *(created when first content lands)* |

**Audience folders (audience-targeted publications):**

| Folder | Audience (matches `architecture/document-id-standard.md` AUDIENCE codes) |
|---|---|
| `graduates/` | Recent graduates / final-year students — `GRAD` |
| `schools/` | Class 10–12 students — `SCHOOL10` / `SCHOOL12` |
| `parents/` | Parents, guardians, teachers, counsellors — `PARENT` |
| `workplace/` | Early-career / workplace-readiness content — `WORK` |

*(`careers/` serves double duty: it was an audience folder and is also the Careers domain folder — the two uses coincide naturally for career-exploration content.)*

## Naming Convention

Each folder holds one subfolder per publication or card series, named after the slug (matching the slug portion of its Document ID), containing that content's Markdown source and any supporting files.

## Rules

1. **Knowledge Cards** live in the domain folder matching their `domain:` metadata field and their Document ID's DOMAIN code — the two must agree.
2. **Audience-targeted publications** live in the folder matching their primary audience and their Document ID's AUDIENCE code — the two must agree.
3. Nothing is added here without a Document ID, complete metadata, and a source template followed, per `architecture/` and `templates/`.
4. This folder is where the real work happens — everything else in `knowledge/` exists to make what lands here consistent, honest, and reusable.

## Examples

- A new Career Profile for "Business Analyst" lands at `publications/careers/business-analyst/source.md`, following `templates/career-profile-template.md`.
- A future formal onboarding of the existing 90-Day Career Clarity Plan into this system would land at `publications/graduates/90-day-career-clarity-plan/source.md` — as a record that *references* the existing PDF and its content, not a duplicate rewrite forced into being on day one.

## Future Expansion

- Subfolders here will grow organically as real publications are written. No further structure is imposed until there's enough real content to show what additional organisation (by exam, by stream, by industry) would actually help.
