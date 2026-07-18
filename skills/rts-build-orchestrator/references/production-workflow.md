# RTS Production Workflow

Recommended repository structure:

```text
game/
  design/
    world_bible.md
    art_bible.md
    audio_bible.md
    mechanics_bible.md
    narrative_bible.md
  assets/
    units/
    buildings/
    terrain/
    ui/
    vfx/
    audio/
    music/
    voice/
  source/
    blender/
    prompts/
    references/
  manifests/
    asset_registry.json
    units.json
    animations.json
    audio.json
    voice_lines.json
    balance.json
  reviews/
    visual_review_queue.md
    music_review_queue.md
    audio_review_queue.md
    vfx_review_queue.md
  reports/
```

Batch loop:

1. Select a narrow batch, such as one unit family or one building set.
2. Create or update asset cards.
3. Generate source assets.
4. Normalize outputs into project folders.
5. Run technical validators.
6. Update statuses and review queues.
7. Produce a report.
8. Wait for human review only where taste or direction matters.
