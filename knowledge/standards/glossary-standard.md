# Glossary Standard

Defines what a Glossary document is, and how it differs from a Knowledge Card — the two are easy to conflate, so the distinction matters.

## Glossary vs. Knowledge Card

- A **Glossary** is one document containing many short term-definitions, organised as a single reference list (this matches `docs/website-update-spec.md` §13's original concept — CUET, credit system, lateral entry, internship, and so on, all in one document).
- A **Knowledge Card** (see `knowledge-card-standard.md`) is an individually versioned, individually addressable document — richer, with its own metadata, relationships, and review cycle — that may cover a term but isn't limited to one.
- In practice: a term that's referenced from many different other documents and benefits from its own metadata/version history is a good candidate to graduate from a Glossary entry into a full Knowledge Card. A term that's simple, stable, and mainly needs a quick one-line lookup can stay a Glossary entry.

## Requirements for a Glossary document

- [ ] Entries are genuinely concise — a Glossary entry is shorter than a Knowledge Card's one-line definition plus expanded explanation combined; if an entry needs that much space, it should be a Knowledge Card instead, linked from the Glossary rather than fully explained in it.
- [ ] Entries are alphabetised or otherwise consistently ordered (by category, if the glossary is large enough to need grouping) — a reader should be able to scan and find a term quickly.
- [ ] Each entry uses plain language per `branding/writing-style.md` — a glossary defining jargon with more jargon has failed its purpose.
- [ ] Where a fuller explanation exists elsewhere (a Knowledge Card, a Guide section), the Glossary entry links to it rather than duplicating that content.
- [ ] Terms are genuinely ones a reader would plausibly not know — don't pad a glossary with terms that don't need defining for the target audience.

## Format

```markdown
**[Term]** — [One-sentence, plain-language definition]. [Optional: link to a fuller Knowledge Card or Guide section for more depth.]
```

## Maintenance

- A Glossary is reviewed as a whole document on its `review_due` cycle (per `architecture/metadata-standard.md`), but individual entries should also be corrected immediately if a term changes meaning or naming (an exam gets renamed, for instance) rather than waiting for the scheduled review.
