# Database performance playbook

Use this after correctness is established. Never optimize from a single synthetic timing.

## Evidence sequence

1. Pin the engine/version, workload class, representative parameters, concurrency, data distribution, cache state, and latency/resource objective.
2. Identify workload-level offenders from native history and statistics before tuning one pasted query.
3. Capture a non-executing estimated plan first. Use an actual/analyze plan only when execution cost and side effects are understood.
4. Compare estimated versus actual rows, loops, time, reads, spills, waits, memory, parallelism, and partition/index pruning.
5. Locate the first material divergence rather than blaming the most visually expensive node.
6. Test one hypothesis at a time: query shape, statistics, index, partitioning, schema, cache/memory, contention, or application access pattern.
7. Verify result equivalence plus p50/p95/p99 latency, throughput, CPU, I/O, memory, lock time, write amplification, storage, and plan stability.
8. Roll out with a bounded canary, monitoring window, abort threshold, and reversal step.

## Engine-native evidence

| Engine | Workload evidence | Plan evidence | Important caveat |
|---|---|---|---|
| PostgreSQL | `pg_stat_statements`, cumulative statistics, locks/waits | `EXPLAIN`, then scoped `EXPLAIN (ANALYZE, BUFFERS)` | Analyze executes the statement; stale statistics and parameter values can dominate the plan. |
| MySQL | Performance Schema and statement summaries | `EXPLAIN` / JSON / TREE, then scoped `EXPLAIN ANALYZE` | Analyze executes supported statements; check optimizer statistics before forcing hints. |
| SQL Server/Azure SQL | Query Store runtime and wait history | estimated/actual execution plan | Plan forcing is an operational intervention with monitoring and an explicit unforce path. |
| SQLite | application timings and database statistics | `EXPLAIN QUERY PLAN` | Output format is diagnostic and may change; verify behavior on the shipped SQLite version. |

## Index decision

Derive the index from predicates, join keys, ordering/grouping, selectivity, and returned columns. Check existing prefix/overlapping indexes first. Price the read benefit against insert/update/delete cost, vacuum/maintenance, storage, cache pressure, build locks, replication lag, and removal risk. Avoid cargo-cult indexes on every filter column.

## Contention and maintenance

Separate CPU/I/O query cost from lock waits, connection saturation, buffer/cache pressure, checkpoints, compaction/vacuum, replication, and storage latency. Maintenance commands can rewrite data or take strong locks; treat them as production changes, not harmless tuning.

## Primary references

- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html)
- [PostgreSQL pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html)
- [PostgreSQL indexes](https://www.postgresql.org/docs/current/indexes.html)
- [PostgreSQL monitoring](https://www.postgresql.org/docs/current/monitoring.html)
- [MySQL 8.4 EXPLAIN](https://dev.mysql.com/doc/refman/8.4/en/explain.html)
- [MySQL optimization](https://dev.mysql.com/doc/refman/8.4/en/optimization.html)
- [SQL Server Query Store tuning](https://learn.microsoft.com/en-us/sql/relational-databases/performance/tune-performance-with-the-query-store)
- [SQLite query planner](https://www.sqlite.org/queryplanner.html)
