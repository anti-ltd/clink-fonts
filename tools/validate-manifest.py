#!/usr/bin/env python3
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {"OFL-1.1", "Apache-2.0", "MIT", "CC0-1.0"}
SHA256 = re.compile(r"^[0-9a-f]{64}$")
ID = re.compile(r"^[a-z0-9][a-z0-9-]*$")

try:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as error:
    raise SystemExit(f"manifest: {error}")

errors = []
seen_ids = set()
for font in manifest.get("fonts", []):
    font_id = font.get("id", "<unknown>")
    asset = font.get("asset", {})
    path_text = asset.get("path", "")
    path = ROOT / path_text

    if not ID.fullmatch(font.get("id", "")):
        errors.append(f"{font_id}: id must be lowercase kebab-case")
    if font.get("id") in seen_ids:
        errors.append(f"{font_id}: duplicate id")
    seen_ids.add(font.get("id"))
    if not font.get("name") or not font.get("version"):
        errors.append(f"{font_id}: name and version are required")
    if font.get("license") not in ALLOWED:
        errors.append(f"{font_id}: licence must be one of {sorted(ALLOWED)}")
    if not font.get("attribution") or not font.get("postScriptName"):
        errors.append(f"{font_id}: attribution and postScriptName are required")
    if not path_text.startswith("Fonts/") or ".." in path_text:
        errors.append(f"{font_id}: asset path must stay under Fonts/")
    if path.suffix.lower() not in {".otf", ".ttf"}:
        errors.append(f"{font_id}: asset must be .otf or .ttf")
    if not path.is_file():
        errors.append(f"{font_id}: asset is missing: {path_text}")
        continue

    raw = path.read_bytes()
    if len(raw) < 12 or raw[:4] not in {b"\x00\x01\x00\x00", b"OTTO", b"true", b"typ1"}:
        errors.append(f"{font_id}: asset does not have a recognised TrueType/OpenType header")
    if not SHA256.fullmatch(asset.get("sha256", "")):
        errors.append(f"{font_id}: asset SHA-256 must be lowercase hex")
    elif asset["sha256"] != hashlib.sha256(raw).hexdigest():
        errors.append(f"{font_id}: asset SHA-256 is incorrect")
    if asset.get("byteCount") != len(raw):
        errors.append(f"{font_id}: asset byteCount is incorrect")
    url = asset.get("url", "")
    if not url.startswith("https://github.com/"):
        errors.append(f"{font_id}: asset URL must be an HTTPS GitHub URL")
    if not asset.get("url", "").endswith(f"/releases/download/latest/{path.name}"):
        errors.append(f"{font_id}: asset URL must point to the latest release asset")

if not manifest.get("fonts"):
    errors.append("manifest must contain at least one font")

if errors:
    print("\n".join(errors), file=sys.stderr)
    raise SystemExit(1)

print(f"validated {len(manifest['fonts'])} font(s)")
