# Verify this Clink fonts repository

Read `README.md`, `PROMPT.md`, `tools/build-manifest.py`, and `tools/validate-manifest.py`. Audit the repository; do not modify files unless asked to fix a specific finding.

Run:

```sh
python3 tools/build-manifest.py
python3 tools/validate-manifest.py
```

Inspect every `Fonts/*.ttf` and `Fonts/*.otf` asset and its metadata. Confirm each font has a unique permanent lowercase kebab-case id, accurate visible name/version, complete attribution, a licence allowing redistribution and iOS embedding (`OFL-1.1`, `Apache-2.0`, `MIT`, or `CC0-1.0`), and the required licence text where applicable. Verify each declared PostScript name against the binary with an available font-inspection tool; never infer it from the filename. Confirm that hashes, byte counts, and release URLs are generator-produced, not hand-maintained.

Check that `manifest.json` is regenerated and complete, binaries and metadata retain a stable identity, and no unexpected workflow changes exist. Report commands, validation output, every font checked, and precise failures or unrun checks. Do not report a clean result if licence or embedded-name verification was not possible.
