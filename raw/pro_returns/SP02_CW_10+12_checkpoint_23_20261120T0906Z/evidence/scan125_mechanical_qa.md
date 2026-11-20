# Scan125 bounded mechanical QA

Checked: 2026-11-20 01:12:36 UTC
Page: B10-09_10_scan125
Finalized record timestamp: 2026-11-20 01:11:53 UTC

**PASS — no structural issues found.**

## Scope

One bounded pass checked all actual supplied root JSON fields against the finalized record, required schema/accepted values, identity/page hash, inventory/collation/count projections, crop IDs/references/finite geometry/parameters/safe paths, root Python AST and page TeX lexical structure. No fixed field count was assumed.

Bounded metadata and syntax only; no images, image headers, witness prose, context, source edit replay, reading judgments, audits, freeze, compilation, archive access or upload. Separately authorized checkpoint preparation is documented separately.

Progress and CHECK_EVENTS were read as raw bytes solely for before/after protection hashes. Their contents were not interpreted or changed. Only this Markdown file and its companion JSON were written by the page check.

## Results

| Item | Result |
| --- | ---: |
| Page bytes | 4080 |
| Asserted edit entries (not replayed) | 22 |
| Changes | 43 |
| Against C | 23 |
| Against H | 42 |
| Crop recipes | 65 |
| Inventory rows | 41 |
| All inventory rows transcribed | True |
| Actual root JSON fields compared | 15 |
| Final record fields | 21 |

Expected counts: 4,080 bytes, 43 changes, 41 inventory rows, 65 crop recipes and 22 asserted edits.
Findings: none.
Root/final field differences: none.

Lexical result: True; 95 brace pairs, 22 math pairs and 6 environment pairs. No macro expansion or compilation was performed.

All 6 protected inputs were compared byte-for-byte before/after the check. Changed inputs: none. Exact SHA256 fingerprints, actual field sets and helper hashes are in the companion JSON.

## Limits

Crop pixel-extent bounds were not checked because no images or headers were opened. Source-C hash format was checked without reopening source bytes or replaying edits. No protected input was edited.
