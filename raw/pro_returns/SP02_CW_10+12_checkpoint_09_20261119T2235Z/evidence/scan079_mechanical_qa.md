# Scan079 mechanical QA

Checked: 2026-11-19 20:12:21 UTC. Syntax checks: 2026-11-19 20:12:22 UTC.

**Result: all requested mechanical checks passed.** No transcription decision was made.

## Counts

| Item | Result |
| --- | ---: |
| Finalized page bytes | 3892 |
| Exact asserted edits | 24 |
| Change records | 35 |
| Loci against C | 20 |
| Loci against H | 34 |
| Crop recipes | 39 |
| Inventory rows, all transcribed=yes | 78 |
| Remaining doubt records, preserved | 10 |
| Source dimensions from header | 1683 × 2153 |

The record contains **39 crop recipes**; root's provisional estimate was 38. The confirmed byte length, changes, inventory count, and dimensions agree with root's supplied values.

## Checks

Record identity, map correspondence, metadata schema, change kinds and flags, source-C and page hashes all agree. Every edit has its asserted sequential occurrence count, and exact replay from C produces the finalized page bytes.

All crop IDs and references resolve; source paths, transform parameters, and source-pixel bounds are valid. Inventory normalization and overrides agree with resolved rows. Inventory, collation, changes, count rows, and all remaining-doubt rows match their current report projections.

The root script passes Python AST parsing without execution or bytecode generation. The page passes lexical brace, math-delimiter, environment, and group-boundary checks. No TeX compilation was performed.

Source: `source/SP02_CW_10+12_scans/B10-06_10_scan079.jpg`; file bytes: 794513. Image access was limited to `PIL.Image.open(source).size`. No pixel content was decoded, rendered, or viewed.

## Input identities

| Input | SHA256 |
| --- | --- |
| `pages/B10-06_10_scan079.tex` | `77bccd840ea4f25c7fe3f6ae80b8270730714794ee10277c3e2a9233c292f593` |
| `documentation/page_records/B10-06_10_scan079.json` | `25dc5e326e20562665e27a245bdb7d1ebba7e0ecfe5a86cd2e779b7640982ab4` |
| Witness C `codex/B10-06/pages/B10-06_10_scan079.tex` | `fd12de4bf53e35dae8f315e35cc4716a02846e982b878b86170aeb165da3ba65` |
| `work/record079.py` | `316641d531581eecf7156fdf4f681f9859bfb0aeecf1e916b9a4bce56a3c7a58` |
| Canonical crop-recipe metadata | `47d6050f5fc67844da0e43df60d7914a0cd034a603d5d1d46b7fe72e249419da` |

The companion `scan079_mechanical_qa.json` records every edit's expected/actual count, helper identities, inventory and report hashes, and syntax evidence.

## Root-supplied audit reminder

Root flagged the unresolved classification-overprint detail on scan079. This QA records that reminder only; it does not identify, classify, or adjudicate the overprinted reading. Existing root uncertainty records are preserved.

## Reproduction

From the workspace root:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_page.py SP02_CW_10+12/documentation/page_records/B10-06_10_scan079.json
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/validate_tex.py SP02_CW_10+12/pages/B10-06_10_scan079.tex --json
```

These commands do not finalize or write a page. Crop bounds can be repeated with `resolve_scan_source()`, header dimensions from `Image.open(source).size`, and `validate_crop_metadata(recipe, dimensions)`.

Original witnesses and scans are external dependencies. Scan payload bytes were not hashed under this header-only scope. Shared-report hashes identify the checked snapshot and may change as later pages finalize. At this snapshot `documentation/root_scripts/record079.py` was absent and awaits the normal checkpoint documentation refresh.

Pages, records, and scripts were preserved. No files were removed; no context, compilation, audit, freeze, packaging, or upload action occurred.

