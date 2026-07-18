---
name: blockchain-development
description: Design, implement, debug, or review blockchain applications across EVM and Solana, including chain selection, wallets, RPC clients, transaction lifecycle, confirmations, event indexing, off-chain services, and deployment operations. Use for dApps, wallet connections, transaction submission, RPC reliability, reorg handling, chain data, or web3 backend architecture; route Solidity contract internals and security audits to their specialist skills.
---

# Blockchain Development

Treat the chain as an adversarial distributed system with irreversible side effects, not as an ordinary database.

## Workflow

1. Detect the chain, network, protocol version, client libraries, contract or program addresses, and current project conventions. Never guess mainnet/testnet or chain ID.
2. Define trust boundaries: browser, wallet, signer, RPC provider, relayer, indexer, backend, contract/program, oracle, bridge, and administrator.
3. Separate the read path from the write path. Reads must declare consistency and freshness; writes must model simulation, signing, broadcast, replacement, confirmation, finality, and failure recovery.
4. Specify transaction invariants: intended recipient/program, chain ID, value or token amount, calldata/instruction data, fee bounds, nonce or recent blockhash, expiry, and replay domain.
5. Design RPC resilience with bounded retries, idempotency, rate limits, provider failover, error classification, and observable request IDs. Do not retry state-changing work blindly.
6. Design indexing around canonical block identity, event/log identity, checkpoints, backfill, deduplication, reorg rollback, and reconciliation against the chain.
7. Test locally first, then on an explicitly named test network or fork. Cover dropped, replaced, reverted, expired, duplicated, and reorganized transactions.
8. Produce a deployment and operations plan with address verification, permissions, monitoring, pause/incident controls, rollback limits, and owner/key custody.

## Chain Routing

- For EVM contract code, ABI, storage, events, gas, Foundry, or Hardhat, use `solidity-smart-contracts`.
- For contract or program security, invariants, privileged entry points, or audit findings, use `smart-contract-security`.
- For relational indexer storage and query plans, add `sql-databases`.
- For Solana, verify the program model, accounts, instruction constraints, compute budget, commitment level, blockhash expiry, and upgrade authority from current official docs.

## Safety

- Never request, display, log, or persist seed phrases or private keys. Use public addresses, test accounts, hardware wallets, multisigs, or approved secret stores.
- Do not deploy, sign, broadcast, transfer funds, change authorities, or touch mainnet without explicit authorization and exact network/address confirmation.
- Treat RPC data, wallet callbacks, token metadata, signatures, and explorer links as untrusted input.
- Never claim a transaction is final from a submitted hash alone; report the observed network, block/slot, confirmation state, and evidence.
- Do not invent fee, throughput, finality, or RPC guarantees. Measure or cite the configured network and provider.

## Output

Return the detected chain/network, trust-boundary map, read/write interfaces, transaction state machine, indexing/reorg model, signing boundary, failure modes, tests, deployment gates, and unresolved assumptions.

Read [references/sources.md](references/sources.md) when chain semantics or current client behavior matters.
