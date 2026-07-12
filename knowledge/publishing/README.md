# publishing/

## Purpose

Describes how a single Markdown source document, written once under `publications/`, can become a PDF, a DOCX, a Google Doc, an HTML page, or a website section — without maintaining separate, drifting copies of the same content in four different formats.

**This is documentation only.** No renderer, script, or build tool exists yet. This folder describes the intended pipeline and the per-format rules content must follow so that pipeline is possible later — it does not implement it.

## Contents

| File | Covers |
|---|---|
| `publishing-workflow.md` | The overall single-source-to-many-outputs concept and process |
| `markdown-standard.md` | How the Markdown source itself must be structured to stay renderer-agnostic |
| `pdf-standard.md` | Rules specific to PDF output (including the print-friendly cover rule) |
| `docx-standard.md` | Rules specific to Word/DOCX output |
| `google-doc-standard.md` | How content moves into Google Docs for collaborative review |

## Naming Convention

One file per output format, plus the workflow overview and the shared Markdown-source standard that every format depends on.

## Rules

1. The Markdown source under `publications/` is always the single source of truth. No format-specific file (a `.docx`, a rendered `.pdf`) is ever hand-edited independently of its source — a fix goes into the Markdown, then gets re-rendered.
2. Format-specific standards describe *constraints the source must respect* (e.g. "don't rely on colour alone, since some renderers strip it") more than they describe *how to build a renderer*. Building the actual renderer is future, separate work.
3. Every rendered output still carries the metadata from `architecture/metadata-standard.md` in some visible form appropriate to its format (a PDF footer, a document properties field, a page's schema markup) — see each format's standard for specifics.

## Examples

- The existing `assets/enaasan-90-day-career-clarity-plan.pdf` was, in practice, generated from a Python/ReportLab script rather than from a Markdown source — it predates this standard. A future version of that document, if it adopts this pipeline, would have its content live as Markdown under `publications/graduates/`, with the PDF as one rendered output alongside a potential DOCX and web version.

## Future Expansion

- Once an actual renderer is built (a separate, explicit task), this folder should gain an `implementation-notes.md` documenting what tool or script does the rendering — kept distinct from the standards, which describe requirements independent of any specific tool.
