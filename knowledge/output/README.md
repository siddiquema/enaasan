# output/

## Purpose

Reserved for compiled/rendered artifacts produced by the pipeline described in `publishing/publishing-workflow.md` — a PDF rendered from a Markdown source, a DOCX for review, a rendered HTML fragment. These are **build products**, not source content: nothing here should ever be hand-edited directly, since any manual edit would be lost the next time the source is re-rendered.

A renderer now exists: `knowledge/publishing/tools/build.py` (see `publishing/implementation-notes.md` for usage and limitations). It writes HTML, PDF, and DOCX outputs here, named by Document ID. `epub/` remains reserved and empty.

## Contents

| Folder | Holds |
|---|---|
| `pdf/` | Rendered PDF outputs |
| `docx/` | Rendered DOCX outputs |
| `epub/` | Rendered EPUB outputs (reserved for a possible future e-reader format) |
| `html/` | Rendered HTML fragment outputs |

All four subfolders currently hold only a `.gitkeep` placeholder.

## Naming Convention

Rendered files are named after the source publication's Document ID (e.g. `ENA-WORKBOOK-GRAD-90-day-career-clarity-plan-v1.1.pdf`), once rendering exists — this keeps the output traceable back to its exact source version without needing to open the file.

## Rules

1. Never hand-edit a file in `output/` — fix the source under `publications/` and re-render.
2. `output/` is a candidate for `.gitignore` once real rendering exists and produces files regularly (build products often don't belong in version control) — that decision is deferred until there's an actual pipeline to evaluate against, not made speculatively now.
3. Nothing in `output/` is automatically deployed to the live website — embedding a rendered artifact into `enaasan.online` remains a separate, explicit task each time, per `knowledge/README.md`'s top-level rule.

## Examples

- Once a renderer exists, publishing `ENA-CHECKLIST-GRAD-before-your-first-interview-v1.0` would produce `output/pdf/ENA-CHECKLIST-GRAD-before-your-first-interview-v1.0.pdf` alongside its Markdown source remaining the canonical version under `publications/graduates/`.

## Future Expansion

- Once a real pipeline exists, this README should be updated with the actual tool/command used to render into each subfolder — kept as an addition to this file rather than moved into `publishing/`, since `publishing/` describes standards and requirements, while this note would describe the specific implementation.
