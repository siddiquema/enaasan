# Knowledge Card Standard

**Do not create any actual cards from this file.** This defines the standard; real cards are written under `publications/` using `templates/knowledge-card-template.md`, and the one example below is explicitly illustrative only.

## Purpose

A Knowledge Card is the smallest independently reusable unit of enaasan knowledge — a single term or concept, written once, referenced from many places (a Glossary, an FAQ answer, a Guide, a Career Profile) without being rewritten each time it comes up. Where a Glossary (see `glossary-standard.md`) is one document containing many short definitions, a Knowledge Card is an individually versioned, individually addressable document in its own right — richer, with its own metadata and relationships, and not necessarily limited to defining a single word (a card can cover a short concept or process, e.g. "how CUET counselling rounds work," not only a term like "CUET" itself).

## Fields

Per `templates/knowledge-card-template.md`:

1. **One-line definition** — ≤25 words, must be understandable with zero other context.
2. **Expanded explanation** — ≤150 words, enough for genuine understanding, not just recognition.
3. **Why it matters** — the practical stakes, tied to a real decision or situation a reader faces.
4. **Related** — cards, documents, careers (the relationship layer — see below).
5. **Source** — where applicable (a fact/definition from an official body); omitted for general concepts that don't need external sourcing.

## Metadata

Uses the full standard block from `architecture/metadata-standard.md`. For Knowledge Cards specifically:

- `estimated_reading_time` should almost always be well under a minute — if it's creeping toward several minutes, the content has likely outgrown the Knowledge Card format and should be a Guide instead.
- `difficulty` is usually `Not applicable` unless the concept genuinely has prerequisite complexity.

## Relationships

Knowledge Cards are meant to interlink:

- **Card → Card:** a prerequisite or closely related concept (e.g. a card on "lateral entry" might relate to a card on "diploma").
- **Card → Document:** any Guide, FAQ, or Career Profile where the concept is discussed in more depth or applied context.
- **Card → Career:** where the concept is specifically relevant to understanding a particular career path.

Keep these links current — if a related card is retired, update the reference rather than leaving a dead pointer.

## Naming Convention

Document ID uses type `KCARD`; slug is the concept name in kebab-case (e.g. `cuet`, `lateral-entry`, `how-cuet-counselling-rounds-work`).

## Versioning

Follows `architecture/versioning-standard.md` generally. In practice, most Knowledge Card updates are minor (a definition gets clearer, a source link is refreshed); a major bump is rare and would mean the underlying concept itself is being redefined or substantially expanded in scope.

## Lifecycle

Same `Draft → In Review → Published → Under Revision/Retired` flow as any publication (`architecture/versioning-standard.md`), but Knowledge Cards are reviewed more frequently for factual currency than other types, since they're often the first place a changed fact (a renamed exam, a shifted eligibility rule) needs correcting — and the place that correction then propagates from, wherever the card is referenced.

## Example (illustrative only — not a published card)

```
Term: CUET

One-line definition: A common national entrance test used by many Indian universities
for undergraduate admission, replacing separate university-specific entrance exams.

Expanded explanation: [~100 words explaining what it covers, who takes it, and how
scores are used — illustrative placeholder, not real published content.]

Why it matters: A student choosing between JEE-based and CUET-based routes into a
degree needs to understand this distinction before comparing colleges.

Related cards: [lateral-entry], [degree-vs-diploma]
Related documents: [FAQ Q7 — "Should I do B.Tech via JEE, or through CUET..."]
```

This is a shape reference only — an actual CUET card, if created, lives under `publications/` with full real metadata and content reviewed per `publication-standard.md`.
