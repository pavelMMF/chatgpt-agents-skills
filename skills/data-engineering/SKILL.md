---
name: data-engineering
description: Design, implement, and review reliable batch, streaming, CDC, and lakehouse or warehouse pipelines. Use for ingestion, ETL/ELT, orchestration, partitioning, idempotency, retries, backfills, schema evolution, data contracts, lineage, observability, capacity, cost, and runbooks; do not deploy or mutate production infrastructure without explicit authorization.
---

# Data Engineering

Design for replay, partial failure, and change. A successful happy-path run is not sufficient evidence.

## Workflow

1. Capture sources, consumers, volume, velocity, history, latency, availability, consistency, retention, and cost constraints.
2. Define input/output contracts: schema, keys, event time, freshness, ownership, compatibility, and quality gates.
3. Select batch, micro-batch, streaming, or CDC from requirements rather than fashion.
4. Design partitions, checkpoints, deduplication, watermarks, retries, and atomic publication.
5. Make every stage idempotent or explicitly record why it cannot be.
6. Design backfill and replay before launch: bounded range, concurrency, isolation, validation, and rollback.
7. Add lineage, metrics, logs, traces, alerts, dead-letter/quarantine handling, and a runbook.
8. Test schema changes, late/out-of-order data, duplicates, partial writes, dependency outages, and recovery.

## Reliability Contract

- When material requirements are unknown, separate confirmed facts, assumptions, and conditional choices; do not silently select technologies or guarantees.
- Never use wall-clock `now` as the only partition or business-time anchor for replayable jobs.
- Do not publish partial output as complete. Use staging plus atomic swap/commit where supported.
- Retries must not duplicate effects.
- Separate control-plane state from data-plane payloads.
- Preserve raw or reconstructable inputs when replay is a requirement.
- Define exactly-once claims in terms of observable business effects, not messaging slogans.
- Backfills must have dry-run, blast-radius, cost, and cancellation controls.
- Schema evolution must declare backward/forward compatibility and consumer migration.

## Routing

- Use `data-architecture` for platform topology and strategic tradeoffs.
- Use `data-quality-governance` for contracts, ownership, lineage, and policy controls.
- Use `sql-databases` for query plans, transactions, and schema mechanics.
- Use `analytics-engineering` for warehouse transformation and semantic models.

## Output

Return: requirements, pipeline stages, state/idempotency model, failure modes, backfill plan, quality/lineage, observability, cost controls, rollout, and rollback.

Read [references/sources.md](references/sources.md) for primary references.
