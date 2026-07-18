---
name: mle-workflow
description: Production machine-learning engineering workflow for data contracts, reproducible training, evaluation, deployment, monitoring, and rollback. Use when building, reviewing, or hardening ML systems beyond one-off notebooks, including feature pipelines, model registries, batch or online inference, drift, retraining, and operational readiness.
---

# Machine-Learning Engineering Workflow

Deliver a measurable product capability, not just a trained artifact. Use `ml-system-architecture` first when the module boundaries or serving topology are still undecided.

## 1. Frame the Capability

Record:

- user or system decision the model changes;
- prediction unit, population, horizon, and action;
- baseline and cost of false positives, false negatives, abstention, and delay;
- offline, online, guardrail, latency, reliability, privacy, and cost measures;
- launch, rollback, and decommissioning criteria.

Do not invent targets. Mark unknowns and propose how to measure them.

## 2. Define the Data Contract

Specify entity grain, source ownership, event and processing time, labels, feature availability, point-in-time joins, allowed lateness, schema compatibility, privacy class, retention, and snapshot identity.

Before training, test:

- leakage across time, entities, labels, and preprocessing;
- duplicates, missingness, impossible values, class balance, and slice coverage;
- train, validation, and test independence;
- reproducible extraction and immutable evaluation sets.

Route pipeline and backfill design to `data-engineering`; route contracts, lineage, and sensitive-data controls to `data-quality-governance`.

## 3. Establish a Baseline

Implement the cheapest credible baseline first: existing rule, heuristic, simple statistical model, or current production behavior. Preserve preprocessing with the artifact and make training deterministic where practical.

Record environment, code revision, configuration, dataset snapshot, random seeds, features, hyperparameters, metrics, and artifact digest. Use `tdd` for implementation tests and `eval-harness` for formal comparisons.

## 4. Evaluate by Failure Mode

Choose metrics from the decision and error costs. Include calibration, threshold analysis, slice performance, confidence intervals or repeated-run variability, robustness to missing or shifted inputs, latency, memory, throughput, and cost where relevant.

Keep evaluation data isolated from training, feature selection, and prompt iteration. Treat offline metrics as gates, not guarantees. Use `experimentation-causal-inference` when evaluating product impact with an experiment or making a causal claim.

## 5. Package the Prediction Interface

Version and validate:

- input and output schemas;
- preprocessing and feature definitions;
- model artifact and dependencies;
- thresholds, abstention, fallback, and error behavior;
- provenance and compatibility metadata.

Aim for train/serve parity. Test empty, malformed, extreme, stale, missing, and out-of-distribution inputs without exposing sensitive data.

## 6. Choose Serving and State

Derive batch, streaming, online, edge, retrieval, or hybrid serving from measured freshness, latency, throughput, consistency, and recovery requirements. Store labels, prediction logs, feature snapshots, experiments, and drift evidence through explicit database contracts; use `sql-databases` and `data-architecture` for those decisions.

Do not add a feature store, vector database, streaming platform, or model registry until a concrete requirement justifies the operational cost.

## 7. Release Safely

Use the lowest-risk applicable sequence:

1. offline replay;
2. shadow evaluation;
3. limited canary or controlled experiment;
4. staged expansion;
5. full release only after gates pass.

Define the traffic scope, duration, quality and safety guardrails, owner, observation window, rollback trigger, last-known-good artifact, and rollback procedure. Production deployment or traffic changes require explicit authorization.

## 8. Observe and Operate

Monitor system health and model behavior separately:

- service errors, saturation, queueing, latency, throughput, and cost;
- input schema and distribution change;
- prediction distribution, calibration, and delayed-label quality;
- critical slices, fairness or safety guardrails where applicable;
- feature freshness, fallback use, and model-version mix.

Use `bi-data-visualization` for operational scorecards and `data-quality-governance` for control ownership. Alerts need an owner, runbook, evidence link, containment action, and recovery verification.

## 9. Retrain Deliberately

Trigger retraining from new evidence, not a calendar alone. Reuse the same contracts and gates, compare against the deployed champion, and retain rollback artifacts. Record why data, features, code, or policy changed.

## Review Checklist

- The product decision and baseline are explicit.
- Dataset and feature provenance are reproducible.
- Leakage and slice risks have been tested.
- Evaluation matches operational consequences.
- Prediction interfaces are versioned and validated.
- Rollout, fallback, rollback, and ownership are concrete.
- Monitoring covers service, data, model, and product behavior.
- Security, privacy, governance, and cost assumptions are visible.

For an independent architecture review, delegate to the read-only `ml_architect` agent. Use `context-budget` or the existing `token_budgeter` agent for context and reasoning-budget planning; do not rely on hard-coded model prices without current verification.
