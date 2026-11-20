# Scan124 bounded mechanical QA

Checked: 2026-11-20 00:58:21 UTC
Page: B10-09_10_scan124
Finalized record timestamp: 2026-11-20 00:56:58 UTC

**PASS — no structural issues found.**

## Scope

One bounded pass checked all actual supplied root JSON fields against the finalized record, required schema/accepted values, exact identity/page hash, inventory/collation/count projections, crop IDs/references/finite geometry/parameters/safe paths, root Python AST and page TeX lexical structure. No fixed field count was assumed.

Bounded metadata and syntax only; no images, image headers, witness prose, context, source edit replay, reading judgments, audits, freeze, compilation, archive access, upload or checkpoint preparation.

Progress and CHECK_EVENTS were read as raw bytes solely for before/after protection hashes. Their contents were not interpreted or changed. Only this Markdown file and its companion JSON were written.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 6126 |
| Asserted edit entries (not replayed) | 31 |
| Changes | 61 |
| Against C | 32 |
| Against H | 59 |
| Crop recipes | 82 |
| Inventory rows | 69 |
| All inventory rows transcribed | True |
| Actual root JSON fields compared | 15 |
| Final record fields | 21 |

Expected counts: 6,126 bytes, 61 changes, 69 inventory rows and 82 crop recipes.
Findings: none.
Root/final field differences: none.

Lexical result: True; 125 brace pairs, 28 math pairs and 13 environment pairs. No macro expansion or compilation was performed.

All 6 protected inputs were compared byte-for-byte before/after the check. Changed inputs: none. Exact SHA256 fingerprints, actual field sets and helper hashes are in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because no images or headers were opened. Source-C hash format was checked without reopening source bytes or replaying edits. No protected input was edited.
