---
name: data-quality-governance
description: Design or review data quality, contracts, ownership, lineage, privacy, retention, observability, and incident controls for analytical and operational datasets. Use for quality rules, governance models, PII handling, lineage gaps, freshness incidents, and control matrices.
---

# Data Quality and Governance

Make important data trustworthy without separating governance from actual risk.

## Workflow

1. Identify the process, critical data elements, consumers, owners, and consequences of failure.
2. Record the contract: grain, schema, semantics, keys, allowed values, freshness, availability, and compatibility policy.
3. Test completeness, validity, uniqueness, integrity, timeliness, distribution, and volume as relevant.
4. Trace lineage from source to consumption; mark manual steps, opaque transformations, and ownership handoffs.
5. Classify sensitive fields and document purpose, access, retention, deletion, residency, and audit needs. Escalate legal interpretations.
6. Place controls at useful boundaries: producer validation, transformation tests, reconciliation, anomaly detection, and consumer checks.
7. Define severity, owner, runbook, containment, recovery, communication, and post-incident learning.
8. Separate implemented controls from recommendations and report residual risk.

## Guardrails

- Never expose secrets, credentials, or personal data in examples or reports.
- Do not grant access, alter retention, delete data, or run repair/backfill jobs without explicit authorization.
- A passing schema test is not proof of semantic correctness.
- Use deterministic contracts and statistical monitoring where each fits.

## Output

Provide a control matrix with asset, owner, risk, rule, invariant or threshold, enforcement point, evidence, alert path, recovery action, and residual risk.

## Routing

- Use `data-engineering` for pipeline implementation and recovery.
- Use `analytics-engineering` for dbt model and metric contracts.
- Use `security-best-practices` when explicitly asked for a security review.

## References

See [references/sources.md](references/sources.md).
