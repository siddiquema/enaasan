# Learning Path Standard

What makes a Learning Path (see `templates/learning-path-template.md`) complete and correctly sequenced, on top of the general `publication-standard.md`.

## Requirements

- [ ] The destination state (what the reader can understand or do after finishing) is stated plainly and concretely in the opening section — not a vague "you'll know more."
- [ ] Every step names the specific document it points to by Document ID, not just a topic description — a Learning Path with steps like "learn about entrance exams" (no link) has failed; it must say which Guide or Card, specifically.
- [ ] Each step's "why this step" reasoning genuinely justifies its position in the sequence — if a step could be reordered or removed without changing the outcome, question whether it belongs.
- [ ] `prerequisites` in the metadata block accurately reflects what a reader needs before starting — don't assume prior enaasan reading that isn't explicitly listed there.
- [ ] The path explicitly says it isn't a rigid, mandatory sequence a reader must complete before acting — per `branding/brand-guidelines.md`'s "decisions are recoverable" value, a Learning Path is a recommended order, not a gate.

## Sequencing principles

- Order steps by genuine dependency (a concept needed to understand the next step) or by natural decision order (explore options → narrow down → prepare to act), not by arbitrary convenience.
- Keep the total number of steps realistic for the stated `estimated_completion_time` — a path with 15 steps claiming "30 minutes" has miscalibrated one or the other.
- A Learning Path should mostly *curate and sequence existing documents* rather than contain large amounts of original content — if a "step" is actually several paragraphs of new material, that material likely belongs in its own Guide or Card, linked from the path.

## Maintenance

- If any linked document is retired or its Document ID's version changes materially (a major bump), the Learning Path's step and its `related_documents` reference need review — a Learning Path pointing to an outdated or retired document is a broken path, not a cosmetic issue.
