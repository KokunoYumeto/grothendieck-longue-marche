# Cote 156-6 — consolidated diplomatic transcription

## Scope and status

This edition covers the supplied scans 016–033, corresponding to handwritten pages 15–32. All 18 first readings have received the main reader’s crop review. 6 of 18 independent second readings have been adjudicated. The final transcription has not yet been frozen.

The scan images are the authority. The latest attached prompt governs; the earlier attached prompt versions are historical. No OCR, PDF text extraction, handwriting-recognition software, external mathematical research, or TeX compilation was used. Image processing was limited to documented crops, enlargement, contrast, sharpening and rotation for direct visual reading.

## Files

| File or directory | Contents |
|---|---|
| pages/ | Current consolidated LaTeX fragment for each scan. |
| SP112_CW_156-6_transcription.tex | All current page fragments in order, without a preamble. Formula-number placement is set on the left once for the edition. |
| SP112_CW_156-6_changes.md | Per-page decisions, witness readings, stroke evidence, confidence, counts and consequential corrections. |
| SP112_CW_156-6_collation.tsv | Localized differences from witness H, excluding macro-only changes. |
| SP112_CW_156-6_doubts.md | Notation table, remaining uncertainties, abbreviations and legibility note. |
| SP112_CW_156-6_inventory.csv | Every inventoried text block, display, diagram, margin, insertion and deletion, with transcription status. |
| SP112_CW_156-6_notes.md | Reading notes and the mathematical claims or limited checks actually considered. |
| CHECK_EVENTS.tsv | Actual mathematical check/use events at their stated strength. A visual transcription is not a proof. |
| SP112_CW_156-6_hand_log.md | Local observations about handwriting, corrections and layout. |
| SP112_CW_156-6_sheet_feedback.md | Classified localized error counts and recurring observations for later runs. |
| second/ | Fixed neutral box/group lists, immutable first readings, independent second readings, token differences, crop decisions and hash receipts. |
| first_reading_pages/ | Generated page text before blind comparison, matching the page hashes in the fixed second-reading manifest. Final readings are in pages/. |
| crops/ | Every saved first-reading and second-reading crop, including documented superseded crops. Original scans are not included. |
| records/ | Reader returns, crop coordinates, main-reader observations, coverage reviews, workflow evidence and validation records. |
| scripts/ | Reproducible image, comparison, assembly, validation and packaging programs; explicit manual decisions remain in the records. |
| progress.log | UTC completion/audit events, immutable hash anchors, checkpoint history and final freeze verification. |
| FILELIST.tsv | Every archived file except this self-referential manifest, with byte length and SHA-256. The manifest is generated from the archive’s staged bytes. |

## How to read the uncertainty and corrections

The supplied diplomatic macros retain deletion, insertion, margin placement and uncertainty. A favored alternative is not certainty. Clear slips, unfinished formulas, unexpanded short forms, local operator spellings, and mismatched handwritten delimiters are preserved. Font uncertainty is qualified at its first relevant occurrence on each page; later recurring forms use the same primary approximation. Canceled writing is not recovered merely because a likely sentence or formula can be guessed.

Crop coordinates are in pixels of the original whole scan, before enlargement or rotation. Narrow overlapping component boxes can belong to a single complete formula; the opaque group lists bind those components without revealing a proposed reading to the second reader. Blank or nonlexical leader boxes still receive explicit rows.

First-page line counts reflect the recorded counting scope. In particular scan031’s 24 counts main baselines only; its approximately 50–54 occupied baselines including additions were not retained as an exact tally. Scan033’s approximately 30–31 physical baselines is explicitly an estimate, while 46 is its exact logical inventory count. These are not inflated into exact physical-line claims.

The model identifier for this run is GPT-6 Astra Pro. The runtime does not expose a separately verifiable effort setting. Reader identities identify independent task contexts, not different model families. The exposure ledger excludes a reader from every page whose reading summary or private box metadata it had already received. Hash and structural checks establish workflow consistency; they do not prove a paleographic reading.

## Independent audit status

| Scan | First reader | Assigned second reader | Boxes | Token differences | Changed places | Status |
|---|---|---|---:|---:|---:|---|
| 016 | reader_a | reader_b | 47 | 42 | 9 | adjudicated |
| 017 | reader_b | reader_c | 50 | 44 | 3 | adjudicated |
| 018 | reader_c | reader_a | 39 | 32 | 4 | adjudicated |
| 019 | reader_c | reader_a | 44 | 33 | 4 | adjudicated |
| 020 | reader_b | reader_a | 68 | 65 | 12 | adjudicated |
| 021 | reader_a | reader_c | 51 | 41 | 4 | adjudicated |
| 022 | reader_a | reader_b | 47 | — | — | pending |
| 023 | reader_c | reader_a | 73 | — | — | pending |
| 024 | reader_b | reader_a | 68 | — | — | pending |
| 025 | reader_a | reader_c | 48 | — | — | pending |
| 026 | reader_c | reader_a | 57 | — | — | pending |
| 027 | reader_b | reader_c | 36 | — | — | pending |
| 028 | reader_a | reader_b | 41 | — | — | pending |
| 029 | reader_c | reader_b | 56 | — | — | pending |
| 030 | reader_b | reader_c | 42 | — | — | pending |
| 031 | reader_c | reader_b | 71 | — | — | pending |
| 032 | reader_a | reader_b | 31 | — | — | pending |
| 033 | reader_b | reader_c | 70 | — | — | pending |

A token difference can be a wrapper, spacing-boundary, alternate spelling or substantive ink reading. Each is adjudicated on a crop. “Changed places” counts changed boxed readings recorded by that audit; it is not the total count of changed characters or a claim that each comparison difference was an error.

## Input provenance

| Supplied file | Bytes | SHA-256 |
|---|---:|---|
| SP112_CW_156-6.zip | 21429946 | 6214efc819773f80165304322dfad7281621019b60b6ac2bd484714fc08281dd |
| PROMPT(20261124-133237).md | 43084 | da5ba7be0b9dd85e72a9307a85a6a64adc8d397b386e450674f4344a52d9114b |

The source archive was unpacked once. Witness C is the supplied draft; witness H is the supplied Commutator text at commit aef7db2. Original scans, witness files, source papers, attached prompts and earlier checkpoint ZIPs are excluded from returned archives. The records contain only the quotations and reading evidence needed to document this edition.

Guide generated: 2026-11-24 18:14:38 UTC.
