# Scan075 mechanical QA

Checked: 2026-11-19 20:03:09 UTC. Syntax checks: 2026-11-19 20:02:26 UTC.

**Result: all requested mechanical checks passed. No transcription judgment is made by this report.**

## Counts

| Item | Count |
| --- | ---: |
| Exact asserted edits | 24 |
| Change records | 52 |
| Loci against C | 23 |
| Loci against H | 50 |
| Crop recipes | 40 |
| Inventory rows | 48 |

All inventory rows are marked `transcribed=yes`.

## Checks performed

- The record identity and stored map row agree with the page map.
- The original witness-C byte hash and finalized page byte hash agree with the record.
- Every sequential edit has exactly its asserted occurrence count. Replaying the edits from C produces the finalized page bytes exactly.
- Record fields, change kinds, flags, confidence values, and crop parameters satisfy the existing metadata validator.
- Every crop source resolves safely to this scan. Crop IDs are unique, every change's individual or composite crop reference resolves, and every box is within the source dimensions.
- Inventory normalization, explicit overrides, and resolved rows agree. Inventory, collation, change tables, counts, and doubt rows agree with their current report projections.
- The root script passes Python AST parsing without execution or bytecode generation.
- The page passes lexical brace, math-delimiter, environment, and group-boundary checks. No TeX compilation was performed.
- Input pages, records, and scripts remained unchanged during verification.

## Image-header metadata

| Source | Width | Height | File bytes |
| --- | ---: | ---: | ---: |
| `source/SP02_CW_10+12_scans/B10-05_10_scan075.jpg` | 1674 | 2152 | 748846 |

Bounds use source-pixel boxes with exclusive right and bottom edges. Image access was limited to `PIL.Image.open(source).size`; no pixel content was decoded, rendered, or viewed.

## Input identities

| Input | SHA256 |
| --- | --- |
| Page `pages/B10-05_10_scan075.tex` | `82a3236dc97c71a77b9d49411512ff932b9b8bef6788a5b5afbf5a62ef73deaf` |
| Record `documentation/page_records/B10-05_10_scan075.json` | `19886424c9226f2022316365035ad035a149826e9cd17d94fabfd481600b50d9` |
| Witness C `codex/B10-05/pages/B10-05_10_scan075.tex` | `00434b031147ccd31f5f5891a86b7f4f063438ead4305a6a2e25613409ad3aaa` |
| Root script `work/record075.py` | `c60caa1a711404f12e20bf32553f0c82ee525e22289285a1c9faa417fc1099ac` |
| Canonical crop-recipe metadata | `9887eff9f6ab2d00c14c004b927751f47a86d48e3a6fe3d13ad967ad7e2ab09f` |

The adjacent `scans075_077_mechanical_qa.json` records every edit's expected and actual count, helper hashes, report-snapshot hashes, inventory-metadata hash, and the finalized-count snapshot.

## Reproduction and remaining dependencies

From the workspace root, these existing commands repeat edit-count/inventory preparation and lexical checks without finalizing or writing a page:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_page.py SP02_CW_10+12/documentation/page_records/B10-05_10_scan075.json
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/validate_tex.py SP02_CW_10+12/pages/B10-05_10_scan075.tex --json
```

Crop metadata can be rechecked with `resolve_scan_source()`, `Image.open(source).size`, and `validate_crop_metadata(recipe, dimensions)`; no crop rendering is needed.

The original witness packet and scan directory are external dependencies and are intentionally omitted from deliverable archives. Scan payloads were not hashed during this header-only check. The root script's copy at `documentation/root_scripts/record075.py` was absent at this snapshot and should be captured by the normal checkpoint documentation refresh. Later page finalizations will change shared-report hashes; the recorded hashes identify the checked snapshot.

This QA did not open context, view scan content, compile TeX, change readings, create audit/freeze events, package, or upload anything.

