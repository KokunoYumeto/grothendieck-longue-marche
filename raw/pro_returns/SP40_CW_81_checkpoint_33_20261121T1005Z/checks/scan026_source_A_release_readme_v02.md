# A release review v02

Use this exact factored review instead of the verbose v01 review chunks. The v01 pool, operations and byte replay remain the reversible source record. No original file was changed, and no root review is claimed.

All 63 captured difference rows remain. New final row 31 is A026-L13. The full exact id permutation is in `scan026_source_A_release_manifest_v01.json`.

For each exact_field_products entry, the logical paths are every record + every suffix. The finite equality check confirms each listed product exactly equals its assigned original operation set. No absent cross-product combination is supplied.

For logical /differences/@ID paths, replace @ID by that source id’s old_index or new_index from the manifest. The old pointer is null when the old node is absent; the final pointer is null when the final node is absent. Other logical paths are ordinary JSON pointers. All use RFC6901 escaping. Numeric indices are zero-based.

old_node is the exact prior node id in pool_v01.json; null means this field did not exist. All final values are printed once. Unchanged field values are omitted from the delta only and remain in the frozen raw sources.

A node of kind object retains its exact ordered key array; array retains exact length; id-list retains the full ordered ids. A kind value node is the exact JSON scalar.

The review prints 122 distinct final values once and maps all 670 final changed/added nodes. Both complete report byte strings were recovered exactly, including JSON key order.

- `out/checks/scan026_source_A_release_review_v02_01.jsonl`: 11 values, 12308 bytes.
- `out/checks/scan026_source_A_release_review_v02_02.jsonl`: 41 values, 12488 bytes.
- `out/checks/scan026_source_A_release_review_v02_03.jsonl`: 31 values, 12219 bytes.
- `out/checks/scan026_source_A_release_review_v02_04.jsonl`: 34 values, 11665 bytes.
- `out/checks/scan026_source_A_release_review_v02_05.jsonl`: 5 values, 2125 bytes.
