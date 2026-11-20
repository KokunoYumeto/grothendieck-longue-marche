# Independent reading — scan 006, R2

## Scope and view record

Only the authorized scan 006 packet, brief, crop helper, and this reader’s own files were used. No OCR, external research, other page, or other reader’s material was inspected. The whole image was viewed once, half a once, and half b once. Nine tight crops were made and viewed once each: **3 source views + 9 crop views = 12 image views**. No place was recropped or re-viewed. Crop JPEGs and one JSON transform record for each are in `crops/`; `views_metadata.json` records the dimensions and half offsets. The whole image is 1678 × 2036; half a begins at y=0 and half b at y=938. All report bounding boxes use whole-image coordinates.

The exact task-start clock was not captured. The earliest actual recorded clock was 2026-11-20 09:42:59 UTC. Reading and report validation finished at 2026-11-20 09:51:00 UTC.

## Complete reading

The complete diplomatic page is `reading.tex`. It contains every text block, the authorial folio, the archival-number comment, both underlined stretches, both marginal marks, both cancellations, the inline primed point, and the three closing/signature lines. It preserves the original wording, abbreviations and grammar. There are no freestanding mathematical displays or diagrams on this sheet.

## Discrepancies (13)

2 rows are against C; 12 are against H. A row can count against both. H contains no uncertainty flag at these places. Equivalent markup alone is not counted. The C changes are the placement of the exclamation mark at the p.19 label and narrowing the signature doubt to the compressed suffix.

### R2-006-01 — Authorial page number at top centre

- **C:** `\mspage{2.}`
- **H:** `omission`
- **Reading:** `\mspage{2.}`
- **Flags:** against C = False; against H = True; kind = omission; confidence = high.
- **Evidence:** Half a and crop 01: dark curved 2 with a pale separate point at its lower right; this is distinct from the archival 5 at the bottom left.
- **Whole-image box:** `[738, 33, 778, 65]`; crop: `crops/01_folio.jpg`.

### R2-006-02 — Underlined p.19 label

- **C:** `\uline{p.19 etc}`
- **H:** `p.19 etc`
- **Reading:** `\uline{p.19 etc}`
- **Flags:** against C = False; against H = True; kind = omission; confidence = high.
- **Evidence:** Half a: a continuous dark underline runs below p.19 etc and ends before the separated colon. H omits the underline.
- **Whole-image box:** `[204, 147, 324, 210]`; crop: `none; settled from the halves`.

### R2-006-03 — Exclamation mark beside the p.19 label

- **C:** `subtle (but this could be expected).\n\margin{!}`
- **H:** `omission`
- **Reading:** `\margin{!}\uline{p.19 etc}`
- **Flags:** against C = True; against H = True; kind = insertion or placement; confidence = high.
- **Evidence:** Half a: a long near-vertical dark stroke and a detached lower dot stand in the left margin beside the beginning of the p.19 paragraph, not beside its final line. The mark is retained and anchored at that label; H omits it.
- **Whole-image box:** `[134, 168, 160, 225]`; crop: `none; settled from the halves`.

### R2-006-04 — Cancelled sign after an easier one

- **C:** `one\deleted{\unsure{?}}.`
- **H:** `one.`
- **Reading:** `one\deleted{\unsure{?}}.`
- **Flags:** against C = False; against H = True; kind = omission; confidence = medium.
- **Evidence:** Crop 03: above the following live baseline point is a curved hook with dense intersecting transverse and oblique strokes. A question-shaped original is possible but not fully recoverable. The cancellation itself is certain and cannot be omitted. Whether the lower point was reused from the cancelled punctuation cannot be established.
- **Whole-image box:** `[647, 208, 690, 268]`; crop: `crops/03_cancelled_sign.jpg`.

### R2-006-05 — Scope of underline in the line 3 condition

