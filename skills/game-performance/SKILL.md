---
name: game-performance
description: Diagnose and optimize game frame time, CPU, GPU, memory, allocations, loading, streaming, draw calls, shaders, physics, AI, animation, networking, and build size using profiler evidence. Use for stutter, low FPS, spikes, memory pressure, slow loads, thermal limits, platform budgets, or performance regressions in Unity, Unreal, Godot, or custom engines.
---

# Game Performance

Optimize the measured bottleneck on the target build and device, not the most visible code.

## Workflow

1. Define target platform/device, build type, scene, camera path, workload, quality settings, frame target, memory/load constraints, and reproduction steps.
2. Capture a stable baseline outside misleading editor overhead where possible. Record frame-time percentiles and traces, not only average FPS.
3. Classify the bottleneck: main thread, worker/job, render thread, GPU, memory/GC, IO/streaming, shader compilation, network, or thermal throttling.
4. Drill into the largest reproducible cost and form one causal hypothesis.
5. Change one bounded factor, capture the same scenario, and compare trace evidence plus visual/gameplay correctness.
6. Check secondary effects across representative content, quality tiers, devices, long sessions, loading transitions, and multiplayer where relevant.
7. Add a regression benchmark or budget gate with reproducible capture instructions.

## Guardrails

- Do not optimize editor-only measurements as if they were target-build truth.
- Do not trade correctness, readability, accessibility, or visual intent for unmeasured gains.
- Do not guess universal triangle, draw-call, texture, memory, or FPS budgets.
- Do not change global quality, render pipeline, compression, or asset import settings without authorization and rollback.

## Output

Return the reproduction, baseline, trace evidence, bottleneck, hypothesis, change, before/after result, quality risks, rejected explanations, and regression guard.

Read [references/sources.md](references/sources.md).
