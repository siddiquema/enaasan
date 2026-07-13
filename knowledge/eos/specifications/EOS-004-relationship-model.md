# EOS-004: Relationship Model

**Status:** Draft for Review
**Version:** 1.0
**Last Updated:** 2026-07-13
**Owner:** Chief Knowledge Architect
**Depends on:** EOS-001, EOS-002, EOS-003 (validated via EOS-003.1), KA-1.0, LEARNING_PHILOSOPHY v1.0
**Normative Language:** RFC 2119 (SHALL, SHOULD, MAY)

---

## PURPOSE

Define how EnaasanOS objects connect: the complete relationship vocabulary, which side stores each link, cardinality, what happens when related objects change or retire, and how composition semantics work (what a Publication "made of cards" actually means).

EOS-002 described relationships in prose ("a Publication contains Knowledge Cards"; "a Career requires Skills"). EOS-003 defined the `relationships` field and a starter vocabulary. This specification makes relationships **precise enough to validate** — and keeps them few enough to actually use.

---

## PROBLEM BEING SOLVED

Untyped links ("related documents") cannot answer the questions the system exists to answer:

- A learning path builder needs *prerequisite order*, not "related"
- A hub rendering "students also explored" needs *similarity*, not "related"
- An editor needs to find *contradictions* before students do
- A retirement process needs to know *what replaces what*
- An AI consumer needs to know that an example *illustrates* a claim rather than *proving* it

And relationships stored casually rot: bidirectional copies drift, links point at retired objects, prerequisite chains silently become circular. The model below prevents each failure by rule rather than vigilance.

---

## FOUR PRINCIPLES

**P1 — Typed only.** Every relationship SHALL use a vocabulary type defined here. Free-form predicates are prohibited; if a needed type is missing, it is added to this specification first (cheap: a list extension, not an ADR — but deliberate).

**P2 — One direction stored, the knower stores it.** Every relationship SHALL be stored on exactly one side — the object that *cannot be fully understood without the other*, which is almost always the dependent, composed, or newer object. Inverses (`required-by`, `embedded-in`, `superseded-by`) exist only as derived views, never as stored data. Two stored copies of one fact always drift; one copy cannot disagree with itself.

**P3 — Context lives in the relationship.** Where a relationship carries context — an embed's lead-in, a path step's "why this, why now" — that context is stored *with the relationship*, never inside the target object (KA-1.0 R2). This is what keeps cards reusable.

