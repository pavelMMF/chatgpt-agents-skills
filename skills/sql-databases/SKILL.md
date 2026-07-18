---
name: sql-databases
description: Design, review, debug, and optimize SQL and relational database changes across OLTP and analytical systems. Use for query correctness, joins and grain, execution plans, indexing, transactions, schema design, migrations, warehouse SQL, and database performance; require explicit authorization before any mutation, DDL, migration, or production query.
---

# SQL and Databases

Prefer read-only inspection. Never assume a dialect, schema, data volume, or production authorization.

## Workflow

1. Identify engine, version, workload, environment, table sizes, constraints, and whether the request is read-only.
2. Establish the expected grain and invariants of every input and output relation.
3. Review correctness before performance: filters, null semantics, join cardinality, duplicates, time zones, window frames, and integer/decimal behavior.
4. Reduce the query to a small reproducible case when debugging.
5. Inspect the actual execution plan when available. Distinguish estimated from measured rows and cost.
6. Propose the smallest change that addresses the demonstrated bottleneck.
7. Verify with representative data, result equivalence, plan changes, latency distribution, and resource use.

## Safety Gate

Do not run or recommend as an automatic step:

- unbounded scans on costly or production warehouses;
- `UPDATE`, `DELETE`, `MERGE`, DDL, migrations, vacuum/rewrite operations, or index creation without explicit scope;
- destructive schema changes without compatibility, backup, rollout, and rollback plans;
- queries containing credentials or raw sensitive values.

Use `EXPLAIN` before `EXPLAIN ANALYZE` when execution could be expensive or mutating. On systems where explain variants execute statements, confirm behavior first.

## Review Checklist

- Grain and primary/business keys are explicit.
- Join cardinality matches intent and is tested.
- Nulls, duplicates, late data, and time zones are handled.
- Predicates preserve partition/index pruning where applicable.
- Index proposals account for write amplification and storage.
- Transaction isolation and retry behavior match concurrency risks.
- Migrations are backward compatible or use expand/migrate/contract.
- The rollback condition is observable and rehearsable.

## Routing

- Use `analytics-engineering` for dimensional models and governed metrics.
- Use `data-engineering` for orchestration, backfills, and pipeline reliability.
- Use `data-analysis` when the main goal is insight rather than database design.

## Output

Return: engine assumptions, correctness findings, plan evidence, proposed change, risk, verification, and rollback. Never invent performance targets; derive them from workload requirements.

Read [references/performance-playbook.md](references/performance-playbook.md) for evidence-first tuning across PostgreSQL, MySQL, SQL Server, and SQLite. Read [references/schema-change-playbook.md](references/schema-change-playbook.md) for production DDL, backfills, cutovers, and rollback planning.

Read [references/sources.md](references/sources.md) for primary database references.

