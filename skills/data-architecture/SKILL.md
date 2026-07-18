---
name: data-architecture
description: Design or review data-platform architecture, domain boundaries, data products, warehouses, lakehouses, streaming systems, semantic layers, metadata, lineage, and migration paths. Use for platform topology, build-versus-buy decisions, data mesh or lakehouse proposals, authoritative-source conflicts, or cross-domain contracts.
---

# Data Architecture

Design deep modules with narrow, stable interfaces. Treat datasets, events, metrics, and access policies as versioned contracts.

## Workflow

1. Identify producers, consumers, decisions, authoritative sources, ownership, sensitivity, freshness, consistency, recovery, retention, and measured scale.
2. Map current data and control flows, duplicated truth, manual handoffs, coupling, and failure domains.
3. Define domain and platform modules. For each interface specify grain, schema, semantics, keys, time model, compatibility, quality, availability, access, and owner.
4. Compare three perspectives:
   - minimal interface: the smallest platform that solves the current problem;
   - flexible interface: extension seams for likely future domains and workloads;
   - common-path UX: the safest routine path for producers, engineers, analysts, and operators.
5. Evaluate batch, streaming, warehouse, lakehouse, operational store, semantic layer, catalog, and federation only against concrete requirements.
6. Define metadata, lineage, observability, governance, incident ownership, and cost allocation.
7. Plan an incremental migration with adapters, dual-running only where justified, reconciliation, consumer cutover, rollback, and decommissioning.
8. Record the decision, alternatives, evidence, tradeoffs, and revisit triggers.

## Guardrails

- Do not introduce a data mesh, lakehouse, streaming platform, catalog, or feature store as a goal by itself.
- Do not invent volume, latency, retention, reliability, or regulatory requirements.
- Avoid one shared canonical model for unrelated domains; prefer explicit translation seams.
- Separate control plane from data plane and analytical truth from operational transaction state.
- Do not authorize migrations, access changes, replication, or retention changes.

## Output

Return requirements, current-state map, proposed modules and interfaces, option matrix, ownership, governance, failure and recovery model, migration sequence, risks, unresolved questions, and an ADR-ready recommendation.

## Routing

- Use `data-engineering` for pipeline implementation.
- Use `analytics-engineering` for transformation and metric-layer design.
- Use `ml-system-architecture` for training, serving, retrieval, and model lifecycle concerns.

## References

See [references/sources.md](references/sources.md).
