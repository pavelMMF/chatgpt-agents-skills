---
name: analytics-engineering
description: Design and review governed warehouse transformations, dimensional models, marts, semantic metrics, tests, freshness, documentation, and safe model evolution. Use for dbt-style staging/intermediate/mart layers, facts and dimensions, incremental models, metric definitions, lineage, and analytics release planning; route tool-specific dbt implementation to the bundled dbt skills.
---

# Analytics Engineering

Treat analytical models as versioned interfaces between source systems and decisions.

## Workflow

1. Define the business process, model grain, consumers, refresh expectation, and ownership.
2. Discover existing sources, models, metrics, and lineage before adding a new model.
3. Work backward from the consumer contract: keys, dimensions, measures, history, and allowed latency.
4. Choose the shallowest useful layer:
   - staging for source-aligned renaming and typing;
   - intermediate for reusable transformations at a clear grain;
   - marts for stable facts, dimensions, and decision-facing models.
5. Define metric semantics once: numerator, denominator, entity, time grain, filters, and late-arriving behavior.
6. Add tests proportional to risk: keys, relationships, accepted domains, reconciliation, freshness, and complex transformation unit tests.
7. Document purpose, grain, ownership, important columns, and known limitations.
8. Evaluate downstream impact and plan a compatibility window for breaking changes.

## Design Rules

- One model, one declared grain.
- Reuse existing transformations when the grain and semantics match; do not add models by habit.
- Keep raw-source quirks in staging and business semantics in governed layers.
- Separate event time, processing time, and reporting time.
- Make incremental logic idempotent and test full-refresh equivalence on a bounded sample.
- Do not silently redefine a published metric or reuse a name for different semantics.
- Treat dashboards, reverse ETL, ML features, and exports as consumers even when they are outside the transformation DAG.

## dbt Routing

- `using-dbt-for-analytics-engineering`: implement and validate dbt models.
- `adding-dbt-unit-test`: test complex SQL transformations.
- `building-dbt-semantic-layer`: define MetricFlow entities, dimensions, and metrics.
- `working-with-dbt-mesh`: contracts, access, versions, breaking changes, and cross-project refs.

All warehouse writes or expensive builds require the user's authorization and a bounded selector. Prefer parse, compile, list, or limited preview before build/full-refresh.

## Output

Return: consumer need, grain, proposed model DAG, metric contract, tests, lineage/ownership, compatibility plan, and verification commands.

Read [references/sources.md](references/sources.md) for primary sources and vendored-skill provenance.

