# A report release: exact source delta

This is a source-only comparison. It records no ink decision and claims no root review.

Old captured report: `out/checks/scan026_root_preread/A_report.json` (`9002cdee8aa033f56d8111a6df8acb159671d569050432aefa354c7b0d61c66a`).

Final frozen report: `out/readers/026/A/report.json` (`1f4f9f23873d17e9bbd341c59f32b1739855a5e1e6fad2c28d3328283faeab56`).

The 63 old difference ids all remain. Final difference row 31 is the new `A026-L13`; old indices 0–30 map to final indices 0–30, and old indices 31–62 map to final indices 32–63. The full 64-entry exact mapping is in the manifest.

There are 670 changed or added codec nodes and 122 distinct final node values among those changes. Each distinct final value appears once in the review files, with all its exact old/new field paths and any old identical-value paths. Scalar values and container order/length metadata are both included.

Read the following review files completely; no field value or occurrence list is abbreviated:

- `out/checks/scan026_source_A_release_review_v01_01.jsonl` — 2 distinct values, 1781 bytes.

- `out/checks/scan026_source_A_release_review_v01_02.jsonl` — 1 distinct values, 49663 bytes.

- `out/checks/scan026_source_A_release_review_v01_03.jsonl` — 2 distinct values, 951 bytes.

- `out/checks/scan026_source_A_release_review_v01_04.jsonl` — 1 distinct values, 20409 bytes.

- `out/checks/scan026_source_A_release_review_v01_05.jsonl` — 6 distinct values, 10694 bytes.

- `out/checks/scan026_source_A_release_review_v01_06.jsonl` — 5 distinct values, 10427 bytes.

- `out/checks/scan026_source_A_release_review_v01_07.jsonl` — 7 distinct values, 11147 bytes.

- `out/checks/scan026_source_A_release_review_v01_08.jsonl` — 11 distinct values, 13015 bytes.

- `out/checks/scan026_source_A_release_review_v01_09.jsonl` — 12 distinct values, 13480 bytes.

- `out/checks/scan026_source_A_release_review_v01_10.jsonl` — 10 distinct values, 13037 bytes.

- `out/checks/scan026_source_A_release_review_v01_11.jsonl` — 13 distinct values, 12646 bytes.

- `out/checks/scan026_source_A_release_review_v01_12.jsonl` — 21 distinct values, 13217 bytes.

- `out/checks/scan026_source_A_release_review_v01_13.jsonl` — 13 distinct values, 13158 bytes.

- `out/checks/scan026_source_A_release_review_v01_14.jsonl` — 11 distinct values, 9703 bytes.

- `out/checks/scan026_source_A_release_review_v01_15.jsonl` — 1 distinct values, 10831 bytes.

- `out/checks/scan026_source_A_release_review_v01_16.jsonl` — 1 distinct values, 10852 bytes.

- `out/checks/scan026_source_A_release_review_v01_17.jsonl` — 5 distinct values, 6098 bytes.


The value pool and operations retain both sides. `scan026_source_A_release_build.py` supplies the finite forward and inverse maps. Replay recovered both original report byte strings exactly, including object key order, with the original hashes. This byte-level equality concerns these source files only.


A parent inventory attribution and a nested candidate attribution remain separate source fields; this procedure never assigns one field’s scope to another.
