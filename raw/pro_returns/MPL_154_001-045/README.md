# MPL_154_001–045 — delivered edition and research notes

This package contains a diplomatic LaTeX transcription of **all 44 retained scans** of cote 154, scans 001–045 with scan 011 omitted from the supplied set. The page files and combined fragment were frozen before the contextual research began. The final verification report and progress log record the comparison with all 45 frozen SHA-256 values.

## Main files

| File or folder | Contents |
|---|---|
| `MPL_154_001-045_transcription.tex` | The complete fragment, in scan order, starting with `\cotefile{154}` and `\scanpage{1}`; no document class or preamble. |
| `pages/` | One canonical `.tex` fragment for each retained scan. These are the frozen sources, not the historical page-writing scripts. |
| `MPL_154_001-045_doubts.md` | Consolidated notation table, complete current doubt index, abbreviation list and legibility assessment. |
| `MPL_154_001-045_inventory.csv` | 1,235 individually indexed page elements, each marked `yes`. |
| `MPL_154_001-045_notes.md` | English research notes: 114 numbered items; contextual comparisons; 67 indexed authorial questions, deferrals or revisions; titles, dates and page counts; and the research-state disposition. |
| `progress.log` | UTC work record, per-page completion and second-audit records, freeze hashes, context-opening time, checkpoint records and final verification. |
| `records/` | Frozen-hash manifest, validation and research-search records, comparison memos, and historical working materials. |
| `scripts/` | Work and recovery scripts retained to document how the files were produced. |

The main research notes are the final synthesis. Files named `*_draft.md`, the research-support memos, `reading_observations.md`, `reading_doubts_history.md` and the inventory before reconciliation are **working/history records**, not alternate authoritative editions. The current doubts and inventory are the main files named above.

## Coverage and documentary distinctions

| Measure | Count |
|---|---:|
| Retained scan pages | 44 |
| Frozen page files plus combined fragment | 45 |
| Inventory text elements | 377 |
| Inventory displays | 54 |
| Inventory diagrams/tables | 11 |
| Inventory drawing elements | 109 |
| Inventory marginal notes | 74 |
| Inventory deletions | 379 |
| Inventory insertions | 231 |
| Current `\unsure` occurrences | 464 |
| Current `\illegible` groups | 4, totaling an estimated seven words |

The sheet classifications comprise one institutional cover, 22 text sheets and 21 reused-typed sheets. Some of the latter show writing on the reverse of printed stock; classification does not imply that every page has a separate readable front-side printed block. No whole retained sheet was classified as a cancelled draft, although the transcription preserves many local cancellations and abandoned constructions.

The 44-scan selection count is not an authorial page count. The notes distinguish the two handwritten numbering sequences, marginal foliation, printer page labels and archive scan numbering. The institutional cover is not promoted to a mathematical title. Dates on reused 1982 computer printouts do not date the handwriting.

## How to read the transcription

The requested state macros retain cancellations, insertions, margins, underlining, drawings, diagrams and uncertainty. A first alternative in `\unsure{reading|alternative}` is the proposal based on the ink, not a mathematical correction. A surprising word, symbol, count or notation may be intentional or unresolved; the research notes do not change it.

Mathematical diagrams use `tikz-cd` or arrays for tables. Drawings use TikZ and contain their written labels. There are no embedded scan images. Fine pen jitter, exact curvature and printer spacing are approximations, not measurements. The least secure readings are crowded cancellations, small polygon accents and primes, labels crossing colored strokes, and faint printed repeated-character borders; the doubts file identifies the individual locations.

The final fragment requires definitions for the user-specified page-state macros and the usual mathematics and TikZ packages. `records/qa_wrapper.tex.txt` records the temporary **technical compile wrapper** used before the freeze. It uses colors for some states and suppresses underline rendering, so it is a syntax/layout inspection aid, not a final critical-edition stylesheet; its absolute `\input` path must be changed if reused elsewhere. Its extra cote-heading page accounts for 45 PDF pages during the technical compile, while the transcription itself contains 44 scan markers. The requested deliverable is the source fragment, not that temporary PDF.

## Research-note conventions and conclusions

The source keys M, R, N77, N127, H, B1 and B2 are defined at the start of the notes. A locator such as `019:43–47` means scan 019 and lines of its frozen page fragment. H uses Hua's own page numbering; here H page *p* corresponds to archive scan *p*+1, independently of the manuscript's restarted foliation.

The primary classification is **neither** of the two proposed broad subjects: this is specifically combinatorial geometry of relative-position and deployment surfaces, directly comparable with the *Esquisse* §8 problem, with a connection to tame topology but no established identification with the 1986 geometry-of-forms programme. This is a narrower classification than the earlier packages' broad tame-topology placement, and that difference is explicit.

The main unresolved mathematical items are scan 019's expected injectivity; scan 025's local-system assertion and face compatibility; scan 035's chord-realization sufficiency; and the exceptional surface completion in scans 040–043. The notes distinguish the five surface variants, the source's local arguments and withdrawals, our conditional consistency tests, and the limitations of the modernized comparison. No result in the supplied research-state register was promoted, refuted or otherwise changed in status.

## Method and integrity

The same reader transcribed all retained pages in order, directly viewing each whole page and both supplied halves, then performed a second visual audit of every page. No OCR was used. Context comparison and analytical review were delegated only after the transcription freeze.

The freeze is **2026-11-17 15:15:39 UTC**; context contents were first opened at **15:15:45 UTC**. One protocol deviation is disclosed in the notes and log: the ZIP directory metadata was listed before the freeze, but its file contents were not opened then and did not guide a reading. All post-freeze reading differences are confined to the research notes.

Do not rerun historical `pageNNN.py`, `workflow.py` without its checkpoint argument, or `audit.py` against the delivered sources: those scripts document earlier writing operations and could overwrite frozen files. The canonical delivered page fragments, combined fragment and their hash manifest are the final record. The validation script reads them without rewriting them; the context-search script writes only its search journal.

The supplied scans, input ZIPs, prompt and context source files are deliberately excluded from this archive. The archive includes the new deliverables and work records; contextual excerpts in the search journal document the comparisons rather than reproduce the supplied source files in full.
