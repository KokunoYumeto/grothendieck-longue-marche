# Documentation-only audit: scans 179–180

## Scope

Read the complete `report.json` and `reading.tex` returns for A, B and C on each of scans 179 and 180; then both `decision.json` files, both consolidated page TeX files, and both `main_viewed_crops.txt` ledgers. No image, crop, original scan, original witness source, PDF, external source, other page, or future-page content was opened. No TeX engine or rendering was used. JSON paths below use zero-based array indices.

The audit tests the written record only. Recorded visual justifications are accepted as adjudications, without a fresh judgment about the ink.

## Finding

### 1. Scan 180: final inventory assigns the archive number to the author's hand, contrary to all three reader records

- **Final location:** `records/scan180/decision.json`, `$.inventory[10].hand` is `"his hand"`. The same object identifies `$.inventory[10].element` as `"archive sheet number"` and `$.inventory[10].first_words_or_objects` as `"180"`.
- **Reader A:** `records/scan180/A/report.json`, `$.inventory[10].hand` is `"archive pencil; not assigned to the author"`.
- **Reader B:** `records/scan180/B/report.json`, `$.inventory[9].hand` is `"archive pencil hand, separate from the main writing"`.
- **Reader C:** `records/scan180/C/report.json`, `$.inventory[10].hand` is `"archive pencil hand"`.
- **Internal corroboration:** `records/scan180/decision.json`, `$.notes` distinguishes author page 35 from archive pencil 180, and `$.doubt_review[15].evidence` calls 180 the “distinct archive pencil” number. `pages/H134-06_134-2_scan180.tex` retains 180 only in the archive-sheet comment. No entry in `$.reader_comparisons` supplies a reason for reassignment to the author's hand.

This is a concrete attribution contradiction introduced by the final inventory. It does not require choosing between competing ink readings: the three reader inventories agree on the archival role, and two explicitly separate it from the author/main hand. The documentation supports an archive-pencil attribution, while the consolidated field asserts the author's hand.

## Remaining checks

No additional unresolved omission or contradiction was found in the requested areas.

| Check | Scan 179 | Scan 180 |
|---|---|---|
| Witness differences | All reported physical loci are represented in `$.differences[0..15]`; the two C-reader L9a rows are covered by the combined wording/placement entry `$.differences[8]`. | All reported physical loci are represented in `$.differences[0..17]`. |
| Reader disagreements | `$.reader_comparisons[0..8]` addresses article, noun ending, overwritten layers, plural ending, insertion scope, finis, adjective ending, C's L18 comma ledger inconsistency, and combined versus split overwrite inventory rows. | `$.reader_comparisons[0..4]` addresses the loc stop, inline-point representation, adjective alternatives, cancelled accent, and the distinction between textual doubt and physical-mark origin. |
| Required C questions | All 11 questions are covered by `$.doubt_review[0..10]`. | All 14 questions and both earlier-note topics are covered by `$.doubt_review[0..15]`. C reader's earlier-note content is present in its notes although its question array has only the 14 numbered questions. |
| Uncertainty-only differences from H | Added uncertainty for finis and first P uses `"other"` at `$.differences[12].kind` and `$.differences[14].kind`. | First-P uncertainty uses `"other"` at `$.differences[10].kind`. The connector rows change the preferred sign from H's arrow to a plain connector with arrow alternative, so they are not merely uncertainty wrappers around the same preferred sign. |
| Distinct inventory coverage | All reader objects, including both states of the combined overwrite sites and the single underline recorded within the prose entry, are covered by `$.inventory[0..14]`. | All reader objects, including the point beside X, detached slash and point pair, are covered by `$.inventory[0..10]`; the hand attribution defect is Finding 1. |
| Notes and events | All three reader `$.check_events` arrays are empty. Final `$.notes`, `$.check_events[0..4]` and `$.note_statements[0..3]` consistently distinguish source assertions from independent proof. | All three reader `$.check_events` arrays are empty. Final `$.notes`, `$.check_events[0..4]` and `$.note_statements[0..3]` likewise make no unsupported claim of proof, computation or mathematical checking. |
| Final page agreement | The consolidated TeX follows the final readings and retained doubts. | The consolidated TeX follows the final readings and retained doubts. |
| Recorded main crop references | All crop paths explicitly cited in the decision occur in the 14-entry, duplicate-free main-viewed ledger. | All crop paths explicitly cited in the decision occur in the 16-entry, duplicate-free main-viewed ledger. |

## Recorded adjudication grounds

These are the final record's stated reasons, not independent visual findings of this audit.

- **Scan 179:** `$.reader_comparisons[0..7].decision` selects des from an e return and hooked s; singular diagramme from the absence of a separate low final s hook; the preferred overwritten order from darker high l-like versus paler low d-like strokes, with both alternatives retained; élémentaires from a separate descending hook; one raised replacement group from its alignment above the cancellation; doubt on finis from broken faint strokes; précisé/précisée from a visible acute and unresolved vowel count; and no L18 comma because the terminal stroke belongs to s. The written record explicitly acknowledges and disposes of C's inconsistent comma coverage entry.
- **Scan 180:** `$.reader_comparisons[0..3].decision` selects unpunctuated first loc because the dark end belongs to c; a literal inline point beside X from its separated low position, without assigning sentence meaning; virtuels/mutuels from the v/i-like beginning, small high point, r-like entry and clear l/s ending; and a/à/comma for the cancelled mark because the loop survives but a separate accent does not. `$.reader_comparisons[4].decision` retains uncertain origin/function of physically clear marks in notes and inventory rather than adding textual doubt tokens.

Only this audit report was created. Pages, decisions, shared aggregates and notes were not modified.

## Root disposition

Root reports that Finding 1 has been corrected: `records/scan180/decision.json`, `$.inventory[10].hand` now reads `"archive pencil hand; distinct from main writing"`. Root also restricted the helper's author-hand normalization. No page text changed.

The report above was restored verbatim from the retained written tool-call text after the workspace reset. This separate disposition records Root's supplied correction; no new audit or image inspection was performed during recovery. Only this report was restored.
