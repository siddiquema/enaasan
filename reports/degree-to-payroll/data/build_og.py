"""Write og.html (1200 x 627 lead-chart card for LinkedIn) from validation_log.csv. Render it to ../og.png with a headless browser.
Every number on the card comes from the log, so the card cannot drift from the report."""
import csv
from pathlib import Path

D = Path(__file__).resolve().parent
LOG = {r["id"]: r["number_as_printed"] for r in csv.DictReader(open(D / "validation_log.csv", encoding="utf-8"))}
AB = {"MH": "Maharashtra", "KA": "Karnataka", "TG": "Telangana", "TN": "Tamil Nadu", "KL": "Kerala", "AP": "Andhra Pradesh",
      "WB": "West Bengal", "OD": "Odisha", "JH": "Jharkhand", "AS": "Assam", "BR": "Bihar"}
HIGH = {"MH", "KA", "TG", "TN"}
rows = sorted(AB, key=lambda a: -float(LOG[f"F2.{a}"]))
bars = "\n".join(
    f'<div class="r"><span>{AB[a]}</span><div class="t"><b class="{"g" if a in HIGH else ""}" style="width:{float(LOG[f"F2.{a}"]) / 12 * 100:.1f}%"></b><i>{LOG[f"F2.{a}"]}</i></div></div>'
    for a in rows)
html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@400;500&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:627px;background:#0D1B2A;color:#F2EFE9;font-family:'DM Sans',sans-serif;border-top:8px solid #F0A500;position:relative;overflow:hidden}}
.k{{position:absolute;left:64px;top:46px;font-family:'DM Mono',monospace;color:#F0A500;letter-spacing:.14em;font-size:17px}}
.u{{position:absolute;right:64px;top:40px;font-family:'Syne',sans-serif;font-weight:800;font-size:24px}} .u em{{font-style:normal;color:#F0A500}}
h1{{position:absolute;left:64px;top:96px;width:470px;font-family:'Syne',sans-serif;font-weight:800;font-size:48px;line-height:1.02;letter-spacing:-.02em}}
.big{{position:absolute;left:64px;top:252px;font-family:'Syne',sans-serif;font-weight:800;font-size:74px;color:#F0A500;letter-spacing:-.03em}}
.big small{{font-size:36px;color:#A8C0D4}}
.cap{{position:absolute;left:64px;top:356px;width:430px;font-size:21px;line-height:1.35;color:#F2EFE9}}
.note{{position:absolute;left:64px;top:452px;width:430px;font-size:15px;line-height:1.4;color:#A8C0D4}}
.ch{{position:absolute;left:556px;top:112px;width:580px}}
.ch h2{{font-family:'DM Sans',sans-serif;font-weight:500;font-size:22px}} .ch p{{color:#A8C0D4;font-size:15px;margin:4px 0 14px}}
.r{{display:grid;grid-template-columns:170px 1fr;align-items:center;height:31px;font-size:17px}}
.t{{display:flex;align-items:center;gap:8px}} .t b{{display:block;height:22px;background:#A8C0D4;border-radius:0 3px 3px 0;min-width:3px}} .t b.g{{background:#F0A500}}
.t i{{font-style:normal;font-family:'DM Mono',monospace;font-size:16px}}
.src{{position:absolute;left:64px;bottom:34px;font-family:'DM Mono',monospace;font-size:13px;color:#A8C0D4}}
</style></head><body>
<div class="k">ENAASAN RESEARCH · REPORT NO. 3</div>
<div class="u">en<em>aasan</em>.online/reports</div>
<h1>From Degree to Payroll</h1>
<div class="big">{LOG["F2.MH"]} <small>vs</small> {LOG["F2.BR"]}</div>
<div class="cap">young people joining formal payroll per 100 aged 18–23: Maharashtra vs Bihar, 2023-24.</div>
<div class="note">A ratio, not a placement rate. EPFO counts formal payroll only.</div>
<div class="ch"><h2>Formal-payroll entry per 100 people aged 18–23</h2><p>2023-24 · EPFO net payroll ages 18–25 ÷ population 18–23 · scale 0–12</p>
{bars}
</div>
<div class="src">Sources: EPFO payroll release 20 Sep 2025 (state-wise, by age); AISHE 2023-24, Table 38</div>
</body></html>"""
(D / "og.html").write_text(html, encoding="utf-8")
print("og.html written")
