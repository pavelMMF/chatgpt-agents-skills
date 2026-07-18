---
name: rts-audio-pipeline
description: Create, organize, validate, and review RTS audio assets including sound effects, UI sounds, ambient loops, music, voice lines, subtitle manifests, loudness checks, audio variants, and audio review queues.
---

# RTS Audio Pipeline

Use this skill for SFX, UI sounds, ambience, music, voice, subtitles, audio manifests, and review queues.

## Categories

Separate audio into:

- `sfx`
- `ui`
- `ambience`
- `music`
- `voice`

For SFX and voice, technical validation can mark files as ready for integration. For music, never mark final approval automatically; use `needs_music_review` until the user approves it.

## Technical Checks

Check every audio file for:

1. Correct file format.
2. Correct sample rate.
3. No clipping.
4. Sensible loudness target when tooling is available.
5. Clean start and end.
6. No clicks on loops.
7. Correct naming.
8. Manifest entry exists.
9. At least 3 variants for repeated gameplay sounds when possible.

## Voice Rules

Voice lines should track:

- speaker id
- line id
- faction
- context
- emotion
- subtitle text
- audio file
- approval status

## Useful Scripts

Use `scripts/validate_audio_manifest.py` to validate a manifest and inspect WAV files with Python stdlib:

```bash
python "$CODEX_HOME/skills/rts-audio-pipeline/scripts/validate_audio_manifest.py" manifests/audio.json --root . --check-files
```

Read `references/audio-spec.md` for defaults.
