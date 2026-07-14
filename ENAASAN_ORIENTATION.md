# Enaasan: Orientation & Status

**Last updated:** 2026-07-14  
**Phase:** Content Sprints (Architecture frozen at v1.0)  
**Status:** Live, operating under the Enaasan Knowledge Standard v1.0

---

## What Is Enaasan?

Enaasan is an **original educational platform** built to close the information asymmetry that keeps talented students from making better decisions about their futures.

**The core problem we solve:** Indian high school and college students are told what to do — "study harder," "get better marks," "improve soft skills" — without being given the reasoning, evidence, or uncertainty that would let them judge for themselves whether the advice is right *for their situation*.

**Our approach:** Every piece of guidance Enaasan publishes includes:
1. **Reasoning** — why this matters
2. **Evidence** — what we know and how we know it
3. **Uncertainty** — what we don't know, what varies, what you must verify yourself

We publish this as **Knowledge Cards** (the smallest reusable unit), composed into **Publications** (like guides), surfaced on the website as **spokes** (focused pages), all powered by a **reuse infrastructure** that means one card can serve multiple audiences without being rewritten.

**In practice today:** We have five published Communication Skills Knowledge Cards, a draft guide composing them, and a website integration plan ready to build. The reference examples are done; we're now proving the system works at scale.

---

## Where We Stand

### What's Live (Reference Collection v1.0 — 2026-07-14)

**Five published Knowledge Cards on Communication Skills:**

1. **Definition** (v1.0) — What communication competency actually is (4 dimensions, distinct from English fluency)
2. **Framework** (v1.0) — The 5 competencies employers assess (active listening, clarity, emotional intelligence, persuasion, adaptability)
3. **Salary Premium** (v1.0) — Why communication commands 20–30% higher salary (organizational research + our modeling, verified against originals)
4. **Readiness Checklist** (v1.0) — 30-item self-assessment with scoring and a 3-month development plan
5. **Worked Examples** (v1.0) — Three illustrated career scenarios (agent, analyst, team lead) showing the premium in rupees over time

**Maturity:** All `seed` level (the lowest rung on the earned ladder; they will graduate only through real usage and feedback). All have passed the adversarial review gate and source verification. They are the reference examples for every future Knowledge Card.

### What's in Progress (Sprint 1: Communication Skills)

**Communication Skills Guide** (v0.1, draft):
- Embeds all five cards in teaching order (define → assess → value → illustrate → self-assess)
- Contains only connective narrative; zero card content is duplicated
- Awaits its own review gate (48h cooling from 2026-07-14)
- Will publish at v1.0 once gated

**Website Integration Plan (prepared, not yet built):**
- `/skills/communication/` spoke page — renders the Guide, not raw cards
- Design: existing dark-navy/gold system, navigation parity, i18n hooks
- Answer capsule (TL;DR), Article JSON-LD schema, interactive checklist tool (phase 2)
- Links in: bps.html Tip 8, site-wide footer, careers.html skills mention
- Sitemap + IndexNow on ship

**Reuse Registry** (live):
- Seven entries: five embeds (guide) + two planned surfaces
- First operational instance of the Knowledge Reuse discipline
- Version bump → update checklist (mandatory or consciously deferred)

### What's Paused (Per EIC Directive)

