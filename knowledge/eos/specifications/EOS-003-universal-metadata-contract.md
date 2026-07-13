# EOS-003: Universal Metadata Contract

**Status:** Approved — part of the Enaasan Knowledge Standard v1.0 (validated by EOS-003.1 pilot)
**Version:** 1.0
**Last Updated:** 2026-07-13
**Owner:** Chief Knowledge Architect
**Depends on:** EOS-001 (Philosophy), EOS-002 (Object Model), KA-1.0 (Knowledge Architecture), LEARNING_PHILOSOPHY v1.0
**Normative Language:** RFC 2119 (SHALL, SHOULD, MAY)

---

## PURPOSE

Define the metadata contract that every EnaasanOS object carries: which fields exist, what each means, which are required, and — critically — **why each field is allowed to exist**.

This specification is governed by the two-way rule from LEARNING_PHILOSOPHY §6:

> A metadata field that cannot be traced to a Learning Philosophy commitment is bureaucracy and SHALL be removed. A commitment with no enforcing field or rule is a gap and SHALL be closed.

Accordingly, **every field in this contract carries a `Traces to` line** naming the commitment(s) it enforces. A proposal to add a field without a traceable commitment SHALL be rejected.

This document remains technology-independent (EOS-001, Principle 1). It defines fields as concepts; how they are written down (YAML front matter, JSON, database columns) is a representation-layer concern (see §8 for the mapping to the current Markdown representation).

---

## PROBLEM BEING SOLVED

Without a universal contract:

- Every object type invents its own metadata shape; nothing can be queried across types ("show me everything due for review" becomes impossible)
- Quality commitments stay aspirational — "we review high-stakes content often" means nothing unless *stakes* and *review dates* are recorded somewhere queryable
- Reuse breaks — a hub cannot surface objects by stage if stage isn't a controlled field
- AI consumption becomes guesswork — a future assistant cannot distinguish measured fact from opinion unless evidence is machine-readable
- New authors have no checklist for "what makes this object complete"

The contract makes the Learning Philosophy *enforceable*: each moral commitment becomes a field plus a validation rule.

---

## CONTRACT STRUCTURE: TWO TIERS, NOT ONE

The contract has two tiers:

- **Tier 1 — Core Contract:** fields every one of the 10 object types SHALL carry. Deliberately small.
- **Tier 2 — Knowledge Extension:** additional fields that knowledge-bearing objects (Knowledge Card, Publication, Learning Path, Career, Skill) SHALL carry. Planning and measurement objects (Initiative, Task, Decision, Metric, Release) do not carry these — a Task does not have an evidence level, and pretending it does would be exactly the bureaucracy the philosophy forbids.

