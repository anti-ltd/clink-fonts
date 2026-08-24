# Add a Clink font pack

You are adding one redistributable font asset to this repository. Read `README.md`, `tools/build-manifest.py`, and `tools/validate-manifest.py` before changing anything. Confirm the font licence permits redistribution and iOS embedding; only `OFL-1.1`, `Apache-2.0`, `MIT`, and `CC0-1.0` are accepted.

Place exactly one `.ttf` or `.otf` in `Fonts/`, including its licence text where needed. Add metadata for it to the `METADATA` mapping in `tools/build-manifest.py`: permanent lowercase kebab-case id, visible name, version, accepted licence identifier, complete attribution, and the exact PostScript name embedded in the font binary. Never guess the PostScript name from the filename—inspect it with a font tool when possible. Keep the binary and metadata identity stable across updates.

Run:

```sh
python3 tools/build-manifest.py
python3 tools/validate-manifest.py
```

Include the regenerated `manifest.json`. Do not hand-edit checksums, byte counts, or release URLs; the generator owns them. Do not alter the release workflow. Finish by identifying the source and licence of the font, its PostScript name, the files added, and the validation result.
