# The Enaasan Knowledge Standard — Version 1.0

**Declared:** 2026-07-14
**Status:** Frozen as v1.0. Changes require a version bump and a documented reason.

The Enaasan Knowledge Standard v1.0 consists of four specifications plus one validation record:

| Document | Role | Status |
|---|---|---|
| [EOS-001](EOS-001-philosophy.md) | Philosophy — Knowledge as Code methodology, 10 design principles, layered architecture | Approved v1.0 |
| [EOS-002](EOS-002-object-model.md) | Object Model — 10 frozen object types, categories, lifecycles, Purpose & Outcome | Approved v1.1 |
| [EOS-003](EOS-003-universal-metadata-contract.md) | Universal Metadata Contract — two-tier fields, philosophy traceability, interlock rules V1–V10 | Approved v1.0 |
| [EOS-003.1](EOS-003.1-metadata-retrofit-pilot.md) | Retrofit Pilot — empirical validation on real content; produced refinements R1–R8 | Complete |
| [EOS-004](EOS-004-relationship-model.md) | Relationship Model — 17 typed relationships, knower rule, lifecycle rules L1–L5, validation RV1–RV8 | Approved v1.0 |

**Companion documents outside the EOS series:**

- [`knowledge/LEARNING_PHILOSOPHY.md`](../../LEARNING_PHILOSOPHY.md) — the educational commitments the standard enforces; supreme over all structure
- [`knowledge/architecture/knowledge-architecture-1.0.md`](../../architecture/knowledge-architecture-1.0.md) — KA-1.0, Enaasan's application of the standard (domains, facets, placement)
- [`knowledge/architecture/knowledge-architecture-1.1-plan.md`](../../architecture/knowledge-architecture-1.1-plan.md) — planned enhancements (maturity criteria, reuse registry)
- [`knowledge/architecture/metadata-standard.md`](../../architecture/metadata-standard.md) — the Markdown/YAML representation of EOS-003
- [`knowledge/templates/AUTHOR_TEMPLATE.md`](../../templates/AUTHOR_TEMPLATE.md) — the contributor-facing authored core

## Roadmap change (2026-07-14)

The originally sketched **EOS-005 (Planning as Code)** and **EOS-006 (Publishing as Code)** will **not** be written as EOS specifications. Operational processes — how work flows, how reviews happen, how content ships — are deliberately kept out of the knowledge-governance standard and live in the separate **Operational Standards (OPS) series** (`knowledge/ops/`), beginning with OPS-001 (Editorial Workflow).

The boundary: **EOS defines what knowledge IS** (objects, metadata, relationships — stable for years). **OPS defines how work FLOWS** (workflows, roles, cadences — allowed to change as the team and tooling change). OPS documents conform to EOS; EOS never depends on OPS.
