# Scan076 mechanical QA

Checked: 2026-11-19 20:03:09 UTC. Syntax checks: 2026-11-19 20:02:26 UTC.

**Result: all requested mechanical checks passed. No transcription judgment is made by this report.**

## Counts

| Item | Count |
| --- | ---: |
| Exact asserted edits | 26 |
| Change records | 56 |
| Loci against C | 26 |
| Loci against H | 56 |
| Crop recipes | 50 |
| Inventory rows | 47 |

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
| `source/SP02_CW_10+12_scans/B10-05_10_scan076.jpg` | 1681 | 2151 | 819176 |

Bounds use source-pixel boxes with exclusive right and bottom edges. Image access was limited to `PIL.Image.open(source).size`; no pixel content was decoded, rendered, or viewed.

## Input identities

| Input | SHA256 |
| --- | --- |
| Page `pages/B10-05_10_scan076.tex` | `73639bee722ad2d7f55c475144c05f4b29325259208d7cc67f7d6f31fb551093` |
| Record `documentation/page_records/B10-05_10_scan076.json` | `f2c70407caa2644e4db9dbe2595d255c320c36e6476537dfbd3c4898de25f3db` |
| Witness C `codex/B10-05/pages/B10-05_10_scan076.tex` | `5cca69971167aee95c102825f642df50ffa38b412b43a740dd64cd2636bb2a9e` |
| Root script `work/record076.py` | `6c843cd40011715e6c704481d6be688376ad3d9572666ad228920c226d8a9e52` |
| Canonical crop-recipe metadata | `b1b3fcc8f23abf87af3fe9fca37667e4fa9703d52f93ec2faeed559e71bd0d16` |

The adjacent `scans075_077_mechanical_qa.json` records every edit's expected and actual count, helper hashes, report-snapshot hashes, inventory-metadata hash, and the finalized-count snapshot.

## Reproduction and remaining dependencies

From the workspace root, these existing commands repeat edit-count/inventory preparation and lexical checks without finalizing or writing a page:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_page.py SP02_CW_10+12/documentation/page_records/B10-05_10_scan076.json
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/validate_tex.py SP02_CW_10+12/pages/B10-05_10_scan076.tex --json
```

Crop metadata can be rechecked with `resolve_scan_source()`, `Image.open(source).size`, and `validate_crop_metadata(recipe, dimensions)`; no crop rendering is needed.

The original witness packet and scan directory are external dependencies and are intentionally omitted from deliverable archives. Scan payloads were not hashed during this header-only check. The root script's copy at `documentation/root_scripts/record076.py` was absent at this snapshot and should be captured by the normal checkpoint documentation refresh. Later page finalizations will change shared-report hashes; the recorded hashes identify the checked snapshot.

This QA did not open context, view scan content, compile TeX, change readings, create audit/freeze events, package, or upload anything.

