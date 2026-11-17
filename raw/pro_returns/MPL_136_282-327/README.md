# MPL_136_282–327

Diplomatic transcription and research notes for the 45 supplied scans of Montpellier cote 136, scans 282–327, with blank scan 319 omitted as specified in the assignment.

## Principal deliverables

| File or directory | Contents |
|---|---|
| `MPL_136_282-327_transcription.tex` | Combined LaTeX fragment, in scan order, without a preamble or macro definitions. |
| `pages/` | All 45 individual page fragments. |
| `MPL_136_282-327_doubts.md` | Final notation table, reading uncertainties and alternatives, confidence assessments, abbreviation list, and legibility report. |
| `MPL_136_282-327_inventory.csv` | 1,132 inventoried elements, each marked transcribed; 33 text sheets, 10 reused typed sheets, one cover, and one cancelled draft. |
| `MPL_136_282-327_notes.md` | The integrated research report: direct answers to the assigned questions, 67 numbered research notes, 24 entries on unverified or deferred steps, six title/pagination notes, ten reading questions, the RESULTS_STATE reconciliation, and references. |
| `progress.log` | UTC page-completion and second-reading records, notation review, transcription freeze, context opening, and final hash verification. |
| `frozen_hashes.sha256` | SHA-256 values of the 45 page fragments and the combined transcription. |

## Evidence and review

The transcription was read in one stream by the principal reader, using each whole-page image and both supplied halves. No OCR was used. Every page received a separate second visual audit; the transcription was frozen before the context archive was opened. Subsequent contextual and mathematical comparisons are confined to the research notes and their supporting records.

The final transcription contains 499 `\unsure` occurrences and one `\illegible{3}` occurrence. These marks express unresolved readings; the doubts file also preserves positioned reservations that do not correspond one-to-one with an inline macro. Mechanical validation verifies file coverage, permitted notation, structural consistency, inventory coverage, and the frozen hashes; it cannot certify the correctness of a handwritten reading.

The files are LaTeX fragments for an edition that supplies the specified editorial macros and the necessary mathematics/TikZ packages. A successful TeX compilation was not possible in the available environment because the format and required packages were missing. The compilation-environment record documents that limitation; no rendered PDF or successful compilation is claimed.

## Supporting work

`records/` contains doubt-extraction tables, research dossiers, detailed algebraic calculations, compilation-environment records, and the final validation report. The integrated notes and final doubts file are the principal reports; `records/doubts_table_draft.md` is explicitly retained as a superseded working record. Earlier contextual notes and RESULTS_STATE statuses are treated as reported research leads unless independently checked, and the report distinguishes manuscript assertions from the present calculations.

`scripts/` retains the tools used to record, assemble, validate, and package the work. The assembly script refuses to rewrite a frozen transcription. The archive excludes the supplied scans, context files, input archives, image crops, and Python bytecode caches.

To repeat the final structural checks after extraction, run `python3 scripts/validate_package.py --final --strict-macros` from this directory. To verify the frozen transcription without modifying the log, run `python3 scripts/assemble_and_freeze.py --verify`.
