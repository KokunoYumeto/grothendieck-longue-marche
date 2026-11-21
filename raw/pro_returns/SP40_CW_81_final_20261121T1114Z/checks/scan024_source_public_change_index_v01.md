# Scan 024 — compact source-binding and public-change index

This index adds no source or record change. The frozen v02 projection remains the public binding authority.

## Remaining own-reader layer

`scan024_source_reader_binding_plan_v01.json` has SHA-256 `ba0680b67bb24ea4d957a75d051f211cb44512e12a6e7c61eab631c5deec1b2d`.

Its exact selectors cover 216 current reader fields and all 180 referenced reader pool values: 24 complete frames, 151 local appendices and five editorial/source-scope chunks. The 54 group-description recipes identify each own candidate/state field, ordered original JSON pointer, source-comment line span, contained group and inventory clause. Original file hashes are stored once under `frozen_source_files`; every selector names its file ID, exact character/UTF-8 byte span, span hash and JSON pointer when applicable.

- `group_description_recipes`: the existing frame substitutions' editorial JSON and source-comment provenance.
- `appendix_recipes`: all 151 local appendices, with exact original difference/doubt rows, ordered emitted fields, and explicit duplicate-object correspondence.
- `restored_inventory_clauses` and `twelve_inventory_focus`: the twelve restored original component identities and hand fields, with their frame and pool bindings.
- `A_D29_focus`: A's exact candidate-specific hand, role-confidence, alternatives and Q-D29 separate-scope pointers.
- `reader_field_bindings`: every current reader field's v02 pool IDs and exact own-role basis, including bounded absence and source-only S statements.

The supplied read-only interpreter is `scan024_source_reader_binding_replay.py`, SHA-256 `7006138fc90e05cb89de42d91218a0b69ba09faaf0ee622bf6516da899c7ad10`. Root reported successfully replaying the complete mapping against the frozen originals and current v02 fields. The source clerk did not execute that replay or a test pass.

## Closure 1: exact public changed-value locations

The complete immutable change list is `scan024_source_bounded_closure_v01.json#/record_changes`, also available one entry per line in `scan024_source_bounded_changes_v01.jsonl`.

Each entry contains `path`, `operation`, `semantic_role`, `old_present`, `new_present`, and exact `old_exact_value` / `new_exact_value` references. Each value reference includes its immutable record path/hash, JSON pointer, character/UTF-8 byte bounds and body hash. Small scalars additionally appear as `old_value` / `new_value`.

For the printed public reading queue, use changed paths in these fields:

- `/decisions/N/C`, `/H`, `/final`, `/readers/A`, `/readers/B`, `/readers/C`, `/evidence`, `/qualification`, `/confidence`, `/kind`, `/marked_in_H`, `/C_doubt_status`, `/S_id`, `/S_status`, `/diff_C`, `/diff_H`, and `/mathematical_consequence`.
- `/doubts/N/location`, `/reading`, `/alternatives`, `/confidence`, and `/reason`.
- `/inventory/N/sheet_kind`, `/hand`, `/element`, `/kind`, `/position`, `/first_words_or_objects`, and `/transcribed`.
- `/notes` and `/brief_version`.

The reader-role changes are indexed by `semantic_role`: 57 A fields, three B fields and 43 C fields. Their actual new source material is resolved through the binding plan above, so the complete containing frames need not be reread for each field. C64 is the sole changed witness-C field. The only changed selected finals are L38 and L39. All H and evidence fields remained unchanged.

Current mirrors under `selected_graphical_groups` and `source_locus_coverage`, exact authority additions and necessary map-hash replacements remain fully present in the closure. They do not add another independent public text to this reading queue. Canonical C-status metadata has its own exact closure paths and was separately reviewed by root.

Closure 2's alternatives-only additions retain all earlier v02 pool IDs. Its 49 new pool values and 58 changed array bindings are isolated in `scan024_source_public_projection_delta_v02.json`; its exact old/new field references are in `scan024_source_bounded_closure_v02.json`.
