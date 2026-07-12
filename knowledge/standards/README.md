# standards/

## Purpose

Defines the acceptance bar each publication type must meet before it's considered done — the rules a document has to satisfy, as distinct from `templates/`, which defines the blank structure it starts from. A template gives you the shape; a standard tells you when that shape is correctly and completely filled in.

## Contents

| File | Covers |
|---|---|
| `publication-standard.md` | The lifecycle and review process every publication type shares, regardless of type |
| `knowledge-card-standard.md` | The detailed standard for Knowledge Cards specifically — fields, relationships, lifecycle |
| `learning-path-standard.md` | What makes a Learning Path complete and correctly sequenced |
| `worksheet-standard.md` | Rules for the fill-in-the-blank worksheet portions used inside Workbooks |
| `checklist-standard.md` | What makes a Checklist item well-formed and a Checklist complete |
| `glossary-standard.md` | How a Glossary document (a collection of short term-definitions) differs from a Knowledge Card, and what it must contain |

## Naming Convention

`<topic>-standard.md`. `publication-standard.md` is the umbrella one every publication follows; the rest add type-specific requirements on top of it.

## Rules

1. `publication-standard.md` applies to every single publication, regardless of type. The other five files add requirements specific to their type, on top of — never instead of — the umbrella standard.
2. A standard defines requirements and acceptance criteria. It is not itself a place to write real content — see each file for its own "do not create actual X" boundary, consistent with the instruction that this whole layer is documentation only.
3. If a standard and a template disagree (the template's structure doesn't actually satisfy the standard's requirements), fix the template — the standard is the source of truth for what "done" means.

## Examples

- Before marking a new Knowledge Card as `Published`, check it against every requirement in `knowledge-card-standard.md`, not just against whether it used `templates/knowledge-card-template.md`'s headings.

## Future Expansion

- A `comparison-page-standard.md` is a likely future addition once the Comparison Page content type from `docs/website-update-spec.md` §12 gets a template.
