# Scan025 independent source coverage inventory

Source-only inventory; no source file was changed. All identities use their original file plus JSON pointer. Own-reader readings, witness C/H fields and any later selected fields retain their separate roles.

| Reader | Differences | Doubts | Inventory | Groups | Text spans | Literal drawing commands |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| A | 21 | 14 | 29 | 21 | 19 | 143 |
| B | 28 | 15 | 32 | 18 | 6 | 149 |
| C | 28 | 18 | 31 | 21 | 4 | 151 |

The source packet has 8 actual C doubt rows, 8 separately scoped notation/slip rows, and 13 inventory rows.

Recorded 369 original row references, 60 complete group references, 29 text-span references, 443 literal drawing-command references, and 816 original qualification/hand/scope metadata fields.

Source checks: 477; failed checks: 16.

## Concrete findings

- {"kind": "group_marker_map_identity_or_order_mismatch", "reader": "A", "begins": ["A025-G00", "A025-S01", "A025-G01", "A025-G02", "A025-G03", "A025-G04", "A025-G05", "A025-S02", "A025-M01", "A025-G06", "A025-S03", "A025-G07", "A025-G08", "A025-S04", "A025-G09", "A025-M02", "A025-S05", "A025-S06", "A025-S07", "A025-S08", "A025-M03"], "ends": ["A025-G00", "A025-S01", "A025-G01", "A025-G02", "A025-G03", "A025-G04", "A025-G05", "A025-M01", "A025-S02", "A025-G06", "A025-S03", "A025-G07", "A025-G08", "A025-S04", "A025-M02", "A025-G09", "A025-S05", "A025-S06", "A025-S07", "A025-S08", "A025-M03"], "expected": ["A025-G00", "A025-S01", "A025-G01", "A025-G02", "A025-G03", "A025-G04", "A025-G05", "A025-S02", "A025-G06", "A025-S03", "A025-G07", "A025-G08", "A025-S04", "A025-G09", "A025-S05", "A025-S06", "A025-S07", "A025-S08", "A025-M03", "A025-M01", "A025-M02"]}
- {"kind": "group_marker_map_identity_or_order_mismatch", "reader": "B", "begins": ["B025-S02"], "ends": ["B025-S01", "B025-G02", "B025-G03", "B025-G04", "B025-S02", "B025-S03", "B025-G05", "B025-G06", "B025-S04", "B025-G07", "B025-S05", "B025-S06", "B025-S07", "B025-G09", "B025-G08", "B025-S08", "B025-M01", "B025-M02"], "expected": ["B025-S01", "B025-G02", "B025-G03", "B025-G04", "B025-S02", "B025-S03", "B025-G05", "B025-G06", "B025-S04", "B025-G07", "B025-S05", "B025-S06", "B025-S07", "B025-G08", "B025-S08", "B025-M01", "B025-M02", "B025-G09"]}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/4", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/5", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/11", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/13", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/17", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/18", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/19", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/20", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/21", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/22", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/23", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/25", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/26", "literal_field": "reader_source_quote"}
- {"kind": "stored_reader_span_mismatch", "path": "out/readers/025/B/report.json", "json_pointer": "/differences/27", "literal_field": "reader_source_quote"}

## Required preservation points

- Keep original C rows R01–R08 at their actual scope. A local_decisions and C local_parts remain attached to their original row identities.
- Keep A inventory scope_note, B inventory local_hand_scopes, and C inventory compound hand values. Complete group metadata and candidate-specific hand scopes remain at their original source pointers.
- Keep each complete graphical group, every node/word command, every drawing command, and adjoining text at the original source offset. Group and text-span boundaries are recorded literally.
- Preserve source-silent own-reader material from complete TeX. C’s live et candidate remains in reader C’s source role; B’s que-plus-point group remains in reader B’s source role.
- H marker catalog contains no uncertainty macro; supplied letters and the two note objects retain their local source spans. All later local marked_in_H choices belong to root review.
- S_scope records seven source rows and an empty direct_page_25_reading_rows array; its exact scope statement is bound as original source metadata.

Stage1 source-pool/projection replay remains pending source025 handoff.
