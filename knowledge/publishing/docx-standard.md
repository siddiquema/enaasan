# DOCX Standard

Rules specific to Word/DOCX output — used primarily as a review and editing format (a reviewer commenting and tracking changes) rather than as enaasan's primary reader-facing distribution format, which is more often PDF or the website itself.

## Purpose of the DOCX form

The main reason a publication needs a DOCX rendering is collaborative review: track changes, inline comments, suggestions from a second reviewer, before a document is finalised per `standards/publication-standard.md`. Treat it as a working format, not a polished deliverable, unless a specific publication is explicitly meant to be distributed as a Word document.

## Style mapping

| Markdown element | Word style |
|---|---|
| `#` H1 | Title style, matching brand heading font where the template supports it |
| `##` H2 | Heading 1 |
| `###` H3 | Heading 2 |
| Body paragraph | Normal |
| Blockquote callout | A dedicated "Note" paragraph style — shaded background, not just italics, so it's visually distinct enough to survive a quick skim |
| Checklist (`- [ ]`) | Word's native checkbox content control, where the rendering tool supports it, or a plain bulleted list with an empty checkbox character otherwise |

## Review workflow expectations

- Track Changes is expected to be on for any DOCX used in the review step of `standards/publication-standard.md`.
- Comments should reference the specific metadata field or content section they concern, so feedback is easy to action against the Markdown source afterward.
- Once review is complete, changes are folded back into the canonical Markdown source — the DOCX with tracked changes is not itself the source of truth going forward, even after review.

## Colour and print considerations

- Where a DOCX is intended to be printed (less common than PDF for this purpose, but possible), the same print-friendliness principle from `visual-language.md` and `pdf-standard.md` applies — no full-page dark cover fills.
- Word's default light theme is generally already print-friendly; the main risk is a reviewer applying a dark background manually. Don't.

## What this standard does not cover

- It does not specify a particular DOCX-generation library or tool — implementation detail for the future pipeline described in `publishing-workflow.md`.
