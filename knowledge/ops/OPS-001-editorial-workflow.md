# OPS-001: Editorial Workflow

**Series:** Operational Standards (OPS)
**Status:** Draft for Review
**Version:** 1.0
**Last Updated:** 2026-07-14
**Owner:** Founder / Editor-in-Chief
**Conforms to:** Enaasan Knowledge Standard v1.0 (EOS-001–004), LEARNING_PHILOSOPHY v1.0, KA-1.0

---

## 0. WHAT OPS IS — AND HOW IT DIFFERS FROM EOS

**EOS defines what knowledge IS.** Objects, metadata, relationships. Designed to be stable for a decade.

**OPS defines how work FLOWS.** Who does what, in what order, on what cadence. Allowed — expected — to change as the team, tooling, and volume change. An OPS revision is routine; an EOS revision is an event.

OPS documents SHALL conform to EOS; EOS SHALL never depend on OPS. If this workflow ever conflicts with the metadata contract or the Learning Philosophy, the workflow is wrong.

**Honest scale note:** today Enaasan is one founder plus an AI assistant. This workflow is written for that reality — roles below are *hats, not headcount* — while defining the seams where contributors can plug in later without redesign.

---

## 1. THE PIPELINE AT A GLANCE

```
IDEA ──→ TRIAGE ──→ DRAFT ──→ REVIEW ──→ PUBLISH ──→ MAINTAIN ──→ RETIRE
         (worth          (author       (reviewer      (surfaces     (review_due    (supersedes,
          making?)        hat)          hat)           + registry)   queue)         re-point links)
```

Each stage below defines: entry condition, the work, exit condition, and where it's tracked.

---

## 2. STAGE 1 — IDEA INTAKE

**Sources, in priority order:**

1. **Student signals** — questions submitted (WS-16 when built), search queries that found nothing, FAQ gaps
2. **Voices extraction** — durable insights inside letters and student contributions (KA-1.0 Rule V2; `extracted-from`)
3. **Domain gap analysis** — domains or stages with thin coverage (today: MINDSET and DECIDING have zero cards)
4. **The existing GitHub backlog** — content-labeled issues
5. **Founder/contributor observation** — stigma, misinformation, or confusion seen in the wild

**Tracking:** every idea that survives 30 seconds of thought becomes a **GitHub issue** with label `content`, plus the domain as a label (`pathways` / `careers` / `skills` / `deciding` / `mindset`). GitHub Issues is the idea queue; the knowledge repo holds only work that has entered drafting. Ideas are cheap and issues are cheap — the filter comes next.

---

## 3. STAGE 2 — TRIAGE (THE WORTH-MAKING TEST)

**Cadence:** weekly, 30 minutes, all new `content` issues at once.

Each idea is tested against the Learning Philosophy card-worthiness test (LP §2), asked as four blunt questions:

