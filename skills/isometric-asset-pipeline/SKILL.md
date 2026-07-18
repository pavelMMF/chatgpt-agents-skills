---
name: isometric-asset-pipeline
description: Create, normalize, validate, and review isometric RTS visual assets such as units, buildings, terrain, sprite sheets, animations, shadows, masks, and VFX. Use when working on graphics, animation manifests, or asset QA for classic isometric RTS-style games.
---

# Isometric Asset Pipeline

Prefer source-based asset creation: keep editable 3D, layered, or prompt/source files, then render deterministic 2D outputs. A pretty PNG without source and manifest is not production-ready.

## Default Pipeline

1. Read `design/art_bible.md` when present.
2. Create or update an asset card through `asset-librarian`.
3. Produce source files under `source/`.
4. Render or export normalized outputs under `assets/`.
5. Generate a preview sheet for human review.
6. Validate sprite/animation manifests.
7. Set status to `needs_visual_review` unless the user explicitly approves it.

## Visual Rules

For RTS units and buildings, prefer:

- 8 directions by default, 16 for premium/hero assets if the engine supports it
- fixed isometric camera angle
- fixed lighting rig per biome/faction set
- transparent PNG outputs
- consistent shadow style
- bottom-center unit pivot
- footprint-center building pivot
- stable scale across faction variants

## Technical Checks

For each sprite or animation, verify:

1. Frame dimensions are consistent.
2. Transparent background is clean.
3. Pivot point is stable.
4. Bounding boxes do not crop important pixels.
5. Direction count matches the manifest.
6. Animation frame count matches the manifest.
7. Required states exist.
8. Hit frames are marked for attacks.
9. Shadow is present and not cropped when required.
10. Preview sheet exists for human review.

If an asset passes technical checks but still needs artistic approval, use `needs_visual_review`, not `approved`.

## Useful Scripts

Use `scripts/validate_sprite_manifest.py` to check a JSON sprite manifest:

```bash
python "$CODEX_HOME/skills/isometric-asset-pipeline/scripts/validate_sprite_manifest.py" manifests/animations.json --root . --check-files
```

Read `references/sprite-spec.md` before defining new sprite sheet requirements.
