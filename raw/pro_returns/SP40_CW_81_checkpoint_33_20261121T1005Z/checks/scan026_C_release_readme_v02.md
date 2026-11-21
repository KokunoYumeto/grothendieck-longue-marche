# C release: exact source delta

Source-only comparison; no ink decision and no root review are claimed. All six captured/frozen input hashes matched, and all source files remained unchanged.

Read `scan026_C_release_manifest_v01.json`, `scan026_C_release_review_index_v02.json`, every numbered review chunk below, both complete text diffs, and `scan026_C_release_replay_v01.json`. The index defines every finite alias and Cartesian product used by the compact review.

The complete report delta has 4510 operations: 2791 additions, 1353 replacements, and 366 deletions. The pool contains 776 exact nodes; 165 novel final nodes are printed in full and 611 exact captured-node matches are identified by literal numeric JSON pointers. All full candidates and role/hand/attachment fields remain reconstructible with their exact paths and container order.

All 76 captured difference ids remain. New D43 and D44 occupy final indices 44 and 45. Old indices 0–43 map to the same indices; old indices 44–75 map to final indices 46–77. The manifest prints the complete 78-entry id-to-index mapping.

The written full pool/operations and the written compact review were independently reloaded and expanded. Both yielded the complete frozen report bytes forward and the complete captured report bytes backward. The unified TeX and Markdown diffs were also parsed and replayed in both directions with exact byte equality. No raw source inconsistency was edited.

- `out/checks/scan026_C_release_review_v02_01.jsonl` — 346 complete rows, 10980 bytes.
- `out/checks/scan026_C_release_review_v02_02.jsonl` — 178 complete rows, 10998 bytes.
- `out/checks/scan026_C_release_review_v02_03.jsonl` — 97 complete rows, 10988 bytes.
- `out/checks/scan026_C_release_review_v02_04.jsonl` — 231 complete rows, 10984 bytes.
- `out/checks/scan026_C_release_review_v02_05.jsonl` — 261 complete rows, 10999 bytes.
- `out/checks/scan026_C_release_review_v02_06.jsonl` — 269 complete rows, 10994 bytes.
- `out/checks/scan026_C_release_review_v02_07.jsonl` — 327 complete rows, 10976 bytes.
- `out/checks/scan026_C_release_review_v02_08.jsonl` — 393 complete rows, 10984 bytes.
- `out/checks/scan026_C_release_review_v02_09.jsonl` — 278 complete rows, 10966 bytes.
- `out/checks/scan026_C_release_review_v02_10.jsonl` — 191 complete rows, 6032 bytes.

Complete text diffs:

- `out/checks/scan026_C_release_reading.tex.diff` — 39 lines, 2281 bytes.
- `out/checks/scan026_C_release_reading.md.diff` — 155 lines, 13394 bytes.
