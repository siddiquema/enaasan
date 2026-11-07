"""Recompute every number printed in Report No. 3 from the CSVs in this folder, and check the page against the result.

  python -P recompute.py            -> writes validation_log.csv and sources_rows.html, then checks ../index.html
  python -P recompute.py --raw DIR  -> also re-reads PLFS Tables 22 and 24 and AISHE Tables 33 and 38 for the comparison
                                       states from the raw files in a state-jobs-gap checkout (second, independent route)

Each figure has: an id, the claim, the value exactly as printed, the data file and row it comes from, the source document
and table, and (where one exists) the matching check in state-jobs-gap's own 289-row validation log
(state-jobs-gap_validation_log.csv, copied here). The script exits non-zero if any figure fails.
"""
import csv, html, re, subprocess, sys, glob
from pathlib import Path

D = Path(__file__).resolve().parent
PAGE = D.parent / "index.html"
R = lambda f: list(csv.DictReader(open(D / f, encoding="utf-8")))

STATES = ["West Bengal", "Tamil Nadu", "Karnataka", "Maharashtra", "Kerala", "Andhra Pradesh", "Telangana",
          "Odisha", "Jharkhand", "Bihar", "Assam", "Sikkim"]
EPFO_NAME = {"Odisha": "ORISSA"}
AB = {"West Bengal": "WB", "Tamil Nadu": "TN", "Karnataka": "KA", "Maharashtra": "MH", "Kerala": "KL", "Andhra Pradesh": "AP",
      "Telangana": "TG", "Odisha": "OD", "Jharkhand": "JH", "Bihar": "BR", "Assam": "AS", "Sikkim": "SK", "all India": "IN"}

# ---------------------------------------------------------------- load
pop = {r["state_as_in_aishe"].replace("Tamilnadu", "Tamil Nadu"): int(r["total"]) for r in R("aishe_population_18_23.csv")}
ug = {(r["year"], r["state"]): (int(r["male"]), int(r["female"]), int(r["total"])) for r in R("aishe_outturn_by_state.csv") if r["level"] == "Under Graduate"}
ep, rel = {}, {}
for r in R("epfo_statewise_net_payroll.csv"):
    k = (r["period"], r["state"], r["age_bucket"])
    if k not in rel or r["release_date"] > rel[k]:          # newest release wins (EPFO revises past figures)
        rel[k], ep[k] = r["release_date"], int(r["net_payroll"])
edu = {(r["indicator"], r["sector"], r["sex"], r["state"], r["education"]): r["value"] for r in R("plfs2025_education_by_state.csv")}
rse = {(r["age_group"], r["state"]): r for r in R("plfs2025_rse_state.csv")}
wage = {r["state"]: r for r in R("plfs2025_regular_wage_by_state.csv")}
city = {r["city"]: r for r in R("plfs2025_city_regular_wage.csv")}
rob = {r["state"]: r for r in R("robustness_plfs.csv")}
summ = {r["state"]: r for f in ("large_states_summary.csv", "adjacent_states_summary.csv") for r in R(f)}
sjg = [dict(zip(["group", "claim", "found", "expected", "result"], row)) for row in list(csv.reader(open(D / "state-jobs-gap_validation_log.csv", encoding="utf-8")))[1:]]
BUCKETS = ["Less than 18", "18-21", "22-25", "26-28", "29-35", "More than 35"]


def epf(fy, state, buckets):
    return sum(ep[(fy, EPFO_NAME.get(state, state.upper()), b)] for b in buckets)


def sjg_ref(text):
    """Line number(s) in state-jobs-gap_validation_log.csv whose claim contains `text` (header = line 1)."""
    hits = [str(i + 2) for i, r in enumerate(sjg) if text in r["claim"] and r["result"] == "PASS"]
    return "sjg log line " + ";".join(hits) if hits else ""


def ind(n):
    """Indian digit grouping: 1417724 -> 14,17,724."""
    s = str(int(round(n)))
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    head = re.sub(r"(\d)(?=(\d\d)+$)", r"\1,", head)
    return head + "," + tail