- **C:** `irreducible in \uline{Zariski topology}`
- **H:** `\emph{irreducible in Zariski topology}`
- **Reading:** `irreducible in \uline{Zariski topology}`
- **Flags:** against C = False; against H = True; kind = other; confidence = high.
- **Evidence:** Half a: the underline begins beneath the Z of Zariski and continues through topology. There is no corresponding underline beneath irreducible in. This is a difference in emphasis extent, not merely the use of emph rather than uline.
- **Whole-image box:** `[684, 414, 1117, 479]`; crop: `none; settled from the halves`.

### R2-006-06 — Separator after p.33,34 etc

- **C:** `p.33,34 etc \unsure{..|:}\quad`
- **H:** `p.33, 34 etc.\ ---`
- **Reading:** `p.33,34 etc \unsure{..|:}\quad`
- **Flags:** against C = False; against H = True; kind = misread symbol or index; confidence = medium.
- **Evidence:** Crop 04: two separate short dark points lie close together, the second slightly lower and to the right. Their horizontal displacement exceeds their vertical displacement. No long dash is present and no point immediately follows the c of etc. Two baseline points are preferred, with an oblique colon retained as an alternative.
- **Whole-image box:** `[351, 649, 506, 713]`; crop: `crops/04_p33_separator.jpg`.

### R2-006-07 — Gap after theor.9.4

- **C:** `p.43 theor.9.4\quad You`
- **H:** `p.43 theor.\ 9.4 --- You`
- **Reading:** `p.43 theor.9.4\quad You`
- **Flags:** against C = False; against H = True; kind = text not on the page; confidence = high.
- **Evidence:** Half a: the label is followed by blank space and then You. There is no horizontal dash in that gap.
- **Whole-image box:** `[324, 736, 497, 801]`; crop: `none; settled from the halves`.

### R2-006-08 — Lowercase for after satisfactory

- **C:** `satisfactory . for instance`
- **H:** `satisfactory. For instance`
- **Reading:** `satisfactory . for instance`
- **Flags:** against C = False; against H = True; kind = misread word; confidence = high.
- **Evidence:** Crop 06: for begins with a long narrow stem and a small loop at its top, matching the lowercase f inside the immediately preceding satisfactory. The faint detached period between the words is visible.
- **Whole-image box:** `[1379, 734, 1580, 804]`; crop: `crops/06_for_instance.jpg`.

### R2-006-09 — Compressed word after constant

- **C:** `\unsure{fibres|fibers}`
- **H:** `fibers`
- **Reading:** `\unsure{fibres|fibers}`
- **Flags:** against C = False; against H = True; kind = misread word; confidence = medium.
- **Evidence:** Crop 05: f, i, the tall b and the final s are visible. Between b and s the connected low strokes include a short rising shoulder and a shallow curl; these favour r-e but do not completely exclude e-r. The preferred diplomatic reading is fibres, while fibers remains an explicit alternative. This is not a conclusive rejection of H.
- **Whole-image box:** `[792, 807, 874, 863]`; crop: `crops/05_fibres.jpg`.

### R2-006-10 — Gap after p.45. line 5 etc.

- **C:** `p.45. line 5 etc.\quad Is`
- **H:** `p.45. line 5 etc.\ --- Is`
- **Reading:** `p.45. line 5 etc.\quad Is`
- **Flags:** against C = False; against H = True; kind = text not on the page; confidence = high.
- **Evidence:** Halves a and b: the point after etc is followed by open paper before Is. No dash crosses the gap.
- **Whole-image box:** `[341, 946, 591, 1020]`; crop: `none; settled from the halves`.

### R2-006-11 — Two marginal strokes beside the Lefschetz appendix paragraph

- **C:** `\margin{\figure{\begin{tikzpicture}\draw (0,0)--(-.05,.8);\draw (.12,-.05)--(.09,.65);\end{tikzpicture}}}`
- **H:** `omission`
- **Reading:** `\margin{\figure{\begin{tikzpicture}\draw (0,0)--(-.05,.8);\draw (.12,-.05)--(.09,.65);\end{tikzpicture}}}`
- **Flags:** against C = False; against H = True; kind = drawing or diagram; confidence = high.
- **Evidence:** Half b: two separate thin near-vertical strokes stand in the left margin, slanting slightly right toward their lower ends. The left stroke starts higher; the right stroke reaches a little lower. They are reproduced as a marginal drawing, without assigning a mathematical meaning.
- **Whole-image box:** `[260, 1081, 307, 1211]`; crop: `none; settled from the halves`.

