# Editorial Calibration Baseline

**Status:** Approved v1.0 (EIC, 2026-07-14)
**Source:** Extracted from the first execution of the OPS-001 review gate on the five founding communication cards (see `knowledge/ops/sprint-logs/2026-07-communication-sprint.md` for the findings that produced each rule).
**Scope:** Applies to every Knowledge Card and Publication reviewed after this date. Reviewers check these alongside the metadata gate; authors who internalize them will pass review faster.

These nine rules exist because each one caught a real defect in carefully-written content. None is theoretical.

---

1. **A card may not carry claims above its own evidence rating.** Quantitative claims live in the card that owns them; other cards point to that card and speak qualitatively. *(Caught: a definition card asserting the salary premium's percentages.)*

2. **Cross-surface consistency is part of fact-checking.** Numbers in a card must agree with what Enaasan already publishes anywhere else. Internal contradiction is a gate failure even if each number is individually defensible. *(Caught: illustrative salaries ~10x the ladders published on bps.html.)*

3. **Recompute every worked calculation at review.** Both premises and arithmetic. *(Caught: a calculation wrong in both — and it had already survived one editing pass.)*

4. **Data analysis cannot prove what it doesn't observe.** If the source can't isolate the variable, any derived figure is modeling — rate it as such and say "modeled" in the body, never "based on analysis of." *(Caught: a premium-by-communication-quality table attributed to postings data that doesn't record communication quality.)*

5. **Composites are labeled in the body, not just metadata.** The reader must see "illustrative composite," not just the reviewer. *(Caught: constructed A/B personas under "Real Example" headings.)*

6. **Frameworks that coexist must be bridged.** When two cards slice the same concept differently, one carries an explicit "two lenses, one thing" note — otherwise the cluster reads as self-contradiction. *(Caught: four dimensions vs. five competencies.)*

7. **Scoring instruments are checked as instruments.** Bands must cover every possible score exactly once; edge cases must land somewhere. *(Caught: scoring bands that left valid scores uninterpretable.)*

8. **No "Linked Cards" sections in bodies.** Typed relationships in front matter are the single relationship record; body prose may reference a card by ID inline where it genuinely helps the reader.

9. **Currency and idiom hygiene.** Money is in rupees with Indian formatting; headers and phrasing match the reader's world. *(Caught: "In dollars:" headings over rupee arithmetic.)*

---

**Amending this baseline:** new rules are added when a review catches a defect class not covered here — with the catch documented, same as these. Rules are removed only if they stop earning their keep. This file is operational (OPS-layer); changing it does not touch the Knowledge Standard.
