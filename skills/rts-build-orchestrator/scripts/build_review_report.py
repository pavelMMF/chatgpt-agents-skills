#!/usr/bin/env python3
"""Build a compact review report from an RTS asset registry."""
import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

REVIEW_STATUSES = {
    "needs_visual_review",
    "needs_audio_review",
    "needs_music_review",
    "needs_fix",
    "validation_failed",
}


def load_assets(path: Path):
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, dict) and "assets" in data:
        return data["assets"]
    if isinstance(data, list):
        return data
    raise SystemExit("Registry must be a list or an object with an 'assets' array.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("registry", type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    assets = load_assets(args.registry)
    by_status = Counter(asset.get("status", "missing_status") for asset in assets)
    by_type = Counter(asset.get("type", "unknown") for asset in assets)
    review = defaultdict(list)

    for asset in assets:
        status = asset.get("status", "missing_status")
        if status in REVIEW_STATUSES:
            review[status].append(asset.get("id", "<missing id>"))

    lines = ["# Asset Review Report", "", f"Total assets: {len(assets)}", "", "## By Status"]
    for status, count in sorted(by_status.items()):
        lines.append(f"- {status}: {count}")
    lines.extend(["", "## By Type"])
    for typ, count in sorted(by_type.items()):
        lines.append(f"- {typ}: {count}")
    lines.extend(["", "## Review Queue"])
    if review:
        for status, ids in sorted(review.items()):
            lines.append(f"### {status}")
            for asset_id in sorted(ids):
                lines.append(f"- {asset_id}")
    else:
        lines.append("No assets currently need review.")

    text = "\n".join(lines) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
