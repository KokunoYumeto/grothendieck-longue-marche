## Current status (supersedes the troubleshooting handoff below)

The same reader_c continued successfully. The original and both prepared halves have each been read once; lossless WebP transport solved the oversized image delivery issue. All seventeen evidence crops have been read. The complete first-reading proposal and metadata are now in proposed/148_scan068.tex and proposed/148_scan068.json. No replacement reader or blind second reading was used.

# Reader C handoff: 148_scan068

## Why a fresh reader is needed
The long-running reader_c thread hit a cumulative `functions.exec` image-output ceiling. Two attempts to display the existing first half returned exactly: `Code Mode session output limit reached: omitted 0 text bytes; discarded 0 text segments, 1 images, 0 audio items`. Increasing max_output_tokens to 20000 did not help. Neither half image has been delivered or read. This is a tool failure, not an unresolved reading.

## Work actually completed
- Read this page's C.tex and H.tex, differences.tsv, images.json and PREAMBLE.tex.
- MARKS.tsv was printed in the same call, but its middle was truncated. A fresh reader must read the complete MARKS table (compact columns are enough). There are 144 IDs, M0800–M0943: a 12-row × 8-column letter banner (M0800–M0895), then 12-row × 4-column zero patterns (M0896–M0943).
- The current page's guide.md and refreshed notation.md have NOT yet been read in this new assignment. The same general guide was followed on earlier assignments, but the fresh reader should read the current copies.
- Viewed the ORIGINAL 148_scan068.jpg exactly once for layout. Do not repeat this initial original view in the continued first reading; the remaining halves show all its ink at higher resolution.
- No half was read, no crop was made/viewed, and no transcription or JSON proposal has been written.
- No other page source/packet/root notes were opened.

## Source and existing prepared halves
Original: `/workspace/scratch/f28c4f52d3ec/source/SP83_C13_148+149_scans/148_scan068.jpg`, size 3015 × 2227.
- half1 `/workspace/scratch/f28c4f52d3ec/halves/148_scan068_half1.png`, source box [0,0,1658,2227]; UNREAD.
- half2 `/workspace/scratch/f28c4f52d3ec/halves/148_scan068_half2.png`, source box [1357,0,3015,2227]; UNREAD.

## Original-view layout observations (not final readings)
A landscape reused line-printer sheet, green ruled/hatched bands, sprocket holes at left/right. Pencil/pen sketches stand upright in the upper-right region; the printed listing in the lower half is upside down relative to these sketches. Pale handwritten folio 67 sits at lower left. Attribution of this folio must remain `unnamed hand (folio annotation; attribution uncertain)`.

Approximate sketch regions, to refine from the still-unread right half:
- Small loop/oval with a dark vertex around (1758,362), roughly x1695–1993, y135–425; a faint interior arc/chord goes toward the upper-right part of its outline.
- Tiny graph row around x2070–2490, y125–182: apparently three short vertical segments with endpoint dots, followed by two pairs of separated dots. Verify every stroke and whether any extra dot/line exists.
- Upper-right six-point oval/circle, x2454–2845, y190–518. Dark vertices approximately (2605,222), (2758,202), (2792,415), (2577,511), (2527,457), (2515,287). Multiple outer retracings and faint chords; every connection needs the crop reading, not C's schematic connectivity.
- Long dark edge between about (1842,583) and (2242,454), with small endpoint circles, a long surrounding narrow oval, extension lines and two near-vertical rays at its right endpoint; roughly x1680–2380,y345–650.
- Shorter dark edge between about (2071,740) and (2287,686), each endpoint circled, inside a wider pale oval; roughly x1925–2400,y610–858.
- Two-hole oval with a narrow connecting band and radial segments, roughly x2430–2810,y590–950. No labels were apparent at original scale, but the half/crop must decide.

Printed regions (all still require line-by-line reading and cropped evidence):
- Six repeated small-font job-record rows across approximately x230–2865, y935–1140, upside down. C supplies six identical rows `****A END JOB 653 PREDONTA  ROOM  11.24.04 AM 02 JUN 82 R6.PR1  SYS JES2 JOB 653 END A****`. Verify every character, spacing and repeat independently; H only mentions the date in an editorial note.
- Large PREDONTA block letters made from repeated small letters, around x430–2680,y1200–1595. As viewed upside down, A is leftmost and P rightmost. Each block-letter glyph has 12 print rows. C places a separate uncertainty on each cell of its 12×8 array. A practical crop plan is one enlarged 180-degree-rotated crop per complete block letter, so all 12 associated marks have evidence together; manually count characters and spaces, with no OCR.
- Four large zero-like patterns made from small printed zeros, around x1470–2700,y1690–2095. C gives 12 rows per pattern and doubts every row. There also appear to be SMALL PRINTED LABELS adjacent to these large patterns (below them in the unrotated original, therefore above after 180-degree rotation), which C omits. Their letters were not read at original scale; do not guess them from context. Include complete labels with the pattern crops and read everything.
- Lower folio 67 around x155–247,y2100–2168, to refine from half1.

## Required continuing workflow
Read only packets/148_scan068 and that page's named images. Read each existing half ONCE, then create/view tight enlarged evidence crops for all material differences, all resolved C marks, all open figure/print details. No OCR, web, TeX compilation or blind second reading. All visible printer output must be transcribed, including graphic letter/zero patterns and any missing small labels; use standard LaTeX/TikZ and current macros. Every drawing connection must be reproduced, and uncertainty retained where faint strokes do not decide. C's graphic approximations and H's prose descriptions are witnesses, not evidence.

Write complete proposed/148_scan068.tex and .json with the current guide schema. `decisions` must contain exactly the supplied MARKS IDs; new/implicit decisions go separately. Provide individual remaining doubts, sheet_kind=reused_typed throughout, and truthful mathematical/background check events. Include exhaustive unique blind-audit boxes for every required category, every numeric label/index/exponent, every printed cell still doubtful, every figure corrected, all margin/revision material. Keep generators and intermediates. Send crop paths early so root can inspect before acceptance.
