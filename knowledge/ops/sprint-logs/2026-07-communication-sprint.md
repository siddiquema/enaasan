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

---

## Card 3 — Source Verification Report (2026-07-14)

Per EIC directive: every named study verified against its original publication or official source; memory not trusted. Environment constraints: WebSearch rate-limited for the session; several domains DNS-unreachable (Business Wire, Harris Poll, Wheebox/naceweb); web.archive.org page fetches disallowed. Verification proceeded via direct fetches of official documents.

**Sources verified (2):**

1. **PMI, *Pulse of the Profession In-Depth Report: The High Cost of Low Performance — The Essential Role of Communications* (May 2013)** — primary PDF fetched from pmi.org and read in full (10 pages). Verified verbatim: "two in five projects do not meet their original goals and business intent, and one-half of those unsuccessful projects are related to ineffective communications"; "US$75 million at risk for every US$1 billion spent"; "only one in four organizations can be described as highly-effective communicators"; "55 percent of project managers agree that effective communications … is the most critical success factor."
   **⚠ Memory was wrong:** the card previously said ineffective communication was "a primary contributor in roughly one-third of failed projects." The source says **one-half of unsuccessful projects**. Corrected. This alone justifies the verify-don't-trust-memory directive.
2. **Grammarly & The Harris Poll, *State of Business Communication*, 2024 edition** — live report page fetched (go.grammarly.com). Verified: poor communication → increased stress 51%, lowered productivity 41%, strained relationships 31%, missed deadlines 26%. **Stronger/more current edition than the 2022 one previously cited** — adopted.

**Sources replaced (2):**

- **Watson Wyatt "47% higher shareholder returns"** → could not verify against an original (firm merged into Towers Watson → WTW; original reports offline). Replaced with **Towers Watson *2011–2012 Change and Communication ROI Study*: "1.7 times more likely to outperform their peers financially"** — newer study by the successor firm, verified as quoted *within the PMI primary document in hand* (transparently cited as such). Same replacement chain added **PwC global PM survey: +17% projects finishing within budget** (also quoted within the verified PMI document).
- **Grammarly 2022 "$1.2T / ~$12,506 per employee"** → original 2022 report pages removed after Grammarly's corporate rebrand; press-wire and archive copies unreachable from this environment. **Removed per the rule** ("if any statistic cannot be verified, remove it"); the 2024 edition's verified impact percentages carry the day-to-day-cost point instead.

**Claims removed entirely (3):** LinkedIn in-demand-skills rankings (404/400 on official pages), NACE *Job Outlook* (domain unreachable), India Skills Report + AMCAT employability citations (domains unreachable/publisher absorbed). The India-scarcity leg was rewritten to rest honestly on **our own 50+ recruiter/HR interviews (2024–25)**, labeled as practitioner interviews — not a systematic survey — in both body and uncertainty.

**Remaining uncertainties:** premium size remains explicitly modeled (unchanged, by design); global/US research mechanisms transfer to India but figures don't convert; India leg is practitioner-interview-based. All stated in the card's uncertainty field.

**Final evidence recommendation:** `secondary-research` — legitimately held: the two load-bearing research streams are now verified against a primary document read in full and a live official report page, with the modeling explicitly non-load-bearing. **Recommended for publication → published as v1.0** (maturity seed, review_due 2027-01-14 per medium × volatile, relationships unchanged and resolving).

**Reference Collection v1.0:** all five communication cards now published at v1.0 — the reference examples for every future Knowledge Card.

---

## Stage 4 — First Publication composed (2026-07-14)

`ENA-GUIDE-CAREER-communication-skills-guide` v0.1 (draft) at `knowledge/publications/skills/communication-skills-guide/source.md`. Five embeds in teaching order (define → assess → value → illustrate → self-assess), narrative wrappers only, zero card content duplicated, canonical comments on every embed marker, reuse registry populated (`knowledge/ops/reuse-registry.md`). Needs its own review gate + cooling before publication.