### R2-006-12 — Narrowing the signature doubt

- **C:** `\unsure{J.P. Murre}`
- **H:** `J. P. Murre.`
- **Reading:** `J.P. Mu\unsure{rre}`
- **Flags:** against C = True; against H = False; kind = other; confidence = high.
- **Evidence:** Crop 09: J and P are individually formed and each has its own detached point. The tall three-stroke M and the following low u are legible. Only the final connected rre sequence remains compressed. C doubt is narrowed to those letters; H preferred letters are unchanged in this row, and its terminal period is addressed separately.
- **Whole-image box:** `[990, 1813, 1145, 1874]`; crop: `crops/09_signature.jpg`.

### R2-006-13 — No separate full stop after the signature surname

- **C:** `\unsure{J.P. Murre}`
- **H:** `J. P. Murre.`
- **Reading:** `J.P. Mu\unsure{rre}`
- **Flags:** against C = False; against H = True; kind = text not on the page; confidence = high.
- **Evidence:** Crop 09: the surname ends in a connected low horizontal flourish. There is no separate period at the right or in the lower-right area below its ending; the only clear detached dots belong to the initials.
- **Whole-image box:** `[1090, 1831, 1155, 1880]`; crop: `crops/09_signature.jpg`.

## C doubt dispositions and retained doubts

All four inherited C doubt places were inspected. None is fully resolved at every letter/sign. The signature is substantially narrowed: J.P. and Mu are clear; only rre remains marked. The point after the surname supplied by H is absent.

- **After an easier one:** `\deleted{\unsure{?}}`. Crop 03 confirms crossing-out and a surviving upper hook, but the original sign is obscured. The question-mark candidate is retained without inventing a second candidate. The lower baseline point is visible and live.
- **After p.33,34 etc:** `\unsure{..|:}`. Crop 04 shows two close diagonally arranged points. The almost horizontal arrangement favours two periods, but a steeply slanted colon cannot be excluded. No dash is visible.
- **Theor.9.4 comment, after constant:** `\unsure{fibres|fibers}`. Crop 05 secures f-i-b and the final s. The tiny connected interior strokes favour r-e, but their compressed joins do not decisively rule out e-r.
- **Signature:** `J.P. Mu\unsure{rre}`. Crop 09 resolves J, P, both initial points, M and u. The final rre remains a compressed connected flourish; doubt is therefore retained only on that suffix. No other page or external identity was used.

The four remaining doubt loci are the cancelled question-shaped sign, the two-point separator, fibres/fibers, and the final rre of the surname. S.json is empty; there are no S rows.

## Inventory

| Element | Kind | Position | Content/state |
|---|---|---|---|
| E01 | text | top centre, approximately (740,35) | Authorial folio 2., encoded as \mspage{2.} |
| E02 | text | upper left, y=80–116 | word to use else. |
| E03 | text | upper block, y=145–331 | \uline{p.19 etc} : I expected lemma 4.3; through the lemma 4.4 comment |
| E04 | margin note | left margin beside the p.19 label, y=174–219 | ! |
| E05 | deletion | after an easier one, approximately (660,228) | \deleted{\unsure{?}} |
| E06 | text | upper middle, y=351–409 | p.26. line 1: I shall try to find a precise reference. |
| E07 | text | upper middle, y=416–520 | line 3 : the condition : irreducible in \uline{Zariski topology} |
| E08 | text | middle, y=547–596 | last line in 3) : it seems necessary to mention also the points $s\prime$ |
| E09 | text | middle, y=647–704 | p.33,34 etc \unsure{../:} I did not see an easier proof for prop 7.4. |
| E10 | text | middle, y=738–923 | p.43 theor.9.4 You have mentioned; including constant \unsure{fibres/fibers} |
| E11 | text | middle, y=951–1014 | p.45. line 5 etc. Is this indication sufficient? |
| E12 | text | below centre, y=1054–1171 | I have not written an appendix on the Lefschetz theory. |
| E13 | drawing | left margin beside the appendix paragraph, x=270–299, y=1089–1204 | Two thin vertical/slightly slanting strokes; reproduced with marginal TikZ drawing |
| E14 | text | lower block, y=1247–1656 | It is not necessary to return the manuscript; through date of your first volume. |
| E15 | deletion | inside parenthesis in lower block, x=1450–1520, y=1405–1451 | \deleted{foto}, followed by live photo |
| E16 | text | lower right, y=1668–1795 | With best regards,\\ Sincerely yours,\\ |
| E17 | text | lower right, y=1815–1869 | J.P. Mu\unsure{rre}; no final detached period |
| E18 | text | bottom-left edge, approximately (29,1993) | Archival 5, represented only by % archive sheet number: 5 |

