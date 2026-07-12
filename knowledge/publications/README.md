# publications/

## Purpose

Where real, written, reviewed enaasan content actually lives — as distinct from `templates/` (blank structure) and `standards/` (acceptance rules). This folder is intentionally empty of content today; it's a set of prepared containers, organised by audience, ready to receive real publications as they're written.

## Contents

| Folder | Audience (matches `architecture/document-id-standard.md` AUDIENCE codes) |
|---|---|
| `graduates/` | Recent graduates / final-year students — `GRAD` |
| `schools/` | Class 10–12 students — `SCHOOL10` / `SCHOOL12` |
| `parents/` | Parents, guardians, teachers, counsellors — `PARENT` |
| `careers/` | General career-exploration content, Career Profiles, Roadmaps — `CAREER` |
| `workplace/` | Early-career / workplace-readiness content — `WORK` |

## Naming Convention

Each audience folder holds one subfolder per publication, named after the publication's slug (matching the slug portion of its Document ID), containing that publication's Markdown source and any publication-specific supporting files.

## Rules

1. A publication lives in the folder matching its `audience` metadata field and its Document ID's AUDIENCE code — the two must agree.
2. Nothing is added here without a Document ID, complete metadata, and a source template followed, per `architecture/` and `templates/`.
3. This folder is where the real work happens — everything else in `knowledge/` exists to make what lands here consistent, honest, and reusable.

## Examples

- A new Career Profile for "Business Analyst" lands at `publications/careers/business-analyst/source.md`, following `templates/career-profile-template.md`.
- A future formal onboarding of the existing 90-Day Career Clarity Plan into this system would land at `publications/graduates/90-day-career-clarity-plan/source.md` — as a record that *references* the existing PDF and its content, not a duplicate rewrite forced into being on day one.

## Future Expansion

- Subfolders here will grow organically as real publications are written. No further structure is imposed until there's enough real content to show what additional organisation (by exam, by stream, by industry) would actually help.