f1 = lambda x: f"{x:.1f}"
SRC = {  # source documents; table and page are given per figure
    "aishe": ("1", "All India Survey on Higher Education (AISHE) 2023-24, Final Report", "2023-24",
              "https://www.dohe-education.gov.in/static/uploads/2026/07/8616f33dfee644ab6b87a2bd0658b18d.pdf"),
    "epfo": ("2", "EPFO Provisional Payroll Data, release of 20 Sep 2025 (file ccb62712-September-2025.pdf)", "FY2023-24 and FY2024-25",
             "https://www.epfo.gov.in/data-hub/"),
    "plfs": ("3", "PLFS Annual Report 2025 (January-December 2025)", "2025",
             "https://www.mospi.gov.in/uploads/publications_reports/publications_reports1780040415321_0624fb13-fb47-40bc-b470-7c7e9635c3ef_PLFS_2025_F_REV_29052026.pdf"),
    "city": ("4", "PLFS 2025: Labour Market Dynamics in Million-plus Cities", "2025",
             "https://www.mospi.gov.in/uploads/publications_reports/publications_reports1782803524108_424fcfc9-f57d-4057-b4bd-abd52aae828d_Million_plus_city_F.pdf"),
}
FIG = []


def add(fid, claim, printed, value, src, table, datafile, datarow, sjg="", tol=None):
    FIG.append(dict(id=fid, claim=claim, printed=printed, value=value, src=src, table=table, file=datafile, row=datarow, sjg=sjg, tol=tol))


# ---------------------------------------------------------------- Finding 1: UG pass-outs per 100 people aged 18-23, 2023-24
for s in STATES:
    v = ug[("2023-24", s)][2] / pop[s] * 100
    add(f"F1.{AB[s]}", f"{s}: UG pass-outs per 100 people aged 18-23, 2023-24", f1(v), v, "aishe",
        "Table 33 (UG pass-outs) / Table 38 (population 18-23)", "aishe_outturn_by_state.csv + aishe_population_18_23.csv",
        f"2023-24, {s}, Under Graduate total = {ug[('2023-24', s)][2]}; population = {pop[s]}",
        f"matches summary file ({summ[s]['ug_per_100_youth_2023_24']})")
    add(f"F1.{AB[s]}.n", f"{s}: UG pass-outs, 2023-24", ind(ug[("2023-24", s)][2]), ug[("2023-24", s)][2], "aishe", "Table 33",
        "aishe_outturn_by_state.csv", f"2023-24, {s}, Under Graduate, total")
for s in ("Kerala", "West Bengal", "Maharashtra"):
    v = ug[("2023-24", s)][1] / ug[("2023-24", s)][2] * 100
    add(f"F1.{AB[s]}.fem", f"{s}: women's share of UG pass-outs, 2023-24 (%)", f1(v), v, "aishe", "Table 33",
        "aishe_outturn_by_state.csv", f"2023-24, {s}, Under Graduate, female / total")

# ---------------------------------------------------------------- Finding 2: EPFO net payroll aged 18-25 per 100 people aged 18-23, 2023-24
EP_STATES = [s for s in STATES if s != "Sikkim"]                      # Sikkim is not in EPFO's state tables
for s in EP_STATES:
    n = epf("2023-24", s, ["18-21", "22-25"])
    v = n / pop[s] * 100
    add(f"F2.{AB[s]}", f"{s}: EPFO net payroll aged 18-25 per 100 people aged 18-23, 2023-24", f1(v), v, "epfo",
        "State-wise net payroll by age band (pp. 18-23) / AISHE Table 38", "epfo_statewise_net_payroll.csv + aishe_population_18_23.csv",
        f"2023-24, {EPFO_NAME.get(s, s.upper())}, 18-21 + 22-25 = {n}; population = {pop[s]}",
        sjg_ref(f"{s}: formal entrants per 100 young people, 2023-24") or f"matches summary file ({summ[s]['epfo_per_100_youth_2023_24']})")
    add(f"F2.{AB[s]}.n", f"{s}: EPFO net payroll aged 18-25, 2023-24", ind(n), n, "epfo", "State-wise net payroll by age band",
        "epfo_statewise_net_payroll.csv", f"2023-24, {EPFO_NAME.get(s, s.upper())}, 18-21 + 22-25")
    b = epf("2023-24", s, ["22-25"]) / pop[s] * 100
    add(f"F2.{AB[s]}.2225", f"{s}: EPFO net payroll aged 22-25 only per 100 people aged 18-23, 2023-24", f1(b), b, "epfo",
        "State-wise net payroll, age band 22-25 / AISHE Table 38", "epfo_statewise_net_payroll.csv + aishe_population_18_23.csv",
        f"2023-24, {EPFO_NAME.get(s, s.upper())}, 22-25")
    add(f"F2.{AB[s]}.pop", f"{s}: population aged 18-23, 2023-24", ind(pop[s]), pop[s], "aishe", "Table 38 (population projection based on Census 2011)",
        "aishe_population_18_23.csv", f"2023-24, {s}, ALL Categories, total",
        sjg_ref("West Bengal population aged 18-23") if s == "West Bengal" else "checked against official PDF Table 38 (see README)")

