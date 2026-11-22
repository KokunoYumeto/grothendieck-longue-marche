# Packaging reference and geometry repair

Date: 2026-11-21 20:19 UTC. Reader: reader_a, GPT-6 Astra Pro, effort not exposed, run SP92.

Scope authorized by root: edit `scripts/portable_archive.py` and `scripts/restore_png_crops.py`, plus this technical log. No archive was created or changed. No evidence image, manuscript reading, seal, comparison data, or existing record was modified.

## Observed issue

Basename-wide replacement would rename 333 historical display-path fields in 16 blind manifests/reader records, although the external scratch display PNGs were never re-encoded. The current inventory has 586 exact bare-basename JSON values identifying evidence crops; all occur under `viewed_crops` or `crops_viewed`.

The only embedded crop-container digests found are the 12 `crops[*].crop_sha256` fields in `second/151_scan005_reader_record.json`. They correctly identify the original PNG bytes. They remain original evidence provenance, while the encoding manifest separately identifies the stored encoding. No stale second-reading digest was found: all 23 existing second TSVs have no crop-basename replacement hits; all 11 explicit reader TSV hashes, 69 comparison-input hashes, and 50 first/box seal hashes matched at audit time. Only schemas, paths, and hashes were inspected; manuscript text was not displayed or read.

## Repair

- Both directions now use one shared rewrite helper. It changes qualified `crops/<filename>` references and exact bare JSON values only under the two explicit crop keys. Non-crops display paths, unknown bare-name fields, bare names in prose, and digest values are preserved.
- The restoration script has an import-safe `main` guard, allowing the packager to use the same helper without executing restoration. Qualified-only edits preserve surrounding text formatting. JSON is reserialized only when an approved bare-name value changes.
- Second-reading TSVs are now explicitly frozen alongside first readings, box lists, page files, and combined transcriptions. Restoration also protects all descendants of `pages/`.
- Before JPEG XL decoding, both scripts call `ffprobe` and require the encoded width and height to match the expected image dimensions. This supplements the existing pixel-byte/digest checks. Restoration also checks an existing target PNG's dimensions.
- The generated `CROP_ENCODING.md` explains original `crop_sha256` provenance, distinguishes original-file, stored-file, and pixel hashes, and states that historical display paths remain as observed. It documents the added `ffprobe` requirement.

## Validation

Executed only synthetic string/JSON checks and mocked probe responses: 16 reference-string cases, JSON key-scope and inverse-mapping checks, preservation of historical paths and hash values, and five mocked ffprobe cases including rejection of swapped dimensions. Both edited scripts parsed successfully. `ffprobe` is available at `/usr/bin/ffprobe`. No image was opened/decoded, no TeX was run, no package/restoration entry point was invoked, and no data file was written by validation.

Script hashes after the repair:

- `portable_archive.py`: `4f30a574efcae26de3037fe445b71f9dbb2ac11fd5f9d90e720f1bbd623bdaed`
- `restore_png_crops.py`: `4787d48dcf2e27d864cce079b99b201622735b6106fea13ddadcf45c4ade0dcc`

An already running repack keeps the code it loaded at launch. These repairs apply to subsequent invocations and to final source packages built from the updated scripts; no existing checkpoint ZIP was altered.
