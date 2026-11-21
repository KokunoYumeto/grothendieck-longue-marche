# Reader B: lossless archive engineering

## Outcome

`result/scripts/compact_archive_v2.py` is complete and verified against a full restoration of checkpoint 05. Its source matches the script stored inside the tested transport archive.

| File set | Compact size | Headroom below 512 MiB |
| --- | ---: | ---: |
| Checkpoint 05, previous v1 transport | 525,219,148 bytes | 11,651,764 bytes |
| Checkpoint 05, new v2 transport | 464,307,470 bytes | 72,563,442 bytes |
| Current-tree projection, 852 PNGs | 492,975,422 bytes | 43,895,490 bytes |

The actual checkpoint saving is **60,911,678 bytes (11.60%)**. The current-tree projection covers 1,403 source entries and uses 800 lossless JPEG XL payloads plus 52 exact derivations. It is a captured-file-set projection; later notes, reports, or new crops will change the final size. Projection completed at 2026-11-21T02:07:52.382261+00:00.

## Method and preservation

The new representation stores verified recipes for redundant helper images and 180-degree companion views. A parent must be another PNG present in the same original package. Recipes record the complete crop, resize, rotation, channel, contrast, and sharpening operations used by the retained original helper generator. Each candidate was executed and its **complete resulting PNG bytes** compared against the existing original PNG before acceptance. Every one of the 52 current candidates passed. Five were added after checkpoint 05, so its archive uses 47 recipes.

Ordinary images retain the existing lossless-JXL representation and cache. Other files remain directly readable with unchanged bytes. Exact-byte aliases are supported, although the current PNG set contained no duplicates. The manifest records every original entry's path, byte count, and SHA256, every image payload or full parent recipe, and all required reconstruction parameters. Dependencies are checked for cycles. Restoration uses included parent data; attached scans and the external encoding cache are unnecessary.

The new transport ZIP is `deliverables/compact_v2/SP83_C13_148+149_checkpoint_05.zip`. It is a transport copy of the existing checkpoint, with SHA256:

`14c1ae4f606f025daca5cbe7803d4467a33d25461893c55e4f5c6e2e6103e60f`

The original checkpoint remains unchanged; its hash still equals the pre-existing v1 manifest:

`442b894bcd547cd9692d7f01c37c7365cc4f5319635be7881bfb6d33cd8cc2ce`

## Full verification

The new transport was extracted into `archive_v2_verification/cp05`, then its **archived** restoration script restored and verified all 778 images. A separate verifier reopened the original checkpoint ZIP and compared every source entry directly with its restored counterpart. All **1,244 entries passed: 778 PNGs and 466 other files**. There were no mismatches.

Details are retained in `reader_b_archive_restore_verification.json`, including each original path/hash. The independent test generator is `reader_b_verify_archive_v2.py`. All working files are retained. No accepted page, record, frozen TSV, or existing aggregate was edited, and no upload was performed.

## Commands for the main reader

Run from the workspace root after the next original package has been frozen:

```sh
python result/scripts/compact_archive_v2.py \
  deliverables/SP83_C13_148+149_checkpoint_06.zip \
  deliverables/compact_v2/SP83_C13_148+149_checkpoint_06.zip \
  --report result/qa/cp06_compact_v2_report.json
```

Use a destination that does not already exist. The input must be the original package, rather than a previously compacted ZIP. The same positional command works for the final original package and its distinct compact destination.

For a current-tree size projection:

```sh
python result/scripts/compact_archive_v2.py --analyze-tree result \
  --report result/qa/current_compact_v2_projection.json
```

After extracting a v2 ZIP, restore all original PNG names with:

```sh
python scripts/restore_crops.py
```

To restore and verify every original entry:

```sh
python scripts/compact_archive_v2.py --verify-all
```

The tested environment is Python 3.12.14, Pillow 13.0.0, NumPy 2.3.5, zlib 1.3.2, and FFmpeg with JPEG XL decoding. Exact versions are recorded in the manifest. A different PNG encoder version may yield different PNG bytes even for identical pixels; restoration fails before writing a nonmatching file. Matching the recorded library versions reproduces the tested bytes.

## Handoff documentation

The main reader should update `result/image_transport_note.md` before the next/final package: its current wording describes only v1. V2 includes `CROP_COMPRESSION_MANIFEST_V2.json` and `CROPS_README_V2.md`, while keeping `scripts/restore_crops.py` as the entry point. The note should cover exact parent-crop derivations as well as lossless JXL. That existing note was left unchanged under the read-only assignment.

The separate static QA findings remain in `reader_b_static_findings.json` and `reader_b_static_findings.md`.