# ---------------------------------------------------------------- Finding 3: PLFS regular salaried share and social security
for s in EP_STATES:
    r = rob[s]
    add(f"F3.{AB[s]}.reg", f"{s}: regular wage/salaried share of all workers, usual status, 2025 (%)", r["regular_share_of_workers"],
        float(r["regular_share_of_workers"]), "plfs", "Appendix A, Table (19), rural+urban, persons, column 4", "robustness_plfs.csv",
        f"{s}, regular_share_of_workers", sjg_ref(f"{s}: regular wage/salaried share of workers"))
    add(f"F3.{AB[s]}.nossb", f"{s}: regular non-farm employees with no social security benefit, 2025 (%)", r["regular_no_ssb_share"],
        float(r["regular_no_ssb_share"]), "plfs", "Appendix A, Table (36), rural+urban, persons", "robustness_plfs.csv",
        f"{s}, regular_no_ssb_share", sjg_ref(f"{s}: regular non-farm jobs with no social security"))

# ---------------------------------------------------------------- Finding 4: graduate unemployment and participation (age 15+), with RSE
G = lambda ind_, sex, s, e: float(edu[(ind_, "rural+urban", sex, s, e)].rstrip("*"))
for s in STATES + ["all India"]:
    for sex, tag in (("persons", "ur"), ("female", "ur.f"), ("male", "ur.m")):
        v = G("UR", sex, s, "graduate")
        add(f"F4.{AB[s]}.{tag}", f"{s}: unemployment rate, graduates, age 15+, {sex}, 2025 (%)", f1(v), v, "plfs",
            "Appendix A, Table (24), rural+urban", "plfs2025_education_by_state.csv", f"24, UR, rural+urban, {sex}, {s}, graduate",
            sjg_ref(f"unemployment, {s}, graduate") if sex == "persons" else "")
    v = G("LFPR", "female", s, "graduate")
    add(f"F4.{AB[s]}.lfpr.f", f"{s}: labour force participation rate, women graduates, age 15+, 2025 (%)", f1(v), v, "plfs",
        "Appendix A, Table (22), rural+urban, female", "plfs2025_education_by_state.csv", f"22, LFPR, rural+urban, female, {s}, graduate",
        sjg_ref(f"graduate women in labour force, {s}"))
    u = G("UR", "persons", s, "all")
    add(f"F4.{AB[s]}.all", f"{s}: unemployment rate, all education levels, age 15+, persons, 2025 (%)", f1(u), u, "plfs",
        "Appendix A, Table (24), rural+urban, persons", "plfs2025_education_by_state.csv", f"24, UR, rural+urban, persons, {s}, all",
        sjg_ref(f"unemployment, {s}, all"))
    rv = float(rse[("15+", s)]["person_ur"])
    add(f"F4.{AB[s]}.rse", f"{s}: published RSE of the all-education unemployment rate, age 15+, persons (%)", f"{rv:.2f}", rv, "plfs",
        "Appendix B, Table (1RSE), rural+urban, age 15+ (report page B-8)", "plfs2025_rse_state.csv", f"15+, {s}, person_ur")
    lo, hi = u * (1 - 1.96 * rv / 100), u * (1 + 1.96 * rv / 100)
    add(f"F4.{AB[s]}.ci", f"{s}: 95% range of the all-education unemployment rate = rate x (1 +/- 1.96 x RSE)", f"{lo:.1f}–{hi:.1f}",
        f"{lo:.1f}–{hi:.1f}", "plfs", "derived from Table (24) and Table (1RSE)", "plfs2025_education_by_state.csv + plfs2025_rse_state.csv",
        f"{s}: {u} x (1 +/- 1.96 x {rv}/100)")
women_higher = all(G("UR", "female", s, "graduate") > G("UR", "male", s, "graduate") for s in STATES + ["all India"])
add("F4.women_higher_everywhere", "Women graduates' unemployment rate is above men's in every state in the set and in India", "True", str(women_higher),
    "plfs", "Appendix A, Table (24)", "plfs2025_education_by_state.csv", "female vs male, graduate, rural+urban, 12 states + all India")

