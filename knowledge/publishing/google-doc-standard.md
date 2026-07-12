# Google Doc Standard

How content moves into Google Docs, and what Google Docs is (and isn't) used for in enaasan's workflow.

## Purpose of the Google Doc form

Real-time collaborative drafting and review — particularly useful when more than one person needs to comment, suggest edits, or co-write simultaneously, which is harder to do well in a plain Markdown file or even a DOCX passed back and forth. Google Docs is a *process* tool for enaasan, not a *distribution* format — enaasan does not publish a "read this on Google Docs" link to the public as a final deliverable; the public-facing form is the website, a PDF, or another rendered output.

## Moving content in

Since no automated pipeline exists yet (see `publishing-workflow.md`), moving a Markdown source into Google Docs today is a manual step:

1. Start from a Google Doc template that mirrors the heading styles, callout treatment, and colour palette described in `visual-language.md`, so pasted content doesn't need heavy reformatting.
2. Paste the Markdown content in, then apply heading styles matching the source's `#`/`##`/`###` structure.
3. Recreate callouts (the bold-lead-in blockquote pattern from `markdown-standard.md`) using a shaded table cell or a "Note" paragraph style in the template, consistently.

## Moving content back out

After collaborative review and comment resolution in the Google Doc, changes are folded back into the canonical Markdown source under `publications/` — the Google Doc is not itself kept as the source of truth once review concludes, for the same reason a reviewed DOCX isn't (see `docx-standard.md`).

## Commenting conventions

- Comments should reference metadata fields or specific sections by name, matching the same convention as DOCX review, so feedback maps cleanly back onto the Markdown source.
- Resolve comments only once the corresponding change has actually landed in the Markdown source — resolving a comment in the Doc without updating the source loses the feedback.

## What this standard does not cover

- It does not specify Google Workspace account/permission setup, or any automated Docs API integration — that would be a separate, explicit task if ever pursued, and is out of scope for this documentation-only layer.