This resolves KA-1.1 open question 2: maturity, evidence, and their siblings are knowledge-object concerns. *(A Task doesn't mature; it completes.)*

---

## TIER 1: THE CORE CONTRACT (ALL 10 OBJECT TYPES)

### 1.1 `id`

- **What:** Permanent, unique, never-reused identifier. For the current representation, the Document ID standard applies (`ENA-<TYPE>-<AUDIENCE|DOMAIN>-<slug>`); the contract requires only permanence and uniqueness, not that format.
- **Rules:** Assigned at Draft, never changes, never reused after retirement. Facet-like properties (audience, stage) SHALL NOT be part of identity; only permanent properties (type, domain for cards) may be.
- **Traces to:** *Corrections are public* and *knowledge retires visibly* (LP §4) — both require references that survive every change; *single source of truth* (EOS-001 P2).

### 1.2 `title`

- **What:** Human-readable name, in the object's language, written for the actual reader.
- **Rules:** Reader-facing, plain words. Not the slug.
- **Traces to:** *Written for our actual reader* (LP §3).

### 1.3 `description`

- **What:** One or two sentences: what this is and who should care.
- **Rules:** SHALL be understandable without opening the object. Used by views, search results, and AI retrieval as the object's self-introduction.
- **Traces to:** *Decision-usefulness* (LP §1) — a student (or editor) deciding whether to read something is itself a decision we owe honest help with.

### 1.4 `type` and `category`

- **What:** `type` = one of the 10 frozen EOS-002 object types. `category` = the specialization within the type (card: definition/mental-model/checklist/faq/framework/reflection/example; publication: guide/workbook/playbook/career-profile/reference/toolkit/letter/student-voice).
- **Rules:** Both from controlled vocabularies. New categories are cheap (list extension); new types require an ADR (EOS-002 freeze).
- **Traces to:** *What makes a card worth creating* (LP §2) — the type/category decision procedure (KA-1.0 §6) is how the worth-creating test is applied in practice.

### 1.5 `purpose`

- **What:** Why this object exists — for knowledge objects, **which student decision or fear it serves**; for planning objects, which goal it advances.
- **Rules:** Required. For knowledge objects it SHALL name a real decision point or anxiety ("helps a 12th-grader weigh BPS against its stigma"), not a topic ("about BPS"). An object whose purpose cannot be stated this way fails the belonging test and SHALL NOT be published.
- **Traces to:** *The decision-usefulness test* (LP §1); *real decision point* (LP §2).

### 1.6 `outcome`

- **What:** What the consumer can *do* after consuming this object.
- **Rules:** Required. For knowledge objects, SHALL be phrased as a **capability the student gains** ("student can compare B.Com and BBA using criteria that matter to their situation"), NEVER as a decision made for them ("student chooses B.Com"). This phrasing rule is validated at review.
- **Traces to:** *Agency over dependence* (LP §5) — the outcome field is where "teach the how of thinking" becomes checkable; *we inform decisions, we never make them* (LP §5).

### 1.7 `status`

- **What:** Workflow state. Vocabulary per EOS-002 lifecycles (draft, review, published, maintained, deprecated, archived — subset varies by type as specified there).
- **Rules:** Transitions follow the object's EOS-002 state machine. Published knowledge objects SHALL enter maintenance, not stand still.
- **Traces to:** *Publishing is the beginning of a responsibility* (LP §4).

### 1.8 `version`

- **What:** Version identifier (major.minor per the existing versioning standard).
- **Rules:** Draft = 0.x. Every version change is recorded with who and when; history is preserved and public.
- **Traces to:** *Corrections are public, not embarrassing* (LP §4).

### 1.9 `owner`

- **What:** The named human (or team with a named point of contact) answerable for this object.
- **Rules:** SHALL be a person or team — never "AI", never blank, never anonymous. Ownership transfer is recorded in history. The owner is the person who "would repeat its claims to a student's face."
- **Traces to:** *A named human answers for everything* (LP §5); *canonical ownership* (EOS-001 P5).

### 1.10 `created` / `updated`

- **What:** Timestamps of creation and last substantive change.
- **Rules:** `updated` changes on substance, not typo fixes (representation layer may track both; the contract requires substance-tracking).
- **Traces to:** *Knowledge decays* (LP §4) — a reader deserves to know how old what they're reading is.

### 1.11 `language`

- **What:** The language of this object's content (`en`, `ta`, `te`, `hi`, extensible).
- **Rules:** Language variants are the same object in different languages, linked, with per-language review dates — not independent objects (EOS-001 P7). A translation SHALL carry its own `last_reviewed`, because a translation can go stale independently of its source.
- **Traces to:** *In the student's language — genuinely* (LP §3).

### 1.12 `relationships`

- **What:** Typed links to other objects. Starter vocabulary per KA-1.1 plan: `requires`, `elaborates`, `exemplifies`, `compares`, `contradicts`, `supersedes`, `extracted-from` — to be completed by EOS-004.
- **Rules:** Stored in one direction only; inverses are derived, never stored (two stored directions drift). `supersedes` is mandatory when an object replaces another.
- **Traces to:** *Knowledge retires visibly* (LP §4 — `supersedes`); *composable knowledge* (EOS-001 P4); *extraction rule* (KA-1.0 V2 — `extracted-from`).

### 1.13 `visibility`

- **What:** `private` (drafting) | `internal` (reviewable) | `public` (published to students).
- **Rules:** Knowledge objects SHALL NOT be `public` before completing review (status ≥ published) and meeting Tier 2 validation (§3). Distinct from `status`: status is where the work is; visibility is who may see it.
- **Traces to:** *Do no harm comes before be helpful* (LP §5) — unready knowledge is not shown to students.

### 1.14 `license`

- **What:** Usage terms. Default: free to read, download, and share for personal and educational use.
- **Rules:** Default applies unless explicitly overridden with justification; no object may require payment or personal data for access.
- **Traces to:** *Free means actually free* (LP §5).

### 1.15 `tags` (optional)

- **What:** Free-text discovery keywords.
- **Rules:** MAY be present; SHALL NOT carry structural meaning (nothing may query tags to make decisions — that's what controlled facets are for).
- **Traces to:** *Decision-usefulness* (LP §1) via findability — weakly. This is the contract's most marginal field; it survives only because it is explicitly non-structural and zero-maintenance. If it grows structural weight, it SHALL be converted to a controlled facet or removed.

### 1.16 `ai_metadata` (reserved, empty)

- **What:** A reserved namespace for future AI-consumption hints (retrieval weighting, answer-context rules, citation requirements).
- **Rules:** Reserved and empty in this version. When populated (future phase), any AI-facing rule SHALL enforce the same philosophy commitments — in particular, an AI consumer SHALL receive evidence and uncertainty alongside content, so it cannot present opinion as fact. Reserving the namespace now prevents ad-hoc AI fields later.
- **Traces to:** *The three attachments rule* (LP §5) applied to machine consumers; forward-compatibility (EOS-001, Principle E).

---

## TIER 2: THE KNOWLEDGE EXTENSION (KNOWLEDGE CARD, PUBLICATION, LEARNING PATH, CAREER, SKILL)

### 2.1 `domain`

- **What:** Exactly one of the five KA-1.0 domains (Pathways, Careers, Skills, Deciding, Mindset).
- **Rules:** The canonical home; never changes (if it must, that's a new object superseding the old). Boundary tests per KA-1.0 §3.
- **Traces to:** *Single source of truth* (EOS-001 P2) via one-canonical-home (KA-1.0 R1).

### 2.2 `stage` and `audience` (facets, multi-valued)

- **What:** `stage`: every life stage where this applies (after10, after12, college, graduate, early-career). `audience`: student, parent, educator.
- **Rules:** Multi-valued, controlled vocabularies. Facets drive surfacing (hubs, paths, search); they never drive filing.
- **Traces to:** *Closing the information asymmetry* (LP §1) — the same truth reaches every group that needs it, rather than being rewritten per audience; *reusability* (LP §2).

### 2.3 `register`

- **What:** `reference` (timeless, maintained) | `voice` (dated, immutable).
- **Rules:** Voice objects carry `published_date` and are exempt from review cycles (§2.7) — they are honest artifacts of a moment. Durable insights in voice objects are extracted into reference cards (`extracted-from`).
- **Traces to:** *Timely vs. timeless honesty* (LP §2); *a stale card is worse than no card* (LP §2) — the register split is what lets letters exist without becoming stale reference.

### 2.4 `stakes`

- **What:** `high` | `medium` | `low` — the consequence to a student of this content being wrong. High: content that can redirect years or money (stream choice criteria, exam eligibility, career-entry requirements). Medium: content that shapes preferences (salary ranges, growth ladders). Low: content where error costs a re-read (study tips, reflection prompts).
- **Rules:** Required. Set at review, not by the author alone (authors underestimate stakes). Drives validation: see §3 interlock rules.
- **Traces to:** *The stakes are asymmetric, and we must never forget it* (LP §5) — this field is that sentence made mechanical. *(New field — no prior standard had it; the philosophy demanded it.)*

### 2.5 `evidence` and `evidence_notes`

- **What:** `evidence`: the controlled level of the object's weakest load-bearing claim — `primary-research` | `secondary-research` | `expert-opinion` | `anecdotal` | `opinion`. `evidence_notes`: what the content rests on, named ("NASSCOM BPS report 2024-25; Glassdoor/AmbitionBox postings analysis; 25 practitioner interviews").
- **Rules:** Required on knowledge objects. Rated by the *weakest* load-bearing claim, not the average — a card of official data with one anecdotal salary figure is `anecdotal` until that figure is sourced or removed. Claim-level tagging remains deferred (KA-1.1 → 1.2+).
- **Traces to:** *Say what we know, and how we know it* (LP §3); *the three attachments rule* (LP §5).

### 2.6 `uncertainty`

- **What:** What we don't know, what varies by situation, and what the student must verify themselves ("salary bands vary 15–30% by city and shift; verify current figures with live postings; eligibility criteria change — check the official notification").
- **Rules:** Required when `stakes: high` or `evidence` is `anecdotal`/`opinion`; RECOMMENDED otherwise. An empty uncertainty field on a high-stakes object SHALL block publication — high-stakes content with "nothing uncertain" is a claim we are almost never entitled to make.
- **Traces to:** *No false certainty* (LP §3); *the three attachments rule* (LP §5). *(New field — introduced by the philosophy amendment.)*

### 2.7 `last_reviewed` / `review_due`

- **What:** When a human last verified this content; when verification is next owed.
- **Rules:** Required for `register: reference`; not applicable to `voice`. `review_due` is set by the interlock rules (§3), not chosen freely. An overdue object is flagged and, if `stakes: high`, SHALL have its visibility reconsidered.
- **Traces to:** *Review rhythm matched to decay* (LP §4).

### 2.8 `maturity`

- **What:** `seed` | `developing` | `established` | `authoritative` — earned position on the quality ladder, orthogonal to `status`.
- **Rules:** Earned via per-level criteria checklists (to be finalized in the KA-1.1 spec; direction fixed here): levels require survived reviews, use on real surfaces, incorporated feedback, and (for `authoritative`) classified evidence and priority-language translation. Maturity CAN demote (stale source, failed review). Authors SHALL NOT self-assign above `developing`.
- **Traces to:** *Knowledge matures through contact with students, not through polish* (LP §4).

---

## §3 VALIDATION: THE INTERLOCK RULES

Fields are necessary but not sufficient; the philosophy lives in how they constrain each other. These rules SHALL be enforced at review (by checklist today, by tooling in Phase 2):

| # | Rule | Traces to |
|---|---|---|
| V1 | `stakes: high` ⇒ `review_due` ≤ 6 months AND `evidence` ≥ `secondary-research` AND `uncertainty` non-empty | Asymmetric stakes; do no harm (LP §5) |
| V2 | `stakes: medium` ⇒ `review_due` ≤ 12 months | Review rhythm (LP §4) |
| V3 | `evidence` ∈ {anecdotal, opinion} ⇒ `uncertainty` non-empty, and surfaces SHOULD label the content as judgment | No false certainty (LP §3) |
| V4 | `outcome` SHALL be capability-phrased; reviewer rejects decision-phrased outcomes ("student chooses X") | Agency over dependence (LP §5) |
| V5 | `owner` SHALL name a human or team; "AI" alone is invalid | Named human accountability (LP §5) |
| V6 | `visibility: public` ⇒ status ≥ published AND all Tier-2 required fields present and valid | Do no harm (LP §5) |
| V7 | `status: retired/archived` ⇒ a `supersedes` inverse exists or an explicit "no replacement" note | Knowledge retires visibly (LP §4) |
| V8 | `category: student-voice` ⇒ consent record exists per the consent policy (prerequisite: that policy, KA-1.0 open q.4) | Student-voice protection (LP §5) |
| V9 | `register: voice` objects are immutable after publication except for corrections of fact attributed in history | Timely vs. timeless honesty (LP §2) |
| V10 | A translation's `last_reviewed` is per-language; a stale translation of a fresh source is still stale | Language equity (LP §3) |

---

## §4 REVERSE TRACEABILITY: EVERY COMMITMENT HAS TEETH

The philosophy's two-way rule requires checking both directions. Commitment → enforcing fields/rules:

| LP Commitment | Enforced by |
|---|---|
| Decision-usefulness test (§1, §2) | `purpose` (1.5), `description` (1.3) |
| Willingness to maintain (§2) | `review_due` (2.7), V1–V2, maturity demotion (2.8) |
| Timely vs. timeless honesty (§2) | `register` (2.3), V9 |
| Honesty over encouragement (§3) | `evidence_notes` (2.5), `uncertainty` (2.6) — omission becomes visible |
| Say how we know it (§3) | `evidence`, `evidence_notes` (2.5) |
| No false certainty (§3) | `uncertainty` (2.6), V3 |
| Language equity (§3) | `language` (1.11), V10 |
| Review rhythm (§4) | `last_reviewed`/`review_due` (2.7), V1–V2 |
| Earned maturity (§4) | `maturity` (2.8) |
| Public corrections (§4) | `version` (1.8) + history |
| Visible retirement (§4) | `relationships: supersedes` (1.12), V7 |
| Asymmetric stakes (§5) | `stakes` (2.4), V1 |
| Do no harm (§5) | `visibility` (1.13), V6 |
| Free means free (§5) | `license` (1.14) |
| Inform, never decide / three attachments (§5) | `evidence` + `evidence_notes` + `uncertainty` together; `ai_metadata` reservation (1.16) |
| Agency over dependence (§5) | `outcome` capability-phrasing (1.6), V4 |
| Named human accountability (§5) | `owner` (1.9), V5 |
| Student-voice protection (§5) | V8 + consent policy prerequisite |

No commitment is left without a mechanism; no field lacks a commitment. The contract is closed in both directions.

---

## DESIGN DECISIONS

**D1 — Two tiers instead of one universal set.**
*Alternatives:* one contract for everything (simpler, but forces `evidence` onto Tasks — meaningless fields rot discipline); per-type contracts (precise, but kills cross-type querying).
*Trade-off:* two tiers add one concept but keep both universality (Tier 1 queries span everything) and honesty (Tier 2 exists only where it means something).

**D2 — `stakes` as a first-class field.**
*Alternative:* infer stakes from domain or category (exam content = high).
*Rejected because* stakes cut across domains — a MINDSET card on dropping out is high-stakes; a CAREERS card listing employers by city is low-stakes. Inference would be wrong exactly where it matters. *Cost:* one more judgment call per object; mitigated by setting it at review, not authorship.

**D3 — `uncertainty` as its own field, not folded into `evidence_notes`.**
*Alternative:* one combined sourcing-and-caveats field.
*Rejected because* the philosophy amendment names uncertainty as one of three distinct attachments, and because surfaces will render them differently (evidence as a badge, uncertainty as a reader-facing caveat box). Merged fields get skipped; the separate field makes the caveat's absence visible (V1, V3).

**D4 — Evidence rated by the weakest load-bearing claim.**
*Alternative:* rate by the predominant evidence level.
*Rejected because* a student harmed by the one unsourced claim is not comforted by the average. The strict rule also creates the right pressure: source the weak claim or cut it.

**D5 — `ai_metadata` reserved now, empty now.**
*Alternative:* omit until needed.
*Rejected because* namespaces added under pressure skip philosophy review. Reserving it now attaches the constraint (AI consumers get evidence + uncertainty, always) before any implementation exists to argue with.

**D6 — Facets excluded from identity.**
Already decided in KA-1.0 A2; restated here as contract law: identity is permanent, facets evolve, therefore facets never enter `id`.

---

## EXAMPLES (TECHNOLOGY-NEUTRAL)

**A Knowledge Card (Tier 1 + Tier 2):**

```
id:            ENA-KCARD-SKILL-communication-salary-premium
type:          knowledge-card        category: mental-model
title:         Why Communication Skills Command a 20–30% Salary Premium
description:   The economic mechanism behind the communication pay gap,
               with premiums by role level.
purpose:       Helps a student deciding whether communication practice is
               worth deliberate investment alongside marks/technical prep.
outcome:       Student can evaluate any "soft skills matter" claim in
               rupee terms and judge the ROI for their own situation.
status:        draft                 version: 0.1
owner:         Career Guidance (S. Ahamed)
created:       2026-07-12            updated: 2026-07-13
language:      en
visibility:    internal
license:       default (free)
domain:        skills
stage:         [after12, college, graduate, early-career]
audience:      [student, parent]
register:      reference
stakes:        medium
evidence:      secondary-research
evidence_notes: Glassdoor/AmbitionBox postings analysis (2024-25);
               NASSCOM BPS report; 50+ recruiter interviews.
uncertainty:   Premiums vary by company tier, city, and shift; figures are
               indicative ranges, not offers — verify against live postings.
last_reviewed: 2026-07-12            review_due: 2027-07-12   (V2: ≤12mo)
maturity:      seed
relationships: elaborates → ENA-KCARD-SKILL-communication-competency-definition
               exemplified-by ← (derived) …salary-impact-bps
```

**A Task (Tier 1 only):**

```
id:        ENA-TASK-write-mindset-domain-first-cards
type:      task
title:     Write the first three MINDSET domain cards
purpose:   Advances the domain-coverage goal — MINDSET is the only
           domain with zero cards.
outcome:   Three reviewed cards exist; MINDSET folder is no longer empty.
status:    backlog     version: 0.1
owner:     S. Ahamed   created/updated: 2026-07-13
language:  en          visibility: internal
relationships: contributes-to → (initiative TBD)
```
*(No domain, no evidence, no stakes — Tier 2 does not apply, by design.)*

**A voice letter (Tier 2, voice register):**

```
id:        ENA-LETTER-WORK-what-a-recruiter-told-me
type:      publication   category: letter   register: voice
published_date: 2026-08-01   (immutable; no review_due — V9)
evidence:  anecdotal
uncertainty: One recruiter's view, one week, one city. (V3 satisfied)
relationships: (future) extracted-from ← any card distilled from it
```

---

## RELATIONSHIP TO THE EXISTING `metadata-standard.md` (PROPOSED AMENDMENT A4)

The current YAML standard is one *representation* of this contract. Gaps between contract and representation, to be closed in a follow-up amendment (**A4 — proposed, not executed**):

| Contract field | In current YAML standard? |
|---|---|
| purpose, outcome | ✗ missing |
| stakes, evidence, evidence_notes, uncertainty | ✗ missing |
| maturity | ✗ missing |
| register, domain, stage, audience | ✓ (added by A1) |
| visibility | ✗ missing (implied by status today) |
| ai_metadata | ✗ missing (reserved) |
| id/title/version/status/author/reviewed/license/tags/relationships | ✓ present (relationships untyped until EOS-004) |

---

## FUTURE CONSIDERATIONS

- **EOS-004** completes the relationship vocabulary this contract references (1.12)
- **KA-1.1 spec** finalizes maturity level criteria (2.8) and the reuse registry (which is an *index about* objects, deliberately not a field *on* them — KA-1.1 area 4)
- **Claim-level evidence** (KA-1.2+) will refine 2.5 without changing it
- **`ai_metadata`** population is a Phase 4 concern with its constraint already fixed (D5)
- **Per-language review dashboards** become possible once V10 is practiced

## QUESTIONS STILL OPEN

1. Should `stakes` be reviewable by students ("report: this mattered more than you thought")? Leaning yes eventually — it's the field most likely to be miscalibrated from the inside.
2. `visibility: internal` currently equals "reviewable" — do we need a fourth state for content shared with external reviewers (teachers, counsellors) pre-publication? Defer until the need is real.
3. Does a Learning Path's `evidence` mean anything (it owns no claims)? Current answer: a path inherits the minimum evidence of its steps for display purposes, but records none itself. To be confirmed in EOS-004 when composition semantics are formal.

---

## DOCUMENT HISTORY

| Version | Date | Change | Author |
|---------|------|--------|--------|
| 1.0 | 2026-07-13 | Initial contract: two-tier structure (core + knowledge extension), 16 core + 8 extension fields each with philosophy traceability, 10 interlock validation rules, reverse-traceability table closing the two-way rule, amendment A4 proposed for the YAML representation | Chief Knowledge Architect |
