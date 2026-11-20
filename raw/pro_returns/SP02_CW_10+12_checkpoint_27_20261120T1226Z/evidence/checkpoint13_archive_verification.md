# Checkpoint13 archive verification

Verified: 2026-11-20 01:41:35 UTC
Archive created: 2026-11-20T01:39:05.888986+00:00

**PASS**

| Check | Result |
| --- | --- |
| ZIP entries | 424 |
| ZIP bytes | 2477594 |
| Uncompressed bytes | 12575988 |
| CRC test | True |
| Entry SHA256 matches | 424 |
| Finalized pages / records | 73 / 73 |
| Required provisional scan127 files | 3 / 3 |
| Excluded source/scan/witness/context/image/archive entries | 0 |
| Archive unchanged during verification | True |

Archive SHA256: e6124d40a365b702cb828f4e2bfec321a1f2d5a3a3d5e92ec6ff2c92c0473bf0

Combined transcription: 307086 bytes; SHA256 4ffb8aeb2fa5b76c761a376cc5bee80fa7cd213a7f7668794bf4b9ea8a8998dd.

## Snapshot comparison

Every ZIP entry was checked against the captured work/checkpoint13_manifest.json path/size/SHA256 list. The 73 finalized pages and 73 records additionally match the archived checkpoint13_preparation_073 metadata. The combined transcription matches that same archived preparation. No current mutable progress log or other live output entry was used as a ZIP comparison target.

## Provisional scan127 entries

- documentation/scan127_provisional_013.md — 5883 bytes; SHA256 da365b81446f3f356adf33600fd6528a7c8c8d676e2279a55ca2e876ce4cd539
- documentation/scan127_provisional_013_crops.json — 12651 bytes; SHA256 777171841fb24f7d6270898d45fbdc42798ffdadf4976b2518e9b71812f5d5fd
- documentation/scan127_provisional_013_crop_script.py — 3044 bytes; SHA256 2d973d231569a6e1de8e206232a5574b2db3eeb5fb4ae8b8f1aa9fca63db2263

## Findings

None. All requested archive-integrity and inclusion checks passed.

## Scope

CRC/hash checks streamed bytes without interpreting prose or rendering files. No images, witness source files or context were opened; the archive was not extracted. No finalized page, record, live report, progress log, CHECK_EVENTS file, audit/freeze state or archive was modified. No archive was created or uploaded. Only this evidence and its companion JSON were written after packaging.
