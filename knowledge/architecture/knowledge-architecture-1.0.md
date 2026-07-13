# Enaasan Knowledge Architecture 1.0 (KA-1.0)

**Status:** Draft for Review
**Version:** 1.0-draft
**Last Updated:** 2026-07-12
**Owner:** Chief Knowledge Architect
**Depends on:** EOS-001 (Philosophy), EOS-002 (Object Model)
**Amends (pending approval):** `document-id-standard.md`, `metadata-standard.md` (see §10)

---

## 0. WHAT THIS DOCUMENT IS — AND IS NOT

This is the **information architecture of Enaasan's knowledge**: what the knowledge domains are, where each piece of content canonically lives, and how one piece of content is reused across many student journeys without duplication.

**Relationship to other documents:**

- **EOS-001 / EOS-002** define the *grammar* — what a Knowledge Card, Publication, or Learning Path IS, for any implementation.
- **KA-1.0 (this document)** defines *Enaasan's floor plan* — how Enaasan's actual knowledge is organized using that grammar.
- **`knowledge-architecture.md`** (existing) describes the *repository layer* — folders, templates, standards. It remains valid; this document sits above it conceptually.

**This document is NOT:**

- Website navigation design (which links go in the nav bar)
- URL structure (`/after12` vs `/hubs/after12`)
- Homepage design
- Visual design or page layouts
- A migration plan for existing HTML pages

Those are application-layer decisions that will be *derived from* this architecture later. Getting this layer right first is what makes those decisions easy instead of contentious.

---

## 1. THE CENTRAL PROBLEM THIS SOLVES

The same piece of knowledge is needed in many places.

"Why communication skills command a salary premium" is relevant to:

- A 12th-grader choosing between streams (evidence that soft skills matter as much as marks)
- A BPS career guide reader (why some agents out-earn others in the same role)
- A graduate preparing for interviews (what to emphasize)
- A parent questioning whether "personality development" is worth anything

The naive solution — write it into each page — is what the site does today, and it fails predictably: four copies drift apart, corrections miss three of them, and translation costs quadruple.

The architecture below makes duplication *structurally unnecessary* through one central rule:

