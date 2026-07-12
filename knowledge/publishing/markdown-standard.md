# Markdown Standard

The rules the Markdown source itself must follow so it can be reliably rendered into multiple output formats later, and so it stays readable as plain text in the meantime (since no renderer exists yet, the Markdown file *is* the document people read).

## Front matter

Every publication source starts with the YAML metadata block from `architecture/metadata-standard.md`, delimited by `---` lines, before any content.

## Heading hierarchy

- `#` (H1) — the document title, used exactly once, matching the `title` metadata field.
- `##` (H2) — major sections.
- `###` (H3) — subsections within a major section.
- Don't skip levels (an H3 must sit under an H2, not directly under the H1's implicit top level).

## Callouts

Enaasan's existing site pattern for a highlighted note (an "Honest note," a verify-reminder) is a blockquote with a bold lead-in phrase:

```markdown
> **Honest note:** a structured job search typically takes 3–6 months — that's normal, not failure.
```

Use this pattern consistently rather than inventing new callout syntax per document — a renderer can reliably style "blockquote starting with a bold phrase" the same way everywhere.

## Checklists

```markdown
- [ ] Item one
- [ ] Item two
```

Standard GitHub-Flavored-Markdown task list syntax — renders as plain text checkable items even with no special tooling, and can become an interactive checkbox in an HTML render or a fillable field in a DOCX render later.

## Tables

Use standard Markdown pipe tables for anything genuinely tabular (comparison content, a skill-gap tracker). Don't force prose into a table just for visual variety, and don't force tabular data into prose — match the structure to the content, per `docs/website-update-spec.md` §12's comparison template.

## Fill-in fields (worksheets)

For a printable line a reader writes on by hand (as in the 90-Day Plan's self-audit pages), represent it in Markdown as a labelled line followed by a blank, e.g.:

```markdown
My real constraints — money, location, family expectations, time:

_______________________________________________
```

A PDF/DOCX renderer turns the underline into an actual ruled writing line; in plain Markdown it's still legible as "here's where you write your answer."

## What not to do

- No raw HTML embedded in the Markdown except where genuinely unavoidable — it undermines the "renders cleanly to multiple formats" goal.
- No format-specific styling instructions inside the content Markdown (no "make this bold red" — that's a rendering decision governed by `visual-language.md` and the per-format standards, not something the author hard-codes per document).
- No embedded absolute file paths to images — reference assets by a stable name under `assets/`, per that folder's README.

## Relationship to `writing-style.md`

This file governs *structure* (headings, callouts, tables). `branding/writing-style.md` governs *prose* (sentence length, spelling, tone). A document should satisfy both.
