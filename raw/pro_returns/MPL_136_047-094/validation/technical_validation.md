# Technical validation of the page fragments and inventory

Final table and integrity refresh: 2026-11-16 14:38:25 UTC. The compilation results below refer to the previously accepted final page snapshots; this refresh recounted the final tables, checked their Markdown structure and verified the frozen transcription hashes.

## Scope

These are mechanical checks of the final 46 page fragments and the associated tables. They do not constitute a second handwriting reading, a visual comparison of diagrams, or a judgment of mathematical correctness. No scan image, OCR output, context-archive content, or literature was used in these checks. The page fragments, combined transcription, inventory, doubts, research notes, observations and progress log were not edited during this technical validation.

## Results

| Check | Result |
|---|---|
| Expected scan files | All 46 present: 048–078 and 080–094 |
| Scan macros | One correct scan macro per page; the cote macro occurs in the first page |
| Brace and environment checks | Passed for every page |
| XeLaTeX compilation | Every final page revision has a successful independent snapshot compilation |
| Missing-character warnings | None in the accepted final runs |
| Snapshot identity | All 46 current page hashes match the successful compilation snapshots and refreshed uncertainty-extraction hashes |
| Frozen transcription integrity | All 47 hashes in `transcription_frozen.sha256` match: 46 page fragments and the combined transcription |
| Editorial macro names | Only the specified editorial macros occur; the remaining commands are standard LaTeX/math/TikZ commands |
| Disallowed file-level additions | No preamble, image inclusion, input/include command, caption command or macro definition occurs in the page fragments |
| Inventory schema | Correct columns; valid kind and sheet-kind labels; unique element identifiers within each scan |
| Inventory coverage | 950 rows across all 46 scans; every row has `transcribed=yes` |
| Uncertainty extraction | 494 `\unsure` and 50 `\illegible` occurrences; 544 total; no malformed braced arguments |
| Doubts-document tables | 544 lexical-macro rows plus 6 additional geometry/provenance rows; 30 notation rows and 94 abbreviation rows |
| Uncertainty-row coverage | All 544 extracted macro IDs have exactly one doubt-table row with the correct scan; no missing, unexpected or duplicate IDs |
| Markdown table structure | All 4 tables in the doubts document and all 6 tables in the research notes have consistent GFM column counts; escaped internal bars are respected |
| Research-note numbering | 65 items, numbered R001–R065 without gaps or duplicates |

The compilation wrapper is separate from the deliverable fragments. It supplies transparent definitions for the editorial macros and loads the required mathematical and TikZ packages. It uses no-argument transparent wrappers so that TikZ matrix ampersands are tokenized correctly. No preamble was inserted into a page or the combined transcription. Compilation checks syntax and command availability; it does not certify the physical placement or shape of manuscript elements.

The full 46-page run succeeded. After the final accent encoding change on scan 050, that page was compiled again successfully and its source hash was refreshed. The accepted runs have no missing-character warnings. Pagination and line-width warnings from the temporary wrapper are not manuscript-layout findings because the requested deliverable is a LaTeX fragment without a fixed page design.

## Inventory counts

| Element kind | Rows |
|---|---:|
| Text | 420 |
| Display | 162 |
| Diagram | 54 |
| Drawing | 28 |
| Margin note | 110 |
| Insertion | 58 |
| Deletion | 118 |
| **Total** | **950** |

Deletion, insertion and diagram macro counts agree with the corresponding inventory counts on every scan. A margin wrapper can contain an element inventoried as a drawing, and one wrapper can contain more than one separately inventoried note. Consequently, counting wrappers alone is not an inventory-completeness test. The remaining numerical differences are accounted for as follows.

| Scan | Source count / inventory count | Existing inventory representation |
|---|---|---|
| 054 | 4 margin wrappers / 2 margin-note rows | The two additional wrappers contain the drawings in 054-07 and 054-19. |
| 072 | 3 margin wrappers / 4 margin-note rows | Row 072-08 records the ellipse-marked arrow label within the diagram. |
| 076 | 4 margin wrappers / 5 margin-note rows | One wrapper contains the two notes separately recorded in 076-08 and 076-10. |
| 077 | 1 figure wrapper / 2 drawing rows | The circled D in 077-11 is encoded with `\textcircled`, not a figure wrapper. |
| 081 | 2 margin wrappers / 1 margin-note row | The additional wrapper contains drawing 081-11. |
| 087 | 2 margin wrappers / 1 margin-note row | The additional wrapper contains drawing 087-08. |
| 089 | 3 margin wrappers / 2 margin-note rows | The additional wrapper contains drawing 089-07. |
| 094 | 5 margin wrappers / 4 margin-note rows | The additional wrapper contains drawing 094-29. |

This reconciliation is based on source structure and existing inventory labels. It identifies no remaining unexplained macro-count difference and makes no new reading judgment. It does not by itself prove that every ink element was captured; that belongs to the primary reader's page-by-page inventory audit.

## Included evidence and reproducibility

- `validated_pages.sha256` identifies the 46 final page revisions that passed compilation and matched the refreshed uncertainty extraction.
- `validated_tables.sha256` identifies the inventory and doubts documents counted in this report.
- `doubt_extraction_counts.tsv` records uncertainty-macro counts for each scan.
- `inventory_count_reconciliation.tsv` records the eight explained count differences above.
- `scripts/validate_package.py` checks package structure, ordered concatenation, inventory schema and frozen hashes when available.
- `scripts/extract_doubts.py` parses balanced arguments recursively, preserves raw contents, links nested uncertainty macros, and splits alternatives only at unescaped bars outside brace groups. Such lexical splitting does not decide whether a bar has a mathematical meaning.
- `scripts/check_inventory_macros.py` reports command names, nesting and numerical macro/inventory differences without altering content.
- `scripts/check_tex_compilation.py` compiles independent temporary page snapshots with an external validation wrapper.

Selected validation wrappers, compiler logs, command output, extraction reports and manifests are retained in `validation/history/` as an audit trail. Earlier rounds may record failures that were superseded by the accepted final runs; the current compilation claims refer to the final page revisions identified by `validated_pages.sha256`. The TeX runtime, format files, temporary page snapshots and generated compilation PDFs remain outside the deliverable package.

The combined transcription, freeze record and post-context integrity check are separate assembly-stage records in `progress.log`. This refresh verified all 47 entries of `transcription_frozen.sha256`; `validated_tables.sha256` identifies the final inventory and doubts documents counted here. The Markdown and numbering checks on the research notes are structural checks at the refresh time, not a transcription freeze or a mathematical review.