> **Knowledge is FILED by domain (what it's about) and SURFACED by facet (who needs it, when).**
>
> A piece of knowledge has exactly ONE home, chosen by subject matter. Audiences, life stages, hubs, and journeys never own content — they *reference* it.

Everything else in this document is elaboration of that rule.

---

## 2. THE TWO-AXIS MODEL

Every knowledge object in Enaasan is positioned on two independent axes:

**Axis 1 — DOMAIN (where it lives).** The subject matter. Every object has exactly one domain. This determines its canonical home, its owner, and its review cycle.

**Axis 2 — FACETS (how it's found).** Metadata describing who it serves, at which life stage, in which language, in what form, and in what register. An object can carry many facet values. Facets power hubs, search, learning paths, and AI retrieval.

```
                        FACETS (surfacing) →
                stage: after12   audience: student   lang: EN
                        ↓               ↓               ↓
DOMAIN          ┌─────────────────────────────────────────┐
(filing)        │                                         │
   ↓            │   One card, one home,                   │
skills ────────→│   surfaced into many contexts           │
                │                                         │
                └─────────────────────────────────────────┘
```

**Why two axes and not one:** A single hierarchy forces every object into one path (`after12 → skills → communication`), which breaks the moment a second audience needs it. Separating filing from surfacing means the filing never has to change when a new audience, hub, or journey appears.

---

## 3. THE FIVE CORE KNOWLEDGE DOMAINS

All Enaasan knowledge falls into five domains. Domains are deliberately few, mutually exclusive, and defined by the *question the student is asking*:

| # | Domain | The student's question | Examples |
|---|--------|------------------------|----------|
| **D1** | **PATHWAYS** | *"What can I study, and how do I get in?"* | Streams (PCM/PCB/Commerce/Arts), courses, entrance & state exams, institutions, eligibility, after-10th options, distance education |
| **D2** | **CAREERS** | *"What work exists, and what is it really like?"* | Career profiles (BPS, Data Scientist), sectors, roles, salaries, growth ladders, day-in-the-life, employer landscapes |
| **D3** | **SKILLS** | *"What capabilities do I need, and how do I build them?"* | Communication, analytical thinking, digital literacy — definition, why it matters, how to develop, how it's assessed |
| **D4** | **DECIDING** | *"How do I choose?"* | Decision frameworks, comparison content (B.Com vs BBA), decision traps, self-assessment, the 90-Day Plan |
| **D5** | **MINDSET** | *"How do I handle the pressure and the people?"* | Family expectations, marks obsession, failure and restarts, confidence, talking to parents, wellbeing during exam years |

### Boundary tests (adjacent-domain disambiguation)

When content seems to straddle domains, the deciding question is **what the student is trying to DO** when they need it:

| Content | Looks like | Actually belongs in | Why |
|---|---|---|---|
| "BPS analyst salary ranges" | Skills? Money? | **CAREERS** | Describes the world of work |
| "B.Com vs BBA compared" | Pathways? | **DECIDING** | Its purpose is choice-making; it *references* Pathways cards |
| "How to tell parents you don't want engineering" | Careers? | **MINDSET** | The difficulty is emotional/relational, not informational |
| "Which stream leads to law?" | Deciding? | **PATHWAYS** | Factual route information; no choice framework involved |
| "Communication skills salary premium" | Careers? | **SKILLS** | It's about the capability; careers are the evidence |

**Note on "money":** Salary data belongs to CAREERS; course fees and scholarships belong to PATHWAYS. Money is an attribute of those domains, not a domain itself. If financial-planning content grows substantially (education loans, earning while studying), it becomes a candidate for a sixth domain — via the ADR process, per EOS-002's freeze discipline.

**Note on parents:** "Parents" is an *audience facet*, not a domain. A card explaining stream choices *to parents* lives in PATHWAYS with `audience: parent`. Content about *handling* parental pressure lives in MINDSET. This distinction prevents an entire duplicate "parents' site" from growing in parallel.

---

## 4. THE FACET SYSTEM

Facets are controlled-vocabulary metadata. Every knowledge object carries them; hubs, paths, search, and AI retrieval query them.

| Facet | Values | Notes |
|---|---|---|
| **stage** | `after10` \| `after12` \| `college` \| `graduate` \| `early-career` | Multi-valued. The communication cards carry four of five |
| **audience** | `student` \| `parent` \| `educator` | Multi-valued. Replaces "pick exactly one audience" (see §10) |
| **language** | `en` \| `ta` \| `te` \| `hi` | Language variants of one object, not separate objects (EOS-001, Principle 7) |
| **category** | Card: `definition` \| `mental-model` \| `checklist` \| `faq` \| `framework` \| `reflection` \| `example` — Publication: `guide` \| `workbook` \| `playbook` \| `career-profile` \| `reference` \| `toolkit` \| `letter` \| `student-voice` | From EOS-002, extended with the two Voices categories |
| **register** | `reference` \| `voice` | See §5, Voices |

**Rule:** facet vocabularies are controlled (fixed lists, extended deliberately), never free text. Free-text tags may exist *additionally* for discovery, but nothing structural may depend on free-text tags.

---

## 5. OBJECT ROLES: HOW CARDS, PUBLICATIONS, PATHS, TOOLS, AND VOICES RELATE

The architecture uses the 10 frozen EOS-002 object types. Two things people will ask for — "Tools" and "Voices" — are deliberately NOT new object types. Here is each role:

### 5.1 Knowledge Card — the atom

- Lives in exactly **one domain** (its canonical home)
- Carries facets for every context it serves
- Contains **zero context-specific framing**. The card about salary premiums never says "as you saw earlier in this BPS guide…" — that sentence belongs to whoever embeds it (§7)

### 5.2 Publication — the molecule

- Composes 3+ cards **by reference** into a complete reading experience
- Has a **primary domain** (the BPS guide → CAREERS) but may embed cards from any domain (a SKILLS card, a DECIDING checklist)
- Owns its *narrative connective tissue*: introductions, transitions, context wrappers around embedded cards

### 5.3 Learning Path — the journey

- A **sequence** of publications and cards serving a specific stage + goal ("Interview-ready in 4 weeks", `stage: graduate`)
- Owns **no content** — only ordering, pacing, and step framing ("now that you've assessed yourself, see what the gaps cost in salary terms →")
- Paths are the primary mechanism by which one card serves *different journeys in different sequence positions*

### 5.4 Tools — interactive RENDERINGS, not objects

A "tool" (tappable checklist, self-scoring quiz, stream-picker) is an **application-layer rendering of an existing card or publication** — not a new content type.

- The 50-item communication checklist card (content) → rendered as an interactive scored checklist (tool)
- A future aptitude quiz → a rendering of Framework/Reflection cards
- **Test:** if the tool's questions/content were deleted, would knowledge be lost? If yes, that knowledge belongs in a card, and the tool renders it. The tool itself owns only interactivity (scoring logic, UI state)

This keeps the 10-object freeze intact and — more importantly — keeps tool content translatable, reviewable, and versioned like all other knowledge.

### 5.5 Voices — Publication categories with a special register

Newsletter-style letters and student contributions are **Publications** with `register: voice` and category `letter` or `student-voice`. Not a new object type, but governed by two special rules:

**Rule V1 — Timely vs. timeless split.** Reference content (register: `reference`) is maintained and re-reviewed forever. Voice content is **dated and immutable** — a July 2026 letter is a historical artifact; we don't re-review it annually. Its metadata carries a publication date instead of a review cycle.

**Rule V2 — The extraction rule.** When a letter produces a durable insight ("the marks-obsession trap"), that insight is **extracted into a Knowledge Card** in the appropriate domain (MINDSET), and the letter links to the card. The letter keeps its original prose; the card becomes the reusable, maintained version. Voice content is thus a *source* of knowledge, never a *home* for it.

### 5.6 Hubs — saved VIEWS, not objects

A hub (`after12`, `graduates`, `parents`) is a **query over facets plus a curated layer**:

```
hub(after12) = ALL objects WHERE stage=after12
             + editorial pinning (what to show first)
             + stage-specific framing text (owned by the hub page)
```

Hubs own no knowledge. When a new communication card is tagged `stage: after12`, the After-12 hub can surface it with zero changes to the card. This is what makes hubs cheap to add: a `college` hub next year is a new query + curation, not new content.

### 5.7 Glossary and FAQ — views, not silos

Same pattern, worth naming explicitly because both exist in the backlog:

- **Glossary** (WS-13) = the view of all `category: definition` cards across all domains. Not a separate list of terms to maintain.
- **FAQ** = the view of all `category: faq` cards. The 32 existing Q&As on `faq.html` are, structurally, 32 unrecognized FAQ cards; retrofitting them is a future task (consistent with `knowledge-architecture.md`'s retrofit note).

### The relationship picture

```
DOMAINS (5)          hold →  KNOWLEDGE CARDS (atoms, one home each)
                               ↑ embed (by reference + context wrapper)
                             PUBLICATIONS (molecules; incl. Voices w/ register:voice)
                               ↑ sequence (by reference + step framing)
                             LEARNING PATHS (journeys)

FACETS (stage/audience/language/category/register)
        power → HUBS, GLOSSARY, FAQ, SEARCH, AI RETRIEVAL   (views — own nothing)

APPLICATION LAYER renders any of the above → web page, PDF, TOOL (interactive), API
```

---

## 6. PLACEMENT RULES: WHAT BELONGS WHERE

The decision procedure for any new piece of content:

```
1. Is it a single reusable concept, fact, framework, or example?
      → KNOWLEDGE CARD. File in its domain (use §3 boundary tests). Done.

2. Is it a coherent multi-card reading experience on one topic?
      → PUBLICATION. Primary domain by subject. Compose cards by reference.
        Write only connective tissue as new prose.

3. Is it a goal + ordered sequence for a specific stage?
      → LEARNING PATH. Reference existing publications/cards. Write only step framing.

4. Is it interactive (scoring, branching, input)?
      → The CONTENT is a card (rule 1). The INTERACTIVITY is a tool rendering.
        Never bury knowledge inside tool code.

5. Is it timely, personal, or opinionated (a letter, a student's idea)?
      → VOICES publication (register: voice). Dated, immutable.
        Extract durable insights into cards (Rule V2).

6. Is it "everything a particular group needs"?
      → That's a HUB — a view. Tag the underlying objects with the right facets
        and curate. Create NO new content objects for it.
```

**Two hard rules that prevent architectural decay:**

**R1 — One canonical home.** Every card lives in exactly one domain. If a card seems to need two homes, either the boundary test (§3) resolves it, or it's actually two cards.

**R2 — Context lives in the relationship, not the object.** Any sentence that mentions the surrounding context ("in BPS specifically…", "before you take the quiz below…") belongs to the embedding publication/path/hub — never inside the card. This is the single discipline that keeps cards reusable. A card that has absorbed context from one home can no longer travel.

---

## 7. REUSE MECHANICS: THE THREE VERBS

There are exactly three ways content is reused. Each carries its own context wrapper, which is how the same card reads naturally in different settings without modification:

| Verb | Who uses it | What it means | Where context framing lives |
|---|---|---|---|
| **EMBED** | Publications | Card's content is included inline (transclusion) | The publication writes a lead-in/lead-out around the embedded card |
| **SEQUENCE** | Learning Paths | Card/publication is a step in an ordered journey | The path writes step framing ("why this, why now") |
| **SURFACE** | Hubs, glossary, FAQ, search, AI | Object appears in a filtered view via facets | The view writes its own headline/grouping; object is untouched |

In today's static-site reality, "embed" is implemented by hand (copy at build/authoring time with a comment pointing to the canonical source) until Phase 2 tooling exists. The *architecture* is what matters now: authors must know which copy is canonical and which is a rendering. The canonical source is always the file in `knowledge/`.

---

## 8. WORKED EXAMPLE: ONE COMMUNICATION CARD, FIVE SURFACES, ZERO DUPLICATION

Take the five communication cards created today (canonical home: **SKILLS domain**), specifically Card 3, *"Why Communication Skills Command a 20–30% Salary Premium"*:

**Facets:** `stage: [after12, college, graduate, early-career]` · `audience: [student, parent]` · `category: mental-model` · `register: reference` · `language: en`

| # | Surface | Mechanism | What that surface adds (context wrapper) | What changes in the card |
|---|---------|-----------|------------------------------------------|--------------------------|
| 1 | **BPS Career Guide** (CAREERS publication) | EMBED | Lead-in: "You saw in Tip 8 that communication is your most portable asset. Here is what it is worth in rupees, in this exact industry:" — then embeds the card's salary tables | **Nothing** |
| 2 | **After-12 Hub** (view) | SURFACE | Hub groups it under "Skills that decide your first salary" for `stage: after12` browsers | **Nothing** |
| 3 | **"Interview-Ready" Learning Path** (`stage: graduate`) | SEQUENCE | Step 3 of 5, framed: "You've self-assessed (step 2). Before you practice, understand what's financially at stake:" | **Nothing** |
| 4 | **Interactive readiness checker** (tool) | RENDERING of Card 4 (the checklist), which *links to* Card 3 in its results screen ("your gaps are costing you roughly this much →") | Scoring logic, UI | **Nothing** |
| 5 | **A future letter** ("What a Hyderabad BPS recruiter told me last week") | Voices publication *links to* the card as the evidence base; if the letter surfaces a new durable insight, it's extracted into a new card (Rule V2) | The letter's personal narrative | **Nothing** |

When the 2027 salary data arrives, **one file** is updated, its version increments, its `last_reviewed` date resets — and every surface above is correct again (automatically in Phase 2+; via a known, greppable canonical reference until then).

This is the architecture working as designed: the card never knew about any of its five contexts, and none of the five contexts own it.

---

## 9. MAPPING THE CURRENT SITE INTO KA-1.0

Nothing moves today. But every existing page now has a defined architectural identity, which tells us exactly how each will evolve:

| Existing page | Architectural identity | Domain | Evolution direction |
|---|---|---|---|
| `streams.html` | Publication (guide) | PATHWAYS | Decompose stream descriptions into definition cards |
| `after12.html` | Proto-hub mixed with content | PATHWAYS + view | Content → cards; page becomes the After-12 hub view |
| `after10.html` | Proto-hub mixed with content | PATHWAYS + view | Same as above |
| `state-exams.html` | Publication (reference) | PATHWAYS | Exam entries → cards (volatile data, short review cycles) |
| `careers.html` | Publication (reference) | CAREERS | Career blurbs → future Career objects + profile publications |
| `bps.html` | Publication (guide) — the richest on the site | CAREERS | Roles/ladders/tips → cards; page becomes composition |
| `faq.html` | FAQ view rendered statically | cross-domain | 32 Q&As → 32 `category: faq` cards |
| `90-day-plan.html` + PDF | Publication (workbook) | DECIDING | Already identified in `knowledge-architecture.md` |
| `guide.html` | Proto-hub | cross-domain | Absorbed by hub system |
| `index.html` | Application (router) | — | Not knowledge; belongs to website layer |
| New: `knowledge/publications/skills/communication/` | 5 cards, correctly domain-filed | SKILLS | First native KA-1.0 content — the pattern-setter |

---

## 10. AMENDMENTS REQUIRED TO EXISTING STANDARDS (PROPOSED, NOT EXECUTED)

KA-1.0 conflicts with three existing rules. Proposed resolutions, pending approval:

**A1 — `metadata-standard.md`: "pick exactly one audience."**
Replace with multi-valued `audience` and `stage` facets (§4). The old rule's intent (prevent unfocused writing) is preserved by a better mechanism: cards are focused by *atomicity*, not by audience-exclusivity. The guidance "if it serves two audiences it should be two documents" is exactly backwards for reusable knowledge and would have forced duplicating all five communication cards.

**A2 — `document-id-standard.md`: AUDIENCE code baked into every ID.**
`ENA-KCARD-GRAD-…` makes audience part of a card's permanent identity — but audience is a facet, and facets change (we WILL tag cards for new stages later; IDs must never change). Proposal:
- **Knowledge Cards:** domain code replaces audience code → `ENA-KCARD-SKILL-communication-salary-premium-v1.0`
- **Audience-targeted publications** (workbooks, letters written *for* someone): audience codes remain meaningful and stay
- Domain codes: `PATH`, `CAREER`, `SKILL`, `DECIDE`, `MIND`

**A3 — `publications/` folder layout is audience-first.**
Cards need domain homes. Proposal: `knowledge/publications/<domain>/…` for cards and domain-natural publications; the existing audience folders (`graduates/`, `parents/`…) remain valid for genuinely audience-targeted publications. The `skills/communication/` folder created today conforms to this proposal already. No existing file moves.

---

## 11. WHAT THIS ARCHITECTURE DELIBERATELY DEFERS

- **URL design and navigation** — application layer, decided after hubs are specified
- **Transclusion tooling** (automated embed rendering) — Phase 2; manual with canonical-source comments until then
- **Retrofitting existing HTML content into cards** — incremental, per-page decisions, never a big-bang migration
- **A sixth domain for money/financial planning** — revisit via ADR if that content area grows
- **Recommendation/personalization logic** — application layer consuming facets; nothing to design here yet

---

## 12. QUESTIONS STILL OPEN

1. **Hub curation weight** — is a hub 90% query + 10% pinning, or heavily hand-curated? Affects how much editorial effort each hub costs. Recommend: start heavily curated (quality), automate later (scale).
2. **MINDSET vs DECIDING boundary** — decision *traps* (#66) have both emotional and framework aspects. Current ruling: traps are DECIDING (they're about the choice process); pressure/family content is MINDSET. Revisit if it chafes in practice.
3. **Voices naming** — "Voices" is a working label for the register + its categories; the public-facing name is a branding decision, out of scope here.
4. **Student-voice consent policy** — required before the first `student-voice` publication; belongs in `standards/`.
5. **Translation scope per facet** — do `voice`-register publications get translated at all, or stay in their original language as artifacts? Leaning: letters stay original-language; extracted cards get translated.

---

## DOCUMENT HISTORY

| Version | Date | Change | Author |
|---------|------|--------|--------|
| 1.0-draft | 2026-07-12 | Initial architecture: two-axis model, five domains, facet system, object roles (incl. Tools-as-renderings, Voices-as-register, hubs-as-views), placement rules, reuse verbs, communication-cards worked example, current-site mapping, standards amendments A1–A3 | Chief Knowledge Architect |