# ---------------------------------------------------------------- Finding 5: pay
for s in EP_STATES + ["Sikkim", "all India"]:
    w = wage[s]
    for col, tag, lab in (("ru_person", "", "persons"), ("ru_female", ".f", "women"), ("ru_male", ".m", "men")):
        v = int(w[col])
        add(f"F5.{AB[s]}{tag}", f"{s}: average monthly earnings of regular wage/salaried employees, CWS, rural+urban, {lab}, 2025 (Rs)",
            "₹" + ind(v), v, "plfs", "Appendix A, Table (38), CWS (report page A-237)", "plfs2025_regular_wage_by_state.csv",
            f"{s}, {col}", sjg_ref("West Bengal average regular wage or salary, persons") if (s == "West Bengal" and not tag) else
            (sjg_ref("India average regular wage or salary, persons") if (s == "all India" and not tag) else ""))
CITIES = [c for c, r in city.items() if r["state_in_comparison_set"]] + ["all million-plus cities", "urban India"]
for c in CITIES:
    v = int(city[c]["person"])
    add(f"F5.city.{c}", f"{c}: average monthly earnings of regular wage/salaried employees, CWS, persons, 2025 (Rs)", "₹" + ind(v), v,
        "city", "Table 8 (report page B-28)", "plfs2025_city_regular_wage.csv", f"{c}, person",
        sjg_ref(f"{c.replace(' MC', '')} average regular wage") if c in ("Kolkata MC", "Greater Mumbai MC", "Chennai MC") else "")
v = int(city["Kolkata MC"]["female"])
add("F5.city.Kolkata.f", "Kolkata MC: average monthly earnings of regular employees, women (Rs)", "₹" + ind(v), v, "city", "Table 8",
    "plfs2025_city_regular_wage.csv", "Kolkata MC, female")
rank = sorted([s for s in wage if s != "all India"], key=lambda s: int(wage[s]["ru_person"]))
add("F5.WB.rank", "West Bengal's average regular wage is the 2nd lowest of 35 States/UTs in Table 38", "2 of 35",
    f"{rank.index('West Bengal') + 1} of {len(rank)}", "plfs", "Appendix A, Table (38)", "plfs2025_regular_wage_by_state.csv",
    "rank of ru_person among 35 States/UTs", sjg_ref("West Bengal is the second lowest of 35 states"))

# ---------------------------------------------------------------- West Bengal close-up (the 458,000)
for fy in ("2022-23", "2023-24", "2024-25"):
    a = epf(fy, "West Bengal", BUCKETS)
    add(f"WB.all.{fy}", f"West Bengal EPFO net payroll, all ages, FY{fy}", ind(a), a, "epfo", "State-wise net payroll by age band, all six bands",
        "epfo_statewise_net_payroll.csv", f"{fy}, WEST BENGAL, sum of 6 age bands (release {rel[(fy, 'WEST BENGAL', '22-25')]})",
        sjg_ref("2024-25 net formal payroll, all ages") if fy == "2024-25" else "")
a = epf("2024-25", "West Bengal", ["18-21", "22-25"])
add("WB.1825.2024-25", "West Bengal EPFO net payroll, ages 18-25, FY2024-25", ind(a), a, "epfo", "State-wise net payroll by age band",
    "epfo_statewise_net_payroll.csv", "2024-25, WEST BENGAL, 18-21 + 22-25", sjg_ref("2024-25 net formal payroll, ages 18-25"))
b = epf("2024-25", "West Bengal", ["22-25"])
add("WB.2225.2024-25", "West Bengal EPFO net payroll, ages 22-25, FY2024-25", ind(b), b, "epfo", "State-wise net payroll, age band 22-25",
    "epfo_statewise_net_payroll.csv", "2024-25, WEST BENGAL, 22-25")
c = epf("2024-25", "West Bengal", ["26-28", "29-35", "More than 35"])
add("WB.26plus.2024-25", "West Bengal EPFO net payroll, ages 26 and over, FY2024-25", ind(c), c, "epfo", "State-wise net payroll, bands 26-28, 29-35, 35+",
    "epfo_statewise_net_payroll.csv", "2024-25, WEST BENGAL, 26-28 + 29-35 + More than 35")

