"""Extract the two small tables this report needs that are not among state-jobs-gap's cleaned files.

Reads raw files from a checkout of github.com/siddiquema/state-jobs-gap pinned at the SHA in data/README.md.
Writes, next to this script:
  aishe_population_18_23.csv   AISHE 2023-24 Final Report, Table 38 (sheet "38Pop2020(2011)"): population aged 18-23,
                               all categories, male / female / total, every State/UT and All India.
  plfs2025_rse_state.csv       PLFS Annual Report 2025, Appendix B, Table (1RSE): RSE (%) of LFPR, WPR and UR, usual status
                               (ps+ss), rural+urban, for age 15-29 (report page B-7) and age 15+ (page B-8).

Usage:  python -P extract_extras.py <path to state-jobs-gap checkout>
Needs:  openpyxl, and pdftotext (poppler) on PATH.
"""
import csv, glob, re, subprocess, sys
from pathlib import Path

import openpyxl

SRC = Path(sys.argv[1])
OUT = Path(__file__).resolve().parent

# ---- AISHE Table 38 (population 18-23, 2023-24)
wb = openpyxl.load_workbook(SRC / "raw/aishe/AISHE Final Report 2023-24 (1).xlsx", read_only=True, data_only=True)
sheet = next(n for n in wb.sheetnames if n.replace(" ", "").startswith("38"))
rows = []
for r in wb[sheet].iter_rows(values_only=True):
    c = [x for x in r if x is not None]
    if len(c) >= 11 and isinstance(c[1], str):                       # numbered State/UT rows: Sl.No, name, 9 numbers
        rows.append([c[1].strip(), c[2], c[3], c[4]])
    elif len(c) >= 10 and c[0] == "All India":
        rows.append(["All India", c[1], c[2], c[3]])
with open(OUT / "aishe_population_18_23.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["year", "state_as_in_aishe", "male", "female", "total", "source"])
    for s, m, f, t in rows:
        w.writerow(["2023-24", s, m, f, t, f"AISHE 2023-24 Final Report, Table 38, sheet {sheet}, ALL Categories"])
print(f"aishe_population_18_23.csv: {len(rows)} rows")

# ---- PLFS Table (1RSE), rural+urban, 15-29 and 15+ (PDF pages 534 and 535 = report pages B-7 and B-8)
pdf = glob.glob(str(SRC / "raw/plfs/*PLFS_2025_F_REV*.pdf"))[0]
COLS = ["male_lfpr", "male_wpr", "male_ur", "female_lfpr", "female_wpr", "female_ur", "person_lfpr", "person_wpr", "person_ur"]
out = []
for page, age in ((534, "15-29"), (535, "15+")):
    t = subprocess.run(["pdftotext", "-raw", "-f", str(page), "-l", str(page), pdf, "-"], capture_output=True, text=True, check=True).stdout
    assert "rural+urban" in t and ("15-29 years" if age == "15-29" else "15 years and above") in t and "Table (1RSE)" in t, (page, age)
    n = 0
    for line in t.splitlines():
        m = re.match(r"^([A-Za-z&.\- ]+?) ((?:\d+\.\d+ ){8}\d+\.\d+)$", line.strip())
        if m:
            out.append([age, m.group(1)] + m.group(2).split() + [f"PLFS Annual Report 2025, Appendix B, Table (1RSE), rural+urban, age {age}, PDF page {page}"])
            n += 1
    print(f"RSE page {page} ({age}): {n} rows")
with open(OUT / "plfs2025_rse_state.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["age_group", "state"] + COLS + ["source"])
    w.writerows(out)

# ---- PLFS Table (38): average monthly wage/salary earnings of regular wage/salaried employees, CWS, by State/UT (PDF page 314)
t = subprocess.run(["pdftotext", "-raw", "-f", "314", "-l", "314", pdf, "-"], capture_output=True, text=True, check=True).stdout
assert "Table (38): Average wage/salary earnings" in t and "CWS for each State" in t
WCOLS = ["rural_male", "rural_female", "rural_person", "urban_male", "urban_female", "urban_person", "ru_male", "ru_female", "ru_person"]
wage = []
for line in t.splitlines():
    m = re.match(r"^([A-Za-z&.\- ]+?) ((?:[\d,]+ ){8}[\d,]+)$", line.strip())
    if m and not m.group(1).startswith("employee"):
        wage.append([m.group(1).strip()] + [v.replace(",", "") for v in m.group(2).split()]
                    + ["PLFS Annual Report 2025, Appendix A, Table (38), CWS, Rs per month, PDF page 314 (report page A-237)"])
print(f"Table 38 wages: {len(wage)} rows")
with open(OUT / "plfs2025_regular_wage_by_state.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["state"] + WCOLS + ["source"])
    w.writerows(wage)

# ---- Million-plus Cities report, Table 8: average monthly wage/salary earnings of regular employees, CWS, every city
CITY_STATE = {  # state grouping as printed in the report's list of million-plus cities
    "Greater Visakhapatnam MC": "Andhra Pradesh", "Vijayawada MC": "Andhra Pradesh", "Patna MC": "Bihar",
    "Dhanbad MC": "Jharkhand", "Ranchi MC": "Jharkhand", "Bengaluru MC": "Karnataka",
    "Chhatrapati Sambhajinagar MC": "Maharashtra", "Greater Mumbai MC": "Maharashtra", "Kalyan-Dombivli MC": "Maharashtra",
    "Nagpur MC": "Maharashtra", "Nashik MC": "Maharashtra", "Navi Mumbai MC": "Maharashtra", "Pimpri Chinchwad MC": "Maharashtra",
    "Pune MC": "Maharashtra", "Thane MC": "Maharashtra", "Vasai Virar MC": "Maharashtra",
    "Chennai MC": "Tamil Nadu", "Coimbatore MC": "Tamil Nadu", "Madurai MC": "Tamil Nadu",
    "Greater Hyderabad MC": "Telangana", "Howrah MC": "West Bengal", "Kolkata MC": "West Bengal",
}
cpdf = glob.glob(str(SRC / "raw/plfs/*Million_plus_city_F.pdf"))[0]
ct = subprocess.run(["pdftotext", "-raw", cpdf, "-"], capture_output=True, text=True, check=True).stdout
block = ct.split("Table 8: Average wage/salary earnings (Rs.) during the preceding calendar month from regular")[1]
block = block.split("Labour Market Dynamics in Million-plus Cities")[0]
assert "wage/salaried employment in CWS for each million-plus city" in block
city = []
for line in block.splitlines():
    m = re.match(r"^(.+? MC|all million-plus cities|urban India) ([\d,]+\*?) ([\d,]+\*?) ([\d,]+\*?)$", line.strip())
    if m:
        city.append([m.group(1), CITY_STATE.get(m.group(1), "")] + [v.replace(",", "") for v in m.group(2, 3, 4)]
                    + ["PLFS 2025 Labour Market Dynamics in Million-plus Cities, Table 8 (report page B-28), CWS, Rs per month"])
print(f"city Table 8 wages: {len(city)} rows")
with open(OUT / "plfs2025_city_regular_wage.csv", "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["city", "state_in_comparison_set", "male", "female", "person", "source"])
    w.writerows(city)
