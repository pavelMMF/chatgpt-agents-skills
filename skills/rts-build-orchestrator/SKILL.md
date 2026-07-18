---
name: rts-build-orchestrator
description: Coordinate a multi-agent production pipeline for an isometric RTS game, including asset planning, graphics, animation, audio, mechanics, narrative, validation, review queues, and build reports. Use when Codex needs to plan, run, or audit the full RTS content production workflow.
---

# RTS Build Orchestrator

Use this skill as the top-level production coordinator for an isometric RTS content pipeline. Treat the project as a repeatable asset factory with validation gates, not as isolated creative prompts.

## Core Workflow

1. Read the relevant project bibles when they exist:
   - `design/world_bible.md`
   - `design/art_bible.md`
   - `design/audio_bible.md`
   - `design/mechanics_bible.md`
   - `design/narrative_bible.md`

2. Convert requests into asset cards before generating content.

3. Route each task to the narrowest domain skill:
   - visual assets, sprite sheets, isometric renders, animation QA: `isometric-asset-pipeline`
   - registry, manifests, statuses, review queues: `asset-librarian`
   - SFX, music, voice, subtitles, loudness checks: `rts-audio-pipeline`
   - mechanics and balance: project scripts/tests first, then design notes
   - story and campaign text: narrative bible first, then consistency checks

4. Require validation before approval. A generated asset is not automatically approved.

5. Keep human review mandatory for:
   - final visual style
   - music
   - VFX taste and readability
   - important voice performances
   - faction-defining narrative decisions

6. Produce a batch report after each run:
   - created assets
   - changed manifests
   - validation failures
   - review queue
   - suggested next batch

## Status Rules

Use these statuses consistently:

- `planned`
- `in_progress`
- `generated`
- `validation_failed`
- `needs_visual_review`
- `needs_audio_review`
- `needs_music_review`
- `needs_fix`
- `approved`
- `deprecated`

Only use `approved` when all required files exist, technical validation passed, and required human review passed.

## Useful Scripts

Use `scripts/build_review_report.py` to summarize asset registry status and review queues:

```bash
python "$CODEX_HOME/skills/rts-build-orchestrator/scripts/build_review_report.py" manifests/asset_registry.json
```

Read `references/production-workflow.md` when setting up a new repository structure or planning a full production run.
