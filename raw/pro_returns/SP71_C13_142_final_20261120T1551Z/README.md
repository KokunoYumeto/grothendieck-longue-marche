# SP71_C13_142 — consolidated diplomatic transcription

This edition covers the 24 supplied scans in order: 052–064, then 066–076. The separate cover is scan 066. The supplied H page numbers are one less than the scan numbers; there is no dedicated H text for scan 066.

## Reading and scope

The root reader personally read every scan against C and H, completed the page apparatus before proceeding, then read all 24 consolidated pages against the images a second time. A final comparison checked recurring notation across the run. No page reading, ink decision, or mathematical decision was delegated. A separate structural review examined only file coverage, schemas, counts, macro strings, and packaging rules. No OCR, text recognition, external research, or TeX compilation was used.

The transcription follows the ink, including apparent authorial slips, absent accents, repeated numbering, unmatched written punctuation, cancellations, insertions, and marginal notes. Mathematical repairs and conditional interpretations appear only in the notes and check events. The scans supplied with the task are the primary sources; no claim is made that this edition replaces examination of them.

## Contents

| File or directory | Purpose |
| --- | --- |
| `pages/142_scanNNN.tex` | Final page fragments, one per scan. These are the authoritative transcription files. |
| `SP71_C13_142_transcription.tex` | Exact ordered concatenation of the 24 fragments, without a preamble. Use the PREAMBLE.tex supplied with the task. |
| `SP71_C13_142_changes.md` | Witness differences, counts, consequential readings, unresolved places, and the full crop ledger by scan. |
| `SP71_C13_142_collation.tsv` | H differences only; 373 rows, with no rows for 066. |
| `decisions.tsv` | All 138 supplied MARKS entries, in their original order. |
| `SP71_C13_142_doubts.md` | Cross-page notation review, remaining doubts, exact occurrence index of in-text uncertainty marks, abbreviations, and legibility assessment. |
| `SP71_C13_142_inventory.csv` | 475 inventoried text and graphic elements, including additions and cancellations. |
| `SP71_C13_142_notes.md` | English notes on what each sheet states, reading implications, authorial slips, and qualifications of the mathematical checks. |
| `CHECK_EVENTS.tsv` | 63 check events, each classified according to the actual work performed. |
| `SP71_C13_142_hand_log.md` | Observed letter forms, notation habits, scope, exceptions, and witness consequences. |
| `SP71_C13_142_sheet_feedback.md` | Counts by error-sheet kind and specific recurring mechanisms for future passes. |
| `progress.log` | Actual UTC completion/audit times, checkpoint record, freeze hashes, and final unchanged-hash confirmation. |
| `audit_log.md` | Second-reading observations, source-level corrections, and representation repairs. |
| `crop_register.tsv` | Original pixel boxes and processing metadata for all 144 crops. |
| `scripts/` | Reading-record data, report generation, page-assembly history, image-view preparation, structural validation, and packaging helpers. |

The final changes apparatus contains 393 substantive places: 84 differ from C and 373 from H, with overlap. The confidence totals are 255 high, 94 medium, and 44 low. Certainty-only entries are separate and are not included in these counts. Grouped figure or formula revisions are explicitly located; these totals are not counts of changed letters or strokes.

## Scripts and reproducibility

The final `pages/` files and `scripts/records/NNN.py` records include the audit and global-review changes. `scripts/record_reading.py` regenerates the apparatus and concatenated fragment from those current files. The `pageNNN.py` assembly scripts document the original page construction and some subsequent repairs; they are not a replacement for the final page files. Their save routine refuses to overwrite existing records. Do not rebuild the final edition by rerunning the initial assembly scripts.

Image preparation was limited to native overlapping halves and one crop per unresolved place. The supplied images, witness texts, halves, crops, prior checkpoint archives, caches, and attached prompt are deliberately absent from this archive. To resume image work, restore the original attachments alongside the work directory. Every crop is documented without returning its image.

Structural validation is deliberately narrower than an editorial judgment: it checks page and mark coverage, table structure, count agreement, ordered progress entries, concatenation, frozen hashes, and archive contents. It does not certify an ink reading or a mathematical theorem. A static macro scan can flag TikZ-local variables such as `\a` or the second slash of `\\P`; the reviewed lexical cases are explained in the validation record. No rendering or compilation is implied by these checks.
