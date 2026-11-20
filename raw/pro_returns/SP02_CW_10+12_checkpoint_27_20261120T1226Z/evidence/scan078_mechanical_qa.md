# Scan078 mechanical QA

Checked: 2026-11-19 20:06:54 UTC. Syntax checks: 2026-11-19 20:06:50 UTC.

**Result: all requested mechanical checks passed.** No transcription decisions were made.

## Counts and image-header metadata

| Item | Result |
| --- | ---: |
| Finalized page bytes | 5465 |
| Exact asserted edits | 28 |
| Change records | 55 |
| Loci against C | 28 |
| Loci against H | 52 |
| Crop recipes | 54 |
| Inventory rows, all transcribed=yes | 102 |
| Source dimensions | 1680 × 2151 |
| Source file bytes | 686057 |

The byte length, change count, inventory count, and dimensions match the values supplied by root. Source: `source/SP02_CW_10+12_scans/B10-06_10_scan078.jpg`.

## Verified checks

- Record identity and stored map row match the page map.
- Source-C and finalized-page byte hashes agree with the record.
- All 28 edits have their asserted occurrence counts; replay from C reproduces the finalized page bytes exactly.
- Schema, change kinds, confidence values, and C/H flags are valid.
- All 54 crop IDs and references resolve; source paths are safe; recipe parameters and source-pixel bounds are valid.
- Inventory normalization and overrides agree with the resolved rows. Inventory, collation, changes, counts, and doubts match their report projections.
- The root script passes Python AST parsing without execution or bytecode generation.
- The page passes lexical brace, math-delimiter, environment, and group-boundary checks.
- Pages, records, and scripts were preserved. No files were removed.

Image access was limited to `PIL.Image.open(source).size`. No pixels were decoded, rendered, or viewed. No context access, OCR, compilation, or reading adjudication occurred.

## Input identities

| Input | SHA256 |
| --- | --- |
| `pages/B10-06_10_scan078.tex` | `16a145711863d28f05930ce1771e22ad95ada4bd7c9cb4f84ffdb6236a49aad2` |
| `documentation/page_records/B10-06_10_scan078.json` | `201d27c5de4e907987d14da14a8c27d5885318ae458b39bb9c30b5c75742561e` |
| Witness C `codex/B10-06/pages/B10-06_10_scan078.tex` | `6d48aba11f3e8a8bfe6eb99094c4f4038eb3aee4a4253ab44c2a2a1f5f70df02` |
| `work/record078.py` | `f6a74b2b1cef5104b10cc2cf6d98e68b89d7528b5b04f2ba4bdd6e139268124b` |
| Canonical crop-recipe metadata | `b5fb5eb3daa330e8b3999d67ccde5b5167d9ddba1c1903ecf1002d3cd309f22f` |

The companion `scan078_mechanical_qa.json` records each edit's expected/actual count, inventory and report hashes, helper hashes, and syntax evidence.

## Reproduction

From the workspace root, existing non-finalizing commands are:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_page.py SP02_CW_10+12/documentation/page_records/B10-06_10_scan078.json
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/validate_tex.py SP02_CW_10+12/pages/B10-06_10_scan078.tex --json
```

Crop bounds can be repeated with `resolve_scan_source()`, header dimensions from `Image.open(source).size`, and `validate_crop_metadata(recipe, dimensions)`; no rendering is required.

The original witness packet and scans remain external dependencies. Scan payload bytes were not hashed under this header-only check. Shared-report hashes identify this snapshot and may change after later pages finalize. At this snapshot `documentation/root_scripts/record078.py` was absent; the normal checkpoint documentation refresh should preserve the existing root script there.

No packaging, upload, audit, or freeze action was performed.

