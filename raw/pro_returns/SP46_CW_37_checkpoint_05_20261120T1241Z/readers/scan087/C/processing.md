# Scan 087 — independent reader C processing record

## Scope and source delivery

Read in full: brief_v09.md, conventions.md, PREAMBLE.tex, and the assigned scan087 packet (meta.json, C.tex, H.tex, C_context.md, notation.json). H contains description only and is unavailable as a transcription.

Actual visual source views, in order, each exactly once:

1. B37-04_37_scan087.jpg, 1687 × 2149: complete-page layout.
2. B37-04_37_scan087_a.jpg, 1687 × 1154: complete line-by-line reading of the upper half.
3. B37-04_37_scan087_b.jpg, 1687 × 1155: complete line-by-line reading of the lower half.

The lower half begins at whole-image y = 994; the halves overlap by 160 pixels. No OCR, recognition software, external research, published text, other page, other reader, or TeX compilation was used.

## Completed half readings before cropping

The complete page is a typed contents continuation. Its printed page number has flanking hyphens, - 539 -. The archive number is handwritten 86 at lower left. The main text comprises entries 3.8–3.9, heading § 4 and entries 4.1–4.5, heading § 5 and entries 5.1–5.7, heading § 6 and entries 6.1–6.8, a cancelled section-start stub, live heading § 7 and entries 7.1–7.6, including a cancelled stub before 7.5. No full-page deletion, title, date, signature, mathematical display, or labelled diagram is present.

All words, number fields, punctuation, accents, hyphens, leader runs and writing states were compared line by line with C. The page-number hyphens were settled from half a and require no crop. The ordinary A and B outlines in entries 4.1–4.3 were settled from half a. The crowded lack of space after 4.5. is retained. All remaining open places were listed before making any crop.

## Open loci retained for one crop and one inspection apiece

| Crop | Whole-image bbox | Reason left open by halves |
|---|---|---|
| 01 | [650,318,817,372] | Faint comma after annelés in 4.1; verify its lower trace and material status. |
| 02 | [947,1092,1120,1152] | Small detached mark above annelés in 5.7; identify ink shape versus surface evidence. |
| 03 | [780,1288,1040,1351] | M_f in 6.2; inspect the individual capital outline, index, and writing operation. |
| 04 | [1228,1293,1447,1348] | Cancelled word in 6.2; C explicitly doubts project/projecti. |
| 05 | [790,1494,1005,1544] | Overtyped letter pair in fermeture, 6.5; verify each underlying and live character. |
| 06 | [639,1594,826,1642] | Cancelled glyph after sur in 6.7; C explicitly doubts l/1. |
| 07 | [404,1633,644,1683] | First E of Existence in 6.8 has a crowded contour; verify whether an underletter exists. |
| 08 | [259,1668,400,1749] | Cancelled section-start row before live § 7; C explicitly doubts numeral and point. |
| 09 | [304,1964,470,2020] | Cancelled 7 stub before 7.5; C explicitly doubts a point. |
| 10 | [1420,1505,1590,1567] | Detached dark diagonal pair at right of 6.5; shape and material status. |
| 11 | [1220,1863,1397,1911] | Faint detached points above leaders of 7.3; shape and material status. |

Each crop is taken from the original whole JPEG only, retained as a unique JPEG, enlarged to width 2600 px with Pillow LANCZOS, with zero rotation. Crops use autocontrast with cutoff 0 and a light UnsharpMask (radius 1.2, percent 110, threshold 3). Exact file names and sizes are saved in crop_processing.json. No settled place is recropped. Delivery records and outcomes are added after the inspections.

## Crop deliveries and outcomes

All requested images reached the visual context in full. There were no truncated or failed image deliveries, and no retry or second view. Batches were 01–03, 04–06, 07–09, and 10–11. Every crop has requested_deliveries = 1 and actual_visual_views = 1 in crop_processing.json.

| Crop | Outcome of its single inspection |
|---|---|
| 01 | Faded comma retained. Its low rounded head and descending tail are recoverable. |
| 02 | Detached hook retained graphically with unresolved origin and function. No white channel, crease or scratch was established. |
| 03 | Ordinary typed M and lowered typed f confirmed. The bottom bar is the f serif; there is no independent underline. |
| 04 | Cancelled project/projecti remains unresolved at the final cell. The recoverable string is not completed from context. |
| 05 | Both exchanged old/live letters in fermeture support C's exact deletion encoding. |
| 06 | Slashed l/1 retained. The broad foot and hooked head survive, but the letter/numeral distinction is not forced. |
| 07 | Existence begins with an ordinary single E; the crowded contours do not establish a different underletter. |
| 08 | Section sign and 7 recovered. The following point remains merged with an X foot; absence is recorded as an explicit alternative. |
| 09 | Cancelled 7 recovered; the following point remains doubtful, with no-point/cancellation-ink as an explicit alternative. |
| 10 | Dark diagonal pair retained graphically. Rounded triangular lower-left point and slanted upper-right oval; origin and function unresolved. |
| 11 | Faint separated pair above leaders retained graphically. Left form is notched and right form oval; origin and function unresolved. |

The three unassigned graphic loci were not silently interpreted as punctuation or accents, and their rendering does not assign an author or a writing operation. There was no crop-based exclusion as identifiable surface damage. Diffuse paper texture, ordinary mottling and folds were not promoted into manuscript marks.

## Deliverables and checks

reading.tex is the complete diplomatic page reading. report.json contains eight decision rows (including all four explicit C doubt loci), six rows with diff_c = true, 43 inventory rows, full exact graphic snippets, notation observations, and an empty check_events list. H remains unavailable throughout.

Validation passed for brace balance, nested environment balance, inline math delimiter parity, required report keys, decision bboxes, retained crop paths, explicit-doubt coverage, H-unavailability flags, and the inventory kind vocabulary. Results are retained in validation.json. No TeX engine, build, OCR, external source, other page or other reader was used.
