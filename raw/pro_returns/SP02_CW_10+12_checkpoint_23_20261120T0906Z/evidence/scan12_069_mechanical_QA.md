# Cote 12, scan 069 mechanical QA

Checked: 2026-11-20 05:22:19 UTC.

**PASS**.

| Check | Result |
|---|---|
| Page | B12-01_12_scan069; 1265 bytes |
| Actual root fields | 15; differences 0 |
| Edits / asserted replacements | 9 / 9 |
| Changes / against C / against H | 22 / 13 / 19 |
| Actual H collation rows | 19; exact projection passes: True |
| Inventory | 13; all transcribed=yes |
| Crop recipes | 56 = 42 + 14 |
| Remaining doubts | 7 |
| Root builder / prepared-final equality | True / True |
| AST / lexical | True / True |
| Prior finalized files | 174 match checkpoint18 and remain unchanged |
| Total protected files | 194 |

Page SHA-256: `7d7998d681d0a2757b2c1b4d72c32e5c89692b88cdca7d6e43c7b918fec76903`.

All nonempty exact replacement outputs occur in the final fragment: True. This is an opaque string-presence check, not source replay. Crop numeric geometry, transformation parameters, references and safe paths were checked; pixel extent bounds were not checked because no image or header was opened. No witness prose or context was accessed, and no reading decisions, compilation, audit, freeze, staging or packaging occurred.

Issues: None.
