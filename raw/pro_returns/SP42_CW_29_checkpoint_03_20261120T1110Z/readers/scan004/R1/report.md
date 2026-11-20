# Scan 004 — independent reader R1

## Reading and scope

Completed only scan 004, using the supplied packet and three source images. The complete diplomatic transcription is in `reading.tex`; the structured collation and full inventory are in `report.json`. Every agreed typed word and sign was read against the image. No OCR, outside research, other page, or other reader was consulted.

The body agrees with C in its wording, spelling, accents and punctuation. The page reads **2.** at the top. It asks for a reply only if the writer has misunderstood the recipient's new set-up, proposes a preliminary manuscript for discussion at Bures, gives **June 2** as the planned arrival, and hopes to complete the **definite** version during the stay. The nonstandard **as good as I can** remains unchanged. The final **e** of **definite** is blue handwriting following the black typed **definit**; `reading.tex` explicitly marks that completion as an insertion. The signature is retained as `\unsure{J.P. Murre}`. The small archive **3** at bottom left is retained solely as a comment.

## Source-view and crop counts

- Whole image: **1 view** for layout.
- Supplied half A: **1 view**, read line by line.
- Supplied half B: **1 view**, including the lower margins.
- Tight crops created: **2**; each viewed **once**, with no recrop or repeated image view.
- Total image-view calls: **5**.

Whole image: 1678 × 2039. Half A: 1678 × 1099, offset (0, 0). Half B: 1678 × 1100, offset (0, 939). Pixel comparison supports those offsets; no recognition was used. All report bounding boxes are in whole-image coordinates. `crop_metadata.json` records the source bounds, 2400-pixel LANCZOS enlargement, autocontrast, light sharpening, zero rotation, and JPEG quality 95/subsampling 0.

The only places open after the halves were the final handwritten e and its faint higher mark, and the compressed signature. They were listed before crops in `open_after_halves.md`.

## Substantive differences

**Three rows**, all against H; none changes C's underlying ink reading.

| ID | Place | C / H | R1 decision and evidence |
| --- | --- | --- | --- |
| R1-004-01 | Top page number | C: `2.`; H: omitted | Retain `\mspage{2.}`. Half A clearly shows a black typed 2 and separate period. Bounds [764, 68, 810, 101]. |
| R1-004-02 | Signature terminal punctuation | C: no terminal period; H: `Murre.` | No period after the surname. Crop 02 shows the final connected blue stroke followed by blank paper. Bounds [801, 717, 983, 789]. This is certain even though the signature's full alphabetic expansion is not. |
| R1-004-03 | Bottom archive foliation | C: archive 3 comment; H: omitted | Retain `% archive sheet number: 3`. Half B shows the pale handwritten numeral at the extreme bottom left. Bounds [23, 1982, 51, 2017]. |

The separate closing/signature line breaks are preserved, but H's line collapse is excluded from the substantive count under the brief's line-wrapping rule. The hand-origin wrapper for the final e is likewise not counted as loss of a letter: both witnesses retain the e at the correct word position. The insertion macro in R1 makes that observed state explicit. C's three literal dots and H's ellipsis character are the same count here. H has no uncertainty flags.

## C questions and S

- **Final e:** resolved as a blue cursive e with a loop and lower turn. No readable typed underletter or cancellation is seen. The higher pale grey speck does not resolve into a blue accent, so no accent is added. Crop 01.
- **Both 2 glyphs:** confirmed typed on half A, with matching rounded top, narrow descending waist and flat baseline. Neither is blue handwriting.
- **Signature:** the C qualification remains. A long descending first initial, looped second initial, point-like separators and large M followed by low compressed waves support **J.P. Murre**, but do not resolve every letter independently. No alternate complete surname is securely supported. Crop 02.
- **as good as I can:** confirmed exactly, including separate o bowls in good, across the two typed lines.
- **Mathematical-step note:** no formula, theorem or proof-check instruction occurs here. No mathematical proof or computation was performed.
- **Title/date/page note:** no title or year; June 2 in the body; typed 2.; separate archive 3.
- **S:** the supplied `S.json` is an empty list; there are no S rows to adjudicate.

## Remaining doubt

One doubt remains: the complete alphabetic expansion of the blue signature, provisionally **J.P. Murre**, at medium confidence. The reading keeps the uncertainty at the signature. Main-reader adjudication may refine this expansion; no other complete candidate is sufficiently supported in this reading. The absence of a terminal surname period is resolved.

## Complete element inventory

| Element | Hand and position | Transcription |
| --- | --- | --- |
| E01 | Typewriter; top centre | `2.` as page number. |
| E02 | Typewriter; nine-line body paragraph | Entire paragraph from I realize to Bures. |
| E03 | Blue pen; end of typed definit | Hand-added e at its actual position, with insertion state. |
| E04 | Typewriter; first closing line, left | With kind regards, |
| E05 | Typewriter; next closing line, farther right | Sincerely yours, |
| E06 | Blue pen; beneath second closing line | Uncertain J.P. Murre, without terminal period. |
| E07 | Pale grey/pencil; extreme bottom left | Archive 3 in a comment only. |

No letterhead, address, stamp, underlining, deletion, diagram, drawing or further marginal prose was observed. The large lower area is blank except for archive foliation. The insertion and all inventory assertions are represented in `reading.tex`.

## Limits and brief feedback

No theory mentioned in the letter was independently verified; the page contains no mathematical argument to check. `check_events` is empty. The brief's distinction between handwritten completion and formal insertion markup is not fully specified; R1 uses both macros for the blue e and treats that markup refinement as conventional rather than a new textual discrepancy.