a = epf("2024-25", "West Bengal", BUCKETS)
add("WB.458k", "West Bengal EPFO net payroll, all ages, FY2024-25, rounded to the nearest thousand (the circulating '458,000')", "458,000",
    round(a, -3), "epfo", "State-wise net payroll by age band, all six bands", "epfo_statewise_net_payroll.csv", "2024-25, WEST BENGAL, sum of 6 age bands")
add("F5.cities.count", "Number of million-plus cities with a regular wage estimate in Table 8", "46",
    sum(1 for c in city if c.endswith(" MC")), "city", "Table 8", "plfs2025_city_regular_wage.csv", "rows ending 'MC'",
    sjg_ref("number of million-plus cities with a regular wage estimate"))
add("F5.states.count", "Number of States/UTs ranked in PLFS Table 38 (excluding all India)", "35", len(rank), "plfs", "Appendix A, Table (38)",
    "plfs2025_regular_wage_by_state.csv", "rows other than all India")
add("META.sjg_checks", "Checks in state-jobs-gap's validation log at d8703d6, all PASS", "289",
    sum(1 for r in sjg if r["result"] == "PASS") if all(r["result"] == "PASS" for r in sjg) else -1, "plfs",
    "state-jobs-gap report/validation_log.csv (processing record, not a statistic)", "state-jobs-gap_validation_log.csv", "all rows")

# ---------------------------------------------------------------- check against the copied summary files and write the log
fails = []
for f in FIG:
    expect = f["printed"]
    got = f["value"]
    if isinstance(got, (int, float)):
        shown = expect.replace("₹", "").replace(",", "")
        ok = abs(float(shown) - got) <= (0.05 if "." in shown else 0.5)
        got_s = f"{got:.4f}" if isinstance(got, float) else str(got)
    else:
        ok, got_s = (str(got) == expect), str(got)
    if f["sjg"].startswith("matches summary file"):
        ok = ok and f["sjg"].endswith(f"({expect})")
    f["recomputed"], f["result"] = got_s, "PASS" if ok else "FAIL"
    if not ok:
        fails.append(f["id"])

# ---------------------------------------------------------------- optional second route: raw PLFS and AISHE files
if "--raw" in sys.argv:
    SJG = Path(sys.argv[sys.argv.index("--raw") + 1])
    pdf = glob.glob(str(SJG / "raw/plfs/*PLFS_2025_F_REV*.pdf"))[0]
    ann = subprocess.run(["pdftotext", "-raw", pdf, "-"], capture_output=True, text=True, check=True).stdout.split("\f")
    NUM = r"-?[\d,]+(?:\.\d+)?\*?"

    def table(tno, which):
        hits = [p for p in ann if re.search(rf"Table \({tno}\):", p) and re.search(r"^West Bengal ", p, re.M)]
        out = {}
        for l in hits[which].splitlines():
            m = re.match(rf"^([A-Za-z&.\- ]+?) ((?:{NUM} ){{9}}{NUM})$", l.strip())
            if m:
                out[m.group(1).replace("Keralam", "Kerala")] = [float(v.replace(",", "").rstrip("*")) for v in m.group(2).split()]
        return out
    t24 = {"persons": table(24, -1), "male": table(24, -3), "female": table(24, -2)}
    t22f = table(22, -2)
    for s in STATES + ["all India"]:
        for sex, tag in (("persons", "ur"), ("female", "ur.f"), ("male", "ur.m")):
            f = next(x for x in FIG if x["id"] == f"F4.{AB[s]}.{tag}")
            raw = t24[sex][s][6]
            ok = abs(raw - f["value"]) < 1e-9
            f["raw_check"] = f"raw PDF Table 24 = {raw} {'PASS' if ok else 'FAIL'}"
            if not ok: fails.append(f["id"] + " (raw)")
        f = next(x for x in FIG if x["id"] == f"F4.{AB[s]}.lfpr.f")
        raw = t22f[s][6]; ok = abs(raw - f["value"]) < 1e-9
        f["raw_check"] = f"raw PDF Table 22 = {raw} {'PASS' if ok else 'FAIL'}"
        if not ok: fails.append(f["id"] + " (raw)")
        f = next(x for x in FIG if x["id"] == f"F4.{AB[s]}.all")
        raw = t24["persons"][s][9]; ok = abs(raw - f["value"]) < 1e-9
        f["raw_check"] = f"raw PDF Table 24 = {raw} {'PASS' if ok else 'FAIL'}"
        if not ok: fails.append(f["id"] + " (raw)")
    import openpyxl
    wb = openpyxl.load_workbook(SJG / "raw/aishe/AISHE Final Report 2023-24 (1).xlsx", read_only=True, data_only=True)
    sh = next(n for n in wb.sheetnames if n.replace(" ", "").lower().startswith("33") and "cat" not in n.lower() and n[-1] != "a")
    raw_ug = {}
    for r in wb[sh].iter_rows(values_only=True):
        # by cell position: State, then male/female/total triples Ph.D. (+1..+3), M.Phil. (+4..+6), PG (+7..+9), UG (+10..+12)
        r = list(r)
        i = next((j for j, x in enumerate(r) if isinstance(x, str) and j + 12 < len(r) and isinstance(r[j - 1] if j else None, int)), None)
        if i is not None:
            raw_ug[r[i].strip().replace("Tamilnadu", "Tamil Nadu")] = r[i + 12]
    for s in STATES:
        f = next(x for x in FIG if x["id"] == f"F1.{AB[s]}.n")
        raw = raw_ug.get(s); ok = raw == f["value"]
        f["raw_check"] = f"raw AISHE xlsx Table 33 UG total = {raw} {'PASS' if ok else 'FAIL'}"
        if not ok: fails.append(f["id"] + " (raw)")