No new cards are being authored until the first Publication → Website Surface cycle completes. Backlog candidates (daily-practice playbook, interview communication, English-vs-communication FAQ, parents' role) remain available but are not in progress.

---

## Our Standards & Philosophy

### The Foundation: Learning Philosophy v1.0

Eleven foundational commitments that justify every structural decision:

1. **Closing the information asymmetry** — students deserve the same honest information privileged families have
2. **The decision-usefulness test** — content must serve a real student decision or fear, not just explain a topic
3. **Timely vs. timeless honesty** — some insights are durable (reference); others are of-the-moment (voices/letters); confusing the two is a lie
4. **Honesty over encouragement** — we say what's true, not what's comforting
5. **Say how we know it** — evidence and sources are visible; methodology is transparent
6. **No false certainty** — uncertainty is disclosed; the student judges risk themselves
7. **Language equity** — every page, every card is in the student's actual language (not dumbed down, not academic)
8. **Review rhythm matched to decay** — knowledge goes stale; we re-verify on a schedule tied to how fast it ages
9. **Earned maturity** — content earns credibility through real usage, not polish; maturity is demotable
10. **Public corrections** — when we're wrong, the correction is visible; history is kept; we don't hide errors
11. **Knowledge should increase agency, not dependence** — the student who outgrows us is our success, not our failure

**The three-part rule (core to everything we do):**  
Every piece of advice ships with reasoning, evidence, and uncertainty attached. Advice stripped of these is an instruction, and we do not publish instructions for other people's lives.

### The Knowledge Standard v1.0 (Frozen)

**EOS-001: Philosophy** — Knowledge as Code methodology; 10 design principles; technology-independent; designed for 10-year stability.

**EOS-002: Object Model** — 10 first-class object types (frozen, never to expand):
- Knowledge objects: Knowledge Card, Publication, Learning Path, Career, Skill
- Planning objects: Initiative, Task, Decision
- Measurement: Metric, Release

Each with Purpose, Outcome, and a defined lifecycle. Object Categories allow specialization (card: definition/mental-model/checklist/FAQ/framework/reflection/example) without creating new types.

**EOS-003: Universal Metadata Contract** — Every object carries 24 fields (16 core + 8 knowledge-specific):
- Authored by contributors: 9 fields (title, description, purpose, outcome, stage, audience, evidence, evidence_notes, uncertainty)
- Set at review: stakes, volatile, maturity, relationships
- Derived automatically: visibility, updated, review_due, register, language, etc.

Every field traces to a Learning Philosophy commitment. No field without a commitment; no commitment without a mechanism.

**EOS-003.1: Retrofit Pilot** — Verified the contract on real content (the five communication cards). Extracted nine calibration rules that are now operational standards for every future card.

**EOS-004: Relationship Model** — 17 typed relationships in 4 families:
- Structural: embeds, sequences (with context wrappers)
- Semantic: requires, elaborates, exemplifies, compares, contradicts, supersedes, extracted-from
- Domain: requires-skill, develops-skill, profiles, similar-to
- Planning: contributes-to, depends-on, affects, measures, produces, includes

One direction stored (the knower stores it); inverses derived. No relationship drift because there's no place for it to happen.

**OPS-001: Editorial Workflow** — The operational process:
1. **Idea intake** (GitHub Issues, labeled by domain)
2. **Triage** (weekly, 30 min: worth-making test as four blunt questions)
3. **Drafting** (author hat; uses AUTHOR_TEMPLATE; 5–10 min metadata + body)
4. **Review gate** (reviewer hat; 48h cooling period minimum; adversarial stakes/evidence confirmation)
5. **Publishing** (mechanical: canonical comments, reuse registry, sitemap/IndexNow)
6. **Maintenance** (monthly review queue + season-aligned sweeps: April–May results, Sep–Oct exams, January salary)
7. **Retirement** (visible: supersedes link or "no replacement" note)

### Knowledge Architecture 1.0

**Two-axis model:**
- **Domain axis (filing):** Where knowledge lives permanently — one of five domains (Pathways, Careers, Skills, Deciding, Mindset)
- **Facet axis (surfacing):** How knowledge is discovered — stage (after10, after12, college, graduate, early-career) + audience (student, parent, educator) + language + category + register

**One card, many surfaces:** The communication-salary-premium card serves five different hubs via facet filtering — zero duplication, zero sync problems.

**Three reuse verbs:**
- EMBED (publications transclude cards with context; e.g., the Communication Skills Guide)
- SEQUENCE (paths order objects with step framing; e.g., a learning path steps through cards)
- SURFACE (hubs render objects by facet query; e.g., "all communication content for after-12 students")

---

## What's Pending

### Next (Necessary to Complete Sprint 1)

- [ ] **Guide review gate (after 48h cooling)** → publish Communication Skills Guide v1.0
- [ ] **Build `/skills/communication` website page** → first spoke; renders the guide; canonical references; reuse registry entries live
- [ ] **Verify page plumbing** — sitemap entry, IndexNow, internal links (bps.html Tip 8, footer, careers.html)

### After Sprint 1 (Blocked Until First Cycle Completes)

- [ ] **Card 4 as interactive tool** — phase 2 of the `/skills/communication` page (client-side scored checklist per KA-1.0 §5.4)
- [ ] **Content translation workflow** — TA/TE/HI translations of the Reference Collection (OPS-002 candidate: will require translation-specific OPS)
- [ ] **Student-voice consent policy** — prerequisite for launching the Voices section (letters, student contributions; OPS-002 candidate)
- [ ] **Next-wave card ideas in backlog** (ready for triage when Sprint 1 closes):
  - Daily-practice playbook (how to practice communication daily)
  - Interview communication (checklist)
  - English fluency vs. communication (FAQ)
  - Parents' role (guide for parents supporting a student)

### Architecture (No Changes During Freeze; Evidence Only)

Six friction observations logged in the sprint log (F1–F6), all at the edges:
- **F1 — Citation rot:** 2022 sources became unreachable in ~3 years; an evidence vault (archived copies at citation time) is worth future discussion
- **F2 — Verification-pending state:** Tooling reach forced removal of probably-true-but-unverifiable claims; a holding state was tempting but rejected
- **F3 — ID standard tension:** Publications filed by domain but carrying audience codes in their IDs; livable but awkward
- **F4 — Derived evidence floor judgment:** Which embeds are "load-bearing" for publication evidence rating is not fully specified; resolved by judgment + notes
- **F5 — Volatile inheritance:** Publications inherit `volatile` from volatile embedded cards; an implication, not a stated rule
- **F6 — Memory verification:** PMI "one-third" misquote survived authoring and two review passes; source verification caught it

None of these warrant standards changes during the freeze. They are evidence for future architectural review.

---

## What We're Trying to Achieve Now

### This Sprint (Proving the Lifecycle Works)

**Objective:** Validate that the Enaasan Knowledge Standard v1.0 can successfully support the complete lifecycle of **Knowledge Card → Editorial Review → Publication → Website Surface → Reuse**, end to end, with no standards changes and only friction logging.

**Success criteria:**
- Five reference-quality Knowledge Cards published and live
- First Publication composed, gated, and published
- First website surface live and integrated
- Reuse registry tracking dependencies
- No architectural changes (only evidence recorded)

**Why this matters:** If this cycle works cleanly, the standards have earned the right to support the next hundred Knowledge Cards. If friction appears, we document it as evidence for future revisions, but we do not change the standards now.

### The Longer Arc (Next 12–24 Months)

**Phase 2 — Content at Scale:**
- Grow the SKILLS domain (communication is 1 card cluster; 4–5 more clusters planned: English proficiency, technical interviewing, leadership, emotional intelligence, time management)
- Build out remaining domains (PATHWAYS: stream-choice guides; CAREERS: company profiles; DECIDING: comparison frameworks; MINDSET: pressure, resilience, career changes)
- Implement KA-1.1 enhancements (maturity criteria formalized, evidence tracking refined, semantic relationships, reuse registry automation)

**Phase 3 — AI & Tooling:**
- KA-1.1 validation script: automated checks for RV1–RV8 (relationship conformance, acyclicity, dangling links, completeness)
- Evidence vault: archived source documents at citation time (prevents citation rot)
- AI consumption: typed relationships enable next-generation AI consumers to distinguish exemplifies (illustration) from requires (prerequisite) from contradicts (alarm)

**Phase 4 — Platform & Scale:**
- Translations at scale (TA/TE/HI localisation per OPS-specific workflow)
- Interactive tools (Card 4 scored checklist as phase 2; future: career pathway simulators, skill trackers, learning path builders)
- Hub ecosystem (curated, saved facet views: "all communication content for after-12 students"; "all leadership skills"; "this semester's exam-prep content")
- Export/print: PDF guides, printable checklists, downloadable career PDFs

**Long-term vision:** Enaasan becomes a recognized, trusted, original knowledge platform for Indian student decision-making — not a content library, but a thinking tool. Every piece of guidance is traceable, updatable, reusable, and fair.

---

## Guiding Principles (Non-Negotiable)

1. **Architecture is frozen until proven.** Standards v1.0 stands; we prove it first; we change it second (with evidence).
2. **Editorial integrity is absolute.** Every load-bearing claim is verified against original sources. If unverifiable, removed. Never lowered.
3. **IP compliance is built in.** Original voice, proper attribution, minimal quotation, clear licensing. Write every artifact to a legal due-diligence standard.
4. **Reuse is the unit of work.** Not "write 50 cards"; "prove the reuse model works at scale." Quality over volume.
5. **The student is the audience.** Not "what's academically correct" but "what does this student need to decide better?" Clarity and honesty first.
6. **Maturity is earned, not assigned.** Cards start at `seed`; they graduate through real usage, real feedback, real evidence of student value.

---

## How to Navigate This Document

- **New to Enaasan?** Read: What Is Enaasan → Learning Philosophy → Knowledge Standard summary (EOS-001–004 titles)
- **Implementing a new card?** Read: OPS-001 Editorial Workflow → AUTHOR_TEMPLATE (in `/templates/`) → Editorial Calibration Baseline (9 rules)
- **Curious about the architecture?** Read: Knowledge Architecture 1.0 → EOS-004 Relationship Model → Friction Log (F1–F6)
- **Planning next phase?** Read: What's Pending → Guiding Principles → long-term vision section

---

## Key Files & Their Purpose

| File | Purpose |
|---|---|
| `knowledge/LEARNING_PHILOSOPHY.md` | The 11 commitments that justify every structural decision |
| `knowledge/eos/specifications/` | The frozen Knowledge Standard v1.0 (EOS-001–004) |
| `knowledge/architecture/knowledge-architecture-1.0.md` | Two-axis model, five domains, facet system, reuse mechanics |
| `knowledge/architecture/metadata-standard.md` | The YAML representation of EOS-003 (what fields, why) |
| `knowledge/templates/AUTHOR_TEMPLATE.md` | The 9 authored fields a contributor actually fills in |
| `knowledge/standards/editorial-calibration-baseline.md` | The 9 rules that caught real defects in real content |
| `knowledge/ops/OPS-001-editorial-workflow.md` | The 7-stage pipeline: idea → triage → draft → review → publish → maintain → retire |
| `knowledge/ops/sprint-logs/2026-07-communication-sprint.md` | Current sprint state: five cards published, first guide drafted, friction logged |
| `knowledge/ops/reuse-registry.md` | The `used_by` index: which surfaces use which cards (and the update checklist) |

---

## The Status in One Sentence

**Enaasan Knowledge Standard v1.0 is frozen and proven on the Reference Collection (five communication Knowledge Cards, one Publication, one website integration ready to build); we are now running the first full content sprint to prove the system scales cleanly before expanding to the next 100 Knowledge Cards.**
