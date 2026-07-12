# Implementation Notes — the rendering pipeline as actually built

*Added 2026-07-12, when the first real publication (ENA-WORKBOOK-GRAD-first-90-days-job-search) made the pipeline described in `publishing-workflow.md` real. This file documents the specific tools; the standards files remain tool-independent.*

## The tool

`knowledge/publishing/tools/build.py` — a single Python script, run from the repo root:

```
python knowledge/publishing/tools/build.py knowledge/publications/<audience>/<slug>/source.md
```

It parses the source's YAML front matter and constrained Markdown (per `markdown-standard.md`) and writes three outputs to `knowledge/output/`, named by Document ID:

| Output | How |
|---|---|
| `output/html/<id>.html` | Direct emission — standalone file, screen styles + `@media print` A4 styles in one |
| `output/pdf/<id>.pdf` | Microsoft Edge headless (`--headless --print-to-pdf`) rendering that same HTML — A4, print-friendly light cover per `branding/visual-language.md` |
| `output/docx/<id>.docx` | `python-docx` — built-in heading styles, explicit DXA cell widths, clear-type shading, literal ☐ characters for checklists |

## Requirements

- Python 3 with `python-docx` installed (`pip install python-docx`)
- Microsoft Edge (for the PDF step; `--skip-pdf` flag skips it)

## The Google Docs deliverable

There is no separate Google Docs file format. The DOCX is deliberately built **Google-Docs-import-safe** (no content controls, no percentage table widths, no embedded fonts): upload it to Google Drive and open with Google Docs, per `google-doc-standard.md`. That imported Doc is the collaborative-review surface; the Markdown source remains canonical.

## Known limitations

- The PDF has no page numbers (Chromium's headless print does not support `@page` margin-box content). The DOCX and HTML compensate via structure; revisit if this matters for print distribution.
- The parser supports only the constructs in `markdown-standard.md` — that constraint is a feature (it keeps sources renderable), but means fancy Markdown will be silently mis-rendered. Check output after adding new construct types.
- Rendered outputs are committed to git for now (per `output/README.md`, the gitignore decision was deferred). `.gitattributes` marks `*.pdf`/`*.docx` binary so Windows line-ending conversion can never corrupt them.
