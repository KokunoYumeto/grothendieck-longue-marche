# Reader B processing record — scan 086

## Scope

Read only the assigned scan086 packet (meta.json, C.tex, H.tex, C_context.md, notation.json), brief_v08.md, conventions.md, PREAMBLE.tex and the three source images listed by meta.json. H is descriptive only and was unavailable as a transcription. No OCR, recognition software, external research, other page, other reader, delegation, or TeX engine was used.

## Image order and coordinates

1. Whole JPEG, 1700 × 2150, viewed once for layout.
2. Half a, 1700 × 1155, viewed once and read line by line. Whole-image offset (0, 0).
3. Half b, 1700 × 1155, viewed once and read line by line. Whole-image offset (0, 995), giving 160 pixels of overlap.

All text, punctuation, accents, leaders, visible correction states and page/archive numbering were checked during the half reading. Entries 6.4 and 6.6 were settled at that stage and were not recropped. No whole image or half was reopened.

## Open-locus list fixed after both halves

- Section 4 heading: extra low-right point after the period (C doubt).
- Entry 5.3: older a/e under live d (C doubt).
- Entry 5.5: older s/b under live f (C doubt).
- Entry 6.10: older l/t under live i (C doubt).
- Entry 6.10: comma/period after schéma (C doubt).
- Vertical trace between section 4 and entry 4.1 leaders (new material/graphic uncertainty).
- Pair of small dark points above entry 6.3 leaders (new material/graphic uncertainty).

## Crop generation and delivery

make_crops.py creates one crop for each listed locus directly from the original whole JPEG. Each crop is RGB, resized to 2400 pixels across using LANCZOS, autocontrasted with zero cutoff, and sharpened using UnsharpMask radius 1.2, percent 110, threshold 3. Each is saved as JPEG with quality 96 and no chroma subsampling. No crop was rotated. Exact bounding boxes, sizes, parameters, requested deliveries and actual visual views are recorded in crop_processing.json.

All seven crops were actually displayed once, in batches 01–03, 04–06, and 07. No delivery was truncated. No image or decided locus was viewed twice. The low broken trace beneath the 6.10 correction was identified within its one retained correction crop, without a new crop or reinspection.

## Output and verification

reading.tex contains the complete diplomatic page. report.json records every C difference, all five explicit C doubts, and confirmed C-context targets. Unassigned marks are reproduced geometrically under unsure markers, without asserting they are authored ink or punctuation. The two flanking dashes of the typed page number are preserved in mspage.

Only source-level brace, environment, math-delimiter, report-schema and coverage checks were performed after writing. Their results are in validation.json. No TeX compilation was attempted.
