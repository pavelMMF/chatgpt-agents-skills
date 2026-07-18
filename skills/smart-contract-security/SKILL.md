---
name: smart-contract-security
description: Perform evidence-based security review of smart contracts and blockchain programs by mapping state-changing entry points, roles, trust boundaries, assets, invariants, external calls, token behavior, oracle and bridge assumptions, upgradeability, signatures, economic attacks, and operational controls. Use for Solidity/EVM, Solana/Rust, Move, CosmWasm, Cairo, or other contract audits, threat models, Slither/Echidna/Foundry findings, exploitability triage, or pre-deployment security gates.
---

# Smart Contract Security

Assume public inputs, adversarial ordering, composability, and financially motivated attackers. A clean scanner report is not an audit.

## Workflow

1. Define scope, chain/runtime, exact commit, deployed addresses if relevant, assets at risk, trusted actors, excluded dependencies, and whether only read-only review is authorized.
2. Build context from specifications, architecture, source, inheritance/modules, deployment scripts, roles, upgrade paths, external protocols, and operational controls.
3. Enumerate every state-changing external entry point. Record caller restrictions, modifiers/constraints, written state, transferred value, external calls, and expected callers for callbacks.
4. State security properties before hunting bugs: authorization, solvency/value conservation, accounting, state-machine transitions, replay resistance, price assumptions, liveness, and upgrade safety.
5. Trace privileged and attacker-controlled flows across calls. Review reentrancy, authorization bypass, initialization, storage collisions, signature domain/replay, oracle/MEV manipulation, token quirks, rounding/precision, denial of service, gas/compute exhaustion, and cross-chain trust.
6. Run repository-installed static analysis, unit/fuzz/invariant tests, and fork/local simulations when available. Treat tool output as leads; verify each finding in source and tests. Do not install or execute external tools without approval.
7. For each credible issue, document evidence, violated property, prerequisites, attack path, impact, likelihood, confidence, remediation, and a regression test. Separate confirmed findings from hypotheses and informational hardening.
8. Re-run affected tests and scanners after fixes. Record residual risks, centralized powers, key custody, monitoring, pause/incident response, and independent audit requirements.

## Rationalizations to Reject

- "It is a standard implementation" — verify the actual version, overrides, initialization, and composition.
- "Only the owner can call it" — trace how ownership or roles are obtained, transferred, delegated, and recovered.
- "The external contract is trusted" — model compromise, upgrade, callback, malformed return data, and changed behavior.
- "Tests pass" — confirm that tests encode security properties and adversarial sequences.
- "The scanner is clean" — scanners miss business logic, economic attacks, oracle assumptions, and cross-contract state.
- "The value is small today" — analyze reachable authority and future deposits, not only current TVL.

## Safety

- Keep review read-only unless the user explicitly asks for fixes. Never test exploits against public networks or third-party systems.
- Do not request or expose keys, seed phrases, signing payloads, private RPC URLs, or secrets.
- Do not claim a complete audit without declared scope, exact revision, executed evidence, limitations, and independent human review appropriate to the value at risk.
- Use proof-of-concept tests only in local, forked, or otherwise authorized environments; avoid publishing weaponized details before coordinated remediation.

## Finding Format

Return: severity, confidence, title, affected files/functions, violated invariant, prerequisites, attack path, impact, evidence or local reproduction, remediation, regression test, and residual risk. Finish with scope coverage, tools/tests actually run, privileged-role map, unresolved hypotheses, and deployment blockers.

Read [references/sources.md](references/sources.md) for primary security guidance and the reviewed external-skill provenance.
