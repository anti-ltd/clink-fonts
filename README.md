<p align="center">
  <img src="https://raw.githubusercontent.com/anti-ltd/clink-language-packs/main/icon-1024.png" width="96" alt="Clink app icon">
</p>

<h1 align="center">Clink fonts</h1>

<p align="center">Open, redistributable font packs for Clink.</p>

Clink can install verified font files and use them in custom keyboard themes. Font binaries stay separate from themes: a theme stores only the verified PostScript name of the selected face. This repository accepts only fonts whose licences permit redistribution and embedding in an iOS app.

## Official Clink repositories

[Language packs](https://github.com/anti-ltd/clink-language-packs) · [Layouts](https://github.com/anti-ltd/clink-layouts) · [Profiles](https://github.com/anti-ltd/clink-profiles) · [Themes](https://github.com/anti-ltd/clink-themes) · [Panels](https://github.com/anti-ltd/clink-panels) · [Actions](https://github.com/anti-ltd/clink-actions) · [Fonts](https://github.com/anti-ltd/clink-fonts)

## Included fonts

The official repository currently includes **Basic**, an OFL-1.1-licensed sans-serif font from Sorkin Type Co. It is included as a small test font so Clink's repository discovery, checksum verification, Core Text registration, and theme typography picker can be exercised end to end.

## Make your first font pack

You do not need to build Clink or write a custom installer.

1. Fork this repository.
2. Add an `.otf` or `.ttf` file to the [`Fonts/`](Fonts) folder.
3. Confirm that its licence permits redistribution and embedding. Accepted SPDX identifiers are `OFL-1.1`, `Apache-2.0`, `MIT`, and `CC0-1.0`.
4. Add the font metadata to `tools/build-manifest.py` with a permanent lowercase `id`, visible `name`, licence, attribution, exact PostScript name, and release version.
5. Run `python3 tools/build-manifest.py` to generate the manifest, then run `python3 tools/validate-manifest.py`.
6. Keep the `id` stable across updates and use a version that identifies the font release.
7. Push to `main`. The included GitHub Action validates the manifest and publishes the checked-in fonts, license files, and `manifest.json` to the `latest` GitHub Release.

A complete manifest entry looks like this:

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

The `postScriptName` must match the name inside the actual binary. Do not use the filename or a display name in its place. The release asset URL must point to this repository's GitHub Release. The generator fills the hash, byte count, and release URL from the checked-in asset.

## Add your repository to Clink

After you publish your first GitHub Release, open **General → Repositories** in Clink and add `owner/repository`, for example:

```text
your-name/my-clink-fonts
```

Then open **Customize → Look**, go to the theme editor's **Typography** section, and install a font from the repository. The font becomes available to custom themes after Clink verifies and registers it. Fonts are data-only, but only add repositories whose licensing and release contents you trust.

## What Clink verifies

Clink accepts only public HTTPS GitHub release manifests. Every font must use an approved redistributable licence, be an `.otf` or `.ttf` file within the size limit, and match the manifest's byte count and SHA-256 hash. Clink also reads the binary's font descriptors and requires the declared PostScript name to be present before installation.

Fonts are downloaded into a staging directory, verified, registered for the current process, and then moved into the installed pack directory. A theme stores only the PostScript name; the font binary remains in the verified font-pack store.

## Publishing is automatic

Keep `Fonts/`, `tools/`, and `.github/workflows/` in your fork. Add or update a font, regenerate the manifest, and push to `main`. GitHub Actions validates the manifest and refreshes the `latest` release so Clink can download the verified assets.
