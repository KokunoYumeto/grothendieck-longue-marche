# Final validation scope

The validation scripts check deterministic assembly and metadata consistency without making new manuscript readings or executing TeX.

## Generated tables and combined transcription

`scripts/validate_deliverables.py` now requires the combined transcription and compares it with the builder's assembly of every `pages/147_scan*.tex` file in filename order: the cote header, blank-line separators, each page with trailing whitespace removed, and the final newline.

In both ordinary and `--complete` mode, it compares these generated tables with a single snapshot of the reviewed JSON records:

- `decisions.tsv`: every schema field, header, row count and row order, including the builder's numeric decision-ID sort and `ink` fallback for `what the ink shows`.
- `SP78_C13_147_inventory.csv`: every schema field, header, row count and row order, preserving the CSV writer's treatment of embedded whitespace and empty values.
- `SP78_C13_147_collation.tsv`: every schema field, header, row count and row order for precisely the changes marked `against_H`, including the evidence/crop/box string and the `marked_in_H` value.

The TSV comparisons use the builder's existing `clean` and `evidence` helpers. No builder schema or substantive reading is changed. Diagnostics identify affected rows and fields, with a bounded number of examples.

The existing page, crop, box, inventory and decision checks remain. `--complete` also requires the full scan and page-file scope, completed audits and second-reading files, the input MARKS ID sequence, and the other listed deliverables. Ordinary validation reports unfinished audits separately under `pending_audits`; they do not cause ordinary mode to fail.

## Freeze precondition

Before creating a hash manifest or appending freeze records, `scripts/freeze_transcription.py freeze` now requires page-file coverage/order to match `run_state.json`, requires the combined transcription, and verifies that it matches the same current-page assembly used by the builder. Existing root-review/audit approval and manifest-overwrite checks remain. The verification mode is unchanged.

After the remaining audits and the final builder run, run `python -B scripts/validate_deliverables.py --complete` before freezing. Table consistency is checked by the validator; the freeze helper independently guards the page/combined assembly.

## Validation of this change

Both edited scripts passed Python syntax parsing. An ordinary validator run returned exit status 0 with no consistency issues; audits 071–079 were still pending in that snapshot. No complete validation, freeze/verify invocation, builder run, TeX execution, test suite, or change to manuscript pages, reviewed records, frozen readings, adjudications or check events was performed for this script repair.

These gates establish structural and deterministic consistency. They do not establish the correctness of the manuscript readings, the semantic consistency of every free-form note, or mathematical proof validity.

## Final execution

At 2026-11-21 00:41:11 UTC, the complete structural validator passed with24 approved pages and no pending audits or issues. The separate evidence-integrity check verified all372 box readings against their preserved hashes,296 differing-box decisions and57 changed boxes. The51 indexed marks and539 inventory elements are present. These results remain structural/documentary checks; they do not enlarge the recorded mathematical check events.
