# Safe schema-change playbook

Treat DDL, backfills, index builds, table rewrites, vacuum/compaction, and constraint validation as production mutations.

## Expand, migrate, contract

1. **Expand:** add backward-compatible structures; identify lock level, rewrite risk, replication impact, disk headroom, and old/new application compatibility.
2. **Migrate:** backfill in resumable bounded batches with stable keys, rate limits, checkpoints, reconciliation, lag/load guards, and idempotent retries.
3. **Cut over:** dual-read or dual-write only when necessary and with a declared source of truth; compare counts, checksums, invariants, and application errors.
4. **Contract:** remove old paths only after all consumers are confirmed migrated and the observation window passes.

## Required plan

- Exact engine/version and generated SQL from the migration framework.
- Table/index sizes, row counts, traffic and write rate, maintenance window, and replicas.
- Lock behavior and maximum acceptable wait; set bounded statement/lock timeouts where supported.
- Compatibility matrix for old/new application versions and rolling deploy order.
- Backfill key, batch size control, pause/resume, retry, and reconciliation queries.
- Abort signals for latency, locks, errors, disk, replication lag, and data mismatch.
- Rollback reality: distinguish reversible application cutover from irreversible/destructive data changes.
- Backup/restore or snapshot evidence appropriate to risk; a backup without a tested restore is not a rollback plan.

## Guardrails

- Do not combine schema introduction, full backfill, consumer cutover, and destructive cleanup in one deployment.
- Do not assume an ORM migration is online because its source diff looks small; inspect emitted SQL.
- Do not create or rebuild large indexes, validate constraints, change types, or set non-null blindly in production.
- Prefer additive changes and shadow validation. Preserve old data until reconciliation and rollback windows close.

## Primary references

- [PostgreSQL explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html)
- [PostgreSQL ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html)
- [MySQL InnoDB online DDL](https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl.html)
- [SQL Server online index operations](https://learn.microsoft.com/en-us/sql/relational-databases/indexes/perform-index-operations-online)
