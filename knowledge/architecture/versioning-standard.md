# Versioning Standard

## Version numbers

Format: `<major>.<minor>` (e.g. `1.1`, `2.0`). No patch/third number — this is content, not software; the distinctions that matter are "does the guidance change" (major) and "does the wording/detail change without changing the guidance" (minor).

## Pre-release

- A document in `Draft` status uses `0.x` (`0.1`, `0.2`, …), incrementing the minor number with each meaningful draft revision.
- The first version considered complete and reviewed becomes `1.0` and moves to `Published` status (after passing the review described in `standards/publication-standard.md`).

## Minor version bump (`1.0` → `1.1`)

Use for a change that does **not** alter what the document actually tells the reader to think or do:

- Fixing typos, grammar, broken links
- Updating a specific fact that's now outdated but doesn't change the guidance (an official exam name changed, a link moved to a new URL, a salary range figure was refreshed)
- Adding an example, clarifying a sentence, improving formatting
- Adding new cross-references (`related_documents`, `related_careers`, `related_skills`) as the knowledge layer grows

## Major version bump (`1.1` → `2.0`)

Use for a change that alters the actual guidance:

- A recommendation reverses or materially changes (e.g. "a drop year is usually not worth it" becomes "a drop year is often worth it under these specific conditions")
- Structural rewrite — sections added, removed, or reordered in a way that changes how a reader would use the document
- The target audience changes
- A significant new option or pathway is added that changes the overall picture (e.g. a Career Profile that previously covered 3 entry routes now covers 6, changing the "typical path" advice)

## Status transitions

```
Draft (0.x) → In Review → Published (1.0, then 1.x, 2.x, …) → Under Revision → Published (next version)
                                                              ↘ Retired
```

- `Under Revision`: the *previous* published version stays available and citable while a new one is being worked on. Don't leave a document with no available version while revising it.
- `Retired`: the document is no longer maintained. Its final version number is kept as history. If something replaces it, that document's `related_documents` should reference this one, and vice versa if practical.

## Rules

1. Every version bump updates three places consistently: the `version` metadata field, the version suffix on the `document_id`, and `last_reviewed` (set to the date the new version was finalised).
2. `review_due` is recalculated on every version bump, not just left from the previous version — see the cadence guidance in `metadata-standard.md`.
3. Minor bumps don't require the full review workflow in `standards/publication-standard.md`; major bumps do.
4. Never skip straight from `0.x` to a major version above `1.0` — the first published version is always `1.0`.
