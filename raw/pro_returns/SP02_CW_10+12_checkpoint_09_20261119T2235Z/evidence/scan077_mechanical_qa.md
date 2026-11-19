# Scan077 mechanical QA

Checked: 2026-11-19 20:03:09 UTC. Syntax checks: 2026-11-19 20:02:26 UTC.

**Result: all requested mechanical checks passed. No transcription judgment is made by this report.**

## Counts

| Item | Count |
| --- | ---: |
| Exact asserted edits | 23 |
| Change records | 34 |
| Loci against C | 21 |
| Loci against H | 31 |
| Crop recipes | 41 |
| Inventory rows | 91 |

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
| `source/SP02_CW_10+12_scans/B10-06_10_scan077.jpg` | 1680 | 2150 | 646933 |

Bounds use source-pixel boxes with exclusive right and bottom edges. Image access was limited to `PIL.Image.open(source).size`; no pixel content was decoded, rendered, or viewed.

## Input identities

| Input | SHA256 |
| --- | --- |
| Page `pages/B10-06_10_scan077.tex` | `2a64b36c6e4643218d64a0eff7eb290884ba0305a9d03b835b6f641837946feb` |
| Record `documentation/page_records/B10-06_10_scan077.json` | `e402ce0fa7fa8690034cdfa0397aaa694783d6127d3132bc8b6dc1a2a8f7e77e` |
| Witness C `codex/B10-06/pages/B10-06_10_scan077.tex` | `0df8cf44b986f7628c50025dcd9e89f7e56a8f495b480ce8bf94d3a645a92207` |
| Root script `work/record077.py` | `bad31f7f7557a702ad9744fdb98541486effdd22fbcd4ff02c1c77c8e9a4ded2` |
| Canonical crop-recipe metadata | `dc98b266b3bc2f5a85143e122e21e237c0f1afab884d0dc1c0733a4328e3f411` |

The adjacent `scans075_077_mechanical_qa.json` records every edit's expected and actual count, helper hashes, report-snapshot hashes, inventory-metadata hash, and the finalized-count snapshot.

## Reproduction and remaining dependencies

From the workspace root, these existing commands repeat edit-count/inventory preparation and lexical checks without finalizing or writing a page:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_page.py SP02_CW_10+12/documentation/page_records/B10-06_10_scan077.json
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/validate_tex.py SP02_CW_10+12/pages/B10-06_10_scan077.tex --json
```

Crop metadata can be rechecked with `resolve_scan_source()`, `Image.open(source).size`, and `validate_crop_metadata(recipe, dimensions)`; no crop rendering is needed.

The original witness packet and scan directory are external dependencies and are intentionally omitted from deliverable archives. Scan payloads were not hashed during this header-only check. The root script's copy at `documentation/root_scripts/record077.py` was absent at this snapshot and should be captured by the normal checkpoint documentation refresh. Later page finalizations will change shared-report hashes; the recorded hashes identify the checked snapshot.

## Root-supplied audit reminder

In this fragment workflow C's \tag* places labels on the right unless the fragment explicitly places them on the left. Root reported correcting two left labels on scan077. This QA did not inspect label placement or alter prior pages.

This QA did not open context, view scan content, compile TeX, change readings, create audit/freeze events, package, or upload anything.

