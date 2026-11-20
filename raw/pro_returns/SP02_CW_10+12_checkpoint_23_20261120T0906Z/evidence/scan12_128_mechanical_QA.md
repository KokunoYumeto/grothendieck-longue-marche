# B12-02_12_scan128 mechanical QA

Checked: 2026-11-20 08:05:48 UTC.

**PASS**.

| Check | Result |
|---|---|
| Page | B12-02_12_scan128; 2543 bytes |
| Actual root fields | 15; differences 0 |
| Edits / asserted replacements | 0 / 0 |
| Changes / against C / against H | 7 / 0 / 0 |
| H collation rows | 0; exact flag projection checked |
| Inventory | 23; all transcribed=yes |
| Crop recipes | 49 |
| Remaining doubts | 0 |
| Root builder / prepared-final equality | True / True |
| AST / lexical | True / True |
| Opaque edit replay / exact old counts | True / True |
| Full crop / preview files present | 49 / 49 |
| Prior finalized files | 200 saved hashes match and remain unchanged |
| Total protected files | 221 |

Page SHA-256: 0de77718f602177803a4d3e02f3c555ce6dcb81e0460ff10aa910f21a90b18d6.

All nonempty exact replacement outputs occur in the final fragment: True. This presence check is supplemented by explicitly authorized opaque source hash and sequential exact-count replay; replay details are recorded in JSON. For a zero-edit page, this confirms retained C text after standard newline normalization. Crop numeric geometry, transformation parameters, references and safe paths were checked; pixel extent bounds were not checked because no image or header was opened. Only the mapped C bytes were processed automatically for hash and edit comparison; no source prose was displayed or interpreted, and no witness notes, H source, image/header, or context was opened. No reading decisions, manuscript compilation, audit, freeze, staging or packaging occurred.

Issues: None.
