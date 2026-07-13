# Knowledge Architecture 1.1 — Planning Document

**Status:** Plan (not yet a specification)
**Version:** 0.1
**Last Updated:** 2026-07-13
**Owner:** Chief Knowledge Architect
**Builds on:** KA-1.0 (approved 2026-07-13), EOS-001, EOS-002
**Coordinates with:** EOS-003 (Universal Metadata Contract — not yet written)

---

## 0. SCOPE AND CONSTRAINTS

KA-1.1 is an **enhancement release**, not a structural one. Four hard constraints, set at approval of KA-1.0:

1. **The object model does not expand.** The 10 EOS-002 types remain frozen. Everything below is metadata, controlled vocabulary, or convention — nothing is a new object type.
2. **Filing by domain, surfacing by facet is preserved untouched.** No enhancement may give any view, hub, or audience ownership of content.
3. **Everything in KA-1.1 is additive.** A KA-1.0-conformant card remains conformant under KA-1.1; new fields arrive with defaults, never as retroactive breakage.
4. **Nothing lands that doesn't improve publishing, reuse, search, or AI consumption** (the EOS-002 value filter).

KA-1.1 covers four enhancement areas: **knowledge maturity**, **evidence levels**, **semantic relationships**, and **reuse metadata**.

---

## 1. ENHANCEMENT AREA 1: KNOWLEDGE MATURITY

### The problem

`status` (Draft → In Review → Published) describes *workflow position*, not *content quality*. Two published cards can differ enormously: one is a first pass written from one source; another has survived three review cycles, student feedback, and a translation. Readers, reusers, and AI systems currently can't tell them apart.

### The proposal to develop

A `maturity` field, orthogonal to `status`:

| Level | Meaning (draft definition) |
|---|---|
| `seed` | First written pass; believed correct but unvalidated beyond the author |
| `developing` | Reviewed once; used on at least one surface; known gaps documented |
| `established` | Survived a full review cycle; multiple surfaces; feedback incorporated |
| `authoritative` | Enaasan's reference answer on the topic; evidence classified; translated to priority languages |

**Key design questions for the spec:**

- Is maturity *asserted* (owner judgment) or *earned* (criteria checklist per level)? Leaning: earned, with a short objective checklist per level — otherwise it inflates.
- Can maturity go *down*? (e.g., established card whose data source goes stale). Leaning: yes — staleness demotes.
- Should surfaces display maturity to students, or is it internal? Leaning: internal at first; a public "confidence" treatment is a later editorial decision.

### Why it's an enhancement, not a structure change

It's one controlled-vocabulary field plus level criteria. No object, domain, or facet changes.

---

## 2. ENHANCEMENT AREA 2: EVIDENCE LEVELS

### The problem

EOS-002 already defines evidence classification conceptually (Primary Research / Secondary Research / Expert Opinion / Anecdotal / Opinion) and the communication cards carry a free-prose "Evidence Level" line. But it isn't a controlled field yet, so nothing can query it, badge it, or flag "high-stakes claim resting on low evidence."

### The proposal to develop

1. **Object-level field** (KA-1.1): `evidence: primary-research | secondary-research | expert-opinion | anecdotal | opinion` — the evidence level of the object's *weakest load-bearing claim*, plus `evidence_notes` for sourcing.
2. **Claim-level classification** (explicitly deferred, likely KA-1.2+): per-claim tagging inside card bodies. EOS-002 flagged this as demanding; it stays an aspiration until the object-level habit is established.

**Key design questions for the spec:**