Every inventory item is represented in `reading.tex`; separate rows identify the actual cancellations. There are no claimed hand-added accents, typed words, or additional insertion states. All body text is handwritten. The hand or medium of the marginal marks is not identified beyond their visible contrast with the cursive main text.

## Notes and mathematical status

Handwritten continuation of a letter, carrying authorial page number 2. and archival numeral 5. It comments on proofs, a Zariski-topology irreducibility condition, primed points, a theorem involving constant fibres and crossings, a possible Lefschetz appendix, and manuscript production/deadline arrangements. The page closes with regards and a signature. All ordinary prose, punctuation, underlines, margins and cancellations were read against the image, including witness agreements. The main hand is not externally attributed. Crops 02, 07 and 08 reconsidered tall initial letter strokes in word, copy and manuscript; these were read as the letter’s cursive lowercase forms, and the witnesses’ case readings were retained. The two clear cancellations are the upper question-shaped sign and foto. No additional insertion, diagram, display, stamp, letterhead, title or date is visible. S.json is the empty array, so there are no S rows to adjudicate.

The author’s explicit doubts and promised work include the difficulty of finding shorter proofs for lemma 4.3 and prop 7.4, the subtlety of lemma 4.4, an outstanding reference, the undesirable irreducibility condition, adding points s′, the unsatisfactory formulation of theorem 9.4, the sufficiency of an indication, and the unwritten Lefschetz appendix. These remain authorial statements. No independent proof or computation was performed; `check_events` is intentionally empty. The only mathematical notation decision is the visually clear lowercase s with one prime.

The page has no title or date. Its own folio is 2.; the archival numeral is 5. The cited manuscript pages are 19, 26, 33,34, 43 and 45.

## Crop record

| Crop | Target | Result |
|---|---|---|
| 01_folio.jpg | Folio punctuation | 2. retained; point is pale but separate. |
| 02_opening_word.jpg | Initial letter of word | Lowercase reading retained from the cursive ductus. |
| 03_cancelled_sign.jpg | Crossed sign after one | Cancellation certain; ? remains uncertain. |
| 04_p33_separator.jpg | Two-point separator | Two points clear; periods/oblique-colon interpretation retained. |
| 05_fibres.jpg | Compressed r/e order | fibres preferred, fibers still possible. |
| 06_for_instance.jpg | Lowercase f and preceding point | for, with lowercase looped f; faint period present. |
| 07_copy_initial.jpg | copy at manuscript line start | Lowercase reading retained. |
| 08_manuscript_initial.jpg | manuscript at line start | Lowercase reading retained by its repeated cursive form. |
| 09_signature.jpg | Initials, surname and final punctuation | J.P. Mu clear; suffix rre doubtful; no separate terminal point. |

## Main-reader adjudication

The four retained doubt loci warrant adjudication from their saved evidence. The interpretation of the two low diagonal points as periods or colon is unresolved at the level of intended punctuation, although the physical two-point form is clear. The cancelled sign’s dot may have been reused as the live period; the image does not determine that chronology. No mathematical correction is proposed.

