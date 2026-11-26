# SP110_CW_134-2 — consolidated diplomatic transcription

## Scope and authority

This package covers only archive scans **184–185**, manuscript pages **39–40**, cote **134-2**. The latest attached prompt governs the work; the older prompt versions are not separate tasks. Witness H's corresponding pages are 183–184. Rows for other scans in the supplied mechanical difference list were excluded.

The supplied images decide the readings. No OCR, PDF text recognition, external historical or mathematical research, or TeX compilation was used. The notation, uncertainty, deletion and insertion macros follow the supplied witness-C preamble and conventions.

## Final deliverables

| File / directory | Purpose |
| --- | --- |
| pages/ | The two final page fragments, named as in witness C. |
| SP110_CW_134-2_transcription.tex | Ordered combined fragment, beginning with one cotefile marker and containing no preamble. |
| SP110_CW_134-2_changes.md | C/H/final decisions, confidence, source-stroke descriptions and exact crop boxes; also blind-audit changes. |
| SP110_CW_134-2_collation.tsv | Required eleven-column list of differences from H. |
| SP110_CW_134-2_doubts.md | Current notation table, remaining alternatives, abbreviations and legibility assessment. |
| SP110_CW_134-2_inventory.csv | Required eight-column element inventory; every element marked transcribed. |
| SP110_CW_134-2_notes.md and CHECK_EVENTS.tsv | Short per-page notes and explicit records of what was checked or merely reported. |
| SP110_CW_134-2_sheet_feedback.md | Counts under the ten supplied error-sheet categories, with qualifications. |
| SP110_CW_134-2_hand_log.md | Locally verified handwriting habits, scope and exceptions. |
| progress.log | Actual UTC work events, completion/audit entries and the frozen transcription hashes. |

## Reading and audit evidence

- **crops/** contains first-reading and independently generated blind-reading crops, with tab-separated pixel-box manifests. A crop's coordinates refer to the original 1681-pixel-wide supplied whole scan. The images are enlarged for inspection; enlargement is not additional source detail.
- **second/** preserves each neutral box list, the root reading committed before comparison, the independent reading, the literal token comparison, and the final adjudication. Original committed first/second readings are not rewritten to make them agree.
- **drafts/** preserves first-reader reports and page snapshots, root pre-audit page snapshots, and structured decision records used to build the logs. These are documentation of earlier decisions. The final transcription is in pages/ and the combined fragment.
- **scripts/** contains crop, comparison, report-building and structural-validation utilities. No recognition or TeX-rendering step is part of them.
- **sources.tsv** identifies the supplied inputs by name and SHA-256. The attached scans, witnesses, prompts and earlier notation tables are intentionally not copied into this output archive.

Two first readers handled the two leaves separately; a third reader was initially reserved for the blind stage. The request for three simultaneous first readings on different pages cannot literally be met with two pages. A proposed reassignment at the blind stage was declined when the reader noticed indirect exposure to candidate text; a fresh context was used instead. These assignments and the preserved evidence are recorded in the progress log.

Line numbers in the reports are physical handwritten body baselines, not lines of the LaTeX files. Scan 184 has 24; scan 185 has 19 including its three closing/signature lines. Page and archive numbers are inventoried separately.

The supplied PREAMBLE.tex is needed by the surrounding edition but is not duplicated here. Only the transcription fragments are frozen by the reported SHA-256 values; later packaging metadata does not change their text.

## Completed audit

The independent audit covers 40 boxes. There are 29 literal token-difference boxes; those include harmless scope, syntax and spacing differences and are not a count of errors. Adjudication changed one preferred word ending and resolved two added doubts, all on scan 184. Eight doubt groups remain in the final pages. The final inventory contains 32 elements, all marked yes. The package includes one supplemental audit crop that widens the L15 ending to include the following word.

All 13 original C doubt groups have dispositions: six resolved, seven retained or narrowed. One newly added doubt remains (coh./ch.); the added constant/constante and les/le doubts were resolved during the blind audit.
