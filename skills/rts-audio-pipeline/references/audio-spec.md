# Audio Specification

Default formats:

- SFX: WAV, 48 kHz, 16-bit or 24-bit source
- UI: WAV, 48 kHz
- Ambience: WAV master, OGG runtime export
- Music: WAV master, OGG runtime export
- Voice: WAV master, OGG runtime export

Recommended naming:

```text
assets/audio/sfx/{event_id}_{variant}.wav
assets/audio/ui/{event_id}.wav
assets/audio/ambience/{ambience_id}_loop.wav
assets/music/{track_id}/{section}.wav
assets/voice/{speaker_id}/{line_id}.wav
```

Examples:

```text
assets/audio/sfx/musket_fire_01.wav
assets/audio/sfx/musket_fire_02.wav
assets/voice/officer/polish_mission_01_intro_003.wav
assets/music/main_theme/exploration_loop.wav
```

Human review required:

- final music
- final voice acting
- stylistically important SFX

Audio manifest shape:

```json
{
  "audio": [
    {
      "id": "musket_fire",
      "type": "sfx",
      "event": "unit.musket.fire",
      "files": [
        "assets/audio/sfx/musket_fire_01.wav",
        "assets/audio/sfx/musket_fire_02.wav",
        "assets/audio/sfx/musket_fire_03.wav"
      ],
      "loop": false,
      "status": "needs_audio_review"
    }
  ]
}
```
