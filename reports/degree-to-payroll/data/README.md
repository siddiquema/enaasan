# Data for Research Report No. 3 — From Degree to Payroll

Every number in `../index.html`, `../degree-to-payroll.pdf` and `../og.png` is recomputed from the files in this folder by
`recompute.py` and listed, one row per number, in `validation_log.csv`.

## Where the data comes from

- **Source repository:** https://github.com/siddiquema/state-jobs-gap (public)
- **Pinned commit:** `d8703d6305ced309fba0edf41212c164b4003ad2` (main, 6 Nov 2026, "Add note on what the 458,000 payroll figure is made of and on idle youth (#10)")
- **Copied:** cleaned CSVs only (Option A). The `raw/` folder (about 42 MB) and the dashboard were **not** copied.
- **Provenance:** `provenance/aishe-PROVENANCE.md`, `provenance/epfo-PROVENANCE.md` and `provenance/plfs-PROVENANCE.md` are the three PROVENANCE.md files from `raw/aishe`, `raw/epfo` and `raw/plfs` at the pinned commit. They name each original file, its publisher page and download date.
- **Validation inherited:** `state-jobs-gap_validation_log.csv` is the pinned repository's `report/validation_log.csv`: 289 checks, all PASS, re-deriving its tables from the raw files by a second route.

## Files copied unchanged from state-jobs-gap `data/`

All twelve were byte-compared with the pinned commit after copying.

| File | What it is |
|---|---|
| `aishe_outturn_by_state.csv` | AISHE pass-outs (out-turn) by state, year (2019-20 to 2023-24) and level, male/female/total. AISHE Table 33. |
| `epfo_statewise_net_payroll.csv` | EPFO net payroll by state, age band and period, from the Jan 2025 and Sep 2025 releases (use the newest release for each period). |
| `plfs2025_education_by_state.csv` | PLFS 2025 Appendix A Tables 22–24: LFPR, WPR and UR by highest education level, State/UT, sector and sex, age 15+, usual status. |
| `plfs2025_district_snapshot.csv` | PLFS 2025 district snapshot: LFPR, WPR, UR (15+) and NEET (15–29) for states and their larger districts. Not used in the report text. |
| `peer_ratio.csv` | UG pass-outs and EPFO 18–25 net payroll by year for West Bengal and four peer states. Not used in the report text. |
| `adjacent_states_summary.csv` | Summary for West Bengal and its neighbours (Odisha, Jharkhand, Bihar, Assam, Sikkim). Used as a cross-check of the per-100 ratios. |
| `large_states_summary.csv` | Same summary for West Bengal and six large states. Used as a cross-check of the per-100 ratios. |
| `robustness_plfs.csv` | PLFS 2025 Tables 19, 35, 36 by state: regular wage/salaried share of workers, limited-company share, share of regular non-farm jobs without social security; plus EPFO per 100 youth. |
| `tamil_nadu_cities.csv`, `tamil_nadu_summary.csv` | Tamil Nadu city indicators (Million-plus Cities report) and state summary. Superseded in the report by `plfs2025_city_regular_wage.csv`; kept as the brief requires. |
| `maharashtra_cities.csv` | Maharashtra city indicators (Million-plus Cities report). Superseded as above. |
| `wb_gap.csv` | West Bengal UG pass-outs vs EPFO net payroll by year, 2019-20 to 2023-24. Cross-check for the West Bengal close-up. |

## Files extracted for this report (`extract_extras.py`)

The brief's file list did not contain the population denominator, the published margins of error or state wages. With the
user's agreement these were extracted from raw files already in the pinned repository (the same documents it cites), by
`python -P extract_extras.py <path to state-jobs-gap checkout>`:

| File | Source | Notes |
|---|---|---|
| `aishe_population_18_23.csv` | AISHE 2023-24, Table 38 (Excel sheet `38Pop2020(2011)`) | Population aged 18–23, all categories. A projection based on Census 2011. Values were also checked against Table 38 in the official PDF at the dohe-education.gov.in URL. |
| `plfs2025_rse_state.csv` | PLFS Annual Report 2025, Appendix B, Table (1RSE), rural+urban, ages 15–29 (PDF p. 534, report p. B-7) and 15+ (PDF p. 535, report p. B-8) | Published relative standard errors of LFPR, WPR and UR by State/UT and sex. No RSE is published by education level. |
| `plfs2025_regular_wage_by_state.csv` | PLFS Annual Report 2025, Appendix A, Table (38), CWS (PDF p. 314, report p. A-237) | Average monthly wage/salary earnings of regular employees by State/UT, rural/urban/combined, by sex. Means, not medians. |
| `plfs2025_city_regular_wage.csv` | PLFS 2025 Labour Market Dynamics in Million-plus Cities, Table 8 (report p. B-28) | Same measure for all 46 million-plus cities, plus the all-cities and urban-India rows; cities in the comparison states are tagged with their state. |

The PLFS Annual Report and Million-plus Cities PDFs in the pinned repository are byte-identical (MD5) to the files served at
the URLs cited in the report, checked on 7 Nov 2026.

## Scripts and outputs

| File | What it does |
|---|---|
| `recompute.py` | Recomputes every printed figure from the CSVs; writes `validation_log.csv`; refreshes the number-by-number Sources table in `../index.html`; fails if any number on the page is missing from the log (apart from years, ages, table numbers and chart scales in `page_number_allowlist.txt`). With `--raw <checkout>` it also re-reads PLFS Tables 22 and 24 and AISHE Table 33 from the raw files. |
| `validation_log.csv` | One row per number: id, claim, value as printed, source document, table, year, data file, data row, recomputed value, PASS/FAIL, the matching state-jobs-gap check (where one exists) and the raw-file check (where run). |
| `page_number_allowlist.txt` | Non-statistical numbers allowed on the page. |
| `build_og.py`, `og.html` | Build the 1200 × 627 LinkedIn card from the log; `og.html` is rendered to `../og.png` with headless Chrome. |

Last full run (7 Nov 2026): 260 figures, 260 PASS; 77 also re-read from the raw files, all PASS; 245 of the figures appear on the page.
