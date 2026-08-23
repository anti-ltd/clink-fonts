#!/usr/bin/env python3
"""Build clink-fonts/manifest.json from the checked-in font assets."""
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "anti-ltd/clink-fonts")

METADATA = {
    "Basic-Regular.ttf": {
        "id": "basic",
        "name": "Basic",
        "version": "latest",
        "license": "OFL-1.1",
        "attribution": "Copyright (c) 2011-2014, Sorkin Type Co (www.sorkintype.com), with Reserved Font Name 'Basic'. Licensed under the SIL Open Font License 1.1.",
        "postScriptName": "Basic-Regular",
    },
}

fonts = []
for path in sorted((ROOT / "Fonts").iterdir()):
    if path.suffix.lower() not in {".ttf", ".otf"}:
        continue
    metadata = METADATA.get(path.name)
    if metadata is None:
        raise SystemExit(f"missing metadata for {path.name}")
    raw = path.read_bytes()
    fonts.append({
        **metadata,
        "asset": {
            "path": f"Fonts/{path.name}",
            "url": f"https://github.com/{REPOSITORY}/releases/download/latest/{path.name}",
            "sha256": hashlib.sha256(raw).hexdigest(),
            "byteCount": len(raw),
        },
    })

if not fonts:
    raise SystemExit("no .ttf or .otf assets found")

(ROOT / "manifest.json").write_text(
    json.dumps({"version": "latest", "fonts": fonts}, indent=2) + "\n",
    encoding="utf-8",
)
