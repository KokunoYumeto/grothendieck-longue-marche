# SP109_CW_134-2 — completed diplomatic second pass

## Main files

- `SP109_CW_134-2_transcription.tex`: the seventeen accepted pages, scans 153–169, in order as a single LaTeX fragment without a preamble.
- `pages/`: the same pages separately, with the original witness-C filenames.
- `SP109_CW_134-2_changes.md`: per-page witness comparisons, counts, consequential mathematical corrections, and all blind-reading adjudications.
- `SP109_CW_134-2_collation.tsv`: the places differing from witness H, using the requested column names and kinds.
- `SP109_CW_134-2_doubts.md`: current notation, remaining doubts, abbreviations and legibility assessment.
- `SP109_CW_134-2_inventory.csv`: every inventoried page element and its transcription status.
- `SP109_CW_134-2_notes.md`: English notes on each page’s claims, the author’s qualifications, actual local checks, and sheet information.
- `SP109_CW_134-2_sheet_feedback.md` and `SP109_CW_134-2_hand_log.md`: error-kind counts and locally evidenced handwriting habits.
- `CHECK_EVENTS.tsv`: mathematical and notation-check events, distinguishing calculations and local rechecks from background claims.

## Completion and evidence

All 17 pages have a completed first-pass acceptance and blind second-reading audit in `progress.log`. The first pass used all three readers; the independent reader for each page differs from its first reader. `assignments.tsv` records the assignments. Blank assignment timestamps were not reconstructed.

There are 420 recorded first-pass decision crops and 451 independent-reading boxes. Token comparison found 277 differing boxes. All were adjudicated on saved crops; 74 boxes changed the page, including added uncertainty. Two separately marked agreement rechecks are also documented. Those counts describe the second-reading workflow, not additional witness discrepancies.

The final witness log has 311 places: 85 differ from C and 271 from H, with 45 places differing from both. The confidence totals are 235 high, 46 medium and 30 low. These are counts of logged places. New uncertainty around an unchanged preferred reading is not an extra witness-change row; resolution of an original witness doubt is documented as a reading decision.

`crops/` contains the saved enlarged crops. `second/` contains every neutral box list, the first reading saved before comparison, the independently written reading, token differences, supplemental crop coordinates and reading-table hashes. `records/` contains the detailed page records; `scripts/` contains the programs used for crop production, comparison, adjudication bookkeeping, assembly and verification. No OCR, external research or TeX compilation was used.

## Current state and working history

The accepted page files and their completed `second_review` records control the final reading. Some first-pass `notation_updates`, earlier reading snippets, and files in `working_history/` intentionally retain superseded decisions. The current notation and final notes have been reconciled separately; historical records are not additional final transcriptions.

The one-time adjudication scripts record decisions already applied. Do not rerun them as assembly commands: they can repeat append operations, and `audit.finish` rejects an already-audited page. `manage.py assemble` regenerates aggregate deliverables from current records and the curated supporting files. `final_audit.py` and `validate_records.py` perform static bookkeeping checks, not manuscript recognition or mathematical proof. The provenance report gives the scope and results of its geometry, pixel-origin and metadata checks; lexical candidates in it are not automatic errors.

`frozen_hashes.json` and `progress.log` record the SHA-256 values of all 17 page files and the combined transcription, with the final unchanged-hash check. `MANIFEST.sha256` covers every packaged file except the manifest itself. `checkpoints.json` identifies the two previously saved checkpoint archives; those archives are not nested here.

Unchanged scans, witnesses, attached prompts and source preambles are excluded. The supplied preamble is required to use the LaTeX fragment, as requested in the task.
