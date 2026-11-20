# Scan115 bounded mechanical QA

Checked: 2026-11-19 22:29:09 UTC  
Page: `B10-08_10_scan115`  
Result: **Structural checks PASS; supplied root-field-count expectation differs.**

## Finding

The request expected 15 root JSON fields; the supplied root JSON has **16**, including `inventory_remove_elements`. All 16 fields match the finalized record and pass the metadata schema. No page or record change was made. The companion JSON retains this expectation discrepancy in its issues list, so its overall `all_mechanical_checks_pass` is false while `structural_checks_pass` is true.

## Counts

| Item | Result |
| --- | ---: |
| Page bytes | 2129 |
| Asserted edit entries (not replayed) | 15 |
| Changes | 25 |
| Against C | 16 |
| Against H | 24 |
| Crop recipes | 40 |
| Inventory rows | 25, all transcribed |
| Root JSON fields compared | 16 |

Schema/accepted values, identity, root/final-record correspondence, page hash, inventory/report projections, crop IDs/references/geometry/parameters/safe paths, Python AST and TeX lexical checks passed. Lexical counts: 38 brace pairs, 10 math pairs and 2 environment pairs; no issues.

All six protected inputs (page, record, root script, root JSON, progress log and CHECK_EVENTS) were unchanged byte-for-byte before/after the check. The two log files were accessed only as raw bytes for protection hashes during this page QA.

## Scope and limits

No witness prose, scan/image files, image headers or context were opened. No source edit replay, reading decisions, audit/freeze operation or compilation occurred. Crop pixel-extent bounds were not checked; source-C hash format was checked without source access. Only this page QA evidence was written by the page check. The separately authorized checkpoint preparation is recorded in distinct checkpoint09 preparation evidence.
