# Metadata Standard

Every publication in `knowledge/publications/`, regardless of type, carries this metadata block as YAML front matter at the top of its Markdown source. No publication is considered complete without it.

This standard is the Markdown/YAML **representation** of the EOS-003 Universal Metadata Contract. Every field traces to a Learning Philosophy commitment (see EOS-003 for the full traceability); a field that traces to nothing gets removed, per the two-way rule.

> **Amendment history:**
> **A1 (KA-1.0):** `audience` and `stage` became multi-valued facets; `domain` and `register` added; "pick exactly one audience" withdrawn — focus is enforced by atomicity, not audience-exclusivity.
> **A4 (EOS-003 + EOS-003.1 pilot findings, R1–R8):** contract fields added (`description`, `purpose`, `outcome`, `stakes`, `volatile`, `evidence`, `evidence_notes`, `uncertainty`, `maturity`, typed `relationships`); `visibility`, `updated`, and `review_due` became **derived** fields; authoring conventions added from pilot evidence.

---

## Authored vs. derived: what a contributor actually writes

The pilot (EOS-003.1) showed the contract's ~24 fields split cleanly. **Contributors hand-write only the authored core (~9 fields); everything else is defaulted, inferred, or set at review.** Contributors should start from `templates/AUTHOR_TEMPLATE.md`, which contains only the authored fields.

| Authored by the contributor | Defaulted / inferred | Set or confirmed at review |
|---|---|---|
| title, description, purpose, outcome, stage, audience, evidence (proposal), evidence_notes, uncertainty | id, type, category, domain, language, created, updated (git), version, status, visibility (derived), register, license, review_due (computed) | stakes (confirmed), evidence (confirmed), maturity (raised), relationships (checked) |

---

## The block

```yaml
---
# ── identity (inferred/assigned — do not hand-edit after creation) ──
id: ENA-<TYPE>-<AUDIENCE or DOMAIN>-<slug>          # per document-id-standard.md
type: knowledge-card | publication | learning-path | ...
category: definition | mental-model | checklist | faq | framework | reflection | example |
          guide | workbook | playbook | career-profile | reference | toolkit | letter | student-voice
domain: pathways | careers | skills | deciding | mindset
language: en | ta | te | hi
version: <major>.<minor>                             # Draft = 0.x
status: draft | review | published | maintained | deprecated | archived | retired
owner: "[Named human or team — never 'AI' alone]"
created: YYYY-MM-DD
license: default                                     # free to read/download/share; override needs justification

# ── authored core (the contributor writes these — see AUTHOR_TEMPLATE.md) ──
title: "[Reader-facing title, plain words]"
description: "[1–2 sentences: WHAT this is and who should care]"
purpose: "[The student decision or fear this serves — not the topic]"
outcome: "[A capability the student GAINS — never a decision made for them]"
stage: [after10, after12, college, graduate, early-career]   # every stage where it applies
audience: [student, parent, educator]                        # everyone it genuinely serves
evidence: primary-research | secondary-research | expert-opinion | anecdotal | opinion
evidence_notes: "[What it rests on, named sources; label illustrative composites]"
uncertainty: "[What we don't know, what varies, what the student must verify]"

# ── review-owned (proposed by author, confirmed at review) ──
stakes: high | medium | low          # consequence to a student of this being wrong
volatile: true | false               # does it contain fast-aging data (salaries, fees, exam patterns, cutoffs)?
maturity: seed | developing | established | authoritative    # seed by default; only reviewers raise it
relationships:                       # typed, one direction only (vocabulary per EOS-004)
  - requires: ENA-...
  - exemplifies: ENA-...

# ── derived (never hand-written) ──
# updated:      from git history
# visibility:   derived from status (private until review, internal in review, public when published)
# review_due:   computed from stakes × volatile (table below)
register: reference | voice          # defaulted from category (letter/student-voice → voice)
last_reviewed: YYYY-MM-DD            # set by the reviewer at each review; per-language for translations
---
```

A ready-to-copy contributor version (authored fields only) lives at `templates/AUTHOR_TEMPLATE.md`.

---

## Derived-field rules

**`review_due` — computed, never hand-picked** (pilot finding §3.5: stakes alone was insufficient; volatility is the second input):

| | `volatile: true` | `volatile: false` |
|---|---|---|
| **stakes: high** | 3 months | 6 months |
| **stakes: medium** | 6 months | 12 months |
| **stakes: low** | 12 months | 24 months |
| **register: voice** | — immutable, no review cycle (corrections of fact only, attributed in history) | — |

**`visibility`** — derived from status until a genuine exception exists (e.g., pre-publication access for an external reviewer). If an exception arises, set it explicitly and note why.