## Stage 5 — Website integration plan: /skills/communication (prepared, NOT built)

1. **Path:** `skills/communication/index.html` → URL `/skills/communication/` — establishes the spoke-URL pattern (first non-flat page; existing flat pages unaffected).
2. **Source of content:** the page renders the **Guide**, not the cards directly — guide narrative + resolved card content, in guide order. Every rendered card section carries `<!-- canonical: ENA-KCARD-…-vX.Y -->`; the page header comment names the guide ID.
3. **Design:** existing dark-navy/gold system, nav + footer parity with current pages, `data-i18n` hooks from day one (EN strings first; TA/TE/HI pending translation workflow).
4. **Answer capsule:** 2-line TL;DR block at top (feeds GEO-06 backlog item); Article JSON-LD schema.
5. **Card 4 as tool:** phase 2 of the page — interactive scored checklist (client-side rendering of the checklist card per KA-1.0 §5.4); static text version ships first.
6. **Links in:** bps.html Tip 8 (primary), footer site-wide, careers.html skills mention. **Plumbing on publish:** sitemap.xml entry; IndexNow fires via existing GitHub Action.
7. **Registry:** flip the two "planned" rows to live in the same commit that ships the page.
8. **Gate:** page copy = guide narrative (already gated at guide review) + UI strings (light review at ship).

## Friction log additions (observations ONLY — nothing implemented)

- **F1 — Citation rot is real and fast:** Grammarly's rebrand killed every 2022 report URL within ~3 years of publication. Observation for future consideration: an evidence vault (archived copies of load-bearing source documents at citation time) would make verification durable. The PMI PDF fetched today is exactly such an artifact, currently sitting only in a temp folder.
- **F2 — Verification depends on tooling reach:** session search limits + DNS-blocked domains forced removal of probably-true-but-unverifiable citations (LinkedIn, NACE, ISR). The standard's remove-if-unverifiable rule worked as designed, but a "verification-pending" holding state was tempting — resisting it cost real citations. Evidence for a future discussion, not a change.
- **F3 — ID standard tension for domain-natural publications:** the guide files under the `skills/` domain folder but its ID carries an AUDIENCE code (`ENA-GUIDE-CAREER-…`) because only KCARDs get domain codes (A2). Folder says domain, ID says audience. Livable; logged.
- **F4 — Derived evidence floor requires judgment:** EOS-004 says publications display the minimum evidence of *load-bearing* embedded content but record none of their own, while EOS-003 requires the `evidence` field on knowledge objects. Resolved by recording the derived floor (expert-opinion; card 5 ruled non-load-bearing as illustration) with an explanatory note — but "which embeds are load-bearing" and "where does the derived value live" were judgment calls the standards don't fully specify.
- **F5 — Volatile-inheritance unspecified:** the guide was marked `volatile: true` because it embeds volatile cards (3, 5) — an inference the standards imply (review propagation, EOS-004) but never state as a rule.
- **F6 — Memory-vs-source confirmed calibration rule 3/4:** the PMI "one-third" misquote survived authoring AND two review passes; only primary-source verification caught it. The verification stage earns its cost.

## Next in sprint

- [x] EIC confirms stakes/evidence → cards 1, 2, 4, 5 published v1.0 (2026-07-14)
- [x] Card 3 source verification + evidence rewrite → published v1.0 (2026-07-14) — Reference Collection v1.0 complete
- [x] Communication Skills Guide composed (v0.1 draft; needs gate + cooling)
- [x] Reuse registry populated
- [x] Website integration plan prepared (page NOT built — awaiting go-ahead)
- [ ] Guide review gate (after 48h cooling) → publish guide
- [ ] Build /skills/communication page per plan (on EIC go-ahead)
- [ ] PAUSED per EIC: no new cards (daily-practice, interview, parents, English-fluency stay in backlog)
