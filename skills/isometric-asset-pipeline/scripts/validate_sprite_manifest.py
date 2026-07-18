#!/usr/bin/env python3
"""Validate an isometric RTS sprite manifest."""
import argparse
import json
from pathlib import Path

REQUIRED_TOP = {"id", "type", "directions", "required_animations", "animations", "pivot"}
VALID_DIRECTIONS_8 = {"n", "ne", "e", "se", "s", "sw", "w", "nw"}


def fail(errors, asset_id, message):
    errors.append(f"{asset_id}: {message}")


def get_sprites(data):
    if isinstance(data, dict) and "sprites" in data:
        return data["sprites"]
    if isinstance(data, list):
        return data
    raise SystemExit("Sprite manifest must be a list or an object with a 'sprites' array.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--check-files", action="store_true")
    args = parser.parse_args()

    data = json.loads(args.manifest.read_text(encoding="utf-8-sig"))
    sprites = get_sprites(data)
    errors = []

    for sprite in sprites:
        asset_id = sprite.get("id", "<missing id>")
        missing = REQUIRED_TOP - set(sprite)
        if missing:
            fail(errors, asset_id, f"missing fields: {', '.join(sorted(missing))}")
            continue

        directions = sprite["directions"]
        if len(directions) not in (8, 16):
            fail(errors, asset_id, "directions must contain 8 or 16 entries")
        if len(directions) == 8 and set(directions) != VALID_DIRECTIONS_8:
            fail(errors, asset_id, "8-direction sprites must use n, ne, e, se, s, sw, w, nw")

        pivot = sprite["pivot"]
        if not (isinstance(pivot, list) and len(pivot) == 2 and all(isinstance(v, int) for v in pivot)):
            fail(errors, asset_id, "pivot must be [x, y] integers")

        animations = sprite["animations"]
        for name in sprite["required_animations"]:
            if name not in animations:
                fail(errors, asset_id, f"missing required animation '{name}'")

        for name, anim in animations.items():
            frames = anim.get("frames")
            if not isinstance(frames, int) or frames <= 0:
                fail(errors, asset_id, f"animation '{name}' has invalid frame count")
            if name == "attack" and "hit_frame" not in anim:
                fail(errors, asset_id, "attack animation is missing hit_frame")
            if name == "death" and anim.get("loop") is not False:
                fail(errors, asset_id, "death animation must set loop=false")
            if args.check_files:
                for file_name in anim.get("files", []):
                    if not (args.root / file_name).exists():
                        fail(errors, asset_id, f"missing file: {file_name}")

        if args.check_files and sprite.get("preview") and not (args.root / sprite["preview"]).exists():
            fail(errors, asset_id, f"missing preview: {sprite['preview']}")

    if errors:
        print("Sprite manifest validation failed:")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"Sprite manifest OK: {len(sprites)} sprite entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
