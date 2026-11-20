# Scan 136 mechanical QA

Checked: 2026-11-20 04:28:28 UTC.

**Result: PASS** — metadata, exact opaque record/report comparisons, and lexical syntax only.

| Check | Result |
|---|---|
| Page key | B10-10_10_scan136 |
| Page bytes | 4955 |
| Actual root fields | 14; differences 0 |
| Edits / asserted replacements | 19 / 19 |
| Changes / against C / against H | 35 / 19 / 33 |
| Inventory | 42; all transcribed=yes: True |
| Crops | 98 = 83 + 8 + 7 |
| Remaining doubts | 4 |
| Prepared equals final | True |
| Root builder equals JSON | True |
| Python AST / TeX lexical | True / True |
| Protected inputs | 20 current inputs plus 164 prior finalized files; changes 0 |

Page SHA-256: `a0a4b4eb5bb15c662436d4bf7a8e878f7a4e83d6b4015406a4615240783f1fa2`.

All crop IDs, references, safe source paths, numeric geometry and transformation parameters were checked. Pixel extent bounds were not checked; no image or image header was opened. Source C hash was checked for format only. No source edits were replayed. Root script save was intercepted in memory. The seven-node TikZ representation was not assessed visually or mathematically.

Issues: None.

## Isolated QA adapter retry

At 2026-11-20 04:29:01 UTC, the bounded reconstruction adapter was adjusted to resolve the root script’s workspace-relative recipe paths against the fixed workspace. Only the same three captured JSON streams were allowed. Root script reconstruction now matches root JSON exactly; no protected input changed. The initial adapter failure remains recorded in the JSON attempt history. No root script, recipe, page, record, report, or log was changed.
