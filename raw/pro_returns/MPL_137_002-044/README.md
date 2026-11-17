# MPL_137_002-044 — final package

## Deliverables

- `MPL_137_002-044_transcription.tex`: the complete diplomatic LaTeX fragment, with 42 scans in order, 002–044 excluding the supplier's blank 006.
- `pages/`: one frozen TeX file per retained scan.
- `MPL_137_002-044_doubts.md`: the pre-context notation decisions, complete index of 471 uncertainty markers and 36 unreadable-word-count markers, abbreviation glossary, and legibility assessment.
- `MPL_137_002-044_inventory.csv`: 833 transcribed elements, all marked `yes`.
- `MPL_137_002-044_notes.md`: 107 research items, the four planning-question answers, the two required standing sections, contextual comparisons, and APA references; approximately 15,000 words including the supporting sections.
- `progress.log`: the page completions, second visual audits, notation review, freeze, context opening, hourly checkpoints, and final verification.
- `records/` and `scripts/`: the audit trail, independent mathematical checks, context-search ledger, and reproducible structural/package checks.

The source scans, supplied context, and attachment ZIPs are intentionally excluded. The two numbered hourly checkpoints were saved separately during work; this ZIP is the final deliverable.

## Evidence and limitations

One reader performed the transcription, second visual audits, and notation comparison. Research-only delegation began after the freeze; those workers did not read scan images or edit the transcription. All 42 page files and the combined transcription have their original freeze hashes in `records/frozen_hashes.json` and in the log, and their final comparison is recorded in `records/final_validation.json`.

The manuscript is difficult and contains unresolved readings. In particular, the faint early leaves, overwritten scalar expressions, final pairing, and pen drawings should be checked against the supplied images before relying on a disputed reading. The drawings are manual TikZ approximations. Structural validation is not a successful TeX compilation; the required support packages were unavailable, and the fragment deliberately has no preamble or definitions for the user-specified editorial macros.

The preflight listing of the context ZIP's filenames and the scan-033 save-order exception are disclosed in `progress.log`; no context payload was read before the freeze. The notes never change the frozen transcription, even where a mathematical calculation or the supplied modernized reading suggests another interpretation.

## Working records

Earlier readings in the page JSON records and historical page/audit scripts are retained as process evidence. The authoritative readings are the frozen files in `pages/` and the matching combined fragment. Running the historical page-writing, audit, notation, or freeze scripts would reconstruct earlier working states; they are included for documentation, not as a command sequence to rerun on the final text.

The final research-note bodies are stored once in the canonical notes Markdown. `scripts/build_notes.py` reads those bodies and the metadata in `records/note_definitions.json`; `scripts/render_notes.py` refreshes locations and the per-item search ledger when the original context is available in a sibling `context/` directory. This arrangement avoids duplicate literature summaries while preserving the research workflow.

The read-only-to-TeX checks are `python scripts/validate_structure.py` and `python scripts/validate_final.py`, run from this package directory. They write their reports under `records/` and leave the transcription unchanged.