with open(D / "validation_log.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["id", "claim", "number_as_printed", "source_no", "source_document", "source_table", "year", "data_file", "data_row",
                "recomputed", "result", "state_jobs_gap_check", "raw_file_check"])
    for f in FIG:
        no, doc, year, _ = SRC[f["src"]]
        w.writerow([f["id"], f["claim"], f["printed"], no, doc, f["table"], year, f["file"], f["row"], f["recomputed"], f["result"], f["sjg"], f.get("raw_check", "")])

# ---------------------------------------------------------------- page check: every number on the page must be a logged figure
if PAGE.exists():
    page_src = PAGE.read_text(encoding="utf-8")
    body = re.sub(r"<!-- BEGIN:sources_rows.*?<!-- END:sources_rows -->", " ", page_src, flags=re.S)
    text = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->|<head>.*?</head>|<code>.*?</code>", " ", body, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text).replace("−", "-")
    tokens = set(re.findall(r"₹?\d[\d,]*(?:\.\d+)?", text)) | set(re.findall(r"\d+\.\d–\d+\.\d", text))
    used = [f for f in FIG if f["printed"] in tokens or f["printed"] == "True"]
    rows = []
    for i, f in enumerate(used, 1):
        no, doc, year, url = SRC[f["src"]]
        rows.append(f'<tr><td>{i}</td><td>{html.escape(f["printed"])}</td><td>{html.escape(f["claim"])}</td><td><a href="#src-{no}">[{no}]</a> {html.escape(f["table"])}</td>'
                    f'<td>{html.escape(year)}</td><td>{f["id"]}</td></tr>')
    block = "<!-- BEGIN:sources_rows (generated by data/recompute.py; do not edit by hand) -->\n" + "\n".join(rows) + "\n<!-- END:sources_rows -->"
    new_src = re.sub(r"<!-- BEGIN:sources_rows.*?<!-- END:sources_rows -->", lambda m: block, page_src, flags=re.S)
    if new_src != page_src:
        PAGE.write_text(new_src, encoding="utf-8")
    print(f"page uses {len(used)} logged figures; number-by-number table refreshed")
    printed = {f["printed"] for f in FIG}
    printed |= {p.replace("₹", "") for p in printed}
    for f in FIG:
        if "–" in f["printed"]:
            printed |= set(f["printed"].split("–"))
    allow = {l.split("#")[0].strip() for l in open(D / "page_number_allowlist.txt", encoding="utf-8")} - {""}
    unknown = []
    for tok in re.findall(r"₹?\d[\d,]*(?:\.\d+)?", text):
        if tok in printed or tok in allow or tok.rstrip(".,") in printed or tok.rstrip(".,") in allow:
            continue
        unknown.append(tok)
    if unknown:
        print("Numbers on the page that are not in the validation log or the allowlist:", sorted(set(unknown)))
        fails.append("page")

print(f"{len(FIG)} figures, {sum(f['result'] == 'PASS' for f in FIG)} PASS; raw-route checks: {sum(1 for f in FIG if f.get('raw_check'))}")
if fails:
    print("FAIL:", fails)
    sys.exit(1)
