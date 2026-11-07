# Report No. 3 — publish kit (held back until the review gate clears)

Report: `reports/degree-to-payroll/` (branch `report/degree-to-payroll`). Draft finished 7 Nov 2026.
Per `docs/research-reports.md` step 7 and OPS-001 §5, the earliest review is **9 Nov 2026** (48-hour cooling period).
Nothing in this file is live. Apply it only after the review below passes.

## 1. Before publishing — open items

- [ ] **Practitioner view** box: Siddique to write (the only `class="ph"` left on the page). Keep the "Opinion — not data" label; no uncited numbers.
- [ ] **Language reviewers:** Tamil (reviewer TBD), Telugu (Vijaya), Hindi (Shafi) to check or rewrite the draft summaries. They currently carry a "Draft — awaiting review" flag and a note saying not to quote them. After review, remove the flags and the note.
- [ ] **Review gate:** check every number against its source table, using `reports/degree-to-payroll/data/validation_log.csv` (one row per number) and the PDFs it cites. Rerun `python -P reports/degree-to-payroll/data/recompute.py` after any text edit.
- [ ] Set `datePublished` / `dateModified` / `article:published_time` to the real publication date, and change "Draft, November 2026" in the meta row to "Published …".
- [ ] Remove `<meta name="robots" content="noindex, nofollow"/>` and the DRAFT banner (`<div class="template-banner …">`).
- [ ] Regenerate the PDF after the edits above (it currently carries the draft banner and the practitioner placeholder).
- [ ] Add the card and sitemap entry below; IndexNow runs on merge to `main`.

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
    <lastmod>YYYY-MM-DD</lastmod>
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
