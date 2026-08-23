# Clink Fonts

Verified, redistributable font packs for Clink.

This repository must contain only fonts whose licence permits redistribution in
an iOS app. Accepted SPDX identifiers are `OFL-1.1`, `Apache-2.0`, `MIT`, and
`CC0-1.0`. Do not add Apple fonts, personal-use fonts, trial fonts, or any font
whose licence does not explicitly permit distribution and embedding.

## Publishing a font

Publish a GitHub Release containing the font (`.otf` or `.ttf`) and update the
release `manifest.json` with one entry:

```json
{
  "id": "atkinson-hyperlegible-next",
  "name": "Atkinson Hyperlegible Next",
  "version": "2025.1",
  "license": "OFL-1.1",
  "attribution": "Copyright (c) Braille Institute. Licensed under the SIL Open Font License 1.1.",
  "postScriptName": "AtkinsonHyperlegibleNext-Regular",
  "asset": {
    "path": "Fonts/AtkinsonHyperlegibleNext-Regular.ttf",
    "url": "https://github.com/anti-ltd/clink-fonts/releases/download/v2025.1/AtkinsonHyperlegibleNext-Regular.ttf",
    "sha256": "lowercase-sha256-of-the-release-asset",
    "byteCount": 123456
  }
}
```

Clink downloads only assets from this repository's GitHub Releases, checks their
SHA-256 checksum, verifies the declared PostScript name from the binary, and
installs the font per process. A theme stores only the verified PostScript name.
