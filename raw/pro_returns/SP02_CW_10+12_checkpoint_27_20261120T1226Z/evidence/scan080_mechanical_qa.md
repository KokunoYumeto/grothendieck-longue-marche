# Scan080 mechanical QA

Checked: 2026-11-19 20:21:13 UTC. Syntax checks: 2026-11-19 20:21:14 UTC.

**Result: all requested mechanical checks passed.**

| Item | Result |
| --- | ---: |
| Finalized page bytes | 4772 |
| Exact asserted edits | 25 |
| Change records | 41 |
| Loci against C / H | 25 / 41 |
| Crop recipes | 44 |
| Inventory rows, all transcribed=yes | 92 |
| Source dimensions from header | 1684 × 2155 |
| Source file bytes | 832773 |

The page byte length, change count, inventory count, and crop count agree with root's supplied values.

## Verification

Record identity and map correspondence, source-C and page hashes, metadata schema, change kinds and flags all agree. Every asserted edit has the correct sequential occurrence count; replay from C reproduces the finalized page bytes exactly.

All crop IDs and references resolve. Sources are safely confined to the known scan directory, transform metadata is valid, and every source-pixel box is within the header dimensions. Inventory normalization and overrides agree with resolved rows. Current inventory, collation, changes, counts, and doubts match their record projections.

The finalized root script passes Python AST parsing without execution or bytecode. The page passes lexical brace, math-delimiter, environment, and group-boundary checks without TeX compilation.

Source: `source/SP02_CW_10+12_scans/B10-06_10_scan080.jpg`. Image access was limited to `PIL.Image.open(source).size`; no pixel content was decoded, rendered, or viewed. No context was accessed and no reading decision was made.

## Input identities

| Input | SHA256 |
| --- | --- |
| `pages/B10-06_10_scan080.tex` | `3a6493caeca9938b913fea289e89d607064e9f812cb0f0fffeb7aa370f58a471` |
| `documentation/page_records/B10-06_10_scan080.json` | `5e171f60224a0d724ce9d84eaa11090be23370d791ccc0ef2f4a67e04e7e1ed1` |
| Witness C `codex/B10-06/pages/B10-06_10_scan080.tex` | `1b29c46e72a40f60e134f606670be90603d1cb1635725f9a69b5b842a3b37b0d` |
| `work/record080.py` | `8c6e70fd26ec7aed58d91f7c273325b7c226d24a7a6358279af6c830a3a99eb6` |
| Canonical crop recipes | `113037ca86c666003122bf8503a324dc70e72cc76cfc0aecd4742a6883a85825` |

The companion `scan080_mechanical_qa.json` preserves every edit's expected/actual count, helper identities, inventory and report hashes, and syntax evidence.

## Historical checkpoint06 material

There is exactly one finalized record for scan080: `documentation/page_records/B10-06_10_scan080.json`. Root identifies `documentation/in_progress_080_record.py` as intentional historical checkpoint06 documentation. It is not counted as another finalized record. Root owns supersession of the in-progress snapshot; this QA leaves those files unchanged.

## Reproduction

From the workspace root, existing non-finalizing commands are:

```bash
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/record_page.py SP02_CW_10+12/documentation/page_records/B10-06_10_scan080.json
PYTHONDONTWRITEBYTECODE=1 python SP02_CW_10+12/scripts/validate_tex.py SP02_CW_10+12/pages/B10-06_10_scan080.tex --json
```

Bounds can be repeated using `resolve_scan_source()`, `Image.open(source).size`, and `validate_crop_metadata(recipe, dimensions)`. Original witnesses and scans remain external dependencies. Scan payload bytes were not hashed; shared-report hashes identify this snapshot. The finalized `record080.py` awaits the normal documentation refresh.

Pages, records, and scripts were preserved. No files were removed, and no audit, freeze, packaging, or upload action occurred.

