#!/usr/bin/env python3
"""Validate an RTS audio manifest and inspect WAV files when available."""
import argparse
import json
import wave
from pathlib import Path

AUDIO_TYPES = {"sfx", "ui", "ambience", "music", "voice"}
REVIEW_REQUIRED = {"music", "voice"}


def get_audio(data):
    if isinstance(data, dict) and "audio" in data:
        return data["audio"]
    if isinstance(data, list):
        return data
    raise SystemExit("Audio manifest must be a list or an object with an 'audio' array.")


def inspect_wav(path: Path):
    with wave.open(str(path), "rb") as wav:
        return {
            "channels": wav.getnchannels(),
            "sample_rate": wav.getframerate(),
            "sample_width": wav.getsampwidth(),
            "frames": wav.getnframes(),
        }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--check-files", action="store_true")
    parser.add_argument("--expected-rate", type=int, default=48000)
    args = parser.parse_args()

    data = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    entries = get_audio(data)
    errors = []

    for idx, entry in enumerate(entries):
        label = entry.get("id", f"audio[{idx}]") if isinstance(entry, dict) else f"audio[{idx}]"
        if not isinstance(entry, dict):
            errors.append(f"{label}: entry must be an object")
            continue
        if not entry.get("id"):
            errors.append(f"{label}: missing id")
        if entry.get("type") not in AUDIO_TYPES:
            errors.append(f"{label}: invalid type '{entry.get('type')}'")
        files = entry.get("files")
        if not isinstance(files, list) or not files:
            errors.append(f"{label}: files must be a non-empty list")
            continue
        if entry.get("type") == "sfx" and len(files) < 3 and entry.get("repeated", True):
            errors.append(f"{label}: repeated sfx should provide at least 3 variants")
        if entry.get("type") in REVIEW_REQUIRED and entry.get("status") == "approved":
            if entry.get("human_review") != "passed":
                errors.append(f"{label}: {entry.get('type')} cannot be approved without human_review=passed")

        if args.check_files:
            for file_name in files:
                path = args.root / file_name
                if not path.exists():
                    errors.append(f"{label}: missing file: {file_name}")
                    continue
                if path.suffix.lower() == ".wav":
                    try:
                        meta = inspect_wav(path)
                    except wave.Error as exc:
                        errors.append(f"{label}: invalid wav {file_name}: {exc}")
                        continue
                    if meta["sample_rate"] != args.expected_rate:
                        errors.append(f"{label}: {file_name} sample_rate={meta['sample_rate']} expected={args.expected_rate}")
                    if meta["frames"] <= 0:
                        errors.append(f"{label}: {file_name} has no audio frames")

    if errors:
        print("Audio manifest validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Audio manifest OK: {len(entries)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
