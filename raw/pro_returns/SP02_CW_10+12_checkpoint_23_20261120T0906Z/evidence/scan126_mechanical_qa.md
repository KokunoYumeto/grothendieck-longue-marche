# Scan126 bounded mechanical QA

Checked: 2026-11-20 01:28:55 UTC
Page: B10-09_10_scan126
Finalized record timestamp: 2026-11-20 01:28:11 UTC

**PASS — no structural issues found.**

## Scope

One bounded pass checked all actual root JSON fields against the finalized record, required schema/accepted values (including kind labels), identity/page hash, exact inventory/collation/count projections, crop IDs/references/finite geometry/parameters/safe paths, root Python AST and page TeX lexical structure. No fixed field count was assumed.

Bounded metadata and syntax only; no images, image headers, witness prose, context, source edit replay, reading judgments, audits, freeze, compilation, archive access or upload. Separately authorized checkpoint preparation is documented separately.

Progress and CHECK_EVENTS were read as raw bytes solely for before/after protection hashes. Their contents were not interpreted or changed. Only this Markdown file and its companion JSON were written by the page check.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 5282 |
| Asserted edit entries (not replayed) | 24 |
| Changes | 79 |
| Against C | 47 |
| Against H | 66 |
| Crop recipes | 81 |
| Inventory rows | 88 |
| All inventory rows transcribed | True |
| Remaining doubt entries | 9 |
| Actual root JSON fields compared | 15 |
| Final record fields | 21 |

Expected counts: 5,282 bytes, 79 changes, 88 inventory rows, 81 crop recipes and 9 remaining doubts.
Findings: none.
Root/final field differences: none.

Lexical result: True; 156 brace pairs, 55 math pairs and 6 environment pairs. No macro expansion or compilation was performed.

All 6 protected inputs were compared byte-for-byte before/after the check. Changed inputs: none. Exact SHA256 fingerprints, actual field sets and helper hashes are in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because no images or headers were opened. Source-C hash format was checked without reopening source bytes or replaying edits. Doubt entries were counted, not interpreted. No protected input was edited.
