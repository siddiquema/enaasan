# Research Reports — how to publish one

Quarterly, data-backed reports at `https://enaasan.online/reports/`, shared on LinkedIn.
Milestone: **Research Reports** on GitHub.

## The hard rule

**No invented, estimated or "modelled" statistics.** Every number on the page, in the PDF,
in the LinkedIn post and in the Open Graph description must trace to either:

- a cited public source — dataset, table number, year and official URL
  (e.g. PLFS, AISHE, AICTE, India Skills Report), or
- Enaasan's own survey data, with the method published in the report.

If a number cannot be traced, leave it out. Practitioner experience (for example from BPS
hiring) is welcome, but it goes in the **Practitioner view** box labelled
"Opinion — not data" and carries no uncited numbers. This matches `GOV-001` and the
editorial calibration baseline (`knowledge/standards/editorial-calibration-baseline.md`).

## Files

| Path | What it is |
|---|---|
| `reports/index.html` | Public list of reports (indexed, in sitemap) |
| `reports/_template/index.html` | Report page template — `noindex`, not in sitemap, never sent to IndexNow |
| `reports/reports.css` | Shared styles (site navy/gold, follows dark/light/slate themes) |
| `reports/<slug>/index.html` | A published report |
| `reports/<slug>/<slug>.pdf` | Downloadable PDF of the same report |
| `reports/<slug>/og.png` | 1200 × 627 lead chart for LinkedIn previews |

## Steps

1. **Data first.** Download every table listed in the report's data-collection issue. Keep the
   original files and record table number, year and URL in the Sources table.
2. **Copy the template:** `reports/_template/` → `reports/<slug>/` (e.g. `career-choice-gap`).
3. **Fill every placeholder** (highlighted gold on the page; search the file for `class="ph"` and `[`):
   - headline finding, executive summary, 3–4 findings (one chart + one stat each)
   - "Where students and parents start"
   - Methodology, Limitations, Sources table (one row per number), How to cite
   - structured data (`Report` + one `Dataset` per source) and Open Graph tags
4. **Charts:** build each chart only from its source table. The caption names the source row.
5. **Summaries in Tamil, Telugu, Hindi:** written or checked by the reviewer
   (Telugu — Vijaya, Hindi — Shafi, Tamil — TBD). Same numbers and sources as the English.
   The three section headings in the template were written by the drafting assistant —
   have each reviewer confirm them.
6. **PDF:** export the finished page to `reports/<slug>/<slug>.pdf` (light background for printing).
7. **Review gate** (OPS-001): 48-hour cooling period, then check every number against its source table.
8. **Publish:** remove the `noindex` tag and the template banner; add a card to `reports/index.html`;
   add the URL to `sitemap.xml`. IndexNow is submitted automatically when the page is merged to `main`.
9. **LinkedIn:** one chart (`og.png`) + three-line insight + link. Every number in the post must
   appear in the report's Sources table.

## Checklist before merging a report

- [ ] No `class="ph"` left in the page (`grep -c 'class="ph"' reports/<slug>/index.html` returns 0)
- [ ] Every number has a Sources row with table, year and URL
- [ ] Opinion is only in the Practitioner view box
- [ ] `noindex` and the template banner removed
- [ ] Listed on `reports/index.html` and in `sitemap.xml`
- [ ] PDF and `og.png` present
