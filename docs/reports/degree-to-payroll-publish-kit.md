# Report No. 3 — publish kit

**Status 15 Nov 2026:** page, card, sitemap and PDF prepared for publication on **15 Nov 2026** (branch `report/degree-to-payroll`). Publishing = merging this branch to `main`; IndexNow runs on merge. Then post section 4.

Report: `reports/degree-to-payroll/` (branch `report/degree-to-payroll`). Draft finished 7 Nov 2026.
Per `docs/research-reports.md` step 7 and OPS-001 §5, the earliest review is **9 Nov 2026** (48-hour cooling period).
Nothing in this file is live. Apply it only after the review below passes.

## 1. Before publishing — open items

- [x] **Practitioner view** box: removed for launch (as Reports 1 and 2). Can be added later as a dated update; keep the "Opinion — not data" label and no uncited numbers. Previous placeholder markup is in commit `eadb02c`.
- [x] **Language summaries:** removed for launch (English only, as Reports 1 and 2). The drafts are in commit `eadb02c` (section `#langs`); restore after Tamil (TBD), Telugu (Vijaya) and Hindi (Shafi) review, and log it under Corrections/updates.
- [x] **Review gate** (13 Nov 2026: 260 figures, 260 PASS; 77 re-read from the raw files at state-jobs-gap `d8703d6`, all PASS): check every number against its source table, using `reports/degree-to-payroll/data/validation_log.csv` (one row per number) and the PDFs it cites. Rerun `python -P reports/degree-to-payroll/data/recompute.py` after any text edit.
- [x] Set `datePublished` / `dateModified` / `article:published_time` to the real publication date, and change "Draft, November 2026" in the meta row to "Published …".
- [x] Remove `<meta name="robots" content="noindex, nofollow"/>` and the DRAFT banner (`<div class="template-banner …">`).
- [x] Regenerate the PDF (13 Nov 2026, headless Chrome, 24 pp). Print from a copy with `<details class="numbers" open>`, or the per-number table drops out (15 pp).
- [x] Add the card and sitemap entry below; IndexNow runs on merge to `main`.

## 2. Card for `reports/index.html` (insert above Report No. 2)

```html
      <li class="report-card">
        <span class="status">Published · November 2026</span>
        <h3><a href="/reports/degree-to-payroll/">Report No. 3 — From Degree to Payroll</a></h3>
        <p>For every 100 people aged 18–23, Maharashtra added 11.1 young people to formal payroll in 2023-24; West Bengal added 2.1 and Bihar 0.3. Formal-job entry, graduate unemployment and pay, state by state, from EPFO, AISHE 2023-24 and PLFS 2025.</p>
        <p style="margin-top:12px"><a href="/reports/degree-to-payroll/" style="color:var(--gold);font-weight:600">Read the report →</a> · <a href="/reports/degree-to-payroll/degree-to-payroll.pdf" style="color:var(--gold)">PDF</a></p>
      </li>
```

## 3. Entry for `sitemap.xml` (after Report No. 2)

```xml
  <!-- Research Report No. 3: From Degree to Payroll -->
  <url>
    <loc>https://enaasan.online/reports/degree-to-payroll/</loc>
    <lastmod>2026-11-15</lastmod>
    <changefreq>yearly</changefreq>
    <priority>0.8</priority>
  </url>
```

## 4. LinkedIn post draft

Image: `reports/degree-to-payroll/og.png` (formal-payroll entry per 100 people aged 18–23, 2023-24).

> For every 100 people aged 18–23, Maharashtra added 11.1 young people to formal payroll in 2023-24. West Bengal added 2.1. Bihar added 0.3.
> Kerala is the exception that matters: few EPFO entrants, yet 40.0% of its workers hold regular salaried jobs, the highest of the states we compared.
> And in every state we compared, women graduates face higher unemployment than men.
>
> It is a ratio, not a placement rate — the report explains what the official data does and does not count.
> Enaasan Research Report No. 3, From Degree to Payroll: https://enaasan.online/reports/degree-to-payroll/

Every number in the post (11.1, 2.1, 0.3, 40.0%) is in the report's Sources table (IDs `F2.MH`, `F2.WB`, `F2.BR`, `F3.KL.reg`);
the women's claim is `F4.women_higher_everywhere`. Post only after the report is live.
