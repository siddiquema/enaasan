# PDF Standard

Rules specific to PDF output, building on `visual-language.md` and `markdown-standard.md`.

## The print-friendliness rule (repeated here because it matters most for PDFs specifically)

**No full-bleed dark-coloured cover or first page on any PDF meant to be printed.** This is the single most important PDF-specific rule enaasan has, established directly from a real print-cost concern raised about the 90-Day Career Clarity Plan's cover design.

- Cover/first page: light or white base background. Dark navy and gold used as accents — a header band, a rule line, the wordmark, a coloured title — not as a full-page fill.
- Interior worksheet pages: white background, dark text, as already established in the existing 90-Day Plan's interior pages (pages 2–10 of that document already follow this correctly — only the cover needs the print-friendly treatment).
- A PDF intended purely for on-screen reading (not filling in, not printing) is a different case and may reasonably use a richer, screen-appropriate design — but if there's any reasonable chance a reader prints it, default to the print-friendly cover.

## Page size and layout

- A4, matching Indian printer/paper conventions (not US Letter).
- Margins wide enough that home/office printers won't clip content (roughly 18mm as a baseline, matching the existing 90-Day Plan).
- File size kept small (the existing 90-Day Plan is ~22KB for 10 pages) — enaasan's audience includes readers on limited mobile data; a PDF should open and download quickly on a basic connection.

## Typography in PDF

- Headings in Syne (or the closest available bold sans-serif if Syne isn't embeddable in the rendering tool used), body text in DM Sans or an equivalent clean sans-serif, consistent with `visual-language.md`.
- Font sizes and line spacing generous enough to stay legible when printed at home, including in greyscale.

## Structural requirements

- Every PDF includes: a title/cover, the content itself, and a closing section that names enaasan, the site URL, and — per `branding/brand-guidelines.md` — an honest note about what the document can and can't promise.
- A footer or header on interior pages identifies the document (title, page number) so a printed, stapled copy stays identifiable if pages get separated.
- Document metadata (the PDF's own title/author properties, not to be confused with visible page content) should reflect the `title` and `author` fields from `architecture/metadata-standard.md`.

## What this standard does not cover

- It does not specify a particular PDF-generation tool or library — that's an implementation detail for whenever the pipeline in `publishing-workflow.md` is actually built.
