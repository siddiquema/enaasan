# publications/schools/

## Purpose

Real publications aimed at Class 10–12 students — stream choice, entrance exams, after-10th and after-12th pathways. Corresponds to the `SCHOOL10` and `SCHOOL12` audience codes in `architecture/document-id-standard.md`, and to the `/after10` and `/after12` topic hub concepts in `docs/website-update-spec.md` §10.

## Contents

Empty today. Each future publication gets its own subfolder, named by slug.

## Naming Convention

`publications/schools/<slug>/source.md`. Since this folder spans two audience codes (`SCHOOL10` and `SCHOOL12`), each publication's own metadata `audience` field and Document ID disambiguate which stage it targets — the folder itself isn't split further unless it grows large enough to need that.

## Rules

Same as the parent `publications/README.md`.

## Examples

- A future Guide such as "Which stream should I choose after 10th" would formalise content that currently exists as FAQ answers (`faq.html` Q1–Q6) into a fuller, standalone document here, cross-linked back to the relevant FAQ entries via `related_documents`.

## Future Expansion

- If this folder grows substantially, it may split into `schools/after-10th/` and `schools/after-12th/` subfolders — not done preemptively, since there's no content here yet to justify it.
