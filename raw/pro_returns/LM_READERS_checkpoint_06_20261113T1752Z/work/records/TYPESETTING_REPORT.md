# Typesetting and verification report

**Status: PROVISIONAL — NOT A FINISHED RELEASE.**

Edition date: 13 November 2026. This report is assembled from the saved log, link, source and painted-bound measurements and the attributed visual-review records. Each PDF is identified by its SHA-256 below. Page numbers in this report are physical PDF pages, starting at 1; manuscript and scan numbers remain separate.

## 1. Coverage and editorial decisions

The original three archive manifests contain 1,022 files; every length and digest was verified. Both language masters contain all 116 packages and all 1,588 scans in order. All 245 English translation units reconstruct their source packages byte for byte. French unit assembly is exact after the original reader’s newline normalization; 44 packages use CRLF in their raw source. `SOURCE_INTEGRITY.md`, `SOURCE_SCAN_MARKS.tsv` and `SOURCE_UNIT_ASSEMBLY.tsv` give the checks and the supplied historical exceptions.

One common annotated body generates every form of each language. It records 10,888 effective authorial variants: 6,702 deletions and 4,186 insertions. Another 380 nested edits wholly inside cancelled passages remain in their complete outer entries. No new conjectural manuscript reading or slip correction was introduced. The English has one additional recorded glossary correction, “structure with loops” → “loop structure” at 140-2:296. `CHANGES_FR.tsv`, `CHANGES_EN.tsv`, `APPARATUS_COUNTS.md` and `MASTER_INTEGRITY.md` document the exact projections.

Every original doubtful and illegible mark remains. The reading forms retain uncertainty from cancelled passages in scan-end fragments, with a dagger at the originating line. Short notes are measured against the three-line margin rule; longer notes form labelled, ruled, breakable blocks. All 237 archive-footer occurrences are listed in `ARCHIVE_FOOTERS.tsv`: the institutional line is omitted, and each independently transcribed manuscript-page number is retained.

The supplied translation has documented mathematical comparison exceptions; this edition does not misdescribe it as literally byte-identical mathematical source. The independent formula audit accounts for the nine historical changed/missing cases, raised abbreviation endings, translated diagram prose and the written-out m-bar shorthand. No unexplained additional mathematical difference was found. The glossary report inventories all 117 entries. Of these, 94 have multiple paragraph-aligned candidate spellings or forms, including inflection; these matches are not all translation inconsistencies.

## 2. Before and after: compilation and painted bounds

“Before” means the actual baseline of the newly assembled form, before its source-local width repairs. It already includes the common annotated-edition infrastructure and mechanical compile repairs. It is not the original draft. The separate supplied English draft had 382 overfull boxes, maximum 331.94247 pt; all 382 records and all 93 previous fit-pass records were mapped back to scans and covered by the final selection. Sanitized complete baseline and final logs are in `work/records/logs/`.

| PDF stem | Stage | Pages | Overfull boxes | Above 2 pt | Widest pt | Errors | Missing glyphs | Outside sheet | Outside permitted area |
|---|---|---|---|---|---|---|---|---|---|
| LM_FR_diplomatique | before | 856 | 29 | 28 | 344.62918 | 0 | 0 | 8 | 9 |
| LM_FR_diplomatique | after | 865 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| LM_FR_corrige_apparat | before | 1523 | 23 | 22 | 344.62918 | 0 | 0 | 8 | 9 |
| LM_FR_corrige_apparat | after | 1533 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| LM_FR_texte_de_lecture | before | 945 | 23 | 21 | 344.62918 | 0 | 0 | 7 | 8 |
| LM_FR_texte_de_lecture | after | 949 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| LM_EN_corrected_apparatus | before | 1531 | 26 | 25 | 331.55484 | 0 | 0 | 7 | 8 |
| LM_EN_corrected_apparatus | after | 1540 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| LM_EN_reading | before | 954 | 26 | 25 | 331.55484 | 0 | 0 | 8 | 9 |
| LM_EN_reading | after | 956 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| LM_FR_master_annotated | before | 1523 | 23 | 22 | 344.62918 | 0 | 0 | 8 | 9 |
| LM_FR_master_annotated | after | 1533 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| LM_EN_master_annotated | before | 1531 | 26 | 25 | 331.55484 | 0 | 0 | 7 | 8 |
| LM_EN_master_annotated | after | 1540 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

The painted-bound check runs on every page using MuPDF’s native bounding-box device, including text, strokes, fills and images. It uses the supplied geometry: 25 mm margins, a 20 mm right note column with 10 pt separation, 12 pt head allowance, and the ordinary footer allowance. The supplied tolerances are retained: 1.5 pt at permitted-area edges and 0.5 pt at sheet edges. Landscape pages are measured in their underlying unrotated sheet coordinates. These tolerances are disclosed, not increased to hide failures. See `VERIFICATION_METHOD.md` for the algorithm and calibration.

No blanket scaling callback is used, and `hfuzz` and `vfuzz` remain zero. Source repairs are recorded individually: changed row/column gaps, label offsets and arrow routes, mathematical line breaks, and three landscape diagrams per book. Explicit local diagram sizes are 8.2, 8.5, 9 and 10 pt against the original 11 pt; the smallest is about 74.5%. One physical sketch per language uses a recorded factor of 0.90. The source-size audit checks that every added size or scaling factor meets the 70% floor. The bold Gamma glyph repair preserves the requested notation through a working Unicode math glyph.

### Pages with boundary violations, before and after

**LM_FR_diplomatique.pdf**

Before: beyond sheet — 9, 154, 172, 311, 327, 453, 617, 852; outside permitted area — 9, 18, 154, 172, 311, 327, 453, 617, 852.

After: beyond sheet — none; outside permitted area — none. Accepted single-letter exceptions: 0.

**LM_FR_corrige_apparat.pdf**

Before: beyond sheet — 10, 11, 289, 328, 594, 838, 1104, 1516; outside permitted area — 10, 11, 23, 289, 328, 594, 838, 1104, 1516.

After: beyond sheet — none; outside permitted area — none. Accepted single-letter exceptions: 0.

**LM_FR_texte_de_lecture.pdf**

Before: beyond sheet — 9, 167, 187, 343, 501, 676, 940; outside permitted area — 9, 18, 167, 187, 343, 501, 676, 940.

After: beyond sheet — none; outside permitted area — none. Accepted single-letter exceptions: 0.

**LM_EN_corrected_apparatus.pdf**

Before: beyond sheet — 11, 292, 331, 599, 843, 1111, 1524; outside permitted area — 11, 23, 292, 331, 599, 843, 1111, 1524.

After: beyond sheet — none; outside permitted area — none. Accepted single-letter exceptions: 0.

**LM_EN_reading.pdf**

Before: beyond sheet — 9, 168, 189, 346, 347, 505, 682, 949; outside permitted area — 9, 18, 168, 189, 346, 347, 505, 682, 949.

After: beyond sheet — none; outside permitted area — none. Accepted single-letter exceptions: 0.

**LM_FR_master_annotated.pdf**

Before: beyond sheet — 10, 11, 289, 328, 594, 838, 1104, 1516; outside permitted area — 10, 11, 23, 289, 328, 594, 838, 1104, 1516.

After: beyond sheet — none; outside permitted area — none. Accepted single-letter exceptions: 0.

**LM_EN_master_annotated.pdf**

Before: beyond sheet — 11, 292, 331, 599, 843, 1111, 1524; outside permitted area — 11, 23, 292, 331, 599, 843, 1111, 1524.

After: beyond sheet — none; outside permitted area — none. Accepted single-letter exceptions: 0.

## 3. Links and source marks

Original source counts are 1,588 scan marks, 17,117 doubtful marks and 1,261 illegible marks in each language. Literal marks in alternate master branches, executed source IDs, macro expansions and painted PDF annotation rectangles are distinct quantities. A wrapped mark may produce several rectangles; nested marks may share one. The audit independently reconstructs each marked occurrence’s target and physical-page set from PDF annotations, then compares them with the LuaLaTeX trace and the selected master branch.

| PDF stem | Archive annotations | All external URI annotations | Distinct scans | Executed source IDs | Macro expansions | Unlinked marked IDs |
|---|---|---|---|---|---|---|
| LM_FR_diplomatique | 20113 | 20114 | 1588 | 19966 | 20734 | 0 |
| LM_FR_corrige_apparat | 21449 | 21450 | 1588 | 21374 | 22077 | 0 |
| LM_FR_texte_de_lecture | 25087 | 25088 | 1588 | 25045 | 25685 | 0 |
| LM_EN_corrected_apparatus | 21484 | 21485 | 1588 | 21374 | 22077 | 0 |
| LM_EN_reading | 25137 | 25138 | 1588 | 25045 | 25685 | 0 |
| LM_FR_master_annotated | 21449 | 21450 | 1588 | 21374 | 22077 | 0 |
| LM_EN_master_annotated | 21484 | 21485 | 1588 | 21374 | 22077 | 0 |

### Per-cote target coverage

| PDF stem | Cote | Expected scans | Distinct linked scans | Annotation rectangles | Missing / unexpected scans |
|---|---|---|---|---|---|
| LM_FR_diplomatique | 140-1 | 37 | 37 | 590 | [] / [] |
| LM_FR_diplomatique | 140-2 | 575 | 575 | 7046 | [] / [] |
| LM_FR_diplomatique | 140-3 | 696 | 696 | 9187 | [] / [] |
| LM_FR_diplomatique | 140-4 | 280 | 280 | 3290 | [] / [] |
| LM_FR_corrige_apparat | 140-1 | 37 | 37 | 610 | [] / [] |
| LM_FR_corrige_apparat | 140-2 | 575 | 575 | 7632 | [] / [] |
| LM_FR_corrige_apparat | 140-3 | 696 | 696 | 9751 | [] / [] |
| LM_FR_corrige_apparat | 140-4 | 280 | 280 | 3456 | [] / [] |
| LM_FR_texte_de_lecture | 140-1 | 37 | 37 | 721 | [] / [] |
| LM_FR_texte_de_lecture | 140-2 | 575 | 575 | 8702 | [] / [] |
| LM_FR_texte_de_lecture | 140-3 | 696 | 696 | 11506 | [] / [] |
| LM_FR_texte_de_lecture | 140-4 | 280 | 280 | 4158 | [] / [] |
| LM_EN_corrected_apparatus | 140-1 | 37 | 37 | 610 | [] / [] |
| LM_EN_corrected_apparatus | 140-2 | 575 | 575 | 7664 | [] / [] |
| LM_EN_corrected_apparatus | 140-3 | 696 | 696 | 9755 | [] / [] |
| LM_EN_corrected_apparatus | 140-4 | 280 | 280 | 3455 | [] / [] |
| LM_EN_reading | 140-1 | 37 | 37 | 721 | [] / [] |
| LM_EN_reading | 140-2 | 575 | 575 | 8733 | [] / [] |
| LM_EN_reading | 140-3 | 696 | 696 | 11523 | [] / [] |
| LM_EN_reading | 140-4 | 280 | 280 | 4160 | [] / [] |
| LM_FR_master_annotated | 140-1 | 37 | 37 | 610 | [] / [] |
| LM_FR_master_annotated | 140-2 | 575 | 575 | 7632 | [] / [] |
| LM_FR_master_annotated | 140-3 | 696 | 696 | 9751 | [] / [] |
| LM_FR_master_annotated | 140-4 | 280 | 280 | 3456 | [] / [] |
| LM_EN_master_annotated | 140-1 | 37 | 37 | 610 | [] / [] |
| LM_EN_master_annotated | 140-2 | 575 | 575 | 7664 | [] / [] |
| LM_EN_master_annotated | 140-3 | 696 | 696 | 9755 | [] / [] |
| LM_EN_master_annotated | 140-4 | 280 | 280 | 3455 | [] / [] |

### Per-kind executed marks and links

| PDF stem | Kind | Executed IDs | Linked IDs | Unlinked IDs | Run / page mismatches |
|---|---|---|---|---|---|
| LM_FR_diplomatique | scan | 1588 | 1588 | 0 | 0 / 0 |
| LM_FR_diplomatique | unsure | 17117 | 17117 | 0 | 0 / 0 |
| LM_FR_diplomatique | illegible | 1261 | 1261 | 0 | 0 / 0 |
| LM_FR_corrige_apparat | scan | 1588 | 1588 | 0 | 0 / 0 |
| LM_FR_corrige_apparat | unsure | 18231 | 18231 | 0 | 0 / 0 |
| LM_FR_corrige_apparat | cancelled-anchor | 110 | 110 | 0 | 0 / 0 |
| LM_FR_corrige_apparat | residual-unsure | 127 | 127 | 0 | 0 / 0 |
| LM_FR_corrige_apparat | illegible | 1318 | 1318 | 0 | 0 / 0 |
| LM_FR_texte_de_lecture | scan | 1588 | 1588 | 0 | 0 / 0 |
| LM_FR_texte_de_lecture | cancelled-anchor | 4969 | 4969 | 0 | 0 / 0 |
| LM_FR_texte_de_lecture | unsure | 17117 | 17117 | 0 | 0 / 0 |
| LM_FR_texte_de_lecture | residual-unsure | 110 | 110 | 0 | 0 / 0 |
| LM_FR_texte_de_lecture | illegible | 1261 | 1261 | 0 | 0 / 0 |
| LM_EN_corrected_apparatus | scan | 1588 | 1588 | 0 | 0 / 0 |
| LM_EN_corrected_apparatus | unsure | 18231 | 18231 | 0 | 0 / 0 |
| LM_EN_corrected_apparatus | cancelled-anchor | 110 | 110 | 0 | 0 / 0 |
| LM_EN_corrected_apparatus | residual-unsure | 127 | 127 | 0 | 0 / 0 |
| LM_EN_corrected_apparatus | illegible | 1318 | 1318 | 0 | 0 / 0 |
| LM_EN_reading | scan | 1588 | 1588 | 0 | 0 / 0 |
| LM_EN_reading | cancelled-anchor | 4969 | 4969 | 0 | 0 / 0 |
| LM_EN_reading | unsure | 17117 | 17117 | 0 | 0 / 0 |
| LM_EN_reading | residual-unsure | 110 | 110 | 0 | 0 / 0 |
| LM_EN_reading | illegible | 1261 | 1261 | 0 | 0 / 0 |
| LM_FR_master_annotated | scan | 1588 | 1588 | 0 | 0 / 0 |
| LM_FR_master_annotated | unsure | 18231 | 18231 | 0 | 0 / 0 |
| LM_FR_master_annotated | cancelled-anchor | 110 | 110 | 0 | 0 / 0 |
| LM_FR_master_annotated | residual-unsure | 127 | 127 | 0 | 0 / 0 |
| LM_FR_master_annotated | illegible | 1318 | 1318 | 0 | 0 / 0 |
| LM_EN_master_annotated | scan | 1588 | 1588 | 0 | 0 / 0 |
| LM_EN_master_annotated | unsure | 18231 | 18231 | 0 | 0 / 0 |
| LM_EN_master_annotated | cancelled-anchor | 110 | 110 | 0 | 0 / 0 |
| LM_EN_master_annotated | residual-unsure | 127 | 127 | 0 | 0 / 0 |
| LM_EN_master_annotated | illegible | 1318 | 1318 | 0 | 0 / 0 |

The reading forms have 4,969 cancellation-anchor marks and 110 explicit inherited-uncertainty marks in addition to the original primary marks. They keep the doubts in omitted passages visible and linked. In all forms, the source-ID audit tests the exact branch selected, rather than assuming that all literal master branches execute.

## 4. Warnings and font decisions

The complete warning messages, including continuation lines, are in `LATEX_WARNINGS.tsv`. The complete sanitized logs retain the surrounding diagnostics. Underfull boxes are reported separately from overfull boxes. Margin-placement warnings indicate LaTeX adjusted a margin box vertically; they do not establish that text was lost. The all-page ink audit and the additional margin-line collision audit check the resulting layout.

| PDF stem | Warnings | Margin-placement warnings | Other warnings | Underfull boxes | Undefined references / citations |
|---|---|---|---|---|---|
| LM_FR_diplomatique | 40 | 35 | 5 | 22 | 0 |
| LM_FR_corrige_apparat | 50 | 45 | 5 | 22 | 0 |
| LM_FR_texte_de_lecture | 910 | 905 | 5 | 23 | 0 |
| LM_EN_corrected_apparatus | 48 | 43 | 5 | 20 | 0 |
| LM_EN_reading | 904 | 899 | 5 | 23 | 0 |
| LM_FR_master_annotated | 50 | 45 | 5 | 22 | 0 |
| LM_EN_master_annotated | 48 | 43 | 5 | 20 | 0 |

The ordinary remaining package warnings concern unicode-math’s compatibility definitions, disabled shell escape for an unused EPS converter, and the legacy OMS font shape used by `textcircled`. The actual circled glyph is present and was visually checked. `FONT_REPAIRS.tsv` and `audit_fonts.py` document the separate bold-Gamma correction. Missing-character counts are measured independently; a font substitution is not presented as a missing-glyph diagnostic.

## 5. Visual inspection and local collision repairs

Required pages include every historic overflow site and previous scaling/rotation site mapped by scan, every landscape page, all current nontrivial layout repairs, and forty evenly spread physical pages per book. Selection extends through a scan’s continuation and the next scan boundary. Selected pages were rendered and inspected; dense diagrams and ambiguous labels were also enlarged. The individual observations below retain the actual reviewer and basis.

Review status is tied to the PDF hash, PNG-file hash and decoded RGB-pixel hash. On rebuild, a review carries forward only when both image hashes are identical. A master may inherit an apparatus-reader observation only after a fresh all-page pixel comparison and equality of its actual selected-page PNG; its different title page is inspected separately. Rendering by itself never creates a completed review.

| PDF stem | Required pages | Rendered | Reviewed | Close-check inventory | Landscape pages |
|---|---|---|---|---|---|
| LM_FR_diplomatique | 477 | 477 | 102 | 395 | 155, 174, 622 |
| LM_FR_corrige_apparat | 676 | 676 | 3 | 550 | 293, 332, 1112 |
| LM_FR_texte_de_lecture | 494 | 494 | 14 | 404 | 168, 189, 680 |
| LM_EN_corrected_apparatus | 684 | 684 | 25 | 554 | 294, 334, 1118 |
| LM_EN_reading | 499 | 499 | 15 | 409 | 170, 191, 684 |
| LM_FR_master_annotated | 676 | 676 | 1 | 550 | 293, 332, 1112 |
| LM_EN_master_annotated | 684 | 684 | 1 | 554 | 294, 334, 1118 |

### Equation numbers and page breaks

A separate page-break audit examined106 nonmaster candidates in the preceding complete build. Actual native page-pair inspection confirmed80 detached equation-number instances and cleared26 candidates whose formulas were already on the same page. The repairs are exact paired source bindings: local page-break penalties keep each unchanged number with its complete diagram. No equation text or geometry is changed by those pagination bindings. `PAGINATION_REVIEW_BEFORE.tsv`, the source-binding inventory and the source reconciliation retain the historical observations and their source locations.

The final audit reruns the candidate scan over every page of all seven PDFs, requires an actual final-image observation for every known defect and every new primary candidate, and uses current all-page pixel comparisons for the two apparatus/master duplicates. Its records bind source fragments, PDF hashes and viewed-image hashes. `pagination_verification_final.json` records the final status; rendering alone does not resolve an item.


The long-note renderer also keeps its heading with the first paragraph or diagram while allowing later paragraphs to break normally. Five previously detached diplomatic-note headings are checked on their actual final pages. Section V and its preliminary-data opening at140-3:548 are separately checked in all five primary readers. `heading_closure_final.json` retains the10 source-qualified, image-bound observations.

### Additional native-image findings

`work/data/final_visual_issue_closure.json` retains each observed defect, its original image evidence, the exact repair identifiers and separate confirmations against every affected final book. The following counts distinguish an accepted isolated probe from closure on the actual publication PDF.

| Finding | Source site | Status | Affected books | Final-book confirmations |
|---|---|---|---|---|
| VIS-140-3-441-117 | 140-3:441 | OPEN | 7 | 0 |
| VIS-140-3-449-137-138 | 140-3:449 | OPEN | 7 | 0 |
| VIS-140-2-252-OPTIONS | 140-2:252 | OPEN | 7 | 0 |
| VIS-140-3-443-121 | 140-3:443 | OPEN | 7 | 0 |
| VIS-140-3-520-81 | 140-3:520 | OPEN | 7 | 0 |
| VIS-140-3-637-BLUE-NOTE | 140-3:637 | OPEN | 7 | 0 |
| VIS-140-2-089-SECTION12 | 140-2:89 | OPEN | 7 | 0 |
| VIS-140-3-186-SECTIONII | 140-3:186 | OPEN | 7 | 0 |
| VIS-140-3-506-20bis | 140-3:506 | OPEN | 7 | 0 |
| VIS-140-3-055-3 | 140-3:55 | OPEN | 7 | 0 |
| VIS-140-3-622-HEADING-b | 140-3:622 | OPEN | 7 | 0 |
| VIS-140-3-221-REMARQUE | 140-3:221 | OPEN | 7 | 0 |
| VIS-140-1-025-HEADING-B | 140-1:25 | OPEN | 7 | 0 |
| VIS-GENERATED-RETAINEDDOUBT-HEADING | 140-2:36 | OPEN | 2 | 0 |
| VIS-GENERATED-APPARATUS-HEADING | 140-3:638 | OPEN | 4 | 0 |
| VIS-140-3-408-44 | 140-3:408 | OPEN | 7 | 0 |
| VIS-140-3-649-59 | 140-3:649 | OPEN | 7 | 0 |
| VIS-140-3-656-REMARKS | 140-3:656 | OPEN | 7 | 0 |
| VIS-140-3-590-60 | 140-3:590 | OPEN | 7 | 0 |
| VIS-140-4-115-RANGEHEADING | 140-4:115 | OPEN | 5 | 0 |
| VIS-140-4-267-RANGEHEADING | 140-4:267 | OPEN | 5 | 0 |
| VIS-140-3-565-HEADING-6 | 140-3:565 | OPEN | 7 | 0 |
| VIS-140-3-419-CIRCLED3 | 140-3:419 | OPEN | 7 | 0 |
| VIS-140-3-245-CANCELLEDTAG | 140-3:245 | OPEN | 6 | 0 |
| VIS-140-3-261-CANCELLEDTAG | 140-3:261 | OPEN | 6 | 0 |
| VIS-140-3-363-CANCELLEDTAG | 140-3:363 | OPEN | 6 | 0 |
| VIS-140-3-6-SECTION38 | 140-3:6 | OPEN | 7 | 0 |
| VIS-140-3-575-PROPOSITION | 140-3:575 | OPEN | 7 | 0 |
| VIS-140-4-77-HEADING-7 | 140-4:77 | OPEN | 7 | 0 |
| VIS-140-4-065-EPILABELS | 140-4:65 | OPEN | 7 | 0 |
| VIS-140-3-653-HEADING-2 | 140-3:653 | OPEN | 7 | 0 |
| VIS-140-4-32-THEOREM | 140-4:32 | OPEN | 7 | 0 |
| VIS-140-3-437-TAG108-INTRO | 140-3:437 | OPEN | 7 | 0 |
| VIS-140-4-75-E144-MASK | 140-4:75 | OPEN | 7 | 0 |
| VIS-140-3-519-TAG79-INTRO | 140-3:519 | OPEN | 7 | 0 |
| VIS-140-3-495-SECTION49 | 140-3:495 | OPEN | 7 | 0 |

The common apparatus, retained-uncertainty, package-range and conditional marginal-note heading guards are formatting repairs. `work/data/generated_heading_repairs.json` and the corresponding occurrence rows in `TYPESETTING_FIXES.tsv` identify the generator implementation, original source place and applicable book. They do not add manuscript variants or apparatus entries. The conditional marginal-note rows record where the block renderer can apply; they do not assert that every note prints as a block in every form.

| Generated formatting repair | Recorded source/book occurrences |
|---|---|
| apparatus heading guard | 6152 |
| conditional marginal-note heading guard | 12096 |
| retained heading guard | 2820 |
| scan-range heading guard | 580 |

The separate all-page generated-heading audit searches every publication page for a detached apparatus or retained-doubt heading, a detached separator rule, and a package-range heading without following source content. It closes the actually observed earlier witnesses and accounts for every current candidate. Its source, PDF, image and master-comparison hashes are recorded in `work/data/generated_heading_audit_final.json`.

| Generated-heading closure check | Count |
|---|---|
| Publication PDFs audited | 7 |
| Known witnesses resolved | 0 / 48 |
| Current primary candidates cleared | 0 / 3 |
| Current master candidates covered by identical render | 0 / 2 |
| Unresolved findings | 1 |

`VISUAL_REPAIRS.tsv` records the confirmed label, edge and marginal-note collisions, their paired source repairs and the isolated proofs. These include defects wholly inside the permitted area, which a bounding-box test alone cannot find. `LAYOUT_REPAIR_DETAILS.tsv`, `TYPESETTING_FIXES.tsv` and the exact replacement manifests retain source positions and before/after text. The complete per-page review records are in `work/verification/<PDF stem>/VISUAL_REVIEW.tsv`; the following is their readable transcription.

### LM_FR_diplomatique.pdf

PDF SHA-256: `d6259d202365b2c36ee512477c9207e35a95df017a9e8d74df2638806fe17e07`.

| Physical page | Status | Selection reason | Reviewer and inspection basis | Observation |
|---|---|---|---|---|
| 1 | reviewed | evenly spaced sample | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: title, author, edition label, archive credit and date are centered with clear spacing and generous margins. |
| 6 | reviewed | layout_before_sites.json:1 140-1:4 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: successive formula rows, boxed relations and the ruled marginal-note block fit; short right-margin annotations remain separated from the body. |
| 7 | reviewed | layout_before_sites.json:1 140-1:4 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: long algebraic derivations remain inside the text block; short blue right-margin notes stay in their own column. |
| 8 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:5 140-1:10 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the upper branching diagram and lower exact-sequence diagrams fit with visible gaps between groups; the intervening marginal-note block is clear.; Native 2.5×: the branching groups and central extensions are readable; double arrows remain distinct and all indices and braced products fit.; Final native 2.5× full-page review: branching central extensions, braces and all uncertain group indices are legible; lower exact sequences remain within the page. |
| 9 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:5 140-1:10 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the repaired scan10 diagram now separates the subgroup annotation from the curved arrows; subsequent displays fit below it. This page is queued for enlarged diagram inspection.; Close inspection at900px/page: the repaired subgroup annotation and D3/D-prime3 labels are clear of the routed arrows. The second diagram's rho/sigma arrow labels are legible, and the succeeding large braces and modular assignments fit.; Native 2.5×: the first large scan-10 routing leaves the raised subgroup annotation clear of its paths; curved maps retain clear endpoints and Cartesian annotations.; Final native 2.5× full-page review: the raised subgroup annotation and rerouted first large diagram have clear object/label gaps; crossing paths do not strike the Cartesian text. |
| 10 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:3 140-1:12; layout_repairs_applied.json:5 140-1:10 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the projection label is clear of the crossing diagonal; both branching and exact-sequence diagrams are complete, with note m15 separated.; Native 2.5×: the second large scan-10 projection label is to the right of the crossing diagonal with visible white clearance; the adjacent extension formulas fit.; Current native 2.5× page inspection: the projection pr_1 is shifted along its horizontal arrow and the diagonal to E no longer crosses it; all group objects and the lower exact-sequence diagram remain legible. |
| 11 | reviewed | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:3 140-1:12 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: tall fractions and braces fit without crossing adjacent rows; the small marginal-note block and following scan markers remain clear.; Close inspection at900px/page: nested fractions, underbraces and the tall handwritten bracket remain distinct; note m16 does not collide with the following scan markers or equations. |
| 12 | reviewed | layout_before_sites.json:8 140-1:15 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the long sequence of centered fraction identities is evenly spaced and within the text width; the next scan begins without a collision.; Close inspection at900px/page: successive fraction identities and parity conditions have separate baselines; the small cancelled display beginning scan15 is intact above the footer. |
| 13 | reviewed | layout_before_sites.json:8 140-1:15 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: grey cancelled formulas remain visible, the inserted marginal-note block fits, and the transcribed printed ARTICLE5/ARTICLE6 text at the foot stays inside the type block.; Close inspection at900px/page: the cancelled formulas retain distinct superscripts and underbraces, the modular-value rows in note m19 are separated, and the printed article text ends above the footer. |
| 14 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:8 140-1:15; layout_before_sites.json:9 140-1:16 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the small commutative diagrams, ruled marginal notes and central geometric sketch are separated; the short right-margin verification note fits.; Close inspection at900px/page: arrows stop outside their labels in both commutative diagrams; the geometric sketch, note m23 and the final note m24 remain separated. |
| 15 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:13 140-1:17; layout_before_sites.json:9 140-1:16 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: short ruled notes and the small sketch fit above the grey diagram; neither the lower arrows nor the footer are clipped.; Close inspection at900px/page: all three ruled notes have intact contents; the central sketch and the lower cancelled diagram have clear strokes, labels and spacing. |
| 16 | reviewed | layout_before_sites.json:13 140-1:17; layout_before_sites.json:14 140-1:18; layout_pass_sites.json:31 140-1:18 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the grey cancelled table and its blue alternatives fit; the short right-margin central-element note is clear of the body and footer.; Close inspection at900px/page: the cancelled table and branching diagram remain legible; the central-element note is isolated in the right margin, and the three modular assignments are clear. |
| 17 | reviewed | layout_before_sites.json:14 140-1:18; layout_before_sites.json:15 140-1:19; layout_pass_sites.json:31 140-1:18; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:54 140-1:19; layout_repairs_applied.json:4 140-1:19 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the upper lattice diagram and full-width ruled note are clear; the following scan marker has adequate separation from the prose.; Close inspection at900px/page: the upper three-column lattice has clear vertical arrowheads and labels; the ruled note below retains all blue alternatives without clipping. |
| 18 | reviewed | layout_before_sites.json:15 140-1:19; layout_before_sites.json:16 140-1:20; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:54 140-1:19; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:13 140-1:20; layout_repairs_applied.json:4 140-1:19; layout_repairs_applied.json:8 140-1:20 | assistant/root; Actual full-page review in release578_pending sheets001–002, four pages per sheet at900px each. | The large source sketch, intersecting drawn strokes and colored annotations remain contained. The Scans20–37 heading is followed by its scan marker, circled manuscript number and complete branching diagram; no lower-page clipping is visible. |
| 19 | reviewed | layout_before_sites.json:16 140-1:20; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:13 140-1:20; layout_repairs_applied.json:8 140-1:20 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the top ruled marginal note and the stack of grey cancelled diagrams have distinct vertical separation and no visible clipping.; Close inspection at900px/page: the bundle/tangent annotation and the grey cancelled diagram stack have readable labels and adequate separation from their horizontal strokes.; Current native 2.5× page inspection: the marginal derivation and grey cancelled rectangular and branching diagrams are complete, with legible blue uncertain symbols and no clipped endpoints. |
| 21 | reviewed | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23; layout_repairs_applied.json:14 140-1:25 | assistant/root; Actual full-page review in release578_pending sheets001–002, four pages per sheet at900px each. | The lemma, note m39 and cohomology displays fit cleanly. Colored alternatives and cancellations remain distinct. The scan25 marker closes this page; the B opening is kept together at the following page22. |
| 22 | reviewed | layout_repairs_applied.json:14 140-1:25 | assistant/root; Actual full-page review in release578_pending sheets001–002, four pages per sheet at900px each. | B, the two-invertible opening and its formula now share the page. The following remark, source address heading and stacked diagrams remain readable, including the lower dashed-face drawings; no edge clipping is visible. |
| 23 | reviewed | evenly spaced sample | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the small upper diagram and the broad grey cancelled diagram below it fit; the final horizontal source rule is separated from the diagrams. |
| 24 | reviewed | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the large upper lattice and the two lower exact sequences fit; both ruled notes and the short right-margin annotation remain clear. |
| 25 | reviewed | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the circular sketch and successive formula rows fit; the grey cancelled prose retains its blue alternatives without clipping. |
| 26 | reviewed | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the opening ruled formula note and the lower branching lattice are separated; the lattice is queued for a closer label check. |
| 27 | reviewed | layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the vertical exact sequence and long horizontal rows fit; the note with the circuit/tree annotation remains inside its ruled block. |
| 28 | reviewed | layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the outlined source annotation and lower triangle/exact sequences fit, with no visible clipping at either side. |
| 31 | reviewed | layout_before_sites.json:23 140-1:36; layout_before_sites.json:24 140-1:36; layout_pass_sites.json:34 140-1:36; layout_pass_sites.json:56 140-1:36; layout_repairs_applied.json:9 140-1:36 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the dense lower commutative diagram fits above the final ruled note; close inspection is needed for its small arrow labels. |
| 32 | reviewed | layout_before_sites.json:23 140-1:36; layout_before_sites.json:24 140-1:36; layout_pass_sites.json:34 140-1:36; layout_pass_sites.json:56 140-1:36; layout_repairs_applied.json:9 140-1:36 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the short concluding formula and manuscript-page markers are intact; the large blank remainder is the deliberate end of cote140-1 before the next cote starts. |
| 33 | reviewed | layout_before_sites.json:25 140-2:4 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the transcribed contents list wraps long entries within the body while retaining its right-hand manuscript page references. |
| 34 | reviewed | layout_before_sites.json:25 140-2:4 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the remaining contents entries, scan markers, propositions and ruled marginal notes fit without collisions. |
| 41 | reviewed | layout_before_sites.json:26 140-2:28 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the upper field diagram and subsequent formulas fit; small right-margin notes are separate from the running prose. |
| 42 | reviewed | layout_before_sites.json:26 140-2:28; layout_before_sites.json:27 140-2:29 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: grey cancelled text, inserted ruled notes and the lower diamond diagram all remain within the block and clearly separated. |
| 45 | reviewed | evenly spaced sample; layout_before_sites.json:28 140-2:35 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: paragraph text and the two long ruled notes remain legible and inside the body, including the lower boxed exact sequence. |
| 47 | reviewed | layout_before_sites.json:29 140-2:39 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the top exact-sequence diagram and lower small diagram fit; short margin comments do not collide with the body. |
| 49 | reviewed | layout_before_sites.json:30 140-2:42 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview inspected: the central prism diagram and its explanatory paragraph fit. The prism is additionally queued for enlarged inspection because its labels are dense. |
| 50 | reviewed | layout_before_sites.json:30 140-2:42; layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The wavy source separator, displayed maps and three circled notation marks are contained; the bottom marginal-note block remains above the footer. |
| 51 | reviewed | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44; layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The central diamond and lower two-square diagram are contained and separated from the surrounding prose and note rule; no clipping is visible at overview scale. |
| 52 | reviewed | layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Two distinct note blocks at the top and the composite-arrow display near the bottom fit the page; scan marks and footer remain separate. |
| 62 | reviewed | layout_before_sites.json:35 140-2:69 | assistant/root; Actual full-page review in release578_pending sheets001–002, four pages per sheet at900px each. | The prose, note m171 and boxed lower-right formula fit within the body. Scan markers and manuscript numbers are separate, and blue/red/teal readings remain legible. |
| 66 | reviewed | layout_before_sites.json:36 140-2:80 | assistant/root; Actual full-page review in release578_pending sheets001–002, four pages per sheet at900px each. | Note m184 retains its rule, label and tall narrow sketch together. Section10 begins with its text, and the lower Pi displays remain inside the body without collision. |
| 67 | reviewed | evenly spaced sample; layout_before_sites.json:36 140-2:80 | assistant/root; Actual full-page review in release578_pending sheets001–002, four pages per sheet at900px each. | Scans81–90 begins with substantive prose. Note m187 has its first text on the same page, section11 and its maps remain readable, and marginal source numbers do not collide with the body. |
| 69 | reviewed | layout_before_sites.json:37 140-2:88 | assistant/root; Actual full-page review in release578_pending sheets001–002, four pages per sheet at900px each. | The long cancellation and colored readings remain distinguishable. Note m197 includes its short arrow chain; the m198 origin marker is visible at the foot before its following-page note. No page-edge overflow is visible. |
| 70 | reviewed | layout_before_sites.json:37 140-2:88; layout_repairs_applied.json:15 140-2:89 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The ruled m198 note heading is on the same page as its tall vertical sketch. The following topological-analogy prose and short Pi maps fit cleanly; scan/page markers remain separate. |
| 82 | reviewed | layout_before_sites.json:38 140-2:122 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The upper diamond and its explanatory side text are contained; the lower boxed formula and two small diagrams are separated from adjacent paragraphs. |
| 83 | reviewed | layout_before_sites.json:38 140-2:122 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The upper group triangle, middle arrow chain and lower formula remain inside the text measure; the page footer is unobstructed. |
| 85 | reviewed | layout_before_sites.json:39 140-2:130 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The short arrow chain and displayed cohomology formula are contained; both lower marginal-note rules and their text remain separate. |
| 86 | reviewed | layout_before_sites.json:39 140-2:130 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The upper diamond and bottom two-row diagram are contained; the intervening note block and section heading do not crowd the diagrams. |
| 90 | reviewed | evenly spaced sample; layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | assistant/root; Actual full-page review in release578_pending sheets001–002, four pages per sheet at900px each. | The theorem and extension diagrams fit. Scans141–150 retains its opening prose and formula on this page, and note m262 stays with its text. The following fundamental lemma has an opening line before its normal continuation. |
| 91 | reviewed | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | assistant/root; Actual full-page review in release578_pending sheets003–004, four pages per sheet at900px each. | The fundamental-lemma proof, disc transformations and small formula blocks fit cleanly; colored doubtful and illegible readings remain distinct from gray cancellations. |
| 92 | reviewed | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | assistant/root; Actual full-page review in release578_pending sheets003–004, four pages per sheet at900px each. | The conformal-action discussion and lemma continuation stay within the body; scan and manuscript-page markers are clear, with no crowding at the page edges. |
| 93 | reviewed | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | assistant/root; Actual full-page review in release578_pending sheets003–004, four pages per sheet at900px each. | Notes m263 and m264 retain their labels and first text. The theorem, two-line classifying map and corollary are complete within the body; gray cancelled prose remains visible. |
| 97 | reviewed | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | assistant/root; Actual full-page review in release578_pending sheets003–004, four pages per sheet at900px each. | The exterior-square and quadratic-polynomial displays fit. Note m277 contains its tall narrow sketch under its heading; m278 retains its text and short diagram with readable blue alternatives. |
| 98 | reviewed | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | assistant/root; Actual full-page review in release578_pending sheets003–004, four pages per sheet at900px each. | Section16 retains its opening and short map. The Scans161–170 heading has following prose; notes m280, m281 and m283 and the cancelled lower diagram stay contained. |
| 99 | reviewed | layout_before_sites.json:46 140-2:162 | assistant/root; Actual full-page review in release578_pending sheets003–004, four pages per sheet at900px each. | Three small topos diagrams retain legible endpoints and separated arrow labels. Source alternatives and the surrounding prose remain within the body area. |
| 100 | reviewed | layout_before_sites.json:47 140-2:164; layout_before_sites.json:48 140-2:165; layout_repairs_applied.json:17 140-2:165 | assistant/root; Actual full-page review in release578_pending sheets003–004, four pages per sheet at900px each. | The upper and lower topos diamonds and their curved-arrow annotations fit. Note m284 begins with its complete first paragraph and continues normally; no clipping is visible. |
| 101 | reviewed | layout_before_sites.json:48 140-2:165; layout_before_sites.json:49 140-2:166; layout_repairs_applied.json:17 140-2:165 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: pseudo-commutativity is inside the upper-right triangle, both red illegibility marks clear strokes, and the two live diagrams and note m285 remain distinct.; Native 2.5×: the cancelled diamond has the pseudo-commutativity label inside the upper-right triangle and the lower illegibility marker clear of the central vertical. The live diagrams below remain clear.; Current native 2.5× page inspection: the cancelled pseudo-commutative diagram has both words inside its upper-right triangle, with the lower illegibility label clear of the central vertical and curved path; following live diagrams are clear. |
| 102 | reviewed | layout_before_sites.json:49 140-2:166 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: both square diagrams and two lower triangles are complete; the short triangle-supérieur margin annotation is separate. |
| 112 | reviewed | evenly spaced sample | assistant/root; Actual full-page review in release578_pending sheets003–004, four pages per sheet at900px each. | Notes m307–m309 retain their rule, heading and text. The short right-margin corollary note is separated from the body; long colored and cancelled passages fit without edge overflow. |
| 113 | pending | layout_before_sites.json:50 140-2:197 | ;  |  |
| 115 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205 | ;  |  |
| 116 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205; layout_repairs_applied.json:18 140-2:206 | ;  |  |
| 118 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 119 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 121 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 122 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217; layout_before_sites.json:57 140-2:220 | ;  |  |
| 123 | pending | layout_before_sites.json:57 140-2:220 | ;  |  |
| 124 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 128 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 129 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 134 | pending | evenly spaced sample; layout_repairs_applied.json:19 140-2:252; layout_repairs_applied.json:20 140-2:252; layout_repairs_applied.json:21 140-2:251; layout_repairs_applied.json:22 140-2:252 | ;  |  |
| 135 | pending | layout_repairs_applied.json:19 140-2:252; layout_repairs_applied.json:20 140-2:252; layout_repairs_applied.json:22 140-2:252 | ;  |  |
| 138 | pending | layout_before_sites.json:60 140-2:259 | ;  |  |
| 141 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 142 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 145 | pending | layout_before_sites.json:62 140-2:280 | ;  |  |
| 146 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 147 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 154 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | ;  |  |
| 155 | reviewed | landscape page; layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: landscape chain, lower identifications and curved right endpoint are complete and contained; a native-vector enlargement will confirm small labels.; Native 3× enlargement: the full horizontal homotopy sequence, equality rows, curved final arrow and all uncertain product/pi indices are separated and lie within the landscape page. No additional defect found.; Current native 3× full-landscape inspection: the long homotopy exact sequence is entirely inside the landscape area; lower identifications, blue uncertain symbols and the right curved arrow are legible and separate. |
| 156 | reviewed | evenly spaced sample; layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the long braced exact sequences, boxed extension and final vertical equality fit with no visible clipping.; Current native 2.5× page inspection: continuation after the landscape has complete brace systems, boxed exact sequence and final vertical equality, all within the portrait text area. |
| 158 | reviewed | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the two short exact sequences, note m430 and stabilizer formulas are complete; the right faithfulness comment stays separate. |
| 159 | reviewed | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: note m431, the scans311–320 heading and dense centralizer discussion fit; the short closure note is clear in the right margin. |
| 163 | reviewed | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:26 140-2:321 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: sequence diagram10 and the vertical map in note m438 have distinct endpoints; display11 and lower prose fit. |
| 166 | reviewed | layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_before_sites.json:71 140-2:329; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:25 140-2:328 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: diagrams21–22 and24 are complete, including the lower identifications; note m441 and cancelled equation fragments remain legible. |
| 167 | reviewed | layout_before_sites.json:71 140-2:329; layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:27 140-2:331; layout_repairs_applied.json:28 140-2:331 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: diagram25 and its lower identifications fit; the scans331–340 heading is separated from its opening text.; Current native 2.5× page inspection: top extension displays (25)/(26) retain their labels and uncertain homomorphisms; the following prose and scan331 introduction fit the page. |
| 168 | reviewed | layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:27 140-2:331; layout_repairs_applied.json:28 140-2:331 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: diagram26 has one note heading/rule in its right prose cell; the arrow endpoint, note m442 text and surrounding group objects remain separate.; Native 2.5×: the 105pt prose cell has one marginal-note heading/rule and one endpoint reference; the retained note text stays inside the diagram cell without overlap.; Current native 2.5× page inspection: note m442 in the diagram cell has exactly one rule and heading, one anchor at the arrow endpoint and complete text; surrounding Galois objects and equations27/28 are clear. |
| 173 | reviewed | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the prose and cancelled formulas remain complete, and the explicit landscape-continuation notice140-2-344-D1 is visible after scan344.; Current native 2.5× page inspection: scan344 starts with its manuscript page reference and explicit landscape-continuation notice; preceding quotient formulas remain complete. |
| 174 | reviewed | landscape page; layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the full branching landscape diagram is contained, with distinct left discretification boxes and right object lists; native-vector enlargement follows.; Native 3× enlargement: every branching discreficiation/préarithmétisation object, multiline isomorphism list and {±1}/group arrow label is clear; the full landscape chain fits its page. No additional defect found.; Current native 3× full-landscape inspection: the predicretification hierarchy, bracketed groups, multiline Isom objects and every long connecting arrow fit the page; arrow labels and node text remain separate. |
| 175 | reviewed | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: both pas séparé notes have distinct baselines; three graphical note blocks and the lower quotient formula remain complete.; Native 2.5×: the two doubtful pas séparé notes occupy distinct baselines, and the surrounding marginal sketches remain readable.; Current native 2.5× page inspection: the two pas séparé notes appear on distinct lines in the right margin; three following marginal sketches retain their separate headings and complete paths. |
| 176 | reviewed | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the subgroup list, lemma, note m456 and lower prediscretification maps fit with clear group-object accents. |
| 177 | reviewed | layout_before_sites.json:75 140-2:348; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:29 140-2:348 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: graphical note m457, note m458 and the three-row exact-sequence diagram remain complete; the red illegibility label clears the vertical path. |
| 178 | reviewed | evenly spaced sample; layout_before_sites.json:75 140-2:348; layout_before_sites.json:76 140-2:349; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:29 140-2:348 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the moved formula has its original-position marker140-2-348-M1 and two clear display lines; note m459 and the lower cancelled paragraph remain separated. |
| 179 | reviewed | layout_before_sites.json:77 140-2:352 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the Hurwitz sum and formulas1–3 fit; the cohomology comparison and note m460 remain separated. |
| 180 | reviewed | layout_before_sites.json:77 140-2:352 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: note m461, long profinite-group formulas and the cancelled passage are complete; the source-stroke description is contained at the bottom. |
| 183 | reviewed | layout_before_sites.json:78 140-2:362 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: diagram8 has distinct vertical maps and its question mark remains between them; the scans361–370 heading and dense proof fit. |
| 184 | reviewed | layout_before_sites.json:78 140-2:362 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: formula9, the union of index sets and both lower torsor triangles are complete, with separate edge labels and a clear footer. |
| 187 | reviewed | layout_before_sites.json:79 140-2:371 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the scans371–380 heading, subgroup inclusions9–12 and final surjection13 fit; note m464 has a clear rule. |
| 188 | reviewed | layout_before_sites.json:79 140-2:371 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: formulas14–23, the circled object and right marginal definitions are complete; note m470 is separate above the last display. |
| 191 | reviewed | layout_repairs_applied.json:33 140-2:382 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Scans381–382: the two extension sequences, source labels1 and2, circled source markers and coloured alternatives fit; paragraph and diagram spacing is clear. |
| 192 | reviewed | layout_before_sites.json:80 140-2:384; layout_pass_sites.json:40 140-2:384; layout_pass_sites.json:64 140-2:384; layout_repairs_applied.json:33 140-2:382 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the centralizer formula, note m485 and lower map4 fit; the short Galois/question annotation is clear in the margin. |
| 193 | reviewed | layout_before_sites.json:81 140-2:387 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: note m486 and the fixed-point/normalizer discussion remain legible, with formulas5 and the final arrow chain inside the text area. |
| 196 | reviewed | layout_repairs_applied.json:34 140-2:397 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The brace formulas3–4, diagram5 and map6 remain readable. Ruled notes m489/m491/m492 and the short right-margin notes are separated, with no edge clipping. |
| 197 | reviewed | layout_repairs_applied.json:34 140-2:397 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The triangle with tag8 and the sequences9–10 stay with their equation labels. Note m494 opens with its text and continues into its sequence; the manuscript question marks are retained. No collision is visible at this scale. |
| 200 | reviewed | evenly spaced sample; layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404; layout_repairs_applied.json:35 140-2:407 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Scans404–407: short displays17–19 and the bracketed source annotation fit; note m500 remains separated by its rule. The bottom scan transition has no stranded note heading. |
| 201 | reviewed | layout_repairs_applied.json:35 140-2:407 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The maps20–24, central square22 and cancelled formula24 are all contained with their tags. Scan408/409 transitions and marginal manuscript numbers are clear. |
| 202 | reviewed | layout_pass_sites.json:41 140-2:411 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the two prose columns around the category arrow are readable; notes m508/m509 and the scans411–420 heading remain distinct. |
| 205 | reviewed | layout_repairs_applied.json:36 140-2:417; layout_repairs_applied.json:38 140-2:417 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: equation26 has its doubtful annotation above the dashed diagonal and commutativity annotation inside the lower-right triangle; neither is crossed. The explanatory source paragraph and formulas27–29 fit.; Native 2.5×: the two-line uncertain commutativity annotation is clear inside the upper triangle; the smaller commutativity annotation remains inside the lower-right triangle clear of diagonal and vertical paths.; Current native 2.5× inspection: tag(26) stays with its diagram; the two-line doubtful commutativity annotation is inside the upper triangle and the small comm. is inside the lower-right triangle, both clear of paths. The explanatory paragraph is complete. |
| 206 | reviewed | layout_before_sites.json:84 140-2:419; layout_before_sites.json:85 140-2:419; layout_pass_sites.json:4 140-2:419; layout_pass_sites.json:42 140-2:419; layout_pass_sites.json:59 140-2:419; layout_pass_sites.json:65 140-2:419; layout_repairs_applied.json:37 140-2:419 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the formerly wide equivalence30 is readable in two prose columns; note m516 and the lower vertical identification fit. |
| 207 | reviewed | layout_before_sites.json:86 140-2:423 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the top crossed square has clear objects and distinct solid/dashed paths; the section heading and note m517 are separated. |
| 208 | reviewed | layout_before_sites.json:86 140-2:423 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: groupoid products and map chains fit; note m518 and the short right commutation comment are legible and contained. |
| 210 | reviewed | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: notes m521/m522 and the scans431–440 heading are distinct; both right conjecture comments remain clear of the body. |
| 215 | reviewed | layout_before_sites.json:89 140-2:443 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: cancelled and live commutative squares are both complete; note m534 and the two versions of equation10 remain distinct. |
| 217 | reviewed | layout_before_sites.json:90 140-2:450 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the blue exact-sequence grid16, boxed boundary formulas and display18 are clear; short right notes do not touch the body. |
| 218 | pending | layout_before_sites.json:90 140-2:450; layout_before_sites.json:91 140-2:452 | ;  |  |
| 219 | reviewed | layout_before_sites.json:91 140-2:452; layout_before_sites.json:92 140-2:454 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the source-drawn top bracket, notes m539–m541, piecewise map27 and lower identities fit without clipping. |
| 220 | reviewed | layout_before_sites.json:92 140-2:454 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: formulas28–36 and the three-line uncertain relation32 fit; note blocks m542/m544 and the right NB are separate. |
| 221 | reviewed | layout_before_sites.json:93 140-2:457 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: involution conditions a–c, the Euler-characteristic derivation38 and the two-case correction39 are contained; both notes have clear rules. |
| 222 | reviewed | layout_before_sites.json:93 140-2:457 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: the coloured case discussion, note m547 and the final underbraced group product remain legible above the footer. |
| 223 | reviewed | evenly spaced sample; layout_before_sites.json:94 140-2:462 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final900px inspection: formulas40–46, note m548, the parity cases45 and the bottom multi-line index statement fit with clear baselines. |
| 224 | reviewed | layout_before_sites.json:94 140-2:462 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final 900px four-up: conjugation formulas, marginal calculation m550, equations47–48 and lower two-case definition are contained and separated; uncertainty and illegibility colours remain readable. |
| 234 | pending | layout_before_sites.json:95 140-2:492 | ;  |  |
| 235 | pending | layout_before_sites.json:95 140-2:492 | ;  |  |
| 237 | pending | layout_before_sites.json:96 140-2:502 | ;  |  |
| 238 | pending | layout_before_sites.json:96 140-2:502 | ;  |  |
| 239 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:39 140-2:508 | ;  |  |
| 240 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:39 140-2:508 | ;  |  |
| 242 | pending | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | ;  |  |
| 245 | pending | evenly spaced sample; layout_before_sites.json:101 140-2:519; layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:41 140-2:520 | ;  |  |
| 246 | pending | layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:41 140-2:520 | ;  |  |
| 248 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:42 140-2:527 | ;  |  |
| 249 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:42 140-2:527 | ;  |  |
| 251 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | ;  |  |
| 252 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533; layout_before_sites.json:107 140-2:536 | ;  |  |
| 253 | pending | layout_before_sites.json:107 140-2:536 | ;  |  |
| 266 | pending | layout_before_sites.json:108 140-2:567 | ;  |  |
| 267 | pending | evenly spaced sample; layout_before_sites.json:108 140-2:567; layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:43 140-2:568; layout_repairs_applied.json:44 140-2:568 | ;  |  |
| 268 | pending | layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:43 140-2:568; layout_repairs_applied.json:44 140-2:568 | ;  |  |
| 272 | reviewed | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final 900px four-up: cote140-3 source contents page, boxed part heading, brace group and note634 remain readable; long entries wrap within the type area. |
| 273 | reviewed | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4; layout_before_sites.json:114 140-3:5 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final 900px four-up: dense source contents continuation and mathematical entry labels are contained; blue alternative numbering and right-hand source page numbers remain distinguishable. |
| 274 | reviewed | layout_before_sites.json:114 140-3:5; layout_repairs_applied.json:45 140-3:6 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final 900px four-up: contents continuation, notes639–640 and start ofsection38 are readable; four group-map displays fit with separate labels and tags. |
| 275 | pending | layout_repairs_applied.json:45 140-3:6 | ;  |  |
| 278 | reviewed | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final 900px four-up: functoriality text and isomorphisms20–21 are contained; note653 begins with substantive mathematical content below its heading, no overlap. |
| 279 | reviewed | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final 900px four-up: rational-map fraction, coordinate explanations and note656 are clear; source cancelled continuation remains distinguishable at page foot. |
| 281 | reviewed | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | typeset; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final 900px four-up: relations22–25, right-margin NB and long ruled calculation660 have clear baselines; lower formula chain fits and no text crosses the rule/footer. |
| 282 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 283 | pending | layout_repairs_applied.json:46 140-3:21 | ;  |  |
| 284 | pending | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | ;  |  |
| 287 | pending | layout_repairs_applied.json:47 140-3:33 | ;  |  |
| 288 | pending | layout_before_sites.json:124 140-3:36; layout_repairs_applied.json:47 140-3:33 | ;  |  |
| 289 | pending | evenly spaced sample; layout_before_sites.json:124 140-3:36 | ;  |  |
| 290 | pending | layout_repairs_applied.json:48 140-3:40 | ;  |  |
| 291 | pending | layout_repairs_applied.json:48 140-3:40; layout_repairs_applied.json:49 140-3:41 | ;  |  |
| 292 | pending | layout_repairs_applied.json:50 140-3:44 | ;  |  |
| 296 | pending | layout_repairs_applied.json:51 140-3:55; layout_repairs_applied.json:52 140-3:56 | ;  |  |
| 297 | pending | layout_before_sites.json:125 140-3:58; layout_repairs_applied.json:52 140-3:56 | ;  |  |
| 298 | pending | layout_before_sites.json:125 140-3:58; layout_before_sites.json:126 140-3:59 | ;  |  |
| 299 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 300 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 303 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 306 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 307 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 308 | pending | layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75 | ;  |  |
| 309 | pending | layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75; layout_before_sites.json:133 140-3:76 | ;  |  |
| 311 | pending | evenly spaced sample | ;  |  |
| 314 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:53 140-3:85; layout_repairs_applied.json:54 140-3:85; layout_repairs_applied.json:55 140-3:85; layout_repairs_applied.json:56 140-3:85; layout_repairs_applied.json:57 140-3:85; layout_repairs_applied.json:58 140-3:85; layout_repairs_applied.json:59 140-3:85 | ;  |  |
| 315 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_before_sites.json:136 140-3:86; layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:53 140-3:85; layout_repairs_applied.json:54 140-3:85; layout_repairs_applied.json:55 140-3:85; layout_repairs_applied.json:56 140-3:85; layout_repairs_applied.json:57 140-3:85; layout_repairs_applied.json:58 140-3:85; layout_repairs_applied.json:59 140-3:85 | ;  |  |
| 316 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:60 140-3:88 | ;  |  |
| 317 | pending | layout_before_sites.json:139 140-3:90; layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:60 140-3:88 | ;  |  |
| 318 | pending | layout_before_sites.json:139 140-3:90; layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91 | ;  |  |
| 319 | pending | layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91; layout_before_sites.json:145 140-3:92 | ;  |  |
| 320 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 322 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 323 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95; layout_repairs_applied.json:61 140-3:97; layout_repairs_applied.json:67 140-3:97 | ;  |  |
| 324 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98; layout_repairs_applied.json:61 140-3:97; layout_repairs_applied.json:67 140-3:97 | ;  |  |
| 325 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98 | ;  |  |
| 329 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 330 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 331 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 333 | pending | evenly spaced sample; layout_before_sites.json:153 140-3:111 | ;  |  |
| 334 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 338 | pending | layout_repairs_applied.json:68 140-3:121 | ;  |  |
| 339 | pending | layout_repairs_applied.json:68 140-3:121 | ;  |  |
| 353 | pending | layout_before_sites.json:154 140-3:148 | ;  |  |
| 354 | pending | layout_before_sites.json:154 140-3:148 | ;  |  |
| 355 | pending | evenly spaced sample | ;  |  |
| 358 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 361 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 375 | pending | layout_before_sites.json:157 140-3:185; layout_repairs_applied.json:69 140-3:186 | ;  |  |
| 376 | pending | layout_repairs_applied.json:69 140-3:186 | ;  |  |
| 378 | pending | evenly spaced sample | ;  |  |
| 379 | pending | layout_before_sites.json:158 140-3:191; layout_before_sites.json:159 140-3:191; layout_before_sites.json:160 140-3:192 | ;  |  |
| 380 | pending | layout_before_sites.json:160 140-3:192; layout_before_sites.json:161 140-3:194 | ;  |  |
| 381 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 383 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 384 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 389 | pending | layout_repairs_applied.json:70 140-3:208 | ;  |  |
| 390 | pending | layout_repairs_applied.json:70 140-3:208; layout_repairs_applied.json:71 140-3:209 | ;  |  |
| 392 | pending | layout_before_sites.json:164 140-3:212; layout_before_sites.json:165 140-3:213 | ;  |  |
| 393 | pending | layout_before_sites.json:165 140-3:213; layout_before_sites.json:166 140-3:215 | ;  |  |
| 394 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 397 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_repairs_applied.json:72 140-3:221 | ;  |  |
| 398 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_before_sites.json:169 140-3:222; layout_repairs_applied.json:72 140-3:221 | ;  |  |
| 399 | pending | layout_before_sites.json:169 140-3:222 | ;  |  |
| 400 | pending | evenly spaced sample | ;  |  |
| 404 | pending | layout_before_sites.json:170 140-3:231 | ;  |  |
| 405 | pending | layout_before_sites.json:170 140-3:231; layout_before_sites.json:171 140-3:232 | ;  |  |
| 406 | pending | layout_before_sites.json:171 140-3:232 | ;  |  |
| 412 | pending | layout_repairs_applied.json:73 140-3:245 | ;  |  |
| 419 | pending | layout_repairs_applied.json:74 140-3:261 | ;  |  |
| 420 | pending | layout_repairs_applied.json:74 140-3:261 | ;  |  |
| 422 | pending | evenly spaced sample | ;  |  |
| 426 | pending | layout_repairs_applied.json:75 140-3:275 | ;  |  |
| 427 | pending | layout_repairs_applied.json:75 140-3:275 | ;  |  |
| 430 | pending | layout_before_sites.json:172 140-3:282 | ;  |  |
| 431 | pending | layout_before_sites.json:172 140-3:282; layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 432 | pending | layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 442 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 443 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 444 | pending | evenly spaced sample | ;  |  |
| 451 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:76 140-3:320 | ;  |  |
| 452 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:76 140-3:320 | ;  |  |
| 453 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 454 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 455 | pending | layout_before_sites.json:179 140-3:327 | ;  |  |
| 456 | pending | layout_before_sites.json:179 140-3:327; layout_before_sites.json:180 140-3:328; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:77 140-3:328 | ;  |  |
| 457 | pending | layout_before_sites.json:180 140-3:328; layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:73 140-3:329; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:77 140-3:328; layout_repairs_applied.json:78 140-3:329 | ;  |  |
| 458 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:78 140-3:329 | ;  |  |
| 461 | pending | layout_before_sites.json:182 140-3:334; layout_repairs_applied.json:80 140-3:335 | ;  |  |
| 462 | pending | layout_repairs_applied.json:80 140-3:335 | ;  |  |
| 466 | pending | evenly spaced sample | ;  |  |
| 468 | pending | layout_before_sites.json:183 140-3:346 | ;  |  |
| 469 | pending | layout_before_sites.json:183 140-3:346 | ;  |  |
| 472 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 473 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 475 | pending | layout_before_sites.json:185 140-3:356 | ;  |  |
| 476 | pending | layout_before_sites.json:185 140-3:356; layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357; layout_repairs_applied.json:81 140-3:358 | ;  |  |
| 477 | pending | layout_repairs_applied.json:81 140-3:358 | ;  |  |
| 479 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362; layout_repairs_applied.json:84 140-3:363 | ;  |  |
| 480 | pending | layout_repairs_applied.json:84 140-3:363 | ;  |  |
| 488 | pending | evenly spaced sample | ;  |  |
| 489 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 490 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 496 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 508 | pending | layout_repairs_applied.json:91 140-3:408; layout_repairs_applied.json:92 140-3:408; layout_repairs_applied.json:93 140-3:408 | ;  |  |
| 509 | pending | layout_repairs_applied.json:94 140-3:410 | ;  |  |
| 510 | pending | layout_repairs_applied.json:94 140-3:410 | ;  |  |
| 511 | pending | evenly spaced sample; layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 512 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 513 | pending | layout_before_sites.json:192 140-3:415 | ;  |  |
| 514 | pending | layout_before_sites.json:192 140-3:415; layout_before_sites.json:193 140-3:416 | ;  |  |
| 515 | pending | layout_before_sites.json:193 140-3:416 | ;  |  |
| 516 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:98 140-3:419 | ;  |  |
| 517 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:98 140-3:419 | ;  |  |
| 522 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:95 140-3:425 | ;  |  |
| 524 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 525 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429; layout_before_sites.json:197 140-3:431 | ;  |  |
| 526 | pending | layout_before_sites.json:197 140-3:431 | ;  |  |
| 527 | pending | layout_before_sites.json:197 140-3:431; layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432 | ;  |  |
| 528 | pending | layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432; layout_before_sites.json:200 140-3:433 | ;  |  |
| 530 | pending | layout_repairs_applied.json:107 140-3:436; layout_repairs_applied.json:108 140-3:436; layout_repairs_applied.json:109 140-3:436 | ;  |  |
| 531 | pending | layout_repairs_applied.json:107 140-3:436; layout_repairs_applied.json:108 140-3:436; layout_repairs_applied.json:109 140-3:436; layout_repairs_applied.json:110 140-3:437; layout_repairs_applied.json:111 140-3:437 | ;  |  |
| 532 | pending | layout_repairs_applied.json:110 140-3:437; layout_repairs_applied.json:111 140-3:437; layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438 | ;  |  |
| 533 | pending | evenly spaced sample; layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438; layout_repairs_applied.json:116 140-3:439; layout_repairs_applied.json:117 140-3:440; layout_repairs_applied.json:99 140-3:440 | ;  |  |
| 534 | pending | layout_repairs_applied.json:103 140-3:441; layout_repairs_applied.json:117 140-3:440; layout_repairs_applied.json:99 140-3:440 | ;  |  |
| 535 | pending | layout_repairs_applied.json:103 140-3:441 | ;  |  |
| 536 | pending | layout_before_sites.json:201 140-3:444; layout_repairs_applied.json:106 140-3:443 | ;  |  |
| 537 | pending | layout_before_sites.json:201 140-3:444 | ;  |  |
| 538 | pending | layout_pass_sites.json:12 140-3:446; layout_repairs_applied.json:101 140-3:446 | ;  |  |
| 539 | pending | layout_pass_sites.json:12 140-3:446; layout_repairs_applied.json:101 140-3:446 | ;  |  |
| 540 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:100 140-3:448 | ;  |  |
| 541 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:100 140-3:448; layout_repairs_applied.json:104 140-3:449; layout_repairs_applied.json:105 140-3:449 | ;  |  |
| 544 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 545 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 546 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 548 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 549 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 550 | pending | layout_repairs_applied.json:118 140-3:462; layout_repairs_applied.json:119 140-3:463; layout_repairs_applied.json:120 140-3:463; layout_repairs_applied.json:121 140-3:463 | ;  |  |
| 551 | pending | layout_repairs_applied.json:119 140-3:463; layout_repairs_applied.json:120 140-3:463; layout_repairs_applied.json:121 140-3:463 | ;  |  |
| 552 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 553 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 554 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 555 | pending | evenly spaced sample; layout_before_sites.json:208 140-3:468; layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 556 | pending | layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 561 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 562 | pending | layout_before_sites.json:211 140-3:479; layout_repairs_applied.json:122 140-3:480; layout_repairs_applied.json:123 140-3:480 | ;  |  |
| 563 | pending | layout_repairs_applied.json:122 140-3:480; layout_repairs_applied.json:123 140-3:480 | ;  |  |
| 566 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 568 | pending | layout_before_sites.json:213 140-3:491 | ;  |  |
| 569 | pending | layout_before_sites.json:213 140-3:491; layout_before_sites.json:214 140-3:492 | ;  |  |
| 570 | pending | layout_before_sites.json:214 140-3:492; layout_repairs_applied.json:124 140-3:494 | ;  |  |
| 573 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 574 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 576 | pending | layout_repairs_applied.json:126 140-3:503 | ;  |  |
| 577 | pending | evenly spaced sample; layout_repairs_applied.json:126 140-3:503 | ;  |  |
| 579 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:127 140-3:506; layout_repairs_applied.json:128 140-3:506 | ;  |  |
| 580 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:127 140-3:506; layout_repairs_applied.json:128 140-3:506 | ;  |  |
| 581 | pending | layout_before_sites.json:217 140-3:509 | ;  |  |
| 582 | pending | layout_before_sites.json:217 140-3:509; layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 583 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 586 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 587 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 588 | pending | layout_before_sites.json:221 140-3:517; layout_before_sites.json:222 140-3:518 | ;  |  |
| 589 | pending | layout_before_sites.json:222 140-3:518; layout_before_sites.json:223 140-3:519; layout_repairs_applied.json:129 140-3:519; layout_repairs_applied.json:134 140-3:519 | ;  |  |
| 590 | pending | layout_before_sites.json:223 140-3:519; layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:129 140-3:519; layout_repairs_applied.json:133 140-3:520; layout_repairs_applied.json:134 140-3:519 | ;  |  |
| 591 | pending | layout_before_sites.json:224 140-3:520; layout_before_sites.json:225 140-3:522; layout_repairs_applied.json:133 140-3:520 | ;  |  |
| 592 | pending | layout_before_sites.json:225 140-3:522 | ;  |  |
| 593 | pending | layout_before_sites.json:225 140-3:522; layout_repairs_applied.json:135 140-3:523 | ;  |  |
| 594 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:130 140-3:525; layout_repairs_applied.json:135 140-3:523; layout_repairs_applied.json:136 140-3:524; layout_repairs_applied.json:137 140-3:524; layout_repairs_applied.json:138 140-3:525; layout_repairs_applied.json:139 140-3:525 | ;  |  |
| 595 | pending | layout_repairs_applied.json:130 140-3:525; layout_repairs_applied.json:138 140-3:525; layout_repairs_applied.json:139 140-3:525 | ;  |  |
| 598 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530; layout_before_sites.json:229 140-3:531 | ;  |  |
| 599 | pending | evenly spaced sample; layout_before_sites.json:229 140-3:531; layout_before_sites.json:230 140-3:532 | ;  |  |
| 600 | pending | layout_before_sites.json:230 140-3:532; layout_before_sites.json:231 140-3:533; layout_before_sites.json:232 140-3:534 | ;  |  |
| 601 | pending | layout_before_sites.json:232 140-3:534; layout_before_sites.json:233 140-3:535 | ;  |  |
| 602 | pending | layout_before_sites.json:233 140-3:535; layout_before_sites.json:234 140-3:536; layout_repairs_applied.json:140 140-3:536 | ;  |  |
| 603 | pending | layout_before_sites.json:234 140-3:536; layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_before_sites.json:238 140-3:538; layout_repairs_applied.json:140 140-3:536 | ;  |  |
| 604 | pending | layout_before_sites.json:238 140-3:538; layout_before_sites.json:239 140-3:539; layout_before_sites.json:240 140-3:540 | ;  |  |
| 605 | pending | layout_before_sites.json:240 140-3:540; layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 606 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541; layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:141 140-3:542; layout_repairs_applied.json:145 140-3:542 | ;  |  |
| 607 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_before_sites.json:245 140-3:543; layout_repairs_applied.json:141 140-3:542; layout_repairs_applied.json:145 140-3:542; layout_repairs_applied.json:146 140-3:543; layout_repairs_applied.json:147 140-3:543; layout_repairs_applied.json:148 140-3:543 | ;  |  |
| 608 | pending | layout_before_sites.json:245 140-3:543; layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:146 140-3:543; layout_repairs_applied.json:147 140-3:543; layout_repairs_applied.json:148 140-3:543; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544 | ;  |  |
| 609 | pending | layout_before_sites.json:246 140-3:544; layout_before_sites.json:247 140-3:545; layout_repairs_applied.json:142 140-3:545; layout_repairs_applied.json:143 140-3:545; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544; layout_repairs_applied.json:151 140-3:545; layout_repairs_applied.json:152 140-3:545; layout_repairs_applied.json:153 140-3:545; layout_repairs_applied.json:154 140-3:545; layout_repairs_applied.json:155 140-3:545; layout_repairs_applied.json:156 140-3:545 | ;  |  |
| 610 | pending | layout_before_sites.json:247 140-3:545; layout_before_sites.json:248 140-3:546; layout_repairs_applied.json:142 140-3:545; layout_repairs_applied.json:143 140-3:545; layout_repairs_applied.json:144 140-3:546; layout_repairs_applied.json:151 140-3:545; layout_repairs_applied.json:152 140-3:545; layout_repairs_applied.json:153 140-3:545; layout_repairs_applied.json:154 140-3:545; layout_repairs_applied.json:155 140-3:545; layout_repairs_applied.json:156 140-3:545 | ;  |  |
| 611 | pending | layout_before_sites.json:248 140-3:546; layout_before_sites.json:249 140-3:547; layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:144 140-3:546; layout_repairs_applied.json:157 140-3:548 | ;  |  |
| 612 | pending | layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:157 140-3:548 | ;  |  |
| 615 | pending | layout_before_sites.json:251 140-3:554; layout_repairs_applied.json:158 140-3:554 | ;  |  |
| 616 | pending | layout_before_sites.json:251 140-3:554; layout_before_sites.json:252 140-3:555; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:158 140-3:554; layout_repairs_applied.json:159 140-3:555 | ;  |  |
| 617 | pending | layout_before_sites.json:252 140-3:555; layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:159 140-3:555; layout_repairs_applied.json:160 140-3:556 | ;  |  |
| 618 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_before_sites.json:255 140-3:557; layout_pass_sites.json:14 140-3:557; layout_pass_sites.json:75 140-3:557; layout_repairs_applied.json:160 140-3:556; layout_repairs_applied.json:162 140-3:557 | ;  |  |
| 619 | pending | layout_before_sites.json:255 140-3:557; layout_before_sites.json:256 140-3:558; layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559; layout_pass_sites.json:14 140-3:557; layout_pass_sites.json:75 140-3:557; layout_repairs_applied.json:162 140-3:557 | ;  |  |
| 620 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 621 | pending | evenly spaced sample; layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559; layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:163 140-3:561 | ;  |  |
| 622 | pending | landscape page; layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:163 140-3:561 | ;  |  |
| 623 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:161 140-3:562; layout_repairs_applied.json:163 140-3:561; layout_repairs_applied.json:166 140-3:562; layout_repairs_applied.json:167 140-3:562 | ;  |  |
| 624 | pending | layout_repairs_applied.json:161 140-3:562; layout_repairs_applied.json:166 140-3:562; layout_repairs_applied.json:167 140-3:562 | ;  |  |
| 625 | pending | layout_repairs_applied.json:168 140-3:565 | ;  |  |
| 626 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567; layout_repairs_applied.json:168 140-3:565 | ;  |  |
| 627 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567; layout_repairs_applied.json:169 140-3:568 | ;  |  |
| 628 | pending | layout_repairs_applied.json:169 140-3:568 | ;  |  |
| 629 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 630 | pending | layout_before_sites.json:262 140-3:570; layout_before_sites.json:263 140-3:573; layout_repairs_applied.json:170 140-3:573 | ;  |  |
| 631 | pending | layout_before_sites.json:263 140-3:573; layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:170 140-3:573; layout_repairs_applied.json:171 140-3:574 | ;  |  |
| 632 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:171 140-3:574; layout_repairs_applied.json:173 140-3:575 | ;  |  |
| 633 | pending | layout_before_sites.json:265 140-3:577; layout_repairs_applied.json:173 140-3:575 | ;  |  |
| 634 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 637 | pending | layout_before_sites.json:266 140-3:582 | ;  |  |
| 638 | pending | layout_before_sites.json:266 140-3:582 | ;  |  |
| 639 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 640 | pending | layout_before_sites.json:267 140-3:585; layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 641 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586; layout_before_sites.json:270 140-3:587 | ;  |  |
| 642 | pending | layout_before_sites.json:270 140-3:587; layout_before_sites.json:271 140-3:588 | ;  |  |
| 643 | pending | evenly spaced sample; layout_before_sites.json:271 140-3:588; layout_before_sites.json:272 140-3:589 | ;  |  |
| 644 | pending | layout_before_sites.json:272 140-3:589; layout_repairs_applied.json:175 140-3:590 | ;  |  |
| 645 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 646 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 650 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 651 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 654 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:176 140-3:606 | ;  |  |
| 655 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:176 140-3:606 | ;  |  |
| 656 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:178 140-3:609 | ;  |  |
| 657 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:178 140-3:609 | ;  |  |
| 661 | pending | layout_before_sites.json:275 140-3:616 | ;  |  |
| 662 | pending | layout_before_sites.json:275 140-3:616; layout_before_sites.json:276 140-3:617 | ;  |  |
| 663 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:179 140-3:619 | ;  |  |
| 664 | pending | layout_before_sites.json:277 140-3:619; layout_before_sites.json:278 140-3:621; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:18 140-3:621; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:177 140-3:621; layout_repairs_applied.json:179 140-3:619; layout_repairs_applied.json:184 140-3:621 | ;  |  |
| 665 | pending | layout_before_sites.json:278 140-3:621; layout_pass_sites.json:18 140-3:621; layout_repairs_applied.json:177 140-3:621; layout_repairs_applied.json:184 140-3:621; layout_repairs_applied.json:185 140-3:622; layout_repairs_applied.json:186 140-3:622; layout_repairs_applied.json:187 140-3:622; layout_repairs_applied.json:188 140-3:622; layout_repairs_applied.json:189 140-3:622 | ;  |  |
| 666 | pending | evenly spaced sample; layout_repairs_applied.json:185 140-3:622; layout_repairs_applied.json:186 140-3:622; layout_repairs_applied.json:187 140-3:622; layout_repairs_applied.json:188 140-3:622; layout_repairs_applied.json:189 140-3:622; layout_repairs_applied.json:190 140-3:623; layout_repairs_applied.json:191 140-3:623 | ;  |  |
| 667 | pending | layout_before_sites.json:279 140-3:625; layout_repairs_applied.json:190 140-3:623; layout_repairs_applied.json:191 140-3:623 | ;  |  |
| 668 | pending | layout_before_sites.json:279 140-3:625; layout_before_sites.json:280 140-3:627 | ;  |  |
| 669 | pending | layout_before_sites.json:280 140-3:627; layout_before_sites.json:281 140-3:629; layout_repairs_applied.json:192 140-3:628 | ;  |  |
| 670 | pending | layout_before_sites.json:281 140-3:629 | ;  |  |
| 671 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 674 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:194 140-3:637; layout_repairs_applied.json:196 140-3:637 | ;  |  |
| 675 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:193 140-3:638; layout_repairs_applied.json:194 140-3:637; layout_repairs_applied.json:196 140-3:637 | ;  |  |
| 681 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:207 140-3:649 | ;  |  |
| 682 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:207 140-3:649 | ;  |  |
| 683 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:197 140-3:653; layout_repairs_applied.json:208 140-3:653 | ;  |  |
| 684 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:197 140-3:653; layout_repairs_applied.json:208 140-3:653 | ;  |  |
| 685 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:209 140-3:656; layout_repairs_applied.json:210 140-3:656 | ;  |  |
| 686 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:209 140-3:656; layout_repairs_applied.json:210 140-3:656 | ;  |  |
| 687 | pending | layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_repairs_applied.json:198 140-3:658; layout_repairs_applied.json:199 140-3:658 | ;  |  |
| 688 | pending | evenly spaced sample; layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:198 140-3:658; layout_repairs_applied.json:199 140-3:658; layout_repairs_applied.json:200 140-3:659; layout_repairs_applied.json:201 140-3:659 | ;  |  |
| 689 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:200 140-3:659; layout_repairs_applied.json:201 140-3:659; layout_repairs_applied.json:202 140-3:660 | ;  |  |
| 690 | pending | layout_repairs_applied.json:202 140-3:660 | ;  |  |
| 691 | pending | layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:203 140-3:662 | ;  |  |
| 692 | pending | layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:203 140-3:662 | ;  |  |
| 696 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 701 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 702 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 704 | pending | layout_repairs_applied.json:213 140-3:685; layout_repairs_applied.json:214 140-3:685 | ;  |  |
| 705 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:213 140-3:685; layout_repairs_applied.json:214 140-3:685; layout_repairs_applied.json:215 140-3:686 | ;  |  |
| 706 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:215 140-3:686; layout_repairs_applied.json:216 140-3:688; layout_repairs_applied.json:217 140-3:688 | ;  |  |
| 707 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:216 140-3:688; layout_repairs_applied.json:217 140-3:688; layout_repairs_applied.json:218 140-3:689 | ;  |  |
| 708 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:218 140-3:689 | ;  |  |
| 709 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692 | ;  |  |
| 710 | pending | evenly spaced sample; layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692; layout_repairs_applied.json:219 140-3:693; layout_repairs_applied.json:220 140-3:693 | ;  |  |
| 711 | pending | layout_repairs_applied.json:219 140-3:693; layout_repairs_applied.json:220 140-3:693 | ;  |  |
| 714 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 716 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 717 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 718 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 719 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 722 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:221 140-4:20 | ;  |  |
| 723 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:221 140-4:20 | ;  |  |
| 727 | pending | layout_before_sites.json:311 140-4:29 | ;  |  |
| 728 | pending | layout_repairs_applied.json:223 140-4:31; layout_repairs_applied.json:224 140-4:31; layout_repairs_applied.json:225 140-4:31; layout_repairs_applied.json:226 140-4:32; layout_repairs_applied.json:227 140-4:32 | ;  |  |
| 729 | pending | layout_repairs_applied.json:226 140-4:32; layout_repairs_applied.json:227 140-4:32; layout_repairs_applied.json:228 140-4:33 | ;  |  |
| 730 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:228 140-4:33 | ;  |  |
| 731 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:229 140-4:35; layout_repairs_applied.json:230 140-4:35 | ;  |  |
| 732 | pending | evenly spaced sample; layout_repairs_applied.json:229 140-4:35; layout_repairs_applied.json:230 140-4:35 | ;  |  |
| 735 | pending | layout_before_sites.json:314 140-4:39; layout_before_sites.json:315 140-4:40 | ;  |  |
| 736 | pending | layout_before_sites.json:315 140-4:40; layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41; layout_before_sites.json:318 140-4:42 | ;  |  |
| 737 | pending | layout_before_sites.json:318 140-4:42; layout_before_sites.json:319 140-4:43; layout_before_sites.json:320 140-4:44; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:231 140-4:44 | ;  |  |
| 738 | pending | layout_before_sites.json:320 140-4:44; layout_before_sites.json:321 140-4:45; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:231 140-4:44 | ;  |  |
| 739 | pending | layout_before_sites.json:321 140-4:45; layout_before_sites.json:322 140-4:46 | ;  |  |
| 740 | pending | layout_before_sites.json:322 140-4:46; layout_before_sites.json:323 140-4:47; layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48 | ;  |  |
| 741 | pending | layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48; layout_before_sites.json:327 140-4:49 | ;  |  |
| 742 | pending | layout_before_sites.json:327 140-4:49; layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 743 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50; layout_before_sites.json:331 140-4:51 | ;  |  |
| 744 | pending | layout_before_sites.json:331 140-4:51; layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52; layout_before_sites.json:334 140-4:53 | ;  |  |
| 745 | pending | layout_before_sites.json:334 140-4:53; layout_before_sites.json:335 140-4:54; layout_before_sites.json:336 140-4:55 | ;  |  |
| 746 | pending | layout_before_sites.json:336 140-4:55; layout_before_sites.json:337 140-4:56; layout_before_sites.json:338 140-4:57 | ;  |  |
| 747 | pending | layout_before_sites.json:338 140-4:57 | ;  |  |
| 748 | pending | layout_repairs_applied.json:244 140-4:59 | ;  |  |
| 749 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:245 140-4:61; layout_repairs_applied.json:246 140-4:61; layout_repairs_applied.json:247 140-4:61; layout_repairs_applied.json:248 140-4:61; layout_repairs_applied.json:249 140-4:62 | ;  |  |
| 750 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:249 140-4:62 | ;  |  |
| 751 | pending | layout_repairs_applied.json:242 140-4:65 | ;  |  |
| 752 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:233 140-4:66; layout_repairs_applied.json:234 140-4:66; layout_repairs_applied.json:235 140-4:66; layout_repairs_applied.json:242 140-4:65 | ;  |  |
| 753 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_before_sites.json:343 140-4:67; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:233 140-4:66; layout_repairs_applied.json:234 140-4:66; layout_repairs_applied.json:235 140-4:66 | ;  |  |
| 754 | pending | evenly spaced sample; layout_before_sites.json:344 140-4:70 | ;  |  |
| 755 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 758 | pending | layout_repairs_applied.json:250 140-4:74 | ;  |  |
| 759 | pending | layout_repairs_applied.json:243 140-4:75; layout_repairs_applied.json:250 140-4:74; layout_repairs_applied.json:251 140-4:75; layout_repairs_applied.json:252 140-4:75; layout_repairs_applied.json:253 140-4:75 | ;  |  |
| 760 | pending | layout_repairs_applied.json:243 140-4:75; layout_repairs_applied.json:251 140-4:75; layout_repairs_applied.json:252 140-4:75; layout_repairs_applied.json:253 140-4:75; layout_repairs_applied.json:254 140-4:76; layout_repairs_applied.json:255 140-4:76 | ;  |  |
| 761 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:254 140-4:76; layout_repairs_applied.json:255 140-4:76; layout_repairs_applied.json:258 140-4:77 | ;  |  |
| 762 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:258 140-4:77; layout_repairs_applied.json:259 140-4:78; layout_repairs_applied.json:260 140-4:78; layout_repairs_applied.json:261 140-4:79; layout_repairs_applied.json:262 140-4:79 | ;  |  |
| 763 | pending | layout_repairs_applied.json:261 140-4:79; layout_repairs_applied.json:262 140-4:79; layout_repairs_applied.json:263 140-4:80 | ;  |  |
| 764 | pending | layout_repairs_applied.json:263 140-4:80; layout_repairs_applied.json:264 140-4:81; layout_repairs_applied.json:265 140-4:81 | ;  |  |
| 765 | pending | layout_repairs_applied.json:264 140-4:81; layout_repairs_applied.json:265 140-4:81 | ;  |  |
| 772 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 773 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 775 | pending | layout_repairs_applied.json:269 140-4:96; layout_repairs_applied.json:270 140-4:96 | ;  |  |
| 776 | pending | evenly spaced sample; layout_repairs_applied.json:269 140-4:96; layout_repairs_applied.json:270 140-4:96; layout_repairs_applied.json:271 140-4:97; layout_repairs_applied.json:272 140-4:97 | ;  |  |
| 777 | pending | layout_repairs_applied.json:271 140-4:97; layout_repairs_applied.json:272 140-4:97; layout_repairs_applied.json:273 140-4:98 | ;  |  |
| 778 | pending | layout_before_sites.json:349 140-4:99; layout_repairs_applied.json:273 140-4:98 | ;  |  |
| 779 | pending | layout_before_sites.json:350 140-4:101 | ;  |  |
| 780 | pending | layout_before_sites.json:350 140-4:101; layout_before_sites.json:351 140-4:102 | ;  |  |
| 781 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 782 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 786 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:266 140-4:113 | ;  |  |
| 799 | pending | evenly spaced sample | ;  |  |
| 801 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:274 140-4:136 | ;  |  |
| 802 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:274 140-4:136 | ;  |  |
| 805 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 806 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 807 | pending | layout_before_sites.json:356 140-4:149 | ;  |  |
| 809 | pending | layout_before_sites.json:357 140-4:154 | ;  |  |
| 817 | pending | layout_repairs_applied.json:276 140-4:172 | ;  |  |
| 818 | pending | layout_repairs_applied.json:277 140-4:174; layout_repairs_applied.json:278 140-4:175; layout_repairs_applied.json:279 140-4:175 | ;  |  |
| 819 | pending | layout_repairs_applied.json:278 140-4:175; layout_repairs_applied.json:279 140-4:175 | ;  |  |
| 821 | pending | evenly spaced sample; layout_before_sites.json:358 140-4:181; layout_before_sites.json:359 140-4:181 | ;  |  |
| 822 | pending | layout_before_sites.json:360 140-4:186 | ;  |  |
| 823 | pending | layout_before_sites.json:361 140-4:188 | ;  |  |
| 827 | pending | layout_repairs_applied.json:280 140-4:203; layout_repairs_applied.json:281 140-4:203 | ;  |  |
| 828 | pending | layout_repairs_applied.json:280 140-4:203; layout_repairs_applied.json:281 140-4:203; layout_repairs_applied.json:282 140-4:205 | ;  |  |
| 829 | pending | layout_repairs_applied.json:282 140-4:205 | ;  |  |
| 840 | pending | layout_before_sites.json:362 140-4:230 | ;  |  |
| 843 | pending | evenly spaced sample; layout_before_sites.json:363 140-4:236 | ;  |  |
| 847 | pending | layout_before_sites.json:364 140-4:245 | ;  |  |
| 849 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 850 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 856 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 857 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 858 | pending | layout_before_sites.json:367 140-4:266; layout_before_sites.json:368 140-4:267 | ;  |  |
| 859 | pending | layout_before_sites.json:368 140-4:267; layout_before_sites.json:369 140-4:268 | ;  |  |
| 860 | pending | layout_before_sites.json:369 140-4:268; layout_before_sites.json:370 140-4:269; layout_before_sites.json:371 140-4:270 | ;  |  |
| 861 | pending | layout_before_sites.json:371 140-4:270; layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_before_sites.json:374 140-4:272; layout_before_sites.json:375 140-4:273; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:286 140-4:271; layout_repairs_applied.json:288 140-4:271 | ;  |  |
| 862 | pending | layout_before_sites.json:375 140-4:273; layout_before_sites.json:376 140-4:274; layout_before_sites.json:377 140-4:275 | ;  |  |
| 863 | pending | layout_before_sites.json:377 140-4:275; layout_before_sites.json:378 140-4:276; layout_before_sites.json:379 140-4:277; layout_repairs_applied.json:287 140-4:276 | ;  |  |
| 864 | pending | layout_before_sites.json:379 140-4:277; layout_before_sites.json:380 140-4:278; layout_before_sites.json:381 140-4:279 | ;  |  |
| 865 | pending | evenly spaced sample; layout_before_sites.json:381 140-4:279; layout_before_sites.json:382 140-4:280 | ;  |  |

### LM_FR_corrige_apparat.pdf

PDF SHA-256: `dbddcc1397d6c927a64de248c44c165a222168160d632ddad0441830e96925db`.

| Physical page | Status | Selection reason | Reviewer and inspection basis | Observation |
|---|---|---|---|---|
| 1 | reviewed | evenly spaced sample | editorial; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Title page is centered, spacious and fully contained; edition title and archive attribution are legible.; Close 4-page sheet inspection: Title page is centered, spacious and fully contained; edition title and archive attribution are legible.; Close 4-page sheet inspection: Title page is centered, spacious and fully contained; edition title and archive attribution are legible. |
| 6 | reviewed | layout_before_sites.json:1 140-1:4 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | Scan2 apparatus entries remain separated, and the scan4 opening identities and boxed relations fit below the markers. The footer and right margin are clear. |
| 7 | reviewed | layout_before_sites.json:1 140-1:4 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The rho-product derivation, underbraces, boxed conclusion and central-extension displays fit within the text width. The apparatus starts with its rule, heading and first entry together. |
| 8 | reviewed | layout_before_sites.json:1 140-1:4 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | Long conjugation computations remain separated vertically and fit within the page. Both short right-margin notes stay outside the main formulas, and the continued apparatus at the top is legible. |
| 10 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:5 140-1:10 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | Marginal note m12 retains its heading, explanatory text and diagrams on the page. The successive exact-sequence diagrams, blue alternatives and lower apparatus have clear spacing. |
| 11 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:5 140-1:10 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The large scan10 group diagram remains within the page width, with its nodes, routed lines and labels visible. The following group presentations and smaller maps fit below it without clipping. |
| 12 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:5 140-1:10 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The second scan10 diagram is complete above its apparatus. The pr1 label, blue alternatives and adjoining nodes are distinct at this full-page scale; the apparatus rule and first entry stay together. |
| 13 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:3 140-1:12; layout_repairs_applied.json:5 140-1:10 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | Note m15 begins with its rule, heading and proposition, followed by the complete extension diagram. Formula lines remain separated and clear of the page number. |
| 14 | reviewed | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:3 140-1:12 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The large nested fractions and underbraces remain intact within the text area. Note m16 retains its heading and formula body, and the scan12 apparatus starts with its first entry. |
| 15 | reviewed | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:3 140-1:12 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The continued apparatus and scan14 algebraic calculations are legible and contained within the page. The paired formula columns and lower modular-arithmetic lines have distinct spacing. |
| 16 | reviewed | layout_before_sites.json:8 140-1:15 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The parity calculations and scan14 apparatus are separated clearly. Note m19 keeps its heading with the modular computations; the following ARTICLE5 prose starts with multiple lines. |
| 17 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:8 140-1:15; layout_before_sites.json:9 140-1:16 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The large cancelled passage in the apparatus remains fully visible in gray with its blue uncertainty marks. Its explanation and the scan16 cartesian square fit below without collision. |
| 18 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:9 140-1:16 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | Notes m22, m23, m25 and m26 retain their headings with their respective text, sketch or calculations. The loop sketch and central diagrams fit within the page; the short à vérifier/OK note remains visible at the foot. |
| 19 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:9 140-1:16 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | Note m27 begins on the page with its complete curved-arrow sketch beneath the heading. The following source paragraph and scan16 apparatus are contained and clearly separated. |
| 20 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:13 140-1:17; layout_before_sites.json:9 140-1:16 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The cancelled scan17 material remains represented by references and its apparatus; the Cas non orienté note is visible. The first cancelled tree and later formulas in the apparatus fit their entry blocks. |
| 21 | reviewed | layout_before_sites.json:13 140-1:17; layout_before_sites.json:14 140-1:18; layout_pass_sites.json:31 140-1:18 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The continued apparatus preserves the canceled incidence arrays and small branching diagram with blue uncertainty fragments. Entry spacing is distinct, and the next scan markers remain visible. |
| 22 | reviewed | layout_before_sites.json:14 140-1:18; layout_pass_sites.json:31 140-1:18 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The vertical extension diagram is intact within the main column, and the short right-margin note stays separate. Note m32 has its rule, heading and body together before the scan18 apparatus. |
| 23 | reviewed | layout_before_sites.json:14 140-1:18; layout_before_sites.json:15 140-1:19; layout_pass_sites.json:31 140-1:18; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:54 140-1:19; layout_repairs_applied.json:4 140-1:19 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The large source sketch, sphere drawing and sloping annotation lines are fully contained on the page. Its surrounding apparatus remains separated from the drawing and page furniture. |
| 24 | reviewed | layout_before_sites.json:15 140-1:19; layout_before_sites.json:16 140-1:20; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:54 140-1:19; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:13 140-1:20; layout_repairs_applied.json:4 140-1:19; layout_repairs_applied.json:8 140-1:20 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | Scans20–37 begins with its source diagram on the same page. The extensive cartesian-arrow network is contained, and note m35 keeps its heading with the opening text and displayed formula. |
| 25 | reviewed | layout_before_sites.json:16 140-1:20; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:13 140-1:20; layout_repairs_applied.json:8 140-1:20 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | Both scan20 and scan21 apparatus headings retain their first entries. The cancelled boxed table, exact sequence and branching diagram remain complete and visible within the apparatus. |
| 27 | reviewed | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23 | editorial; Actual 2x2 contact sheets, each full page at900px; revision578 prefix before573 repair | The lemma and note m39 retain their opening text and exact-sequence diagram. Subsequent homological formulas and the product expression fit within the text width with clear vertical separation. |
| 28 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23 | ;  |  |
| 29 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23; layout_repairs_applied.json:14 140-1:25 | ;  |  |
| 30 | pending | layout_repairs_applied.json:14 140-1:25 | ;  |  |
| 32 | pending | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | ;  |  |
| 33 | pending | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | ;  |  |
| 34 | pending | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | ;  |  |
| 35 | pending | layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | ;  |  |
| 36 | pending | layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | ;  |  |
| 40 | pending | evenly spaced sample | ;  |  |
| 41 | pending | layout_before_sites.json:23 140-1:36; layout_before_sites.json:24 140-1:36; layout_pass_sites.json:34 140-1:36; layout_pass_sites.json:56 140-1:36; layout_repairs_applied.json:9 140-1:36 | ;  |  |
| 42 | reviewed | layout_before_sites.json:25 140-2:4 | editorial; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The new cote heading and manuscript contents list align cleanly; page references and the bottom apparatus are distinct.; Close inspection in the 4-page sheet: main text, mathematical symbols, note rules and apparatus entries are distinct; no clipped or overprinted content observed. Source contents-list entries and right-side manuscript references are fully visible.; Close inspection in the 4-page sheet: main text, mathematical symbols, note rules and apparatus entries are distinct; no clipped or overprinted content observed. Source contents-list entries and right-side manuscript references are fully visible. |
| 43 | reviewed | layout_before_sites.json:25 140-2:4 | editorial; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The contents continuation and apparatus retain a clear right edge; the start of the next scan stays above the footer.; Close inspection in the 4-page sheet: main text, mathematical symbols, note rules and apparatus entries are distinct; no clipped or overprinted content observed. Source contents-list entries and right-side manuscript references are fully visible.; Close inspection in the 4-page sheet: main text, mathematical symbols, note rules and apparatus entries are distinct; no clipped or overprinted content observed. Source contents-list entries and right-side manuscript references are fully visible. |
| 58 | pending | layout_before_sites.json:26 140-2:28 | ;  |  |
| 59 | pending | layout_before_sites.json:26 140-2:28; layout_before_sites.json:27 140-2:29 | ;  |  |
| 60 | pending | layout_before_sites.json:27 140-2:29 | ;  |  |
| 64 | pending | layout_before_sites.json:28 140-2:35 | ;  |  |
| 65 | pending | layout_before_sites.json:28 140-2:35 | ;  |  |
| 68 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 69 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 70 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 71 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 72 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 73 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 74 | pending | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44 | ;  |  |
| 75 | pending | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44; layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | ;  |  |
| 76 | pending | layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | ;  |  |
| 80 | pending | evenly spaced sample | ;  |  |
| 94 | pending | layout_before_sites.json:35 140-2:69 | ;  |  |
| 103 | pending | layout_before_sites.json:36 140-2:80 | ;  |  |
| 104 | pending | layout_before_sites.json:36 140-2:80 | ;  |  |
| 109 | pending | layout_before_sites.json:37 140-2:88 | ;  |  |
| 110 | pending | layout_before_sites.json:37 140-2:88; layout_repairs_applied.json:15 140-2:89 | ;  |  |
| 111 | pending | layout_repairs_applied.json:15 140-2:89 | ;  |  |
| 119 | pending | evenly spaced sample | ;  |  |
| 139 | pending | layout_before_sites.json:38 140-2:122 | ;  |  |
| 144 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 145 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 146 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 155 | pending | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | ;  |  |
| 156 | pending | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | ;  |  |
| 158 | pending | evenly spaced sample | ;  |  |
| 161 | pending | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | ;  |  |
| 162 | pending | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | ;  |  |
| 171 | pending | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | ;  |  |
| 172 | pending | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | ;  |  |
| 175 | pending | layout_before_sites.json:46 140-2:162 | ;  |  |
| 177 | pending | layout_before_sites.json:47 140-2:164; layout_before_sites.json:48 140-2:165; layout_repairs_applied.json:17 140-2:165 | ;  |  |
| 178 | pending | layout_before_sites.json:48 140-2:165; layout_before_sites.json:49 140-2:166; layout_repairs_applied.json:17 140-2:165 | ;  |  |
| 179 | pending | layout_before_sites.json:49 140-2:166 | ;  |  |
| 180 | pending | layout_before_sites.json:49 140-2:166 | ;  |  |
| 197 | pending | evenly spaced sample | ;  |  |
| 202 | pending | layout_before_sites.json:50 140-2:197 | ;  |  |
| 203 | pending | layout_before_sites.json:50 140-2:197 | ;  |  |
| 208 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205 | ;  |  |
| 209 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205; layout_repairs_applied.json:18 140-2:206 | ;  |  |
| 210 | pending | layout_repairs_applied.json:18 140-2:206 | ;  |  |
| 214 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 215 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 220 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 221 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 222 | pending | layout_before_sites.json:57 140-2:220 | ;  |  |
| 223 | pending | layout_before_sites.json:57 140-2:220 | ;  |  |
| 224 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 225 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 234 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 235 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 237 | pending | evenly spaced sample | ;  |  |
| 249 | pending | layout_repairs_applied.json:21 140-2:251 | ;  |  |
| 250 | pending | layout_repairs_applied.json:19 140-2:252; layout_repairs_applied.json:20 140-2:252; layout_repairs_applied.json:21 140-2:251; layout_repairs_applied.json:22 140-2:252 | ;  |  |
| 251 | pending | layout_repairs_applied.json:19 140-2:252; layout_repairs_applied.json:20 140-2:252; layout_repairs_applied.json:22 140-2:252 | ;  |  |
| 257 | pending | layout_before_sites.json:60 140-2:259 | ;  |  |
| 264 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 265 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 272 | pending | layout_before_sites.json:62 140-2:280 | ;  |  |
| 273 | pending | layout_before_sites.json:62 140-2:280 | ;  |  |
| 276 | pending | evenly spaced sample; layout_before_sites.json:63 140-2:285 | ;  |  |
| 277 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 278 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 291 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | ;  |  |
| 292 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | ;  |  |
| 293 | pending | landscape page; layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | ;  |  |
| 294 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | ;  |  |
| 300 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 301 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 302 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 309 | pending | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:26 140-2:321 | ;  |  |
| 310 | pending | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:26 140-2:321 | ;  |  |
| 315 | pending | evenly spaced sample; layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:25 140-2:328 | ;  |  |
| 316 | pending | layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_before_sites.json:71 140-2:329; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:25 140-2:328 | ;  |  |
| 317 | pending | layout_before_sites.json:71 140-2:329 | ;  |  |
| 318 | pending | layout_before_sites.json:71 140-2:329 | ;  |  |
| 319 | pending | layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:27 140-2:331; layout_repairs_applied.json:28 140-2:331 | ;  |  |
| 331 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | ;  |  |
| 332 | pending | landscape page; layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | ;  |  |
| 333 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | ;  |  |
| 334 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | ;  |  |
| 335 | pending | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | ;  |  |
| 336 | pending | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | ;  |  |
| 338 | pending | layout_before_sites.json:75 140-2:348; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:29 140-2:348 | ;  |  |
| 339 | pending | layout_before_sites.json:75 140-2:348; layout_before_sites.json:76 140-2:349; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:29 140-2:348 | ;  |  |
| 340 | pending | layout_before_sites.json:76 140-2:349 | ;  |  |
| 342 | pending | layout_before_sites.json:77 140-2:352 | ;  |  |
| 343 | pending | layout_before_sites.json:77 140-2:352 | ;  |  |
| 350 | pending | layout_before_sites.json:78 140-2:362 | ;  |  |
| 351 | pending | layout_before_sites.json:78 140-2:362 | ;  |  |
| 355 | pending | evenly spaced sample | ;  |  |
| 358 | pending | layout_before_sites.json:79 140-2:371 | ;  |  |
| 359 | pending | layout_before_sites.json:79 140-2:371 | ;  |  |
| 366 | pending | layout_repairs_applied.json:33 140-2:382 | ;  |  |
| 367 | pending | layout_repairs_applied.json:33 140-2:382 | ;  |  |
| 368 | pending | layout_before_sites.json:80 140-2:384; layout_pass_sites.json:40 140-2:384; layout_pass_sites.json:64 140-2:384 | ;  |  |
| 370 | pending | layout_before_sites.json:81 140-2:387 | ;  |  |
| 371 | pending | layout_before_sites.json:81 140-2:387 | ;  |  |
| 377 | pending | layout_repairs_applied.json:34 140-2:397 | ;  |  |
| 378 | pending | layout_repairs_applied.json:34 140-2:397 | ;  |  |
| 383 | pending | layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404 | ;  |  |
| 384 | pending | layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404; layout_repairs_applied.json:35 140-2:407 | ;  |  |
| 385 | pending | layout_repairs_applied.json:35 140-2:407 | ;  |  |
| 387 | pending | layout_pass_sites.json:41 140-2:411 | ;  |  |
| 393 | pending | layout_repairs_applied.json:36 140-2:417; layout_repairs_applied.json:38 140-2:417 | ;  |  |
| 394 | pending | evenly spaced sample; layout_repairs_applied.json:36 140-2:417; layout_repairs_applied.json:38 140-2:417 | ;  |  |
| 395 | pending | layout_before_sites.json:84 140-2:419; layout_before_sites.json:85 140-2:419; layout_pass_sites.json:4 140-2:419; layout_pass_sites.json:42 140-2:419; layout_pass_sites.json:59 140-2:419; layout_pass_sites.json:65 140-2:419; layout_repairs_applied.json:37 140-2:419 | ;  |  |
| 398 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 399 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 405 | pending | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | ;  |  |
| 406 | pending | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | ;  |  |
| 415 | pending | layout_before_sites.json:89 140-2:443 | ;  |  |
| 416 | pending | layout_before_sites.json:89 140-2:443 | ;  |  |
| 421 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 422 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 423 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 424 | pending | layout_before_sites.json:91 140-2:452 | ;  |  |
| 425 | pending | layout_before_sites.json:91 140-2:452 | ;  |  |
| 426 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 427 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 428 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 429 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 430 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 431 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 433 | pending | evenly spaced sample | ;  |  |
| 435 | pending | layout_before_sites.json:94 140-2:462 | ;  |  |
| 436 | pending | layout_before_sites.json:94 140-2:462 | ;  |  |
| 459 | pending | layout_before_sites.json:95 140-2:492 | ;  |  |
| 466 | pending | layout_before_sites.json:96 140-2:502 | ;  |  |
| 469 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:39 140-2:508 | ;  |  |
| 470 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:39 140-2:508 | ;  |  |
| 471 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:39 140-2:508 | ;  |  |
| 472 | pending | evenly spaced sample | ;  |  |
| 474 | pending | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | ;  |  |
| 475 | pending | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | ;  |  |
| 480 | pending | layout_before_sites.json:101 140-2:519 | ;  |  |
| 481 | pending | layout_before_sites.json:101 140-2:519; layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:41 140-2:520 | ;  |  |
| 482 | pending | layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:41 140-2:520 | ;  |  |
| 487 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:42 140-2:527 | ;  |  |
| 488 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:42 140-2:527 | ;  |  |
| 491 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | ;  |  |
| 492 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | ;  |  |
| 493 | pending | layout_before_sites.json:107 140-2:536 | ;  |  |
| 494 | pending | layout_before_sites.json:107 140-2:536 | ;  |  |
| 512 | pending | evenly spaced sample | ;  |  |
| 518 | pending | layout_before_sites.json:108 140-2:567 | ;  |  |
| 519 | pending | layout_before_sites.json:108 140-2:567 | ;  |  |
| 520 | pending | layout_before_sites.json:108 140-2:567; layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:43 140-2:568; layout_repairs_applied.json:44 140-2:568 | ;  |  |
| 521 | pending | layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:43 140-2:568; layout_repairs_applied.json:44 140-2:568 | ;  |  |
| 529 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | ;  |  |
| 530 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | ;  |  |
| 531 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4; layout_before_sites.json:114 140-3:5 | ;  |  |
| 532 | pending | layout_before_sites.json:114 140-3:5; layout_repairs_applied.json:45 140-3:6 | ;  |  |
| 533 | pending | layout_repairs_applied.json:45 140-3:6 | ;  |  |
| 538 | pending | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | ;  |  |
| 539 | pending | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | ;  |  |
| 543 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 544 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 546 | pending | layout_repairs_applied.json:46 140-3:21 | ;  |  |
| 548 | pending | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | ;  |  |
| 549 | pending | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | ;  |  |
| 551 | pending | evenly spaced sample | ;  |  |
| 554 | pending | layout_repairs_applied.json:47 140-3:33 | ;  |  |
| 555 | pending | layout_repairs_applied.json:47 140-3:33 | ;  |  |
| 557 | pending | layout_before_sites.json:124 140-3:36 | ;  |  |
| 558 | pending | layout_before_sites.json:124 140-3:36 | ;  |  |
| 560 | pending | layout_repairs_applied.json:48 140-3:40 | ;  |  |
| 561 | pending | layout_repairs_applied.json:48 140-3:40; layout_repairs_applied.json:49 140-3:41 | ;  |  |
| 562 | pending | layout_repairs_applied.json:50 140-3:44 | ;  |  |
| 563 | pending | layout_repairs_applied.json:50 140-3:44 | ;  |  |
| 569 | pending | layout_repairs_applied.json:51 140-3:55; layout_repairs_applied.json:52 140-3:56 | ;  |  |
| 570 | pending | layout_repairs_applied.json:52 140-3:56 | ;  |  |
| 571 | pending | layout_before_sites.json:125 140-3:58 | ;  |  |
| 572 | pending | layout_before_sites.json:125 140-3:58; layout_before_sites.json:126 140-3:59 | ;  |  |
| 573 | pending | layout_before_sites.json:126 140-3:59 | ;  |  |
| 575 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 576 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 581 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 582 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 586 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 587 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 588 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 589 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 590 | pending | evenly spaced sample; layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75 | ;  |  |
| 591 | pending | layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75; layout_before_sites.json:133 140-3:76 | ;  |  |
| 592 | pending | layout_before_sites.json:133 140-3:76 | ;  |  |
| 599 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:53 140-3:85; layout_repairs_applied.json:54 140-3:85; layout_repairs_applied.json:55 140-3:85; layout_repairs_applied.json:56 140-3:85; layout_repairs_applied.json:57 140-3:85; layout_repairs_applied.json:58 140-3:85; layout_repairs_applied.json:59 140-3:85 | ;  |  |
| 600 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:53 140-3:85; layout_repairs_applied.json:54 140-3:85; layout_repairs_applied.json:55 140-3:85; layout_repairs_applied.json:56 140-3:85; layout_repairs_applied.json:57 140-3:85; layout_repairs_applied.json:58 140-3:85; layout_repairs_applied.json:59 140-3:85 | ;  |  |
| 601 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_before_sites.json:136 140-3:86; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:53 140-3:85; layout_repairs_applied.json:54 140-3:85; layout_repairs_applied.json:55 140-3:85; layout_repairs_applied.json:56 140-3:85; layout_repairs_applied.json:57 140-3:85; layout_repairs_applied.json:58 140-3:85; layout_repairs_applied.json:59 140-3:85 | ;  |  |
| 602 | pending | layout_before_sites.json:136 140-3:86; layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87 | ;  |  |
| 603 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87 | ;  |  |
| 604 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:60 140-3:88 | ;  |  |
| 605 | pending | layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:60 140-3:88 | ;  |  |
| 606 | pending | layout_before_sites.json:139 140-3:90 | ;  |  |
| 607 | pending | layout_before_sites.json:139 140-3:90 | ;  |  |
| 608 | pending | layout_before_sites.json:139 140-3:90; layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91 | ;  |  |
| 609 | pending | layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91; layout_before_sites.json:145 140-3:92 | ;  |  |
| 610 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 611 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 613 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 614 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 615 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95; layout_repairs_applied.json:61 140-3:97; layout_repairs_applied.json:67 140-3:97 | ;  |  |
| 616 | pending | layout_repairs_applied.json:61 140-3:97; layout_repairs_applied.json:67 140-3:97 | ;  |  |
| 617 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98; layout_repairs_applied.json:61 140-3:97; layout_repairs_applied.json:67 140-3:97 | ;  |  |
| 618 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98 | ;  |  |
| 625 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 626 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 627 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 630 | pending | evenly spaced sample | ;  |  |
| 631 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 632 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 641 | pending | layout_repairs_applied.json:68 140-3:121 | ;  |  |
| 642 | pending | layout_repairs_applied.json:68 140-3:121 | ;  |  |
| 669 | pending | evenly spaced sample; layout_before_sites.json:154 140-3:148 | ;  |  |
| 670 | pending | layout_before_sites.json:154 140-3:148 | ;  |  |
| 675 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 676 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 679 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 680 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 705 | pending | layout_before_sites.json:157 140-3:185 | ;  |  |
| 706 | pending | layout_before_sites.json:157 140-3:185; layout_repairs_applied.json:69 140-3:186 | ;  |  |
| 707 | pending | layout_repairs_applied.json:69 140-3:186 | ;  |  |
| 708 | pending | evenly spaced sample | ;  |  |
| 711 | pending | layout_before_sites.json:158 140-3:191; layout_before_sites.json:159 140-3:191; layout_before_sites.json:160 140-3:192 | ;  |  |
| 712 | pending | layout_before_sites.json:160 140-3:192 | ;  |  |
| 713 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 714 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 718 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 719 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 727 | pending | layout_repairs_applied.json:70 140-3:208 | ;  |  |
| 728 | pending | layout_repairs_applied.json:70 140-3:208; layout_repairs_applied.json:71 140-3:209 | ;  |  |
| 729 | pending | layout_repairs_applied.json:71 140-3:209 | ;  |  |
| 731 | pending | layout_before_sites.json:164 140-3:212 | ;  |  |
| 732 | pending | layout_before_sites.json:164 140-3:212; layout_before_sites.json:165 140-3:213 | ;  |  |
| 733 | pending | layout_before_sites.json:165 140-3:213 | ;  |  |
| 734 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 735 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 740 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_repairs_applied.json:72 140-3:221 | ;  |  |
| 741 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_repairs_applied.json:72 140-3:221 | ;  |  |
| 742 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_before_sites.json:169 140-3:222; layout_repairs_applied.json:72 140-3:221 | ;  |  |
| 743 | pending | layout_before_sites.json:169 140-3:222 | ;  |  |
| 747 | pending | evenly spaced sample | ;  |  |
| 751 | pending | layout_before_sites.json:170 140-3:231 | ;  |  |
| 752 | pending | layout_before_sites.json:170 140-3:231; layout_before_sites.json:171 140-3:232 | ;  |  |
| 753 | pending | layout_before_sites.json:171 140-3:232 | ;  |  |
| 763 | pending | layout_repairs_applied.json:73 140-3:245 | ;  |  |
| 764 | pending | layout_repairs_applied.json:73 140-3:245 | ;  |  |
| 775 | pending | layout_repairs_applied.json:74 140-3:261 | ;  |  |
| 776 | pending | layout_repairs_applied.json:74 140-3:261 | ;  |  |
| 777 | pending | layout_repairs_applied.json:74 140-3:261 | ;  |  |
| 787 | pending | evenly spaced sample | ;  |  |
| 789 | pending | layout_repairs_applied.json:75 140-3:275 | ;  |  |
| 790 | pending | layout_repairs_applied.json:75 140-3:275 | ;  |  |
| 795 | pending | layout_before_sites.json:172 140-3:282 | ;  |  |
| 796 | pending | layout_before_sites.json:172 140-3:282; layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 797 | pending | layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 798 | pending | layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 818 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 819 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 826 | pending | evenly spaced sample | ;  |  |
| 835 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:76 140-3:320 | ;  |  |
| 836 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:76 140-3:320 | ;  |  |
| 837 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:76 140-3:320 | ;  |  |
| 839 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 840 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 843 | pending | layout_before_sites.json:179 140-3:327 | ;  |  |
| 844 | pending | layout_before_sites.json:179 140-3:327; layout_before_sites.json:180 140-3:328; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:77 140-3:328 | ;  |  |
| 845 | pending | layout_before_sites.json:180 140-3:328; layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:73 140-3:329; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:77 140-3:328; layout_repairs_applied.json:78 140-3:329 | ;  |  |
| 846 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:78 140-3:329 | ;  |  |
| 847 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:78 140-3:329 | ;  |  |
| 851 | pending | layout_before_sites.json:182 140-3:334 | ;  |  |
| 852 | pending | layout_before_sites.json:182 140-3:334 | ;  |  |
| 853 | pending | layout_before_sites.json:182 140-3:334; layout_repairs_applied.json:80 140-3:335 | ;  |  |
| 854 | pending | layout_repairs_applied.json:80 140-3:335 | ;  |  |
| 865 | pending | evenly spaced sample; layout_before_sites.json:183 140-3:346 | ;  |  |
| 866 | pending | layout_before_sites.json:183 140-3:346 | ;  |  |
| 874 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 875 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 878 | pending | layout_before_sites.json:185 140-3:356 | ;  |  |
| 879 | pending | layout_before_sites.json:185 140-3:356; layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357 | ;  |  |
| 880 | pending | layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357; layout_repairs_applied.json:81 140-3:358 | ;  |  |
| 881 | pending | layout_repairs_applied.json:81 140-3:358 | ;  |  |
| 882 | pending | layout_repairs_applied.json:81 140-3:358 | ;  |  |
| 885 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362 | ;  |  |
| 886 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362; layout_repairs_applied.json:84 140-3:363 | ;  |  |
| 887 | pending | layout_repairs_applied.json:84 140-3:363 | ;  |  |
| 888 | pending | layout_repairs_applied.json:84 140-3:363 | ;  |  |
| 903 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 904 | pending | evenly spaced sample | ;  |  |
| 914 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 915 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 934 | pending | layout_repairs_applied.json:91 140-3:408; layout_repairs_applied.json:92 140-3:408; layout_repairs_applied.json:93 140-3:408 | ;  |  |
| 935 | pending | layout_repairs_applied.json:91 140-3:408; layout_repairs_applied.json:92 140-3:408; layout_repairs_applied.json:93 140-3:408 | ;  |  |
| 937 | pending | layout_repairs_applied.json:94 140-3:410 | ;  |  |
| 938 | pending | layout_repairs_applied.json:94 140-3:410 | ;  |  |
| 940 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 941 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 942 | pending | layout_before_sites.json:192 140-3:415 | ;  |  |
| 943 | pending | layout_before_sites.json:192 140-3:415 | ;  |  |
| 944 | pending | evenly spaced sample; layout_before_sites.json:192 140-3:415; layout_before_sites.json:193 140-3:416 | ;  |  |
| 945 | pending | layout_before_sites.json:193 140-3:416 | ;  |  |
| 947 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:98 140-3:419 | ;  |  |
| 948 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:98 140-3:419 | ;  |  |
| 953 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:95 140-3:425 | ;  |  |
| 954 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:95 140-3:425 | ;  |  |
| 955 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:95 140-3:425 | ;  |  |
| 957 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 958 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 959 | pending | layout_before_sites.json:197 140-3:431 | ;  |  |
| 960 | pending | layout_before_sites.json:197 140-3:431 | ;  |  |
| 961 | pending | layout_before_sites.json:197 140-3:431; layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432 | ;  |  |
| 962 | pending | layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432; layout_before_sites.json:200 140-3:433 | ;  |  |
| 963 | pending | layout_before_sites.json:200 140-3:433 | ;  |  |
| 964 | pending | layout_before_sites.json:200 140-3:433 | ;  |  |
| 966 | pending | layout_repairs_applied.json:107 140-3:436; layout_repairs_applied.json:108 140-3:436; layout_repairs_applied.json:109 140-3:436 | ;  |  |
| 967 | pending | layout_repairs_applied.json:107 140-3:436; layout_repairs_applied.json:108 140-3:436; layout_repairs_applied.json:109 140-3:436 | ;  |  |
| 968 | pending | layout_repairs_applied.json:107 140-3:436; layout_repairs_applied.json:108 140-3:436; layout_repairs_applied.json:109 140-3:436; layout_repairs_applied.json:110 140-3:437; layout_repairs_applied.json:111 140-3:437 | ;  |  |
| 969 | pending | layout_repairs_applied.json:110 140-3:437; layout_repairs_applied.json:111 140-3:437; layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438 | ;  |  |
| 970 | pending | layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438 | ;  |  |
| 971 | pending | layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438; layout_repairs_applied.json:116 140-3:439 | ;  |  |
| 972 | pending | layout_repairs_applied.json:103 140-3:441; layout_repairs_applied.json:116 140-3:439; layout_repairs_applied.json:117 140-3:440; layout_repairs_applied.json:99 140-3:440 | ;  |  |
| 973 | pending | layout_repairs_applied.json:103 140-3:441 | ;  |  |
| 974 | pending | layout_repairs_applied.json:103 140-3:441; layout_repairs_applied.json:106 140-3:443 | ;  |  |
| 975 | pending | layout_before_sites.json:201 140-3:444; layout_repairs_applied.json:106 140-3:443 | ;  |  |
| 976 | pending | layout_before_sites.json:201 140-3:444 | ;  |  |
| 978 | pending | layout_pass_sites.json:12 140-3:446; layout_repairs_applied.json:101 140-3:446 | ;  |  |
| 979 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:12 140-3:446; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:100 140-3:448; layout_repairs_applied.json:101 140-3:446 | ;  |  |
| 980 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:100 140-3:448; layout_repairs_applied.json:104 140-3:449; layout_repairs_applied.json:105 140-3:449 | ;  |  |
| 981 | pending | layout_repairs_applied.json:104 140-3:449; layout_repairs_applied.json:105 140-3:449 | ;  |  |
| 982 | pending | layout_repairs_applied.json:104 140-3:449; layout_repairs_applied.json:105 140-3:449 | ;  |  |
| 983 | pending | evenly spaced sample | ;  |  |
| 985 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 986 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 987 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 991 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 992 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 993 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 995 | pending | layout_repairs_applied.json:118 140-3:462 | ;  |  |
| 996 | pending | layout_repairs_applied.json:118 140-3:462; layout_repairs_applied.json:119 140-3:463; layout_repairs_applied.json:120 140-3:463; layout_repairs_applied.json:121 140-3:463 | ;  |  |
| 997 | pending | layout_repairs_applied.json:119 140-3:463; layout_repairs_applied.json:120 140-3:463; layout_repairs_applied.json:121 140-3:463 | ;  |  |
| 998 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 999 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 1000 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 1001 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 1002 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 1003 | pending | layout_before_sites.json:208 140-3:468; layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 1004 | pending | layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 1013 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 1014 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 1015 | pending | layout_before_sites.json:211 140-3:479; layout_repairs_applied.json:122 140-3:480; layout_repairs_applied.json:123 140-3:480 | ;  |  |
| 1016 | pending | layout_repairs_applied.json:122 140-3:480; layout_repairs_applied.json:123 140-3:480 | ;  |  |
| 1019 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1020 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1021 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1022 | pending | evenly spaced sample | ;  |  |
| 1023 | pending | layout_before_sites.json:213 140-3:491 | ;  |  |
| 1024 | pending | layout_before_sites.json:213 140-3:491 | ;  |  |
| 1025 | pending | layout_before_sites.json:213 140-3:491; layout_before_sites.json:214 140-3:492 | ;  |  |
| 1026 | pending | layout_before_sites.json:214 140-3:492; layout_repairs_applied.json:124 140-3:494 | ;  |  |
| 1027 | pending | layout_repairs_applied.json:124 140-3:494 | ;  |  |
| 1032 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 1033 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 1037 | pending | layout_repairs_applied.json:126 140-3:503 | ;  |  |
| 1038 | pending | layout_repairs_applied.json:126 140-3:503 | ;  |  |
| 1041 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:127 140-3:506; layout_repairs_applied.json:128 140-3:506 | ;  |  |
| 1042 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:127 140-3:506; layout_repairs_applied.json:128 140-3:506 | ;  |  |
| 1043 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:127 140-3:506; layout_repairs_applied.json:128 140-3:506 | ;  |  |
| 1045 | pending | layout_before_sites.json:217 140-3:509 | ;  |  |
| 1046 | pending | layout_before_sites.json:217 140-3:509; layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1047 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1048 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1052 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 1053 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 1056 | pending | layout_before_sites.json:221 140-3:517 | ;  |  |
| 1057 | pending | layout_before_sites.json:221 140-3:517; layout_before_sites.json:222 140-3:518 | ;  |  |
| 1058 | pending | layout_before_sites.json:222 140-3:518; layout_before_sites.json:223 140-3:519; layout_repairs_applied.json:129 140-3:519; layout_repairs_applied.json:134 140-3:519 | ;  |  |
| 1059 | pending | layout_before_sites.json:223 140-3:519; layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:129 140-3:519; layout_repairs_applied.json:133 140-3:520; layout_repairs_applied.json:134 140-3:519 | ;  |  |
| 1060 | pending | layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:133 140-3:520 | ;  |  |
| 1062 | pending | evenly spaced sample; layout_before_sites.json:225 140-3:522 | ;  |  |
| 1063 | pending | layout_before_sites.json:225 140-3:522 | ;  |  |
| 1064 | pending | layout_before_sites.json:225 140-3:522; layout_repairs_applied.json:135 140-3:523 | ;  |  |
| 1065 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:135 140-3:523; layout_repairs_applied.json:136 140-3:524; layout_repairs_applied.json:137 140-3:524 | ;  |  |
| 1066 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:130 140-3:525; layout_repairs_applied.json:136 140-3:524; layout_repairs_applied.json:137 140-3:524; layout_repairs_applied.json:138 140-3:525; layout_repairs_applied.json:139 140-3:525 | ;  |  |
| 1067 | pending | layout_repairs_applied.json:130 140-3:525; layout_repairs_applied.json:138 140-3:525; layout_repairs_applied.json:139 140-3:525 | ;  |  |
| 1072 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530 | ;  |  |
| 1073 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530; layout_before_sites.json:229 140-3:531 | ;  |  |
| 1074 | pending | layout_before_sites.json:229 140-3:531 | ;  |  |
| 1075 | pending | layout_before_sites.json:229 140-3:531; layout_before_sites.json:230 140-3:532 | ;  |  |
| 1076 | pending | layout_before_sites.json:230 140-3:532; layout_before_sites.json:231 140-3:533 | ;  |  |
| 1077 | pending | layout_before_sites.json:231 140-3:533; layout_before_sites.json:232 140-3:534 | ;  |  |
| 1078 | pending | layout_before_sites.json:232 140-3:534 | ;  |  |
| 1079 | pending | layout_before_sites.json:232 140-3:534; layout_before_sites.json:233 140-3:535 | ;  |  |
| 1080 | pending | layout_before_sites.json:233 140-3:535; layout_before_sites.json:234 140-3:536; layout_repairs_applied.json:140 140-3:536 | ;  |  |
| 1081 | pending | layout_before_sites.json:234 140-3:536; layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_repairs_applied.json:140 140-3:536 | ;  |  |
| 1082 | pending | layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_before_sites.json:238 140-3:538; layout_before_sites.json:239 140-3:539 | ;  |  |
| 1083 | pending | layout_before_sites.json:239 140-3:539; layout_before_sites.json:240 140-3:540 | ;  |  |
| 1084 | pending | layout_before_sites.json:240 140-3:540 | ;  |  |
| 1085 | pending | layout_before_sites.json:240 140-3:540; layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 1086 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 1087 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541; layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:141 140-3:542; layout_repairs_applied.json:145 140-3:542 | ;  |  |
| 1088 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:141 140-3:542; layout_repairs_applied.json:145 140-3:542 | ;  |  |
| 1089 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_before_sites.json:245 140-3:543; layout_repairs_applied.json:141 140-3:542; layout_repairs_applied.json:145 140-3:542; layout_repairs_applied.json:146 140-3:543; layout_repairs_applied.json:147 140-3:543; layout_repairs_applied.json:148 140-3:543 | ;  |  |
| 1090 | pending | layout_before_sites.json:245 140-3:543; layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:146 140-3:543; layout_repairs_applied.json:147 140-3:543; layout_repairs_applied.json:148 140-3:543; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544 | ;  |  |
| 1091 | pending | layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544 | ;  |  |
| 1092 | pending | layout_before_sites.json:246 140-3:544; layout_before_sites.json:247 140-3:545; layout_repairs_applied.json:142 140-3:545; layout_repairs_applied.json:143 140-3:545; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544; layout_repairs_applied.json:151 140-3:545; layout_repairs_applied.json:152 140-3:545; layout_repairs_applied.json:153 140-3:545; layout_repairs_applied.json:154 140-3:545; layout_repairs_applied.json:155 140-3:545; layout_repairs_applied.json:156 140-3:545 | ;  |  |
| 1093 | pending | layout_before_sites.json:247 140-3:545; layout_before_sites.json:248 140-3:546; layout_repairs_applied.json:142 140-3:545; layout_repairs_applied.json:143 140-3:545; layout_repairs_applied.json:144 140-3:546; layout_repairs_applied.json:151 140-3:545; layout_repairs_applied.json:152 140-3:545; layout_repairs_applied.json:153 140-3:545; layout_repairs_applied.json:154 140-3:545; layout_repairs_applied.json:155 140-3:545; layout_repairs_applied.json:156 140-3:545 | ;  |  |
| 1094 | pending | layout_before_sites.json:248 140-3:546; layout_repairs_applied.json:144 140-3:546 | ;  |  |
| 1095 | pending | layout_before_sites.json:248 140-3:546; layout_before_sites.json:249 140-3:547; layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:144 140-3:546; layout_repairs_applied.json:157 140-3:548 | ;  |  |
| 1096 | pending | layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:157 140-3:548 | ;  |  |
| 1101 | pending | evenly spaced sample; layout_before_sites.json:251 140-3:554; layout_repairs_applied.json:158 140-3:554 | ;  |  |
| 1102 | pending | layout_before_sites.json:251 140-3:554; layout_before_sites.json:252 140-3:555; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:158 140-3:554; layout_repairs_applied.json:159 140-3:555 | ;  |  |
| 1103 | pending | layout_before_sites.json:252 140-3:555; layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:159 140-3:555; layout_repairs_applied.json:160 140-3:556 | ;  |  |
| 1104 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_repairs_applied.json:160 140-3:556 | ;  |  |
| 1105 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_repairs_applied.json:160 140-3:556 | ;  |  |
| 1106 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_before_sites.json:255 140-3:557; layout_before_sites.json:256 140-3:558; layout_pass_sites.json:14 140-3:557; layout_pass_sites.json:75 140-3:557; layout_repairs_applied.json:160 140-3:556; layout_repairs_applied.json:162 140-3:557 | ;  |  |
| 1107 | pending | layout_before_sites.json:256 140-3:558; layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1108 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1109 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1111 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:163 140-3:561 | ;  |  |
| 1112 | pending | landscape page; layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:163 140-3:561 | ;  |  |
| 1113 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:163 140-3:561 | ;  |  |
| 1114 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:161 140-3:562; layout_repairs_applied.json:163 140-3:561; layout_repairs_applied.json:166 140-3:562; layout_repairs_applied.json:167 140-3:562 | ;  |  |
| 1115 | pending | layout_repairs_applied.json:161 140-3:562; layout_repairs_applied.json:166 140-3:562; layout_repairs_applied.json:167 140-3:562 | ;  |  |
| 1117 | pending | layout_repairs_applied.json:168 140-3:565 | ;  |  |
| 1118 | pending | layout_repairs_applied.json:168 140-3:565 | ;  |  |
| 1119 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567 | ;  |  |
| 1120 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567 | ;  |  |
| 1121 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567; layout_repairs_applied.json:169 140-3:568 | ;  |  |
| 1122 | pending | layout_repairs_applied.json:169 140-3:568 | ;  |  |
| 1124 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 1125 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 1127 | pending | layout_before_sites.json:263 140-3:573; layout_repairs_applied.json:170 140-3:573 | ;  |  |
| 1128 | pending | layout_before_sites.json:263 140-3:573; layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:170 140-3:573; layout_repairs_applied.json:171 140-3:574 | ;  |  |
| 1129 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:171 140-3:574 | ;  |  |
| 1130 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:171 140-3:574 | ;  |  |
| 1131 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:171 140-3:574; layout_repairs_applied.json:173 140-3:575 | ;  |  |
| 1132 | pending | layout_before_sites.json:265 140-3:577; layout_repairs_applied.json:173 140-3:575 | ;  |  |
| 1133 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 1134 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 1139 | pending | layout_before_sites.json:266 140-3:582 | ;  |  |
| 1140 | pending | evenly spaced sample; layout_before_sites.json:266 140-3:582 | ;  |  |
| 1142 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 1143 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 1144 | pending | layout_before_sites.json:267 140-3:585; layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 1145 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 1146 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586; layout_before_sites.json:270 140-3:587 | ;  |  |
| 1147 | pending | layout_before_sites.json:270 140-3:587 | ;  |  |
| 1148 | pending | layout_before_sites.json:270 140-3:587; layout_before_sites.json:271 140-3:588 | ;  |  |
| 1149 | pending | layout_before_sites.json:271 140-3:588 | ;  |  |
| 1150 | pending | layout_before_sites.json:271 140-3:588; layout_before_sites.json:272 140-3:589 | ;  |  |
| 1151 | pending | layout_before_sites.json:272 140-3:589; layout_repairs_applied.json:175 140-3:590 | ;  |  |
| 1152 | pending | layout_repairs_applied.json:175 140-3:590 | ;  |  |
| 1154 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 1155 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 1161 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 1162 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 1169 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:176 140-3:606 | ;  |  |
| 1170 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:176 140-3:606 | ;  |  |
| 1171 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:176 140-3:606 | ;  |  |
| 1173 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:178 140-3:609 | ;  |  |
| 1174 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:178 140-3:609 | ;  |  |
| 1179 | pending | evenly spaced sample; layout_before_sites.json:275 140-3:616 | ;  |  |
| 1180 | pending | layout_before_sites.json:275 140-3:616; layout_before_sites.json:276 140-3:617 | ;  |  |
| 1181 | pending | layout_before_sites.json:276 140-3:617 | ;  |  |
| 1182 | pending | layout_before_sites.json:276 140-3:617 | ;  |  |
| 1183 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:179 140-3:619 | ;  |  |
| 1184 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:179 140-3:619 | ;  |  |
| 1185 | pending | layout_before_sites.json:278 140-3:621; layout_pass_sites.json:18 140-3:621; layout_repairs_applied.json:177 140-3:621; layout_repairs_applied.json:184 140-3:621 | ;  |  |
| 1186 | pending | layout_before_sites.json:278 140-3:621; layout_pass_sites.json:18 140-3:621; layout_repairs_applied.json:177 140-3:621; layout_repairs_applied.json:184 140-3:621; layout_repairs_applied.json:185 140-3:622; layout_repairs_applied.json:186 140-3:622; layout_repairs_applied.json:187 140-3:622; layout_repairs_applied.json:188 140-3:622; layout_repairs_applied.json:189 140-3:622 | ;  |  |
| 1187 | pending | layout_repairs_applied.json:185 140-3:622; layout_repairs_applied.json:186 140-3:622; layout_repairs_applied.json:187 140-3:622; layout_repairs_applied.json:188 140-3:622; layout_repairs_applied.json:189 140-3:622; layout_repairs_applied.json:190 140-3:623; layout_repairs_applied.json:191 140-3:623 | ;  |  |
| 1188 | pending | layout_repairs_applied.json:190 140-3:623; layout_repairs_applied.json:191 140-3:623 | ;  |  |
| 1190 | pending | layout_before_sites.json:279 140-3:625 | ;  |  |
| 1191 | pending | layout_before_sites.json:279 140-3:625 | ;  |  |
| 1192 | pending | layout_before_sites.json:280 140-3:627 | ;  |  |
| 1193 | pending | layout_before_sites.json:280 140-3:627; layout_repairs_applied.json:192 140-3:628 | ;  |  |
| 1194 | pending | layout_before_sites.json:281 140-3:629; layout_repairs_applied.json:192 140-3:628 | ;  |  |
| 1195 | pending | layout_before_sites.json:281 140-3:629 | ;  |  |
| 1196 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 1197 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 1201 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:194 140-3:637; layout_repairs_applied.json:196 140-3:637 | ;  |  |
| 1202 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:193 140-3:638; layout_repairs_applied.json:194 140-3:637; layout_repairs_applied.json:196 140-3:637 | ;  |  |
| 1203 | pending | layout_repairs_applied.json:193 140-3:638 | ;  |  |
| 1213 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:207 140-3:649 | ;  |  |
| 1214 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:207 140-3:649 | ;  |  |
| 1217 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:197 140-3:653; layout_repairs_applied.json:208 140-3:653 | ;  |  |
| 1218 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:197 140-3:653; layout_repairs_applied.json:208 140-3:653 | ;  |  |
| 1219 | pending | evenly spaced sample; layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:197 140-3:653; layout_repairs_applied.json:208 140-3:653 | ;  |  |
| 1222 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:209 140-3:656; layout_repairs_applied.json:210 140-3:656 | ;  |  |
| 1223 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:209 140-3:656; layout_repairs_applied.json:210 140-3:656 | ;  |  |
| 1224 | pending | layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657 | ;  |  |
| 1225 | pending | layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_repairs_applied.json:198 140-3:658; layout_repairs_applied.json:199 140-3:658 | ;  |  |
| 1226 | pending | layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:198 140-3:658; layout_repairs_applied.json:199 140-3:658; layout_repairs_applied.json:200 140-3:659; layout_repairs_applied.json:201 140-3:659 | ;  |  |
| 1227 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:200 140-3:659; layout_repairs_applied.json:201 140-3:659 | ;  |  |
| 1228 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:200 140-3:659; layout_repairs_applied.json:201 140-3:659; layout_repairs_applied.json:202 140-3:660 | ;  |  |
| 1229 | pending | layout_repairs_applied.json:202 140-3:660 | ;  |  |
| 1231 | pending | layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:203 140-3:662 | ;  |  |
| 1232 | pending | layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:203 140-3:662 | ;  |  |
| 1238 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 1239 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 1248 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 1249 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 1253 | pending | layout_repairs_applied.json:213 140-3:685; layout_repairs_applied.json:214 140-3:685 | ;  |  |
| 1254 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:213 140-3:685; layout_repairs_applied.json:214 140-3:685; layout_repairs_applied.json:215 140-3:686 | ;  |  |
| 1255 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:215 140-3:686 | ;  |  |
| 1257 | pending | layout_repairs_applied.json:216 140-3:688; layout_repairs_applied.json:217 140-3:688 | ;  |  |
| 1258 | pending | evenly spaced sample; layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:216 140-3:688; layout_repairs_applied.json:217 140-3:688; layout_repairs_applied.json:218 140-3:689 | ;  |  |
| 1259 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:218 140-3:689 | ;  |  |
| 1260 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:218 140-3:689 | ;  |  |
| 1263 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692 | ;  |  |
| 1264 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692; layout_repairs_applied.json:219 140-3:693; layout_repairs_applied.json:220 140-3:693 | ;  |  |
| 1265 | pending | layout_repairs_applied.json:219 140-3:693; layout_repairs_applied.json:220 140-3:693 | ;  |  |
| 1269 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 1270 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 1273 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1274 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1275 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1276 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1277 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1278 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1284 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:221 140-4:20 | ;  |  |
| 1285 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:221 140-4:20 | ;  |  |
| 1291 | pending | layout_before_sites.json:311 140-4:29 | ;  |  |
| 1292 | pending | layout_before_sites.json:311 140-4:29; layout_repairs_applied.json:223 140-4:31; layout_repairs_applied.json:224 140-4:31; layout_repairs_applied.json:225 140-4:31 | ;  |  |
| 1293 | pending | layout_repairs_applied.json:223 140-4:31; layout_repairs_applied.json:224 140-4:31; layout_repairs_applied.json:225 140-4:31; layout_repairs_applied.json:226 140-4:32; layout_repairs_applied.json:227 140-4:32 | ;  |  |
| 1294 | pending | layout_repairs_applied.json:226 140-4:32; layout_repairs_applied.json:227 140-4:32; layout_repairs_applied.json:228 140-4:33 | ;  |  |
| 1295 | pending | layout_repairs_applied.json:228 140-4:33 | ;  |  |
| 1296 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:228 140-4:33 | ;  |  |
| 1297 | pending | evenly spaced sample; layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34 | ;  |  |
| 1298 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:229 140-4:35; layout_repairs_applied.json:230 140-4:35 | ;  |  |
| 1299 | pending | layout_repairs_applied.json:229 140-4:35; layout_repairs_applied.json:230 140-4:35 | ;  |  |
| 1303 | pending | layout_before_sites.json:314 140-4:39 | ;  |  |
| 1304 | pending | layout_before_sites.json:314 140-4:39; layout_before_sites.json:315 140-4:40 | ;  |  |
| 1305 | pending | layout_before_sites.json:315 140-4:40; layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41 | ;  |  |
| 1306 | pending | layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41; layout_before_sites.json:318 140-4:42 | ;  |  |
| 1307 | pending | layout_before_sites.json:318 140-4:42; layout_before_sites.json:319 140-4:43 | ;  |  |
| 1308 | pending | layout_before_sites.json:319 140-4:43; layout_before_sites.json:320 140-4:44; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:231 140-4:44 | ;  |  |
| 1309 | pending | layout_before_sites.json:320 140-4:44; layout_before_sites.json:321 140-4:45; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:231 140-4:44 | ;  |  |
| 1310 | pending | layout_before_sites.json:321 140-4:45; layout_before_sites.json:322 140-4:46 | ;  |  |
| 1311 | pending | layout_before_sites.json:322 140-4:46; layout_before_sites.json:323 140-4:47 | ;  |  |
| 1312 | pending | layout_before_sites.json:323 140-4:47 | ;  |  |
| 1313 | pending | layout_before_sites.json:323 140-4:47; layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48 | ;  |  |
| 1314 | pending | layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48; layout_before_sites.json:327 140-4:49 | ;  |  |
| 1315 | pending | layout_before_sites.json:327 140-4:49; layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 1316 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 1317 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50; layout_before_sites.json:331 140-4:51 | ;  |  |
| 1318 | pending | layout_before_sites.json:331 140-4:51; layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52 | ;  |  |
| 1319 | pending | layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52 | ;  |  |
| 1320 | pending | layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52; layout_before_sites.json:334 140-4:53; layout_before_sites.json:335 140-4:54 | ;  |  |
| 1321 | pending | layout_before_sites.json:335 140-4:54; layout_before_sites.json:336 140-4:55 | ;  |  |
| 1322 | pending | layout_before_sites.json:336 140-4:55; layout_before_sites.json:337 140-4:56 | ;  |  |
| 1323 | pending | layout_before_sites.json:337 140-4:56 | ;  |  |
| 1324 | pending | layout_before_sites.json:337 140-4:56; layout_before_sites.json:338 140-4:57 | ;  |  |
| 1325 | pending | layout_before_sites.json:338 140-4:57 | ;  |  |
| 1326 | pending | layout_repairs_applied.json:244 140-4:59 | ;  |  |
| 1327 | pending | layout_repairs_applied.json:244 140-4:59 | ;  |  |
| 1328 | pending | layout_repairs_applied.json:245 140-4:61; layout_repairs_applied.json:246 140-4:61; layout_repairs_applied.json:247 140-4:61; layout_repairs_applied.json:248 140-4:61 | ;  |  |
| 1329 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:245 140-4:61; layout_repairs_applied.json:246 140-4:61; layout_repairs_applied.json:247 140-4:61; layout_repairs_applied.json:248 140-4:61; layout_repairs_applied.json:249 140-4:62 | ;  |  |
| 1330 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:249 140-4:62 | ;  |  |
| 1332 | pending | layout_repairs_applied.json:242 140-4:65 | ;  |  |
| 1333 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:233 140-4:66; layout_repairs_applied.json:234 140-4:66; layout_repairs_applied.json:235 140-4:66; layout_repairs_applied.json:242 140-4:65 | ;  |  |
| 1334 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:233 140-4:66; layout_repairs_applied.json:234 140-4:66; layout_repairs_applied.json:235 140-4:66 | ;  |  |
| 1335 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_before_sites.json:343 140-4:67; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:233 140-4:66; layout_repairs_applied.json:234 140-4:66; layout_repairs_applied.json:235 140-4:66 | ;  |  |
| 1336 | pending | layout_before_sites.json:343 140-4:67 | ;  |  |
| 1337 | pending | evenly spaced sample; layout_before_sites.json:344 140-4:70 | ;  |  |
| 1338 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 1339 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 1343 | pending | layout_repairs_applied.json:250 140-4:74 | ;  |  |
| 1344 | pending | layout_repairs_applied.json:250 140-4:74 | ;  |  |
| 1345 | pending | layout_repairs_applied.json:243 140-4:75; layout_repairs_applied.json:250 140-4:74; layout_repairs_applied.json:251 140-4:75; layout_repairs_applied.json:252 140-4:75; layout_repairs_applied.json:253 140-4:75 | ;  |  |
| 1346 | pending | layout_repairs_applied.json:243 140-4:75; layout_repairs_applied.json:251 140-4:75; layout_repairs_applied.json:252 140-4:75; layout_repairs_applied.json:253 140-4:75 | ;  |  |
| 1347 | pending | layout_repairs_applied.json:243 140-4:75; layout_repairs_applied.json:251 140-4:75; layout_repairs_applied.json:252 140-4:75; layout_repairs_applied.json:253 140-4:75; layout_repairs_applied.json:254 140-4:76; layout_repairs_applied.json:255 140-4:76 | ;  |  |
| 1348 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:254 140-4:76; layout_repairs_applied.json:255 140-4:76; layout_repairs_applied.json:258 140-4:77 | ;  |  |
| 1349 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:258 140-4:77 | ;  |  |
| 1350 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:258 140-4:77; layout_repairs_applied.json:259 140-4:78; layout_repairs_applied.json:260 140-4:78 | ;  |  |
| 1351 | pending | layout_repairs_applied.json:259 140-4:78; layout_repairs_applied.json:260 140-4:78; layout_repairs_applied.json:261 140-4:79; layout_repairs_applied.json:262 140-4:79 | ;  |  |
| 1352 | pending | layout_repairs_applied.json:261 140-4:79; layout_repairs_applied.json:262 140-4:79; layout_repairs_applied.json:263 140-4:80 | ;  |  |
| 1353 | pending | layout_repairs_applied.json:263 140-4:80 | ;  |  |
| 1354 | pending | layout_repairs_applied.json:263 140-4:80; layout_repairs_applied.json:264 140-4:81; layout_repairs_applied.json:265 140-4:81 | ;  |  |
| 1355 | pending | layout_repairs_applied.json:264 140-4:81; layout_repairs_applied.json:265 140-4:81 | ;  |  |
| 1366 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1367 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1368 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1373 | pending | layout_repairs_applied.json:269 140-4:96; layout_repairs_applied.json:270 140-4:96 | ;  |  |
| 1374 | pending | layout_repairs_applied.json:269 140-4:96; layout_repairs_applied.json:270 140-4:96; layout_repairs_applied.json:271 140-4:97; layout_repairs_applied.json:272 140-4:97 | ;  |  |
| 1375 | pending | layout_repairs_applied.json:271 140-4:97; layout_repairs_applied.json:272 140-4:97; layout_repairs_applied.json:273 140-4:98 | ;  |  |
| 1376 | pending | evenly spaced sample; layout_repairs_applied.json:273 140-4:98 | ;  |  |
| 1377 | pending | layout_before_sites.json:349 140-4:99; layout_repairs_applied.json:273 140-4:98 | ;  |  |
| 1378 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1379 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1380 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1381 | pending | layout_before_sites.json:350 140-4:101 | ;  |  |
| 1382 | pending | layout_before_sites.json:350 140-4:101; layout_before_sites.json:351 140-4:102 | ;  |  |
| 1383 | pending | layout_before_sites.json:351 140-4:102 | ;  |  |
| 1385 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 1386 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 1391 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:266 140-4:113 | ;  |  |
| 1392 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:266 140-4:113 | ;  |  |
| 1415 | pending | evenly spaced sample | ;  |  |
| 1417 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:274 140-4:136 | ;  |  |
| 1418 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:274 140-4:136 | ;  |  |
| 1425 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 1426 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 1427 | pending | layout_before_sites.json:356 140-4:149 | ;  |  |
| 1432 | pending | layout_before_sites.json:357 140-4:154 | ;  |  |
| 1446 | pending | layout_repairs_applied.json:276 140-4:172 | ;  |  |
| 1447 | pending | layout_repairs_applied.json:276 140-4:172; layout_repairs_applied.json:277 140-4:174 | ;  |  |
| 1448 | pending | layout_repairs_applied.json:277 140-4:174; layout_repairs_applied.json:278 140-4:175; layout_repairs_applied.json:279 140-4:175 | ;  |  |
| 1449 | pending | layout_repairs_applied.json:278 140-4:175; layout_repairs_applied.json:279 140-4:175 | ;  |  |
| 1453 | pending | layout_before_sites.json:358 140-4:181; layout_before_sites.json:359 140-4:181 | ;  |  |
| 1454 | pending | evenly spaced sample | ;  |  |
| 1456 | pending | layout_before_sites.json:360 140-4:186 | ;  |  |
| 1457 | pending | layout_before_sites.json:360 140-4:186; layout_before_sites.json:361 140-4:188 | ;  |  |
| 1458 | pending | layout_before_sites.json:361 140-4:188 | ;  |  |
| 1467 | pending | layout_repairs_applied.json:280 140-4:203; layout_repairs_applied.json:281 140-4:203 | ;  |  |
| 1468 | pending | layout_repairs_applied.json:282 140-4:205 | ;  |  |
| 1469 | pending | layout_repairs_applied.json:282 140-4:205 | ;  |  |
| 1489 | pending | layout_before_sites.json:362 140-4:230 | ;  |  |
| 1490 | pending | layout_before_sites.json:362 140-4:230 | ;  |  |
| 1494 | pending | evenly spaced sample | ;  |  |
| 1495 | pending | layout_before_sites.json:363 140-4:236 | ;  |  |
| 1496 | pending | layout_before_sites.json:363 140-4:236 | ;  |  |
| 1502 | pending | layout_before_sites.json:364 140-4:245 | ;  |  |
| 1505 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 1506 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 1507 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 1519 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 1520 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 1521 | pending | layout_before_sites.json:367 140-4:266 | ;  |  |
| 1522 | pending | layout_before_sites.json:367 140-4:266 | ;  |  |
| 1523 | pending | layout_before_sites.json:367 140-4:266; layout_before_sites.json:368 140-4:267 | ;  |  |
| 1524 | pending | layout_before_sites.json:368 140-4:267; layout_before_sites.json:369 140-4:268; layout_before_sites.json:370 140-4:269 | ;  |  |
| 1525 | pending | layout_before_sites.json:370 140-4:269; layout_before_sites.json:371 140-4:270 | ;  |  |
| 1526 | pending | layout_before_sites.json:371 140-4:270; layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:286 140-4:271; layout_repairs_applied.json:288 140-4:271 | ;  |  |
| 1527 | pending | layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_before_sites.json:374 140-4:272; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:286 140-4:271; layout_repairs_applied.json:288 140-4:271 | ;  |  |
| 1528 | pending | layout_before_sites.json:374 140-4:272; layout_before_sites.json:375 140-4:273; layout_before_sites.json:376 140-4:274 | ;  |  |
| 1529 | pending | layout_before_sites.json:376 140-4:274; layout_before_sites.json:377 140-4:275 | ;  |  |
| 1530 | pending | layout_before_sites.json:377 140-4:275; layout_before_sites.json:378 140-4:276; layout_repairs_applied.json:287 140-4:276 | ;  |  |
| 1531 | pending | layout_before_sites.json:378 140-4:276; layout_before_sites.json:379 140-4:277; layout_repairs_applied.json:287 140-4:276 | ;  |  |
| 1532 | pending | layout_before_sites.json:379 140-4:277; layout_before_sites.json:380 140-4:278; layout_before_sites.json:381 140-4:279 | ;  |  |
| 1533 | pending | evenly spaced sample; layout_before_sites.json:381 140-4:279; layout_before_sites.json:382 140-4:280 | ;  |  |

### LM_FR_texte_de_lecture.pdf

PDF SHA-256: `3f58bce5a063133f7052c517a6ac531f822fc57c149b63c46deb39890b74cf23`.

| Physical page | Status | Selection reason | Reviewer and inspection basis | Observation |
|---|---|---|---|---|
| 1 | reviewed | evenly spaced sample | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview001 actual inspection: French title, author, archive identification,1588-scan count and date are centered with generous spacing. No page-edge clipping or block-to-block collision is visible at this scale. |
| 6 | reviewed | layout_before_sites.json:1 140-1:4 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Boxed identities, the long expanded power calculation and lower exact sequence fit; the two short marginal notes are separate. |
| 7 | reviewed | layout_before_sites.json:1 140-1:4 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The conjugation computations and their underbraces remain legible, with the source-note block and right-margin annotations clear. |
| 9 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:5 140-1:10 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The tall branching diagram and the two upper sequences fit the page; the curved lower routes stay clear of the body text. |
| 10 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:5 140-1:10 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final 900px review: the scan10 branching diagram is contained; the pr_1 label is on the right portion of its horizontal arrow, clear of the diagonal that formerly crossed it. Dense map endpoints and retained-doubt list remain separate; targeted enlarged check queued.; At6x native vector resolution, pr_1 has clear white space from both the descending diagonal and horizontal arrow; the repaired label crossing is resolved. The source's separate physical slanting stroke at left remains preserved. |
| 11 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:3 140-1:12; layout_repairs_applied.json:5 140-1:10 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview001 actual inspection: Repaired C1:12 diagram and lower calculations are clearly separated. No page-edge clipping or block-to-block collision is visible at this scale.; At 900px, the scan12 vertical exact diagram has clear rows and node endpoints; adjacent parameter cases are contained. |
| 12 | reviewed | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:3 140-1:12 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview001 actual inspection: Nested underbrace calculation and marginal note fit above the retained-doubt list. No page-edge clipping or block-to-block collision is visible at this scale. |
| 13 | reviewed | layout_before_sites.json:8 140-1:15 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview001 actual inspection: Modular arithmetic calculations and small marginal maps fit. No page-edge clipping or block-to-block collision is visible at this scale. |
| 14 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:8 140-1:15; layout_before_sites.json:9 140-1:16 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview001 actual inspection: Manuscript administrative paragraphs, square and marginal notes fit. No page-edge clipping or block-to-block collision is visible at this scale. |
| 15 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:9 140-1:16 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview001 actual inspection: Small physical sketch, square and sparse cancelled-anchor strokes are contained. No page-edge clipping or block-to-block collision is visible at this scale. |
| 16 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:13 140-1:17; layout_before_sites.json:14 140-1:18; layout_before_sites.json:9 140-1:16; layout_pass_sites.json:31 140-1:18 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview001 actual inspection: Cancelled-note anchors leave isolated vertical markers; succeeding scalar formulas and retained doubts are separate. No page-edge clipping or block-to-block collision is visible at this scale. |
| 17 | reviewed | layout_before_sites.json:14 140-1:18; layout_before_sites.json:15 140-1:19; layout_pass_sites.json:31 140-1:18; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:54 140-1:19; layout_repairs_applied.json:4 140-1:19 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview001 actual inspection: Small exact diagram and note are contained above the scan19 start. No page-edge clipping or block-to-block collision is visible at this scale. |
| 18 | reviewed | layout_before_sites.json:15 140-1:19; layout_before_sites.json:16 140-1:20; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:54 140-1:19; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:13 140-1:20; layout_repairs_applied.json:4 140-1:19; layout_repairs_applied.json:8 140-1:20 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview001 actual inspection: Locally reduced physical drawing is contained, with long strokes and sphere visible; close view queued. No page-edge clipping or block-to-block collision is visible at this scale.; At 900px, the locally reduced physical drawing is contained, including the long right strokes. Its source drawing intersections and cancellation strokes are preserved; retained-doubt list remains separate. |
| 19 | reviewed | layout_before_sites.json:16 140-1:20; layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:13 140-1:20; layout_repairs_applied.json:8 140-1:20 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Actual900px page review: the large branching diagram and the two marginal-note blocks remain within the page; the Cart/canonical labels are separated at this scale, and the m35/m39 note headings remain attached to their content. |
| 20 | reviewed | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23; layout_repairs_applied.json:14 140-1:25 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The cohomology sequences and gamma formulas are complete; the retained-doubt block ends before B, which begins the next page. |
| 21 | reviewed | layout_repairs_applied.json:14 140-1:25 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | B and its full surviving paragraph remain together; the following M11 and groupoid diagrams fit, including both dashed separators. |
| 23 | reviewed | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Actual900px page review: the two extension diagrams, circular sketch, and later formula fragments remain within the measure; no overlap or clipping is visible. |
| 24 | reviewed | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Actual900px page review: note m51 stays with its formula content; the lower branching diagram is fully visible, with clear node placement and no new page-scale contact. |
| 25 | reviewed | evenly spaced sample; layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Actual900px review: the upper branching map, paired extension rows and lower inclusion are complete and separated; retained-doubt blocks below them fit without overlap. |
| 29 | reviewed | layout_before_sites.json:23 140-1:36; layout_before_sites.json:24 140-1:36; layout_pass_sites.json:34 140-1:36; layout_pass_sites.json:56 140-1:36; layout_repairs_applied.json:9 140-1:36 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Both multilevel group diagrams fit horizontally; the lower marginal note remains separate from the final arrow row. |
| 30 | reviewed | layout_before_sites.json:23 140-1:36; layout_before_sites.json:24 140-1:36; layout_pass_sites.json:34 140-1:36; layout_pass_sites.json:56 140-1:36; layout_repairs_applied.json:9 140-1:36 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The remaining short map and retained-doubt entries are fully visible; no content is cropped despite the sparse page. |
| 31 | reviewed | layout_before_sites.json:25 140-2:4 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Cote140-2 and its manuscript contents list remain readable with aligned page references and no text in the outer margin. |
| 32 | reviewed | layout_before_sites.json:25 140-2:4 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The contents continuation and opening topoi definitions fit; both marginal-note blocks keep their substantive text with the headings. |
| 41 | reviewed | layout_before_sites.json:26 140-2:28; layout_before_sites.json:27 140-2:29 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The product definitions, small homomorphism displays and three marginal-note blocks remain separated and within the page. |
| 42 | reviewed | layout_before_sites.json:27 140-2:29 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The four-functor diamond and listed conditions are clear; the lower triple of morphisms and right NB note fit. |
| 44 | reviewed | layout_before_sites.json:28 140-2:35 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The upper comparison square, compatibility prose and lower circled sketch remain readable; the short marginal note stays clear. |
| 45 | reviewed | layout_before_sites.json:28 140-2:35 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Boxed homomorphisms and note blocks are readable; the scan36 retained-doubt heading and both entries stay together, also checked natively. |
| 47 | reviewed | layout_before_sites.json:29 140-2:39 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The exact-sequence note diagram and boxed functors remain clear; no heading or rule is stranded at the page foot. |
| 49 | reviewed | layout_before_sites.json:30 140-2:42 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The large commutative prism, its descriptive caption and both marginal-note blocks fit without clipping or visible text overlap. |
| 50 | reviewed | evenly spaced sample; layout_before_sites.json:30 140-2:42; layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The short categorical sequences and lower three-part circled sketch are fully visible; source-doubt blocks remain with their entries. |
| 51 | reviewed | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44; layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The two marginal-note blocks, inversion formulas, diamond diagram and boxed shortened sequence are complete and separated; the next scan begins with substantive prose and two short maps. |
| 52 | reviewed | layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The upper commutative ladder and its two note blocks remain distinct; the lower boxed basepoint formula and subsequent short maps fit without clipping. |
| 63 | reviewed | layout_before_sites.json:35 140-2:69 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The group-extension discussion, three retained-doubt blocks and lower boxed stabilizer identity fit; scan labels and daggers remain outside the equations. |
| 68 | reviewed | layout_before_sites.json:36 140-2:80 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The marginal double-stroke sketch is retained with its heading and comment; section 10 has its opening paragraph, and both short groupoid sequences fit above the final doubt block. |
| 71 | reviewed | layout_before_sites.json:37 140-2:88 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The extension paragraph and short groupoid note are readable; marginal note 196 keeps its circled e and long vertical sketch on the same page. |
| 72 | reviewed | layout_before_sites.json:37 140-2:88; layout_repairs_applied.json:15 140-2:89 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Section 12 stays with the surface definition and T display; the succeeding groupoid maps and the lower product relation remain complete. This heading site also passed the native closure check. |
| 74 | reviewed | evenly spaced sample | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The three successive groupoid/category sequences and lower group-extension formulas are legible, with separate doubt blocks and unobstructed scan marks. |
| 86 | reviewed | layout_before_sites.json:38 140-2:122 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The top branching diagram and explanatory bracket fit; the two lower fundamental-group diagrams are separated from their prose and retained-doubt entries. |
| 87 | reviewed | layout_before_sites.json:38 140-2:122 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The upper Galois branching diagram, kernel sequence and two lower cohomology maps fit; the final question continues as ordinary prose. |
| 90 | reviewed | layout_before_sites.json:39 140-2:130 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Both cohomology cases and the four-node diagram are clear; marginal notes 251–253 retain their text and do not collide with the displays. |
| 91 | reviewed | layout_before_sites.json:39 140-2:130 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The two-row topos diagram and orientation-module maps are complete; section 14 keeps a substantive opening paragraph and its short groupoid descriptions. |
| 95 | reviewed | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The theorem begins with its full introductory sentence and exact sequence; the split extension and class-of-sections display fit with separate doubt blocks. |
| 96 | reviewed | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The fundamental lemma and its two clauses are legible; its proof heading is followed on this page by the first substantive proof sentence after the retained doubts. |
| 98 | reviewed | evenly spaced sample; layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The fixed-point discussion, marginal note 261 and opening theorem text remain legible; the note and retained-doubt rules do not overlap body text. |
| 99 | reviewed | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The class-of-sections display, corollary and note 262 are complete, with the numbered conclusions and lower proof opening separated from their doubt blocks. |
| 103 | reviewed | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The exterior-power identity and quadratic polynomial fit; marginal note 275 keeps its double-stroke sketch and accompanying blue/red annotations with its heading. |
| 104 | reviewed | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The extension diagram, long map definition and section 16 opener fit; all three marginal-note blocks keep their content and rules separate. |
| 105 | reviewed | layout_before_sites.json:46 140-2:162 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The two branching diagrams and lower diamond are complete; intervening prose and doubt blocks have clear separation. |
| 106 | reviewed | layout_before_sites.json:47 140-2:164; layout_before_sites.json:48 140-2:165; layout_repairs_applied.json:17 140-2:165 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Both topos diamonds and the short commutation map are legible, with lower diagram fully above the footer. |
| 107 | reviewed | layout_before_sites.json:48 140-2:165; layout_before_sites.json:49 140-2:166; layout_repairs_applied.json:17 140-2:165 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The six-node topos diagram and lower curved-arrow diamond fit; marginal note 282 stays with its cautionary sentence. |
| 108 | reviewed | layout_before_sites.json:49 140-2:166 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Both large topos diagrams remain within the page, including the right-hand short note; the lower branching diagram is complete. |
| 120 | reviewed | layout_before_sites.json:50 140-2:197 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The prose and marginal notes 306–308 are legible; each note/doubt heading has substantive content and the final item begins normally. |
| 123 | reviewed | evenly spaced sample; layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Numbered formulas 5–14 and the multiline symmetric-product description fit, with separate note blocks and a clear short marginal definition. |
| 124 | reviewed | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205; layout_repairs_applied.json:18 140-2:206 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The square tagged 16 stays with its tag; all quotient and stabilizer formulas 15–22 are complete without overlap. |
| 126 | reviewed | layout_before_sites.json:53 140-2:212 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The two-line quotient identity 30 and full subgroup ladder 31 fit; their tags are adjacent and curved invariant-subgroup arrows remain clear. |
| 127 | reviewed | layout_before_sites.json:53 140-2:212 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The three-line brace display 32, torsor description and theorem 33 are complete; note 324 is retained below with readable content. |
| 129 | reviewed | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Homotopy relations 37–38 and the corollary are fully visible; the long opening condition and final group discussion stay inside the text area. |
| 130 | reviewed | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Marginal notes 330 and 333, the three-line formula 39 and stabilizer relation 40 are separated; the right-side short homotopy note remains legible. |
| 131 | reviewed | layout_before_sites.json:57 140-2:220 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Exact sequences 41–43 and the bottom commutative ladder 44 are complete with their tags; short NB notes remain clear of the right edge. |
| 132 | reviewed | layout_before_sites.json:58 140-2:222 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The theorem, corollary and notes 342–344 are readable; maps 45, 46 and 46bis fit without touching neighboring text. |
| 133 | reviewed | layout_before_sites.json:58 140-2:222 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The large multiline map 48 and homotopy identity 49 remain complete, with the explanatory stabilizer text below its source and no overlap. |
| 137 | reviewed | layout_before_sites.json:59 140-2:233 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Section 20 stays with its introduction and both exact sequences 62–63; the short digression note and two marginal-note blocks fit. |
| 138 | reviewed | layout_before_sites.json:59 140-2:233 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The canonical inclusion 64 and bottom homotopy composite 65 fit; the intervening gerbe discussion and marginal note 356 remain separated. |
| 144 | reviewed | layout_repairs_applied.json:21 140-2:251 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Section 21 keeps its opening paragraph, subgroup filtration 72 and fibration 73; the surrounding doubt blocks have readable contents. |
| 145 | reviewed | layout_repairs_applied.json:19 140-2:252; layout_repairs_applied.json:20 140-2:252; layout_repairs_applied.json:21 140-2:251; layout_repairs_applied.json:22 140-2:252 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The source-option leakage is absent from the three exact sequences at 75; all sequences, tag and note 381 are complete, matching the native syntax closure. |
| 147 | reviewed | evenly spaced sample | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The multiline moduli-space definitions 76–80 remain within the text block and retain their right-side tags without clipping. |
| 149 | reviewed | layout_before_sites.json:60 140-2:259 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The corollary, homotopy relation 83 and tower 84–85 are complete; note 392 and the lower comparison statements are separated. |
| 152 | reviewed | layout_before_sites.json:61 140-2:269 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The categorical equivalence maps and two groupoid sequences fit; marginal notes 393–395 have their text immediately following the headings. |
| 153 | reviewed | layout_before_sites.json:61 140-2:269 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The three short category maps and lower two-row diagram fit with readable surrounding prose; the final explanation stays above the footer. |
| 156 | reviewed | layout_before_sites.json:62 140-2:280 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The hom-category map, two boxed component conditions and fidelity clauses are readable; the long retained-doubt block is separated from the next clause. |
| 157 | reviewed | layout_before_sites.json:62 140-2:280 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The fidelity discussion and section 24 remain complete; notes 408 and 410 contain their text and all short maps fit. |
| 158 | reviewed | layout_before_sites.json:63 140-2:285 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The covering-space introduction, epimorphism and equivariance identity fit; note 412 and the following retained doubts remain separate. |
| 159 | reviewed | layout_before_sites.json:63 140-2:285 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The automorphism identities, exact-sequence diagram and note 413 are fully visible; the lower underlined cohomology expression fits. |
| 166 | reviewed | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The extension and quotient formulas are readable, including the bottom product sequence; the short right-side question mark remains distinct. |
| 167 | reviewed | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The note 424 and lead-in to the wide sequence are retained, followed by an explicit continuation notice to the landscape page. |
| 168 | reviewed | landscape page; layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The complete landscape sequence and its lower identifications fit. A separate native 3x crop was actually inspected: all arrowheads, superscripts, the curved terminal arrow and the calculation note have visible separation. |
| 169 | reviewed | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The post-landscape brace displays and boxed extension are complete; the continuation prose, doubt blocks and lower short map fit. |
| 171 | reviewed | evenly spaced sample | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Section 25bis keeps its opening discussion and exact sequence; the two short right-margin notes are separate from the body. |
| 172 | reviewed | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The centralizer map and notes 427–428 are complete; the long lower doubt list stays separate from the next scan. |
| 177 | reviewed | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:26 140-2:321 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The two-row extension diagram 10, degree-two note and map 11 fit, with all tags and marginal-note text present. |
| 180 | reviewed | layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:25 140-2:328 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The full comparison ladder 21–22 and neighboring sequences 19–23 remain readable; the lower note reference does not obscure the final prose. |
| 181 | reviewed | layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_before_sites.json:71 140-2:329; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:25 140-2:328 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Both comparison diagrams 24–25 and their multiline identifications fit, with the source numbers attached and all explanatory text separated. |
| 182 | reviewed | layout_before_sites.json:71 140-2:329; layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:27 140-2:331; layout_repairs_applied.json:28 140-2:331 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The two-row extension 26 includes one note heading and its full text in the lower-right cell; the following map 27 is complete. |
| 188 | reviewed | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The dense retained-doubt list and following prediscretification discussion fit; the landscape continuation notice remains with scan 344. |
| 189 | reviewed | landscape page; layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The full landscape branching classification fits. Native 3x inspection confirms all multiline nodes, quotient signs, diagonal labels and arrowheads are distinct, with ample outer margins. |
| 190 | reviewed | layout_before_sites.json:73 140-2:344; layout_before_sites.json:74 140-2:346; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:58 140-2:344; layout_pass_sites.json:63 140-2:346; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Both blue pas-separe notes are on separate lines; notes 450 and 451 keep their sketches, and the following NB definition and map remain complete. |
| 191 | reviewed | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The normalizer lemma, prediscretification maps and lower quotient identities fit; the short pas-prouve note is clear in the margin. |
| 192 | reviewed | layout_before_sites.json:75 140-2:348; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:29 140-2:348 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Note 454 retains its double-stroke sketch and note 455 its text; the three exact sequences and lower three-row ladder are complete. |
| 193 | reviewed | layout_before_sites.json:75 140-2:348; layout_before_sites.json:76 140-2:349; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:29 140-2:348 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The moved wide application has its placement notice and both displayed ends visible; the corollary and section 28 keep their openings. |
| 195 | reviewed | evenly spaced sample; layout_before_sites.json:77 140-2:352 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The subgroup argument, marginal note 458 and corollary remain readable; the short manuscript stroke is separate from the following NB. |
| 199 | reviewed | layout_before_sites.json:78 140-2:362 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The upper inclusion diagram 8 fits with its question-mark annotation; the three subsequent scan passages and doubt blocks remain legible. |
| 203 | reviewed | layout_before_sites.json:79 140-2:371 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The subgroup relations 8–12 stay with their explanation and tags, and all doubt blocks retain readable entries. |
| 204 | reviewed | layout_before_sites.json:79 140-2:371 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Relations 13–19 and their superscripts fit; the small right-margin group definitions and question marks are separate from the formulas. |
| 208 | reviewed | layout_repairs_applied.json:33 140-2:382 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The two circled conditions, extension diagram 1 and centralizer sequence 2 remain complete; the right marginal punctuation does not enter the body. |
| 209 | reviewed | layout_before_sites.json:80 140-2:384; layout_pass_sites.json:40 140-2:384; layout_pass_sites.json:64 140-2:384; layout_repairs_applied.json:33 140-2:382 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The circled centralizer condition and maps 3–4 fit; note 482 and the right-margin Galois annotation remain clear. |
| 210 | reviewed | layout_before_sites.json:81 140-2:387 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The prose on finite subgroups and note 483 is legible, with each retained-doubt block separated from the following scan. |
| 214 | reviewed | layout_repairs_applied.json:34 140-2:397 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The composite diagram and maps 5–6 fit; notes 488–489 and their short marginal cautions remain readable. |
| 215 | reviewed | layout_repairs_applied.json:34 140-2:397 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The quotient display 7, triangle 8 and long exact sequence 9 fit with adjacent tags; note 491 has actual content before the footer. |
| 218 | reviewed | layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Maps 16–19 and the boxed triviality condition are complete; note 497 stays with its explanatory text and the lower question begins substantively. |
| 219 | reviewed | layout_repairs_applied.json:35 140-2:407 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The brace diagram 21 and inclusion square 22 keep their tags; the lower map 23 and following conclusion remain on the page. |
| 220 | reviewed | evenly spaced sample | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Maps 24–25 and the two-column verbal category map fit; notes 505–506 both retain content and stay clear of the diagram. |
| 221 | reviewed | layout_pass_sites.json:41 140-2:411 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The axiomatic discussion, short map and notes 509–510 are readable; circled assumptions and lower retained-doubt entries remain separated. |
| 224 | reviewed | layout_repairs_applied.json:36 140-2:417; layout_repairs_applied.json:38 140-2:417 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Tag 26 remains on the page with its complete large ladder; the two blue commutativity annotations occupy distinct clear areas, and the explanatory paragraph follows directly. |
| 225 | reviewed | layout_before_sites.json:84 140-2:419; layout_before_sites.json:85 140-2:419; layout_pass_sites.json:4 140-2:419; layout_pass_sites.json:42 140-2:419; layout_pass_sites.json:59 140-2:419; layout_pass_sites.json:65 140-2:419; layout_repairs_applied.json:37 140-2:419 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The two-column category equivalence 30 fits with its tag and note 513 below; the following paragraph begins normally after retained doubts. |
| 227 | reviewed | layout_before_sites.json:86 140-2:423 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The product groupoid display and short composite are complete; notes 514–515 retain their contents and the lower continuation is unobstructed. |
| 229 | reviewed | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The multiline class-of-sections map and lower admissibility homomorphism fit; the surrounding commentary and doubt blocks remain separated. |
| 230 | reviewed | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The provisional conjecture heading keeps clauses a and b, with clause c and note 522 also on this page; short marginal cancellation note is readable. |
| 235 | reviewed | layout_before_sites.json:89 140-2:443 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The covering-space square and map 10 fit, with proof text and intervening doubt blocks fully visible. |
| 238 | reviewed | layout_before_sites.json:90 140-2:450 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The two boxed boundary definitions and formulas 17–22 remain complete; short left-side annotation is separated from the product display. |
| 239 | reviewed | layout_before_sites.json:90 140-2:450; layout_before_sites.json:91 140-2:452 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The gluing proposition keeps its opening statement and boxed T definition; formulas 23–25 and notes 536–537 fit. |
| 240 | reviewed | layout_before_sites.json:91 140-2:452; layout_before_sites.json:92 140-2:454 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The fixed-locus formula 26, two-case involution definition 27 and lower formula 28 are complete; note 538 and doubt marks are retained. |
| 241 | reviewed | layout_before_sites.json:92 140-2:454 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The brace relation 32 and commutator identity 33 fit; the Remark begins with substantive text before its doubt block, and map 36 is complete. |
| 242 | reviewed | layout_before_sites.json:93 140-2:457 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Formula 37 and conditions a–c remain readable; notes 541–542 and the Remarques paragraph at the foot keep substantive content. |
| 243 | reviewed | layout_before_sites.json:93 140-2:457 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The Euler-characteristic derivation and formulas 38–39 are fully visible; note 543 and the lower case discussion stay separate from the doubts. |
| 244 | reviewed | evenly spaced sample | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The torsor discussion and product identity fit; note 544 and reference involution 40 are complete. |
| 245 | reviewed | layout_before_sites.json:94 140-2:462 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Relations 41–46 fit, including the two-case fixed-point display and multiline index description; note 545 is readable. |
| 246 | reviewed | layout_before_sites.json:94 140-2:462 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The conjugacy calculation, antipodal formula 47 and two-case transformation definition are complete; note 550 keeps its formula at the page foot. |
| 258 | reviewed | layout_before_sites.json:95 140-2:492 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Note 579 keeps its full extension ladder and commentary; Lemmas 2 and 3 have their substantive statements on the page. |
| 261 | reviewed | layout_before_sites.json:96 140-2:502 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The centralizer identities 2–4 and product relation 3 fit; the Remark and note 592 retain substantive content and their following maps. |
| 262 | reviewed | layout_before_sites.json:96 140-2:502 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The curved triangular group diagram is complete; section 36 keeps its title, note 594, defining relation 1 and opening cartographic-group paragraph. |
| 263 | reviewed | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:39 140-2:508 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The proposition keeps its full assertion, manuscript stroke and proof opening; the quotient map 3 and following covering description fit. |
| 264 | reviewed | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:39 140-2:508 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Marginal note 596 retains both sphere sketches; the category equivalence 4 and fiber definition 5 fit with adjacent tags. |
| 266 | reviewed | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Both extension displays 8–9 and the two boxed sequences in note 598 are complete; the short right-margin sum remains readable. |
| 267 | reviewed | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The composite isomorphism 11 and identities 10–17 fit; its hole-filling annotation is readable below the first arrow. |
| 268 | reviewed | evenly spaced sample | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The generator table and formulas 18–24 are complete, including the large lower verbal source node; note 600 has its content on the same page. |
| 270 | reviewed | layout_before_sites.json:101 140-2:519; layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:41 140-2:520 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The moduli formulas 27–30 and note 603 fit; the Galois-cover label is below its arrow with clear separation from the adjacent object scripts. |
| 271 | reviewed | layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:41 140-2:520 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The extension ladder 31 and kernel displays 32–34 fit; their multiple lower identifications are readable and tags remain adjacent. |
| 274 | reviewed | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:42 140-2:527 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The spectral-sequence row and lower identifications are complete; the elliptic-curve formulas and map 39 fit without clipping. |
| 276 | reviewed | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The corollary and composite maps are readable; section 37 keeps its substantive opening before the page boundary. |
| 277 | reviewed | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The proposition has its full opening and definition of X-prime; note 609, the following corollary and exact sequence 3 fit. |
| 278 | reviewed | layout_before_sites.json:107 140-2:536 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The ramification table, isomorphisms 5–6 and exact sequence 7 are complete, with the lower homotopy introduction retained as prose. |
| 293 | reviewed | evenly spaced sample | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The rational j-invariant formulas 58–62 and map 60 fit; note 623 and Remarques have their substantive content. |
| 294 | reviewed | layout_before_sites.json:108 140-2:567 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Formulas 63–66, note 625 and the editorial description of the erased arrow inscription remain legible; the short right-side product note is separate. |
| 295 | reviewed | layout_before_sites.json:108 140-2:567; layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:43 140-2:568; layout_repairs_applied.json:44 140-2:568 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Tag 67 stays with the complete Galois-cover diagram; the raised degree-two label clears its target, and proposition 68 and note 627 fit below. |
| 301 | reviewed | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The new cote heading and manuscript contents fit, including the bracketed subsection list and marginal note 631. |
| 302 | reviewed | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The continuation contents and long parameter descriptions fit within the text area; the right-page references and doubt list remain legible. |
| 303 | reviewed | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4; layout_before_sites.json:114 140-3:5; layout_repairs_applied.json:45 140-3:6 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The remaining contents and notes 636–637 are complete; section 38 is reserved for the next page rather than stranded at the foot. |
| 304 | reviewed | layout_repairs_applied.json:45 140-3:6 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Section 38 keeps its full opening and formula 1, followed by maps 2–6 and the proposition; the repaired opener also passed native closure. |
| 308 | reviewed | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The corollary, path formulas and rational function remain readable; note 650 and all colored alternatives are retained. |
| 309 | reviewed | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The spherical-triangle description and generator identities fit; note 653 stays with its explanation and formula 21. |
| 311 | reviewed | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The brace display 22, long involution identities and formulas 23–25 fit; the right-side NB remains clear of the calculations. |
| 312 | reviewed | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The complete marginal calculation 657 and projective-action formulas 26–28 fit; note 659 has its text and the short right-side category note is legible. |
| 313 | reviewed | layout_repairs_applied.json:46 140-3:21 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The projective quotient 29, diagram 30 and section 39 extension ladder fit; the section retains its opening and subsequent character maps. |
| 314 | reviewed | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The central-scalar composite and maps 5–8 remain complete, with note 668 and each retained-doubt list separated. |
| 317 | reviewed | evenly spaced sample | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The boxed lifting map 21, long automorphism composite 25 and neighboring maps 20–26 fit; their subscripts remain inside the text block. |
| 318 | reviewed | layout_repairs_applied.json:47 140-3:33 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The widened map 28 keeps its tuple label clear of both objects; maps 27–33, note 680 and short prime-number margin note are readable. |
| 319 | reviewed | layout_before_sites.json:124 140-3:36 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The extension sequence 35 and maps 34–40 fit with their quotient identifications and neighboring doubt blocks. |
| 320 | reviewed | layout_before_sites.json:124 140-3:36 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The character map 41, two-line injection 43, central extension 46 and lower Hom-kernel display 48 are complete with adjacent tags. |
| 321 | reviewed | layout_repairs_applied.json:48 140-3:40 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | Section 40 keeps its substantive opener; square 53 stays with its tag, and formulas 49–54 are readable. |
| 322 | reviewed | layout_repairs_applied.json:48 140-3:40; layout_repairs_applied.json:49 140-3:41 | typeset; Actual 2x2 contact-sheet inspection at900px per source page; release578_pending sheets001–034; exact PDF/PNG/pixel evidence preserved in work/data/fr_reading_release578_typeset_review_evidence.json | The equivalence square 56 remains with its tag; notes 690–691 and sequence 58 keep their contents and clear separation. |
| 323 | pending | layout_repairs_applied.json:50 140-3:44 | ;  |  |
| 326 | pending | layout_repairs_applied.json:51 140-3:55 | ;  |  |
| 327 | pending | layout_repairs_applied.json:51 140-3:55; layout_repairs_applied.json:52 140-3:56 | ;  |  |
| 328 | pending | layout_before_sites.json:125 140-3:58; layout_repairs_applied.json:52 140-3:56 | ;  |  |
| 329 | pending | layout_before_sites.json:125 140-3:58; layout_before_sites.json:126 140-3:59 | ;  |  |
| 331 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 332 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 334 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 335 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 337 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 338 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 339 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 340 | pending | layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75; layout_before_sites.json:133 140-3:76 | ;  |  |
| 341 | pending | evenly spaced sample; layout_before_sites.json:133 140-3:76 | ;  |  |
| 346 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:53 140-3:85; layout_repairs_applied.json:54 140-3:85; layout_repairs_applied.json:55 140-3:85; layout_repairs_applied.json:56 140-3:85; layout_repairs_applied.json:57 140-3:85; layout_repairs_applied.json:58 140-3:85; layout_repairs_applied.json:59 140-3:85 | ;  |  |
| 347 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_before_sites.json:136 140-3:86; layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:53 140-3:85; layout_repairs_applied.json:54 140-3:85; layout_repairs_applied.json:55 140-3:85; layout_repairs_applied.json:56 140-3:85; layout_repairs_applied.json:57 140-3:85; layout_repairs_applied.json:58 140-3:85; layout_repairs_applied.json:59 140-3:85 | ;  |  |
| 348 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:60 140-3:88 | ;  |  |
| 349 | pending | layout_before_sites.json:139 140-3:90; layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:60 140-3:88 | ;  |  |
| 350 | pending | layout_before_sites.json:139 140-3:90; layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91 | ;  |  |
| 351 | pending | layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91; layout_before_sites.json:145 140-3:92 | ;  |  |
| 352 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 353 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 355 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 356 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95; layout_repairs_applied.json:61 140-3:97; layout_repairs_applied.json:67 140-3:97 | ;  |  |
| 357 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98; layout_repairs_applied.json:61 140-3:97; layout_repairs_applied.json:67 140-3:97 | ;  |  |
| 358 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98 | ;  |  |
| 363 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 364 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 366 | pending | evenly spaced sample; layout_before_sites.json:153 140-3:111 | ;  |  |
| 367 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 372 | pending | layout_repairs_applied.json:68 140-3:121 | ;  |  |
| 373 | pending | layout_repairs_applied.json:68 140-3:121 | ;  |  |
| 389 | pending | layout_before_sites.json:154 140-3:148 | ;  |  |
| 390 | pending | evenly spaced sample; layout_before_sites.json:154 140-3:148 | ;  |  |
| 394 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 397 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 398 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 412 | pending | layout_before_sites.json:157 140-3:185 | ;  |  |
| 413 | pending | layout_before_sites.json:157 140-3:185; layout_repairs_applied.json:69 140-3:186 | ;  |  |
| 414 | pending | evenly spaced sample; layout_repairs_applied.json:69 140-3:186 | ;  |  |
| 417 | pending | layout_before_sites.json:158 140-3:191; layout_before_sites.json:159 140-3:191; layout_before_sites.json:160 140-3:192 | ;  |  |
| 418 | pending | layout_before_sites.json:160 140-3:192; layout_before_sites.json:161 140-3:194 | ;  |  |
| 419 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 422 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 423 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 428 | pending | layout_repairs_applied.json:70 140-3:208 | ;  |  |
| 429 | pending | layout_repairs_applied.json:70 140-3:208; layout_repairs_applied.json:71 140-3:209 | ;  |  |
| 431 | pending | layout_before_sites.json:164 140-3:212 | ;  |  |
| 432 | pending | layout_before_sites.json:164 140-3:212; layout_before_sites.json:165 140-3:213; layout_before_sites.json:166 140-3:215 | ;  |  |
| 433 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 437 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_repairs_applied.json:72 140-3:221 | ;  |  |
| 438 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_before_sites.json:169 140-3:222; layout_repairs_applied.json:72 140-3:221 | ;  |  |
| 439 | pending | evenly spaced sample; layout_before_sites.json:169 140-3:222 | ;  |  |
| 445 | pending | layout_before_sites.json:170 140-3:231 | ;  |  |
| 446 | pending | layout_before_sites.json:170 140-3:231; layout_before_sites.json:171 140-3:232 | ;  |  |
| 453 | pending | layout_repairs_applied.json:73 140-3:245 | ;  |  |
| 454 | pending | layout_repairs_applied.json:73 140-3:245 | ;  |  |
| 461 | pending | layout_repairs_applied.json:74 140-3:261 | ;  |  |
| 462 | pending | layout_repairs_applied.json:74 140-3:261 | ;  |  |
| 463 | pending | evenly spaced sample | ;  |  |
| 470 | pending | layout_repairs_applied.json:75 140-3:275 | ;  |  |
| 471 | pending | layout_repairs_applied.json:75 140-3:275 | ;  |  |
| 474 | pending | layout_before_sites.json:172 140-3:282 | ;  |  |
| 475 | pending | layout_before_sites.json:172 140-3:282; layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 476 | pending | layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 487 | pending | evenly spaced sample; layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 488 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 498 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:76 140-3:320 | ;  |  |
| 499 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:76 140-3:320 | ;  |  |
| 500 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 501 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 503 | pending | layout_before_sites.json:179 140-3:327; layout_before_sites.json:180 140-3:328; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:77 140-3:328 | ;  |  |
| 504 | pending | layout_before_sites.json:180 140-3:328; layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:73 140-3:329; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:77 140-3:328; layout_repairs_applied.json:78 140-3:329 | ;  |  |
| 505 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:78 140-3:329 | ;  |  |
| 508 | pending | layout_before_sites.json:182 140-3:334 | ;  |  |
| 509 | pending | layout_before_sites.json:182 140-3:334; layout_repairs_applied.json:80 140-3:335 | ;  |  |
| 511 | pending | evenly spaced sample | ;  |  |
| 516 | pending | layout_before_sites.json:183 140-3:346 | ;  |  |
| 521 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 523 | pending | layout_before_sites.json:185 140-3:356 | ;  |  |
| 524 | pending | layout_before_sites.json:185 140-3:356; layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357 | ;  |  |
| 525 | pending | layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357; layout_repairs_applied.json:81 140-3:358 | ;  |  |
| 526 | pending | layout_repairs_applied.json:81 140-3:358 | ;  |  |
| 528 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362; layout_repairs_applied.json:84 140-3:363 | ;  |  |
| 529 | pending | layout_repairs_applied.json:84 140-3:363 | ;  |  |
| 536 | pending | evenly spaced sample | ;  |  |
| 539 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 540 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 546 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 547 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 559 | pending | layout_repairs_applied.json:91 140-3:408; layout_repairs_applied.json:92 140-3:408; layout_repairs_applied.json:93 140-3:408 | ;  |  |
| 560 | pending | evenly spaced sample; layout_repairs_applied.json:91 140-3:408; layout_repairs_applied.json:92 140-3:408; layout_repairs_applied.json:93 140-3:408; layout_repairs_applied.json:94 140-3:410 | ;  |  |
| 561 | pending | layout_repairs_applied.json:94 140-3:410 | ;  |  |
| 562 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 563 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 564 | pending | layout_before_sites.json:192 140-3:415 | ;  |  |
| 565 | pending | layout_before_sites.json:192 140-3:415; layout_before_sites.json:193 140-3:416 | ;  |  |
| 566 | pending | layout_before_sites.json:193 140-3:416 | ;  |  |
| 567 | pending | layout_before_sites.json:193 140-3:416 | ;  |  |
| 568 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:98 140-3:419 | ;  |  |
| 569 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:98 140-3:419 | ;  |  |
| 573 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:95 140-3:425 | ;  |  |
| 574 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:95 140-3:425 | ;  |  |
| 576 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 577 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429; layout_before_sites.json:197 140-3:431 | ;  |  |
| 578 | pending | layout_before_sites.json:197 140-3:431; layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432 | ;  |  |
| 579 | pending | layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432 | ;  |  |
| 580 | pending | layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432; layout_before_sites.json:200 140-3:433 | ;  |  |
| 581 | pending | layout_before_sites.json:200 140-3:433 | ;  |  |
| 582 | pending | layout_repairs_applied.json:107 140-3:436; layout_repairs_applied.json:108 140-3:436; layout_repairs_applied.json:109 140-3:436 | ;  |  |
| 583 | pending | layout_repairs_applied.json:107 140-3:436; layout_repairs_applied.json:108 140-3:436; layout_repairs_applied.json:109 140-3:436; layout_repairs_applied.json:110 140-3:437; layout_repairs_applied.json:111 140-3:437 | ;  |  |
| 584 | pending | evenly spaced sample; layout_repairs_applied.json:110 140-3:437; layout_repairs_applied.json:111 140-3:437; layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438 | ;  |  |
| 585 | pending | layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438 | ;  |  |
| 586 | pending | layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438; layout_repairs_applied.json:116 140-3:439; layout_repairs_applied.json:117 140-3:440; layout_repairs_applied.json:99 140-3:440 | ;  |  |
| 587 | pending | layout_repairs_applied.json:103 140-3:441; layout_repairs_applied.json:117 140-3:440; layout_repairs_applied.json:99 140-3:440 | ;  |  |
| 588 | pending | layout_before_sites.json:201 140-3:444; layout_repairs_applied.json:106 140-3:443 | ;  |  |
| 589 | pending | layout_before_sites.json:201 140-3:444 | ;  |  |
| 590 | pending | layout_before_sites.json:201 140-3:444; layout_pass_sites.json:12 140-3:446; layout_repairs_applied.json:101 140-3:446 | ;  |  |
| 591 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:12 140-3:446; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:100 140-3:448; layout_repairs_applied.json:101 140-3:446 | ;  |  |
| 592 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:100 140-3:448; layout_repairs_applied.json:104 140-3:449; layout_repairs_applied.json:105 140-3:449 | ;  |  |
| 593 | pending | layout_repairs_applied.json:104 140-3:449; layout_repairs_applied.json:105 140-3:449 | ;  |  |
| 596 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 597 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 600 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 601 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 603 | pending | layout_repairs_applied.json:118 140-3:462; layout_repairs_applied.json:119 140-3:463; layout_repairs_applied.json:120 140-3:463; layout_repairs_applied.json:121 140-3:463 | ;  |  |
| 604 | pending | layout_before_sites.json:207 140-3:465; layout_repairs_applied.json:119 140-3:463; layout_repairs_applied.json:120 140-3:463; layout_repairs_applied.json:121 140-3:463 | ;  |  |
| 605 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 606 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 607 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 608 | pending | layout_before_sites.json:208 140-3:468; layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 609 | pending | evenly spaced sample; layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 614 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 615 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 616 | pending | layout_before_sites.json:211 140-3:479; layout_repairs_applied.json:122 140-3:480; layout_repairs_applied.json:123 140-3:480 | ;  |  |
| 617 | pending | layout_repairs_applied.json:122 140-3:480; layout_repairs_applied.json:123 140-3:480 | ;  |  |
| 619 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 620 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 622 | pending | layout_before_sites.json:213 140-3:491 | ;  |  |
| 623 | pending | layout_before_sites.json:213 140-3:491; layout_before_sites.json:214 140-3:492 | ;  |  |
| 624 | pending | layout_repairs_applied.json:124 140-3:494 | ;  |  |
| 628 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 631 | pending | layout_repairs_applied.json:126 140-3:503 | ;  |  |
| 632 | pending | layout_repairs_applied.json:126 140-3:503 | ;  |  |
| 633 | pending | evenly spaced sample | ;  |  |
| 634 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:127 140-3:506; layout_repairs_applied.json:128 140-3:506 | ;  |  |
| 635 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:127 140-3:506; layout_repairs_applied.json:128 140-3:506 | ;  |  |
| 636 | pending | layout_before_sites.json:217 140-3:509 | ;  |  |
| 637 | pending | layout_before_sites.json:217 140-3:509; layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 638 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 641 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 642 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 643 | pending | layout_before_sites.json:221 140-3:517 | ;  |  |
| 644 | pending | layout_before_sites.json:221 140-3:517; layout_before_sites.json:222 140-3:518 | ;  |  |
| 645 | pending | layout_before_sites.json:222 140-3:518; layout_before_sites.json:223 140-3:519; layout_repairs_applied.json:129 140-3:519; layout_repairs_applied.json:134 140-3:519 | ;  |  |
| 646 | pending | layout_before_sites.json:223 140-3:519; layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:129 140-3:519; layout_repairs_applied.json:133 140-3:520; layout_repairs_applied.json:134 140-3:519 | ;  |  |
| 647 | pending | layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:133 140-3:520 | ;  |  |
| 648 | pending | layout_before_sites.json:225 140-3:522 | ;  |  |
| 649 | pending | layout_before_sites.json:225 140-3:522; layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:135 140-3:523; layout_repairs_applied.json:136 140-3:524; layout_repairs_applied.json:137 140-3:524 | ;  |  |
| 650 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:130 140-3:525; layout_repairs_applied.json:136 140-3:524; layout_repairs_applied.json:137 140-3:524; layout_repairs_applied.json:138 140-3:525; layout_repairs_applied.json:139 140-3:525 | ;  |  |
| 651 | pending | layout_repairs_applied.json:130 140-3:525; layout_repairs_applied.json:138 140-3:525; layout_repairs_applied.json:139 140-3:525 | ;  |  |
| 654 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530 | ;  |  |
| 655 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530; layout_before_sites.json:229 140-3:531; layout_before_sites.json:230 140-3:532 | ;  |  |
| 656 | pending | layout_before_sites.json:230 140-3:532; layout_before_sites.json:231 140-3:533; layout_before_sites.json:232 140-3:534 | ;  |  |
| 657 | pending | evenly spaced sample; layout_before_sites.json:232 140-3:534; layout_before_sites.json:233 140-3:535 | ;  |  |
| 658 | pending | layout_before_sites.json:233 140-3:535; layout_before_sites.json:234 140-3:536; layout_repairs_applied.json:140 140-3:536 | ;  |  |
| 659 | pending | layout_before_sites.json:234 140-3:536; layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_before_sites.json:238 140-3:538; layout_repairs_applied.json:140 140-3:536 | ;  |  |
| 660 | pending | layout_before_sites.json:238 140-3:538; layout_before_sites.json:239 140-3:539; layout_before_sites.json:240 140-3:540 | ;  |  |
| 661 | pending | layout_before_sites.json:240 140-3:540; layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 662 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541; layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:141 140-3:542; layout_repairs_applied.json:145 140-3:542 | ;  |  |
| 663 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_before_sites.json:245 140-3:543; layout_repairs_applied.json:141 140-3:542; layout_repairs_applied.json:145 140-3:542; layout_repairs_applied.json:146 140-3:543; layout_repairs_applied.json:147 140-3:543; layout_repairs_applied.json:148 140-3:543 | ;  |  |
| 664 | pending | layout_before_sites.json:245 140-3:543; layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:146 140-3:543; layout_repairs_applied.json:147 140-3:543; layout_repairs_applied.json:148 140-3:543; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544 | ;  |  |
| 665 | pending | layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544 | ;  |  |
| 666 | pending | layout_before_sites.json:246 140-3:544; layout_before_sites.json:247 140-3:545; layout_repairs_applied.json:142 140-3:545; layout_repairs_applied.json:143 140-3:545; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544; layout_repairs_applied.json:151 140-3:545; layout_repairs_applied.json:152 140-3:545; layout_repairs_applied.json:153 140-3:545; layout_repairs_applied.json:154 140-3:545; layout_repairs_applied.json:155 140-3:545; layout_repairs_applied.json:156 140-3:545 | ;  |  |
| 667 | pending | layout_before_sites.json:247 140-3:545; layout_before_sites.json:248 140-3:546; layout_repairs_applied.json:142 140-3:545; layout_repairs_applied.json:143 140-3:545; layout_repairs_applied.json:144 140-3:546; layout_repairs_applied.json:151 140-3:545; layout_repairs_applied.json:152 140-3:545; layout_repairs_applied.json:153 140-3:545; layout_repairs_applied.json:154 140-3:545; layout_repairs_applied.json:155 140-3:545; layout_repairs_applied.json:156 140-3:545 | ;  |  |
| 668 | pending | layout_before_sites.json:248 140-3:546; layout_before_sites.json:249 140-3:547; layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:144 140-3:546; layout_repairs_applied.json:157 140-3:548 | ;  |  |
| 669 | pending | layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:157 140-3:548 | ;  |  |
| 672 | pending | layout_before_sites.json:251 140-3:554; layout_repairs_applied.json:158 140-3:554 | ;  |  |
| 673 | pending | layout_before_sites.json:251 140-3:554; layout_before_sites.json:252 140-3:555; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:158 140-3:554; layout_repairs_applied.json:159 140-3:555 | ;  |  |
| 674 | pending | layout_before_sites.json:252 140-3:555; layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:159 140-3:555; layout_repairs_applied.json:160 140-3:556 | ;  |  |
| 675 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_repairs_applied.json:160 140-3:556 | ;  |  |
| 676 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_before_sites.json:255 140-3:557; layout_before_sites.json:256 140-3:558; layout_pass_sites.json:14 140-3:557; layout_pass_sites.json:75 140-3:557; layout_repairs_applied.json:160 140-3:556; layout_repairs_applied.json:162 140-3:557 | ;  |  |
| 677 | pending | layout_before_sites.json:256 140-3:558; layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 678 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 679 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:163 140-3:561 | ;  |  |
| 680 | pending | landscape page; layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:163 140-3:561 | ;  |  |
| 681 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:161 140-3:562; layout_repairs_applied.json:163 140-3:561; layout_repairs_applied.json:166 140-3:562; layout_repairs_applied.json:167 140-3:562 | ;  |  |
| 682 | pending | evenly spaced sample; layout_repairs_applied.json:161 140-3:562; layout_repairs_applied.json:166 140-3:562; layout_repairs_applied.json:167 140-3:562 | ;  |  |
| 683 | pending | layout_repairs_applied.json:168 140-3:565 | ;  |  |
| 684 | pending | layout_repairs_applied.json:168 140-3:565 | ;  |  |
| 685 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567 | ;  |  |
| 686 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567; layout_repairs_applied.json:169 140-3:568 | ;  |  |
| 687 | pending | layout_repairs_applied.json:169 140-3:568 | ;  |  |
| 688 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 689 | pending | layout_before_sites.json:263 140-3:573; layout_repairs_applied.json:170 140-3:573 | ;  |  |
| 690 | pending | layout_before_sites.json:263 140-3:573; layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:170 140-3:573; layout_repairs_applied.json:171 140-3:574 | ;  |  |
| 691 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:171 140-3:574; layout_repairs_applied.json:173 140-3:575 | ;  |  |
| 692 | pending | layout_before_sites.json:265 140-3:577; layout_repairs_applied.json:173 140-3:575 | ;  |  |
| 693 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 697 | pending | layout_before_sites.json:266 140-3:582 | ;  |  |
| 699 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 700 | pending | layout_before_sites.json:267 140-3:585; layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 701 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586; layout_before_sites.json:270 140-3:587 | ;  |  |
| 702 | pending | layout_before_sites.json:270 140-3:587; layout_before_sites.json:271 140-3:588 | ;  |  |
| 703 | pending | layout_before_sites.json:271 140-3:588; layout_before_sites.json:272 140-3:589 | ;  |  |
| 704 | pending | layout_before_sites.json:272 140-3:589; layout_repairs_applied.json:175 140-3:590 | ;  |  |
| 706 | pending | evenly spaced sample; layout_before_sites.json:273 140-3:593 | ;  |  |
| 711 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 715 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:176 140-3:606 | ;  |  |
| 716 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:176 140-3:606 | ;  |  |
| 718 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:178 140-3:609 | ;  |  |
| 722 | pending | layout_before_sites.json:275 140-3:616 | ;  |  |
| 723 | pending | layout_before_sites.json:275 140-3:616; layout_before_sites.json:276 140-3:617 | ;  |  |
| 724 | pending | layout_before_sites.json:276 140-3:617 | ;  |  |
| 725 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:179 140-3:619 | ;  |  |
| 726 | pending | layout_before_sites.json:277 140-3:619; layout_before_sites.json:278 140-3:621; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:18 140-3:621; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:177 140-3:621; layout_repairs_applied.json:179 140-3:619; layout_repairs_applied.json:184 140-3:621 | ;  |  |
| 727 | pending | layout_before_sites.json:278 140-3:621; layout_pass_sites.json:18 140-3:621; layout_repairs_applied.json:177 140-3:621; layout_repairs_applied.json:184 140-3:621; layout_repairs_applied.json:185 140-3:622; layout_repairs_applied.json:186 140-3:622; layout_repairs_applied.json:187 140-3:622; layout_repairs_applied.json:188 140-3:622; layout_repairs_applied.json:189 140-3:622 | ;  |  |
| 728 | pending | layout_repairs_applied.json:185 140-3:622; layout_repairs_applied.json:186 140-3:622; layout_repairs_applied.json:187 140-3:622; layout_repairs_applied.json:188 140-3:622; layout_repairs_applied.json:189 140-3:622; layout_repairs_applied.json:190 140-3:623; layout_repairs_applied.json:191 140-3:623 | ;  |  |
| 729 | pending | layout_repairs_applied.json:190 140-3:623; layout_repairs_applied.json:191 140-3:623 | ;  |  |
| 730 | pending | evenly spaced sample; layout_before_sites.json:279 140-3:625 | ;  |  |
| 731 | pending | layout_before_sites.json:280 140-3:627; layout_repairs_applied.json:192 140-3:628 | ;  |  |
| 732 | pending | layout_before_sites.json:281 140-3:629; layout_repairs_applied.json:192 140-3:628 | ;  |  |
| 733 | pending | layout_before_sites.json:281 140-3:629; layout_before_sites.json:282 140-3:631 | ;  |  |
| 734 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 736 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:194 140-3:637; layout_repairs_applied.json:196 140-3:637 | ;  |  |
| 737 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:193 140-3:638; layout_repairs_applied.json:194 140-3:637; layout_repairs_applied.json:196 140-3:637 | ;  |  |
| 738 | pending | layout_repairs_applied.json:193 140-3:638 | ;  |  |
| 744 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:207 140-3:649 | ;  |  |
| 745 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:207 140-3:649 | ;  |  |
| 746 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:197 140-3:653; layout_repairs_applied.json:208 140-3:653 | ;  |  |
| 747 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:197 140-3:653; layout_repairs_applied.json:208 140-3:653 | ;  |  |
| 748 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:209 140-3:656; layout_repairs_applied.json:210 140-3:656 | ;  |  |
| 749 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:209 140-3:656; layout_repairs_applied.json:210 140-3:656 | ;  |  |
| 750 | pending | layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_repairs_applied.json:198 140-3:658; layout_repairs_applied.json:199 140-3:658 | ;  |  |
| 751 | pending | layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:198 140-3:658; layout_repairs_applied.json:199 140-3:658; layout_repairs_applied.json:200 140-3:659; layout_repairs_applied.json:201 140-3:659 | ;  |  |
| 752 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:200 140-3:659; layout_repairs_applied.json:201 140-3:659; layout_repairs_applied.json:202 140-3:660 | ;  |  |
| 753 | pending | layout_repairs_applied.json:202 140-3:660 | ;  |  |
| 754 | pending | layout_repairs_applied.json:202 140-3:660 | ;  |  |
| 755 | pending | evenly spaced sample; layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:203 140-3:662 | ;  |  |
| 760 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 767 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 770 | pending | layout_repairs_applied.json:213 140-3:685; layout_repairs_applied.json:214 140-3:685 | ;  |  |
| 771 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:213 140-3:685; layout_repairs_applied.json:214 140-3:685; layout_repairs_applied.json:215 140-3:686 | ;  |  |
| 772 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:215 140-3:686; layout_repairs_applied.json:216 140-3:688; layout_repairs_applied.json:217 140-3:688 | ;  |  |
| 773 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:216 140-3:688; layout_repairs_applied.json:217 140-3:688; layout_repairs_applied.json:218 140-3:689 | ;  |  |
| 774 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:218 140-3:689 | ;  |  |
| 775 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692 | ;  |  |
| 776 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692; layout_repairs_applied.json:219 140-3:693; layout_repairs_applied.json:220 140-3:693 | ;  |  |
| 777 | pending | layout_repairs_applied.json:219 140-3:693; layout_repairs_applied.json:220 140-3:693 | ;  |  |
| 779 | pending | evenly spaced sample | ;  |  |
| 780 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 783 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 785 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 786 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 790 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:221 140-4:20 | ;  |  |
| 794 | pending | layout_before_sites.json:311 140-4:29 | ;  |  |
| 795 | pending | layout_before_sites.json:311 140-4:29 | ;  |  |
| 796 | pending | layout_repairs_applied.json:223 140-4:31; layout_repairs_applied.json:224 140-4:31; layout_repairs_applied.json:225 140-4:31; layout_repairs_applied.json:226 140-4:32; layout_repairs_applied.json:227 140-4:32 | ;  |  |
| 797 | pending | layout_repairs_applied.json:226 140-4:32; layout_repairs_applied.json:227 140-4:32; layout_repairs_applied.json:228 140-4:33 | ;  |  |
| 798 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:228 140-4:33 | ;  |  |
| 799 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34 | ;  |  |
| 800 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:229 140-4:35; layout_repairs_applied.json:230 140-4:35 | ;  |  |
| 801 | pending | layout_repairs_applied.json:229 140-4:35; layout_repairs_applied.json:230 140-4:35 | ;  |  |
| 803 | pending | evenly spaced sample; layout_before_sites.json:314 140-4:39; layout_before_sites.json:315 140-4:40 | ;  |  |
| 804 | pending | layout_before_sites.json:315 140-4:40; layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41 | ;  |  |
| 805 | pending | layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41; layout_before_sites.json:318 140-4:42; layout_before_sites.json:319 140-4:43 | ;  |  |
| 806 | pending | layout_before_sites.json:319 140-4:43; layout_before_sites.json:320 140-4:44; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:231 140-4:44 | ;  |  |
| 807 | pending | layout_before_sites.json:320 140-4:44; layout_before_sites.json:321 140-4:45; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:231 140-4:44 | ;  |  |
| 808 | pending | layout_before_sites.json:321 140-4:45; layout_before_sites.json:322 140-4:46; layout_before_sites.json:323 140-4:47 | ;  |  |
| 809 | pending | layout_before_sites.json:323 140-4:47; layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48 | ;  |  |
| 810 | pending | layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48; layout_before_sites.json:327 140-4:49 | ;  |  |
| 811 | pending | layout_before_sites.json:327 140-4:49; layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 812 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50; layout_before_sites.json:331 140-4:51 | ;  |  |
| 813 | pending | layout_before_sites.json:331 140-4:51; layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52; layout_before_sites.json:334 140-4:53 | ;  |  |
| 814 | pending | layout_before_sites.json:334 140-4:53; layout_before_sites.json:335 140-4:54; layout_before_sites.json:336 140-4:55 | ;  |  |
| 815 | pending | layout_before_sites.json:336 140-4:55; layout_before_sites.json:337 140-4:56 | ;  |  |
| 816 | pending | layout_before_sites.json:337 140-4:56; layout_before_sites.json:338 140-4:57 | ;  |  |
| 817 | pending | layout_before_sites.json:338 140-4:57; layout_repairs_applied.json:244 140-4:59 | ;  |  |
| 818 | pending | layout_repairs_applied.json:244 140-4:59 | ;  |  |
| 819 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:245 140-4:61; layout_repairs_applied.json:246 140-4:61; layout_repairs_applied.json:247 140-4:61; layout_repairs_applied.json:248 140-4:61; layout_repairs_applied.json:249 140-4:62 | ;  |  |
| 820 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:249 140-4:62 | ;  |  |
| 821 | pending | layout_repairs_applied.json:242 140-4:65 | ;  |  |
| 822 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:233 140-4:66; layout_repairs_applied.json:234 140-4:66; layout_repairs_applied.json:235 140-4:66; layout_repairs_applied.json:242 140-4:65 | ;  |  |
| 823 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_before_sites.json:343 140-4:67; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:233 140-4:66; layout_repairs_applied.json:234 140-4:66; layout_repairs_applied.json:235 140-4:66 | ;  |  |
| 824 | pending | layout_before_sites.json:343 140-4:67 | ;  |  |
| 825 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 826 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 827 | pending | evenly spaced sample | ;  |  |
| 829 | pending | layout_repairs_applied.json:250 140-4:74 | ;  |  |
| 830 | pending | layout_repairs_applied.json:243 140-4:75; layout_repairs_applied.json:250 140-4:74; layout_repairs_applied.json:251 140-4:75; layout_repairs_applied.json:252 140-4:75; layout_repairs_applied.json:253 140-4:75 | ;  |  |
| 831 | pending | layout_repairs_applied.json:243 140-4:75; layout_repairs_applied.json:251 140-4:75; layout_repairs_applied.json:252 140-4:75; layout_repairs_applied.json:253 140-4:75; layout_repairs_applied.json:254 140-4:76; layout_repairs_applied.json:255 140-4:76 | ;  |  |
| 832 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:254 140-4:76; layout_repairs_applied.json:255 140-4:76; layout_repairs_applied.json:258 140-4:77 | ;  |  |
| 833 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:258 140-4:77; layout_repairs_applied.json:259 140-4:78; layout_repairs_applied.json:260 140-4:78 | ;  |  |
| 834 | pending | layout_repairs_applied.json:259 140-4:78; layout_repairs_applied.json:260 140-4:78; layout_repairs_applied.json:261 140-4:79; layout_repairs_applied.json:262 140-4:79 | ;  |  |
| 835 | pending | layout_repairs_applied.json:261 140-4:79; layout_repairs_applied.json:262 140-4:79; layout_repairs_applied.json:263 140-4:80 | ;  |  |
| 836 | pending | layout_repairs_applied.json:263 140-4:80; layout_repairs_applied.json:264 140-4:81; layout_repairs_applied.json:265 140-4:81 | ;  |  |
| 837 | pending | layout_repairs_applied.json:264 140-4:81; layout_repairs_applied.json:265 140-4:81 | ;  |  |
| 845 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 846 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 849 | pending | layout_repairs_applied.json:269 140-4:96; layout_repairs_applied.json:270 140-4:96 | ;  |  |
| 850 | pending | layout_repairs_applied.json:269 140-4:96; layout_repairs_applied.json:270 140-4:96; layout_repairs_applied.json:271 140-4:97; layout_repairs_applied.json:272 140-4:97 | ;  |  |
| 851 | pending | layout_before_sites.json:349 140-4:99; layout_repairs_applied.json:271 140-4:97; layout_repairs_applied.json:272 140-4:97; layout_repairs_applied.json:273 140-4:98 | ;  |  |
| 852 | pending | evenly spaced sample; layout_before_sites.json:349 140-4:99 | ;  |  |
| 853 | pending | layout_before_sites.json:349 140-4:99; layout_before_sites.json:350 140-4:101 | ;  |  |
| 854 | pending | layout_before_sites.json:350 140-4:101; layout_before_sites.json:351 140-4:102 | ;  |  |
| 855 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 856 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 860 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:266 140-4:113 | ;  |  |
| 861 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:266 140-4:113 | ;  |  |
| 876 | pending | evenly spaced sample; layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:274 140-4:136 | ;  |  |
| 877 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:274 140-4:136 | ;  |  |
| 881 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 882 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 883 | pending | layout_before_sites.json:356 140-4:149 | ;  |  |
| 885 | pending | layout_before_sites.json:357 140-4:154 | ;  |  |
| 886 | pending | layout_before_sites.json:357 140-4:154 | ;  |  |
| 894 | pending | layout_repairs_applied.json:276 140-4:172 | ;  |  |
| 895 | pending | layout_repairs_applied.json:276 140-4:172; layout_repairs_applied.json:277 140-4:174; layout_repairs_applied.json:278 140-4:175; layout_repairs_applied.json:279 140-4:175 | ;  |  |
| 896 | pending | layout_repairs_applied.json:278 140-4:175; layout_repairs_applied.json:279 140-4:175 | ;  |  |
| 898 | pending | layout_before_sites.json:358 140-4:181; layout_before_sites.json:359 140-4:181 | ;  |  |
| 899 | pending | layout_before_sites.json:358 140-4:181; layout_before_sites.json:359 140-4:181 | ;  |  |
| 900 | pending | evenly spaced sample; layout_before_sites.json:360 140-4:186 | ;  |  |
| 901 | pending | layout_before_sites.json:361 140-4:188 | ;  |  |
| 906 | pending | layout_repairs_applied.json:280 140-4:203; layout_repairs_applied.json:281 140-4:203 | ;  |  |
| 907 | pending | layout_repairs_applied.json:280 140-4:203; layout_repairs_applied.json:281 140-4:203; layout_repairs_applied.json:282 140-4:205 | ;  |  |
| 908 | pending | layout_repairs_applied.json:282 140-4:205 | ;  |  |
| 920 | pending | layout_before_sites.json:362 140-4:230 | ;  |  |
| 921 | pending | layout_before_sites.json:362 140-4:230 | ;  |  |
| 924 | pending | layout_before_sites.json:363 140-4:236 | ;  |  |
| 925 | pending | evenly spaced sample | ;  |  |
| 929 | pending | layout_before_sites.json:364 140-4:245 | ;  |  |
| 931 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 932 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 939 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 940 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 941 | pending | layout_before_sites.json:367 140-4:266 | ;  |  |
| 942 | pending | layout_before_sites.json:367 140-4:266; layout_before_sites.json:368 140-4:267; layout_before_sites.json:369 140-4:268 | ;  |  |
| 943 | pending | layout_before_sites.json:369 140-4:268; layout_before_sites.json:370 140-4:269 | ;  |  |
| 944 | pending | layout_before_sites.json:370 140-4:269; layout_before_sites.json:371 140-4:270; layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:286 140-4:271; layout_repairs_applied.json:288 140-4:271 | ;  |  |
| 945 | pending | layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_before_sites.json:374 140-4:272; layout_before_sites.json:375 140-4:273; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:286 140-4:271; layout_repairs_applied.json:288 140-4:271 | ;  |  |
| 946 | pending | layout_before_sites.json:375 140-4:273; layout_before_sites.json:376 140-4:274; layout_before_sites.json:377 140-4:275 | ;  |  |
| 947 | pending | layout_before_sites.json:377 140-4:275; layout_before_sites.json:378 140-4:276; layout_before_sites.json:379 140-4:277; layout_repairs_applied.json:287 140-4:276 | ;  |  |
| 948 | pending | layout_before_sites.json:379 140-4:277; layout_before_sites.json:380 140-4:278; layout_before_sites.json:381 140-4:279 | ;  |  |
| 949 | pending | evenly spaced sample; layout_before_sites.json:381 140-4:279; layout_before_sites.json:382 140-4:280 | ;  |  |

### LM_EN_corrected_apparatus.pdf

PDF SHA-256: `7a082c2e9caa80bd959a73da61f7f941c7608897701c89d1b92d6dd02abc600f`.

| Physical page | Status | Selection reason | Reviewer and inspection basis | Observation |
|---|---|---|---|---|
| 1 | reviewed | evenly spaced sample | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page sheet: centered author, title, edition name, archive attribution and date are separated cleanly; no title-line clipping. |
| 6 | pending | layout_before_sites.json:1 140-1:4 | ;  |  |
| 7 | reviewed | layout_before_sites.json:1 140-1:4 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page sheet: aligned product calculations and boxed conclusion remain legible; the diagrams, right marginal reading and lower apparatus have distinct spacing. |
| 8 | reviewed | layout_before_sites.json:1 140-1:4 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page sheet: long blue uncertainty alternatives wrap in the main text; the right marginal subgroup note stays separate, and the stacked equations do not collide with the footer. |
| 10 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:294 140-1:10 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page sheet: the marginal note uses its own full-width block; vertical and horizontal group-extension diagrams are contained and the apparatus starts below them. |
| 11 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:294 140-1:10 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page sheet and full900px page: the dense scan10 diagram is contained; the raised subgroup annotation is separate from the curved arrows, the Cart labels remain readable, and the lower group formulas and footer are clear. |
| 12 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:294 140-1:10 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | At 900px, the pr_1 label is separate from the descending diagonal in the large branching diagram; all source strokes and the following scan apparatus fit.; Actual native 6x crop inspected: C1:10 lattice, repaired pr_1 label lies above horizontal arrow and to the right of crossing diagonal; object glyphs/arrowheads clear. Source cancellation stroke at left retained. No new defect. |
| 13 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:292 140-1:12; layout_repairs_applied.json:294 140-1:10 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page sheet: the top apparatus and marginal-note block are distinct from the later commutative diagram; its lower formulas and page number remain clear.; Full900px inspected: repaired C1:12 vertical/long horizontal group diagram has clear object and arrow spacing; no labels touch strokes. |
| 14 | reviewed | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:292 140-1:12 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page close sheet: the tall bracketed fraction calculation remains within the text block; the marginal-note formulas and apparatus underneath have separate baselines.; Full900px inspected: nested underbrace calculation, marginal equations and apparatus remain distinct. |
| 15 | reviewed | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:292 140-1:12 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page close sheet: apparatus entries finish above scan13/14 labels; paired equations and congruence lines below remain separated and inside the page. |
| 16 | reviewed | layout_before_sites.json:8 140-1:15 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page close sheet: the modular calculations, marginal-note block and preserved printed ARTICLE5 text are distinct; the apparatus and bottom page number are not overprinted. |
| 17 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:8 140-1:15; layout_before_sites.json:9 140-1:16 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page close sheet: printed ARTICLE6 continuation precedes a large cancelled-math apparatus entry; the later small pullback square and right marginal note remain separate. |
| 18 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:9 140-1:16 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The half-plane sketch and three-row group diagram fit. Notes m22/m23/m25/m26 start with content; m27’s origin marker remains at the bottom before its following-page sketch. |
| 19 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:9 140-1:16 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The m27 heading and complete source arrow sketch share this page. The following extension paragraph and scan16 apparatus entries fit, with cancellation doubts visibly retained. |
| 20 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:13 140-1:17; layout_before_sites.json:9 140-1:16 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Scan17’s deletion references and surviving note m29 remain visible above the apparatus. The cancelled branching diagram and cancelled formulas are contained in their entries with kinds and reasons. |
| 21 | reviewed | layout_before_sites.json:13 140-1:17; layout_before_sites.json:14 140-1:18; layout_pass_sites.json:31 140-1:18 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page sheet and full900px page: the apparatus diagrams and incidence-relation rows are contained; the scan18 opening equation stays above the page number with a clear lower margin. |
| 22 | reviewed | layout_before_sites.json:14 140-1:18; layout_pass_sites.json:31 140-1:18 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page close sheet: the central multirow group diagram is contained, with the two marginal-note blocks and following apparatus separated. |
| 23 | reviewed | layout_before_sites.json:14 140-1:18; layout_before_sites.json:15 140-1:19; layout_pass_sites.json:31 140-1:18; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:54 140-1:19; layout_repairs_applied.json:293 140-1:19 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page close sheet: the scan19 manuscript drawing is wholly inside the page, including its left circle and long sloping boundary strokes; dense labels will also be checked at full-page size.; Full-page 900-pixel inspection: the locally reduced physical drawing for scan 19, including its long oblique strokes, left circular figure, right curve tip and bottom labels, is entirely on the page and separated from the apparatus rule. No stroke is clipped. |
| 24 | pending | layout_before_sites.json:15 140-1:19; layout_before_sites.json:16 140-1:20; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:54 140-1:19; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:293 140-1:19; layout_repairs_applied.json:297 140-1:20; layout_repairs_applied.json:302 140-1:20 | ;  |  |
| 25 | pending | layout_before_sites.json:16 140-1:20; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:297 140-1:20; layout_repairs_applied.json:302 140-1:20 | ;  |  |
| 27 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23 | ;  |  |
| 28 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23 | ;  |  |
| 29 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23; layout_repairs_applied.json:303 140-1:25 | ;  |  |
| 32 | pending | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | ;  |  |
| 33 | reviewed | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page close sheet: the short matrix calculations and marginal-note formula are clear; the lower apparatus preserves the cancelled relations without intruding into the footer. |
| 34 | reviewed | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page close sheet: the large lower commutative diagram has visible node gaps and stays inside the body; preceding cancelled equations and prose do not overprint it. |
| 35 | pending | layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | ;  |  |
| 36 | pending | layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | ;  |  |
| 40 | reviewed | evenly spaced sample | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page sheet: wide extension sequences fit; the group presentation and bottom apparatus retain clear vertical separation. |
| 41 | reviewed | layout_before_sites.json:23 140-1:36; layout_before_sites.json:24 140-1:36; layout_pass_sites.json:34 140-1:36; layout_pass_sites.json:56 140-1:36; layout_repairs_applied.json:298 140-1:36 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page close sheet: the multirow scan36 diagram, full-width marginal note and short apparatus are contained; scan37 and its manuscript page number are clearly visible.; Full900px inspected: repaired C1:36 group diagram and lower quotient map are contained; broad upward arrows, scalar labels and objects remain separated. |
| 42 | reviewed | layout_before_sites.json:25 140-2:4 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page sheet: the cote140-2 contents list wraps cleanly and keeps its right page-number column; the midpage apparatus and continuation are distinct. |
| 43 | reviewed | layout_before_sites.json:25 140-2:4 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Four-page sheet: the contents continuation, authorial brace description and apparatus remain inside the page; the next section heading and right marginal readings are visible at the foot. |
| 59 | pending | layout_before_sites.json:26 140-2:28; layout_before_sites.json:27 140-2:29 | ;  |  |
| 60 | pending | layout_before_sites.json:27 140-2:29 | ;  |  |
| 65 | reviewed | layout_before_sites.json:28 140-2:35 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview 003: boxed formula, short right note and apparatus align within their allotted areas; no visible overlap. |
| 69 | reviewed | layout_before_sites.json:29 140-2:39 | assistant/glossary; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Overview 003: boxed morphisms and the two-row marginal diagram fit the body; apparatus starts below its separating rule. |
| 70 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 72 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 73 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 74 | pending | layout_before_sites.json:30 140-2:42; layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44 | ;  |  |
| 75 | pending | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44 | ;  |  |
| 76 | pending | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44; layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | ;  |  |
| 77 | pending | layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | ;  |  |
| 80 | pending | evenly spaced sample | ;  |  |
| 94 | pending | layout_before_sites.json:35 140-2:69 | ;  |  |
| 95 | pending | layout_before_sites.json:35 140-2:69 | ;  |  |
| 104 | pending | layout_before_sites.json:36 140-2:80 | ;  |  |
| 110 | pending | layout_before_sites.json:37 140-2:88 | ;  |  |
| 111 | pending | layout_before_sites.json:37 140-2:88; layout_repairs_applied.json:304 140-2:89 | ;  |  |
| 112 | pending | layout_repairs_applied.json:304 140-2:89 | ;  |  |
| 119 | pending | evenly spaced sample | ;  |  |
| 139 | pending | layout_before_sites.json:38 140-2:122 | ;  |  |
| 140 | pending | layout_before_sites.json:38 140-2:122 | ;  |  |
| 145 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 146 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 155 | pending | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | ;  |  |
| 156 | pending | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | ;  |  |
| 159 | pending | evenly spaced sample | ;  |  |
| 162 | pending | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | ;  |  |
| 163 | pending | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | ;  |  |
| 172 | pending | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | ;  |  |
| 173 | pending | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | ;  |  |
| 175 | pending | layout_before_sites.json:46 140-2:162 | ;  |  |
| 176 | pending | layout_before_sites.json:46 140-2:162 | ;  |  |
| 177 | pending | layout_before_sites.json:47 140-2:164 | ;  |  |
| 178 | pending | layout_before_sites.json:47 140-2:164; layout_before_sites.json:48 140-2:165; layout_repairs_applied.json:306 140-2:165 | ;  |  |
| 179 | pending | layout_before_sites.json:48 140-2:165; layout_before_sites.json:49 140-2:166; layout_repairs_applied.json:306 140-2:165 | ;  |  |
| 180 | pending | layout_before_sites.json:49 140-2:166 | ;  |  |
| 198 | pending | evenly spaced sample | ;  |  |
| 203 | pending | layout_before_sites.json:50 140-2:197 | ;  |  |
| 204 | pending | layout_before_sites.json:50 140-2:197 | ;  |  |
| 208 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205 | ;  |  |
| 209 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205; layout_repairs_applied.json:307 140-2:206 | ;  |  |
| 210 | pending | layout_repairs_applied.json:307 140-2:206 | ;  |  |
| 214 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 215 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 216 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 221 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 222 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 223 | pending | layout_before_sites.json:57 140-2:220 | ;  |  |
| 224 | pending | layout_before_sites.json:57 140-2:220 | ;  |  |
| 225 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 226 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 235 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 236 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 238 | pending | evenly spaced sample | ;  |  |
| 250 | pending | layout_repairs_applied.json:310 140-2:251 | ;  |  |
| 251 | pending | layout_repairs_applied.json:308 140-2:252; layout_repairs_applied.json:309 140-2:252; layout_repairs_applied.json:310 140-2:251; layout_repairs_applied.json:311 140-2:252 | ;  |  |
| 252 | pending | layout_repairs_applied.json:308 140-2:252; layout_repairs_applied.json:309 140-2:252; layout_repairs_applied.json:311 140-2:252 | ;  |  |
| 258 | pending | layout_before_sites.json:60 140-2:259 | ;  |  |
| 259 | pending | layout_before_sites.json:60 140-2:259 | ;  |  |
| 265 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 266 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 273 | pending | layout_before_sites.json:62 140-2:280 | ;  |  |
| 274 | pending | layout_before_sites.json:62 140-2:280 | ;  |  |
| 277 | pending | evenly spaced sample; layout_before_sites.json:63 140-2:285 | ;  |  |
| 278 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 279 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 293 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:313 140-2:302 | ;  |  |
| 294 | pending | landscape page; layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:313 140-2:302 | ;  |  |
| 295 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:313 140-2:302 | ;  |  |
| 301 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 302 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 303 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 310 | pending | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:315 140-2:321 | ;  |  |
| 311 | pending | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:315 140-2:321 | ;  |  |
| 317 | pending | evenly spaced sample; layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:314 140-2:328 | ;  |  |
| 318 | pending | layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_before_sites.json:71 140-2:329; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:314 140-2:328 | ;  |  |
| 319 | pending | layout_before_sites.json:71 140-2:329 | ;  |  |
| 320 | pending | layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:316 140-2:331; layout_repairs_applied.json:317 140-2:331 | ;  |  |
| 321 | pending | layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:316 140-2:331; layout_repairs_applied.json:317 140-2:331 | ;  |  |
| 333 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 334 | pending | landscape page; layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 335 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 336 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 337 | pending | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | ;  |  |
| 338 | pending | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | ;  |  |
| 340 | pending | layout_before_sites.json:75 140-2:348; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:318 140-2:348 | ;  |  |
| 341 | pending | layout_before_sites.json:75 140-2:348; layout_before_sites.json:76 140-2:349; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:318 140-2:348 | ;  |  |
| 342 | pending | layout_before_sites.json:76 140-2:349 | ;  |  |
| 344 | pending | layout_before_sites.json:77 140-2:352 | ;  |  |
| 345 | pending | layout_before_sites.json:77 140-2:352 | ;  |  |
| 352 | pending | layout_before_sites.json:78 140-2:362 | ;  |  |
| 353 | pending | layout_before_sites.json:78 140-2:362 | ;  |  |
| 356 | pending | evenly spaced sample | ;  |  |
| 360 | pending | layout_before_sites.json:79 140-2:371 | ;  |  |
| 361 | pending | layout_before_sites.json:79 140-2:371 | ;  |  |
| 368 | pending | layout_repairs_applied.json:322 140-2:382 | ;  |  |
| 369 | pending | layout_repairs_applied.json:322 140-2:382 | ;  |  |
| 370 | pending | layout_before_sites.json:80 140-2:384; layout_pass_sites.json:40 140-2:384; layout_pass_sites.json:64 140-2:384 | ;  |  |
| 372 | pending | layout_before_sites.json:81 140-2:387 | ;  |  |
| 373 | pending | layout_before_sites.json:81 140-2:387 | ;  |  |
| 380 | pending | layout_repairs_applied.json:323 140-2:397 | ;  |  |
| 385 | pending | layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404 | ;  |  |
| 386 | pending | layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404 | ;  |  |
| 387 | pending | layout_repairs_applied.json:324 140-2:407 | ;  |  |
| 390 | pending | layout_pass_sites.json:41 140-2:411 | ;  |  |
| 395 | pending | layout_repairs_applied.json:325 140-2:417; layout_repairs_applied.json:327 140-2:417 | ;  |  |
| 396 | pending | evenly spaced sample; layout_repairs_applied.json:325 140-2:417; layout_repairs_applied.json:327 140-2:417 | ;  |  |
| 397 | pending | layout_before_sites.json:84 140-2:419; layout_before_sites.json:85 140-2:419; layout_pass_sites.json:4 140-2:419; layout_pass_sites.json:42 140-2:419; layout_pass_sites.json:59 140-2:419; layout_pass_sites.json:65 140-2:419; layout_repairs_applied.json:326 140-2:419 | ;  |  |
| 398 | pending | layout_before_sites.json:84 140-2:419; layout_before_sites.json:85 140-2:419; layout_pass_sites.json:4 140-2:419; layout_pass_sites.json:42 140-2:419; layout_pass_sites.json:59 140-2:419; layout_pass_sites.json:65 140-2:419; layout_repairs_applied.json:326 140-2:419 | ;  |  |
| 400 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 401 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 402 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 407 | pending | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | ;  |  |
| 408 | pending | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | ;  |  |
| 418 | pending | layout_before_sites.json:89 140-2:443 | ;  |  |
| 419 | pending | layout_before_sites.json:89 140-2:443 | ;  |  |
| 424 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 425 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 426 | pending | layout_before_sites.json:90 140-2:450; layout_before_sites.json:91 140-2:452 | ;  |  |
| 427 | pending | layout_before_sites.json:91 140-2:452 | ;  |  |
| 428 | pending | layout_before_sites.json:91 140-2:452 | ;  |  |
| 429 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 430 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 431 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 432 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 433 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 434 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 435 | pending | evenly spaced sample | ;  |  |
| 438 | pending | layout_before_sites.json:94 140-2:462 | ;  |  |
| 439 | pending | layout_before_sites.json:94 140-2:462 | ;  |  |
| 461 | pending | layout_before_sites.json:95 140-2:492 | ;  |  |
| 462 | pending | layout_before_sites.json:95 140-2:492 | ;  |  |
| 469 | pending | layout_before_sites.json:96 140-2:502 | ;  |  |
| 472 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:328 140-2:508 | ;  |  |
| 473 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:328 140-2:508 | ;  |  |
| 474 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:328 140-2:508 | ;  |  |
| 475 | pending | evenly spaced sample | ;  |  |
| 477 | pending | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | ;  |  |
| 478 | pending | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | ;  |  |
| 483 | pending | layout_before_sites.json:101 140-2:519; layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:330 140-2:520 | ;  |  |
| 484 | pending | layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:330 140-2:520 | ;  |  |
| 485 | pending | layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:330 140-2:520 | ;  |  |
| 489 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:331 140-2:527 | ;  |  |
| 490 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:331 140-2:527 | ;  |  |
| 493 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | ;  |  |
| 494 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | ;  |  |
| 496 | pending | layout_before_sites.json:107 140-2:536 | ;  |  |
| 514 | pending | evenly spaced sample | ;  |  |
| 521 | pending | layout_before_sites.json:108 140-2:567 | ;  |  |
| 522 | pending | layout_before_sites.json:108 140-2:567; layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:332 140-2:568; layout_repairs_applied.json:333 140-2:568 | ;  |  |
| 523 | pending | layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:332 140-2:568; layout_repairs_applied.json:333 140-2:568 | ;  |  |
| 532 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | ;  |  |
| 533 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | ;  |  |
| 534 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4; layout_before_sites.json:114 140-3:5 | ;  |  |
| 535 | pending | layout_before_sites.json:114 140-3:5; layout_repairs_applied.json:334 140-3:6 | ;  |  |
| 536 | pending | layout_repairs_applied.json:334 140-3:6 | ;  |  |
| 541 | pending | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | ;  |  |
| 542 | pending | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | ;  |  |
| 546 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 547 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 548 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 549 | pending | layout_repairs_applied.json:335 140-3:21 | ;  |  |
| 551 | pending | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | ;  |  |
| 552 | pending | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | ;  |  |
| 553 | pending | evenly spaced sample | ;  |  |
| 557 | pending | layout_repairs_applied.json:336 140-3:33 | ;  |  |
| 558 | pending | layout_repairs_applied.json:336 140-3:33 | ;  |  |
| 560 | pending | layout_before_sites.json:124 140-3:36 | ;  |  |
| 561 | pending | layout_before_sites.json:124 140-3:36 | ;  |  |
| 563 | pending | layout_repairs_applied.json:337 140-3:40; layout_repairs_applied.json:338 140-3:41 | ;  |  |
| 564 | pending | layout_repairs_applied.json:338 140-3:41 | ;  |  |
| 565 | pending | layout_repairs_applied.json:339 140-3:44 | ;  |  |
| 566 | pending | layout_repairs_applied.json:339 140-3:44 | ;  |  |
| 571 | pending | layout_repairs_applied.json:340 140-3:55 | ;  |  |
| 572 | pending | layout_repairs_applied.json:340 140-3:55; layout_repairs_applied.json:341 140-3:56 | ;  |  |
| 573 | pending | layout_before_sites.json:125 140-3:58; layout_repairs_applied.json:341 140-3:56 | ;  |  |
| 574 | pending | layout_before_sites.json:125 140-3:58; layout_before_sites.json:126 140-3:59 | ;  |  |
| 575 | pending | layout_before_sites.json:126 140-3:59 | ;  |  |
| 576 | pending | layout_before_sites.json:126 140-3:59 | ;  |  |
| 578 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 579 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 583 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 584 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 589 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 590 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 591 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 592 | pending | layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75 | ;  |  |
| 593 | pending | evenly spaced sample; layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75; layout_before_sites.json:133 140-3:76 | ;  |  |
| 594 | pending | layout_before_sites.json:133 140-3:76 | ;  |  |
| 602 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:342 140-3:85; layout_repairs_applied.json:343 140-3:85; layout_repairs_applied.json:344 140-3:85; layout_repairs_applied.json:345 140-3:85; layout_repairs_applied.json:346 140-3:85; layout_repairs_applied.json:347 140-3:85; layout_repairs_applied.json:348 140-3:85 | ;  |  |
| 603 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:342 140-3:85; layout_repairs_applied.json:343 140-3:85; layout_repairs_applied.json:344 140-3:85; layout_repairs_applied.json:345 140-3:85; layout_repairs_applied.json:346 140-3:85; layout_repairs_applied.json:347 140-3:85; layout_repairs_applied.json:348 140-3:85 | ;  |  |
| 604 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_before_sites.json:136 140-3:86; layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:342 140-3:85; layout_repairs_applied.json:343 140-3:85; layout_repairs_applied.json:344 140-3:85; layout_repairs_applied.json:345 140-3:85; layout_repairs_applied.json:346 140-3:85; layout_repairs_applied.json:347 140-3:85; layout_repairs_applied.json:348 140-3:85 | ;  |  |
| 605 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87 | ;  |  |
| 606 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:349 140-3:88 | ;  |  |
| 607 | pending | layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:349 140-3:88 | ;  |  |
| 608 | pending | layout_before_sites.json:139 140-3:90 | ;  |  |
| 609 | pending | layout_before_sites.json:139 140-3:90 | ;  |  |
| 610 | pending | layout_before_sites.json:139 140-3:90; layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91 | ;  |  |
| 611 | pending | layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91; layout_before_sites.json:145 140-3:92 | ;  |  |
| 612 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 613 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 616 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 617 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 618 | pending | layout_repairs_applied.json:350 140-3:97; layout_repairs_applied.json:356 140-3:97 | ;  |  |
| 619 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98; layout_repairs_applied.json:350 140-3:97; layout_repairs_applied.json:356 140-3:97 | ;  |  |
| 620 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98 | ;  |  |
| 628 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:351 140-3:107; layout_repairs_applied.json:352 140-3:107; layout_repairs_applied.json:353 140-3:107; layout_repairs_applied.json:354 140-3:107; layout_repairs_applied.json:355 140-3:107 | ;  |  |
| 629 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:351 140-3:107; layout_repairs_applied.json:352 140-3:107; layout_repairs_applied.json:353 140-3:107; layout_repairs_applied.json:354 140-3:107; layout_repairs_applied.json:355 140-3:107 | ;  |  |
| 632 | pending | evenly spaced sample | ;  |  |
| 634 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 635 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 643 | pending | layout_repairs_applied.json:357 140-3:121 | ;  |  |
| 644 | pending | layout_repairs_applied.json:357 140-3:121 | ;  |  |
| 645 | pending | layout_repairs_applied.json:357 140-3:121 | ;  |  |
| 671 | pending | layout_before_sites.json:154 140-3:148 | ;  |  |
| 672 | pending | evenly spaced sample; layout_before_sites.json:154 140-3:148 | ;  |  |
| 678 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 679 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 682 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 683 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 708 | pending | layout_before_sites.json:157 140-3:185 | ;  |  |
| 709 | pending | layout_before_sites.json:157 140-3:185; layout_repairs_applied.json:358 140-3:186 | ;  |  |
| 710 | pending | layout_repairs_applied.json:358 140-3:186 | ;  |  |
| 711 | pending | evenly spaced sample | ;  |  |
| 713 | pending | layout_before_sites.json:158 140-3:191; layout_before_sites.json:159 140-3:191 | ;  |  |
| 714 | pending | layout_before_sites.json:158 140-3:191; layout_before_sites.json:159 140-3:191; layout_before_sites.json:160 140-3:192 | ;  |  |
| 715 | pending | layout_before_sites.json:160 140-3:192 | ;  |  |
| 716 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 717 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 721 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 722 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 730 | pending | layout_repairs_applied.json:359 140-3:208 | ;  |  |
| 731 | pending | layout_repairs_applied.json:359 140-3:208; layout_repairs_applied.json:360 140-3:209 | ;  |  |
| 732 | pending | layout_repairs_applied.json:360 140-3:209 | ;  |  |
| 734 | pending | layout_before_sites.json:164 140-3:212 | ;  |  |
| 735 | pending | layout_before_sites.json:164 140-3:212; layout_before_sites.json:165 140-3:213 | ;  |  |
| 736 | pending | layout_before_sites.json:165 140-3:213; layout_before_sites.json:166 140-3:215 | ;  |  |
| 737 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 738 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 743 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_repairs_applied.json:361 140-3:221 | ;  |  |
| 744 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_before_sites.json:169 140-3:222; layout_repairs_applied.json:361 140-3:221 | ;  |  |
| 745 | pending | layout_before_sites.json:169 140-3:222 | ;  |  |
| 746 | pending | layout_before_sites.json:169 140-3:222 | ;  |  |
| 751 | pending | evenly spaced sample | ;  |  |
| 754 | pending | layout_before_sites.json:170 140-3:231 | ;  |  |
| 755 | pending | layout_before_sites.json:170 140-3:231; layout_before_sites.json:171 140-3:232 | ;  |  |
| 756 | pending | layout_before_sites.json:171 140-3:232 | ;  |  |
| 766 | pending | layout_repairs_applied.json:362 140-3:245 | ;  |  |
| 767 | pending | layout_repairs_applied.json:362 140-3:245 | ;  |  |
| 778 | pending | layout_repairs_applied.json:363 140-3:261 | ;  |  |
| 779 | pending | layout_repairs_applied.json:363 140-3:261 | ;  |  |
| 780 | pending | layout_repairs_applied.json:363 140-3:261 | ;  |  |
| 790 | pending | evenly spaced sample | ;  |  |
| 792 | pending | layout_repairs_applied.json:364 140-3:275 | ;  |  |
| 793 | pending | layout_repairs_applied.json:364 140-3:275 | ;  |  |
| 798 | pending | layout_before_sites.json:172 140-3:282 | ;  |  |
| 799 | pending | layout_before_sites.json:172 140-3:282 | ;  |  |
| 800 | pending | layout_before_sites.json:172 140-3:282; layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 801 | pending | layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 821 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 822 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 830 | pending | evenly spaced sample | ;  |  |
| 839 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:365 140-3:320 | ;  |  |
| 840 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:365 140-3:320 | ;  |  |
| 841 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:365 140-3:320 | ;  |  |
| 842 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 843 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 844 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 847 | pending | layout_before_sites.json:179 140-3:327 | ;  |  |
| 848 | pending | layout_before_sites.json:179 140-3:327; layout_before_sites.json:180 140-3:328; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:366 140-3:328 | ;  |  |
| 849 | pending | layout_before_sites.json:180 140-3:328; layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:73 140-3:329; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:366 140-3:328; layout_repairs_applied.json:367 140-3:329 | ;  |  |
| 850 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:367 140-3:329 | ;  |  |
| 851 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:367 140-3:329 | ;  |  |
| 855 | pending | layout_before_sites.json:182 140-3:334 | ;  |  |
| 856 | pending | layout_before_sites.json:182 140-3:334 | ;  |  |
| 857 | pending | layout_before_sites.json:182 140-3:334; layout_repairs_applied.json:369 140-3:335 | ;  |  |
| 858 | pending | layout_repairs_applied.json:369 140-3:335 | ;  |  |
| 869 | pending | evenly spaced sample; layout_before_sites.json:183 140-3:346 | ;  |  |
| 870 | pending | layout_before_sites.json:183 140-3:346 | ;  |  |
| 878 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 879 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 882 | pending | layout_before_sites.json:185 140-3:356 | ;  |  |
| 883 | pending | layout_before_sites.json:185 140-3:356; layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357 | ;  |  |
| 884 | pending | layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357; layout_repairs_applied.json:370 140-3:358 | ;  |  |
| 885 | pending | layout_repairs_applied.json:370 140-3:358 | ;  |  |
| 886 | pending | layout_repairs_applied.json:370 140-3:358 | ;  |  |
| 889 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362 | ;  |  |
| 890 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362; layout_repairs_applied.json:373 140-3:363 | ;  |  |
| 891 | pending | layout_repairs_applied.json:373 140-3:363 | ;  |  |
| 892 | pending | layout_repairs_applied.json:373 140-3:363 | ;  |  |
| 907 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 908 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 909 | pending | evenly spaced sample | ;  |  |
| 918 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 919 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 920 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 939 | pending | layout_repairs_applied.json:380 140-3:408; layout_repairs_applied.json:381 140-3:408; layout_repairs_applied.json:382 140-3:408 | ;  |  |
| 940 | pending | layout_repairs_applied.json:380 140-3:408; layout_repairs_applied.json:381 140-3:408; layout_repairs_applied.json:382 140-3:408 | ;  |  |
| 941 | pending | layout_repairs_applied.json:383 140-3:410 | ;  |  |
| 942 | pending | layout_repairs_applied.json:383 140-3:410 | ;  |  |
| 943 | pending | layout_repairs_applied.json:383 140-3:410 | ;  |  |
| 945 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 946 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 947 | pending | layout_before_sites.json:192 140-3:415 | ;  |  |
| 948 | pending | evenly spaced sample; layout_before_sites.json:192 140-3:415; layout_before_sites.json:193 140-3:416 | ;  |  |
| 949 | pending | layout_before_sites.json:193 140-3:416 | ;  |  |
| 950 | pending | layout_before_sites.json:193 140-3:416 | ;  |  |
| 951 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:387 140-3:419 | ;  |  |
| 952 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:387 140-3:419 | ;  |  |
| 953 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:387 140-3:419 | ;  |  |
| 958 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:384 140-3:425 | ;  |  |
| 959 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:384 140-3:425 | ;  |  |
| 960 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:384 140-3:425 | ;  |  |
| 962 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 963 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 964 | pending | layout_before_sites.json:197 140-3:431 | ;  |  |
| 965 | pending | layout_before_sites.json:197 140-3:431 | ;  |  |
| 966 | pending | layout_before_sites.json:197 140-3:431; layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432 | ;  |  |
| 967 | pending | layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432; layout_before_sites.json:200 140-3:433 | ;  |  |
| 968 | pending | layout_before_sites.json:200 140-3:433 | ;  |  |
| 969 | pending | layout_before_sites.json:200 140-3:433 | ;  |  |
| 971 | pending | layout_repairs_applied.json:396 140-3:436; layout_repairs_applied.json:397 140-3:436; layout_repairs_applied.json:398 140-3:436 | ;  |  |
| 972 | pending | layout_repairs_applied.json:396 140-3:436; layout_repairs_applied.json:397 140-3:436; layout_repairs_applied.json:398 140-3:436 | ;  |  |
| 973 | pending | layout_repairs_applied.json:396 140-3:436; layout_repairs_applied.json:397 140-3:436; layout_repairs_applied.json:398 140-3:436; layout_repairs_applied.json:399 140-3:437; layout_repairs_applied.json:400 140-3:437 | ;  |  |
| 974 | pending | layout_repairs_applied.json:399 140-3:437; layout_repairs_applied.json:400 140-3:437; layout_repairs_applied.json:401 140-3:438; layout_repairs_applied.json:402 140-3:438; layout_repairs_applied.json:403 140-3:438; layout_repairs_applied.json:404 140-3:438 | ;  |  |
| 975 | pending | layout_repairs_applied.json:401 140-3:438; layout_repairs_applied.json:402 140-3:438; layout_repairs_applied.json:403 140-3:438; layout_repairs_applied.json:404 140-3:438 | ;  |  |
| 976 | pending | layout_repairs_applied.json:401 140-3:438; layout_repairs_applied.json:402 140-3:438; layout_repairs_applied.json:403 140-3:438; layout_repairs_applied.json:404 140-3:438; layout_repairs_applied.json:405 140-3:439 | ;  |  |
| 977 | pending | layout_repairs_applied.json:388 140-3:440; layout_repairs_applied.json:392 140-3:441; layout_repairs_applied.json:405 140-3:439; layout_repairs_applied.json:406 140-3:440 | ;  |  |
| 978 | pending | layout_repairs_applied.json:392 140-3:441 | ;  |  |
| 979 | pending | layout_repairs_applied.json:392 140-3:441; layout_repairs_applied.json:395 140-3:443 | ;  |  |
| 980 | pending | layout_before_sites.json:201 140-3:444; layout_repairs_applied.json:395 140-3:443 | ;  |  |
| 981 | pending | layout_before_sites.json:201 140-3:444 | ;  |  |
| 983 | pending | layout_pass_sites.json:12 140-3:446; layout_repairs_applied.json:390 140-3:446 | ;  |  |
| 984 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:12 140-3:446; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:389 140-3:448; layout_repairs_applied.json:390 140-3:446 | ;  |  |
| 985 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:389 140-3:448; layout_repairs_applied.json:393 140-3:449; layout_repairs_applied.json:394 140-3:449 | ;  |  |
| 986 | pending | layout_repairs_applied.json:393 140-3:449; layout_repairs_applied.json:394 140-3:449 | ;  |  |
| 987 | pending | layout_repairs_applied.json:393 140-3:449; layout_repairs_applied.json:394 140-3:449 | ;  |  |
| 988 | pending | evenly spaced sample | ;  |  |
| 990 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 991 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 992 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 996 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 997 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 1000 | pending | layout_repairs_applied.json:407 140-3:462; layout_repairs_applied.json:408 140-3:463; layout_repairs_applied.json:409 140-3:463; layout_repairs_applied.json:410 140-3:463 | ;  |  |
| 1001 | pending | layout_repairs_applied.json:408 140-3:463; layout_repairs_applied.json:409 140-3:463; layout_repairs_applied.json:410 140-3:463 | ;  |  |
| 1002 | pending | layout_repairs_applied.json:408 140-3:463; layout_repairs_applied.json:409 140-3:463; layout_repairs_applied.json:410 140-3:463 | ;  |  |
| 1003 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 1004 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 1005 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 1006 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 1007 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 1008 | pending | layout_before_sites.json:208 140-3:468; layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 1009 | pending | layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 1018 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 1019 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 1020 | pending | layout_before_sites.json:211 140-3:479; layout_repairs_applied.json:411 140-3:480; layout_repairs_applied.json:412 140-3:480 | ;  |  |
| 1021 | pending | layout_repairs_applied.json:411 140-3:480; layout_repairs_applied.json:412 140-3:480 | ;  |  |
| 1024 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1025 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1026 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1027 | pending | evenly spaced sample | ;  |  |
| 1029 | pending | layout_before_sites.json:213 140-3:491 | ;  |  |
| 1030 | pending | layout_before_sites.json:213 140-3:491; layout_before_sites.json:214 140-3:492 | ;  |  |
| 1031 | pending | layout_before_sites.json:214 140-3:492 | ;  |  |
| 1032 | pending | layout_repairs_applied.json:413 140-3:494 | ;  |  |
| 1033 | pending | layout_repairs_applied.json:413 140-3:494 | ;  |  |
| 1038 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 1039 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 1042 | pending | layout_repairs_applied.json:415 140-3:503 | ;  |  |
| 1043 | pending | layout_repairs_applied.json:415 140-3:503 | ;  |  |
| 1044 | pending | layout_repairs_applied.json:415 140-3:503 | ;  |  |
| 1047 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:416 140-3:506; layout_repairs_applied.json:417 140-3:506 | ;  |  |
| 1048 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:416 140-3:506; layout_repairs_applied.json:417 140-3:506 | ;  |  |
| 1050 | pending | layout_before_sites.json:217 140-3:509 | ;  |  |
| 1051 | pending | layout_before_sites.json:217 140-3:509 | ;  |  |
| 1052 | pending | layout_before_sites.json:217 140-3:509; layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1053 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1054 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1058 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 1059 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 1062 | pending | layout_before_sites.json:221 140-3:517 | ;  |  |
| 1063 | pending | layout_before_sites.json:221 140-3:517; layout_before_sites.json:222 140-3:518 | ;  |  |
| 1064 | pending | layout_before_sites.json:222 140-3:518; layout_before_sites.json:223 140-3:519; layout_repairs_applied.json:418 140-3:519; layout_repairs_applied.json:423 140-3:519 | ;  |  |
| 1065 | pending | layout_before_sites.json:223 140-3:519; layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:418 140-3:519; layout_repairs_applied.json:422 140-3:520; layout_repairs_applied.json:423 140-3:519 | ;  |  |
| 1066 | pending | evenly spaced sample; layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:422 140-3:520 | ;  |  |
| 1067 | pending | layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:422 140-3:520 | ;  |  |
| 1068 | pending | layout_before_sites.json:225 140-3:522 | ;  |  |
| 1069 | pending | layout_before_sites.json:225 140-3:522 | ;  |  |
| 1070 | pending | layout_before_sites.json:225 140-3:522; layout_repairs_applied.json:424 140-3:523 | ;  |  |
| 1071 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:424 140-3:523; layout_repairs_applied.json:425 140-3:524; layout_repairs_applied.json:426 140-3:524 | ;  |  |
| 1072 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:425 140-3:524; layout_repairs_applied.json:426 140-3:524 | ;  |  |
| 1073 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:419 140-3:525; layout_repairs_applied.json:425 140-3:524; layout_repairs_applied.json:426 140-3:524; layout_repairs_applied.json:427 140-3:525; layout_repairs_applied.json:428 140-3:525 | ;  |  |
| 1074 | pending | layout_repairs_applied.json:419 140-3:525; layout_repairs_applied.json:427 140-3:525; layout_repairs_applied.json:428 140-3:525 | ;  |  |
| 1078 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530 | ;  |  |
| 1079 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530 | ;  |  |
| 1080 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530; layout_before_sites.json:229 140-3:531 | ;  |  |
| 1081 | pending | layout_before_sites.json:229 140-3:531; layout_before_sites.json:230 140-3:532 | ;  |  |
| 1082 | pending | layout_before_sites.json:230 140-3:532; layout_before_sites.json:231 140-3:533 | ;  |  |
| 1083 | pending | layout_before_sites.json:231 140-3:533; layout_before_sites.json:232 140-3:534 | ;  |  |
| 1084 | pending | layout_before_sites.json:232 140-3:534 | ;  |  |
| 1085 | pending | layout_before_sites.json:232 140-3:534; layout_before_sites.json:233 140-3:535 | ;  |  |
| 1086 | pending | layout_before_sites.json:233 140-3:535; layout_before_sites.json:234 140-3:536; layout_repairs_applied.json:429 140-3:536 | ;  |  |
| 1087 | pending | layout_before_sites.json:234 140-3:536; layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_repairs_applied.json:429 140-3:536 | ;  |  |
| 1088 | pending | layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_before_sites.json:238 140-3:538 | ;  |  |
| 1089 | pending | layout_before_sites.json:238 140-3:538; layout_before_sites.json:239 140-3:539 | ;  |  |
| 1090 | pending | layout_before_sites.json:239 140-3:539; layout_before_sites.json:240 140-3:540 | ;  |  |
| 1091 | pending | layout_before_sites.json:240 140-3:540; layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 1092 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 1093 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541; layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:430 140-3:542; layout_repairs_applied.json:434 140-3:542 | ;  |  |
| 1094 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:430 140-3:542; layout_repairs_applied.json:434 140-3:542 | ;  |  |
| 1095 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_before_sites.json:245 140-3:543; layout_repairs_applied.json:430 140-3:542; layout_repairs_applied.json:434 140-3:542; layout_repairs_applied.json:435 140-3:543; layout_repairs_applied.json:436 140-3:543; layout_repairs_applied.json:437 140-3:543 | ;  |  |
| 1096 | pending | layout_before_sites.json:245 140-3:543; layout_repairs_applied.json:435 140-3:543; layout_repairs_applied.json:436 140-3:543; layout_repairs_applied.json:437 140-3:543 | ;  |  |
| 1097 | pending | layout_before_sites.json:245 140-3:543; layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:435 140-3:543; layout_repairs_applied.json:436 140-3:543; layout_repairs_applied.json:437 140-3:543; layout_repairs_applied.json:438 140-3:544; layout_repairs_applied.json:439 140-3:544 | ;  |  |
| 1098 | pending | layout_before_sites.json:246 140-3:544; layout_before_sites.json:247 140-3:545; layout_repairs_applied.json:431 140-3:545; layout_repairs_applied.json:432 140-3:545; layout_repairs_applied.json:438 140-3:544; layout_repairs_applied.json:439 140-3:544; layout_repairs_applied.json:440 140-3:545; layout_repairs_applied.json:441 140-3:545; layout_repairs_applied.json:442 140-3:545; layout_repairs_applied.json:443 140-3:545; layout_repairs_applied.json:444 140-3:545; layout_repairs_applied.json:445 140-3:545 | ;  |  |
| 1099 | pending | layout_before_sites.json:247 140-3:545; layout_repairs_applied.json:431 140-3:545; layout_repairs_applied.json:432 140-3:545; layout_repairs_applied.json:440 140-3:545; layout_repairs_applied.json:441 140-3:545; layout_repairs_applied.json:442 140-3:545; layout_repairs_applied.json:443 140-3:545; layout_repairs_applied.json:444 140-3:545; layout_repairs_applied.json:445 140-3:545 | ;  |  |
| 1100 | pending | layout_before_sites.json:247 140-3:545; layout_before_sites.json:248 140-3:546; layout_repairs_applied.json:431 140-3:545; layout_repairs_applied.json:432 140-3:545; layout_repairs_applied.json:433 140-3:546; layout_repairs_applied.json:440 140-3:545; layout_repairs_applied.json:441 140-3:545; layout_repairs_applied.json:442 140-3:545; layout_repairs_applied.json:443 140-3:545; layout_repairs_applied.json:444 140-3:545; layout_repairs_applied.json:445 140-3:545 | ;  |  |
| 1101 | pending | layout_before_sites.json:248 140-3:546; layout_before_sites.json:249 140-3:547; layout_repairs_applied.json:433 140-3:546 | ;  |  |
| 1102 | pending | layout_before_sites.json:249 140-3:547; layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:446 140-3:548 | ;  |  |
| 1103 | pending | layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:446 140-3:548 | ;  |  |
| 1106 | pending | evenly spaced sample | ;  |  |
| 1107 | pending | layout_before_sites.json:251 140-3:554; layout_repairs_applied.json:447 140-3:554 | ;  |  |
| 1108 | pending | layout_before_sites.json:251 140-3:554; layout_repairs_applied.json:447 140-3:554 | ;  |  |
| 1109 | pending | layout_before_sites.json:251 140-3:554; layout_before_sites.json:252 140-3:555; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:447 140-3:554; layout_repairs_applied.json:448 140-3:555 | ;  |  |
| 1110 | pending | layout_before_sites.json:252 140-3:555; layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:448 140-3:555; layout_repairs_applied.json:449 140-3:556 | ;  |  |
| 1111 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_repairs_applied.json:449 140-3:556 | ;  |  |
| 1112 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_before_sites.json:255 140-3:557; layout_pass_sites.json:14 140-3:557; layout_pass_sites.json:75 140-3:557; layout_repairs_applied.json:449 140-3:556; layout_repairs_applied.json:451 140-3:557 | ;  |  |
| 1113 | pending | layout_before_sites.json:255 140-3:557; layout_before_sites.json:256 140-3:558; layout_pass_sites.json:14 140-3:557; layout_pass_sites.json:75 140-3:557; layout_repairs_applied.json:451 140-3:557 | ;  |  |
| 1114 | pending | layout_before_sites.json:256 140-3:558; layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1115 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1116 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1117 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:452 140-3:561 | ;  |  |
| 1118 | pending | landscape page; layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:452 140-3:561 | ;  |  |
| 1119 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:452 140-3:561 | ;  |  |
| 1120 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:450 140-3:562; layout_repairs_applied.json:452 140-3:561; layout_repairs_applied.json:455 140-3:562; layout_repairs_applied.json:456 140-3:562 | ;  |  |
| 1121 | pending | layout_repairs_applied.json:450 140-3:562; layout_repairs_applied.json:455 140-3:562; layout_repairs_applied.json:456 140-3:562 | ;  |  |
| 1123 | pending | layout_repairs_applied.json:457 140-3:565 | ;  |  |
| 1124 | pending | layout_repairs_applied.json:457 140-3:565 | ;  |  |
| 1125 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567 | ;  |  |
| 1126 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567 | ;  |  |
| 1127 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567; layout_repairs_applied.json:458 140-3:568 | ;  |  |
| 1128 | pending | layout_repairs_applied.json:458 140-3:568 | ;  |  |
| 1130 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 1131 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 1133 | pending | layout_before_sites.json:263 140-3:573; layout_repairs_applied.json:459 140-3:573 | ;  |  |
| 1134 | pending | layout_before_sites.json:263 140-3:573; layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:459 140-3:573; layout_repairs_applied.json:460 140-3:574 | ;  |  |
| 1135 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:460 140-3:574 | ;  |  |
| 1136 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:460 140-3:574 | ;  |  |
| 1137 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:460 140-3:574; layout_repairs_applied.json:462 140-3:575 | ;  |  |
| 1138 | pending | layout_before_sites.json:265 140-3:577; layout_repairs_applied.json:462 140-3:575 | ;  |  |
| 1139 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 1140 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 1145 | pending | evenly spaced sample; layout_before_sites.json:266 140-3:582 | ;  |  |
| 1146 | pending | layout_before_sites.json:266 140-3:582 | ;  |  |
| 1148 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 1149 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 1150 | pending | layout_before_sites.json:267 140-3:585; layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 1151 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 1152 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586; layout_before_sites.json:270 140-3:587 | ;  |  |
| 1153 | pending | layout_before_sites.json:270 140-3:587 | ;  |  |
| 1154 | pending | layout_before_sites.json:270 140-3:587; layout_before_sites.json:271 140-3:588 | ;  |  |
| 1155 | pending | layout_before_sites.json:271 140-3:588 | ;  |  |
| 1156 | pending | layout_before_sites.json:271 140-3:588; layout_before_sites.json:272 140-3:589 | ;  |  |
| 1157 | pending | layout_before_sites.json:272 140-3:589; layout_repairs_applied.json:464 140-3:590 | ;  |  |
| 1158 | pending | layout_repairs_applied.json:464 140-3:590 | ;  |  |
| 1160 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 1161 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 1168 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 1169 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 1176 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:465 140-3:606 | ;  |  |
| 1177 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:465 140-3:606 | ;  |  |
| 1180 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:467 140-3:609 | ;  |  |
| 1185 | pending | evenly spaced sample | ;  |  |
| 1186 | pending | layout_before_sites.json:275 140-3:616 | ;  |  |
| 1187 | pending | layout_before_sites.json:275 140-3:616; layout_before_sites.json:276 140-3:617 | ;  |  |
| 1188 | pending | layout_before_sites.json:276 140-3:617 | ;  |  |
| 1189 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:468 140-3:619 | ;  |  |
| 1190 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:468 140-3:619 | ;  |  |
| 1192 | pending | layout_before_sites.json:278 140-3:621; layout_pass_sites.json:18 140-3:621; layout_repairs_applied.json:466 140-3:621; layout_repairs_applied.json:473 140-3:621; layout_repairs_applied.json:474 140-3:622; layout_repairs_applied.json:475 140-3:622; layout_repairs_applied.json:476 140-3:622; layout_repairs_applied.json:477 140-3:622; layout_repairs_applied.json:478 140-3:622 | ;  |  |
| 1193 | pending | layout_repairs_applied.json:474 140-3:622; layout_repairs_applied.json:475 140-3:622; layout_repairs_applied.json:476 140-3:622; layout_repairs_applied.json:477 140-3:622; layout_repairs_applied.json:478 140-3:622 | ;  |  |
| 1194 | pending | layout_repairs_applied.json:474 140-3:622; layout_repairs_applied.json:475 140-3:622; layout_repairs_applied.json:476 140-3:622; layout_repairs_applied.json:477 140-3:622; layout_repairs_applied.json:478 140-3:622; layout_repairs_applied.json:479 140-3:623; layout_repairs_applied.json:480 140-3:623 | ;  |  |
| 1195 | pending | layout_repairs_applied.json:479 140-3:623; layout_repairs_applied.json:480 140-3:623 | ;  |  |
| 1197 | pending | layout_before_sites.json:279 140-3:625 | ;  |  |
| 1198 | pending | layout_before_sites.json:280 140-3:627 | ;  |  |
| 1199 | pending | layout_before_sites.json:280 140-3:627; layout_repairs_applied.json:481 140-3:628 | ;  |  |
| 1200 | pending | layout_before_sites.json:281 140-3:629; layout_repairs_applied.json:481 140-3:628 | ;  |  |
| 1201 | pending | layout_before_sites.json:281 140-3:629 | ;  |  |
| 1202 | pending | layout_before_sites.json:281 140-3:629 | ;  |  |
| 1203 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 1204 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 1208 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:483 140-3:637; layout_repairs_applied.json:485 140-3:637 | ;  |  |
| 1209 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:482 140-3:638; layout_repairs_applied.json:483 140-3:637; layout_repairs_applied.json:485 140-3:637 | ;  |  |
| 1210 | pending | layout_repairs_applied.json:482 140-3:638 | ;  |  |
| 1220 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:496 140-3:649 | ;  |  |
| 1221 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:496 140-3:649 | ;  |  |
| 1224 | pending | evenly spaced sample; layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:486 140-3:653; layout_repairs_applied.json:497 140-3:653 | ;  |  |
| 1225 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:486 140-3:653; layout_repairs_applied.json:497 140-3:653 | ;  |  |
| 1228 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:498 140-3:656; layout_repairs_applied.json:499 140-3:656 | ;  |  |
| 1229 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:498 140-3:656; layout_repairs_applied.json:499 140-3:656 | ;  |  |
| 1230 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:498 140-3:656; layout_repairs_applied.json:499 140-3:656 | ;  |  |
| 1231 | pending | layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657 | ;  |  |
| 1232 | pending | layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_repairs_applied.json:487 140-3:658; layout_repairs_applied.json:488 140-3:658 | ;  |  |
| 1233 | pending | layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:487 140-3:658; layout_repairs_applied.json:488 140-3:658; layout_repairs_applied.json:489 140-3:659; layout_repairs_applied.json:490 140-3:659 | ;  |  |
| 1234 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:489 140-3:659; layout_repairs_applied.json:490 140-3:659 | ;  |  |
| 1235 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:489 140-3:659; layout_repairs_applied.json:490 140-3:659; layout_repairs_applied.json:491 140-3:660 | ;  |  |
| 1236 | pending | layout_repairs_applied.json:491 140-3:660 | ;  |  |
| 1238 | pending | layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:492 140-3:662 | ;  |  |
| 1239 | pending | layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:492 140-3:662 | ;  |  |
| 1244 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 1245 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 1255 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 1256 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 1259 | pending | layout_repairs_applied.json:502 140-3:685; layout_repairs_applied.json:503 140-3:685 | ;  |  |
| 1260 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:502 140-3:685; layout_repairs_applied.json:503 140-3:685; layout_repairs_applied.json:504 140-3:686 | ;  |  |
| 1261 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:504 140-3:686 | ;  |  |
| 1262 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:504 140-3:686 | ;  |  |
| 1263 | pending | layout_repairs_applied.json:505 140-3:688; layout_repairs_applied.json:506 140-3:688 | ;  |  |
| 1264 | pending | evenly spaced sample; layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:505 140-3:688; layout_repairs_applied.json:506 140-3:688; layout_repairs_applied.json:507 140-3:689 | ;  |  |
| 1265 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:507 140-3:689 | ;  |  |
| 1266 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:507 140-3:689 | ;  |  |
| 1269 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692 | ;  |  |
| 1270 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692 | ;  |  |
| 1271 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692; layout_repairs_applied.json:508 140-3:693; layout_repairs_applied.json:509 140-3:693 | ;  |  |
| 1275 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 1276 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 1279 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1280 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1281 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1282 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1283 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1284 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1290 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:510 140-4:20 | ;  |  |
| 1291 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:510 140-4:20 | ;  |  |
| 1297 | pending | layout_before_sites.json:311 140-4:29 | ;  |  |
| 1298 | pending | layout_before_sites.json:311 140-4:29; layout_repairs_applied.json:512 140-4:31; layout_repairs_applied.json:513 140-4:31; layout_repairs_applied.json:514 140-4:31 | ;  |  |
| 1299 | pending | layout_repairs_applied.json:512 140-4:31; layout_repairs_applied.json:513 140-4:31; layout_repairs_applied.json:514 140-4:31; layout_repairs_applied.json:515 140-4:32; layout_repairs_applied.json:516 140-4:32 | ;  |  |
| 1300 | pending | layout_repairs_applied.json:515 140-4:32; layout_repairs_applied.json:516 140-4:32; layout_repairs_applied.json:517 140-4:33 | ;  |  |
| 1301 | pending | layout_repairs_applied.json:517 140-4:33 | ;  |  |
| 1302 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:517 140-4:33 | ;  |  |
| 1303 | pending | evenly spaced sample; layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34 | ;  |  |
| 1304 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:518 140-4:35; layout_repairs_applied.json:519 140-4:35 | ;  |  |
| 1305 | pending | layout_repairs_applied.json:518 140-4:35; layout_repairs_applied.json:519 140-4:35 | ;  |  |
| 1309 | pending | layout_before_sites.json:314 140-4:39 | ;  |  |
| 1310 | pending | layout_before_sites.json:314 140-4:39; layout_before_sites.json:315 140-4:40 | ;  |  |
| 1311 | pending | layout_before_sites.json:315 140-4:40; layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41 | ;  |  |
| 1312 | pending | layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41; layout_before_sites.json:318 140-4:42 | ;  |  |
| 1313 | pending | layout_before_sites.json:318 140-4:42; layout_before_sites.json:319 140-4:43 | ;  |  |
| 1314 | pending | layout_before_sites.json:319 140-4:43; layout_before_sites.json:320 140-4:44; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:520 140-4:44 | ;  |  |
| 1315 | pending | layout_before_sites.json:320 140-4:44; layout_before_sites.json:321 140-4:45; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:520 140-4:44 | ;  |  |
| 1316 | pending | layout_before_sites.json:321 140-4:45; layout_before_sites.json:322 140-4:46 | ;  |  |
| 1317 | pending | layout_before_sites.json:322 140-4:46; layout_before_sites.json:323 140-4:47 | ;  |  |
| 1318 | pending | layout_before_sites.json:323 140-4:47 | ;  |  |
| 1319 | pending | layout_before_sites.json:323 140-4:47; layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48 | ;  |  |
| 1320 | pending | layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48; layout_before_sites.json:327 140-4:49 | ;  |  |
| 1321 | pending | layout_before_sites.json:327 140-4:49; layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 1322 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 1323 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50; layout_before_sites.json:331 140-4:51 | ;  |  |
| 1324 | pending | layout_before_sites.json:331 140-4:51; layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52 | ;  |  |
| 1325 | pending | layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52 | ;  |  |
| 1326 | pending | layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52; layout_before_sites.json:334 140-4:53; layout_before_sites.json:335 140-4:54 | ;  |  |
| 1327 | pending | layout_before_sites.json:335 140-4:54; layout_before_sites.json:336 140-4:55 | ;  |  |
| 1328 | pending | layout_before_sites.json:336 140-4:55; layout_before_sites.json:337 140-4:56 | ;  |  |
| 1329 | pending | layout_before_sites.json:337 140-4:56 | ;  |  |
| 1330 | pending | layout_before_sites.json:337 140-4:56; layout_before_sites.json:338 140-4:57 | ;  |  |
| 1331 | pending | layout_before_sites.json:338 140-4:57 | ;  |  |
| 1332 | pending | layout_before_sites.json:338 140-4:57; layout_repairs_applied.json:533 140-4:59 | ;  |  |
| 1333 | pending | layout_repairs_applied.json:533 140-4:59 | ;  |  |
| 1334 | pending | layout_repairs_applied.json:534 140-4:61; layout_repairs_applied.json:535 140-4:61; layout_repairs_applied.json:536 140-4:61; layout_repairs_applied.json:537 140-4:61 | ;  |  |
| 1335 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:534 140-4:61; layout_repairs_applied.json:535 140-4:61; layout_repairs_applied.json:536 140-4:61; layout_repairs_applied.json:537 140-4:61; layout_repairs_applied.json:538 140-4:62 | ;  |  |
| 1336 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:538 140-4:62 | ;  |  |
| 1337 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:538 140-4:62 | ;  |  |
| 1339 | pending | layout_repairs_applied.json:531 140-4:65 | ;  |  |
| 1340 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:522 140-4:66; layout_repairs_applied.json:523 140-4:66; layout_repairs_applied.json:524 140-4:66; layout_repairs_applied.json:531 140-4:65 | ;  |  |
| 1341 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_before_sites.json:343 140-4:67; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:522 140-4:66; layout_repairs_applied.json:523 140-4:66; layout_repairs_applied.json:524 140-4:66 | ;  |  |
| 1342 | pending | layout_before_sites.json:343 140-4:67 | ;  |  |
| 1343 | pending | evenly spaced sample | ;  |  |
| 1344 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 1345 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 1350 | pending | layout_repairs_applied.json:539 140-4:74 | ;  |  |
| 1351 | pending | layout_repairs_applied.json:532 140-4:75; layout_repairs_applied.json:539 140-4:74; layout_repairs_applied.json:540 140-4:75; layout_repairs_applied.json:541 140-4:75; layout_repairs_applied.json:542 140-4:75 | ;  |  |
| 1352 | pending | layout_repairs_applied.json:532 140-4:75; layout_repairs_applied.json:540 140-4:75; layout_repairs_applied.json:541 140-4:75; layout_repairs_applied.json:542 140-4:75 | ;  |  |
| 1353 | pending | layout_repairs_applied.json:532 140-4:75; layout_repairs_applied.json:540 140-4:75; layout_repairs_applied.json:541 140-4:75; layout_repairs_applied.json:542 140-4:75; layout_repairs_applied.json:543 140-4:76; layout_repairs_applied.json:544 140-4:76 | ;  |  |
| 1354 | pending | layout_repairs_applied.json:543 140-4:76; layout_repairs_applied.json:544 140-4:76 | ;  |  |
| 1355 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:543 140-4:76; layout_repairs_applied.json:544 140-4:76; layout_repairs_applied.json:547 140-4:77 | ;  |  |
| 1356 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:547 140-4:77 | ;  |  |
| 1357 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:547 140-4:77; layout_repairs_applied.json:548 140-4:78; layout_repairs_applied.json:549 140-4:78 | ;  |  |
| 1358 | pending | layout_repairs_applied.json:548 140-4:78; layout_repairs_applied.json:549 140-4:78; layout_repairs_applied.json:550 140-4:79; layout_repairs_applied.json:551 140-4:79 | ;  |  |
| 1359 | pending | layout_repairs_applied.json:550 140-4:79; layout_repairs_applied.json:551 140-4:79; layout_repairs_applied.json:552 140-4:80 | ;  |  |
| 1360 | pending | layout_repairs_applied.json:552 140-4:80; layout_repairs_applied.json:553 140-4:81; layout_repairs_applied.json:554 140-4:81 | ;  |  |
| 1361 | pending | layout_repairs_applied.json:553 140-4:81; layout_repairs_applied.json:554 140-4:81 | ;  |  |
| 1362 | pending | layout_repairs_applied.json:553 140-4:81; layout_repairs_applied.json:554 140-4:81 | ;  |  |
| 1373 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1374 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1375 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1380 | pending | layout_repairs_applied.json:558 140-4:96; layout_repairs_applied.json:559 140-4:96 | ;  |  |
| 1381 | pending | layout_repairs_applied.json:558 140-4:96; layout_repairs_applied.json:559 140-4:96; layout_repairs_applied.json:560 140-4:97; layout_repairs_applied.json:561 140-4:97 | ;  |  |
| 1382 | pending | evenly spaced sample; layout_repairs_applied.json:560 140-4:97; layout_repairs_applied.json:561 140-4:97; layout_repairs_applied.json:562 140-4:98 | ;  |  |
| 1383 | pending | layout_repairs_applied.json:562 140-4:98 | ;  |  |
| 1384 | pending | layout_before_sites.json:349 140-4:99; layout_repairs_applied.json:562 140-4:98 | ;  |  |
| 1385 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1386 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1387 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1388 | pending | layout_before_sites.json:350 140-4:101 | ;  |  |
| 1389 | pending | layout_before_sites.json:350 140-4:101; layout_before_sites.json:351 140-4:102 | ;  |  |
| 1390 | pending | layout_before_sites.json:351 140-4:102 | ;  |  |
| 1392 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 1393 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 1398 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:555 140-4:113 | ;  |  |
| 1399 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:555 140-4:113 | ;  |  |
| 1422 | pending | evenly spaced sample | ;  |  |
| 1424 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:563 140-4:136 | ;  |  |
| 1425 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:563 140-4:136 | ;  |  |
| 1432 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 1433 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 1434 | pending | layout_before_sites.json:356 140-4:149 | ;  |  |
| 1435 | pending | layout_before_sites.json:356 140-4:149 | ;  |  |
| 1439 | pending | layout_before_sites.json:357 140-4:154 | ;  |  |
| 1440 | pending | layout_before_sites.json:357 140-4:154 | ;  |  |
| 1453 | pending | layout_repairs_applied.json:565 140-4:172 | ;  |  |
| 1454 | pending | layout_repairs_applied.json:565 140-4:172; layout_repairs_applied.json:566 140-4:174 | ;  |  |
| 1455 | pending | layout_repairs_applied.json:566 140-4:174; layout_repairs_applied.json:567 140-4:175; layout_repairs_applied.json:568 140-4:175 | ;  |  |
| 1456 | pending | layout_repairs_applied.json:567 140-4:175; layout_repairs_applied.json:568 140-4:175 | ;  |  |
| 1460 | pending | layout_before_sites.json:358 140-4:181; layout_before_sites.json:359 140-4:181 | ;  |  |
| 1461 | pending | evenly spaced sample | ;  |  |
| 1463 | pending | layout_before_sites.json:360 140-4:186 | ;  |  |
| 1464 | pending | layout_before_sites.json:360 140-4:186; layout_before_sites.json:361 140-4:188 | ;  |  |
| 1465 | pending | layout_before_sites.json:361 140-4:188 | ;  |  |
| 1474 | pending | layout_repairs_applied.json:569 140-4:203; layout_repairs_applied.json:570 140-4:203 | ;  |  |
| 1475 | pending | layout_repairs_applied.json:571 140-4:205 | ;  |  |
| 1476 | pending | layout_repairs_applied.json:571 140-4:205 | ;  |  |
| 1497 | pending | layout_before_sites.json:362 140-4:230 | ;  |  |
| 1501 | pending | evenly spaced sample | ;  |  |
| 1502 | pending | layout_before_sites.json:363 140-4:236 | ;  |  |
| 1503 | pending | layout_before_sites.json:363 140-4:236 | ;  |  |
| 1509 | pending | layout_before_sites.json:364 140-4:245 | ;  |  |
| 1510 | pending | layout_before_sites.json:364 140-4:245 | ;  |  |
| 1513 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 1514 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 1526 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 1527 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 1528 | pending | layout_before_sites.json:367 140-4:266 | ;  |  |
| 1529 | pending | layout_before_sites.json:367 140-4:266 | ;  |  |
| 1530 | pending | layout_before_sites.json:367 140-4:266; layout_before_sites.json:368 140-4:267; layout_before_sites.json:369 140-4:268 | ;  |  |
| 1531 | pending | layout_before_sites.json:369 140-4:268; layout_before_sites.json:370 140-4:269 | ;  |  |
| 1532 | pending | layout_before_sites.json:370 140-4:269; layout_before_sites.json:371 140-4:270 | ;  |  |
| 1533 | pending | layout_before_sites.json:371 140-4:270; layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:575 140-4:271; layout_repairs_applied.json:577 140-4:271 | ;  |  |
| 1534 | pending | layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_before_sites.json:374 140-4:272; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:575 140-4:271; layout_repairs_applied.json:577 140-4:271 | ;  |  |
| 1535 | pending | layout_before_sites.json:374 140-4:272; layout_before_sites.json:375 140-4:273; layout_before_sites.json:376 140-4:274 | ;  |  |
| 1536 | pending | layout_before_sites.json:376 140-4:274; layout_before_sites.json:377 140-4:275 | ;  |  |
| 1537 | pending | layout_before_sites.json:377 140-4:275; layout_before_sites.json:378 140-4:276; layout_repairs_applied.json:576 140-4:276 | ;  |  |
| 1538 | pending | layout_before_sites.json:378 140-4:276; layout_before_sites.json:379 140-4:277; layout_repairs_applied.json:576 140-4:276 | ;  |  |
| 1539 | pending | layout_before_sites.json:379 140-4:277; layout_before_sites.json:380 140-4:278; layout_before_sites.json:381 140-4:279 | ;  |  |
| 1540 | pending | evenly spaced sample; layout_before_sites.json:381 140-4:279; layout_before_sites.json:382 140-4:280 | ;  |  |

### LM_EN_reading.pdf

PDF SHA-256: `7d7025c49762baaa31dab7efe1c5bf932b029b2c15681c2eb0c5ae6e71dd06f0`.

| Physical page | Status | Selection reason | Reviewer and inspection basis | Observation |
|---|---|---|---|---|
| 1 | reviewed | evenly spaced sample | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Title page: author, title, year, form, archive/cotes and date are centred cleanly and wholly on the sheet. |
| 6 | pending | layout_before_sites.json:1 140-1:4 | ;  |  |
| 7 | pending | layout_before_sites.json:1 140-1:4 | ;  |  |
| 9 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:294 140-1:10 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Repaired scan-10 diagram fits with its five-line subgroup annotation above the central arrows; labels and endpoints remain visible. The two diagrams above and smaller calculation below are contained. |
| 10 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:294 140-1:10 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Final four-up inspection: group presentation, cases and large lower branching diagram fit; the shifted first-projection label is separated from the diagonal. The source slanted stroke and cancellation doubts remain visible. |
| 11 | reviewed | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:292 140-1:12; layout_repairs_applied.json:294 140-1:10 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Marginal note m15 occupies the text block; its exact-sequence diagram, lifting formulae and bottom display fit without clipping. |
| 12 | reviewed | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:292 140-1:12 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Tall nested-fraction expression, note m16 and subsequent quadratic displays are contained; original uncertainty rows have distinct baselines. |
| 13 | reviewed | layout_before_sites.json:8 140-1:15 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The parity calculations fit in the text block; note m19 and its arrow calculations begin below a clear rule; no collision with the margin scan mark. |
| 14 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:8 140-1:15; layout_before_sites.json:9 140-1:16 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Prose articles, two small diagrams, underlined short margin note and block notes m22/m23 are separated and contained. |
| 15 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:9 140-1:16 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Sketch, Cartesian square and notes m25–m27 fit. The small hand-drawn continuation is clear; the short lifting note in the outer margin is separate. |
| 16 | reviewed | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:13 140-1:17; layout_before_sites.json:14 140-1:18; layout_before_sites.json:9 140-1:16; layout_pass_sites.json:31 140-1:18 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Residual doubts, note m29 and note m31 have clear boundaries; scattered daggers retain the positions of cancelled uncertain material; displayed mappings fit. |
| 17 | reviewed | layout_before_sites.json:14 140-1:18; layout_before_sites.json:15 140-1:19; layout_pass_sites.json:31 140-1:18; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:54 140-1:19; layout_repairs_applied.json:293 140-1:19 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Vertical exact-sequence diagram fits; note m32, residual doubt text and scan/page marks remain distinct. Red illegibility text is visible. |
| 18 | reviewed | layout_before_sites.json:15 140-1:19; layout_before_sites.json:16 140-1:20; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:54 140-1:19; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:293 140-1:19; layout_repairs_applied.json:297 140-1:20; layout_repairs_applied.json:302 140-1:20 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Large source sketch is wholly contained; its original intersecting curves and scattered labels are retained. The residual uncertainty block and circled manuscript-page number in the margin are visible. |
| 19 | reviewed | layout_before_sites.json:16 140-1:20; layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:297 140-1:20; layout_repairs_applied.json:302 140-1:20 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The complete multi-column diagram fits above note m35. Retained cancellation-doubt blocks have entries, sectionA opens with its lemma, and note m39 includes its full exact-sequence sketch. |
| 20 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23; layout_repairs_applied.json:303 140-1:25 | ;  |  |
| 21 | pending | layout_repairs_applied.json:303 140-1:25 | ;  |  |
| 23 | reviewed | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The two complete group diagrams and separating source stroke fit. The scan29 retained-doubt entries and original circle/array sketches remain contained, with cancellation daggers visible. |
| 24 | reviewed | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Note m51 begins with its source formulas. Scan30’s retained-doubt list fits, and the complete large multirow diagram at scan31 remains inside the page. |
| 25 | reviewed | evenly spaced sample; layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | The complete group diagrams and long vertical composite fit. The retained-doubt lists for scans31/32 have entries and stay inside the page; scan marks remain in the right margin. |
| 29 | pending | layout_before_sites.json:23 140-1:36; layout_before_sites.json:24 140-1:36; layout_pass_sites.json:34 140-1:36; layout_pass_sites.json:56 140-1:36; layout_repairs_applied.json:298 140-1:36 | ;  |  |
| 30 | pending | layout_before_sites.json:23 140-1:36; layout_before_sites.json:24 140-1:36; layout_pass_sites.json:34 140-1:36; layout_pass_sites.json:56 140-1:36; layout_repairs_applied.json:298 140-1:36 | ;  |  |
| 31 | pending | layout_before_sites.json:25 140-2:4 | ;  |  |
| 32 | pending | layout_before_sites.json:25 140-2:4 | ;  |  |
| 41 | pending | layout_before_sites.json:26 140-2:28 | ;  |  |
| 42 | pending | layout_before_sites.json:26 140-2:28; layout_before_sites.json:27 140-2:29 | ;  |  |
| 45 | pending | layout_before_sites.json:28 140-2:35 | ;  |  |
| 47 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 48 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 49 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 50 | pending | evenly spaced sample; layout_before_sites.json:30 140-2:42 | ;  |  |
| 51 | pending | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44 | ;  |  |
| 52 | pending | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44; layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | ;  |  |
| 53 | pending | layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | ;  |  |
| 64 | pending | layout_before_sites.json:35 140-2:69 | ;  |  |
| 69 | pending | layout_before_sites.json:36 140-2:80 | ;  |  |
| 72 | pending | layout_before_sites.json:37 140-2:88 | ;  |  |
| 73 | pending | layout_before_sites.json:37 140-2:88; layout_repairs_applied.json:304 140-2:89 | ;  |  |
| 74 | pending | evenly spaced sample | ;  |  |
| 88 | pending | layout_before_sites.json:38 140-2:122 | ;  |  |
| 91 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 92 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 97 | pending | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | ;  |  |
| 99 | pending | evenly spaced sample | ;  |  |
| 100 | pending | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | ;  |  |
| 105 | pending | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | ;  |  |
| 106 | pending | layout_before_sites.json:46 140-2:162 | ;  |  |
| 107 | pending | layout_before_sites.json:46 140-2:162 | ;  |  |
| 108 | pending | layout_before_sites.json:47 140-2:164; layout_before_sites.json:48 140-2:165; layout_before_sites.json:49 140-2:166; layout_repairs_applied.json:306 140-2:165 | ;  |  |
| 109 | pending | layout_before_sites.json:49 140-2:166 | ;  |  |
| 122 | pending | layout_before_sites.json:50 140-2:197 | ;  |  |
| 123 | pending | evenly spaced sample | ;  |  |
| 125 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205 | ;  |  |
| 126 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205; layout_repairs_applied.json:307 140-2:206 | ;  |  |
| 128 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 129 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 131 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 132 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 133 | pending | layout_before_sites.json:57 140-2:220 | ;  |  |
| 134 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 135 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 139 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 140 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 146 | pending | layout_repairs_applied.json:310 140-2:251 | ;  |  |
| 147 | pending | layout_repairs_applied.json:308 140-2:252; layout_repairs_applied.json:309 140-2:252; layout_repairs_applied.json:310 140-2:251; layout_repairs_applied.json:311 140-2:252 | ;  |  |
| 148 | pending | evenly spaced sample; layout_repairs_applied.json:308 140-2:252; layout_repairs_applied.json:309 140-2:252; layout_repairs_applied.json:311 140-2:252 | ;  |  |
| 151 | pending | layout_before_sites.json:60 140-2:259 | ;  |  |
| 154 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 155 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 159 | pending | layout_before_sites.json:62 140-2:280 | ;  |  |
| 161 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 162 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 169 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:313 140-2:302 | ;  |  |
| 170 | pending | landscape page; layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:313 140-2:302 | ;  |  |
| 171 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:313 140-2:302 | ;  |  |
| 172 | pending | evenly spaced sample | ;  |  |
| 174 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 175 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 179 | pending | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:315 140-2:321 | ;  |  |
| 182 | pending | layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:314 140-2:328 | ;  |  |
| 183 | pending | layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_before_sites.json:71 140-2:329; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:314 140-2:328 | ;  |  |
| 184 | pending | layout_before_sites.json:71 140-2:329; layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:316 140-2:331; layout_repairs_applied.json:317 140-2:331 | ;  |  |
| 185 | pending | layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:316 140-2:331; layout_repairs_applied.json:317 140-2:331 | ;  |  |
| 190 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 191 | pending | landscape page; layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 192 | pending | layout_before_sites.json:73 140-2:344; layout_before_sites.json:74 140-2:346; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:58 140-2:344; layout_pass_sites.json:63 140-2:346; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 193 | pending | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | ;  |  |
| 194 | pending | layout_before_sites.json:75 140-2:348; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:318 140-2:348 | ;  |  |
| 195 | pending | layout_before_sites.json:75 140-2:348; layout_before_sites.json:76 140-2:349; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:318 140-2:348 | ;  |  |
| 196 | pending | layout_before_sites.json:76 140-2:349 | ;  |  |
| 197 | pending | evenly spaced sample; layout_before_sites.json:77 140-2:352 | ;  |  |
| 201 | pending | layout_before_sites.json:78 140-2:362 | ;  |  |
| 202 | pending | layout_before_sites.json:78 140-2:362 | ;  |  |
| 205 | pending | layout_before_sites.json:79 140-2:371 | ;  |  |
| 206 | pending | layout_before_sites.json:79 140-2:371 | ;  |  |
| 210 | pending | layout_repairs_applied.json:322 140-2:382 | ;  |  |
| 211 | pending | layout_before_sites.json:80 140-2:384; layout_pass_sites.json:40 140-2:384; layout_pass_sites.json:64 140-2:384; layout_repairs_applied.json:322 140-2:382 | ;  |  |
| 212 | pending | layout_before_sites.json:80 140-2:384; layout_before_sites.json:81 140-2:387; layout_pass_sites.json:40 140-2:384; layout_pass_sites.json:64 140-2:384 | ;  |  |
| 213 | pending | layout_before_sites.json:81 140-2:387 | ;  |  |
| 217 | pending | layout_repairs_applied.json:323 140-2:397 | ;  |  |
| 220 | pending | layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404 | ;  |  |
| 221 | pending | evenly spaced sample; layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404; layout_repairs_applied.json:324 140-2:407 | ;  |  |
| 222 | pending | layout_repairs_applied.json:324 140-2:407 | ;  |  |
| 223 | pending | layout_pass_sites.json:41 140-2:411 | ;  |  |
| 226 | pending | layout_repairs_applied.json:325 140-2:417; layout_repairs_applied.json:327 140-2:417 | ;  |  |
| 227 | pending | layout_before_sites.json:84 140-2:419; layout_before_sites.json:85 140-2:419; layout_pass_sites.json:4 140-2:419; layout_pass_sites.json:42 140-2:419; layout_pass_sites.json:59 140-2:419; layout_pass_sites.json:65 140-2:419; layout_repairs_applied.json:325 140-2:417; layout_repairs_applied.json:326 140-2:419; layout_repairs_applied.json:327 140-2:417 | ;  |  |
| 228 | pending | layout_before_sites.json:84 140-2:419; layout_before_sites.json:85 140-2:419; layout_pass_sites.json:4 140-2:419; layout_pass_sites.json:42 140-2:419; layout_pass_sites.json:59 140-2:419; layout_pass_sites.json:65 140-2:419; layout_repairs_applied.json:326 140-2:419 | ;  |  |
| 229 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 230 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 232 | pending | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | ;  |  |
| 237 | pending | layout_before_sites.json:89 140-2:443 | ;  |  |
| 238 | pending | layout_before_sites.json:89 140-2:443 | ;  |  |
| 240 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 241 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 242 | pending | layout_before_sites.json:91 140-2:452 | ;  |  |
| 243 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 244 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 245 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 246 | pending | evenly spaced sample; layout_before_sites.json:93 140-2:457 | ;  |  |
| 248 | pending | layout_before_sites.json:94 140-2:462 | ;  |  |
| 261 | pending | layout_before_sites.json:95 140-2:492 | ;  |  |
| 264 | pending | layout_before_sites.json:96 140-2:502 | ;  |  |
| 266 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:328 140-2:508 | ;  |  |
| 267 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:328 140-2:508 | ;  |  |
| 269 | pending | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | ;  |  |
| 270 | pending | evenly spaced sample | ;  |  |
| 272 | pending | layout_before_sites.json:101 140-2:519 | ;  |  |
| 273 | pending | layout_before_sites.json:101 140-2:519; layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:330 140-2:520 | ;  |  |
| 276 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:331 140-2:527 | ;  |  |
| 277 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:331 140-2:527 | ;  |  |
| 279 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | ;  |  |
| 280 | pending | layout_before_sites.json:107 140-2:536 | ;  |  |
| 281 | pending | layout_before_sites.json:107 140-2:536 | ;  |  |
| 295 | pending | evenly spaced sample | ;  |  |
| 296 | pending | layout_before_sites.json:108 140-2:567 | ;  |  |
| 297 | pending | layout_before_sites.json:108 140-2:567; layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:332 140-2:568; layout_repairs_applied.json:333 140-2:568 | ;  |  |
| 298 | pending | layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:332 140-2:568; layout_repairs_applied.json:333 140-2:568 | ;  |  |
| 303 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | ;  |  |
| 304 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | ;  |  |
| 305 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4; layout_before_sites.json:114 140-3:5; layout_repairs_applied.json:334 140-3:6 | ;  |  |
| 306 | pending | layout_repairs_applied.json:334 140-3:6 | ;  |  |
| 310 | pending | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | ;  |  |
| 311 | pending | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | ;  |  |
| 313 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 314 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 315 | pending | layout_repairs_applied.json:335 140-3:21 | ;  |  |
| 316 | pending | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | ;  |  |
| 319 | pending | evenly spaced sample | ;  |  |
| 320 | pending | layout_repairs_applied.json:336 140-3:33 | ;  |  |
| 321 | pending | layout_before_sites.json:124 140-3:36 | ;  |  |
| 322 | pending | layout_before_sites.json:124 140-3:36 | ;  |  |
| 323 | pending | layout_repairs_applied.json:337 140-3:40 | ;  |  |
| 324 | pending | layout_repairs_applied.json:337 140-3:40; layout_repairs_applied.json:338 140-3:41 | ;  |  |
| 325 | pending | layout_repairs_applied.json:339 140-3:44 | ;  |  |
| 329 | pending | layout_repairs_applied.json:340 140-3:55 | ;  |  |
| 330 | pending | layout_before_sites.json:125 140-3:58; layout_repairs_applied.json:340 140-3:55; layout_repairs_applied.json:341 140-3:56 | ;  |  |
| 331 | pending | layout_before_sites.json:125 140-3:58; layout_before_sites.json:126 140-3:59 | ;  |  |
| 332 | pending | layout_before_sites.json:126 140-3:59 | ;  |  |
| 333 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 334 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 337 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 340 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 341 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 342 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 343 | pending | layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75; layout_before_sites.json:133 140-3:76 | ;  |  |
| 344 | pending | evenly spaced sample; layout_before_sites.json:133 140-3:76 | ;  |  |
| 349 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:342 140-3:85; layout_repairs_applied.json:343 140-3:85; layout_repairs_applied.json:344 140-3:85; layout_repairs_applied.json:345 140-3:85; layout_repairs_applied.json:346 140-3:85; layout_repairs_applied.json:347 140-3:85; layout_repairs_applied.json:348 140-3:85 | ;  |  |
| 350 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_before_sites.json:136 140-3:86; layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:342 140-3:85; layout_repairs_applied.json:343 140-3:85; layout_repairs_applied.json:344 140-3:85; layout_repairs_applied.json:345 140-3:85; layout_repairs_applied.json:346 140-3:85; layout_repairs_applied.json:347 140-3:85; layout_repairs_applied.json:348 140-3:85 | ;  |  |
| 351 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:349 140-3:88 | ;  |  |
| 352 | pending | layout_before_sites.json:139 140-3:90; layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:349 140-3:88 | ;  |  |
| 353 | pending | layout_before_sites.json:139 140-3:90; layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91 | ;  |  |
| 354 | pending | layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91; layout_before_sites.json:145 140-3:92 | ;  |  |
| 355 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 356 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 358 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 359 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95; layout_repairs_applied.json:350 140-3:97; layout_repairs_applied.json:356 140-3:97 | ;  |  |
| 360 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98; layout_repairs_applied.json:350 140-3:97; layout_repairs_applied.json:356 140-3:97 | ;  |  |
| 361 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98 | ;  |  |
| 366 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:351 140-3:107; layout_repairs_applied.json:352 140-3:107; layout_repairs_applied.json:353 140-3:107; layout_repairs_applied.json:354 140-3:107; layout_repairs_applied.json:355 140-3:107 | ;  |  |
| 367 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:351 140-3:107; layout_repairs_applied.json:352 140-3:107; layout_repairs_applied.json:353 140-3:107; layout_repairs_applied.json:354 140-3:107; layout_repairs_applied.json:355 140-3:107 | ;  |  |
| 368 | pending | evenly spaced sample | ;  |  |
| 369 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 370 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 375 | pending | layout_repairs_applied.json:357 140-3:121 | ;  |  |
| 376 | pending | layout_repairs_applied.json:357 140-3:121 | ;  |  |
| 392 | pending | layout_before_sites.json:154 140-3:148 | ;  |  |
| 393 | pending | evenly spaced sample; layout_before_sites.json:154 140-3:148 | ;  |  |
| 397 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 400 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 401 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 416 | pending | layout_before_sites.json:157 140-3:185; layout_repairs_applied.json:358 140-3:186 | ;  |  |
| 417 | pending | evenly spaced sample; layout_repairs_applied.json:358 140-3:186 | ;  |  |
| 420 | pending | layout_before_sites.json:158 140-3:191; layout_before_sites.json:159 140-3:191; layout_before_sites.json:160 140-3:192 | ;  |  |
| 421 | pending | layout_before_sites.json:160 140-3:192; layout_before_sites.json:161 140-3:194 | ;  |  |
| 422 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 425 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 426 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 431 | pending | layout_repairs_applied.json:359 140-3:208 | ;  |  |
| 432 | pending | layout_repairs_applied.json:359 140-3:208; layout_repairs_applied.json:360 140-3:209 | ;  |  |
| 433 | pending | layout_repairs_applied.json:360 140-3:209 | ;  |  |
| 434 | pending | layout_before_sites.json:164 140-3:212 | ;  |  |
| 435 | pending | layout_before_sites.json:164 140-3:212; layout_before_sites.json:165 140-3:213 | ;  |  |
| 436 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 437 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 440 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_repairs_applied.json:361 140-3:221 | ;  |  |
| 441 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_before_sites.json:169 140-3:222; layout_repairs_applied.json:361 140-3:221 | ;  |  |
| 442 | pending | evenly spaced sample; layout_before_sites.json:169 140-3:222 | ;  |  |
| 448 | pending | layout_before_sites.json:170 140-3:231 | ;  |  |
| 449 | pending | layout_before_sites.json:170 140-3:231; layout_before_sites.json:171 140-3:232 | ;  |  |
| 456 | pending | layout_repairs_applied.json:362 140-3:245 | ;  |  |
| 457 | pending | layout_repairs_applied.json:362 140-3:245 | ;  |  |
| 464 | pending | layout_repairs_applied.json:363 140-3:261 | ;  |  |
| 465 | pending | layout_repairs_applied.json:363 140-3:261 | ;  |  |
| 466 | pending | evenly spaced sample | ;  |  |
| 473 | pending | layout_repairs_applied.json:364 140-3:275 | ;  |  |
| 474 | pending | layout_repairs_applied.json:364 140-3:275 | ;  |  |
| 477 | pending | layout_before_sites.json:172 140-3:282 | ;  |  |
| 478 | pending | layout_before_sites.json:172 140-3:282; layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 479 | pending | layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 491 | pending | evenly spaced sample; layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 501 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:365 140-3:320 | ;  |  |
| 502 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:365 140-3:320 | ;  |  |
| 503 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 504 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 506 | pending | layout_before_sites.json:179 140-3:327 | ;  |  |
| 507 | pending | layout_before_sites.json:179 140-3:327; layout_before_sites.json:180 140-3:328; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:366 140-3:328 | ;  |  |
| 508 | pending | layout_before_sites.json:180 140-3:328; layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:73 140-3:329; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:366 140-3:328; layout_repairs_applied.json:367 140-3:329 | ;  |  |
| 509 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:367 140-3:329 | ;  |  |
| 511 | pending | layout_before_sites.json:182 140-3:334 | ;  |  |
| 512 | pending | layout_before_sites.json:182 140-3:334; layout_repairs_applied.json:369 140-3:335 | ;  |  |
| 513 | pending | layout_repairs_applied.json:369 140-3:335 | ;  |  |
| 515 | pending | evenly spaced sample | ;  |  |
| 519 | pending | layout_before_sites.json:183 140-3:346 | ;  |  |
| 520 | pending | layout_before_sites.json:183 140-3:346 | ;  |  |
| 524 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 525 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 526 | pending | layout_before_sites.json:185 140-3:356 | ;  |  |
| 527 | pending | layout_before_sites.json:185 140-3:356; layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357 | ;  |  |
| 528 | pending | layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357; layout_repairs_applied.json:370 140-3:358 | ;  |  |
| 529 | pending | layout_repairs_applied.json:370 140-3:358 | ;  |  |
| 531 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362 | ;  |  |
| 532 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362; layout_repairs_applied.json:373 140-3:363 | ;  |  |
| 533 | pending | layout_repairs_applied.json:373 140-3:363 | ;  |  |
| 540 | pending | evenly spaced sample | ;  |  |
| 542 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 543 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 549 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 550 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 563 | pending | layout_repairs_applied.json:380 140-3:408; layout_repairs_applied.json:381 140-3:408; layout_repairs_applied.json:382 140-3:408 | ;  |  |
| 564 | pending | evenly spaced sample; layout_repairs_applied.json:383 140-3:410 | ;  |  |
| 565 | pending | layout_repairs_applied.json:383 140-3:410 | ;  |  |
| 566 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 567 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 568 | pending | layout_before_sites.json:192 140-3:415 | ;  |  |
| 569 | pending | layout_before_sites.json:192 140-3:415; layout_before_sites.json:193 140-3:416 | ;  |  |
| 570 | pending | layout_before_sites.json:193 140-3:416 | ;  |  |
| 571 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:387 140-3:419 | ;  |  |
| 572 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:387 140-3:419 | ;  |  |
| 577 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:384 140-3:425 | ;  |  |
| 578 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:384 140-3:425 | ;  |  |
| 580 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 581 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429; layout_before_sites.json:197 140-3:431 | ;  |  |
| 582 | pending | layout_before_sites.json:197 140-3:431; layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432 | ;  |  |
| 583 | pending | layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432 | ;  |  |
| 584 | pending | layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432; layout_before_sites.json:200 140-3:433 | ;  |  |
| 586 | pending | layout_repairs_applied.json:396 140-3:436; layout_repairs_applied.json:397 140-3:436; layout_repairs_applied.json:398 140-3:436 | ;  |  |
| 587 | pending | layout_repairs_applied.json:396 140-3:436; layout_repairs_applied.json:397 140-3:436; layout_repairs_applied.json:398 140-3:436; layout_repairs_applied.json:399 140-3:437; layout_repairs_applied.json:400 140-3:437 | ;  |  |
| 588 | pending | layout_repairs_applied.json:399 140-3:437; layout_repairs_applied.json:400 140-3:437; layout_repairs_applied.json:401 140-3:438; layout_repairs_applied.json:402 140-3:438; layout_repairs_applied.json:403 140-3:438; layout_repairs_applied.json:404 140-3:438 | ;  |  |
| 589 | pending | evenly spaced sample; layout_repairs_applied.json:401 140-3:438; layout_repairs_applied.json:402 140-3:438; layout_repairs_applied.json:403 140-3:438; layout_repairs_applied.json:404 140-3:438 | ;  |  |
| 590 | pending | layout_repairs_applied.json:388 140-3:440; layout_repairs_applied.json:401 140-3:438; layout_repairs_applied.json:402 140-3:438; layout_repairs_applied.json:403 140-3:438; layout_repairs_applied.json:404 140-3:438; layout_repairs_applied.json:405 140-3:439; layout_repairs_applied.json:406 140-3:440 | ;  |  |
| 591 | pending | layout_repairs_applied.json:388 140-3:440; layout_repairs_applied.json:392 140-3:441; layout_repairs_applied.json:406 140-3:440 | ;  |  |
| 592 | pending | layout_before_sites.json:201 140-3:444; layout_repairs_applied.json:395 140-3:443 | ;  |  |
| 593 | pending | layout_before_sites.json:201 140-3:444 | ;  |  |
| 594 | pending | layout_before_sites.json:201 140-3:444; layout_pass_sites.json:12 140-3:446; layout_repairs_applied.json:390 140-3:446 | ;  |  |
| 595 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:12 140-3:446; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:389 140-3:448; layout_repairs_applied.json:390 140-3:446 | ;  |  |
| 596 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:389 140-3:448; layout_repairs_applied.json:393 140-3:449; layout_repairs_applied.json:394 140-3:449 | ;  |  |
| 597 | pending | layout_repairs_applied.json:393 140-3:449; layout_repairs_applied.json:394 140-3:449 | ;  |  |
| 600 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 601 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 604 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 605 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 607 | pending | layout_repairs_applied.json:407 140-3:462; layout_repairs_applied.json:408 140-3:463; layout_repairs_applied.json:409 140-3:463; layout_repairs_applied.json:410 140-3:463 | ;  |  |
| 608 | pending | layout_before_sites.json:207 140-3:465; layout_repairs_applied.json:408 140-3:463; layout_repairs_applied.json:409 140-3:463; layout_repairs_applied.json:410 140-3:463 | ;  |  |
| 609 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 610 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 611 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 612 | pending | layout_before_sites.json:208 140-3:468; layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 613 | pending | evenly spaced sample; layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 618 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 619 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 620 | pending | layout_before_sites.json:211 140-3:479; layout_repairs_applied.json:411 140-3:480; layout_repairs_applied.json:412 140-3:480 | ;  |  |
| 621 | pending | layout_repairs_applied.json:411 140-3:480; layout_repairs_applied.json:412 140-3:480 | ;  |  |
| 623 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 624 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 626 | pending | layout_before_sites.json:213 140-3:491 | ;  |  |
| 627 | pending | layout_before_sites.json:213 140-3:491; layout_before_sites.json:214 140-3:492 | ;  |  |
| 628 | pending | layout_repairs_applied.json:413 140-3:494 | ;  |  |
| 632 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 635 | pending | layout_repairs_applied.json:415 140-3:503 | ;  |  |
| 636 | pending | layout_repairs_applied.json:415 140-3:503 | ;  |  |
| 638 | pending | evenly spaced sample; layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:416 140-3:506; layout_repairs_applied.json:417 140-3:506 | ;  |  |
| 639 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:416 140-3:506; layout_repairs_applied.json:417 140-3:506 | ;  |  |
| 640 | pending | layout_before_sites.json:217 140-3:509 | ;  |  |
| 641 | pending | layout_before_sites.json:217 140-3:509; layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 642 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 645 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 646 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 648 | pending | layout_before_sites.json:221 140-3:517; layout_before_sites.json:222 140-3:518 | ;  |  |
| 649 | pending | layout_before_sites.json:222 140-3:518; layout_before_sites.json:223 140-3:519; layout_repairs_applied.json:418 140-3:519; layout_repairs_applied.json:423 140-3:519 | ;  |  |
| 650 | pending | layout_before_sites.json:223 140-3:519; layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:418 140-3:519; layout_repairs_applied.json:422 140-3:520; layout_repairs_applied.json:423 140-3:519 | ;  |  |
| 651 | pending | layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:422 140-3:520 | ;  |  |
| 652 | pending | layout_before_sites.json:225 140-3:522 | ;  |  |
| 653 | pending | layout_before_sites.json:225 140-3:522; layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:424 140-3:523; layout_repairs_applied.json:425 140-3:524; layout_repairs_applied.json:426 140-3:524 | ;  |  |
| 654 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:419 140-3:525; layout_repairs_applied.json:425 140-3:524; layout_repairs_applied.json:426 140-3:524; layout_repairs_applied.json:427 140-3:525; layout_repairs_applied.json:428 140-3:525 | ;  |  |
| 655 | pending | layout_repairs_applied.json:419 140-3:525; layout_repairs_applied.json:427 140-3:525; layout_repairs_applied.json:428 140-3:525 | ;  |  |
| 658 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530 | ;  |  |
| 659 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530; layout_before_sites.json:229 140-3:531; layout_before_sites.json:230 140-3:532 | ;  |  |
| 660 | pending | layout_before_sites.json:230 140-3:532; layout_before_sites.json:231 140-3:533; layout_before_sites.json:232 140-3:534 | ;  |  |
| 661 | pending | layout_before_sites.json:232 140-3:534; layout_before_sites.json:233 140-3:535 | ;  |  |
| 662 | pending | evenly spaced sample; layout_before_sites.json:233 140-3:535; layout_before_sites.json:234 140-3:536; layout_repairs_applied.json:429 140-3:536 | ;  |  |
| 663 | pending | layout_before_sites.json:234 140-3:536; layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_before_sites.json:238 140-3:538; layout_repairs_applied.json:429 140-3:536 | ;  |  |
| 664 | pending | layout_before_sites.json:238 140-3:538; layout_before_sites.json:239 140-3:539; layout_before_sites.json:240 140-3:540 | ;  |  |
| 665 | pending | layout_before_sites.json:240 140-3:540; layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 666 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541; layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:430 140-3:542; layout_repairs_applied.json:434 140-3:542 | ;  |  |
| 667 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_before_sites.json:245 140-3:543; layout_repairs_applied.json:430 140-3:542; layout_repairs_applied.json:434 140-3:542; layout_repairs_applied.json:435 140-3:543; layout_repairs_applied.json:436 140-3:543; layout_repairs_applied.json:437 140-3:543 | ;  |  |
| 668 | pending | layout_before_sites.json:245 140-3:543; layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:435 140-3:543; layout_repairs_applied.json:436 140-3:543; layout_repairs_applied.json:437 140-3:543; layout_repairs_applied.json:438 140-3:544; layout_repairs_applied.json:439 140-3:544 | ;  |  |
| 669 | pending | layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:438 140-3:544; layout_repairs_applied.json:439 140-3:544 | ;  |  |
| 670 | pending | layout_before_sites.json:246 140-3:544; layout_before_sites.json:247 140-3:545; layout_repairs_applied.json:431 140-3:545; layout_repairs_applied.json:432 140-3:545; layout_repairs_applied.json:438 140-3:544; layout_repairs_applied.json:439 140-3:544; layout_repairs_applied.json:440 140-3:545; layout_repairs_applied.json:441 140-3:545; layout_repairs_applied.json:442 140-3:545; layout_repairs_applied.json:443 140-3:545; layout_repairs_applied.json:444 140-3:545; layout_repairs_applied.json:445 140-3:545 | ;  |  |
| 671 | pending | layout_before_sites.json:247 140-3:545; layout_before_sites.json:248 140-3:546; layout_repairs_applied.json:431 140-3:545; layout_repairs_applied.json:432 140-3:545; layout_repairs_applied.json:433 140-3:546; layout_repairs_applied.json:440 140-3:545; layout_repairs_applied.json:441 140-3:545; layout_repairs_applied.json:442 140-3:545; layout_repairs_applied.json:443 140-3:545; layout_repairs_applied.json:444 140-3:545; layout_repairs_applied.json:445 140-3:545 | ;  |  |
| 672 | pending | layout_before_sites.json:248 140-3:546; layout_before_sites.json:249 140-3:547; layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:433 140-3:546; layout_repairs_applied.json:446 140-3:548 | ;  |  |
| 673 | pending | layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:446 140-3:548 | ;  |  |
| 676 | pending | layout_before_sites.json:251 140-3:554; layout_repairs_applied.json:447 140-3:554 | ;  |  |
| 677 | pending | layout_before_sites.json:251 140-3:554; layout_before_sites.json:252 140-3:555; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:447 140-3:554; layout_repairs_applied.json:448 140-3:555 | ;  |  |
| 678 | pending | layout_before_sites.json:252 140-3:555; layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:448 140-3:555; layout_repairs_applied.json:449 140-3:556 | ;  |  |
| 679 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_repairs_applied.json:449 140-3:556 | ;  |  |
| 680 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_before_sites.json:255 140-3:557; layout_before_sites.json:256 140-3:558; layout_pass_sites.json:14 140-3:557; layout_pass_sites.json:75 140-3:557; layout_repairs_applied.json:449 140-3:556; layout_repairs_applied.json:451 140-3:557 | ;  |  |
| 681 | pending | layout_before_sites.json:256 140-3:558; layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 682 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 683 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:452 140-3:561 | ;  |  |
| 684 | pending | landscape page; layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:452 140-3:561 | ;  |  |
| 685 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:450 140-3:562; layout_repairs_applied.json:452 140-3:561; layout_repairs_applied.json:455 140-3:562; layout_repairs_applied.json:456 140-3:562 | ;  |  |
| 686 | pending | layout_repairs_applied.json:450 140-3:562; layout_repairs_applied.json:455 140-3:562; layout_repairs_applied.json:456 140-3:562 | ;  |  |
| 687 | pending | evenly spaced sample; layout_repairs_applied.json:457 140-3:565 | ;  |  |
| 688 | pending | layout_repairs_applied.json:457 140-3:565 | ;  |  |
| 689 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567 | ;  |  |
| 690 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567; layout_repairs_applied.json:458 140-3:568 | ;  |  |
| 691 | pending | layout_repairs_applied.json:458 140-3:568 | ;  |  |
| 692 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 693 | pending | layout_before_sites.json:262 140-3:570; layout_before_sites.json:263 140-3:573; layout_repairs_applied.json:459 140-3:573 | ;  |  |
| 694 | pending | layout_before_sites.json:263 140-3:573; layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:459 140-3:573; layout_repairs_applied.json:460 140-3:574 | ;  |  |
| 695 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:460 140-3:574; layout_repairs_applied.json:462 140-3:575 | ;  |  |
| 696 | pending | layout_before_sites.json:265 140-3:577; layout_repairs_applied.json:462 140-3:575 | ;  |  |
| 697 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 701 | pending | layout_before_sites.json:266 140-3:582 | ;  |  |
| 702 | pending | layout_before_sites.json:266 140-3:582 | ;  |  |
| 703 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 704 | pending | layout_before_sites.json:267 140-3:585; layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 705 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586; layout_before_sites.json:270 140-3:587 | ;  |  |
| 706 | pending | layout_before_sites.json:270 140-3:587 | ;  |  |
| 707 | pending | layout_before_sites.json:270 140-3:587; layout_before_sites.json:271 140-3:588; layout_before_sites.json:272 140-3:589 | ;  |  |
| 708 | pending | layout_before_sites.json:272 140-3:589; layout_repairs_applied.json:464 140-3:590 | ;  |  |
| 709 | pending | layout_repairs_applied.json:464 140-3:590 | ;  |  |
| 710 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 711 | pending | evenly spaced sample; layout_before_sites.json:273 140-3:593 | ;  |  |
| 715 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 716 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 720 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:465 140-3:606 | ;  |  |
| 721 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:465 140-3:606 | ;  |  |
| 722 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:467 140-3:609 | ;  |  |
| 723 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:467 140-3:609 | ;  |  |
| 727 | pending | layout_before_sites.json:275 140-3:616 | ;  |  |
| 728 | pending | layout_before_sites.json:275 140-3:616; layout_before_sites.json:276 140-3:617 | ;  |  |
| 729 | pending | layout_before_sites.json:276 140-3:617 | ;  |  |
| 730 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:468 140-3:619 | ;  |  |
| 731 | pending | layout_before_sites.json:277 140-3:619; layout_before_sites.json:278 140-3:621; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:18 140-3:621; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:466 140-3:621; layout_repairs_applied.json:468 140-3:619; layout_repairs_applied.json:473 140-3:621 | ;  |  |
| 732 | pending | layout_before_sites.json:278 140-3:621; layout_pass_sites.json:18 140-3:621; layout_repairs_applied.json:466 140-3:621; layout_repairs_applied.json:473 140-3:621; layout_repairs_applied.json:474 140-3:622; layout_repairs_applied.json:475 140-3:622; layout_repairs_applied.json:476 140-3:622; layout_repairs_applied.json:477 140-3:622; layout_repairs_applied.json:478 140-3:622 | ;  |  |
| 733 | pending | layout_repairs_applied.json:474 140-3:622; layout_repairs_applied.json:475 140-3:622; layout_repairs_applied.json:476 140-3:622; layout_repairs_applied.json:477 140-3:622; layout_repairs_applied.json:478 140-3:622; layout_repairs_applied.json:479 140-3:623; layout_repairs_applied.json:480 140-3:623 | ;  |  |
| 734 | pending | layout_repairs_applied.json:479 140-3:623; layout_repairs_applied.json:480 140-3:623 | ;  |  |
| 735 | pending | layout_before_sites.json:279 140-3:625 | ;  |  |
| 736 | pending | evenly spaced sample; layout_before_sites.json:280 140-3:627; layout_repairs_applied.json:481 140-3:628 | ;  |  |
| 737 | pending | layout_before_sites.json:281 140-3:629; layout_repairs_applied.json:481 140-3:628 | ;  |  |
| 738 | pending | layout_before_sites.json:281 140-3:629; layout_before_sites.json:282 140-3:631 | ;  |  |
| 739 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 741 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:483 140-3:637; layout_repairs_applied.json:485 140-3:637 | ;  |  |
| 742 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:482 140-3:638; layout_repairs_applied.json:483 140-3:637; layout_repairs_applied.json:485 140-3:637 | ;  |  |
| 743 | pending | layout_repairs_applied.json:482 140-3:638 | ;  |  |
| 749 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:496 140-3:649 | ;  |  |
| 750 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:496 140-3:649 | ;  |  |
| 751 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:486 140-3:653; layout_repairs_applied.json:497 140-3:653 | ;  |  |
| 752 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:486 140-3:653; layout_repairs_applied.json:497 140-3:653 | ;  |  |
| 753 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:498 140-3:656; layout_repairs_applied.json:499 140-3:656 | ;  |  |
| 754 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:498 140-3:656; layout_repairs_applied.json:499 140-3:656 | ;  |  |
| 755 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:487 140-3:658; layout_repairs_applied.json:488 140-3:658; layout_repairs_applied.json:498 140-3:656; layout_repairs_applied.json:499 140-3:656 | ;  |  |
| 756 | pending | layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:487 140-3:658; layout_repairs_applied.json:488 140-3:658; layout_repairs_applied.json:489 140-3:659; layout_repairs_applied.json:490 140-3:659 | ;  |  |
| 757 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:489 140-3:659; layout_repairs_applied.json:490 140-3:659; layout_repairs_applied.json:491 140-3:660 | ;  |  |
| 758 | pending | layout_repairs_applied.json:491 140-3:660 | ;  |  |
| 759 | pending | layout_repairs_applied.json:491 140-3:660 | ;  |  |
| 760 | pending | evenly spaced sample; layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:492 140-3:662 | ;  |  |
| 765 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 772 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 775 | pending | layout_repairs_applied.json:502 140-3:685; layout_repairs_applied.json:503 140-3:685 | ;  |  |
| 776 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:502 140-3:685; layout_repairs_applied.json:503 140-3:685; layout_repairs_applied.json:504 140-3:686 | ;  |  |
| 777 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:504 140-3:686 | ;  |  |
| 778 | pending | layout_repairs_applied.json:505 140-3:688; layout_repairs_applied.json:506 140-3:688 | ;  |  |
| 779 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:505 140-3:688; layout_repairs_applied.json:506 140-3:688; layout_repairs_applied.json:507 140-3:689 | ;  |  |
| 781 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692 | ;  |  |
| 782 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692; layout_repairs_applied.json:508 140-3:693; layout_repairs_applied.json:509 140-3:693 | ;  |  |
| 785 | pending | evenly spaced sample | ;  |  |
| 786 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 789 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 791 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 792 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 796 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:510 140-4:20 | ;  |  |
| 801 | pending | layout_before_sites.json:311 140-4:29 | ;  |  |
| 802 | pending | layout_repairs_applied.json:512 140-4:31; layout_repairs_applied.json:513 140-4:31; layout_repairs_applied.json:514 140-4:31; layout_repairs_applied.json:515 140-4:32; layout_repairs_applied.json:516 140-4:32 | ;  |  |
| 803 | pending | layout_repairs_applied.json:515 140-4:32; layout_repairs_applied.json:516 140-4:32; layout_repairs_applied.json:517 140-4:33 | ;  |  |
| 804 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:517 140-4:33 | ;  |  |
| 805 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34 | ;  |  |
| 806 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:518 140-4:35; layout_repairs_applied.json:519 140-4:35 | ;  |  |
| 807 | pending | layout_repairs_applied.json:518 140-4:35; layout_repairs_applied.json:519 140-4:35 | ;  |  |
| 809 | pending | evenly spaced sample; layout_before_sites.json:314 140-4:39 | ;  |  |
| 810 | pending | layout_before_sites.json:314 140-4:39; layout_before_sites.json:315 140-4:40; layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41 | ;  |  |
| 811 | pending | layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41; layout_before_sites.json:318 140-4:42 | ;  |  |
| 812 | pending | layout_before_sites.json:318 140-4:42; layout_before_sites.json:319 140-4:43; layout_before_sites.json:320 140-4:44; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:520 140-4:44 | ;  |  |
| 813 | pending | layout_before_sites.json:320 140-4:44; layout_before_sites.json:321 140-4:45; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:520 140-4:44 | ;  |  |
| 814 | pending | layout_before_sites.json:321 140-4:45; layout_before_sites.json:322 140-4:46 | ;  |  |
| 815 | pending | layout_before_sites.json:322 140-4:46; layout_before_sites.json:323 140-4:47 | ;  |  |
| 816 | pending | layout_before_sites.json:323 140-4:47; layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48 | ;  |  |
| 817 | pending | layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48; layout_before_sites.json:327 140-4:49; layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 818 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50; layout_before_sites.json:331 140-4:51 | ;  |  |
| 819 | pending | layout_before_sites.json:331 140-4:51; layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52; layout_before_sites.json:334 140-4:53 | ;  |  |
| 820 | pending | layout_before_sites.json:334 140-4:53; layout_before_sites.json:335 140-4:54 | ;  |  |
| 821 | pending | layout_before_sites.json:335 140-4:54; layout_before_sites.json:336 140-4:55; layout_before_sites.json:337 140-4:56 | ;  |  |
| 822 | pending | layout_before_sites.json:337 140-4:56; layout_before_sites.json:338 140-4:57 | ;  |  |
| 823 | pending | layout_before_sites.json:338 140-4:57 | ;  |  |
| 824 | pending | layout_repairs_applied.json:533 140-4:59 | ;  |  |
| 825 | pending | layout_repairs_applied.json:533 140-4:59; layout_repairs_applied.json:534 140-4:61; layout_repairs_applied.json:535 140-4:61; layout_repairs_applied.json:536 140-4:61; layout_repairs_applied.json:537 140-4:61 | ;  |  |
| 826 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:534 140-4:61; layout_repairs_applied.json:535 140-4:61; layout_repairs_applied.json:536 140-4:61; layout_repairs_applied.json:537 140-4:61; layout_repairs_applied.json:538 140-4:62 | ;  |  |
| 827 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:538 140-4:62 | ;  |  |
| 828 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:522 140-4:66; layout_repairs_applied.json:523 140-4:66; layout_repairs_applied.json:524 140-4:66; layout_repairs_applied.json:531 140-4:65 | ;  |  |
| 829 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:522 140-4:66; layout_repairs_applied.json:523 140-4:66; layout_repairs_applied.json:524 140-4:66 | ;  |  |
| 830 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_before_sites.json:343 140-4:67; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:522 140-4:66; layout_repairs_applied.json:523 140-4:66; layout_repairs_applied.json:524 140-4:66 | ;  |  |
| 831 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 832 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 834 | pending | evenly spaced sample | ;  |  |
| 835 | pending | layout_repairs_applied.json:539 140-4:74 | ;  |  |
| 836 | pending | layout_repairs_applied.json:532 140-4:75; layout_repairs_applied.json:539 140-4:74; layout_repairs_applied.json:540 140-4:75; layout_repairs_applied.json:541 140-4:75; layout_repairs_applied.json:542 140-4:75 | ;  |  |
| 837 | pending | layout_repairs_applied.json:532 140-4:75; layout_repairs_applied.json:540 140-4:75; layout_repairs_applied.json:541 140-4:75; layout_repairs_applied.json:542 140-4:75; layout_repairs_applied.json:543 140-4:76; layout_repairs_applied.json:544 140-4:76 | ;  |  |
| 838 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:543 140-4:76; layout_repairs_applied.json:544 140-4:76; layout_repairs_applied.json:547 140-4:77 | ;  |  |
| 839 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:547 140-4:77 | ;  |  |
| 840 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:547 140-4:77; layout_repairs_applied.json:548 140-4:78; layout_repairs_applied.json:549 140-4:78 | ;  |  |
| 841 | pending | layout_repairs_applied.json:548 140-4:78; layout_repairs_applied.json:549 140-4:78; layout_repairs_applied.json:550 140-4:79; layout_repairs_applied.json:551 140-4:79; layout_repairs_applied.json:552 140-4:80 | ;  |  |
| 842 | pending | layout_repairs_applied.json:552 140-4:80; layout_repairs_applied.json:553 140-4:81; layout_repairs_applied.json:554 140-4:81 | ;  |  |
| 843 | pending | layout_repairs_applied.json:553 140-4:81; layout_repairs_applied.json:554 140-4:81 | ;  |  |
| 852 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 853 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 856 | pending | layout_repairs_applied.json:558 140-4:96; layout_repairs_applied.json:559 140-4:96; layout_repairs_applied.json:560 140-4:97; layout_repairs_applied.json:561 140-4:97 | ;  |  |
| 857 | pending | layout_repairs_applied.json:560 140-4:97; layout_repairs_applied.json:561 140-4:97; layout_repairs_applied.json:562 140-4:98 | ;  |  |
| 858 | pending | evenly spaced sample; layout_before_sites.json:349 140-4:99; layout_repairs_applied.json:562 140-4:98 | ;  |  |
| 859 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 860 | pending | layout_before_sites.json:350 140-4:101 | ;  |  |
| 861 | pending | layout_before_sites.json:350 140-4:101; layout_before_sites.json:351 140-4:102 | ;  |  |
| 862 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 863 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 867 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:555 140-4:113 | ;  |  |
| 868 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:555 140-4:113 | ;  |  |
| 883 | pending | evenly spaced sample; layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:563 140-4:136 | ;  |  |
| 884 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:563 140-4:136 | ;  |  |
| 888 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 889 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 890 | pending | layout_before_sites.json:356 140-4:149 | ;  |  |
| 893 | pending | layout_before_sites.json:357 140-4:154 | ;  |  |
| 901 | pending | layout_repairs_applied.json:565 140-4:172 | ;  |  |
| 902 | pending | layout_repairs_applied.json:565 140-4:172; layout_repairs_applied.json:566 140-4:174 | ;  |  |
| 903 | pending | layout_repairs_applied.json:566 140-4:174; layout_repairs_applied.json:567 140-4:175; layout_repairs_applied.json:568 140-4:175 | ;  |  |
| 904 | pending | layout_repairs_applied.json:567 140-4:175; layout_repairs_applied.json:568 140-4:175 | ;  |  |
| 905 | pending | layout_before_sites.json:358 140-4:181; layout_before_sites.json:359 140-4:181 | ;  |  |
| 906 | pending | layout_before_sites.json:358 140-4:181; layout_before_sites.json:359 140-4:181 | ;  |  |
| 907 | pending | evenly spaced sample; layout_before_sites.json:360 140-4:186 | ;  |  |
| 908 | pending | layout_before_sites.json:361 140-4:188 | ;  |  |
| 913 | pending | layout_repairs_applied.json:569 140-4:203; layout_repairs_applied.json:570 140-4:203 | ;  |  |
| 914 | pending | layout_repairs_applied.json:569 140-4:203; layout_repairs_applied.json:570 140-4:203 | ;  |  |
| 915 | pending | layout_repairs_applied.json:571 140-4:205 | ;  |  |
| 928 | pending | layout_before_sites.json:362 140-4:230 | ;  |  |
| 931 | pending | layout_before_sites.json:363 140-4:236 | ;  |  |
| 932 | pending | evenly spaced sample; layout_before_sites.json:363 140-4:236 | ;  |  |
| 936 | pending | layout_before_sites.json:364 140-4:245 | ;  |  |
| 937 | pending | layout_before_sites.json:364 140-4:245 | ;  |  |
| 939 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 940 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 947 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 948 | pending | layout_before_sites.json:366 140-4:264; layout_before_sites.json:367 140-4:266 | ;  |  |
| 949 | pending | layout_before_sites.json:367 140-4:266; layout_before_sites.json:368 140-4:267 | ;  |  |
| 950 | pending | layout_before_sites.json:368 140-4:267; layout_before_sites.json:369 140-4:268 | ;  |  |
| 951 | pending | layout_before_sites.json:369 140-4:268; layout_before_sites.json:370 140-4:269; layout_before_sites.json:371 140-4:270 | ;  |  |
| 952 | pending | layout_before_sites.json:371 140-4:270; layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_before_sites.json:374 140-4:272; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:575 140-4:271; layout_repairs_applied.json:577 140-4:271 | ;  |  |
| 953 | pending | layout_before_sites.json:374 140-4:272; layout_before_sites.json:375 140-4:273; layout_before_sites.json:376 140-4:274 | ;  |  |
| 954 | pending | layout_before_sites.json:376 140-4:274; layout_before_sites.json:377 140-4:275; layout_before_sites.json:378 140-4:276; layout_repairs_applied.json:576 140-4:276 | ;  |  |
| 955 | pending | layout_before_sites.json:378 140-4:276; layout_before_sites.json:379 140-4:277; layout_before_sites.json:380 140-4:278; layout_repairs_applied.json:576 140-4:276 | ;  |  |
| 956 | pending | evenly spaced sample; layout_before_sites.json:380 140-4:278; layout_before_sites.json:381 140-4:279; layout_before_sites.json:382 140-4:280 | ;  |  |

### LM_FR_master_annotated.pdf

PDF SHA-256: `e953a33c011971fd65c0f7df85254be3d1b744cd73d98aeee9769318ce68dd2f`.

| Physical page | Status | Selection reason | Reviewer and inspection basis | Observation |
|---|---|---|---|---|
| 1 | reviewed | evenly spaced sample | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Actually inspected full 900px title page: author, full French title, year1981, Master annoté, archive/cotes, scan count and edition date are cleanly separated and contained; no clipped or missing type observed. |
| 6 | pending | layout_before_sites.json:1 140-1:4 | ;  |  |
| 7 | pending | layout_before_sites.json:1 140-1:4 | ;  |  |
| 8 | pending | layout_before_sites.json:1 140-1:4 | ;  |  |
| 10 | pending | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:5 140-1:10 | ;  |  |
| 11 | pending | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:5 140-1:10 | ;  |  |
| 12 | pending | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:5 140-1:10 | ;  |  |
| 13 | pending | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:1 140-1:10; layout_repairs_applied.json:2 140-1:10; layout_repairs_applied.json:3 140-1:12; layout_repairs_applied.json:5 140-1:10 | ;  |  |
| 14 | pending | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:3 140-1:12 | ;  |  |
| 15 | pending | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:3 140-1:12 | ;  |  |
| 16 | pending | layout_before_sites.json:8 140-1:15 | ;  |  |
| 17 | pending | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:8 140-1:15; layout_before_sites.json:9 140-1:16 | ;  |  |
| 18 | pending | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:9 140-1:16 | ;  |  |
| 19 | pending | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:9 140-1:16 | ;  |  |
| 20 | pending | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:13 140-1:17; layout_before_sites.json:9 140-1:16 | ;  |  |
| 21 | pending | layout_before_sites.json:13 140-1:17; layout_before_sites.json:14 140-1:18; layout_pass_sites.json:31 140-1:18 | ;  |  |
| 22 | pending | layout_before_sites.json:14 140-1:18; layout_pass_sites.json:31 140-1:18 | ;  |  |
| 23 | pending | layout_before_sites.json:14 140-1:18; layout_before_sites.json:15 140-1:19; layout_pass_sites.json:31 140-1:18; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:54 140-1:19; layout_repairs_applied.json:4 140-1:19 | ;  |  |
| 24 | pending | layout_before_sites.json:15 140-1:19; layout_before_sites.json:16 140-1:20; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:54 140-1:19; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:13 140-1:20; layout_repairs_applied.json:4 140-1:19; layout_repairs_applied.json:8 140-1:20 | ;  |  |
| 25 | pending | layout_before_sites.json:16 140-1:20; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:13 140-1:20; layout_repairs_applied.json:8 140-1:20 | ;  |  |
| 27 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23 | ;  |  |
| 28 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23 | ;  |  |
| 29 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23; layout_repairs_applied.json:14 140-1:25 | ;  |  |
| 30 | pending | layout_repairs_applied.json:14 140-1:25 | ;  |  |
| 32 | pending | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | ;  |  |
| 33 | pending | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | ;  |  |
| 34 | pending | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | ;  |  |
| 35 | pending | layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | ;  |  |
| 36 | pending | layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | ;  |  |
| 40 | pending | evenly spaced sample | ;  |  |
| 41 | pending | layout_before_sites.json:23 140-1:36; layout_before_sites.json:24 140-1:36; layout_pass_sites.json:34 140-1:36; layout_pass_sites.json:56 140-1:36; layout_repairs_applied.json:9 140-1:36 | ;  |  |
| 42 | pending | layout_before_sites.json:25 140-2:4 | ;  |  |
| 43 | pending | layout_before_sites.json:25 140-2:4 | ;  |  |
| 58 | pending | layout_before_sites.json:26 140-2:28 | ;  |  |
| 59 | pending | layout_before_sites.json:26 140-2:28; layout_before_sites.json:27 140-2:29 | ;  |  |
| 60 | pending | layout_before_sites.json:27 140-2:29 | ;  |  |
| 64 | pending | layout_before_sites.json:28 140-2:35 | ;  |  |
| 65 | pending | layout_before_sites.json:28 140-2:35 | ;  |  |
| 68 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 69 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 70 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 71 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 72 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 73 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 74 | pending | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44 | ;  |  |
| 75 | pending | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44; layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | ;  |  |
| 76 | pending | layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | ;  |  |
| 80 | pending | evenly spaced sample | ;  |  |
| 94 | pending | layout_before_sites.json:35 140-2:69 | ;  |  |
| 103 | pending | layout_before_sites.json:36 140-2:80 | ;  |  |
| 104 | pending | layout_before_sites.json:36 140-2:80 | ;  |  |
| 109 | pending | layout_before_sites.json:37 140-2:88 | ;  |  |
| 110 | pending | layout_before_sites.json:37 140-2:88; layout_repairs_applied.json:15 140-2:89 | ;  |  |
| 111 | pending | layout_repairs_applied.json:15 140-2:89 | ;  |  |
| 119 | pending | evenly spaced sample | ;  |  |
| 139 | pending | layout_before_sites.json:38 140-2:122 | ;  |  |
| 144 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 145 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 146 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 155 | pending | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | ;  |  |
| 156 | pending | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | ;  |  |
| 158 | pending | evenly spaced sample | ;  |  |
| 161 | pending | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | ;  |  |
| 162 | pending | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | ;  |  |
| 171 | pending | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | ;  |  |
| 172 | pending | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | ;  |  |
| 175 | pending | layout_before_sites.json:46 140-2:162 | ;  |  |
| 177 | pending | layout_before_sites.json:47 140-2:164; layout_before_sites.json:48 140-2:165; layout_repairs_applied.json:17 140-2:165 | ;  |  |
| 178 | pending | layout_before_sites.json:48 140-2:165; layout_before_sites.json:49 140-2:166; layout_repairs_applied.json:17 140-2:165 | ;  |  |
| 179 | pending | layout_before_sites.json:49 140-2:166 | ;  |  |
| 180 | pending | layout_before_sites.json:49 140-2:166 | ;  |  |
| 197 | pending | evenly spaced sample | ;  |  |
| 202 | pending | layout_before_sites.json:50 140-2:197 | ;  |  |
| 203 | pending | layout_before_sites.json:50 140-2:197 | ;  |  |
| 208 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205 | ;  |  |
| 209 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205; layout_repairs_applied.json:18 140-2:206 | ;  |  |
| 210 | pending | layout_repairs_applied.json:18 140-2:206 | ;  |  |
| 214 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 215 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 220 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 221 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 222 | pending | layout_before_sites.json:57 140-2:220 | ;  |  |
| 223 | pending | layout_before_sites.json:57 140-2:220 | ;  |  |
| 224 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 225 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 234 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 235 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 237 | pending | evenly spaced sample | ;  |  |
| 249 | pending | layout_repairs_applied.json:21 140-2:251 | ;  |  |
| 250 | pending | layout_repairs_applied.json:19 140-2:252; layout_repairs_applied.json:20 140-2:252; layout_repairs_applied.json:21 140-2:251; layout_repairs_applied.json:22 140-2:252 | ;  |  |
| 251 | pending | layout_repairs_applied.json:19 140-2:252; layout_repairs_applied.json:20 140-2:252; layout_repairs_applied.json:22 140-2:252 | ;  |  |
| 257 | pending | layout_before_sites.json:60 140-2:259 | ;  |  |
| 264 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 265 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 272 | pending | layout_before_sites.json:62 140-2:280 | ;  |  |
| 273 | pending | layout_before_sites.json:62 140-2:280 | ;  |  |
| 276 | pending | evenly spaced sample; layout_before_sites.json:63 140-2:285 | ;  |  |
| 277 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 278 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 291 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | ;  |  |
| 292 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | ;  |  |
| 293 | pending | landscape page; layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | ;  |  |
| 294 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:24 140-2:302 | ;  |  |
| 300 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 301 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 302 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 309 | pending | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:26 140-2:321 | ;  |  |
| 310 | pending | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:26 140-2:321 | ;  |  |
| 315 | pending | evenly spaced sample; layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:25 140-2:328 | ;  |  |
| 316 | pending | layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_before_sites.json:71 140-2:329; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:25 140-2:328 | ;  |  |
| 317 | pending | layout_before_sites.json:71 140-2:329 | ;  |  |
| 318 | pending | layout_before_sites.json:71 140-2:329 | ;  |  |
| 319 | pending | layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:27 140-2:331; layout_repairs_applied.json:28 140-2:331 | ;  |  |
| 331 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | ;  |  |
| 332 | pending | landscape page; layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | ;  |  |
| 333 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | ;  |  |
| 334 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:30 140-2:344; layout_repairs_applied.json:32 140-2:344 | ;  |  |
| 335 | pending | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | ;  |  |
| 336 | pending | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | ;  |  |
| 338 | pending | layout_before_sites.json:75 140-2:348; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:29 140-2:348 | ;  |  |
| 339 | pending | layout_before_sites.json:75 140-2:348; layout_before_sites.json:76 140-2:349; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:29 140-2:348 | ;  |  |
| 340 | pending | layout_before_sites.json:76 140-2:349 | ;  |  |
| 342 | pending | layout_before_sites.json:77 140-2:352 | ;  |  |
| 343 | pending | layout_before_sites.json:77 140-2:352 | ;  |  |
| 350 | pending | layout_before_sites.json:78 140-2:362 | ;  |  |
| 351 | pending | layout_before_sites.json:78 140-2:362 | ;  |  |
| 355 | pending | evenly spaced sample | ;  |  |
| 358 | pending | layout_before_sites.json:79 140-2:371 | ;  |  |
| 359 | pending | layout_before_sites.json:79 140-2:371 | ;  |  |
| 366 | pending | layout_repairs_applied.json:33 140-2:382 | ;  |  |
| 367 | pending | layout_repairs_applied.json:33 140-2:382 | ;  |  |
| 368 | pending | layout_before_sites.json:80 140-2:384; layout_pass_sites.json:40 140-2:384; layout_pass_sites.json:64 140-2:384 | ;  |  |
| 370 | pending | layout_before_sites.json:81 140-2:387 | ;  |  |
| 371 | pending | layout_before_sites.json:81 140-2:387 | ;  |  |
| 377 | pending | layout_repairs_applied.json:34 140-2:397 | ;  |  |
| 378 | pending | layout_repairs_applied.json:34 140-2:397 | ;  |  |
| 383 | pending | layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404 | ;  |  |
| 384 | pending | layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404; layout_repairs_applied.json:35 140-2:407 | ;  |  |
| 385 | pending | layout_repairs_applied.json:35 140-2:407 | ;  |  |
| 387 | pending | layout_pass_sites.json:41 140-2:411 | ;  |  |
| 393 | pending | layout_repairs_applied.json:36 140-2:417; layout_repairs_applied.json:38 140-2:417 | ;  |  |
| 394 | pending | evenly spaced sample; layout_repairs_applied.json:36 140-2:417; layout_repairs_applied.json:38 140-2:417 | ;  |  |
| 395 | pending | layout_before_sites.json:84 140-2:419; layout_before_sites.json:85 140-2:419; layout_pass_sites.json:4 140-2:419; layout_pass_sites.json:42 140-2:419; layout_pass_sites.json:59 140-2:419; layout_pass_sites.json:65 140-2:419; layout_repairs_applied.json:37 140-2:419 | ;  |  |
| 398 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 399 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 405 | pending | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | ;  |  |
| 406 | pending | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | ;  |  |
| 415 | pending | layout_before_sites.json:89 140-2:443 | ;  |  |
| 416 | pending | layout_before_sites.json:89 140-2:443 | ;  |  |
| 421 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 422 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 423 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 424 | pending | layout_before_sites.json:91 140-2:452 | ;  |  |
| 425 | pending | layout_before_sites.json:91 140-2:452 | ;  |  |
| 426 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 427 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 428 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 429 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 430 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 431 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 433 | pending | evenly spaced sample | ;  |  |
| 435 | pending | layout_before_sites.json:94 140-2:462 | ;  |  |
| 436 | pending | layout_before_sites.json:94 140-2:462 | ;  |  |
| 459 | pending | layout_before_sites.json:95 140-2:492 | ;  |  |
| 466 | pending | layout_before_sites.json:96 140-2:502 | ;  |  |
| 469 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:39 140-2:508 | ;  |  |
| 470 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:39 140-2:508 | ;  |  |
| 471 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:39 140-2:508 | ;  |  |
| 472 | pending | evenly spaced sample | ;  |  |
| 474 | pending | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | ;  |  |
| 475 | pending | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | ;  |  |
| 480 | pending | layout_before_sites.json:101 140-2:519 | ;  |  |
| 481 | pending | layout_before_sites.json:101 140-2:519; layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:41 140-2:520 | ;  |  |
| 482 | pending | layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:41 140-2:520 | ;  |  |
| 487 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:42 140-2:527 | ;  |  |
| 488 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:42 140-2:527 | ;  |  |
| 491 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | ;  |  |
| 492 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | ;  |  |
| 493 | pending | layout_before_sites.json:107 140-2:536 | ;  |  |
| 494 | pending | layout_before_sites.json:107 140-2:536 | ;  |  |
| 512 | pending | evenly spaced sample | ;  |  |
| 518 | pending | layout_before_sites.json:108 140-2:567 | ;  |  |
| 519 | pending | layout_before_sites.json:108 140-2:567 | ;  |  |
| 520 | pending | layout_before_sites.json:108 140-2:567; layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:43 140-2:568; layout_repairs_applied.json:44 140-2:568 | ;  |  |
| 521 | pending | layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:43 140-2:568; layout_repairs_applied.json:44 140-2:568 | ;  |  |
| 529 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | ;  |  |
| 530 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | ;  |  |
| 531 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4; layout_before_sites.json:114 140-3:5 | ;  |  |
| 532 | pending | layout_before_sites.json:114 140-3:5; layout_repairs_applied.json:45 140-3:6 | ;  |  |
| 533 | pending | layout_repairs_applied.json:45 140-3:6 | ;  |  |
| 538 | pending | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | ;  |  |
| 539 | pending | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | ;  |  |
| 543 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 544 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 546 | pending | layout_repairs_applied.json:46 140-3:21 | ;  |  |
| 548 | pending | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | ;  |  |
| 549 | pending | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | ;  |  |
| 551 | pending | evenly spaced sample | ;  |  |
| 554 | pending | layout_repairs_applied.json:47 140-3:33 | ;  |  |
| 555 | pending | layout_repairs_applied.json:47 140-3:33 | ;  |  |
| 557 | pending | layout_before_sites.json:124 140-3:36 | ;  |  |
| 558 | pending | layout_before_sites.json:124 140-3:36 | ;  |  |
| 560 | pending | layout_repairs_applied.json:48 140-3:40 | ;  |  |
| 561 | pending | layout_repairs_applied.json:48 140-3:40; layout_repairs_applied.json:49 140-3:41 | ;  |  |
| 562 | pending | layout_repairs_applied.json:50 140-3:44 | ;  |  |
| 563 | pending | layout_repairs_applied.json:50 140-3:44 | ;  |  |
| 569 | pending | layout_repairs_applied.json:51 140-3:55; layout_repairs_applied.json:52 140-3:56 | ;  |  |
| 570 | pending | layout_repairs_applied.json:52 140-3:56 | ;  |  |
| 571 | pending | layout_before_sites.json:125 140-3:58 | ;  |  |
| 572 | pending | layout_before_sites.json:125 140-3:58; layout_before_sites.json:126 140-3:59 | ;  |  |
| 573 | pending | layout_before_sites.json:126 140-3:59 | ;  |  |
| 575 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 576 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 581 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 582 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 586 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 587 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 588 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 589 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 590 | pending | evenly spaced sample; layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75 | ;  |  |
| 591 | pending | layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75; layout_before_sites.json:133 140-3:76 | ;  |  |
| 592 | pending | layout_before_sites.json:133 140-3:76 | ;  |  |
| 599 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:53 140-3:85; layout_repairs_applied.json:54 140-3:85; layout_repairs_applied.json:55 140-3:85; layout_repairs_applied.json:56 140-3:85; layout_repairs_applied.json:57 140-3:85; layout_repairs_applied.json:58 140-3:85; layout_repairs_applied.json:59 140-3:85 | ;  |  |
| 600 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:53 140-3:85; layout_repairs_applied.json:54 140-3:85; layout_repairs_applied.json:55 140-3:85; layout_repairs_applied.json:56 140-3:85; layout_repairs_applied.json:57 140-3:85; layout_repairs_applied.json:58 140-3:85; layout_repairs_applied.json:59 140-3:85 | ;  |  |
| 601 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_before_sites.json:136 140-3:86; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:53 140-3:85; layout_repairs_applied.json:54 140-3:85; layout_repairs_applied.json:55 140-3:85; layout_repairs_applied.json:56 140-3:85; layout_repairs_applied.json:57 140-3:85; layout_repairs_applied.json:58 140-3:85; layout_repairs_applied.json:59 140-3:85 | ;  |  |
| 602 | pending | layout_before_sites.json:136 140-3:86; layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87 | ;  |  |
| 603 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87 | ;  |  |
| 604 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:60 140-3:88 | ;  |  |
| 605 | pending | layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:60 140-3:88 | ;  |  |
| 606 | pending | layout_before_sites.json:139 140-3:90 | ;  |  |
| 607 | pending | layout_before_sites.json:139 140-3:90 | ;  |  |
| 608 | pending | layout_before_sites.json:139 140-3:90; layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91 | ;  |  |
| 609 | pending | layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91; layout_before_sites.json:145 140-3:92 | ;  |  |
| 610 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 611 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 613 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 614 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 615 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95; layout_repairs_applied.json:61 140-3:97; layout_repairs_applied.json:67 140-3:97 | ;  |  |
| 616 | pending | layout_repairs_applied.json:61 140-3:97; layout_repairs_applied.json:67 140-3:97 | ;  |  |
| 617 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98; layout_repairs_applied.json:61 140-3:97; layout_repairs_applied.json:67 140-3:97 | ;  |  |
| 618 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98 | ;  |  |
| 625 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 626 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 627 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:62 140-3:107; layout_repairs_applied.json:63 140-3:107; layout_repairs_applied.json:64 140-3:107; layout_repairs_applied.json:65 140-3:107; layout_repairs_applied.json:66 140-3:107 | ;  |  |
| 630 | pending | evenly spaced sample | ;  |  |
| 631 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 632 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 641 | pending | layout_repairs_applied.json:68 140-3:121 | ;  |  |
| 642 | pending | layout_repairs_applied.json:68 140-3:121 | ;  |  |
| 669 | pending | evenly spaced sample; layout_before_sites.json:154 140-3:148 | ;  |  |
| 670 | pending | layout_before_sites.json:154 140-3:148 | ;  |  |
| 675 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 676 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 679 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 680 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 705 | pending | layout_before_sites.json:157 140-3:185 | ;  |  |
| 706 | pending | layout_before_sites.json:157 140-3:185; layout_repairs_applied.json:69 140-3:186 | ;  |  |
| 707 | pending | layout_repairs_applied.json:69 140-3:186 | ;  |  |
| 708 | pending | evenly spaced sample | ;  |  |
| 711 | pending | layout_before_sites.json:158 140-3:191; layout_before_sites.json:159 140-3:191; layout_before_sites.json:160 140-3:192 | ;  |  |
| 712 | pending | layout_before_sites.json:160 140-3:192 | ;  |  |
| 713 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 714 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 718 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 719 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 727 | pending | layout_repairs_applied.json:70 140-3:208 | ;  |  |
| 728 | pending | layout_repairs_applied.json:70 140-3:208; layout_repairs_applied.json:71 140-3:209 | ;  |  |
| 729 | pending | layout_repairs_applied.json:71 140-3:209 | ;  |  |
| 731 | pending | layout_before_sites.json:164 140-3:212 | ;  |  |
| 732 | pending | layout_before_sites.json:164 140-3:212; layout_before_sites.json:165 140-3:213 | ;  |  |
| 733 | pending | layout_before_sites.json:165 140-3:213 | ;  |  |
| 734 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 735 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 740 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_repairs_applied.json:72 140-3:221 | ;  |  |
| 741 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_repairs_applied.json:72 140-3:221 | ;  |  |
| 742 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_before_sites.json:169 140-3:222; layout_repairs_applied.json:72 140-3:221 | ;  |  |
| 743 | pending | layout_before_sites.json:169 140-3:222 | ;  |  |
| 747 | pending | evenly spaced sample | ;  |  |
| 751 | pending | layout_before_sites.json:170 140-3:231 | ;  |  |
| 752 | pending | layout_before_sites.json:170 140-3:231; layout_before_sites.json:171 140-3:232 | ;  |  |
| 753 | pending | layout_before_sites.json:171 140-3:232 | ;  |  |
| 763 | pending | layout_repairs_applied.json:73 140-3:245 | ;  |  |
| 764 | pending | layout_repairs_applied.json:73 140-3:245 | ;  |  |
| 775 | pending | layout_repairs_applied.json:74 140-3:261 | ;  |  |
| 776 | pending | layout_repairs_applied.json:74 140-3:261 | ;  |  |
| 777 | pending | layout_repairs_applied.json:74 140-3:261 | ;  |  |
| 787 | pending | evenly spaced sample | ;  |  |
| 789 | pending | layout_repairs_applied.json:75 140-3:275 | ;  |  |
| 790 | pending | layout_repairs_applied.json:75 140-3:275 | ;  |  |
| 795 | pending | layout_before_sites.json:172 140-3:282 | ;  |  |
| 796 | pending | layout_before_sites.json:172 140-3:282; layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 797 | pending | layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 798 | pending | layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 818 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 819 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 826 | pending | evenly spaced sample | ;  |  |
| 835 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:76 140-3:320 | ;  |  |
| 836 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:76 140-3:320 | ;  |  |
| 837 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:76 140-3:320 | ;  |  |
| 839 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 840 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 843 | pending | layout_before_sites.json:179 140-3:327 | ;  |  |
| 844 | pending | layout_before_sites.json:179 140-3:327; layout_before_sites.json:180 140-3:328; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:77 140-3:328 | ;  |  |
| 845 | pending | layout_before_sites.json:180 140-3:328; layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:73 140-3:329; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:77 140-3:328; layout_repairs_applied.json:78 140-3:329 | ;  |  |
| 846 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:78 140-3:329 | ;  |  |
| 847 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:78 140-3:329 | ;  |  |
| 851 | pending | layout_before_sites.json:182 140-3:334 | ;  |  |
| 852 | pending | layout_before_sites.json:182 140-3:334 | ;  |  |
| 853 | pending | layout_before_sites.json:182 140-3:334; layout_repairs_applied.json:80 140-3:335 | ;  |  |
| 854 | pending | layout_repairs_applied.json:80 140-3:335 | ;  |  |
| 865 | pending | evenly spaced sample; layout_before_sites.json:183 140-3:346 | ;  |  |
| 866 | pending | layout_before_sites.json:183 140-3:346 | ;  |  |
| 874 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 875 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 878 | pending | layout_before_sites.json:185 140-3:356 | ;  |  |
| 879 | pending | layout_before_sites.json:185 140-3:356; layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357 | ;  |  |
| 880 | pending | layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357; layout_repairs_applied.json:81 140-3:358 | ;  |  |
| 881 | pending | layout_repairs_applied.json:81 140-3:358 | ;  |  |
| 882 | pending | layout_repairs_applied.json:81 140-3:358 | ;  |  |
| 885 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362 | ;  |  |
| 886 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362; layout_repairs_applied.json:84 140-3:363 | ;  |  |
| 887 | pending | layout_repairs_applied.json:84 140-3:363 | ;  |  |
| 888 | pending | layout_repairs_applied.json:84 140-3:363 | ;  |  |
| 903 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 904 | pending | evenly spaced sample | ;  |  |
| 914 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 915 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 934 | pending | layout_repairs_applied.json:91 140-3:408; layout_repairs_applied.json:92 140-3:408; layout_repairs_applied.json:93 140-3:408 | ;  |  |
| 935 | pending | layout_repairs_applied.json:91 140-3:408; layout_repairs_applied.json:92 140-3:408; layout_repairs_applied.json:93 140-3:408 | ;  |  |
| 937 | pending | layout_repairs_applied.json:94 140-3:410 | ;  |  |
| 938 | pending | layout_repairs_applied.json:94 140-3:410 | ;  |  |
| 940 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 941 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 942 | pending | layout_before_sites.json:192 140-3:415 | ;  |  |
| 943 | pending | layout_before_sites.json:192 140-3:415 | ;  |  |
| 944 | pending | evenly spaced sample; layout_before_sites.json:192 140-3:415; layout_before_sites.json:193 140-3:416 | ;  |  |
| 945 | pending | layout_before_sites.json:193 140-3:416 | ;  |  |
| 947 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:98 140-3:419 | ;  |  |
| 948 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:98 140-3:419 | ;  |  |
| 953 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:95 140-3:425 | ;  |  |
| 954 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:95 140-3:425 | ;  |  |
| 955 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:95 140-3:425 | ;  |  |
| 957 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 958 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 959 | pending | layout_before_sites.json:197 140-3:431 | ;  |  |
| 960 | pending | layout_before_sites.json:197 140-3:431 | ;  |  |
| 961 | pending | layout_before_sites.json:197 140-3:431; layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432 | ;  |  |
| 962 | pending | layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432; layout_before_sites.json:200 140-3:433 | ;  |  |
| 963 | pending | layout_before_sites.json:200 140-3:433 | ;  |  |
| 964 | pending | layout_before_sites.json:200 140-3:433 | ;  |  |
| 966 | pending | layout_repairs_applied.json:107 140-3:436; layout_repairs_applied.json:108 140-3:436; layout_repairs_applied.json:109 140-3:436 | ;  |  |
| 967 | pending | layout_repairs_applied.json:107 140-3:436; layout_repairs_applied.json:108 140-3:436; layout_repairs_applied.json:109 140-3:436 | ;  |  |
| 968 | pending | layout_repairs_applied.json:107 140-3:436; layout_repairs_applied.json:108 140-3:436; layout_repairs_applied.json:109 140-3:436; layout_repairs_applied.json:110 140-3:437; layout_repairs_applied.json:111 140-3:437 | ;  |  |
| 969 | pending | layout_repairs_applied.json:110 140-3:437; layout_repairs_applied.json:111 140-3:437; layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438 | ;  |  |
| 970 | pending | layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438 | ;  |  |
| 971 | pending | layout_repairs_applied.json:112 140-3:438; layout_repairs_applied.json:113 140-3:438; layout_repairs_applied.json:114 140-3:438; layout_repairs_applied.json:115 140-3:438; layout_repairs_applied.json:116 140-3:439 | ;  |  |
| 972 | pending | layout_repairs_applied.json:103 140-3:441; layout_repairs_applied.json:116 140-3:439; layout_repairs_applied.json:117 140-3:440; layout_repairs_applied.json:99 140-3:440 | ;  |  |
| 973 | pending | layout_repairs_applied.json:103 140-3:441 | ;  |  |
| 974 | pending | layout_repairs_applied.json:103 140-3:441; layout_repairs_applied.json:106 140-3:443 | ;  |  |
| 975 | pending | layout_before_sites.json:201 140-3:444; layout_repairs_applied.json:106 140-3:443 | ;  |  |
| 976 | pending | layout_before_sites.json:201 140-3:444 | ;  |  |
| 978 | pending | layout_pass_sites.json:12 140-3:446; layout_repairs_applied.json:101 140-3:446 | ;  |  |
| 979 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:12 140-3:446; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:100 140-3:448; layout_repairs_applied.json:101 140-3:446 | ;  |  |
| 980 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:100 140-3:448; layout_repairs_applied.json:104 140-3:449; layout_repairs_applied.json:105 140-3:449 | ;  |  |
| 981 | pending | layout_repairs_applied.json:104 140-3:449; layout_repairs_applied.json:105 140-3:449 | ;  |  |
| 982 | pending | layout_repairs_applied.json:104 140-3:449; layout_repairs_applied.json:105 140-3:449 | ;  |  |
| 983 | pending | evenly spaced sample | ;  |  |
| 985 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 986 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 987 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 991 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 992 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 993 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 995 | pending | layout_repairs_applied.json:118 140-3:462 | ;  |  |
| 996 | pending | layout_repairs_applied.json:118 140-3:462; layout_repairs_applied.json:119 140-3:463; layout_repairs_applied.json:120 140-3:463; layout_repairs_applied.json:121 140-3:463 | ;  |  |
| 997 | pending | layout_repairs_applied.json:119 140-3:463; layout_repairs_applied.json:120 140-3:463; layout_repairs_applied.json:121 140-3:463 | ;  |  |
| 998 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 999 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 1000 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 1001 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 1002 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 1003 | pending | layout_before_sites.json:208 140-3:468; layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 1004 | pending | layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 1013 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 1014 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 1015 | pending | layout_before_sites.json:211 140-3:479; layout_repairs_applied.json:122 140-3:480; layout_repairs_applied.json:123 140-3:480 | ;  |  |
| 1016 | pending | layout_repairs_applied.json:122 140-3:480; layout_repairs_applied.json:123 140-3:480 | ;  |  |
| 1019 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1020 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1021 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1022 | pending | evenly spaced sample | ;  |  |
| 1023 | pending | layout_before_sites.json:213 140-3:491 | ;  |  |
| 1024 | pending | layout_before_sites.json:213 140-3:491 | ;  |  |
| 1025 | pending | layout_before_sites.json:213 140-3:491; layout_before_sites.json:214 140-3:492 | ;  |  |
| 1026 | pending | layout_before_sites.json:214 140-3:492; layout_repairs_applied.json:124 140-3:494 | ;  |  |
| 1027 | pending | layout_repairs_applied.json:124 140-3:494 | ;  |  |
| 1032 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 1033 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 1037 | pending | layout_repairs_applied.json:126 140-3:503 | ;  |  |
| 1038 | pending | layout_repairs_applied.json:126 140-3:503 | ;  |  |
| 1041 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:127 140-3:506; layout_repairs_applied.json:128 140-3:506 | ;  |  |
| 1042 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:127 140-3:506; layout_repairs_applied.json:128 140-3:506 | ;  |  |
| 1043 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:127 140-3:506; layout_repairs_applied.json:128 140-3:506 | ;  |  |
| 1045 | pending | layout_before_sites.json:217 140-3:509 | ;  |  |
| 1046 | pending | layout_before_sites.json:217 140-3:509; layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1047 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1048 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1052 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 1053 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 1056 | pending | layout_before_sites.json:221 140-3:517 | ;  |  |
| 1057 | pending | layout_before_sites.json:221 140-3:517; layout_before_sites.json:222 140-3:518 | ;  |  |
| 1058 | pending | layout_before_sites.json:222 140-3:518; layout_before_sites.json:223 140-3:519; layout_repairs_applied.json:129 140-3:519; layout_repairs_applied.json:134 140-3:519 | ;  |  |
| 1059 | pending | layout_before_sites.json:223 140-3:519; layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:129 140-3:519; layout_repairs_applied.json:133 140-3:520; layout_repairs_applied.json:134 140-3:519 | ;  |  |
| 1060 | pending | layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:133 140-3:520 | ;  |  |
| 1062 | pending | evenly spaced sample; layout_before_sites.json:225 140-3:522 | ;  |  |
| 1063 | pending | layout_before_sites.json:225 140-3:522 | ;  |  |
| 1064 | pending | layout_before_sites.json:225 140-3:522; layout_repairs_applied.json:135 140-3:523 | ;  |  |
| 1065 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:135 140-3:523; layout_repairs_applied.json:136 140-3:524; layout_repairs_applied.json:137 140-3:524 | ;  |  |
| 1066 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:130 140-3:525; layout_repairs_applied.json:136 140-3:524; layout_repairs_applied.json:137 140-3:524; layout_repairs_applied.json:138 140-3:525; layout_repairs_applied.json:139 140-3:525 | ;  |  |
| 1067 | pending | layout_repairs_applied.json:130 140-3:525; layout_repairs_applied.json:138 140-3:525; layout_repairs_applied.json:139 140-3:525 | ;  |  |
| 1072 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530 | ;  |  |
| 1073 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530; layout_before_sites.json:229 140-3:531 | ;  |  |
| 1074 | pending | layout_before_sites.json:229 140-3:531 | ;  |  |
| 1075 | pending | layout_before_sites.json:229 140-3:531; layout_before_sites.json:230 140-3:532 | ;  |  |
| 1076 | pending | layout_before_sites.json:230 140-3:532; layout_before_sites.json:231 140-3:533 | ;  |  |
| 1077 | pending | layout_before_sites.json:231 140-3:533; layout_before_sites.json:232 140-3:534 | ;  |  |
| 1078 | pending | layout_before_sites.json:232 140-3:534 | ;  |  |
| 1079 | pending | layout_before_sites.json:232 140-3:534; layout_before_sites.json:233 140-3:535 | ;  |  |
| 1080 | pending | layout_before_sites.json:233 140-3:535; layout_before_sites.json:234 140-3:536; layout_repairs_applied.json:140 140-3:536 | ;  |  |
| 1081 | pending | layout_before_sites.json:234 140-3:536; layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_repairs_applied.json:140 140-3:536 | ;  |  |
| 1082 | pending | layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_before_sites.json:238 140-3:538; layout_before_sites.json:239 140-3:539 | ;  |  |
| 1083 | pending | layout_before_sites.json:239 140-3:539; layout_before_sites.json:240 140-3:540 | ;  |  |
| 1084 | pending | layout_before_sites.json:240 140-3:540 | ;  |  |
| 1085 | pending | layout_before_sites.json:240 140-3:540; layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 1086 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 1087 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541; layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:141 140-3:542; layout_repairs_applied.json:145 140-3:542 | ;  |  |
| 1088 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:141 140-3:542; layout_repairs_applied.json:145 140-3:542 | ;  |  |
| 1089 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_before_sites.json:245 140-3:543; layout_repairs_applied.json:141 140-3:542; layout_repairs_applied.json:145 140-3:542; layout_repairs_applied.json:146 140-3:543; layout_repairs_applied.json:147 140-3:543; layout_repairs_applied.json:148 140-3:543 | ;  |  |
| 1090 | pending | layout_before_sites.json:245 140-3:543; layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:146 140-3:543; layout_repairs_applied.json:147 140-3:543; layout_repairs_applied.json:148 140-3:543; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544 | ;  |  |
| 1091 | pending | layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544 | ;  |  |
| 1092 | pending | layout_before_sites.json:246 140-3:544; layout_before_sites.json:247 140-3:545; layout_repairs_applied.json:142 140-3:545; layout_repairs_applied.json:143 140-3:545; layout_repairs_applied.json:149 140-3:544; layout_repairs_applied.json:150 140-3:544; layout_repairs_applied.json:151 140-3:545; layout_repairs_applied.json:152 140-3:545; layout_repairs_applied.json:153 140-3:545; layout_repairs_applied.json:154 140-3:545; layout_repairs_applied.json:155 140-3:545; layout_repairs_applied.json:156 140-3:545 | ;  |  |
| 1093 | pending | layout_before_sites.json:247 140-3:545; layout_before_sites.json:248 140-3:546; layout_repairs_applied.json:142 140-3:545; layout_repairs_applied.json:143 140-3:545; layout_repairs_applied.json:144 140-3:546; layout_repairs_applied.json:151 140-3:545; layout_repairs_applied.json:152 140-3:545; layout_repairs_applied.json:153 140-3:545; layout_repairs_applied.json:154 140-3:545; layout_repairs_applied.json:155 140-3:545; layout_repairs_applied.json:156 140-3:545 | ;  |  |
| 1094 | pending | layout_before_sites.json:248 140-3:546; layout_repairs_applied.json:144 140-3:546 | ;  |  |
| 1095 | pending | layout_before_sites.json:248 140-3:546; layout_before_sites.json:249 140-3:547; layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:144 140-3:546; layout_repairs_applied.json:157 140-3:548 | ;  |  |
| 1096 | pending | layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:157 140-3:548 | ;  |  |
| 1101 | pending | evenly spaced sample; layout_before_sites.json:251 140-3:554; layout_repairs_applied.json:158 140-3:554 | ;  |  |
| 1102 | pending | layout_before_sites.json:251 140-3:554; layout_before_sites.json:252 140-3:555; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:158 140-3:554; layout_repairs_applied.json:159 140-3:555 | ;  |  |
| 1103 | pending | layout_before_sites.json:252 140-3:555; layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:159 140-3:555; layout_repairs_applied.json:160 140-3:556 | ;  |  |
| 1104 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_repairs_applied.json:160 140-3:556 | ;  |  |
| 1105 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_repairs_applied.json:160 140-3:556 | ;  |  |
| 1106 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_before_sites.json:255 140-3:557; layout_before_sites.json:256 140-3:558; layout_pass_sites.json:14 140-3:557; layout_pass_sites.json:75 140-3:557; layout_repairs_applied.json:160 140-3:556; layout_repairs_applied.json:162 140-3:557 | ;  |  |
| 1107 | pending | layout_before_sites.json:256 140-3:558; layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1108 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1109 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1111 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:163 140-3:561 | ;  |  |
| 1112 | pending | landscape page; layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:163 140-3:561 | ;  |  |
| 1113 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:163 140-3:561 | ;  |  |
| 1114 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:161 140-3:562; layout_repairs_applied.json:163 140-3:561; layout_repairs_applied.json:166 140-3:562; layout_repairs_applied.json:167 140-3:562 | ;  |  |
| 1115 | pending | layout_repairs_applied.json:161 140-3:562; layout_repairs_applied.json:166 140-3:562; layout_repairs_applied.json:167 140-3:562 | ;  |  |
| 1117 | pending | layout_repairs_applied.json:168 140-3:565 | ;  |  |
| 1118 | pending | layout_repairs_applied.json:168 140-3:565 | ;  |  |
| 1119 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567 | ;  |  |
| 1120 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567 | ;  |  |
| 1121 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567; layout_repairs_applied.json:169 140-3:568 | ;  |  |
| 1122 | pending | layout_repairs_applied.json:169 140-3:568 | ;  |  |
| 1124 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 1125 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 1127 | pending | layout_before_sites.json:263 140-3:573; layout_repairs_applied.json:170 140-3:573 | ;  |  |
| 1128 | pending | layout_before_sites.json:263 140-3:573; layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:170 140-3:573; layout_repairs_applied.json:171 140-3:574 | ;  |  |
| 1129 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:171 140-3:574 | ;  |  |
| 1130 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:171 140-3:574 | ;  |  |
| 1131 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:171 140-3:574; layout_repairs_applied.json:173 140-3:575 | ;  |  |
| 1132 | pending | layout_before_sites.json:265 140-3:577; layout_repairs_applied.json:173 140-3:575 | ;  |  |
| 1133 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 1134 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 1139 | pending | layout_before_sites.json:266 140-3:582 | ;  |  |
| 1140 | pending | evenly spaced sample; layout_before_sites.json:266 140-3:582 | ;  |  |
| 1142 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 1143 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 1144 | pending | layout_before_sites.json:267 140-3:585; layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 1145 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 1146 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586; layout_before_sites.json:270 140-3:587 | ;  |  |
| 1147 | pending | layout_before_sites.json:270 140-3:587 | ;  |  |
| 1148 | pending | layout_before_sites.json:270 140-3:587; layout_before_sites.json:271 140-3:588 | ;  |  |
| 1149 | pending | layout_before_sites.json:271 140-3:588 | ;  |  |
| 1150 | pending | layout_before_sites.json:271 140-3:588; layout_before_sites.json:272 140-3:589 | ;  |  |
| 1151 | pending | layout_before_sites.json:272 140-3:589; layout_repairs_applied.json:175 140-3:590 | ;  |  |
| 1152 | pending | layout_repairs_applied.json:175 140-3:590 | ;  |  |
| 1154 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 1155 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 1161 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 1162 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 1169 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:176 140-3:606 | ;  |  |
| 1170 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:176 140-3:606 | ;  |  |
| 1171 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:176 140-3:606 | ;  |  |
| 1173 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:178 140-3:609 | ;  |  |
| 1174 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:178 140-3:609 | ;  |  |
| 1179 | pending | evenly spaced sample; layout_before_sites.json:275 140-3:616 | ;  |  |
| 1180 | pending | layout_before_sites.json:275 140-3:616; layout_before_sites.json:276 140-3:617 | ;  |  |
| 1181 | pending | layout_before_sites.json:276 140-3:617 | ;  |  |
| 1182 | pending | layout_before_sites.json:276 140-3:617 | ;  |  |
| 1183 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:179 140-3:619 | ;  |  |
| 1184 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:179 140-3:619 | ;  |  |
| 1185 | pending | layout_before_sites.json:278 140-3:621; layout_pass_sites.json:18 140-3:621; layout_repairs_applied.json:177 140-3:621; layout_repairs_applied.json:184 140-3:621 | ;  |  |
| 1186 | pending | layout_before_sites.json:278 140-3:621; layout_pass_sites.json:18 140-3:621; layout_repairs_applied.json:177 140-3:621; layout_repairs_applied.json:184 140-3:621; layout_repairs_applied.json:185 140-3:622; layout_repairs_applied.json:186 140-3:622; layout_repairs_applied.json:187 140-3:622; layout_repairs_applied.json:188 140-3:622; layout_repairs_applied.json:189 140-3:622 | ;  |  |
| 1187 | pending | layout_repairs_applied.json:185 140-3:622; layout_repairs_applied.json:186 140-3:622; layout_repairs_applied.json:187 140-3:622; layout_repairs_applied.json:188 140-3:622; layout_repairs_applied.json:189 140-3:622; layout_repairs_applied.json:190 140-3:623; layout_repairs_applied.json:191 140-3:623 | ;  |  |
| 1188 | pending | layout_repairs_applied.json:190 140-3:623; layout_repairs_applied.json:191 140-3:623 | ;  |  |
| 1190 | pending | layout_before_sites.json:279 140-3:625 | ;  |  |
| 1191 | pending | layout_before_sites.json:279 140-3:625 | ;  |  |
| 1192 | pending | layout_before_sites.json:280 140-3:627 | ;  |  |
| 1193 | pending | layout_before_sites.json:280 140-3:627; layout_repairs_applied.json:192 140-3:628 | ;  |  |
| 1194 | pending | layout_before_sites.json:281 140-3:629; layout_repairs_applied.json:192 140-3:628 | ;  |  |
| 1195 | pending | layout_before_sites.json:281 140-3:629 | ;  |  |
| 1196 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 1197 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 1201 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:194 140-3:637; layout_repairs_applied.json:196 140-3:637 | ;  |  |
| 1202 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:193 140-3:638; layout_repairs_applied.json:194 140-3:637; layout_repairs_applied.json:196 140-3:637 | ;  |  |
| 1203 | pending | layout_repairs_applied.json:193 140-3:638 | ;  |  |
| 1213 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:207 140-3:649 | ;  |  |
| 1214 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:207 140-3:649 | ;  |  |
| 1217 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:197 140-3:653; layout_repairs_applied.json:208 140-3:653 | ;  |  |
| 1218 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:197 140-3:653; layout_repairs_applied.json:208 140-3:653 | ;  |  |
| 1219 | pending | evenly spaced sample; layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:197 140-3:653; layout_repairs_applied.json:208 140-3:653 | ;  |  |
| 1222 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:209 140-3:656; layout_repairs_applied.json:210 140-3:656 | ;  |  |
| 1223 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:209 140-3:656; layout_repairs_applied.json:210 140-3:656 | ;  |  |
| 1224 | pending | layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657 | ;  |  |
| 1225 | pending | layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_repairs_applied.json:198 140-3:658; layout_repairs_applied.json:199 140-3:658 | ;  |  |
| 1226 | pending | layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:198 140-3:658; layout_repairs_applied.json:199 140-3:658; layout_repairs_applied.json:200 140-3:659; layout_repairs_applied.json:201 140-3:659 | ;  |  |
| 1227 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:200 140-3:659; layout_repairs_applied.json:201 140-3:659 | ;  |  |
| 1228 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:200 140-3:659; layout_repairs_applied.json:201 140-3:659; layout_repairs_applied.json:202 140-3:660 | ;  |  |
| 1229 | pending | layout_repairs_applied.json:202 140-3:660 | ;  |  |
| 1231 | pending | layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:203 140-3:662 | ;  |  |
| 1232 | pending | layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:203 140-3:662 | ;  |  |
| 1238 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 1239 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 1248 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 1249 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 1253 | pending | layout_repairs_applied.json:213 140-3:685; layout_repairs_applied.json:214 140-3:685 | ;  |  |
| 1254 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:213 140-3:685; layout_repairs_applied.json:214 140-3:685; layout_repairs_applied.json:215 140-3:686 | ;  |  |
| 1255 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:215 140-3:686 | ;  |  |
| 1257 | pending | layout_repairs_applied.json:216 140-3:688; layout_repairs_applied.json:217 140-3:688 | ;  |  |
| 1258 | pending | evenly spaced sample; layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:216 140-3:688; layout_repairs_applied.json:217 140-3:688; layout_repairs_applied.json:218 140-3:689 | ;  |  |
| 1259 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:218 140-3:689 | ;  |  |
| 1260 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:218 140-3:689 | ;  |  |
| 1263 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692 | ;  |  |
| 1264 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692; layout_repairs_applied.json:219 140-3:693; layout_repairs_applied.json:220 140-3:693 | ;  |  |
| 1265 | pending | layout_repairs_applied.json:219 140-3:693; layout_repairs_applied.json:220 140-3:693 | ;  |  |
| 1269 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 1270 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 1273 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1274 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1275 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1276 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1277 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1278 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1284 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:221 140-4:20 | ;  |  |
| 1285 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:221 140-4:20 | ;  |  |
| 1291 | pending | layout_before_sites.json:311 140-4:29 | ;  |  |
| 1292 | pending | layout_before_sites.json:311 140-4:29; layout_repairs_applied.json:223 140-4:31; layout_repairs_applied.json:224 140-4:31; layout_repairs_applied.json:225 140-4:31 | ;  |  |
| 1293 | pending | layout_repairs_applied.json:223 140-4:31; layout_repairs_applied.json:224 140-4:31; layout_repairs_applied.json:225 140-4:31; layout_repairs_applied.json:226 140-4:32; layout_repairs_applied.json:227 140-4:32 | ;  |  |
| 1294 | pending | layout_repairs_applied.json:226 140-4:32; layout_repairs_applied.json:227 140-4:32; layout_repairs_applied.json:228 140-4:33 | ;  |  |
| 1295 | pending | layout_repairs_applied.json:228 140-4:33 | ;  |  |
| 1296 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:228 140-4:33 | ;  |  |
| 1297 | pending | evenly spaced sample; layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34 | ;  |  |
| 1298 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:229 140-4:35; layout_repairs_applied.json:230 140-4:35 | ;  |  |
| 1299 | pending | layout_repairs_applied.json:229 140-4:35; layout_repairs_applied.json:230 140-4:35 | ;  |  |
| 1303 | pending | layout_before_sites.json:314 140-4:39 | ;  |  |
| 1304 | pending | layout_before_sites.json:314 140-4:39; layout_before_sites.json:315 140-4:40 | ;  |  |
| 1305 | pending | layout_before_sites.json:315 140-4:40; layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41 | ;  |  |
| 1306 | pending | layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41; layout_before_sites.json:318 140-4:42 | ;  |  |
| 1307 | pending | layout_before_sites.json:318 140-4:42; layout_before_sites.json:319 140-4:43 | ;  |  |
| 1308 | pending | layout_before_sites.json:319 140-4:43; layout_before_sites.json:320 140-4:44; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:231 140-4:44 | ;  |  |
| 1309 | pending | layout_before_sites.json:320 140-4:44; layout_before_sites.json:321 140-4:45; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:231 140-4:44 | ;  |  |
| 1310 | pending | layout_before_sites.json:321 140-4:45; layout_before_sites.json:322 140-4:46 | ;  |  |
| 1311 | pending | layout_before_sites.json:322 140-4:46; layout_before_sites.json:323 140-4:47 | ;  |  |
| 1312 | pending | layout_before_sites.json:323 140-4:47 | ;  |  |
| 1313 | pending | layout_before_sites.json:323 140-4:47; layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48 | ;  |  |
| 1314 | pending | layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48; layout_before_sites.json:327 140-4:49 | ;  |  |
| 1315 | pending | layout_before_sites.json:327 140-4:49; layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 1316 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 1317 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50; layout_before_sites.json:331 140-4:51 | ;  |  |
| 1318 | pending | layout_before_sites.json:331 140-4:51; layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52 | ;  |  |
| 1319 | pending | layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52 | ;  |  |
| 1320 | pending | layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52; layout_before_sites.json:334 140-4:53; layout_before_sites.json:335 140-4:54 | ;  |  |
| 1321 | pending | layout_before_sites.json:335 140-4:54; layout_before_sites.json:336 140-4:55 | ;  |  |
| 1322 | pending | layout_before_sites.json:336 140-4:55; layout_before_sites.json:337 140-4:56 | ;  |  |
| 1323 | pending | layout_before_sites.json:337 140-4:56 | ;  |  |
| 1324 | pending | layout_before_sites.json:337 140-4:56; layout_before_sites.json:338 140-4:57 | ;  |  |
| 1325 | pending | layout_before_sites.json:338 140-4:57 | ;  |  |
| 1326 | pending | layout_repairs_applied.json:244 140-4:59 | ;  |  |
| 1327 | pending | layout_repairs_applied.json:244 140-4:59 | ;  |  |
| 1328 | pending | layout_repairs_applied.json:245 140-4:61; layout_repairs_applied.json:246 140-4:61; layout_repairs_applied.json:247 140-4:61; layout_repairs_applied.json:248 140-4:61 | ;  |  |
| 1329 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:245 140-4:61; layout_repairs_applied.json:246 140-4:61; layout_repairs_applied.json:247 140-4:61; layout_repairs_applied.json:248 140-4:61; layout_repairs_applied.json:249 140-4:62 | ;  |  |
| 1330 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:249 140-4:62 | ;  |  |
| 1332 | pending | layout_repairs_applied.json:242 140-4:65 | ;  |  |
| 1333 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:233 140-4:66; layout_repairs_applied.json:234 140-4:66; layout_repairs_applied.json:235 140-4:66; layout_repairs_applied.json:242 140-4:65 | ;  |  |
| 1334 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:233 140-4:66; layout_repairs_applied.json:234 140-4:66; layout_repairs_applied.json:235 140-4:66 | ;  |  |
| 1335 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_before_sites.json:343 140-4:67; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:233 140-4:66; layout_repairs_applied.json:234 140-4:66; layout_repairs_applied.json:235 140-4:66 | ;  |  |
| 1336 | pending | layout_before_sites.json:343 140-4:67 | ;  |  |
| 1337 | pending | evenly spaced sample; layout_before_sites.json:344 140-4:70 | ;  |  |
| 1338 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 1339 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 1343 | pending | layout_repairs_applied.json:250 140-4:74 | ;  |  |
| 1344 | pending | layout_repairs_applied.json:250 140-4:74 | ;  |  |
| 1345 | pending | layout_repairs_applied.json:243 140-4:75; layout_repairs_applied.json:250 140-4:74; layout_repairs_applied.json:251 140-4:75; layout_repairs_applied.json:252 140-4:75; layout_repairs_applied.json:253 140-4:75 | ;  |  |
| 1346 | pending | layout_repairs_applied.json:243 140-4:75; layout_repairs_applied.json:251 140-4:75; layout_repairs_applied.json:252 140-4:75; layout_repairs_applied.json:253 140-4:75 | ;  |  |
| 1347 | pending | layout_repairs_applied.json:243 140-4:75; layout_repairs_applied.json:251 140-4:75; layout_repairs_applied.json:252 140-4:75; layout_repairs_applied.json:253 140-4:75; layout_repairs_applied.json:254 140-4:76; layout_repairs_applied.json:255 140-4:76 | ;  |  |
| 1348 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:254 140-4:76; layout_repairs_applied.json:255 140-4:76; layout_repairs_applied.json:258 140-4:77 | ;  |  |
| 1349 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:258 140-4:77 | ;  |  |
| 1350 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:258 140-4:77; layout_repairs_applied.json:259 140-4:78; layout_repairs_applied.json:260 140-4:78 | ;  |  |
| 1351 | pending | layout_repairs_applied.json:259 140-4:78; layout_repairs_applied.json:260 140-4:78; layout_repairs_applied.json:261 140-4:79; layout_repairs_applied.json:262 140-4:79 | ;  |  |
| 1352 | pending | layout_repairs_applied.json:261 140-4:79; layout_repairs_applied.json:262 140-4:79; layout_repairs_applied.json:263 140-4:80 | ;  |  |
| 1353 | pending | layout_repairs_applied.json:263 140-4:80 | ;  |  |
| 1354 | pending | layout_repairs_applied.json:263 140-4:80; layout_repairs_applied.json:264 140-4:81; layout_repairs_applied.json:265 140-4:81 | ;  |  |
| 1355 | pending | layout_repairs_applied.json:264 140-4:81; layout_repairs_applied.json:265 140-4:81 | ;  |  |
| 1366 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1367 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1368 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1373 | pending | layout_repairs_applied.json:269 140-4:96; layout_repairs_applied.json:270 140-4:96 | ;  |  |
| 1374 | pending | layout_repairs_applied.json:269 140-4:96; layout_repairs_applied.json:270 140-4:96; layout_repairs_applied.json:271 140-4:97; layout_repairs_applied.json:272 140-4:97 | ;  |  |
| 1375 | pending | layout_repairs_applied.json:271 140-4:97; layout_repairs_applied.json:272 140-4:97; layout_repairs_applied.json:273 140-4:98 | ;  |  |
| 1376 | pending | evenly spaced sample; layout_repairs_applied.json:273 140-4:98 | ;  |  |
| 1377 | pending | layout_before_sites.json:349 140-4:99; layout_repairs_applied.json:273 140-4:98 | ;  |  |
| 1378 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1379 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1380 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1381 | pending | layout_before_sites.json:350 140-4:101 | ;  |  |
| 1382 | pending | layout_before_sites.json:350 140-4:101; layout_before_sites.json:351 140-4:102 | ;  |  |
| 1383 | pending | layout_before_sites.json:351 140-4:102 | ;  |  |
| 1385 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 1386 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 1391 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:266 140-4:113 | ;  |  |
| 1392 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:266 140-4:113 | ;  |  |
| 1415 | pending | evenly spaced sample | ;  |  |
| 1417 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:274 140-4:136 | ;  |  |
| 1418 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:274 140-4:136 | ;  |  |
| 1425 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 1426 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 1427 | pending | layout_before_sites.json:356 140-4:149 | ;  |  |
| 1432 | pending | layout_before_sites.json:357 140-4:154 | ;  |  |
| 1446 | pending | layout_repairs_applied.json:276 140-4:172 | ;  |  |
| 1447 | pending | layout_repairs_applied.json:276 140-4:172; layout_repairs_applied.json:277 140-4:174 | ;  |  |
| 1448 | pending | layout_repairs_applied.json:277 140-4:174; layout_repairs_applied.json:278 140-4:175; layout_repairs_applied.json:279 140-4:175 | ;  |  |
| 1449 | pending | layout_repairs_applied.json:278 140-4:175; layout_repairs_applied.json:279 140-4:175 | ;  |  |
| 1453 | pending | layout_before_sites.json:358 140-4:181; layout_before_sites.json:359 140-4:181 | ;  |  |
| 1454 | pending | evenly spaced sample | ;  |  |
| 1456 | pending | layout_before_sites.json:360 140-4:186 | ;  |  |
| 1457 | pending | layout_before_sites.json:360 140-4:186; layout_before_sites.json:361 140-4:188 | ;  |  |
| 1458 | pending | layout_before_sites.json:361 140-4:188 | ;  |  |
| 1467 | pending | layout_repairs_applied.json:280 140-4:203; layout_repairs_applied.json:281 140-4:203 | ;  |  |
| 1468 | pending | layout_repairs_applied.json:282 140-4:205 | ;  |  |
| 1469 | pending | layout_repairs_applied.json:282 140-4:205 | ;  |  |
| 1489 | pending | layout_before_sites.json:362 140-4:230 | ;  |  |
| 1490 | pending | layout_before_sites.json:362 140-4:230 | ;  |  |
| 1494 | pending | evenly spaced sample | ;  |  |
| 1495 | pending | layout_before_sites.json:363 140-4:236 | ;  |  |
| 1496 | pending | layout_before_sites.json:363 140-4:236 | ;  |  |
| 1502 | pending | layout_before_sites.json:364 140-4:245 | ;  |  |
| 1505 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 1506 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 1507 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 1519 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 1520 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 1521 | pending | layout_before_sites.json:367 140-4:266 | ;  |  |
| 1522 | pending | layout_before_sites.json:367 140-4:266 | ;  |  |
| 1523 | pending | layout_before_sites.json:367 140-4:266; layout_before_sites.json:368 140-4:267 | ;  |  |
| 1524 | pending | layout_before_sites.json:368 140-4:267; layout_before_sites.json:369 140-4:268; layout_before_sites.json:370 140-4:269 | ;  |  |
| 1525 | pending | layout_before_sites.json:370 140-4:269; layout_before_sites.json:371 140-4:270 | ;  |  |
| 1526 | pending | layout_before_sites.json:371 140-4:270; layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:286 140-4:271; layout_repairs_applied.json:288 140-4:271 | ;  |  |
| 1527 | pending | layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_before_sites.json:374 140-4:272; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:286 140-4:271; layout_repairs_applied.json:288 140-4:271 | ;  |  |
| 1528 | pending | layout_before_sites.json:374 140-4:272; layout_before_sites.json:375 140-4:273; layout_before_sites.json:376 140-4:274 | ;  |  |
| 1529 | pending | layout_before_sites.json:376 140-4:274; layout_before_sites.json:377 140-4:275 | ;  |  |
| 1530 | pending | layout_before_sites.json:377 140-4:275; layout_before_sites.json:378 140-4:276; layout_repairs_applied.json:287 140-4:276 | ;  |  |
| 1531 | pending | layout_before_sites.json:378 140-4:276; layout_before_sites.json:379 140-4:277; layout_repairs_applied.json:287 140-4:276 | ;  |  |
| 1532 | pending | layout_before_sites.json:379 140-4:277; layout_before_sites.json:380 140-4:278; layout_before_sites.json:381 140-4:279 | ;  |  |
| 1533 | pending | evenly spaced sample; layout_before_sites.json:381 140-4:279; layout_before_sites.json:382 140-4:280 | ;  |  |

### LM_EN_master_annotated.pdf

PDF SHA-256: `5f90f4d9023bf8877bdbf51e62488ef9db1747786ce2a3cbe946db2ab040746c`.

| Physical page | Status | Selection reason | Reviewer and inspection basis | Observation |
|---|---|---|---|---|
| 1 | reviewed | evenly spaced sample | root; Previously reviewed page; identical RGB pixels and PNG file after rebuild. | Actually inspected full 900px title page: author, full French title, year1981, Annotated master, archive/cotes, scan count and edition date are cleanly separated and contained; no clipped or missing type observed. |
| 6 | pending | layout_before_sites.json:1 140-1:4 | ;  |  |
| 7 | pending | layout_before_sites.json:1 140-1:4 | ;  |  |
| 8 | pending | layout_before_sites.json:1 140-1:4 | ;  |  |
| 10 | pending | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:294 140-1:10 | ;  |  |
| 11 | pending | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:294 140-1:10 | ;  |  |
| 12 | pending | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:294 140-1:10 | ;  |  |
| 13 | pending | layout_before_sites.json:2 140-1:10; layout_before_sites.json:3 140-1:10; layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:28 140-1:10; layout_pass_sites.json:29 140-1:10; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:51 140-1:10; layout_pass_sites.json:52 140-1:10; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:290 140-1:10; layout_repairs_applied.json:291 140-1:10; layout_repairs_applied.json:292 140-1:12; layout_repairs_applied.json:294 140-1:10 | ;  |  |
| 14 | pending | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:292 140-1:12 | ;  |  |
| 15 | pending | layout_before_sites.json:4 140-1:12; layout_before_sites.json:5 140-1:12; layout_before_sites.json:6 140-1:12; layout_before_sites.json:7 140-1:12; layout_pass_sites.json:30 140-1:12; layout_pass_sites.json:53 140-1:12; layout_repairs_applied.json:292 140-1:12 | ;  |  |
| 16 | pending | layout_before_sites.json:8 140-1:15 | ;  |  |
| 17 | pending | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:8 140-1:15; layout_before_sites.json:9 140-1:16 | ;  |  |
| 18 | pending | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:9 140-1:16 | ;  |  |
| 19 | pending | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:9 140-1:16 | ;  |  |
| 20 | pending | layout_before_sites.json:10 140-1:16; layout_before_sites.json:11 140-1:16; layout_before_sites.json:12 140-1:16; layout_before_sites.json:13 140-1:17; layout_before_sites.json:9 140-1:16 | ;  |  |
| 21 | pending | layout_before_sites.json:13 140-1:17; layout_before_sites.json:14 140-1:18; layout_pass_sites.json:31 140-1:18 | ;  |  |
| 22 | pending | layout_before_sites.json:14 140-1:18; layout_pass_sites.json:31 140-1:18 | ;  |  |
| 23 | pending | layout_before_sites.json:14 140-1:18; layout_before_sites.json:15 140-1:19; layout_pass_sites.json:31 140-1:18; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:54 140-1:19; layout_repairs_applied.json:293 140-1:19 | ;  |  |
| 24 | pending | layout_before_sites.json:15 140-1:19; layout_before_sites.json:16 140-1:20; layout_pass_sites.json:32 140-1:19; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:54 140-1:19; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:293 140-1:19; layout_repairs_applied.json:297 140-1:20; layout_repairs_applied.json:302 140-1:20 | ;  |  |
| 25 | pending | layout_before_sites.json:16 140-1:20; layout_pass_sites.json:33 140-1:20; layout_pass_sites.json:55 140-1:20; layout_repairs_applied.json:297 140-1:20; layout_repairs_applied.json:302 140-1:20 | ;  |  |
| 27 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23 | ;  |  |
| 28 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23 | ;  |  |
| 29 | pending | layout_before_sites.json:17 140-1:23; layout_before_sites.json:18 140-1:23; layout_repairs_applied.json:303 140-1:25 | ;  |  |
| 32 | pending | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | ;  |  |
| 33 | pending | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | ;  |  |
| 34 | pending | layout_before_sites.json:19 140-1:30; layout_before_sites.json:20 140-1:30 | ;  |  |
| 35 | pending | layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | ;  |  |
| 36 | pending | layout_before_sites.json:21 140-1:32; layout_before_sites.json:22 140-1:32 | ;  |  |
| 40 | pending | evenly spaced sample | ;  |  |
| 41 | pending | layout_before_sites.json:23 140-1:36; layout_before_sites.json:24 140-1:36; layout_pass_sites.json:34 140-1:36; layout_pass_sites.json:56 140-1:36; layout_repairs_applied.json:298 140-1:36 | ;  |  |
| 42 | pending | layout_before_sites.json:25 140-2:4 | ;  |  |
| 43 | pending | layout_before_sites.json:25 140-2:4 | ;  |  |
| 59 | pending | layout_before_sites.json:26 140-2:28; layout_before_sites.json:27 140-2:29 | ;  |  |
| 60 | pending | layout_before_sites.json:27 140-2:29 | ;  |  |
| 65 | pending | layout_before_sites.json:28 140-2:35 | ;  |  |
| 69 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 70 | pending | layout_before_sites.json:29 140-2:39 | ;  |  |
| 72 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 73 | pending | layout_before_sites.json:30 140-2:42 | ;  |  |
| 74 | pending | layout_before_sites.json:30 140-2:42; layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44 | ;  |  |
| 75 | pending | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44 | ;  |  |
| 76 | pending | layout_before_sites.json:31 140-2:44; layout_before_sites.json:32 140-2:44; layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | ;  |  |
| 77 | pending | layout_before_sites.json:33 140-2:45; layout_before_sites.json:34 140-2:45 | ;  |  |
| 80 | pending | evenly spaced sample | ;  |  |
| 94 | pending | layout_before_sites.json:35 140-2:69 | ;  |  |
| 95 | pending | layout_before_sites.json:35 140-2:69 | ;  |  |
| 104 | pending | layout_before_sites.json:36 140-2:80 | ;  |  |
| 110 | pending | layout_before_sites.json:37 140-2:88 | ;  |  |
| 111 | pending | layout_before_sites.json:37 140-2:88; layout_repairs_applied.json:304 140-2:89 | ;  |  |
| 112 | pending | layout_repairs_applied.json:304 140-2:89 | ;  |  |
| 119 | pending | evenly spaced sample | ;  |  |
| 139 | pending | layout_before_sites.json:38 140-2:122 | ;  |  |
| 140 | pending | layout_before_sites.json:38 140-2:122 | ;  |  |
| 145 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 146 | pending | layout_before_sites.json:39 140-2:130 | ;  |  |
| 155 | pending | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | ;  |  |
| 156 | pending | layout_before_sites.json:40 140-2:141; layout_before_sites.json:41 140-2:141 | ;  |  |
| 159 | pending | evenly spaced sample | ;  |  |
| 162 | pending | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | ;  |  |
| 163 | pending | layout_before_sites.json:42 140-2:148; layout_before_sites.json:43 140-2:148 | ;  |  |
| 172 | pending | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | ;  |  |
| 173 | pending | layout_before_sites.json:44 140-2:159; layout_before_sites.json:45 140-2:159 | ;  |  |
| 175 | pending | layout_before_sites.json:46 140-2:162 | ;  |  |
| 176 | pending | layout_before_sites.json:46 140-2:162 | ;  |  |
| 177 | pending | layout_before_sites.json:47 140-2:164 | ;  |  |
| 178 | pending | layout_before_sites.json:47 140-2:164; layout_before_sites.json:48 140-2:165; layout_repairs_applied.json:306 140-2:165 | ;  |  |
| 179 | pending | layout_before_sites.json:48 140-2:165; layout_before_sites.json:49 140-2:166; layout_repairs_applied.json:306 140-2:165 | ;  |  |
| 180 | pending | layout_before_sites.json:49 140-2:166 | ;  |  |
| 198 | pending | evenly spaced sample | ;  |  |
| 203 | pending | layout_before_sites.json:50 140-2:197 | ;  |  |
| 204 | pending | layout_before_sites.json:50 140-2:197 | ;  |  |
| 208 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205 | ;  |  |
| 209 | pending | layout_before_sites.json:51 140-2:205; layout_before_sites.json:52 140-2:205; layout_repairs_applied.json:307 140-2:206 | ;  |  |
| 210 | pending | layout_repairs_applied.json:307 140-2:206 | ;  |  |
| 214 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 215 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 216 | pending | layout_before_sites.json:53 140-2:212 | ;  |  |
| 221 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 222 | pending | layout_before_sites.json:54 140-2:217; layout_before_sites.json:55 140-2:217; layout_before_sites.json:56 140-2:217 | ;  |  |
| 223 | pending | layout_before_sites.json:57 140-2:220 | ;  |  |
| 224 | pending | layout_before_sites.json:57 140-2:220 | ;  |  |
| 225 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 226 | pending | layout_before_sites.json:58 140-2:222 | ;  |  |
| 235 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 236 | pending | layout_before_sites.json:59 140-2:233 | ;  |  |
| 238 | pending | evenly spaced sample | ;  |  |
| 250 | pending | layout_repairs_applied.json:310 140-2:251 | ;  |  |
| 251 | pending | layout_repairs_applied.json:308 140-2:252; layout_repairs_applied.json:309 140-2:252; layout_repairs_applied.json:310 140-2:251; layout_repairs_applied.json:311 140-2:252 | ;  |  |
| 252 | pending | layout_repairs_applied.json:308 140-2:252; layout_repairs_applied.json:309 140-2:252; layout_repairs_applied.json:311 140-2:252 | ;  |  |
| 258 | pending | layout_before_sites.json:60 140-2:259 | ;  |  |
| 259 | pending | layout_before_sites.json:60 140-2:259 | ;  |  |
| 265 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 266 | pending | layout_before_sites.json:61 140-2:269 | ;  |  |
| 273 | pending | layout_before_sites.json:62 140-2:280 | ;  |  |
| 274 | pending | layout_before_sites.json:62 140-2:280 | ;  |  |
| 277 | pending | evenly spaced sample; layout_before_sites.json:63 140-2:285 | ;  |  |
| 278 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 279 | pending | layout_before_sites.json:63 140-2:285 | ;  |  |
| 293 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:313 140-2:302 | ;  |  |
| 294 | pending | landscape page; layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:313 140-2:302 | ;  |  |
| 295 | pending | layout_before_sites.json:64 140-2:302; layout_pass_sites.json:2 140-2:302; layout_pass_sites.json:57 140-2:302; layout_repairs_applied.json:313 140-2:302 | ;  |  |
| 301 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 302 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 303 | pending | layout_before_sites.json:65 140-2:310; layout_before_sites.json:66 140-2:310 | ;  |  |
| 310 | pending | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:315 140-2:321 | ;  |  |
| 311 | pending | layout_before_sites.json:67 140-2:321; layout_before_sites.json:68 140-2:321; layout_repairs_applied.json:315 140-2:321 | ;  |  |
| 317 | pending | evenly spaced sample; layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:314 140-2:328 | ;  |  |
| 318 | pending | layout_before_sites.json:69 140-2:328; layout_before_sites.json:70 140-2:328; layout_before_sites.json:71 140-2:329; layout_pass_sites.json:35 140-2:328; layout_pass_sites.json:36 140-2:328; layout_pass_sites.json:60 140-2:328; layout_pass_sites.json:61 140-2:328; layout_repairs_applied.json:314 140-2:328 | ;  |  |
| 319 | pending | layout_before_sites.json:71 140-2:329 | ;  |  |
| 320 | pending | layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:316 140-2:331; layout_repairs_applied.json:317 140-2:331 | ;  |  |
| 321 | pending | layout_before_sites.json:72 140-2:331; layout_pass_sites.json:37 140-2:331; layout_pass_sites.json:62 140-2:331; layout_repairs_applied.json:316 140-2:331; layout_repairs_applied.json:317 140-2:331 | ;  |  |
| 333 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 334 | pending | landscape page; layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 335 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 336 | pending | layout_before_sites.json:73 140-2:344; layout_pass_sites.json:3 140-2:344; layout_pass_sites.json:58 140-2:344; layout_repairs_applied.json:319 140-2:344; layout_repairs_applied.json:321 140-2:344 | ;  |  |
| 337 | pending | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | ;  |  |
| 338 | pending | layout_before_sites.json:74 140-2:346; layout_pass_sites.json:38 140-2:346; layout_pass_sites.json:63 140-2:346 | ;  |  |
| 340 | pending | layout_before_sites.json:75 140-2:348; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:318 140-2:348 | ;  |  |
| 341 | pending | layout_before_sites.json:75 140-2:348; layout_before_sites.json:76 140-2:349; layout_pass_sites.json:39 140-2:348; layout_repairs_applied.json:318 140-2:348 | ;  |  |
| 342 | pending | layout_before_sites.json:76 140-2:349 | ;  |  |
| 344 | pending | layout_before_sites.json:77 140-2:352 | ;  |  |
| 345 | pending | layout_before_sites.json:77 140-2:352 | ;  |  |
| 352 | pending | layout_before_sites.json:78 140-2:362 | ;  |  |
| 353 | pending | layout_before_sites.json:78 140-2:362 | ;  |  |
| 356 | pending | evenly spaced sample | ;  |  |
| 360 | pending | layout_before_sites.json:79 140-2:371 | ;  |  |
| 361 | pending | layout_before_sites.json:79 140-2:371 | ;  |  |
| 368 | pending | layout_repairs_applied.json:322 140-2:382 | ;  |  |
| 369 | pending | layout_repairs_applied.json:322 140-2:382 | ;  |  |
| 370 | pending | layout_before_sites.json:80 140-2:384; layout_pass_sites.json:40 140-2:384; layout_pass_sites.json:64 140-2:384 | ;  |  |
| 372 | pending | layout_before_sites.json:81 140-2:387 | ;  |  |
| 373 | pending | layout_before_sites.json:81 140-2:387 | ;  |  |
| 380 | pending | layout_repairs_applied.json:323 140-2:397 | ;  |  |
| 385 | pending | layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404 | ;  |  |
| 386 | pending | layout_before_sites.json:82 140-2:404; layout_before_sites.json:83 140-2:404 | ;  |  |
| 387 | pending | layout_repairs_applied.json:324 140-2:407 | ;  |  |
| 390 | pending | layout_pass_sites.json:41 140-2:411 | ;  |  |
| 395 | pending | layout_repairs_applied.json:325 140-2:417; layout_repairs_applied.json:327 140-2:417 | ;  |  |
| 396 | pending | evenly spaced sample; layout_repairs_applied.json:325 140-2:417; layout_repairs_applied.json:327 140-2:417 | ;  |  |
| 397 | pending | layout_before_sites.json:84 140-2:419; layout_before_sites.json:85 140-2:419; layout_pass_sites.json:4 140-2:419; layout_pass_sites.json:42 140-2:419; layout_pass_sites.json:59 140-2:419; layout_pass_sites.json:65 140-2:419; layout_repairs_applied.json:326 140-2:419 | ;  |  |
| 398 | pending | layout_before_sites.json:84 140-2:419; layout_before_sites.json:85 140-2:419; layout_pass_sites.json:4 140-2:419; layout_pass_sites.json:42 140-2:419; layout_pass_sites.json:59 140-2:419; layout_pass_sites.json:65 140-2:419; layout_repairs_applied.json:326 140-2:419 | ;  |  |
| 400 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 401 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 402 | pending | layout_before_sites.json:86 140-2:423 | ;  |  |
| 407 | pending | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | ;  |  |
| 408 | pending | layout_before_sites.json:87 140-2:430; layout_before_sites.json:88 140-2:430 | ;  |  |
| 418 | pending | layout_before_sites.json:89 140-2:443 | ;  |  |
| 419 | pending | layout_before_sites.json:89 140-2:443 | ;  |  |
| 424 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 425 | pending | layout_before_sites.json:90 140-2:450 | ;  |  |
| 426 | pending | layout_before_sites.json:90 140-2:450; layout_before_sites.json:91 140-2:452 | ;  |  |
| 427 | pending | layout_before_sites.json:91 140-2:452 | ;  |  |
| 428 | pending | layout_before_sites.json:91 140-2:452 | ;  |  |
| 429 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 430 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 431 | pending | layout_before_sites.json:92 140-2:454 | ;  |  |
| 432 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 433 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 434 | pending | layout_before_sites.json:93 140-2:457 | ;  |  |
| 435 | pending | evenly spaced sample | ;  |  |
| 438 | pending | layout_before_sites.json:94 140-2:462 | ;  |  |
| 439 | pending | layout_before_sites.json:94 140-2:462 | ;  |  |
| 461 | pending | layout_before_sites.json:95 140-2:492 | ;  |  |
| 462 | pending | layout_before_sites.json:95 140-2:492 | ;  |  |
| 469 | pending | layout_before_sites.json:96 140-2:502 | ;  |  |
| 472 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:328 140-2:508 | ;  |  |
| 473 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:328 140-2:508 | ;  |  |
| 474 | pending | layout_before_sites.json:97 140-2:508; layout_before_sites.json:98 140-2:508; layout_pass_sites.json:43 140-2:508; layout_pass_sites.json:66 140-2:508; layout_repairs_applied.json:328 140-2:508 | ;  |  |
| 475 | pending | evenly spaced sample | ;  |  |
| 477 | pending | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | ;  |  |
| 478 | pending | layout_before_sites.json:100 140-2:512; layout_before_sites.json:99 140-2:512; layout_pass_sites.json:44 140-2:512; layout_pass_sites.json:67 140-2:512 | ;  |  |
| 483 | pending | layout_before_sites.json:101 140-2:519; layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:330 140-2:520 | ;  |  |
| 484 | pending | layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:330 140-2:520 | ;  |  |
| 485 | pending | layout_before_sites.json:102 140-2:520; layout_repairs_applied.json:330 140-2:520 | ;  |  |
| 489 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:331 140-2:527 | ;  |  |
| 490 | pending | layout_before_sites.json:103 140-2:527; layout_pass_sites.json:45 140-2:527; layout_pass_sites.json:68 140-2:527; layout_repairs_applied.json:331 140-2:527 | ;  |  |
| 493 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | ;  |  |
| 494 | pending | layout_before_sites.json:104 140-2:533; layout_before_sites.json:105 140-2:533; layout_before_sites.json:106 140-2:533 | ;  |  |
| 496 | pending | layout_before_sites.json:107 140-2:536 | ;  |  |
| 514 | pending | evenly spaced sample | ;  |  |
| 521 | pending | layout_before_sites.json:108 140-2:567 | ;  |  |
| 522 | pending | layout_before_sites.json:108 140-2:567; layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:332 140-2:568; layout_repairs_applied.json:333 140-2:568 | ;  |  |
| 523 | pending | layout_before_sites.json:109 140-2:568; layout_before_sites.json:110 140-2:568; layout_repairs_applied.json:332 140-2:568; layout_repairs_applied.json:333 140-2:568 | ;  |  |
| 532 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | ;  |  |
| 533 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4 | ;  |  |
| 534 | pending | layout_before_sites.json:111 140-3:4; layout_before_sites.json:112 140-3:4; layout_before_sites.json:113 140-3:4; layout_before_sites.json:114 140-3:5 | ;  |  |
| 535 | pending | layout_before_sites.json:114 140-3:5; layout_repairs_applied.json:334 140-3:6 | ;  |  |
| 536 | pending | layout_repairs_applied.json:334 140-3:6 | ;  |  |
| 541 | pending | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | ;  |  |
| 542 | pending | layout_before_sites.json:115 140-3:14; layout_before_sites.json:116 140-3:14 | ;  |  |
| 546 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 547 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 548 | pending | layout_before_sites.json:117 140-3:18; layout_before_sites.json:118 140-3:18; layout_before_sites.json:119 140-3:18; layout_before_sites.json:120 140-3:18; layout_before_sites.json:121 140-3:18 | ;  |  |
| 549 | pending | layout_repairs_applied.json:335 140-3:21 | ;  |  |
| 551 | pending | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | ;  |  |
| 552 | pending | layout_before_sites.json:122 140-3:24; layout_before_sites.json:123 140-3:24 | ;  |  |
| 553 | pending | evenly spaced sample | ;  |  |
| 557 | pending | layout_repairs_applied.json:336 140-3:33 | ;  |  |
| 558 | pending | layout_repairs_applied.json:336 140-3:33 | ;  |  |
| 560 | pending | layout_before_sites.json:124 140-3:36 | ;  |  |
| 561 | pending | layout_before_sites.json:124 140-3:36 | ;  |  |
| 563 | pending | layout_repairs_applied.json:337 140-3:40; layout_repairs_applied.json:338 140-3:41 | ;  |  |
| 564 | pending | layout_repairs_applied.json:338 140-3:41 | ;  |  |
| 565 | pending | layout_repairs_applied.json:339 140-3:44 | ;  |  |
| 566 | pending | layout_repairs_applied.json:339 140-3:44 | ;  |  |
| 571 | pending | layout_repairs_applied.json:340 140-3:55 | ;  |  |
| 572 | pending | layout_repairs_applied.json:340 140-3:55; layout_repairs_applied.json:341 140-3:56 | ;  |  |
| 573 | pending | layout_before_sites.json:125 140-3:58; layout_repairs_applied.json:341 140-3:56 | ;  |  |
| 574 | pending | layout_before_sites.json:125 140-3:58; layout_before_sites.json:126 140-3:59 | ;  |  |
| 575 | pending | layout_before_sites.json:126 140-3:59 | ;  |  |
| 576 | pending | layout_before_sites.json:126 140-3:59 | ;  |  |
| 578 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 579 | pending | layout_before_sites.json:127 140-3:62 | ;  |  |
| 583 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 584 | pending | layout_before_sites.json:128 140-3:68 | ;  |  |
| 589 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 590 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 591 | pending | layout_before_sites.json:129 140-3:73; layout_before_sites.json:130 140-3:73; layout_pass_sites.json:46 140-3:73; layout_pass_sites.json:83 140-3:73 | ;  |  |
| 592 | pending | layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75 | ;  |  |
| 593 | pending | evenly spaced sample; layout_before_sites.json:131 140-3:75; layout_before_sites.json:132 140-3:75; layout_before_sites.json:133 140-3:76 | ;  |  |
| 594 | pending | layout_before_sites.json:133 140-3:76 | ;  |  |
| 602 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:342 140-3:85; layout_repairs_applied.json:343 140-3:85; layout_repairs_applied.json:344 140-3:85; layout_repairs_applied.json:345 140-3:85; layout_repairs_applied.json:346 140-3:85; layout_repairs_applied.json:347 140-3:85; layout_repairs_applied.json:348 140-3:85 | ;  |  |
| 603 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:342 140-3:85; layout_repairs_applied.json:343 140-3:85; layout_repairs_applied.json:344 140-3:85; layout_repairs_applied.json:345 140-3:85; layout_repairs_applied.json:346 140-3:85; layout_repairs_applied.json:347 140-3:85; layout_repairs_applied.json:348 140-3:85 | ;  |  |
| 604 | pending | layout_before_sites.json:134 140-3:85; layout_before_sites.json:135 140-3:85; layout_before_sites.json:136 140-3:86; layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:1 140-3:85; layout_pass_sites.json:5 140-3:85; layout_pass_sites.json:69 140-3:85; layout_pass_sites.json:70 140-3:85; layout_repairs_applied.json:342 140-3:85; layout_repairs_applied.json:343 140-3:85; layout_repairs_applied.json:344 140-3:85; layout_repairs_applied.json:345 140-3:85; layout_repairs_applied.json:346 140-3:85; layout_repairs_applied.json:347 140-3:85; layout_repairs_applied.json:348 140-3:85 | ;  |  |
| 605 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87 | ;  |  |
| 606 | pending | layout_before_sites.json:137 140-3:87; layout_before_sites.json:138 140-3:87; layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:349 140-3:88 | ;  |  |
| 607 | pending | layout_pass_sites.json:6 140-3:88; layout_repairs_applied.json:349 140-3:88 | ;  |  |
| 608 | pending | layout_before_sites.json:139 140-3:90 | ;  |  |
| 609 | pending | layout_before_sites.json:139 140-3:90 | ;  |  |
| 610 | pending | layout_before_sites.json:139 140-3:90; layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91 | ;  |  |
| 611 | pending | layout_before_sites.json:140 140-3:91; layout_before_sites.json:141 140-3:91; layout_before_sites.json:142 140-3:91; layout_before_sites.json:143 140-3:91; layout_before_sites.json:144 140-3:91; layout_before_sites.json:145 140-3:92 | ;  |  |
| 612 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 613 | pending | layout_before_sites.json:145 140-3:92 | ;  |  |
| 616 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 617 | pending | layout_before_sites.json:146 140-3:95; layout_before_sites.json:147 140-3:95 | ;  |  |
| 618 | pending | layout_repairs_applied.json:350 140-3:97; layout_repairs_applied.json:356 140-3:97 | ;  |  |
| 619 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98; layout_repairs_applied.json:350 140-3:97; layout_repairs_applied.json:356 140-3:97 | ;  |  |
| 620 | pending | layout_before_sites.json:148 140-3:98; layout_before_sites.json:149 140-3:98; layout_before_sites.json:150 140-3:98; layout_before_sites.json:151 140-3:98 | ;  |  |
| 628 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:351 140-3:107; layout_repairs_applied.json:352 140-3:107; layout_repairs_applied.json:353 140-3:107; layout_repairs_applied.json:354 140-3:107; layout_repairs_applied.json:355 140-3:107 | ;  |  |
| 629 | pending | layout_before_sites.json:152 140-3:107; layout_pass_sites.json:7 140-3:107; layout_pass_sites.json:71 140-3:107; layout_repairs_applied.json:351 140-3:107; layout_repairs_applied.json:352 140-3:107; layout_repairs_applied.json:353 140-3:107; layout_repairs_applied.json:354 140-3:107; layout_repairs_applied.json:355 140-3:107 | ;  |  |
| 632 | pending | evenly spaced sample | ;  |  |
| 634 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 635 | pending | layout_before_sites.json:153 140-3:111 | ;  |  |
| 643 | pending | layout_repairs_applied.json:357 140-3:121 | ;  |  |
| 644 | pending | layout_repairs_applied.json:357 140-3:121 | ;  |  |
| 645 | pending | layout_repairs_applied.json:357 140-3:121 | ;  |  |
| 671 | pending | layout_before_sites.json:154 140-3:148 | ;  |  |
| 672 | pending | evenly spaced sample; layout_before_sites.json:154 140-3:148 | ;  |  |
| 678 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 679 | pending | layout_before_sites.json:155 140-3:154 | ;  |  |
| 682 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 683 | pending | layout_before_sites.json:156 140-3:158 | ;  |  |
| 708 | pending | layout_before_sites.json:157 140-3:185 | ;  |  |
| 709 | pending | layout_before_sites.json:157 140-3:185; layout_repairs_applied.json:358 140-3:186 | ;  |  |
| 710 | pending | layout_repairs_applied.json:358 140-3:186 | ;  |  |
| 711 | pending | evenly spaced sample | ;  |  |
| 713 | pending | layout_before_sites.json:158 140-3:191; layout_before_sites.json:159 140-3:191 | ;  |  |
| 714 | pending | layout_before_sites.json:158 140-3:191; layout_before_sites.json:159 140-3:191; layout_before_sites.json:160 140-3:192 | ;  |  |
| 715 | pending | layout_before_sites.json:160 140-3:192 | ;  |  |
| 716 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 717 | pending | layout_before_sites.json:161 140-3:194 | ;  |  |
| 721 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 722 | pending | layout_before_sites.json:162 140-3:199; layout_before_sites.json:163 140-3:199 | ;  |  |
| 730 | pending | layout_repairs_applied.json:359 140-3:208 | ;  |  |
| 731 | pending | layout_repairs_applied.json:359 140-3:208; layout_repairs_applied.json:360 140-3:209 | ;  |  |
| 732 | pending | layout_repairs_applied.json:360 140-3:209 | ;  |  |
| 734 | pending | layout_before_sites.json:164 140-3:212 | ;  |  |
| 735 | pending | layout_before_sites.json:164 140-3:212; layout_before_sites.json:165 140-3:213 | ;  |  |
| 736 | pending | layout_before_sites.json:165 140-3:213; layout_before_sites.json:166 140-3:215 | ;  |  |
| 737 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 738 | pending | layout_before_sites.json:166 140-3:215 | ;  |  |
| 743 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_repairs_applied.json:361 140-3:221 | ;  |  |
| 744 | pending | layout_before_sites.json:167 140-3:221; layout_before_sites.json:168 140-3:221; layout_before_sites.json:169 140-3:222; layout_repairs_applied.json:361 140-3:221 | ;  |  |
| 745 | pending | layout_before_sites.json:169 140-3:222 | ;  |  |
| 746 | pending | layout_before_sites.json:169 140-3:222 | ;  |  |
| 751 | pending | evenly spaced sample | ;  |  |
| 754 | pending | layout_before_sites.json:170 140-3:231 | ;  |  |
| 755 | pending | layout_before_sites.json:170 140-3:231; layout_before_sites.json:171 140-3:232 | ;  |  |
| 756 | pending | layout_before_sites.json:171 140-3:232 | ;  |  |
| 766 | pending | layout_repairs_applied.json:362 140-3:245 | ;  |  |
| 767 | pending | layout_repairs_applied.json:362 140-3:245 | ;  |  |
| 778 | pending | layout_repairs_applied.json:363 140-3:261 | ;  |  |
| 779 | pending | layout_repairs_applied.json:363 140-3:261 | ;  |  |
| 780 | pending | layout_repairs_applied.json:363 140-3:261 | ;  |  |
| 790 | pending | evenly spaced sample | ;  |  |
| 792 | pending | layout_repairs_applied.json:364 140-3:275 | ;  |  |
| 793 | pending | layout_repairs_applied.json:364 140-3:275 | ;  |  |
| 798 | pending | layout_before_sites.json:172 140-3:282 | ;  |  |
| 799 | pending | layout_before_sites.json:172 140-3:282 | ;  |  |
| 800 | pending | layout_before_sites.json:172 140-3:282; layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 801 | pending | layout_before_sites.json:173 140-3:283; layout_before_sites.json:174 140-3:283 | ;  |  |
| 821 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 822 | pending | layout_before_sites.json:175 140-3:303; layout_before_sites.json:176 140-3:303 | ;  |  |
| 830 | pending | evenly spaced sample | ;  |  |
| 839 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:365 140-3:320 | ;  |  |
| 840 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:365 140-3:320 | ;  |  |
| 841 | pending | layout_before_sites.json:177 140-3:320; layout_pass_sites.json:8 140-3:320; layout_repairs_applied.json:365 140-3:320 | ;  |  |
| 842 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 843 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 844 | pending | layout_before_sites.json:178 140-3:323 | ;  |  |
| 847 | pending | layout_before_sites.json:179 140-3:327 | ;  |  |
| 848 | pending | layout_before_sites.json:179 140-3:327; layout_before_sites.json:180 140-3:328; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:366 140-3:328 | ;  |  |
| 849 | pending | layout_before_sites.json:180 140-3:328; layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:72 140-3:328; layout_pass_sites.json:73 140-3:329; layout_pass_sites.json:9 140-3:328; layout_repairs_applied.json:366 140-3:328; layout_repairs_applied.json:367 140-3:329 | ;  |  |
| 850 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:367 140-3:329 | ;  |  |
| 851 | pending | layout_before_sites.json:181 140-3:329; layout_pass_sites.json:10 140-3:329; layout_pass_sites.json:73 140-3:329; layout_repairs_applied.json:367 140-3:329 | ;  |  |
| 855 | pending | layout_before_sites.json:182 140-3:334 | ;  |  |
| 856 | pending | layout_before_sites.json:182 140-3:334 | ;  |  |
| 857 | pending | layout_before_sites.json:182 140-3:334; layout_repairs_applied.json:369 140-3:335 | ;  |  |
| 858 | pending | layout_repairs_applied.json:369 140-3:335 | ;  |  |
| 869 | pending | evenly spaced sample; layout_before_sites.json:183 140-3:346 | ;  |  |
| 870 | pending | layout_before_sites.json:183 140-3:346 | ;  |  |
| 878 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 879 | pending | layout_before_sites.json:184 140-3:353 | ;  |  |
| 882 | pending | layout_before_sites.json:185 140-3:356 | ;  |  |
| 883 | pending | layout_before_sites.json:185 140-3:356; layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357 | ;  |  |
| 884 | pending | layout_before_sites.json:186 140-3:357; layout_before_sites.json:187 140-3:357; layout_repairs_applied.json:370 140-3:358 | ;  |  |
| 885 | pending | layout_repairs_applied.json:370 140-3:358 | ;  |  |
| 886 | pending | layout_repairs_applied.json:370 140-3:358 | ;  |  |
| 889 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362 | ;  |  |
| 890 | pending | layout_before_sites.json:188 140-3:362; layout_before_sites.json:189 140-3:362; layout_repairs_applied.json:373 140-3:363 | ;  |  |
| 891 | pending | layout_repairs_applied.json:373 140-3:363 | ;  |  |
| 892 | pending | layout_repairs_applied.json:373 140-3:363 | ;  |  |
| 907 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 908 | pending | layout_before_sites.json:190 140-3:379 | ;  |  |
| 909 | pending | evenly spaced sample | ;  |  |
| 918 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 919 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 920 | pending | layout_before_sites.json:191 140-3:391 | ;  |  |
| 939 | pending | layout_repairs_applied.json:380 140-3:408; layout_repairs_applied.json:381 140-3:408; layout_repairs_applied.json:382 140-3:408 | ;  |  |
| 940 | pending | layout_repairs_applied.json:380 140-3:408; layout_repairs_applied.json:381 140-3:408; layout_repairs_applied.json:382 140-3:408 | ;  |  |
| 941 | pending | layout_repairs_applied.json:383 140-3:410 | ;  |  |
| 942 | pending | layout_repairs_applied.json:383 140-3:410 | ;  |  |
| 943 | pending | layout_repairs_applied.json:383 140-3:410 | ;  |  |
| 945 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 946 | pending | layout_pass_sites.json:47 140-3:413; layout_pass_sites.json:84 140-3:413 | ;  |  |
| 947 | pending | layout_before_sites.json:192 140-3:415 | ;  |  |
| 948 | pending | evenly spaced sample; layout_before_sites.json:192 140-3:415; layout_before_sites.json:193 140-3:416 | ;  |  |
| 949 | pending | layout_before_sites.json:193 140-3:416 | ;  |  |
| 950 | pending | layout_before_sites.json:193 140-3:416 | ;  |  |
| 951 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:387 140-3:419 | ;  |  |
| 952 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:387 140-3:419 | ;  |  |
| 953 | pending | layout_before_sites.json:194 140-3:419; layout_repairs_applied.json:387 140-3:419 | ;  |  |
| 958 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:384 140-3:425 | ;  |  |
| 959 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:384 140-3:425 | ;  |  |
| 960 | pending | layout_pass_sites.json:11 140-3:425; layout_repairs_applied.json:384 140-3:425 | ;  |  |
| 962 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 963 | pending | layout_before_sites.json:195 140-3:429; layout_before_sites.json:196 140-3:429 | ;  |  |
| 964 | pending | layout_before_sites.json:197 140-3:431 | ;  |  |
| 965 | pending | layout_before_sites.json:197 140-3:431 | ;  |  |
| 966 | pending | layout_before_sites.json:197 140-3:431; layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432 | ;  |  |
| 967 | pending | layout_before_sites.json:198 140-3:432; layout_before_sites.json:199 140-3:432; layout_before_sites.json:200 140-3:433 | ;  |  |
| 968 | pending | layout_before_sites.json:200 140-3:433 | ;  |  |
| 969 | pending | layout_before_sites.json:200 140-3:433 | ;  |  |
| 971 | pending | layout_repairs_applied.json:396 140-3:436; layout_repairs_applied.json:397 140-3:436; layout_repairs_applied.json:398 140-3:436 | ;  |  |
| 972 | pending | layout_repairs_applied.json:396 140-3:436; layout_repairs_applied.json:397 140-3:436; layout_repairs_applied.json:398 140-3:436 | ;  |  |
| 973 | pending | layout_repairs_applied.json:396 140-3:436; layout_repairs_applied.json:397 140-3:436; layout_repairs_applied.json:398 140-3:436; layout_repairs_applied.json:399 140-3:437; layout_repairs_applied.json:400 140-3:437 | ;  |  |
| 974 | pending | layout_repairs_applied.json:399 140-3:437; layout_repairs_applied.json:400 140-3:437; layout_repairs_applied.json:401 140-3:438; layout_repairs_applied.json:402 140-3:438; layout_repairs_applied.json:403 140-3:438; layout_repairs_applied.json:404 140-3:438 | ;  |  |
| 975 | pending | layout_repairs_applied.json:401 140-3:438; layout_repairs_applied.json:402 140-3:438; layout_repairs_applied.json:403 140-3:438; layout_repairs_applied.json:404 140-3:438 | ;  |  |
| 976 | pending | layout_repairs_applied.json:401 140-3:438; layout_repairs_applied.json:402 140-3:438; layout_repairs_applied.json:403 140-3:438; layout_repairs_applied.json:404 140-3:438; layout_repairs_applied.json:405 140-3:439 | ;  |  |
| 977 | pending | layout_repairs_applied.json:388 140-3:440; layout_repairs_applied.json:392 140-3:441; layout_repairs_applied.json:405 140-3:439; layout_repairs_applied.json:406 140-3:440 | ;  |  |
| 978 | pending | layout_repairs_applied.json:392 140-3:441 | ;  |  |
| 979 | pending | layout_repairs_applied.json:392 140-3:441; layout_repairs_applied.json:395 140-3:443 | ;  |  |
| 980 | pending | layout_before_sites.json:201 140-3:444; layout_repairs_applied.json:395 140-3:443 | ;  |  |
| 981 | pending | layout_before_sites.json:201 140-3:444 | ;  |  |
| 983 | pending | layout_pass_sites.json:12 140-3:446; layout_repairs_applied.json:390 140-3:446 | ;  |  |
| 984 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:12 140-3:446; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:389 140-3:448; layout_repairs_applied.json:390 140-3:446 | ;  |  |
| 985 | pending | layout_before_sites.json:202 140-3:448; layout_pass_sites.json:85 140-3:448; layout_repairs_applied.json:389 140-3:448; layout_repairs_applied.json:393 140-3:449; layout_repairs_applied.json:394 140-3:449 | ;  |  |
| 986 | pending | layout_repairs_applied.json:393 140-3:449; layout_repairs_applied.json:394 140-3:449 | ;  |  |
| 987 | pending | layout_repairs_applied.json:393 140-3:449; layout_repairs_applied.json:394 140-3:449 | ;  |  |
| 988 | pending | evenly spaced sample | ;  |  |
| 990 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 991 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 992 | pending | layout_before_sites.json:203 140-3:453; layout_before_sites.json:204 140-3:453; layout_before_sites.json:205 140-3:453 | ;  |  |
| 996 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 997 | pending | layout_before_sites.json:206 140-3:458 | ;  |  |
| 1000 | pending | layout_repairs_applied.json:407 140-3:462; layout_repairs_applied.json:408 140-3:463; layout_repairs_applied.json:409 140-3:463; layout_repairs_applied.json:410 140-3:463 | ;  |  |
| 1001 | pending | layout_repairs_applied.json:408 140-3:463; layout_repairs_applied.json:409 140-3:463; layout_repairs_applied.json:410 140-3:463 | ;  |  |
| 1002 | pending | layout_repairs_applied.json:408 140-3:463; layout_repairs_applied.json:409 140-3:463; layout_repairs_applied.json:410 140-3:463 | ;  |  |
| 1003 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 1004 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 1005 | pending | layout_before_sites.json:207 140-3:465 | ;  |  |
| 1006 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 1007 | pending | layout_before_sites.json:208 140-3:468 | ;  |  |
| 1008 | pending | layout_before_sites.json:208 140-3:468; layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 1009 | pending | layout_before_sites.json:209 140-3:469; layout_before_sites.json:210 140-3:469 | ;  |  |
| 1018 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 1019 | pending | layout_before_sites.json:211 140-3:479 | ;  |  |
| 1020 | pending | layout_before_sites.json:211 140-3:479; layout_repairs_applied.json:411 140-3:480; layout_repairs_applied.json:412 140-3:480 | ;  |  |
| 1021 | pending | layout_repairs_applied.json:411 140-3:480; layout_repairs_applied.json:412 140-3:480 | ;  |  |
| 1024 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1025 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1026 | pending | layout_before_sites.json:212 140-3:484 | ;  |  |
| 1027 | pending | evenly spaced sample | ;  |  |
| 1029 | pending | layout_before_sites.json:213 140-3:491 | ;  |  |
| 1030 | pending | layout_before_sites.json:213 140-3:491; layout_before_sites.json:214 140-3:492 | ;  |  |
| 1031 | pending | layout_before_sites.json:214 140-3:492 | ;  |  |
| 1032 | pending | layout_repairs_applied.json:413 140-3:494 | ;  |  |
| 1033 | pending | layout_repairs_applied.json:413 140-3:494 | ;  |  |
| 1038 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 1039 | pending | layout_before_sites.json:215 140-3:499 | ;  |  |
| 1042 | pending | layout_repairs_applied.json:415 140-3:503 | ;  |  |
| 1043 | pending | layout_repairs_applied.json:415 140-3:503 | ;  |  |
| 1044 | pending | layout_repairs_applied.json:415 140-3:503 | ;  |  |
| 1047 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:416 140-3:506; layout_repairs_applied.json:417 140-3:506 | ;  |  |
| 1048 | pending | layout_before_sites.json:216 140-3:506; layout_repairs_applied.json:416 140-3:506; layout_repairs_applied.json:417 140-3:506 | ;  |  |
| 1050 | pending | layout_before_sites.json:217 140-3:509 | ;  |  |
| 1051 | pending | layout_before_sites.json:217 140-3:509 | ;  |  |
| 1052 | pending | layout_before_sites.json:217 140-3:509; layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1053 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1054 | pending | layout_before_sites.json:218 140-3:510; layout_before_sites.json:219 140-3:510 | ;  |  |
| 1058 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 1059 | pending | layout_before_sites.json:220 140-3:514 | ;  |  |
| 1062 | pending | layout_before_sites.json:221 140-3:517 | ;  |  |
| 1063 | pending | layout_before_sites.json:221 140-3:517; layout_before_sites.json:222 140-3:518 | ;  |  |
| 1064 | pending | layout_before_sites.json:222 140-3:518; layout_before_sites.json:223 140-3:519; layout_repairs_applied.json:418 140-3:519; layout_repairs_applied.json:423 140-3:519 | ;  |  |
| 1065 | pending | layout_before_sites.json:223 140-3:519; layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:418 140-3:519; layout_repairs_applied.json:422 140-3:520; layout_repairs_applied.json:423 140-3:519 | ;  |  |
| 1066 | pending | evenly spaced sample; layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:422 140-3:520 | ;  |  |
| 1067 | pending | layout_before_sites.json:224 140-3:520; layout_repairs_applied.json:422 140-3:520 | ;  |  |
| 1068 | pending | layout_before_sites.json:225 140-3:522 | ;  |  |
| 1069 | pending | layout_before_sites.json:225 140-3:522 | ;  |  |
| 1070 | pending | layout_before_sites.json:225 140-3:522; layout_repairs_applied.json:424 140-3:523 | ;  |  |
| 1071 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:424 140-3:523; layout_repairs_applied.json:425 140-3:524; layout_repairs_applied.json:426 140-3:524 | ;  |  |
| 1072 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:425 140-3:524; layout_repairs_applied.json:426 140-3:524 | ;  |  |
| 1073 | pending | layout_before_sites.json:226 140-3:524; layout_repairs_applied.json:419 140-3:525; layout_repairs_applied.json:425 140-3:524; layout_repairs_applied.json:426 140-3:524; layout_repairs_applied.json:427 140-3:525; layout_repairs_applied.json:428 140-3:525 | ;  |  |
| 1074 | pending | layout_repairs_applied.json:419 140-3:525; layout_repairs_applied.json:427 140-3:525; layout_repairs_applied.json:428 140-3:525 | ;  |  |
| 1078 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530 | ;  |  |
| 1079 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530 | ;  |  |
| 1080 | pending | layout_before_sites.json:227 140-3:530; layout_before_sites.json:228 140-3:530; layout_before_sites.json:229 140-3:531 | ;  |  |
| 1081 | pending | layout_before_sites.json:229 140-3:531; layout_before_sites.json:230 140-3:532 | ;  |  |
| 1082 | pending | layout_before_sites.json:230 140-3:532; layout_before_sites.json:231 140-3:533 | ;  |  |
| 1083 | pending | layout_before_sites.json:231 140-3:533; layout_before_sites.json:232 140-3:534 | ;  |  |
| 1084 | pending | layout_before_sites.json:232 140-3:534 | ;  |  |
| 1085 | pending | layout_before_sites.json:232 140-3:534; layout_before_sites.json:233 140-3:535 | ;  |  |
| 1086 | pending | layout_before_sites.json:233 140-3:535; layout_before_sites.json:234 140-3:536; layout_repairs_applied.json:429 140-3:536 | ;  |  |
| 1087 | pending | layout_before_sites.json:234 140-3:536; layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_repairs_applied.json:429 140-3:536 | ;  |  |
| 1088 | pending | layout_before_sites.json:235 140-3:537; layout_before_sites.json:236 140-3:537; layout_before_sites.json:237 140-3:537; layout_before_sites.json:238 140-3:538 | ;  |  |
| 1089 | pending | layout_before_sites.json:238 140-3:538; layout_before_sites.json:239 140-3:539 | ;  |  |
| 1090 | pending | layout_before_sites.json:239 140-3:539; layout_before_sites.json:240 140-3:540 | ;  |  |
| 1091 | pending | layout_before_sites.json:240 140-3:540; layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 1092 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541 | ;  |  |
| 1093 | pending | layout_before_sites.json:241 140-3:541; layout_before_sites.json:242 140-3:541; layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:430 140-3:542; layout_repairs_applied.json:434 140-3:542 | ;  |  |
| 1094 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_repairs_applied.json:430 140-3:542; layout_repairs_applied.json:434 140-3:542 | ;  |  |
| 1095 | pending | layout_before_sites.json:243 140-3:542; layout_before_sites.json:244 140-3:542; layout_before_sites.json:245 140-3:543; layout_repairs_applied.json:430 140-3:542; layout_repairs_applied.json:434 140-3:542; layout_repairs_applied.json:435 140-3:543; layout_repairs_applied.json:436 140-3:543; layout_repairs_applied.json:437 140-3:543 | ;  |  |
| 1096 | pending | layout_before_sites.json:245 140-3:543; layout_repairs_applied.json:435 140-3:543; layout_repairs_applied.json:436 140-3:543; layout_repairs_applied.json:437 140-3:543 | ;  |  |
| 1097 | pending | layout_before_sites.json:245 140-3:543; layout_before_sites.json:246 140-3:544; layout_repairs_applied.json:435 140-3:543; layout_repairs_applied.json:436 140-3:543; layout_repairs_applied.json:437 140-3:543; layout_repairs_applied.json:438 140-3:544; layout_repairs_applied.json:439 140-3:544 | ;  |  |
| 1098 | pending | layout_before_sites.json:246 140-3:544; layout_before_sites.json:247 140-3:545; layout_repairs_applied.json:431 140-3:545; layout_repairs_applied.json:432 140-3:545; layout_repairs_applied.json:438 140-3:544; layout_repairs_applied.json:439 140-3:544; layout_repairs_applied.json:440 140-3:545; layout_repairs_applied.json:441 140-3:545; layout_repairs_applied.json:442 140-3:545; layout_repairs_applied.json:443 140-3:545; layout_repairs_applied.json:444 140-3:545; layout_repairs_applied.json:445 140-3:545 | ;  |  |
| 1099 | pending | layout_before_sites.json:247 140-3:545; layout_repairs_applied.json:431 140-3:545; layout_repairs_applied.json:432 140-3:545; layout_repairs_applied.json:440 140-3:545; layout_repairs_applied.json:441 140-3:545; layout_repairs_applied.json:442 140-3:545; layout_repairs_applied.json:443 140-3:545; layout_repairs_applied.json:444 140-3:545; layout_repairs_applied.json:445 140-3:545 | ;  |  |
| 1100 | pending | layout_before_sites.json:247 140-3:545; layout_before_sites.json:248 140-3:546; layout_repairs_applied.json:431 140-3:545; layout_repairs_applied.json:432 140-3:545; layout_repairs_applied.json:433 140-3:546; layout_repairs_applied.json:440 140-3:545; layout_repairs_applied.json:441 140-3:545; layout_repairs_applied.json:442 140-3:545; layout_repairs_applied.json:443 140-3:545; layout_repairs_applied.json:444 140-3:545; layout_repairs_applied.json:445 140-3:545 | ;  |  |
| 1101 | pending | layout_before_sites.json:248 140-3:546; layout_before_sites.json:249 140-3:547; layout_repairs_applied.json:433 140-3:546 | ;  |  |
| 1102 | pending | layout_before_sites.json:249 140-3:547; layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:446 140-3:548 | ;  |  |
| 1103 | pending | layout_before_sites.json:250 140-3:548; layout_pass_sites.json:86 140-3:548; layout_repairs_applied.json:446 140-3:548 | ;  |  |
| 1106 | pending | evenly spaced sample | ;  |  |
| 1107 | pending | layout_before_sites.json:251 140-3:554; layout_repairs_applied.json:447 140-3:554 | ;  |  |
| 1108 | pending | layout_before_sites.json:251 140-3:554; layout_repairs_applied.json:447 140-3:554 | ;  |  |
| 1109 | pending | layout_before_sites.json:251 140-3:554; layout_before_sites.json:252 140-3:555; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:447 140-3:554; layout_repairs_applied.json:448 140-3:555 | ;  |  |
| 1110 | pending | layout_before_sites.json:252 140-3:555; layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_pass_sites.json:13 140-3:555; layout_pass_sites.json:74 140-3:555; layout_repairs_applied.json:448 140-3:555; layout_repairs_applied.json:449 140-3:556 | ;  |  |
| 1111 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_repairs_applied.json:449 140-3:556 | ;  |  |
| 1112 | pending | layout_before_sites.json:253 140-3:556; layout_before_sites.json:254 140-3:556; layout_before_sites.json:255 140-3:557; layout_pass_sites.json:14 140-3:557; layout_pass_sites.json:75 140-3:557; layout_repairs_applied.json:449 140-3:556; layout_repairs_applied.json:451 140-3:557 | ;  |  |
| 1113 | pending | layout_before_sites.json:255 140-3:557; layout_before_sites.json:256 140-3:558; layout_pass_sites.json:14 140-3:557; layout_pass_sites.json:75 140-3:557; layout_repairs_applied.json:451 140-3:557 | ;  |  |
| 1114 | pending | layout_before_sites.json:256 140-3:558; layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1115 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1116 | pending | layout_before_sites.json:257 140-3:559; layout_before_sites.json:258 140-3:559 | ;  |  |
| 1117 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:452 140-3:561 | ;  |  |
| 1118 | pending | landscape page; layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:452 140-3:561 | ;  |  |
| 1119 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:452 140-3:561 | ;  |  |
| 1120 | pending | layout_before_sites.json:259 140-3:561; layout_pass_sites.json:48 140-3:561; layout_pass_sites.json:87 140-3:561; layout_repairs_applied.json:450 140-3:562; layout_repairs_applied.json:452 140-3:561; layout_repairs_applied.json:455 140-3:562; layout_repairs_applied.json:456 140-3:562 | ;  |  |
| 1121 | pending | layout_repairs_applied.json:450 140-3:562; layout_repairs_applied.json:455 140-3:562; layout_repairs_applied.json:456 140-3:562 | ;  |  |
| 1123 | pending | layout_repairs_applied.json:457 140-3:565 | ;  |  |
| 1124 | pending | layout_repairs_applied.json:457 140-3:565 | ;  |  |
| 1125 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567 | ;  |  |
| 1126 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567 | ;  |  |
| 1127 | pending | layout_before_sites.json:260 140-3:567; layout_before_sites.json:261 140-3:567; layout_repairs_applied.json:458 140-3:568 | ;  |  |
| 1128 | pending | layout_repairs_applied.json:458 140-3:568 | ;  |  |
| 1130 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 1131 | pending | layout_before_sites.json:262 140-3:570 | ;  |  |
| 1133 | pending | layout_before_sites.json:263 140-3:573; layout_repairs_applied.json:459 140-3:573 | ;  |  |
| 1134 | pending | layout_before_sites.json:263 140-3:573; layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:459 140-3:573; layout_repairs_applied.json:460 140-3:574 | ;  |  |
| 1135 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:460 140-3:574 | ;  |  |
| 1136 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:460 140-3:574 | ;  |  |
| 1137 | pending | layout_before_sites.json:264 140-3:574; layout_repairs_applied.json:460 140-3:574; layout_repairs_applied.json:462 140-3:575 | ;  |  |
| 1138 | pending | layout_before_sites.json:265 140-3:577; layout_repairs_applied.json:462 140-3:575 | ;  |  |
| 1139 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 1140 | pending | layout_before_sites.json:265 140-3:577 | ;  |  |
| 1145 | pending | evenly spaced sample; layout_before_sites.json:266 140-3:582 | ;  |  |
| 1146 | pending | layout_before_sites.json:266 140-3:582 | ;  |  |
| 1148 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 1149 | pending | layout_before_sites.json:267 140-3:585 | ;  |  |
| 1150 | pending | layout_before_sites.json:267 140-3:585; layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 1151 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586 | ;  |  |
| 1152 | pending | layout_before_sites.json:268 140-3:586; layout_before_sites.json:269 140-3:586; layout_before_sites.json:270 140-3:587 | ;  |  |
| 1153 | pending | layout_before_sites.json:270 140-3:587 | ;  |  |
| 1154 | pending | layout_before_sites.json:270 140-3:587; layout_before_sites.json:271 140-3:588 | ;  |  |
| 1155 | pending | layout_before_sites.json:271 140-3:588 | ;  |  |
| 1156 | pending | layout_before_sites.json:271 140-3:588; layout_before_sites.json:272 140-3:589 | ;  |  |
| 1157 | pending | layout_before_sites.json:272 140-3:589; layout_repairs_applied.json:464 140-3:590 | ;  |  |
| 1158 | pending | layout_repairs_applied.json:464 140-3:590 | ;  |  |
| 1160 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 1161 | pending | layout_before_sites.json:273 140-3:593 | ;  |  |
| 1168 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 1169 | pending | layout_before_sites.json:274 140-3:600 | ;  |  |
| 1176 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:465 140-3:606 | ;  |  |
| 1177 | pending | layout_pass_sites.json:15 140-3:606; layout_pass_sites.json:76 140-3:606; layout_repairs_applied.json:465 140-3:606 | ;  |  |
| 1180 | pending | layout_pass_sites.json:16 140-3:609; layout_repairs_applied.json:467 140-3:609 | ;  |  |
| 1185 | pending | evenly spaced sample | ;  |  |
| 1186 | pending | layout_before_sites.json:275 140-3:616 | ;  |  |
| 1187 | pending | layout_before_sites.json:275 140-3:616; layout_before_sites.json:276 140-3:617 | ;  |  |
| 1188 | pending | layout_before_sites.json:276 140-3:617 | ;  |  |
| 1189 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:468 140-3:619 | ;  |  |
| 1190 | pending | layout_before_sites.json:277 140-3:619; layout_pass_sites.json:17 140-3:619; layout_pass_sites.json:77 140-3:619; layout_repairs_applied.json:468 140-3:619 | ;  |  |
| 1192 | pending | layout_before_sites.json:278 140-3:621; layout_pass_sites.json:18 140-3:621; layout_repairs_applied.json:466 140-3:621; layout_repairs_applied.json:473 140-3:621; layout_repairs_applied.json:474 140-3:622; layout_repairs_applied.json:475 140-3:622; layout_repairs_applied.json:476 140-3:622; layout_repairs_applied.json:477 140-3:622; layout_repairs_applied.json:478 140-3:622 | ;  |  |
| 1193 | pending | layout_repairs_applied.json:474 140-3:622; layout_repairs_applied.json:475 140-3:622; layout_repairs_applied.json:476 140-3:622; layout_repairs_applied.json:477 140-3:622; layout_repairs_applied.json:478 140-3:622 | ;  |  |
| 1194 | pending | layout_repairs_applied.json:474 140-3:622; layout_repairs_applied.json:475 140-3:622; layout_repairs_applied.json:476 140-3:622; layout_repairs_applied.json:477 140-3:622; layout_repairs_applied.json:478 140-3:622; layout_repairs_applied.json:479 140-3:623; layout_repairs_applied.json:480 140-3:623 | ;  |  |
| 1195 | pending | layout_repairs_applied.json:479 140-3:623; layout_repairs_applied.json:480 140-3:623 | ;  |  |
| 1197 | pending | layout_before_sites.json:279 140-3:625 | ;  |  |
| 1198 | pending | layout_before_sites.json:280 140-3:627 | ;  |  |
| 1199 | pending | layout_before_sites.json:280 140-3:627; layout_repairs_applied.json:481 140-3:628 | ;  |  |
| 1200 | pending | layout_before_sites.json:281 140-3:629; layout_repairs_applied.json:481 140-3:628 | ;  |  |
| 1201 | pending | layout_before_sites.json:281 140-3:629 | ;  |  |
| 1202 | pending | layout_before_sites.json:281 140-3:629 | ;  |  |
| 1203 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 1204 | pending | layout_before_sites.json:282 140-3:631 | ;  |  |
| 1208 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:483 140-3:637; layout_repairs_applied.json:485 140-3:637 | ;  |  |
| 1209 | pending | layout_before_sites.json:283 140-3:637; layout_pass_sites.json:19 140-3:637; layout_pass_sites.json:78 140-3:637; layout_repairs_applied.json:482 140-3:638; layout_repairs_applied.json:483 140-3:637; layout_repairs_applied.json:485 140-3:637 | ;  |  |
| 1210 | pending | layout_repairs_applied.json:482 140-3:638 | ;  |  |
| 1220 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:496 140-3:649 | ;  |  |
| 1221 | pending | layout_before_sites.json:284 140-3:649; layout_repairs_applied.json:496 140-3:649 | ;  |  |
| 1224 | pending | evenly spaced sample; layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:486 140-3:653; layout_repairs_applied.json:497 140-3:653 | ;  |  |
| 1225 | pending | layout_before_sites.json:285 140-3:653; layout_pass_sites.json:20 140-3:653; layout_repairs_applied.json:486 140-3:653; layout_repairs_applied.json:497 140-3:653 | ;  |  |
| 1228 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:498 140-3:656; layout_repairs_applied.json:499 140-3:656 | ;  |  |
| 1229 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:498 140-3:656; layout_repairs_applied.json:499 140-3:656 | ;  |  |
| 1230 | pending | layout_before_sites.json:286 140-3:656; layout_before_sites.json:287 140-3:656; layout_before_sites.json:288 140-3:656; layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_pass_sites.json:49 140-3:656; layout_pass_sites.json:88 140-3:656; layout_repairs_applied.json:498 140-3:656; layout_repairs_applied.json:499 140-3:656 | ;  |  |
| 1231 | pending | layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657 | ;  |  |
| 1232 | pending | layout_before_sites.json:289 140-3:657; layout_before_sites.json:290 140-3:657; layout_before_sites.json:291 140-3:657; layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_repairs_applied.json:487 140-3:658; layout_repairs_applied.json:488 140-3:658 | ;  |  |
| 1233 | pending | layout_before_sites.json:292 140-3:658; layout_before_sites.json:293 140-3:658; layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:21 140-3:658; layout_pass_sites.json:22 140-3:658; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:79 140-3:658; layout_pass_sites.json:80 140-3:658; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:487 140-3:658; layout_repairs_applied.json:488 140-3:658; layout_repairs_applied.json:489 140-3:659; layout_repairs_applied.json:490 140-3:659 | ;  |  |
| 1234 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:489 140-3:659; layout_repairs_applied.json:490 140-3:659 | ;  |  |
| 1235 | pending | layout_before_sites.json:294 140-3:659; layout_before_sites.json:295 140-3:659; layout_pass_sites.json:23 140-3:659; layout_pass_sites.json:81 140-3:659; layout_repairs_applied.json:489 140-3:659; layout_repairs_applied.json:490 140-3:659; layout_repairs_applied.json:491 140-3:660 | ;  |  |
| 1236 | pending | layout_repairs_applied.json:491 140-3:660 | ;  |  |
| 1238 | pending | layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:492 140-3:662 | ;  |  |
| 1239 | pending | layout_before_sites.json:296 140-3:662; layout_pass_sites.json:24 140-3:662; layout_pass_sites.json:82 140-3:662; layout_repairs_applied.json:492 140-3:662 | ;  |  |
| 1244 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 1245 | pending | layout_before_sites.json:297 140-3:668 | ;  |  |
| 1255 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 1256 | pending | layout_before_sites.json:298 140-3:679 | ;  |  |
| 1259 | pending | layout_repairs_applied.json:502 140-3:685; layout_repairs_applied.json:503 140-3:685 | ;  |  |
| 1260 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:502 140-3:685; layout_repairs_applied.json:503 140-3:685; layout_repairs_applied.json:504 140-3:686 | ;  |  |
| 1261 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:504 140-3:686 | ;  |  |
| 1262 | pending | layout_before_sites.json:299 140-3:686; layout_before_sites.json:300 140-3:686; layout_repairs_applied.json:504 140-3:686 | ;  |  |
| 1263 | pending | layout_repairs_applied.json:505 140-3:688; layout_repairs_applied.json:506 140-3:688 | ;  |  |
| 1264 | pending | evenly spaced sample; layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:505 140-3:688; layout_repairs_applied.json:506 140-3:688; layout_repairs_applied.json:507 140-3:689 | ;  |  |
| 1265 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:507 140-3:689 | ;  |  |
| 1266 | pending | layout_before_sites.json:301 140-3:689; layout_repairs_applied.json:507 140-3:689 | ;  |  |
| 1269 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692 | ;  |  |
| 1270 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692 | ;  |  |
| 1271 | pending | layout_before_sites.json:302 140-3:692; layout_before_sites.json:303 140-3:692; layout_repairs_applied.json:508 140-3:693; layout_repairs_applied.json:509 140-3:693 | ;  |  |
| 1275 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 1276 | pending | layout_before_sites.json:304 140-4:4 | ;  |  |
| 1279 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1280 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1281 | pending | layout_before_sites.json:305 140-4:10; layout_before_sites.json:306 140-4:10 | ;  |  |
| 1282 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1283 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1284 | pending | layout_before_sites.json:307 140-4:13; layout_before_sites.json:308 140-4:13; layout_before_sites.json:309 140-4:13 | ;  |  |
| 1290 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:510 140-4:20 | ;  |  |
| 1291 | pending | layout_before_sites.json:310 140-4:20; layout_pass_sites.json:50 140-4:20; layout_pass_sites.json:93 140-4:20; layout_repairs_applied.json:510 140-4:20 | ;  |  |
| 1297 | pending | layout_before_sites.json:311 140-4:29 | ;  |  |
| 1298 | pending | layout_before_sites.json:311 140-4:29; layout_repairs_applied.json:512 140-4:31; layout_repairs_applied.json:513 140-4:31; layout_repairs_applied.json:514 140-4:31 | ;  |  |
| 1299 | pending | layout_repairs_applied.json:512 140-4:31; layout_repairs_applied.json:513 140-4:31; layout_repairs_applied.json:514 140-4:31; layout_repairs_applied.json:515 140-4:32; layout_repairs_applied.json:516 140-4:32 | ;  |  |
| 1300 | pending | layout_repairs_applied.json:515 140-4:32; layout_repairs_applied.json:516 140-4:32; layout_repairs_applied.json:517 140-4:33 | ;  |  |
| 1301 | pending | layout_repairs_applied.json:517 140-4:33 | ;  |  |
| 1302 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:517 140-4:33 | ;  |  |
| 1303 | pending | evenly spaced sample; layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34 | ;  |  |
| 1304 | pending | layout_before_sites.json:312 140-4:34; layout_before_sites.json:313 140-4:34; layout_repairs_applied.json:518 140-4:35; layout_repairs_applied.json:519 140-4:35 | ;  |  |
| 1305 | pending | layout_repairs_applied.json:518 140-4:35; layout_repairs_applied.json:519 140-4:35 | ;  |  |
| 1309 | pending | layout_before_sites.json:314 140-4:39 | ;  |  |
| 1310 | pending | layout_before_sites.json:314 140-4:39; layout_before_sites.json:315 140-4:40 | ;  |  |
| 1311 | pending | layout_before_sites.json:315 140-4:40; layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41 | ;  |  |
| 1312 | pending | layout_before_sites.json:316 140-4:41; layout_before_sites.json:317 140-4:41; layout_before_sites.json:318 140-4:42 | ;  |  |
| 1313 | pending | layout_before_sites.json:318 140-4:42; layout_before_sites.json:319 140-4:43 | ;  |  |
| 1314 | pending | layout_before_sites.json:319 140-4:43; layout_before_sites.json:320 140-4:44; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:520 140-4:44 | ;  |  |
| 1315 | pending | layout_before_sites.json:320 140-4:44; layout_before_sites.json:321 140-4:45; layout_pass_sites.json:25 140-4:44; layout_pass_sites.json:89 140-4:44; layout_repairs_applied.json:520 140-4:44 | ;  |  |
| 1316 | pending | layout_before_sites.json:321 140-4:45; layout_before_sites.json:322 140-4:46 | ;  |  |
| 1317 | pending | layout_before_sites.json:322 140-4:46; layout_before_sites.json:323 140-4:47 | ;  |  |
| 1318 | pending | layout_before_sites.json:323 140-4:47 | ;  |  |
| 1319 | pending | layout_before_sites.json:323 140-4:47; layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48 | ;  |  |
| 1320 | pending | layout_before_sites.json:324 140-4:48; layout_before_sites.json:325 140-4:48; layout_before_sites.json:326 140-4:48; layout_before_sites.json:327 140-4:49 | ;  |  |
| 1321 | pending | layout_before_sites.json:327 140-4:49; layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 1322 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50 | ;  |  |
| 1323 | pending | layout_before_sites.json:328 140-4:50; layout_before_sites.json:329 140-4:50; layout_before_sites.json:330 140-4:50; layout_before_sites.json:331 140-4:51 | ;  |  |
| 1324 | pending | layout_before_sites.json:331 140-4:51; layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52 | ;  |  |
| 1325 | pending | layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52 | ;  |  |
| 1326 | pending | layout_before_sites.json:332 140-4:52; layout_before_sites.json:333 140-4:52; layout_before_sites.json:334 140-4:53; layout_before_sites.json:335 140-4:54 | ;  |  |
| 1327 | pending | layout_before_sites.json:335 140-4:54; layout_before_sites.json:336 140-4:55 | ;  |  |
| 1328 | pending | layout_before_sites.json:336 140-4:55; layout_before_sites.json:337 140-4:56 | ;  |  |
| 1329 | pending | layout_before_sites.json:337 140-4:56 | ;  |  |
| 1330 | pending | layout_before_sites.json:337 140-4:56; layout_before_sites.json:338 140-4:57 | ;  |  |
| 1331 | pending | layout_before_sites.json:338 140-4:57 | ;  |  |
| 1332 | pending | layout_before_sites.json:338 140-4:57; layout_repairs_applied.json:533 140-4:59 | ;  |  |
| 1333 | pending | layout_repairs_applied.json:533 140-4:59 | ;  |  |
| 1334 | pending | layout_repairs_applied.json:534 140-4:61; layout_repairs_applied.json:535 140-4:61; layout_repairs_applied.json:536 140-4:61; layout_repairs_applied.json:537 140-4:61 | ;  |  |
| 1335 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:534 140-4:61; layout_repairs_applied.json:535 140-4:61; layout_repairs_applied.json:536 140-4:61; layout_repairs_applied.json:537 140-4:61; layout_repairs_applied.json:538 140-4:62 | ;  |  |
| 1336 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:538 140-4:62 | ;  |  |
| 1337 | pending | layout_before_sites.json:339 140-4:62; layout_repairs_applied.json:538 140-4:62 | ;  |  |
| 1339 | pending | layout_repairs_applied.json:531 140-4:65 | ;  |  |
| 1340 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:522 140-4:66; layout_repairs_applied.json:523 140-4:66; layout_repairs_applied.json:524 140-4:66; layout_repairs_applied.json:531 140-4:65 | ;  |  |
| 1341 | pending | layout_before_sites.json:340 140-4:66; layout_before_sites.json:341 140-4:66; layout_before_sites.json:342 140-4:66; layout_before_sites.json:343 140-4:67; layout_pass_sites.json:26 140-4:66; layout_pass_sites.json:90 140-4:66; layout_repairs_applied.json:522 140-4:66; layout_repairs_applied.json:523 140-4:66; layout_repairs_applied.json:524 140-4:66 | ;  |  |
| 1342 | pending | layout_before_sites.json:343 140-4:67 | ;  |  |
| 1343 | pending | evenly spaced sample | ;  |  |
| 1344 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 1345 | pending | layout_before_sites.json:344 140-4:70 | ;  |  |
| 1350 | pending | layout_repairs_applied.json:539 140-4:74 | ;  |  |
| 1351 | pending | layout_repairs_applied.json:532 140-4:75; layout_repairs_applied.json:539 140-4:74; layout_repairs_applied.json:540 140-4:75; layout_repairs_applied.json:541 140-4:75; layout_repairs_applied.json:542 140-4:75 | ;  |  |
| 1352 | pending | layout_repairs_applied.json:532 140-4:75; layout_repairs_applied.json:540 140-4:75; layout_repairs_applied.json:541 140-4:75; layout_repairs_applied.json:542 140-4:75 | ;  |  |
| 1353 | pending | layout_repairs_applied.json:532 140-4:75; layout_repairs_applied.json:540 140-4:75; layout_repairs_applied.json:541 140-4:75; layout_repairs_applied.json:542 140-4:75; layout_repairs_applied.json:543 140-4:76; layout_repairs_applied.json:544 140-4:76 | ;  |  |
| 1354 | pending | layout_repairs_applied.json:543 140-4:76; layout_repairs_applied.json:544 140-4:76 | ;  |  |
| 1355 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:543 140-4:76; layout_repairs_applied.json:544 140-4:76; layout_repairs_applied.json:547 140-4:77 | ;  |  |
| 1356 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:547 140-4:77 | ;  |  |
| 1357 | pending | layout_before_sites.json:345 140-4:77; layout_repairs_applied.json:547 140-4:77; layout_repairs_applied.json:548 140-4:78; layout_repairs_applied.json:549 140-4:78 | ;  |  |
| 1358 | pending | layout_repairs_applied.json:548 140-4:78; layout_repairs_applied.json:549 140-4:78; layout_repairs_applied.json:550 140-4:79; layout_repairs_applied.json:551 140-4:79 | ;  |  |
| 1359 | pending | layout_repairs_applied.json:550 140-4:79; layout_repairs_applied.json:551 140-4:79; layout_repairs_applied.json:552 140-4:80 | ;  |  |
| 1360 | pending | layout_repairs_applied.json:552 140-4:80; layout_repairs_applied.json:553 140-4:81; layout_repairs_applied.json:554 140-4:81 | ;  |  |
| 1361 | pending | layout_repairs_applied.json:553 140-4:81; layout_repairs_applied.json:554 140-4:81 | ;  |  |
| 1362 | pending | layout_repairs_applied.json:553 140-4:81; layout_repairs_applied.json:554 140-4:81 | ;  |  |
| 1373 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1374 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1375 | pending | layout_before_sites.json:346 140-4:91; layout_before_sites.json:347 140-4:91; layout_before_sites.json:348 140-4:91 | ;  |  |
| 1380 | pending | layout_repairs_applied.json:558 140-4:96; layout_repairs_applied.json:559 140-4:96 | ;  |  |
| 1381 | pending | layout_repairs_applied.json:558 140-4:96; layout_repairs_applied.json:559 140-4:96; layout_repairs_applied.json:560 140-4:97; layout_repairs_applied.json:561 140-4:97 | ;  |  |
| 1382 | pending | evenly spaced sample; layout_repairs_applied.json:560 140-4:97; layout_repairs_applied.json:561 140-4:97; layout_repairs_applied.json:562 140-4:98 | ;  |  |
| 1383 | pending | layout_repairs_applied.json:562 140-4:98 | ;  |  |
| 1384 | pending | layout_before_sites.json:349 140-4:99; layout_repairs_applied.json:562 140-4:98 | ;  |  |
| 1385 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1386 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1387 | pending | layout_before_sites.json:349 140-4:99 | ;  |  |
| 1388 | pending | layout_before_sites.json:350 140-4:101 | ;  |  |
| 1389 | pending | layout_before_sites.json:350 140-4:101; layout_before_sites.json:351 140-4:102 | ;  |  |
| 1390 | pending | layout_before_sites.json:351 140-4:102 | ;  |  |
| 1392 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 1393 | pending | layout_before_sites.json:352 140-4:105 | ;  |  |
| 1398 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:555 140-4:113 | ;  |  |
| 1399 | pending | layout_pass_sites.json:91 140-4:113; layout_repairs_applied.json:555 140-4:113 | ;  |  |
| 1422 | pending | evenly spaced sample | ;  |  |
| 1424 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:563 140-4:136 | ;  |  |
| 1425 | pending | layout_before_sites.json:353 140-4:136; layout_repairs_applied.json:563 140-4:136 | ;  |  |
| 1432 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 1433 | pending | layout_before_sites.json:354 140-4:147; layout_before_sites.json:355 140-4:147 | ;  |  |
| 1434 | pending | layout_before_sites.json:356 140-4:149 | ;  |  |
| 1435 | pending | layout_before_sites.json:356 140-4:149 | ;  |  |
| 1439 | pending | layout_before_sites.json:357 140-4:154 | ;  |  |
| 1440 | pending | layout_before_sites.json:357 140-4:154 | ;  |  |
| 1453 | pending | layout_repairs_applied.json:565 140-4:172 | ;  |  |
| 1454 | pending | layout_repairs_applied.json:565 140-4:172; layout_repairs_applied.json:566 140-4:174 | ;  |  |
| 1455 | pending | layout_repairs_applied.json:566 140-4:174; layout_repairs_applied.json:567 140-4:175; layout_repairs_applied.json:568 140-4:175 | ;  |  |
| 1456 | pending | layout_repairs_applied.json:567 140-4:175; layout_repairs_applied.json:568 140-4:175 | ;  |  |
| 1460 | pending | layout_before_sites.json:358 140-4:181; layout_before_sites.json:359 140-4:181 | ;  |  |
| 1461 | pending | evenly spaced sample | ;  |  |
| 1463 | pending | layout_before_sites.json:360 140-4:186 | ;  |  |
| 1464 | pending | layout_before_sites.json:360 140-4:186; layout_before_sites.json:361 140-4:188 | ;  |  |
| 1465 | pending | layout_before_sites.json:361 140-4:188 | ;  |  |
| 1474 | pending | layout_repairs_applied.json:569 140-4:203; layout_repairs_applied.json:570 140-4:203 | ;  |  |
| 1475 | pending | layout_repairs_applied.json:571 140-4:205 | ;  |  |
| 1476 | pending | layout_repairs_applied.json:571 140-4:205 | ;  |  |
| 1497 | pending | layout_before_sites.json:362 140-4:230 | ;  |  |
| 1501 | pending | evenly spaced sample | ;  |  |
| 1502 | pending | layout_before_sites.json:363 140-4:236 | ;  |  |
| 1503 | pending | layout_before_sites.json:363 140-4:236 | ;  |  |
| 1509 | pending | layout_before_sites.json:364 140-4:245 | ;  |  |
| 1510 | pending | layout_before_sites.json:364 140-4:245 | ;  |  |
| 1513 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 1514 | pending | layout_before_sites.json:365 140-4:250 | ;  |  |
| 1526 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 1527 | pending | layout_before_sites.json:366 140-4:264 | ;  |  |
| 1528 | pending | layout_before_sites.json:367 140-4:266 | ;  |  |
| 1529 | pending | layout_before_sites.json:367 140-4:266 | ;  |  |
| 1530 | pending | layout_before_sites.json:367 140-4:266; layout_before_sites.json:368 140-4:267; layout_before_sites.json:369 140-4:268 | ;  |  |
| 1531 | pending | layout_before_sites.json:369 140-4:268; layout_before_sites.json:370 140-4:269 | ;  |  |
| 1532 | pending | layout_before_sites.json:370 140-4:269; layout_before_sites.json:371 140-4:270 | ;  |  |
| 1533 | pending | layout_before_sites.json:371 140-4:270; layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:575 140-4:271; layout_repairs_applied.json:577 140-4:271 | ;  |  |
| 1534 | pending | layout_before_sites.json:372 140-4:271; layout_before_sites.json:373 140-4:271; layout_before_sites.json:374 140-4:272; layout_pass_sites.json:27 140-4:271; layout_pass_sites.json:92 140-4:271; layout_repairs_applied.json:575 140-4:271; layout_repairs_applied.json:577 140-4:271 | ;  |  |
| 1535 | pending | layout_before_sites.json:374 140-4:272; layout_before_sites.json:375 140-4:273; layout_before_sites.json:376 140-4:274 | ;  |  |
| 1536 | pending | layout_before_sites.json:376 140-4:274; layout_before_sites.json:377 140-4:275 | ;  |  |
| 1537 | pending | layout_before_sites.json:377 140-4:275; layout_before_sites.json:378 140-4:276; layout_repairs_applied.json:576 140-4:276 | ;  |  |
| 1538 | pending | layout_before_sites.json:378 140-4:276; layout_before_sites.json:379 140-4:277; layout_repairs_applied.json:576 140-4:276 | ;  |  |
| 1539 | pending | layout_before_sites.json:379 140-4:277; layout_before_sites.json:380 140-4:278; layout_before_sites.json:381 140-4:279 | ;  |  |
| 1540 | pending | evenly spaced sample; layout_before_sites.json:381 140-4:279; layout_before_sites.json:382 140-4:280 | ;  |  |

## 6. Reproducibility, privacy and checkpoint retention

Each delivered TeX book is self-contained and compiles twice with LuaLaTeX on a full standard TeX Live installation, with shell escape disabled. The embedded Lua writes only relative audit sidecars. Rebuilding the edition from the original three supplied ZIPs uses the `sources/` and `work/` project structure and scripts described in `README.md`. Original manuscript source packages were not edited.

Complete final verification JSON, all-page bound tables, PDF link tables, source-projection outputs, exact layout manifests, full warning tables and sanitized logs are retained. Contact/overview sheets can be regenerated from the selected-page PNGs and the stored PDF. Identical master images may be represented once with a digest-backed alias inventory; the manifest states every such alias.

Curated repair evidence is retained under both `proofs/visual_repairs/` and `work/visual_repair_proofs/`. These byte-identical copies preserve the earlier archive references and the project-relative paths used by the saved audit scripts; neither set of those paths requires reconstruction.

The final archives contain exactly the seven publication PDFs. Development probe PDFs remain in the immutable checkpoints; their exact source/log records, accepted PNG proof images and hashes are retained. They are excluded because an isolated development proof is superseded by the complete final reader, even when its numerical checks pass. `development_pdf_exclusions.json` identifies each probe and its final replacement; `VISUAL_REPAIRS.tsv` distinguishes historical probe provenance from final-reader evidence.

Checkpoint ZIPs are never overwritten, renamed or deleted. `CHECKPOINT_RETENTION.tsv` lists every checkpoint entry, its original hash, its final archive/path and whether it is preserved byte for byte, superseded by a final version, or explicitly omitted with a reason. This inventory is the authoritative record for every development artifact not copied into the final ZIPs.

All delivered text and PDF text/metadata are checked for local filesystem paths and email addresses. An additional hash-bound audit covers PDF object dictionaries, decoded strings, annotation/action targets and embedded-file absence; `pdf_privacy_audit.json` records its complete inventory and scope. Binary font/image streams are not interpreted. Sanitized logs use an explicit omission marker for machine paths. Relative paths inside the reproducibility project and public archive URLs remain intact. Credit and rights text follows the supplied published record; see `CREDITS_AUDIT.md`.

## Unfinished conditions

- LM_FR_diplomatique: visual_review_complete
- LM_FR_corrige_apparat: visual_review_complete
- LM_FR_texte_de_lecture: visual_review_complete
- LM_EN_corrected_apparatus: visual_review_complete
- LM_EN_reading: visual_review_complete
- LM_FR_master_annotated: visual_review_complete
- LM_EN_master_annotated: visual_review_complete
- Final source-qualified pagination audit is missing
- Final native-image issue closure is not PASS
- Unresolved native-image finding: VIS-140-3-441-117
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-441-117
- Unresolved native-image finding: VIS-140-3-449-137-138
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-449-137-138
- Unresolved native-image finding: VIS-140-2-252-OPTIONS
- Native-image finding lacks all affected final-book confirmations: VIS-140-2-252-OPTIONS
- Unresolved native-image finding: VIS-140-3-443-121
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-443-121
- Unresolved native-image finding: VIS-140-3-520-81
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-520-81
- Unresolved native-image finding: VIS-140-3-637-BLUE-NOTE
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-637-BLUE-NOTE
- Unresolved native-image finding: VIS-140-2-089-SECTION12
- Native-image finding lacks all affected final-book confirmations: VIS-140-2-089-SECTION12
- Unresolved native-image finding: VIS-140-3-186-SECTIONII
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-186-SECTIONII
- Unresolved native-image finding: VIS-140-3-506-20bis
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-506-20bis
- Unresolved native-image finding: VIS-140-3-055-3
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-055-3
- Unresolved native-image finding: VIS-140-3-622-HEADING-b
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-622-HEADING-b
- Unresolved native-image finding: VIS-140-3-221-REMARQUE
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-221-REMARQUE
- Unresolved native-image finding: VIS-140-1-025-HEADING-B
- Native-image finding lacks all affected final-book confirmations: VIS-140-1-025-HEADING-B
- Unresolved native-image finding: VIS-GENERATED-RETAINEDDOUBT-HEADING
- Native-image finding lacks all affected final-book confirmations: VIS-GENERATED-RETAINEDDOUBT-HEADING
- Unresolved native-image finding: VIS-GENERATED-APPARATUS-HEADING
- Native-image finding lacks all affected final-book confirmations: VIS-GENERATED-APPARATUS-HEADING
- Unresolved native-image finding: VIS-140-3-408-44
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-408-44
- Unresolved native-image finding: VIS-140-3-649-59
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-649-59
- Unresolved native-image finding: VIS-140-3-656-REMARKS
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-656-REMARKS
- Unresolved native-image finding: VIS-140-3-590-60
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-590-60
- Unresolved native-image finding: VIS-140-4-115-RANGEHEADING
- Native-image finding lacks all affected final-book confirmations: VIS-140-4-115-RANGEHEADING
- Unresolved native-image finding: VIS-140-4-267-RANGEHEADING
- Native-image finding lacks all affected final-book confirmations: VIS-140-4-267-RANGEHEADING
- Unresolved native-image finding: VIS-140-3-565-HEADING-6
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-565-HEADING-6
- Unresolved native-image finding: VIS-140-3-419-CIRCLED3
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-419-CIRCLED3
- Unresolved native-image finding: VIS-140-3-245-CANCELLEDTAG
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-245-CANCELLEDTAG
- Unresolved native-image finding: VIS-140-3-261-CANCELLEDTAG
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-261-CANCELLEDTAG
- Unresolved native-image finding: VIS-140-3-363-CANCELLEDTAG
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-363-CANCELLEDTAG
- Unresolved native-image finding: VIS-140-3-6-SECTION38
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-6-SECTION38
- Unresolved native-image finding: VIS-140-3-575-PROPOSITION
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-575-PROPOSITION
- Unresolved native-image finding: VIS-140-4-77-HEADING-7
- Native-image finding lacks all affected final-book confirmations: VIS-140-4-77-HEADING-7
- Unresolved native-image finding: VIS-140-4-065-EPILABELS
- Native-image finding lacks all affected final-book confirmations: VIS-140-4-065-EPILABELS
- Unresolved native-image finding: VIS-140-3-653-HEADING-2
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-653-HEADING-2
- Unresolved native-image finding: VIS-140-4-32-THEOREM
- Native-image finding lacks all affected final-book confirmations: VIS-140-4-32-THEOREM
- Unresolved native-image finding: VIS-140-3-437-TAG108-INTRO
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-437-TAG108-INTRO
- Unresolved native-image finding: VIS-140-4-75-E144-MASK
- Native-image finding lacks all affected final-book confirmations: VIS-140-4-75-E144-MASK
- Unresolved native-image finding: VIS-140-3-519-TAG79-INTRO
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-519-TAG79-INTRO
- Unresolved native-image finding: VIS-140-3-495-SECTION49
- Native-image finding lacks all affected final-book confirmations: VIS-140-3-495-SECTION49
- Final all-page generated-heading audit is not PASS
- Generated-heading supporting evidence is stale: witness_inventory
- Generated-heading supporting evidence is stale: work/scripts/verify_generated_heading_final.py
- Generated-heading supporting evidence is stale: work/scripts/verify_pagination_final.py
- Generated-heading actual closure is incomplete: HEADING-LM_FR_diplomatique-p0799-scan_range
- Generated-heading actual closure is incomplete: HEADING-LM_FR_corrige_apparat-p1414-scan_range
- Generated-heading actual closure is incomplete: HEADING-LM_EN_corrected_apparatus-p1421-scan_range
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-3-s638-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-3-s650-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-4-s075-apparatus_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-4-s101-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-4-s113-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-4-s148-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-4-s251-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-4-s266-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-4-s275-apparatus_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-4-s115-scan_range
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_corrige_apparat-140-4-s267-scan_range
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-2-s036-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-2-s148-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-2-s166-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-2-s205-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-2-s207-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-2-s329-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-3-s022-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-3-s209-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-3-s214-retained_doubts_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-3-s321-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-3-s334-retained_doubts_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-3-s411-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-3-s419-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_FR_texte_de_lecture-140-3-s507-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_corrected_apparatus-140-3-s222-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_corrected_apparatus-140-3-s540-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_corrected_apparatus-140-3-s574-apparatus_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_corrected_apparatus-140-3-s587-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_corrected_apparatus-140-4-s075-apparatus_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_corrected_apparatus-140-4-s080-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_corrected_apparatus-140-4-s101-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_corrected_apparatus-140-4-s113-apparatus_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_corrected_apparatus-140-4-s174-apparatus
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-4-s042-retained_doubts_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-4-s077-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-4-s102-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-4-s177-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-2-s220-retained_doubts_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-2-s423-retained_doubts_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-2-s451-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-2-s457-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-2-s459-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-2-s517-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-3-s022-retained_doubts
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-3-s208-retained_doubts_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-3-s462-retained_doubts_rule_only
- Generated-heading actual closure is incomplete: GHKNOWN-LM_EN_reading-140-3-s503-retained_doubts
- Generated-heading master transfer is incomplete: HEADING-LM_FR_master_annotated-p1414-scan_range
- Generated-heading master transfer is incomplete: HEADING-LM_EN_master_annotated-p1421-scan_range
- Generated-heading audit completion counts do not agree
- Generated-heading known-witness closure coverage is incomplete

