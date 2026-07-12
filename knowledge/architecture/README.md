# architecture/

## Purpose

Defines how the Knowledge Layer itself is put together — not what content says, but how every piece of content is identified, described, and allowed to change over time. Read this folder before writing anything under `publications/`.

## Contents

| File | Defines |
|---|---|
| `knowledge-architecture.md` | The overall shape of the layer and how it relates to the website and to `docs/` |
| `metadata-standard.md` | The metadata block every publication must carry |
| `document-id-standard.md` | How every publication gets a unique, stable identifier |
| `versioning-standard.md` | How version numbers increase and what each kind of change means |

## Naming Convention

Files here are named `<topic>-standard.md`, except the one file that isn't a standard on its own but ties the others together (`knowledge-architecture.md`).

## Rules

1. These four documents are the load-bearing ones — every template and standard elsewhere in `knowledge/` refers back to them rather than redefining metadata, IDs, or versioning locally.
2. Changes to any file in this folder are structural changes to the whole layer. Treat edits here as higher-stakes than edits to a single template.

## Examples

- Before creating a new template type not listed in `templates/`, check `document-id-standard.md` for the TYPE code convention and add a new code there first, so the ID stays consistent across every future document of that type.

## Future Expansion

- A `taxonomy-standard.md` may be added once enough publications exist to need a controlled vocabulary for tags, careers, and skills (right now, `tags`, `related_careers`, and `related_skills` in the metadata standard are free-text).