- Interaction with maturity: can a card be `authoritative` on `expert-opinion` evidence? Leaning: yes — career advice is legitimately expert judgment; the two axes measure different things. This is exactly why they must be separate fields.
- Volatile-data linkage: should `evidence` interact with `review_due` (e.g., `secondary-research` salary data forces ≤12-month review)? Leaning: yes, as a rule table in the spec.
- Public display: evidence badges on high-stakes pages align with the existing sources/verification backlog item (WS-06 / issue #72) — the spec should name that issue as its application target.

---

## 3. ENHANCEMENT AREA 3: SEMANTIC RELATIONSHIPS

### The problem

`related_documents` is an untyped list. "Related" can't tell a renderer, a path-builder, or an AI *how* things relate: is Card A a prerequisite of B, a contradiction of B, evidence for B, a comparison with B? EOS-004 (Relationship Model) will define relationship semantics at the EOS grammar level; KA-1.1 applies a *minimal, useful subset* to Enaasan content.

### The proposal to develop

Replace (additively — old field stays valid) the untyped list with typed links, drawn from a small controlled vocabulary. Candidate starter set:

| Relationship | Meaning | Example |
|---|---|---|
| `requires` | Read/understand that first | Five-competencies card *requires* the definition card |
| `elaborates` | Goes deeper on the same concept | Salary-impact example *elaborates* the salary-premium model |
| `exemplifies` | Concrete instance of an abstract claim | BPS example *exemplifies* the premium mental model |
| `compares` | Side-by-side decision content | B.Com-vs-BBA card *compares* two PATHWAYS cards |
| `contradicts` | Conflict requiring editorial resolution | Should be rare; existence of the type makes conflicts findable |
| `supersedes` | This replaces that (retirement links) | Already implied by versioning-standard; make it queryable |
| `extracted-from` | Card was distilled from a voice publication | Implements KA-1.0 Rule V2 mechanically |

**Key design questions for the spec:**

- Direction and inverses: store one direction only (`requires`), derive the inverse (`required-by`) at query time — never store both (they drift). This should be a hard rule.
- How many types is too many? Starter set above is 7; EOS-004 may define more. KA-1.1 should adopt the *minimum* that current content actually exhibits, and let EOS-004 own the full vocabulary.
- **Sequencing dependency:** EOS-004 doesn't exist yet. Decision needed: write EOS-004 first and let KA-1.1 apply it (cleaner, slower), or let KA-1.1's practical needs draft the vocabulary and feed EOS-004 (faster, risk of rework). **Recommendation: EOS-003 and EOS-004 first, then KA-1.1 spec** — KA-1.1 is the application layer of both, and writing it second avoids inventing two vocabularies.

---

## 4. ENHANCEMENT AREA 4: REUSE METADATA

### The problem

KA-1.0 §7 admits the embed verb is manual on a static site: canonical source in `knowledge/`, hand-copied renderings in HTML. Nothing currently records *where each card is used*. When the salary-premium card updates, finding its five surfaces is grep-and-hope. This is the single biggest operational risk in the KA-1.0 design.

### The proposal to develop

1. **`used_by` manifest** — a machine-readable record per card (or one central manifest) listing every surface that embeds or renders it: page, publication, path, tool. Updated whenever a surface adopts a card. This is the "bill of materials" inverted.
2. **Canonical-source comments** — a required comment convention at every rendering site (e.g., in HTML: `<!-- canonical: ENA-KCARD-SKILL-communication-salary-premium-v0.1 -->`), making renderings greppable from the other direction.
3. **Staleness propagation rule** — when a card's version increments, its `used_by` list becomes the update checklist; the card isn't "done updating" until every listed surface is refreshed or consciously deferred.

**Key design questions for the spec:**

- Per-card manifest vs. one central registry? Leaning: central registry file — one place to look, trivially diffable, and avoids touching card files when surfaces change.
- Should `used_by` count as metadata *about the card* (it isn't, really — it's about the surfaces) or a separate index? Architecturally it's an index; storing it inside cards would violate "context lives in the relationship" in spirit.
- Tooling ambition: a validation script (check every canonical-source comment resolves to a real ID; check every registry entry's version matches) is the first genuinely useful automation of Phase 2 — small, high-value, and doesn't touch the website.

---

## 5. HOW THE FOUR AREAS INTERLOCK

These are one system, not four features:

```
EVIDENCE  (how well-supported is it?)   ┐
MATURITY  (how proven/complete is it?)  ├─→ trust signals → surfaces can badge,
                                        ┘   AI can weight, editors can prioritize

SEMANTIC RELATIONSHIPS (how does it connect?) → path-building, contradiction
                                                detection, glossary depth

REUSE METADATA (where does it live downstream?) → safe updates, impact analysis,
                                                  the discipline that makes
                                                  "single source of truth" real
```

A future editorial dashboard question KA-1.1 makes answerable: *"Show me every `established`+ card resting on `anecdotal` evidence that is used on 3+ surfaces"* — i.e., exactly where reputational risk concentrates.

---

## 6. PROPOSED SEQUENCE

| Step | Deliverable | Depends on |
|---|---|---|
| 1 | **EOS-003** Universal Metadata Contract (already next in the EOS queue) — absorbs maturity + evidence as contract fields | EOS-002 (done) |
| 2 | **EOS-004** Relationship Model — full relationship vocabulary | EOS-003 |
| 3 | **KA-1.1 specification** — applies both to Enaasan content: level criteria for maturity, evidence rules per domain, the starter relationship set, the reuse registry format | EOS-003, EOS-004 |
| 4 | **Retrofit pilot** — the five communication cards become the first KA-1.1-conformant content (again the pattern-setters) | KA-1.1 spec |
| 5 | **Validation script** — canonical-comment and registry checker (first Phase 2 tooling) | Step 4 |

This keeps the promise made in EOS-001: specification before implementation, one layer at a time — while giving each spec a concrete application target so it never floats free of reality.

---

## 7. EXPLICIT NON-GOALS FOR KA-1.1

- No new object types (frozen; ADR required)
- No changes to the five domains or the facet axes
- No claim-level evidence tagging (deferred to KA-1.2+)
- No automated transclusion/publishing pipeline (Phase 3 per EOS-001)
- No public-facing trust badges yet (editorial decision after the metadata exists)
- No search or AI features (applications of the metadata, not part of it)

---

## 8. OPEN QUESTIONS

1. Maturity: asserted vs. earned — needs a decision before the spec is written (recommendation: earned, checklist-based).
2. Does `maturity` belong in the EOS-003 universal contract (every object, including Tasks and Decisions?) or only knowledge objects? Leaning: knowledge objects only — a Task doesn't mature, it completes. If so, EOS-003 needs a "knowledge-object extension" section, which is itself a design decision about how the universal contract handles category-specific fields.
3. Relationship storage location for a static repo: front-matter lists vs. central relationships file? (Mirrors the reuse-registry question; they should get the same answer.)
4. Who maintains the reuse registry until tooling exists — author of the card, or author of the surface? Leaning: surface author (they created the dependency).

---

## DOCUMENT HISTORY

| Version | Date | Change | Author |
|---------|------|--------|--------|
| 0.1 | 2026-07-13 | Initial plan: four enhancement areas scoped as additive metadata/conventions; sequencing recommendation (EOS-003 → EOS-004 → KA-1.1 spec → retrofit pilot → validation script) | Chief Knowledge Architect |
