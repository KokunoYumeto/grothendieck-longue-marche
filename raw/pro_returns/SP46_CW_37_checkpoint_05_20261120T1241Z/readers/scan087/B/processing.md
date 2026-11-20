# Scan 087, independent reader B: processing record

## Authorized inputs

Read `brief_v09.md`, `conventions.md`, `PREAMBLE.tex`, and the assigned scan087 packet (`meta.json`, `C.tex`, `H.tex`, `C_context.md`, `notation.json`). No other page or reader was consulted. H supplies description only and is unavailable for transcription collation.

## Source image views

1. `B37-04_37_scan087.jpg`, 1687 × 2149, whole page viewed once for layout.
2. `B37-04_37_scan087_a.jpg`, 1687 × 1154, viewed once and read line by line.
3. `B37-04_37_scan087_b.jpg`, 1687 × 1155, viewed once and read line by line. Whole-page y offset is 994; the overlap was not separately reopened.

Whole-page inventory: page number at top, continuation contents entries 3.8 and 3.9; headings and entries for sections 4–7; typed cancellations and two overprinted letters; pencilled archive 86 lower left. No diagram or inserted prose. No date or separate page title.

## Line-by-line half reading

Half a: top number; 3.8 (two lines), 3.9; section 4 heading; 4.1, 4.2, 4.3, 4.4 (two lines), 4.5 (two lines); section 5 heading; 5.1, 5.2, 5.3, 5.4, 5.5 (two lines), 5.6, 5.7. Read each word, accent, numeral, period, comma, hyphen and leader. Ordinary A and B in section 4 have no independent double-struck outlines. Visible comma spaces in 4.1 and lack of space after 4.5. retained.

Half b: overlap ending 5.5–5.7; section 6 heading without leaders; 6.1; 6.2 with M and lowered f, deleted word and following-line inductive; 6.3; 6.4; 6.5 corrected pair; 6.6; 6.7 extra cancelled glyph; 6.8; cancelled section start; live section 7 heading; 7.1, 7.2, 7.3, 7.4; cancelled start and live 7.5; 7.6; archive 86. Each entry checked against C. All source halves are settled apart from the listed loci below.

## Open loci listed after both halves, before crop inspection

- Top page number: typed versus handwritten construction; flanking hyphens visible.
- 5.7: small detached oblique trace above annelés, material/ink status.
- 6.2: terminal positions of cancelled project/projecti.
- 6.3: possible comma after finitude, rather than first leader dot.
- 6.5: two overlapping correction characters in fermeture.
- Right margin beside 6.5: tiny pair of diagonal dark points, shape and material status.
- 6.7: cancelled l/1 following sur.
- Above live § 7: cancelled section-start numeral and punctuation.
- Before live 7.5: cancelled 7 and possible following point.

## Crop processing

All crops come directly from the original whole-page JPEG. Exactly one retained crop per open locus, no recropping. The crop bboxes use original whole-page pixel coordinates. Each is resized once to width 2600 px with Pillow LANCZOS, RGB autocontrast (cutoff 0), then an UnsharpMask (radius 1.1, percent 115, threshold 3); no rotation. JPEG quality 95, subsampling 0. No OCR, recognition software, external text, research or TeX engine used.

## Actual retained-crop views and outcomes

All requested crop deliveries reached the reader; none was truncated. Each crop was viewed exactly once, in these three batches:

1. `B087_01_page_number.jpg`, `B087_02_anneles_trace.jpg`, `B087_03_project_cancelled.jpg`.
2. `B087_04_finitude_punctuation.jpg`, `B087_05_fermeture_correction.jpg`, `B087_06_margin_points.jpg`.
3. `B087_07_sur_cancelled.jpg`, `B087_08_section_stub.jpg`, `B087_09_entry_stub.jpg`.

Outcomes: retain the top flanking hyphens; the number itself reads 539 and is treated as typewritten. Preserve the detached hooked trace above annelés with uncertain origin. Retain project/projecti without completing a longer word. Mark comma/period after finitude. Confirm the C e/t overprinting sequence in fermeture. Preserve the right marginal point pair with uncertain origin. Retain cancelled l/1. Resolve the cancelled section-start numeral to 7 but retain uncertainty in its point; add an explicit no-point alternative. In the 7.5 stub, retain 7 and keep the following low trace uncertain, adding the possible obscured 3 and no-recoverable-character alternatives permitted by its crowded curved upper and lower contours.

No crop established a paper-coloured scratch channel that would justify removing either detached dark graphic. No further image view or crop was made after these decisions.

## Written outputs and static verification

`reading.tex` contains the whole page. `report.json` has 8 decision records, including all 4 explicit C doubts, 6 substantive C differences, and 42 inventory rows. H fields are null/false throughout. The unchanged 6.5 C-context target is recorded in math_reading_decisions. check_events is empty because no proof or mathematical computation was performed.

After writing: JSON parse and exact top-level schema keys passed; all decision bboxes are present; crop filenames are unique; all H collation fields obey the description-only rule; all four explicit C doubts are represented. TeX braces, begin/end environment nesting, and dollar parity passed. JSON LaTeX strings were checked for accidental doubled decoded command backslashes. No TeX engine was invoked.
