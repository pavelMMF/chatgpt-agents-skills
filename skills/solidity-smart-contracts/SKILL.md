---
name: solidity-smart-contracts
description: Design, implement, test, debug, or review Solidity and EVM smart contracts using the repository's pinned compiler, Foundry or Hardhat, ABI and storage conventions, OpenZeppelin components, upgrade rules, fuzz tests, invariants, and deployment scripts. Use for Solidity code, ERC standards, contract architecture, gas-aware implementation, proxies, contract tests, or EVM deployment preparation; add smart-contract-security for adversarial review.
---

# Solidity Smart Contracts

Build from explicit invariants and repository evidence. Deployed bytecode is difficult or impossible to repair, so favor small interfaces and boring, reviewed components.

## Workflow

1. Inspect `foundry.toml`, Hardhat config, lockfiles, remappings, compiler version, optimizer settings, EVM target, dependency versions, deployment scripts, and existing test style.
2. Write the contract specification before code: actors, assets, state, privileged operations, state transitions, invariants, external dependencies, events, errors, and upgrade policy.
3. Choose the smallest contract/interface boundary. Prefer composition and version-pinned, audited library components over custom token, access-control, cryptography, proxy, or accounting code.
4. Implement checks, effects, and external interactions deliberately. Define authorization, reentrancy boundary, failure behavior, rounding direction, units, signature domain, replay protection, and emergency controls.
5. Keep storage layout explicit. For upgradeable systems, use the repository's established proxy pattern and validate layout compatibility; do not mix incompatible major library versions.
6. Add unit tests for each transition and failure path, fuzz tests for input ranges, invariant tests for system properties, and fork tests only when an external deployed dependency matters.
7. Compile and run the project's own formatter, tests, coverage, size, and gas checks when installed. Do not install tools or change compiler/dependency versions without approval.
8. Prepare deployment evidence: constructor/initializer inputs, deterministic addresses if used, roles/owners, verification commands, post-deploy assertions, and handoff to multisig or governance.

## Review Checklist

- External/public functions expose only the required interface and emit useful events.
- Privileged functions have explicit least-privilege roles, transfer/renounce behavior, and recovery rules.
- Token accounting covers fee-on-transfer, rebasing, missing return values, decimals, and approval edge cases when applicable.
- Arithmetic states units and rounding; loops and storage growth have bounded gas behavior.
- Calls to external contracts handle callbacks, reverts, return data, and reentrancy.
- Upgrade authorization, initializer protection, storage layout, and implementation locking are tested when proxies exist.
- Tests assert state and value conservation, not merely successful execution.

## Safety

- Never deploy, verify, upgrade, transfer ownership, or broadcast a transaction without explicit network, address, account, and authorization.
- Never handle real private keys or seed phrases. Do not put secrets in `.env` examples, commands, logs, or fixtures.
- Do not claim an audit from compilation or unit tests. Use `smart-contract-security` for adversarial analysis and independent review before value-bearing deployment.
- Pin versions and consult current official docs; Solidity, frameworks, and OpenZeppelin APIs change.

## Output

Return the detected toolchain, contract specification, interfaces and invariants, implementation changes, tests executed, gas/size evidence, deployment gates, security handoff, and unresolved risks.

Read [references/sources.md](references/sources.md) before version-sensitive Solidity, Foundry, Hardhat, or OpenZeppelin work.
