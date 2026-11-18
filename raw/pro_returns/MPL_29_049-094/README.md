# MPL_29_049-094

This package contains the diplomatic transcription and research apparatus for **42 retained scans of cote 29**: scans 049–094, excluding 079, 080, 081 and 083 as specified in the task. The single reference to 46 pages in the supplied prompt describes the inclusive range, not the retained image set.

## Main files

| File | Contents |
|---|---|
| `MPL_29_049-094_transcription.tex` | All 42 pages in scan order, as a LaTeX fragment without a document preamble. |
| `pages/` | One separately saved LaTeX fragment per retained scan. |
| `MPL_29_049-094_doubts.md` | Recurring-notation table, 473 explicit uncertainty occurrences, placement reservations, abbreviations and legibility assessment. |
| `MPL_29_049-094_inventory.csv` | 822 element rows, all marked `transcribed=yes`, with sheet-kind classification. |
| `MPL_29_049-094_notes.md` | Research notes, context comparisons, primary-source references, and separate standing sections for author-marked unverified steps and titles/pagination. |
| `CHECK_EVENTS.tsv` | Actual mathematical check/use/refutation events, with model, available effort information, run and outcome. |
| `progress.log` | Start time, immediate page-completion records, second-reading records, freeze hashes, context-opening time and final integrity check. |

## Reading and verification

The primary reader inspected each whole page and both supplied halves, transcribed in order, and completed a second image reading of every page. **No OCR and no parallel transcription or image audit were used.** The notation audit, doubts consolidation and LaTeX compile check preceded the freeze.

The transcription was frozen at **2026-11-18 04:03:52 UTC**, before the context was opened at **04:03:58 UTC**. Its 43 hashes cover the 42 page fragments and their combined transcription. The final validation compares every one with the frozen record; no post-context correction of the transcription is permitted or made.

The fragment uses the state macros specified in the prompt; macro definitions are intentionally absent from the transcription. `work/compile_check.py` supplies a temporary harness for syntax checking, and `work/validate_package.py` performs read-only structural checks. A successful compilation is evidence about syntax, not about the correctness of an ink reading.

## Research apparatus and limits

The main notes keep each item to one to four sentences, with its witness, kind, context comparison, results-state scope and, for own ideas, confidence and reason. Detailed proof calculations remain in `work/birational_research.md`, `work/picard_research.md` and `work/formal_research.md`; a separate review of the formal-Picard counterexample is in `work/picard_formal_counterexample_check.md`.

The supplied Hua interpretation is credited and treated as a lead, never as authority to repair the frozen text. Context references to scans outside the supplied range are identified as such. The results-state entry `29-formal-tame-pi1-self-intersection` receives substantive qualifications, while the nearby LM1 and cote 56 entries are not claimed to be settled.

The least secure readings are the compressed corrections on 050/062, margins on 071, cancelled draft 087, lower margin 092 and overwritten formulas at the foot of 094. The 473 doubt occurrences are explicit reservations, not a measured error rate and not a guarantee that every unmarked reading is correct.

The work records include historical first-pass readings and intermediate notes. Where these differ from the final apparatus, the frozen transcription and consolidated doubts file govern the diplomatic reading, and the main research notes govern the integrated research conclusions. Supplied scans, source archives and context files are not recopied into this package.
