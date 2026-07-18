---
name: ml-system-architecture
description: Design or review production ML and LLM system architecture across data, features, training, evaluation, registry, serving, retrieval, monitoring, rollout, rollback, cost, and governance. Use for architecture decisions, batch versus online inference, RAG, model routing, or ML modernization.
---

# ML System Architecture

Design deep modules with narrow interfaces and explicit operational contracts. Use `mle-workflow` for lifecycle implementation details.

## Workflow

1. Define behavior, prediction unit, latency, throughput, freshness, quality, privacy, cost, and recovery objectives. Mark assumptions.
2. Establish baselines, offline and online evaluation contracts, failure costs, and launch criteria before choosing technology.
3. Map ingestion, labels, features, training, evaluation, registry, deployment, inference, feedback, monitoring, and retraining.
4. Define module interfaces and ownership. Version data contracts, artifacts, features, and prediction schemas.
5. Compare three views: the minimal interface that validates value; flexible seams for likely variants; and the safest common-path developer/operator experience.
6. Choose batch, streaming, online, edge, retrieval, or hybrid paths from measured constraints. Document consistency and fallback behavior.
7. Threat-model leakage, poisoning, prompt injection where relevant, privacy, tenancy, supply chain, and privileged actions.
8. Define shadow or canary rollout, observability, drift and quality monitors, incident response, rollback, and decommissioning.
9. Record the decision, alternatives, evidence, risks, and revisit triggers.

## Guardrails

- Do not invent scale, latency, accuracy, or cost requirements.
- Do not use one offline metric as the complete product objective.
- Keep evaluation data isolated from training and prompt iteration.
- Avoid extra platforms until a concrete requirement justifies them.
- Never deploy, retrain, migrate, or alter production traffic without explicit authorization.

## Output

Return requirements, modules and interfaces, flows, decision matrix, failure modes, controls, rollout and rollback, observability, cost drivers, unresolved questions, and an ADR-ready recommendation.

## References

See [references/sources.md](references/sources.md).
