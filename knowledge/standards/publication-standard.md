# Publication Standard

The requirements every publication must meet, regardless of type, before it's considered `Published` per `architecture/versioning-standard.md`.

## Before starting

- [ ] The correct template from `templates/` has been copied, not improvised from scratch.
- [ ] A Document ID has been assigned per `architecture/document-id-standard.md`.

## Content requirements

- [ ] The metadata block (`architecture/metadata-standard.md`) is completely filled in — no bracketed placeholders remain.
- [ ] The content follows `branding/writing-style.md` and `branding/tone-of-voice.md` — plain language, direct answers first, trade-offs named honestly, no hype.
- [ ] Every claim about outcomes (salary, admission, employment) is either sourced and dated, or explicitly framed as indicative/estimated with the standard disclaimer language (see `templates/career-profile-template.md`'s salary disclaimer as the reference pattern).
- [ ] Any volatile fact (fees, cut-offs, exam dates, eligibility criteria) carries a verification note pointing to the official source, per the pattern already established on `state-exams.html` and in `docs/website-update-spec.md` §6.
- [ ] The document doesn't end on a dead end — it points somewhere next (a related document, an action, a decision), per `docs/website-update-spec.md` §11's related-content principle.
- [ ] `related_documents`, `related_careers`, and `related_skills` metadata fields are populated where genuinely applicable, not left empty by default.

## Review process

1. **Self-review against this checklist** by the author.
2. **Independent review** by at least one other person, checking specifically for: factual accuracy, tone/voice fit, and whether trade-offs are honestly represented (not just whether the writing is polished).
3. Status moves `Draft` → `In Review` when the author believes it's ready for independent review, and → `Published` once that review is satisfied.
4. A **major** version change (per `architecture/versioning-standard.md`) goes through this full process again. A **minor** version change does not require step 2, but the author should still re-check the content requirements above.

## Print-conscious design

- [ ] If the publication will plausibly be printed (Workbooks, Checklists especially), its cover/first page follows the print-friendliness rule in `branding/visual-language.md` — no full-bleed dark background.

## Ongoing maintenance

- [ ] `review_due` is set on every publication and honoured — when that date arrives, the document is re-checked against this standard, even if no specific problem has been reported.
- [ ] A `Retired` document has its `related_documents` (and any document that referenced it) updated to reflect what, if anything, replaces it.

## What this standard does not cover

- Type-specific requirements (what makes a good Knowledge Card, Checklist, Learning Path, or Glossary specifically) — see the other files in this folder.
- Format-specific rendering requirements (PDF, DOCX) — see `publishing/`.
