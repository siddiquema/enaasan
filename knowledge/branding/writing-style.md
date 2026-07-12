# Writing Style

## Reading level

Plain English, written for a reader who may not have English as a first language and may be reading career/education guidance for the first time in their life — not for a reader who already has an English-medium, urban, well-counselled background. Concretely:

- Short to medium sentences. If a sentence needs more than one comma to hold its own weight, consider splitting it.
- Define or contextualise a term the moment it's introduced, even if it's common in some circles (e.g. don't assume "lateral entry" or "cut-off" is already understood — see `standards/glossary-standard.md`).
- Prefer concrete nouns and verbs over abstractions. "You'll spend four sessions a week on this" beats "significant time investment is required."
- Avoid idioms and culturally narrow metaphors that don't translate cleanly (across English fluency levels, and eventually across Tamil/Telugu/Hindi versions of long-form content).

## Spelling convention

Indian English (British-based) spelling for all content copy: *counselling*, *programme*, *specialised*, *recognised*, *maths*, *colour* (in prose; code/CSS variable names may use American spelling incidentally — that's a code convention, not a content one, and doesn't need to match this file).

## Sentence and paragraph construction

- One idea per sentence where possible.
- Paragraphs in guidance content stay short — 2–4 sentences is typical. A wall of text is a sign the content needs a list, a table, or a section break instead.
- Lead with the direct answer, then the reasoning, then the caveat — not the other way around. (This mirrors the FAQ's existing answer structure and the "quick answer" pattern in `docs/website-update-spec.md` §15.)

## Numbers, dates, and specifics

- Use real, specific numbers where they're known ("five to seven hours a week," not "some time each week"), and flag clearly when a number is an estimate or indicative range rather than a guarantee (see the salary-range disclaimer pattern already used in `careers.html`).
- Dates for anything volatile (fees, cut-offs, exam schedules) always come with a "verify with the official source" note — see `standards/publication-standard.md`.

## Accessibility

- Write for screen readers as much as for sighted readers: don't rely on colour alone to convey meaning ("the red ones are riskier" needs a text label too), and don't use directional language that assumes a specific layout ("click the button on the right").
- Avoid dense jargon-heavy sentences that force a re-read — if a sentence needs to be read twice to parse, rewrite it, don't just leave it and hope.
- In printed materials (PDFs), maintain sufficient contrast and font size for readability when printed on an ordinary home/school printer, including in greyscale — see `visual-language.md`'s print-friendliness rule.

## Formatting conventions in Markdown source

- Checklists use `- [ ]` syntax, matching the interactive/worksheet feel already established in the 90-Day Plan.
- Callout-style notes (the site's existing "Honest note:", "💡" verify-note pattern) are written as a blockquote with a bold lead-in, e.g.:

  > **Honest note:** a structured job search typically takes 3–6 months — that's normal, not failure.

- See `publishing/markdown-standard.md` for the full source-formatting rules this feeds into.
