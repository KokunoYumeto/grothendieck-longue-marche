# Mechanical QA record

Recorded 2026-11-15 16:13:45 UTC.

## Scope

The ancillary check covered completed scans 087–102: 16 page files and 231 inventory rows. The partial validator reported zero structural errors and seven review flags for ellipses or “etc.” These checks establish neither transcription accuracy nor visual completeness; no manuscript images or research-context contents were inspected by the mechanical-checking worker.

A subsequent diagram syntax check found one terminal backslash at scan 102, line 15, where the matrix row continued onto the next source line. This was reported to the primary reader, who confirmed that the image has two rows and is handling the correction. The validator now flags a single backslash at a line end within `tikz-cd` for human review. A suspected `\de` occurrence in scan 100 was a tokenization false positive: the source contains a node line break followed by `de`.

## Compilation attempt and environment limit

The combined transcription was rebuilt with `workflow.combined()`. A temporary snapshot and wrapper were used outside the package directory. LuaLaTeX stopped before parsing the document with:

```text
I can't find the format file `lualatex.fmt'!
```

`kpsewhich` found none of `lualatex.fmt`, `xelatex.fmt`, `pdflatex.fmt`, `lualatex.ini`, `xelatex.ini`, `latex.ltx`, `tikz.sty`, `tikz-cd.sty`, `fontspec.sty`, or `ulem.sty`. The engine executables are present; the required TeX distribution files are unavailable. Consequently, no successful compilation or rendered-document verification is claimed. No dependency installation was attempted.

## Reusable harness

`records/compile_wrapper.tex` contains the macro definitions and package imports for a future syntax check. Run it from the package root with an existing temporary output directory, as its header describes. It inputs the current combined transcription directly; no duplicate transcription snapshot is included in the package. The editorial macros retain their arguments with minimal presentation. This harness is for mechanical compilation checks only.

## Follow-up mechanical check: scans 087–120

Recorded 2026-11-15 16:34:49 UTC. The combined transcription was rebuilt with `workflow.combined()` before validation. The checked set comprised 33 page files and 484 inventory rows, excluding the omitted scan 116. The package remains unfrozen.

The partial validator reported zero structural errors: page markers and ordering, combined-file correspondence, inventory structure, completion-log events, brace balance, and environment balance passed. No single-backslash row-separator warning remained, including the previously reported scan 102 location. All authorized state-macro occurrences had braced arguments. Additional syntax counts found an even number of unescaped dollar signs on every page, matching opening/closing display and inline math delimiters, and matching `\left`/`\right` counts. These are syntax checks, not a substitute for compilation or visual reading.

The 12 remaining review flags concern explicit ellipsis syntax or “etc.” at scans 092, 094 (two), 097, 099, 100, 101, 105 (two), 106, 110, and 120. They are review candidates only; they do not establish omissions. No other concrete defect was found in this pass.

### Authorized state-macro counts

| Macro | Count |
|---|---:|
| `\cotefile` | 1 |
| `\scanpage` | 33 |
| `\mspage` | 28 |
| `\deleted` | 149 |
| `\inserted` | 75 |
| `\margin` | 49 |
| `\uline` | 116 |
| `\uuline` | 0 |
| `\diagram` | 22 |
| `\figure` | 4 |
| `\unsure` | 277 |
| `\illegible` | 3 |

Every page containing `\unsure` or `\illegible` had at least one registered doubt row. The exported doubt register contains 151 rows for scans through 120. This page-level presence check does not establish that each individual doubtful reading is covered: a register row may group several occurrences, and numerical counts alone cannot resolve that relationship. The validator now offers `--macro-report` to print macro counts and scan-level exported register-row counts.

No manuscript images or context-archive contents were inspected during this pass. No page transcription was changed. No new compilation attempt or dependency installation was made; the previously documented TeX distribution limitation still governs the available verification.

## Follow-up mechanical check: scans 087–131

Recorded 2026-11-15 16:48:20 UTC. `workflow.combined()` rebuilt the combined transcription. The saved set comprised 43 scans and 665 inventory rows: the 45 numbered positions from 087 through 131, excluding 116 and 127. The partial validator reported zero structural errors and no diagram row-separator warnings. The 27 review flags concern ellipses or “etc.” and require the primary reader's judgment. The transcription remains unfrozen.

`records/doubt_occurrences.json` indexes all 373 doubt-macro occurrences in those 43 page files: 369 `\unsure` and 4 `\illegible`. Each occurrence records the page filename, relative path, scan, one-based source line and column, macro name, complete argument, and argument ending line. Balanced-brace parsing retains nested groups, escaped braces, and all written argument text; comments are masked only during syntax recognition so source offsets remain exact. 24 indexed arguments contain brace characters. Nested doubt macros are indexed individually. Per-page SHA-256 values document the indexed source versions and do not freeze the transcription.

`records/index_doubts.py` is the reusable generator. This pass used `--max-scan 131`; run it without that option to index all saved pages after further work. The index supplies locations and literal source arguments only. It makes no reading, confidence, notation-consistency, or individual register-coverage judgment.

No page transcription or doubt-register entry was edited. No scans or context contents were viewed. No checkpoint was created or uploaded.

## Read-only review of all 48 pages during the visual audit

2026-11-15 17:02:43 UTC. The primary reader's audit is in progress, so source-line references and counts describe this pass and can change before freeze. No combined transcription, doubt index, page file, register, or inventory was rewritten.

### Structural findings

Individual-page brace, environment, and state-macro argument checks and CSV structure checks reported no errors. No single-backslash row-separator warning was found. Additional syntax inspection counted 33 diagram wrappers, 10 figure wrappers, and 85 `\arrow` commands; all diagram/figure wrappers contained the corresponding `tikzcd`/`array` or `tikzpicture` environment, and every inspected arrow option list had a closing bracket and paired quotation marks. These checks do not constitute a successful TeX compilation or visual verification.

### Pagination requiring an inventory check

The following `\mspage` arguments have no inventory row whose identifying field names that page number. The main text may have been grouped in another row; the primary reader should supply or identify the explicit pagination element during audit.

| Scan | Source line | `\mspage` argument |
|---:|---:|---|
| 110 | 30 | `109` |
| 111 | 16 | `110` |
| 112 | 23 | `111` |
| 113 | 14 | `112` |
| 114 | 4 | `113` |
| 115 | 30 | `114` |
| 117 | 31 | `116` |
| 118 | 13 | `117` |
| 119 | 17 | `118` |
| 120 | 11 | `119` |
| 121 | 31 | `120` |
| 122 | 25 | `121` |
| 123 | 25 | `122` |

### Reused typed sheets: pagination-role review

These sheets are classified `reused_typed`. Their current sources place the following labels in `\mspage` and `\margin`, respectively. The primary reader should verify from the image which label is the manuscript sheet number and which belongs to the reused typed text; this mechanical review supplies the exact source pairing without assigning those visual roles.

| Scan | `\mspage` argument | Numeric `\margin` argument |
|---:|---|---|
| 091 | `43` | `90` |
| 093 | `42` | `92` |
| 095 | `-7-` | `94` |
| 097 | `-5-` | `96` |
| 099 | `-4-` | `98` |
| 101 | `96` | `100` |
| 103 | `IV.8` | `102` |
| 105 | `94` | `104` |
| 107 | `92` | `106` |
| 109 | `-10-` | `108` |

### Concrete explanations of margin-count differences

- Scans 111, 113, 115, 120, and 122 encode numeric labels `86`, `84`, `85`, `78`, and `77` in `\margin`. Inventory rows 111.01, 113.01, 115.01, 120.01, and 122.01 identify those exact labels under kind `text`. This is a kind-assignment review, with explicit corresponding inventory entries.
- Scan 112's upper-left `\margin` contains its diagram; inventory row 112.01 records that diagram under kind `diagram`.
- Scan 123's three `\margin` wrappers contain two diagrams and a drawing; rows 123.05, 123.09, and 123.11 record those contents under kinds `diagram`, `diagram`, and `drawing`.
- Scan 091's additional margin wrapper contains a drawing recorded at 091.05; scan 110's additional margin wrapper contains the upper-left diagram recorded at 110.01.
- Scan 121's two callout inventory entries 121.22 and 121.25 occur inside the drawing recorded at 121.21, explaining the extra margin-note rows relative to `\margin` wrappers.
- On numerous other pages, a `\mspage` label has an inventory row of kind `margin note`; this contributes one inventory row without a `\margin` macro. Macro-count equality therefore requires direct element mapping, not an assumption that each outer wrapper has its own row.

### Grouped deletion and insertion rows for element-level audit

The following rows explicitly group several source wrappers. Whether these represent one physical deletion/insertion or several separate elements must be checked against the image by the primary reader.

| Scan | State | Macro count / matching-kind rows | Rows to examine |
|---:|---|---|---|
| 088 | deletion | 7 / 6 | 088.11 groups the two deleted phrases beginning `Dans le cas` and `Prenant` |
| 092 | deletion | 10 / 9 | 092.06 groups `Alors les opér.` and `Soit U` |
| 096 | deletion | 13 / 8 | 096.03, 096.06, 096.13 group several deletions |
| 098 | deletion | 7 / 6 | 098.02 groups `gal.` and `tot.` |
| 100 | deletion | 7 / 6 | 100.16 groups two deletions |
| 100 | insertion | 4 / 3 | 100.07 groups `i∈Z` and `absolue` |
| 102 | deletion | 9 / 7 | 102.10 groups three deletions: `(q)`, `(q)`, and `Z` |
| 104 | deletion | 12 / 6 | 104.05, 104.13, 104.15 group multiple deletions |
| 106 | deletion | 8 / 4 | 106.02, 106.08, 106.09 include grouped or nested deletions |
| 106 | insertion | 3 / 1 | 106.10 groups `une` and `de poids i`; the nested `\inserted{\deleted{\unsure{tel}}}` at source line 11 has no separately identified insertion row |
| 108 | deletion | 10 / 8 | 108.15 and 108.21 each group two deletions |
| 119 | insertion | 4 / 3 | The source's `\inserted{i.e. $U$ un tore}` is nested in a margin wrapper and corresponds to 119.17, currently kind `margin note` |

No scans or context-archive contents were opened. No reading judgment, visual coverage claim, or mathematical correction was made.

## Post-audit, pre-freeze mechanical pass over all 48 pages

2026-11-15 17:28:13 UTC. All 48 page files were checked read-only while final notation edits remained authorized to continue. The partial validator reported 825 inventory rows, zero structural errors, and 29 review flags for ellipses or “etc.” The combined transcription matched the page concatenation at the validator snapshot; no combined mismatch was present in that snapshot. Later source edits can invalidate that result until the requested final rerun.

`records/mechanical_snapshot_hashes.json` records source, inventory, and combined-file hashes around validation; `records/validation_audit_snapshot.txt` preserves the validator output. `records/doubt_occurrences.json` was refreshed for all 48 scans and contains 444 occurrences: 440 `\unsure` and 4 `\illegible`. `records/inventory_macro_review.csv` was refreshed and now identifies state macros nested within `\unsure`, preventing a raw count from being mistaken for an unconditional number of physical elements. `records/inventory_review_snapshot.json` records the report's source hashes and focused findings. All these records are pre-freeze snapshots, not freeze records.

### Actionable reconciliation points

- **Scan 121, inventory 121.16 and 121.17:** both rows have kind `deletion`, position `NB margin`, and the identical identifier `de (overwritten in au nb de 2n)`. The revised NB in the current source has one `\deleted{\unsure{de}}`. The page therefore has 12 deletion macros and 13 deletion inventory rows. Reconcile the duplicate inventory entries with the audited source. The new `distincts` insertion is represented by 121.32; the three insertion macros have three insertion rows.
- **Scan 088, inventory 088.11:** this row still groups the two separate source wrappers for the deleted phrases beginning `Dans le cas qui nous occupe` and `Prenant`. The page has seven deletion macros and six deletion rows. Review the element grouping required by the inventory rule; the content has an identifying row, so the count difference alone establishes no textual omission.
- **Scan 137, inventory 137.24:** the row identifier still writes ordinary arrows from `U` to `G` and from `G` to `G^(0)`, while the revised source models both connectors as `\unsure{\text{—}|\longrightarrow}` labels on phantom connectors. Align the inventory identifier with the current source uncertainty. This is a metadata consistency point, with no proposed change to the reading.

### Focused checks that found no additional gap

- All 50 `\mspage` occurrences now have an exact identifying inventory entry. This includes every previously flagged pagination label on scans 110–115 and 117–123. The complete mapping is in `records/pagination_inventory_review.csv`.
- Scan 094 has two figure macros and two drawing rows, 094.03 and 094.13. The inserted label and accompanying margin element also have inventory entries.
- Scan 110's new upper-left diagram has five rows of four cells. All ten directional arrow targets lie within written cells, including the three-row phantom connector. Its braces, option brackets, quotation marks, and row separators pass the mechanical checks. The page has three diagrams and three diagram rows.
- Scan 117's compatibility-note outline is represented by one figure macro and drawing row 117.12, alongside margin-note row 117.11.
- Scan 132 has 14 lexical deletion macros and 13 deletion rows. Exactly one deletion macro is inside the `\unsure` alternative in `\inserted{\unsure{Enfin|\deleted{Enfin}}}`. Row 132.01 identifies the inserted word; the extra lexical macro count is accounted for by that alternative state and supplies no evidence of another physical element.
- Scan 135 contains eight `\margin{D R}` occurrences and eight inventory stamp rows. Its vertical separator has one figure macro and drawing row 135.31. The remaining margin count difference is explained by the drawing's outer margin wrapper.
- Scan 137's phantom connector labels have balanced option brackets and quotation marks. All five directional arrows in the lower diagram target written cells. The other two diagrams also pass those target-bound checks.
- Across all pages, all 87 arrow commands inspected had closed option brackets and paired label quotation marks. No malformed row separator or unbalanced state wrapper was found.

No page, inventory, doubt-register, combined-transcription, or progress-log content was changed by this worker. No images or context contents were opened. No compilation or installation was attempted. A final rerun remains necessary after the primary reader's notation edits.

## Requested rerun after final notation edits

2026-11-15 17:30:23 UTC. The requested single fresh structural validation of the current 48 files reported **zero errors**, 825 inventory rows, and 29 ellipsis/“etc.” review flags. The combined transcription matched the current page files. The root-generated balanced doubt index was verified against every current source hash and occurrence: **499 total, comprising 495 `\unsure` and 4 `\illegible`**. That index was verified without rewriting it.

The two inventory reconciliations have been completed by the primary reader: scan 088 now has seven deletion macros and seven deletion rows; scan 121 has twelve deletion macros and twelve deletion rows. No exact duplicate inventory entries remain. All 50 manuscript-pagination occurrences retain exact identifying inventory rows. The macro and pagination comparison CSVs and snapshot metadata were refreshed for these source versions.

The scan 110 diagram source is byte-identical to the version whose row targets and option syntax were checked in the preceding pass. The final scan 137 diagram was inspected again after its alphabet change to `\mathscr`: its two phantom uncertainty labels, arrow directions, row separators, and target cells remain structurally complete. Scan 135 still has eight literal `D R` margin arguments and eight corresponding stamp rows. The new drawings on scans 094 and 117 and the vertical separator on 135 retain their identifying drawing rows. The extra deletion count on 132 remains the single cancellation alternative nested in `\unsure`.

One inventory-identifier consistency point remains at the time of this rerun: 137.24 depicts the `U`–`G` and `G`–`G^(0)` connections as ordinary arrows, whereas the source preserves dash/arrow uncertainty. This does not indicate a missing diagram or a TeX syntax defect; the identifier can be made consistent with the source uncertainty without changing the reading.

No pages, inventory, doubt register, combined transcription, or progress log were changed by this worker. No images or context were opened. The current results are ready for the primary reader's freeze procedure; these records do not themselves declare a freeze.
