# Document ID Standard

Every publication gets exactly one Document ID, assigned when it's created, kept for the document's entire life (including all future versions and even after retirement).

> **Amended per KA-1.0 (`knowledge-architecture-1.0.md`, amendment A2):** the third ID segment is an **AUDIENCE code for audience-targeted publications** but a **DOMAIN code for Knowledge Cards** (`KCARD`). Rationale: audience is a facet and facets change over a card's life; an ID must never change. A card's domain is its one permanent, canonical home, so it belongs in the identity.

## Format

```
Audience-targeted publications:  ENA-<TYPE>-<AUDIENCE>-<slug>-v<major>.<minor>
Knowledge Cards (TYPE = KCARD):  ENA-KCARD-<DOMAIN>-<slug>-v<major>.<minor>
```

## TYPE codes

| Code | Publication type | Template |
|---|---|---|
| `GUIDE` | Guide | `templates/guide-template.md` |
| `WORKBOOK` | Workbook | `templates/workbook-template.md` |
| `PLAYBOOK` | Playbook | `templates/playbook-template.md` |
| `REFGUIDE` | Reference Guide | `templates/guide-template.md` (reference variant — see that template's notes) |
| `PROFILE` | Career Profile | `templates/career-profile-template.md` |
| `ROADMAP` | Career Roadmap | `templates/career-profile-template.md` (roadmap variant — see that template's notes) |
| `KCARD` | Knowledge Card | `templates/knowledge-card-template.md` |
| `LPATH` | Learning Path | `templates/learning-path-template.md` |
| `CHECKLIST` | Checklist | `templates/checklist-template.md` |
| `GLOSSARY` | Glossary | none yet — a glossary is one document containing many terms; see `standards/glossary-standard.md` |
| `FAQ` | FAQ collection | `templates/faq-template.md` |

If a genuinely new type is needed, add its code and template here and in `templates/README.md` in the same change — don't invent a code ad hoc inside a single document.

## AUDIENCE codes (all TYPEs except KCARD)

| Code | Meaning |
|---|---|
| `GRAD` | Recent graduates / final-year students |
| `SCHOOL10` | Class 10 students (stream choice, after-10th paths) |
| `SCHOOL12` | Class 11–12 students (entrance exams, after-12th paths) |
| `PARENT` | Parents, guardians, teachers, counsellors |
| `CAREER` | General career-exploration content, not tied to a single life stage |
| `WORK` | Early-career / workplace-readiness content |
| `ALL` | Genuinely audience-agnostic content (used sparingly — see the `audience` field note in `metadata-standard.md`) |

These map to the *primary* audience of an audience-targeted publication and, loosely, to the audience subfolders of `publications/` (`graduates/`, `schools/`, `parents/`, `careers/`, `workplace/`). Note that the `audience:` metadata field itself is multi-valued per KA-1.0 amendment A1; the ID code reflects the primary audience the publication was written for.

## DOMAIN codes (TYPE = KCARD only)

| Code | KA-1.0 Domain | The student's question |
|---|---|---|
| `PATH` | Pathways | "What can I study, and how do I get in?" |
| `CAREER` | Careers | "What work exists, and what is it really like?" |
| `SKILL` | Skills | "What capabilities do I need?" |
| `DECIDE` | Deciding | "How do I choose?" |
| `MIND` | Mindset | "How do I handle the pressure and the people?" |

For a `KCARD`, the third segment is **always** a DOMAIN code, matching the card's `domain:` metadata field exactly. (`CAREER` appears in both tables; the TYPE segment disambiguates — `ENA-PROFILE-CAREER-…` is an audience code, `ENA-KCARD-CAREER-…` is a domain code.)

**Worked example (real):** the communication salary-premium card at `publications/skills/communication/03-why-communication-commands-premium.md` is `ENA-KCARD-SKILL-communication-salary-premium-v0.1` — domain `SKILL` in the ID and it stays there even as the card's `stage` and `audience` facets grow over time.

## Slug

- Kebab-case, short, descriptive, derived from the title but not required to match it exactly.
- Stays the same across versions. If a revision changes the document's scope enough that the old slug no longer fits, that's a strong signal that it's actually a new document (new ID) with `related_documents` linking to the old one — not a renamed version of the same one.

## Version suffix

- Format `v<major>.<minor>`, exactly matching the `version` field — see `versioning-standard.md`.
- The ID string is only updated when the file itself is updated to that version; don't pre-increment the ID for a version that hasn't landed in the document yet.

## Worked example

The existing 90-Day Career Clarity Plan (`assets/enaasan-90-day-career-clarity-plan.pdf`), if formally onboarded to this layer, would be:

```
ENA-WORKBOOK-GRAD-90-day-career-clarity-plan-v1.1
```

- Type: `WORKBOOK` — it's worksheets and a tracker, not a plain-read guide.
- Audience: `GRAD` — written for graduates, per its content.
- Slug: `90-day-career-clarity-plan` — matches its existing filename stem for continuity.
- Version: `v1.1` — matches the filename convention already used for the source PDF the user provided (`enaasan-90-day-career-clarity-plan-v1.1.pdf`).

## Rules

1. IDs are never reused, even after a document is retired.
2. IDs are never renumbered to close gaps or reorder documents.
3. A Document ID is assigned once a publication reaches Draft status in `publications/`, not before — templates and standards themselves don't get Document IDs, since they aren't publications.
