# Scan081 mechanical QA

Metadata checked: 2026-11-19 20:25:28 UTC. Syntax checked: 2026-11-19 20:25:29 UTC.

**Result: all requested mechanical checks passed.** This report makes no transcription judgment.

## Counts

| Item | Result |
| --- | ---: |
| Finalized page bytes | 3820 |
| Exact asserted edits | 12 |
| Change records | 32 |
| Loci against C / H | 13 / 32 |
| Crop recipes | 31 |
| Inventory rows, all transcribed=yes | 80 |

## Verification

Record identity, map correspondence, source-C and page hashes, schema, change kinds, flags, and confidence fields agree. Every edit has its asserted sequential occurrence count; exact replay from C reproduces the finalized page bytes.

All crop IDs and individual/composite references resolve. Source paths remain inside the known scan directory, transformation metadata is valid, and each source-pixel box is within the image-header dimensions. Inventory normalization and overrides agree with resolved rows. Inventory, collation, changes, counts, and doubt rows match their record projections.

The finalized root script passes Python AST parsing without execution or bytecode. The page passes lexical brace, math-delimiter, environment, and group-boundary checks. No TeX compilation occurred.

## Image-header metadata

| Source | Width | Height | File bytes |
| --- | ---: | ---: | ---: |
| `source/SP02_CW_10+12_scans/B10-06_10_scan081.jpg` | 1676 | 2151 | 649248 |

Image access was limited to `PIL.Image.open(source).size`; no pixel content was decoded, rendered, or viewed. No OCR or context access occurred.

## Input identities

| Input | SHA256 |
| --- | --- |
| `Page pages/B10-06_10_scan081.tex` | `bd8a7d0c891aee5ae8e4382f0fdf4a9acecfdac024d002e1cc7546e63344d185` |
| `Record documentation/page_records/B10-06_10_scan081.json` | `f0dcc9d9ae4865427bda37b9c975766cdfddaa9008719dca36a37a586475cce2` |
| `Witness C codex/B10-06/pages/B10-06_10_scan081.tex` | `0dd12b6546357e154dfb7b860f4e04dd6d5aa3bdb47627601a31cd7c85a43650` |
| `Root script work/record081.py` | `89a53fd2c9c418312edf24e2dfb9dd853524e3de66eefa1b513fdacbcb6aa467` |
| `Canonical crop metadata` | `af047603ffb76d364da7809eb0881d7b9926a8e43a10f3a60cede9eedf78a5a5` |

The companion `scan081_mechanical_qa.json` records each edit's expected and actual count, helper hashes, inventory-metadata hash, report-snapshot hashes, and syntax evidence.

Root's supplied byte length, change count, inventory count, and crop count all match.

## Reproduction and scope

From the workspace root, existing commands repeat edit-count/inventory preparation and lexical checks without finalizing or writing a page:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_page.py SP02_CW_10+12/documentation/page_records/B10-06_10_scan081.json
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/validate_tex.py SP02_CW_10+12/pages/B10-06_10_scan081.tex --json
```

Crop bounds can be repeated with `resolve_scan_source()`, `Image.open(source).size`, and `validate_crop_metadata(recipe, dimensions)`. Original witnesses and scans remain external dependencies. Scan payload bytes were not hashed under this header-only scope. Shared-report hashes identify the checked snapshot and may change when later pages finalize.

At this snapshot `documentation/root_scripts/record081.py` was absent; it awaits the normal checkpoint documentation refresh.

Pages, records, and scripts were preserved. No files were removed and no audit, freeze, packaging, or upload action occurred.