**`updated`** — taken from git history at render/validation time. Do not maintain by hand; it will drift.

---

## Field-by-field rules (authored and review-owned fields)

- **`title`** — reader-facing, plain words, and *honest*: a title may not claim more than the content delivers (pilot: "Real Examples" of composites had to become "Worked Examples").
- **`description` vs `purpose`** — description = **what it is**; purpose = **the decision or fear it serves**. If your purpose reads like a topic summary, it's a description; name the student moment instead.
- **`outcome`** — must be phrased as a capability the student gains ("student can compare/evaluate/judge…"), never a decision made for them ("student chooses X"). Reviewers reject decision-phrased outcomes (EOS-003 V4). Model sentences in AUTHOR_TEMPLATE.md.
- **`stage` / `audience`** — multi-valued facets; list everywhere the content genuinely applies. Facets drive surfacing (hubs, paths, search); they never decide filing — `domain` does.
- **`domain`** — exactly one of the five KA-1.0 domains; the canonical home; never changes. Boundary tests in `knowledge-architecture-1.0.md` §3.
- **`evidence`** — rated by the **weakest load-bearing claim**, not the average or the best source. Authors propose; reviewers confirm adversarially (pilot: authors over-claim — 2 of 5 pre-pilot ratings were inflated).
- **Illustrative-composite convention** (pilot R3): a constructed scenario built on real data is rated by what it *carries* —
  - composite is **load-bearing** for the card's claim → rate `anecdotal`, write "illustrative composite" in `evidence_notes`, and label it in the body;
  - composite is **explanatory only** (the claim rests on real data elsewhere) → the data's rating stands; disclose the composite in `evidence_notes`.
- **`uncertainty`** — required when stakes are high or evidence is anecdotal/opinion; recommended always. Per-category starting points (pilot R4):
  - *definition* → framing variance: "this is one widely-used framing, not a universal standard"
  - *data-bearing (salaries, fees, dates)* → verify-live instructions: what varies, by how much, where to check
  - *checklist / self-assessment* → instrument limits: self-assessment is unreliable; thresholds are heuristics
  - *example* → composite/anecdote disclaimer: no real outcome will match; direction, not forecast
  - *mental-model / framework* → scope limits: where the model breaks down
- **`stakes`** — the consequence to a student of this content being wrong. High: can redirect years or money (eligibility, entry requirements, stream criteria). Medium: shapes preferences (salary ranges, growth ladders, readiness guidance). Low: error costs a re-read (study tips, reflection prompts). Author proposes; **reviewer confirms** — authors sit too close to their own content to rate its blast radius.
- **`volatile`** — true if the content contains data that ages in months: salaries, fees, exam patterns, cutoffs, hiring trends. Feeds the `review_due` table.
- **`maturity`** — earned, not asserted: `seed` (default at creation) → `developing` (one review survived, used on ≥1 surface) → `established` (full review cycle + feedback incorporated) → `authoritative` (evidence classified, priority translations exist). Only reviewers raise it; anyone may propose demotion when a source goes stale. Full criteria: KA-1.1 spec (pending).
- **`relationships`** — typed links, stored in **one direction only** (inverses are derived, never written). Vocabulary and direction rules: EOS-004. Omit the key entirely when empty.
- **`owner`** — a named human or team; never "AI" alone. AI may assist drafting (per the site's public transparency commitment); a person answers for every published claim.
- **`last_reviewed`** — set by the reviewer at each completed review. Translations carry their own: a stale translation of a fresh source is still stale.
- **`license`** — default: free to read, download, and share for personal and educational use; not for resale or republication without permission. Overrides need explicit justification.
- **`tags`** *(optional)* — free-text discovery only; nothing structural may depend on tags. Omit rather than invent.

### Legacy fields

`prerequisites`, `related_documents`, `related_careers`, `related_skills`, `subtitle`, `reading_level`, `estimated_reading_time` / `estimated_completion_time`, `difficulty` remain valid on existing documents. On next substantive touch: `prerequisites` migrates to `relationships: requires`, `related_*` to the appropriate typed relationship (per EOS-004); reading/completion estimates and difficulty stay as optional presentation hints.

---

## The review gate (pilot R8)

A document does not move `review → published` until the reviewer has explicitly:

1. **Confirmed `stakes`** (or corrected it — and with it, the computed `review_due`)
2. **Confirmed `evidence`** against the weakest-load-bearing-claim rule, adversarially
3. **Checked `outcome`** is capability-phrased (V4) and `uncertainty` is present where required (V1/V3)
4. **Verified `relationships`** point at real, current IDs
5. Set `last_reviewed`; raised `maturity` only if criteria are met

This gate is a checklist today and tooling in Phase 2 (the validation script planned in KA-1.1 area 4).
