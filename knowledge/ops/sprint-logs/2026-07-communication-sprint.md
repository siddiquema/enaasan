# Sprint Log — Communication Skills (Sprint 1)

**Started:** 2026-07-14
**Scope:** First content sprint under the frozen Knowledge Standard v1.0 + OPS-001. Doubles as the calibration exercise for the editorial standard — these five cards become the reference examples future contributors imitate.

---

## Stage 1 — Review gate on the five founding cards (2026-07-14)

Reviewer-hat pass per OPS-001 §5 (content review + metadata gate). Cooling period satisfied (drafted 07-12, reviewed 07-14). **All five cards returned findings — none passed clean.** That is the gate working, not the cards failing unusually; they were written carefully.

### Findings by card

**Card 1 (definition):** carried card 3's quantitative claim ("20-30% higher salary") beyond its own `expert-opinion` rating → softened to qualitative with a pointer. References claimed "primary research source" → corrected. The 4-dimensions vs 5-competencies split across cards 1–2 could read as self-contradiction → bridge note added.

**Card 2 (framework):** references presented the five-competency grouping as external fact; it is our synthesis → reworded to own it. Mini self-rating table now points to the full checklist instrument.

**Card 3 (mental model) — the serious catch:** the mechanism illustrations used an agent at ₹30 LPA and a supervisor at ₹50 LPA — **~10x reality, contradicting Enaasan's own published ladders on bps.html** (agents ₹1.8–4 LPA, TLs ₹4.5–8 LPA) — and the arithmetic itself was wrong (₹30 LPA ÷ 250 ÷ 8 ≈ ₹25/min, not ₹15). Sections rebuilt with realistic numbers. Section headers said "In dollars" over rupee math → fixed. **Evidence demoted secondary-research → expert-opinion:** postings analysis cannot isolate communication quality; the premium-by-level table is informed modeling, and it is load-bearing. Table caption now says so. 20-year projections added to uncertainty. `volatile: true` set; review_due 6 months.

**Card 4 (checklist):** scoring bands were mathematically incoherent (a student with 10✅/20⚠️/0❌ fit no row) → rebuilt as ✅-count-only bands out of 30, plus a zero-✅-section override. Relationship of the six sections to the five-competency framework now stated. References note the bands are heuristics, not psychometrics.

**Card 5 (example):** section headings still said "Real Example 1/2/3" for constructed composites → "Worked Example." The R3 in-body labeling requirement was unmet → composite callout added at the top. References now state no source contains these individuals. `volatile: true`; review_due 6 months.

**All cards:** body "Linked Cards" placeholder sections removed (typed relationships in front matter are the single source); status → `review`, version → 0.3; review_due recomputed from the stakes × volatile table (cards 1–2: low+stable = 24 months; card 4: medium+stable = 12; cards 3, 5: medium+volatile = 6).

### Awaiting EIC confirmation (the two adversarial calls per card)

| Card | Proposed stakes | Proposed evidence |
|---|---|---|
| 1 definition | low | expert-opinion |
| 2 framework | low | expert-opinion |
| 3 salary premium | medium | **expert-opinion** (demoted this pass) |
| 4 checklist | medium | expert-opinion |
| 5 worked examples | medium | anecdotal |

**EIC decision (2026-07-14):** Cards 1, 2, 4, 5 approved as proposed → **published, v1.0**. Card 3 **held** for an evidence-strengthening pass focused on organizational/workplace research rather than salary estimates.

**Card 3 strengthening pass (2026-07-14, v0.4):** load-bearing claims re-grounded in published organizational research (Grammarly/Harris Poll 2022, PMI Pulse of the Profession 2013, Watson Wyatt Communication ROI, LinkedIn/NACE demand rankings, India Skills Report + AMCAT employability reporting) via a new "What Organizational Research Shows" section; the premium table is now explicitly non-load-bearing illustration. Evidence re-rated `secondary-research` on that restructured basis. US studies labeled as US in body and uncertainty. Awaiting final EIC approval.

The nine calibration rules below were **approved by the EIC (2026-07-14)** as the initial baseline and promoted to `knowledge/standards/editorial-calibration-baseline.md`.

---

## Calibration rules extracted (the reference standard for all future cards)

1. **A card may not carry claims above its own evidence rating.** Quantitative claims live in the card that owns them; other cards point, qualitatively.
2. **Cross-surface consistency is part of fact-checking.** Numbers in a card must agree with what Enaasan already publishes (bps.html ladders); internal contradiction is a gate failure even when each number is individually defensible.
3. **Check the arithmetic.** Every worked calculation gets recomputed at review. Twice-wrong numbers (wrong premise AND wrong math) survived authoring and one retrofit pass.
4. **Data analysis can't prove what it doesn't observe.** If the source can't isolate the variable (postings don't label communicators), the derived table is modeling → expert-opinion, and the body says "modeled," not "based on analysis."
5. **Composites are labeled in the body, not just metadata** (R3) — the reader must see it, not just the system.
6. **Frameworks that coexist must be bridged** — two cards slicing one concept differently (4 dimensions / 5 competencies) need an explicit "two lenses, one thing" note or they read as contradiction.
7. **Scoring instruments must be checked as instruments** — bands must cover every possible score exactly once.
8. **"Linked Cards" body sections are dead** — typed relationships in front matter are the only relationship record; body prose may reference cards by ID inline where it helps the reader.
9. **Currency/idiom hygiene** — "In dollars" over rupee math is the kind of tell that erodes trust with the actual reader.

## Friction log (evidence for future architecture proposals — none proposed now)

- The stakes × volatile review_due table worked exactly as designed; zero hesitation this pass (pilot refinement R2 validated).
- Rule 2 (cross-surface consistency) has no mechanical support yet — nothing links a card's numbers to bps.html's numbers. The reuse registry (KA-1.1) covers *embeds*, not *claims-about-the-same-facts*. Logged as friction; NOT proposing a fix during the freeze.
- Removing "Linked Cards" sections raises a rendering question for later: surfaces should render related-content blocks FROM typed relationships (aligns with backlog WS-11).

## Next in sprint

- [x] EIC confirms stakes/evidence → cards 1, 2, 4, 5 published v1.0 (2026-07-14)
- [ ] Card 3 final approval after evidence-strengthening pass (v0.4, in review)
- [ ] Triage next-wave card ideas (worth-making test): daily-practice playbook, interview communication, English-vs-communication FAQ, parents' role
- [ ] Compose the Communication Skills Guide (first Publication; ≥3 embeds with context wrappers)
- [ ] First website surface + reuse registry entries