1. **Which student, at which decision or fear?** (No named moment → reject or park)
2. **Who answers this today?** (If a good honest answer already exists and ranks — link to it instead; we fill gaps, not the internet)
3. **Will it be needed in more than one place?** (One-context content → it's prose on that page, not a card)
4. **Will we re-verify it on schedule?** (Not willing → don't create it; a stale card is worse than none)

**Triage outcomes** (recorded on the issue):

| Outcome | Meaning |
|---|---|
| `accepted:card` / `accepted:publication` | Enters the drafting queue with domain + rough stakes noted |
| `accepted:letter` | Timely/personal — routed to the Voices stream, not the reference pipeline |
| `parked` | Real but not now (thin audience today, seasonal, blocked) — revisit quarterly |
| `rejected` | Fails the test; issue closed with one honest sentence why |

**Exit condition:** an accepted issue names the object type, domain, target stage(s), and the student moment it serves — which is 4 of the 9 authored fields before drafting begins.

---

## 4. STAGE 3 — DRAFTING

**Who:** the author (owner-to-be). AI assistance is normal and encouraged; the named human owner answers for every claim regardless (LP §5, metadata `owner` rule).

**The work:**

1. Start from [`AUTHOR_TEMPLATE.md`](../templates/AUTHOR_TEMPLATE.md) — the 9 authored fields — plus the matching body template from `templates/`
2. Write the body per the standards in `standards/` and the brand voice in `branding/`
3. Propose `evidence` honestly (the template teaches the two over-claiming traps the pilot caught) and write real `evidence_notes` — named sources, not "research shows"
4. Write `uncertainty` using the per-category starters
5. Declare typed `relationships` to existing objects (EOS-004 vocabulary)
6. Self-check against the review gate before requesting review — the author runs the same checklist the reviewer will

**Budget expectation:** metadata 5–10 min (pilot-validated); body per its type's standard. If metadata takes longer than the body, the concept probably isn't atomic — go back to triage.

**Exit condition:** status `draft → review`; the draft lives in its domain folder in `knowledge/publications/`.

---

## 5. STAGE 4 — REVIEW (THE GATE)

**Who:** the reviewer hat. **Solo-operator rule:** the same person MAY wear both hats, but never in the same sitting — a minimum **48-hour cooling period** between finishing a draft and reviewing it. The pilot proved even careful authors over-claim evidence and under-rate stakes; distance is the cheapest reviewer we have. When a second person exists, author ≠ reviewer becomes mandatory.

**The review has two halves:**

**A. Content review** — is it true, honest, and ours?
- Facts spot-checked against the named sources in `evidence_notes`
- Tone per `branding/` (honest, plain, Indian English, no false certainty)
- Title-honesty check (a title may not promise more than the content delivers)
- Reads correctly for the actual reader (first-generation student, on a phone)

**B. The metadata gate** (per `metadata-standard.md`, R8 — mechanical, checklist-driven):
1. Confirm `stakes` (adversarially — what's the real blast radius if wrong?)
2. Confirm `evidence` by the weakest load-bearing claim
3. Check `outcome` is capability-phrased; `uncertainty` present where V1/V3 require
4. Verify `relationships` resolve to real, current IDs (RV1–RV5 by hand until the validation script exists)
5. Set `last_reviewed`; `review_due` follows from the stakes × volatile table; raise `maturity` only if criteria met

**Outcomes:** approve (→ publish), or return to draft with specific findings. A return is normal, not a failure — the pilot returned 2 of 5 evidence ratings.

**SLA:** review requested → completed within **7 days**, or the requester escalates (today: to the calendar; later: to the editor).

---

## 6. STAGE 5 — PUBLISHING

Publishing is mechanical by design — every judgment already happened.

**Checklist (in order):**

1. Status → `published`; visibility derives to `public`; version → 1.0 (first publication) or increments per versioning-standard
2. **Surfaces:** render/embed onto the target page(s), each rendering carrying its canonical-source comment (`<!-- canonical: ENA-… -->`)
3. **Reuse registry:** record every surface that now uses the object (the manual `used_by` list until KA-1.1 tooling; the surface creator records the dependency — the agreed convention)
4. **Site plumbing** (when a website surface changed): sitemap entry if a new page, IndexNow fires via the existing GitHub Action, i18n keys if the surface is translated UI
5. **Relationships:** any `supersedes` link takes effect — the superseded object's surfaces get re-pointed (EOS-004 L1)
6. Commit with a `feat(knowledge):` message naming the object IDs

**Exit condition:** the object is live, findable, and every place it appears is recorded.

---

## 7. STAGE 6 — MAINTENANCE (EVIDENCE KEPT ALIVE)

This is where most knowledge systems quietly die; the cadences below are the countermeasure.

**7.1 The review queue.** `review_due` is computed (stakes × volatile), so the maintenance workload is a *queryable list*, not a memory. **Cadence: monthly, first week** — pull everything due in the next 60 days, re-verify each against its named sources, update `last_reviewed`, bump version if content changed.

**7.2 Re-verification means the named sources.** `evidence_notes` names what a card rests on; re-verification means re-pulling those sources. If a source is dead or superseded: replace it, or demote `evidence` and add the gap to `uncertainty`. Evidence maintenance is why sources are named, not gestured at.

**7.3 Season-aligned sweeps** (Enaasan-specific, and more important than the calendar cadence): high-stakes volatile content is verified **before the season students act on it** —

| Sweep | When | Content |
|---|---|---|
| Results/admissions sweep | April–May | Stream criteria, cutoff mechanics, admission processes, after-10th/after-12th pages |
| Exam-notification sweep | September–October | State exams, entrance exam patterns, eligibility |
| Salary-data sweep | January | Salary ranges, hiring trends across careers/skills content |

A student acting on our content during the season it matters is the whole point; that's when it must be freshest.

**7.4 Demotion and staleness.** Overdue high-stakes content: 30-day grace, then `maturity` demotes and the surface SHOULD show a "being re-verified" caveat — visible honesty over silent staleness (LP §4).

**7.5 Feedback intake.** Report-an-issue links (backlog WS-05/#71) route to GitHub issues labeled `correction`; corrections jump the review queue. A confirmed student-reported error is the highest-priority editorial work there is.

---

## 8. STAGE 7 — RETIREMENT

Per EOS-004 L1 and the philosophy's "knowledge retires visibly":

1. Confirm replacement: `supersedes` on the successor, or an explicit "no replacement" note
2. Re-point all load-bearing links (`embeds`, `sequences`, `requires`) using the reuse registry as the checklist
3. Status → `retired`; the historical file stays (git history is the archive); any live URL redirects or banners to the successor
4. The retirement is a commit, not a deletion

---

## 9. ROLES (HATS, NOT HEADCOUNT)

| Hat | Owns | Today worn by |
|---|---|---|
| **Editor-in-Chief** | Triage decisions, the review gate, maturity raises, this workflow | Founder |
| **Author/Owner** | Drafting, evidence honesty, maintenance of owned objects | Founder + AI assistance |
| **Reviewer** | The gate (§5), adversarial stakes/evidence confirmation | Founder (48h cooling rule) |
| **Translator** *(future)* | Language variants + per-language review dates | — (workflow: OPS candidate) |
| **Voices curator** *(future)* | Student submissions, consent, extraction | — (blocked on consent policy — OPS-002 candidate) |

Seams for growth are already in the model: a new contributor gets the AUTHOR_TEMPLATE and an assigned domain; the gate doesn't change, only who sits on each side of it.

---

## 10. CADENCE SUMMARY

| Rhythm | Activity |
|---|---|
| Weekly (30 min) | Triage new `content` issues |
| Monthly (first week) | Review queue: everything due within 60 days |
| Monthly | One Voices letter (sustainable floor; number them, don't date-pressure them) |
| Quarterly | Parked-ideas revisit; process metrics check (§11); KA/OPS doc review |
| Seasonal | The three sweeps (§7.3) |

## 11. PROCESS METRICS (MEASURING THE WORKFLOW, NOT THE STUDENTS)

- **Review debt:** count of objects past `review_due` — the single most honest health number; target: zero high-stakes overdue, ever
- **Time-in-review:** request → completion; target ≤ 7 days
- **Triage honesty:** rejected ÷ total ideas — if nothing gets rejected, the test isn't being applied
- **Correction latency:** student-reported error → fix published

---

## 12. WHAT OPS-001 DELIBERATELY EXCLUDES

- **Planning/roadmap process** (initiatives, quarterly goals, GitHub issue taxonomy beyond `content`) — future OPS-002/003 candidate
- **Student-voice consent policy** — its own OPS document, prerequisite before the first `student-voice` publication
- **Translation workflow** — own OPS document when Telugu localisation (WS-17/#81) starts
- **Publishing automation** (transclusion, PDF/DOCX generation) — Phase 2+ tooling; this document describes the manual process that tooling will later absorb
- **Website deployment mechanics** — unchanged, documented in `docs/`

---

## QUESTIONS STILL OPEN

1. Is the 48-hour cooling period enough distance for solo self-review, or should high-stakes content additionally require an external spot-check (a domain-knowledgeable friend) before publication?
2. Should `parked` ideas expire (auto-close after two quarterly revisits) to keep the queue honest?
3. When contributors arrive: do they draft in branches/PRs (review = PR review) or in the drafts folder? Leaning PRs — the review gate maps cleanly onto PR review — but deciding now would be designing for a team that doesn't exist yet.

---

## DOCUMENT HISTORY

| Version | Date | Change | Author |
|---------|------|--------|--------|
| 1.0 | 2026-07-14 | Initial workflow: 7-stage pipeline, worth-making triage test, solo-operator review gate with cooling period, publishing checklist, evidence maintenance with season-aligned sweeps, retirement procedure, hats-not-headcount roles, process metrics | Founder / Chief Knowledge Architect |
