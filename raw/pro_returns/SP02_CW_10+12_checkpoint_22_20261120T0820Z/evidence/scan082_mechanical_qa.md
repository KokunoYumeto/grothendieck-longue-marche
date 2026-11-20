# Scan082 mechanical QA

Metadata checked: 2026-11-19 20:36:23 UTC. Syntax checked: 2026-11-19 20:36:25 UTC.

**Result: all requested mechanical checks passed.** This report makes no transcription judgment.

## Counts

| Item | Result |
| --- | ---: |
| Finalized page bytes | 5674 |
| Exact asserted edits | 27 |
| Change records | 53 |
| Loci against C / H | 27 / 45 |
| Crop recipes | 53 |
| Inventory rows, all transcribed=yes | 99 |

## Verification

Record identity, map correspondence, source-C and page hashes, schema, change kinds, flags, and confidence fields agree. Every edit has its asserted sequential occurrence count; exact replay from C reproduces the finalized page bytes.

All crop IDs and individual/composite references resolve. Source paths remain inside the known scan directory, transformation metadata is valid, and each source-pixel box is within the image-header dimensions. Inventory normalization and overrides agree with resolved rows. Inventory, collation, changes, counts, and doubt rows match their record projections.

The finalized root script passes Python AST parsing without execution or bytecode. The page passes lexical brace, math-delimiter, environment, and group-boundary checks. No TeX compilation occurred.

## Image-header metadata

| Source | Width | Height | File bytes |
| --- | ---: | ---: | ---: |
| `source/SP02_CW_10+12_scans/B10-06_10_scan082.jpg` | 1687 | 2157 | 919486 |

Image access was limited to `PIL.Image.open(source).size`; no pixel content was decoded, rendered, or viewed. No OCR or context access occurred.

## Input identities

| Input | SHA256 |
| --- | --- |
| `Page pages/B10-06_10_scan082.tex` | `20c82616997a6b50bd55744397728da7bedf7b8c1a76e4701712edacd9debde5` |
| `Record documentation/page_records/B10-06_10_scan082.json` | `851ec79e11824898713b32eae95fd371c14c0d236da26674551aebe4be34e819` |
| `Witness C codex/B10-06/pages/B10-06_10_scan082.tex` | `8861c702f3e204c8f6be7323ee876137517d64fb49044737801d51279b332d92` |
| `Root script work/record082.py` | `bf116d8343cd58c29f24c53b2ad068827a3e6331e310939aacbbdd907373a290` |
| `Root JSON work/record082.json` | `c54899131b2589855c347a6632a6ad86ee4e64111ee65068c00a60a73d6327af` |
| `Canonical crop metadata` | `a920fa4a893d4f45557279900f3b837d33e2073be5314eaf4995127f5bd4fa58` |

The companion `scan082_mechanical_qa.json` records each edit's expected and actual count, helper hashes, inventory-metadata hash, report-snapshot hashes, and syntax evidence.

Root's supplied byte length, change count, inventory count, and crop count match. All **16 root-authored fields** in `work/record082.json` agree with the finalized record after cote/scan type normalization. The final record adds only the six generated map/key/hash/inventory/timestamp fields. No root JSON or script was executed or modified.

## Reproduction and scope

From the workspace root, existing commands repeat edit-count/inventory preparation and lexical checks without finalizing or writing a page:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_page.py SP02_CW_10+12/documentation/page_records/B10-06_10_scan082.json
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/validate_tex.py SP02_CW_10+12/pages/B10-06_10_scan082.tex --json
```

Crop bounds can be repeated with `resolve_scan_source()`, `Image.open(source).size`, and `validate_crop_metadata(recipe, dimensions)`. Original witnesses and scans remain external dependencies. Scan payload bytes were not hashed under this header-only scope. Shared-report hashes identify the checked snapshot and may change when later pages finalize.

At this snapshot `documentation/root_scripts/record082.py` was absent; it awaits the normal checkpoint documentation refresh.

Pages, records, and scripts were preserved. No files were removed and no audit, freeze, packaging, or upload action occurred.

