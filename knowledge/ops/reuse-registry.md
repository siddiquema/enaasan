# Reuse Registry

The manual `used_by` index required by OPS-001 §6.3: every surface that embeds or renders a knowledge object is recorded here, **by whoever creates the dependency** (the surface author). When an object's version increments, its rows below are the update checklist — the object is not "done updating" until every listed surface is refreshed or consciously deferred (EOS-004 L2).

Format: one row per (object → surface) dependency. `Mechanism` per EOS-004: embed / sequence / rendering / link.

| Object (canonical ID) | Version in use | Surface | Mechanism | Status | Recorded |
|---|---|---|---|---|---|
| ENA-KCARD-SKILL-communication-competency-definition | 1.0 | ENA-GUIDE-CAREER-communication-skills-guide (Part 1) | embed | draft | 2026-07-14 |
| ENA-KCARD-SKILL-five-communication-competencies | 1.0 | ENA-GUIDE-CAREER-communication-skills-guide (Part 2) | embed | draft | 2026-07-14 |
| ENA-KCARD-SKILL-communication-salary-premium | 1.0 | ENA-GUIDE-CAREER-communication-skills-guide (Part 3) | embed | draft | 2026-07-14 |
| ENA-KCARD-SKILL-communication-salary-impact-bps | 1.0 | ENA-GUIDE-CAREER-communication-skills-guide (Part 3) | embed | draft | 2026-07-14 |
| ENA-KCARD-SKILL-communication-readiness-checklist | 1.0 | ENA-GUIDE-CAREER-communication-skills-guide (Part 4) | embed | draft | 2026-07-14 |
| ENA-GUIDE-CAREER-communication-skills-guide | 0.1 | /skills/communication website page | rendering | **planned** — see website integration plan (sprint log) | 2026-07-14 |
| ENA-GUIDE-CAREER-communication-skills-guide | 0.1 | bps.html (Tip 8 outbound link) | link | **planned** | 2026-07-14 |
| ENA-GUIDE-CAREER-first-job | 0.1 | /skills/first-job website page | rendering | **live** | 2026-07-14 |

**Maintenance rules:**
1. New dependency → new row, same commit as the surface change.
2. Card version bump → walk every row for that card; update "Version in use" only after the surface is actually refreshed.
3. A surface that is retired gets its rows deleted in the retiring commit.
4. This file is currently hand-maintained; the KA-1.1 validation script is expected to generate and check it later. Until then it is source-of-truth for "where is this used?"
