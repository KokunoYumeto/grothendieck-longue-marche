# SP60_CW_71 — Package guide

The final diplomatic transcription is in `pages/`, one fragment per scan, and in `SP60_CW_71_transcription.tex`, the combined fragment. The supplied witness preamble defines the required macros. No TeX compilation is part of this package's validation.

The changes log records differences from C or H and the scan evidence used to decide them. The H collation contains only discrepancies on pages where H supplies source text. Its many source-block omissions must be distinguished from attempted readings; the error-sheet feedback explains that distinction. Remaining uncertainty, notation, abbreviations, inventory, hand observations, reading notes, and actual check events have their own named deliverables.

The final hand descriptions distinguish the main manuscript, marginal annotation layers, and unattributed sketches by observed appearance. They do not identify every writer or assert that each intervention belongs to a different person; the hand log states the limits of attribution.

## Supporting records

- `decisions.tsv` stores the primary reader's decisions, witness-change flags, primary categories, confidence, and crop evidence.
- `doubt_records.tsv` stores doubt and certainty statuses. `notation.tsv` and `hand.tsv` support their corresponding readable logs.
- `CHECK_EVENTS.tsv` records the kind of checking actually performed. Transcription alone does not constitute a proof check.
- `progress.log` records page completion, second readings, and the final transcription hashes. Consult the final freeze and unchanged-hash confirmation when checking integrity.
- `STRUCTURAL_REVIEW.md` is a generated metadata report, dated at its last validation. Its approximate uncertainty matches are review aids, not independent manuscript readings.
- `UNCERTAINTY_ACKNOWLEDGEMENTS.tsv` records the primary reader's manual mappings where approximate string matching was insufficient. Each is bound to a page-file SHA-256; later edits invalidate that acknowledgement until it is deliberately reviewed again.

## Scripts and reproducibility

`scripts/page*.py`, `scripts/audit*.py`, `scripts/record.py`, and `scripts/finalize_metadata.py` document the historical writing and final reconciliation workflow. **Do not rerun them wholesale against a finished package.** They can append duplicate rows, overwrite files, or regenerate the combined transcription. The append-only helper does not automatically supersede an earlier doubt status or synchronize an edited decision into an already written H collation. Historical script defaults are not authoritative over the finalized inventory or hand descriptions.

The crop scripts document operations on the original attached scans. Those scans, witnesses, and crop images are deliberately absent from this package.

The following tools can be used separately:

- `python3 scripts/generate_feedback.py .` regenerates only the error-sheet feedback from the current decision and doubt tables.
- `python3 scripts/validate_package.py .` performs structural checks without compilation. Use `--incomplete` only for a working checkpoint; `--report STRUCTURAL_REVIEW.md` updates the metadata report. Add `--zip /path/to/SP60_CW_71.zip` to check an already built archive, omitting `--report` so the report is not changed after packaging.
- `python3 scripts/package.py verify` compares all twelve frozen transcription hashes with the current bytes. `verify --log` also appends the successful unchanged-hash event. The `build --target /path/to/SP60_CW_71.zip` action verifies those hashes, excludes caches, and refuses to overwrite an existing archive. A second `freeze` is refused once a freeze is recorded.

Finish every content edit and regeneration before freezing the transcription. Recompute and compare the recorded hashes before packaging. A structural pass does not certify paleographic accuracy, mathematical validity, or the semantic completeness of the inventory.

## Checkpoint continuity

The final output folder was checked against the member list of `SP60_CW_71_checkpoint_01.zip`: all 45 noncache member paths are present, with no duplicate checkpoint members. Later readings and reconciliation can update their contents; this check verifies retention of the documented files, not byte identity with the earlier checkpoint. Earlier checkpoint archives are not nested inside the final ZIP.
