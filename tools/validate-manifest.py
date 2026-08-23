#!/usr/bin/env python3
import json
import re
import sys

ALLOWED = {"OFL-1.1", "Apache-2.0", "MIT", "CC0-1.0"}
SHA256 = re.compile(r"^[0-9a-f]{64}$")

with open("manifest.json", encoding="utf-8") as source:
    manifest = json.load(source)

errors = []
for font in manifest.get("fonts", []):
    asset = font.get("asset", {})
    if font.get("license") not in ALLOWED:
        errors.append(f"{font.get('id', '<unknown>')}: licence must be one of {sorted(ALLOWED)}")
    if not font.get("attribution") or not font.get("postScriptName"):
        errors.append(f"{font.get('id', '<unknown>')}: attribution and postScriptName are required")
    if not asset.get("path", "").lower().endswith((".otf", ".ttf")):
        errors.append(f"{font.get('id', '<unknown>')}: asset must be .otf or .ttf")
    if not SHA256.fullmatch(asset.get("sha256", "")):
        errors.append(f"{font.get('id', '<unknown>')}: asset SHA-256 must be lowercase hex")

if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)