**P4 — Relationships pass the value filter.** A relationship type earns its place only by improving publishing, reuse, search, or AI consumption (EOS-002's filter). This vocabulary is deliberately small; "nice to model" is not a reason.

---

## THE VOCABULARY

Four families, seventeen types. Each entry: **stored on → points to**, cardinality, meaning.

### Family 1 — Structural (composition)

These implement "composed of" from EOS-002. Both carry ordering and MAY carry a context wrapper.

| Type | Stored on → points to | Cardinality | Meaning |
|---|---|---|---|
| `embeds` | Publication → Card | 1 pub : N cards; a card embedded by M pubs | The card's content appears inline in this publication. Wrapper: lead-in/lead-out prose. Order: position in the publication. |
| `sequences` | Learning Path → Publication or Card | 1 path : N steps; an object sequenced by M paths | The object is a step in this path. Wrapper: step framing ("why this, why now"). Order: step number. |

**Composition semantics:**
- A Publication SHALL embed ≥3 cards (EOS-002); a Path SHALL sequence ≥2 steps.
- **Derived evidence floor** *(resolves EOS-003 open question 3)*: a Publication or Path displays, for trust purposes, the **minimum evidence level among its load-bearing embedded/sequenced content**. It records no evidence of its own — it owns narrative, not claims. Its own connective prose that makes claims must either cite an embedded card or be extracted into one.
- **Review propagation:** reviewing a Publication SHALL include checking whether any embedded card is past `review_due`; a publication is not "fresh" while its load-bearing cards are stale.

### Family 2 — Semantic (knowledge ↔ knowledge)

| Type | Stored on → points to | Cardinality | Meaning |
|---|---|---|---|
| `requires` | later object → prerequisite | N : M | Consume the target first; this object assumes it. SHALL be acyclic. |
| `elaborates` | deeper object → base object | N : M | Goes deeper on the same concept. |
| `exemplifies` | example → claim/model | N : M | Concrete instance illustrating (not proving) the target. |
| `compares` | comparison object → each compared object | 1 : 2+ | Side-by-side decision content pointing at what it compares. |
| `contradicts` | either object → the other | N : M, symmetric in meaning | The two make incompatible claims. Existence of this link is an editorial alarm, not a resting state (see lifecycle rules). |
| `supersedes` | new object → old object | 1 : 1 per hop; chains allowed, SHALL be acyclic | This replaces that. Mandatory at retirement with a replacement (EOS-003 V7). |
| `extracted-from` | reference card → voice publication | N cards : 1 letter | The card distills a durable insight born in a letter or student voice (KA-1.0 Rule V2). |

### Family 3 — Domain (career guidance semantics)

| Type | Stored on → points to | Cardinality | Meaning |
|---|---|---|---|
| `requires-skill` | Career → Skill | N : M | The career needs this capability. Distinct from `requires` (reading order) — this is a capability requirement. |
| `develops-skill` | Card / Publication / Path → Skill | N : M | Consuming this content builds that skill. Powers "how do I build X?" surfaces. |
| `profiles` | Publication → Career | N pubs : 1 career (typically 1:1) | This publication is the in-depth treatment of that career. |
| `similar-to` | Career → Career | N : M | Careers a student weighing one should also see ("students also explored"). Stored once (on the object whose ID sorts first, to prevent double entry). |

### Family 4 — Planning (work and measurement)

| Type | Stored on → points to | Cardinality | Meaning |
|---|---|---|---|
| `contributes-to` | Task → Initiative | N tasks : 1 initiative | Every task serves exactly one initiative (EOS-002). |
| `depends-on` | Task → Task | N : M | Blocker ordering. SHALL be acyclic. |
| `affects` | Decision → Initiative or Task | N : M | The decision changes that work's direction or scope. |
| `measures` | Metric → Initiative | N metrics : 1 initiative | The metric tracks that initiative's outcome. |
| `produces` | Task or Initiative → knowledge object | N : M | The work delivered that object. The provenance link between planning and knowledge. |
| `includes` | Release → any object | 1 release : N objects; an object in M releases | Grouped into that versioned release. |

**Mapping from EOS-002 prose:** "contains" → `embeds`/`sequences`/`includes` by type; "is described in" → inverse of `profiles`; "supports" → `contributes-to`; "enables/owns" → `produces` (from the owning side, derived views give the rest).

---

## DIRECTION: WHO STORES WHAT (THE KNOWER RULE)

The stored side in every case above follows one principle:

> **The object that would be incomplete, unbuildable, or meaningless without the other stores the link.**

A publication is meaningless without its cards → it stores `embeds`. A card is complete alone → it stores nothing about who embeds it. The new version knows the old → `supersedes` lives on the new. The task exists to serve the initiative → `contributes-to` lives on the task. The extracted card knows its source letter → `extracted-from` lives on the card.

Derived inverse names (for rendering and queries only, never stored): `embedded-in`, `sequenced-in`, `required-by`, `elaborated-by`, `exemplified-by`, `compared-in`, `superseded-by`, `yielded` (inverse of extracted-from), `required-by-career`, `developed-by`, `profiled-in`, `supported-by` (initiative←tasks), `measured-by`, `produced-by`, `included-in`.

---

## LIFECYCLE INTERACTION RULES

What happens to relationships when objects change state:

| # | Rule |
|---|---|
| L1 | **Retirement:** an object SHALL NOT reach `retired`/`archived` while other objects' load-bearing links (`embeds`, `sequences`, `requires`) point at it — those links are first re-pointed (usually at its successor via `supersedes`) or consciously removed. Non-load-bearing links (`elaborates`, `similar-to`) may survive retirement; renderers follow the supersedes chain to the live head. |
| L2 | **Version bump:** links reference IDs, not versions, so they survive updates. The reuse registry (KA-1.1 area 4) — which is exactly the derived inverse index of `embeds`/`sequences`/renderings — becomes the update checklist for every surface. |
| L3 | **Contradiction:** a stored `contradicts` SHALL open an editorial resolution with a deadline of the shorter `review_due` of the two objects. If either object is `stakes: high`, both SHALL carry a visible caveat until resolved. Resolution ends in: one object corrected, one superseded, or the disagreement documented in both `uncertainty` fields as legitimate ("sources genuinely disagree"). |
| L4 | **Voice immutability:** `extracted-from` targets never change (letters are immutable, V9), so these links cannot rot. |
| L5 | **Dangling links:** a link whose target ID does not resolve is a validation **error**, not a warning. |

---

## VALIDATION RULES

Enforced at review now, by the KA-1.1 validation script later:

- **RV1** Every relationship type SHALL be from this vocabulary, and its from/to object types SHALL match the tables above.
- **RV2** Every target ID SHALL resolve to an existing object (L5).
- **RV3** No self-references.
- **RV4** `requires`, `depends-on`, and `supersedes` graphs SHALL be acyclic.
- **RV5** No stored inverses: the presence of both `requires` on A→B and any stored "required-by" on B→A is an error (P2).
- **RV6** A retired object with no `superseded-by` (derived) SHALL carry an explicit "no replacement" note (EOS-003 V7).
- **RV7** A Publication with fewer than 3 `embeds`, or a Path with fewer than 2 `sequences`, fails completeness.
- **RV8** `contradicts` without an open resolution note is an error (L3).

---

## STORAGE (MODEL LEVEL ONLY)

Relationships are stored **with the knower object's metadata** (the `relationships` list, EOS-003 1.12). A **central derived index** — regenerated, never hand-edited — provides inverse lookups and powers the reuse registry. This gives one answer to the two open storage questions (KA-1.1 q3 and q4): *front matter is the source of truth; the registry is a build artifact; the surface author who creates a dependency records it, and the index makes it visible to everyone else.*

Representation details (file format of the index, generation tooling) are Phase 2 concerns.

---

## EXAMPLES (REAL OBJECTS)

**Already live in the retrofitted cards:**

```
five-communication-competencies   requires    → communication-competency-definition
communication-salary-premium      requires    → communication-competency-definition
communication-readiness-checklist requires    → five-communication-competencies
communication-salary-impact-bps   exemplifies → communication-salary-premium
```

Derived views this yields with zero extra authoring: the definition card's page can show "built on by 2 cards" (`required-by`); the salary-premium card shows its worked example (`exemplified-by`); a path builder knows the checklist cannot be step 1.

**Domain family, once Careers/Skills objects exist:**

```
career:bps            requires-skill → skill:communication
career:bps            similar-to     → career:business-analyst
publication:bps-guide profiles       → career:bps
publication:bps-guide embeds         → communication-salary-impact-bps
                                       (wrapper: "Here is what this is worth
                                        in rupees, in this exact industry:")
kcard:five-communication-competencies develops-skill → skill:communication
```

**Voices extraction, when the first letter ships:**

```
kcard:marks-obsession-trap (MINDSET)  extracted-from → letter:2026-08-what-a-parent-asked-me
```

**Planning provenance:**

```
task:write-communication-cards  contributes-to → initiative:skills-domain-coverage
task:write-communication-cards  produces       → [the five ENA-KCARD-SKILL-* ids]
```

---

## DESIGN DECISIONS

**D1 — One-direction storage with derived inverses.**
*Alternative:* store both directions for query convenience. *Rejected:* every bidirectional store eventually disagrees with itself; the derived index gives the same query power with one source of truth. *Cost:* inverse queries need the index — acceptable, it's a build artifact.

**D2 — Small controlled vocabulary (17 types).**
*Alternatives:* free-form predicates (maximum expressiveness, zero queryability — rejected); a large ontology (SKOS/schema.org-style — rejected as bureaucracy that authors won't use correctly). *Trade-off:* some nuance is lost ("inspired-by" isn't expressible); the value filter says that's fine until a surface needs it.

**D3 — `requires` (reading order) split from `requires-skill` (capability).**
The pilot cards used `requires` for prerequisites; careers need capability semantics. One overloaded type would make "what must I read first?" and "what must I be able to do?" indistinguishable to a path builder — the two questions a guidance site most needs to keep apart.

**D4 — `contradicts` as a first-class alarm.**
*Alternative:* handle contradictions purely editorially, off the record. *Rejected:* undocumented contradictions are exactly how a growing knowledge base lies to students by accident. Making the link storable makes the problem findable; L3 makes it terminating.

**D5 — Composition carries context; targets stay clean.**
Already law (KA-1.0 R2); restated here because embeds/sequences are where it will be tested daily.

**D6 — No relationship weights, strengths, or confidence scores.**
*Deferred:* recommendation engines may someday want them. Adding numbers nobody maintains is bureaucracy today; the value filter says no until a real consumer exists.

---

## TRADE-OFFS

| Chosen | Cost | Benefit |
|---|---|---|
| 17 types, closed list | Occasional "no type fits" moments | Every link is queryable and validatable |
| Knower-side storage | Inverse queries need a derived index | Zero drift; one source of truth |
| Acyclicity enforced (RV4) | Some legitimate mutual dependencies must be remodeled | Path building and prerequisite ordering always terminate |
| Contradiction tracking with deadlines | Editorial workload when found | The knowledge base cannot quietly disagree with itself on high-stakes content |

---

## FUTURE CONSIDERATIONS

- **EOS-005 (Planning as Code)** builds directly on Family 4 — GitHub Issues map onto Task/Initiative objects whose links are already defined here
- **KA-1.1 spec** formalizes the derived index (reuse registry) format and the validation script implementing RV1–RV8
- **Phase 2** may generate the index automatically from front matter; **Phase 4** AI retrieval consumes typed links (an `exemplifies` target is context, not evidence — the type prevents an AI from citing an illustration as proof)
- **Weights/confidence** (D6) revisit when a recommendation surface exists

## QUESTIONS STILL OPEN

1. Should `compares` targets be ordered (the comparison's "primary" subject first), or is it unordered? Leaning unordered; the comparison publication owns its own framing.
2. `similar-to` tie-break (store on lexically-first ID) is a convention, not a semantic — is there a better home for genuinely symmetric relationships? Revisit if a second symmetric type appears.
3. Does `develops-skill` need a level qualifier (introduces vs. deepens)? Deferred under D6 reasoning until a skills-path surface exists.

---

## DOCUMENT HISTORY

| Version | Date | Change | Author |
|---------|------|--------|--------|
| 1.0 | 2026-07-13 | Initial model: 4 principles, 17-type vocabulary in 4 families, knower-rule direction, lifecycle rules L1–L5, validation rules RV1–RV8, composition semantics incl. derived evidence floor (closes EOS-003 open q3), single-answer storage decision (front matter + derived index) closing KA-1.1 open qs 3–4 | Chief Knowledge Architect |
