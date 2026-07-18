#!/usr/bin/env python3
"""Validate an RTS asset registry without third-party dependencies."""
import argparse
import json
import re
from pathlib import Path

ALLOWED_STATUSES = {
    "planned",
    "in_progress",
    "generated",
    "validation_failed",
    "needs_visual_review",
    "needs_audio_review",
    "needs_music_review",
    "needs_fix",
    "approved",
    "deprecated",
}
ALLOWED_TYPES = {
    "unit",
    "building",
    "terrain",
    "ui",
    "vfx",
    "sfx",
    "music",
    "voice",
    "mechanic",
    "narrative",
}
REQUIRED = {"id", "type", "status", "source", "outputs", "qa", "provenance"}
ID_RE = re.compile(r"^[a-z0-9_]+$")


def get_assets(data):
    if isinstance(data, dict) and "assets" in data:
        return data["assets"]
    if isinstance(data, list):
        return data
    raise SystemExit("Registry must be a list or an object with an 'assets' array.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("registry", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--check-files", action="store_true")
    args = parser.parse_args()

    data = json.loads(args.registry.read_text(encoding="utf-8-sig"))
    assets = get_assets(data)
    errors = []
    seen = set()

    for idx, asset in enumerate(assets):
        label = asset.get("id", f"asset[{idx}]") if isinstance(asset, dict) else f"asset[{idx}]"
        if not isinstance(asset, dict):
            errors.append(f"{label}: asset card must be an object")
            continue

        missing = REQUIRED - set(asset)
        if missing:
            errors.append(f"{label}: missing fields: {', '.join(sorted(missing))}")

        asset_id = asset.get("id")
        if not isinstance(asset_id, str) or not ID_RE.match(asset_id):
            errors.append(f"{label}: id must use lowercase letters, digits, and underscores")
        elif asset_id in seen:
            errors.append(f"{label}: duplicate id")
        else:
            seen.add(asset_id)

        if asset.get("type") not in ALLOWED_TYPES:
            errors.append(f"{label}: invalid type '{asset.get('type')}'")
        if asset.get("status") not in ALLOWED_STATUSES:
            errors.append(f"{label}: invalid status '{asset.get('status')}'")

        for field in ("source", "outputs"):
            if not isinstance(asset.get(field), list):
                errors.append(f"{label}: {field} must be a list")
                continue
            if args.check_files:
                for file_name in asset[field]:
                    if not (args.root / file_name).exists():
                        errors.append(f"{label}: missing {field} file: {file_name}")

        qa = asset.get("qa", {})
        if asset.get("status") == "approved":
            if qa.get("technical_validation") != "passed":
                errors.append(f"{label}: approved asset must have qa.technical_validation=passed")
            if qa.get("human_review") not in ("passed", "not_required"):
                errors.append(f"{label}: approved asset must have qa.human_review=passed or not_required")

    if errors:
        print("Asset registry validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Asset registry OK: {len(assets)} assets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
