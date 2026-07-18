---
name: asset-librarian
description: Maintain asset registries, asset cards, manifests, validation states, provenance, review queues, and build reports for a game production pipeline. Use when tracking generated assets, deciding approval status, validating manifests, or organizing review queues.
---

# Asset Librarian

Use this skill whenever content must be tracked, validated, approved, rejected, or routed to human review. The asset registry is the source of truth.

## Asset Card Rules

Every asset must have an asset card. Do not rely on filenames alone.

Each card should track:

- `id`
- `type`
- `category`
- `faction` or equivalent grouping when relevant
- `status`
- `source`
- `outputs`
- `required_states`
- `qa`
- `provenance`
- `notes`

Use `approved` only when required files exist, technical validation passed, and required human review passed.

## Statuses

Allowed statuses:

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

## Batch Duties

For each batch:

1. Create or update asset cards.
2. Validate required fields.
3. Validate referenced files when possible.
4. Update domain manifests.
5. Update review queues.
6. Produce a short report.

## Useful Scripts

Use `scripts/validate_asset_registry.py` to validate a registry:

```bash
python "$CODEX_HOME/skills/asset-librarian/scripts/validate_asset_registry.py" manifests/asset_registry.json --root . --check-files
```

Read `references/asset-card-schema.json` when creating or validating cards.
