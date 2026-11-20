# Scan 005 — independent reader R1

## Scope and source views

Complete transcription: [reading.tex](reading.tex). Structured report: [report.json](report.json). This reading is confined to scan 005 and the permitted C/H packet. No other reader, other page, OCR, or outside source was consulted.

Source views: whole page **1**, half A **1**, half B **1**, tight crops **12**; **15 image views total**. Each crop was viewed once. All crop coordinates refer to the original 1678 × 2043 image. Half B starts at whole-image y = 941. Crop JPEGs and individual transformation metadata are in `crops/`; source alignment and timing metadata are in `source_view_metadata.json`.

Start clock: not captured. Earliest actual recorded time: 2026-11-20T09:25:43.653198+00:00. Finished: 2026-11-20T09:36:26.173169+00:00.

## Reading and findings

Handwritten letter to Grothendieck dated at Voorschoten on March 29 1967. The opening reports dispatch of a manuscript on the tame fundamental group and borrowed papers. The terminology paragraph discusses scheme/prescheme and doublet. The references paragraph distinguishes the EGA references and SGA 1960/61 references and mentions the purity theorem. The p.3 and p.5 comments discuss the ordinary-finite-group assumption. The p.6 comment asks about covering as a translation of revêtement, distinguishing it from covering in a topology; it runs off this page after what. Grey marginal writing includes stroke with a line, SGA 1, a circled O.K mark, and an uncircled O.K. No signature or authorial foliation occurs on this page.

There are **24 substantive difference rows**, including **6 against C** and **22 against H**. **5 doubts remain**. H has no uncertainty macro at any listed locus, so every `marked_in_H` value is false. S is an empty array, and there are no S rows.

The principal changes are the singular **reason**, the interior point in bottom-margin **O.K.**, preservation of the separate circled marginal note, restoration of the Serre/Lang parenthesis omitted by H, singular **paper**, and exact punctuation/underlining. The correction before general remains a cancelled uncertain f with an added a. New narrow doubts preserve the capital/lower-case initial of With/with, the name separator, and the small extra mark beside an exclamation point. No unsupported mathematical normalization has been made.

## Complete discrepancy register

### R1-005-01 — Date line, after 1967

- C: `Voorschoten, March 29 1967`
- H: `Voorschoten, March 29 1967.`
- Reading: `Voorschoten, March 29 1967`
- Against C: False; against H: True; kind: text not on the page; confidence: high.
- Evidence: Half A: the final 7 ends the date; the area immediately to its right is blank. H supplies a period.
- Whole-image bounding box: `[1340, 111, 1427, 161]`. Crop: none; resolved from the indicated half.

### R1-005-02 — Address line, after 11

- C: `Palestrinalaan 11`
- H: `Palestrinalaan 11.`
- Reading: `Palestrinalaan 11`
- Against C: False; against H: True; kind: text not on the page; confidence: high.
- Evidence: Half A: two separate numeral strokes 11 end the address, with no terminal dot.
- Whole-image bounding box: `[1190, 177, 1261, 223]`. Crop: none; resolved from the indicated half.

### R1-005-03 — Terminology paragraph, opening punctuation

- C: `As to the terminology:`
- H: `As to the terminology.`
- Reading: `As to the terminology:`
- Against C: False; against H: True; kind: misread symbol or index; confidence: high.
- Evidence: Crop 01 shows two separate vertically disposed dark points following the final y, hence a colon.
- Whole-image bounding box: `[678, 476, 712, 512]`. Crop: [crops/01_terminology_punctuation.jpg](crops/01_terminology_punctuation.jpg).

### R1-005-04 — Terminology paragraph, in stead

- C: `in stead`
- H: `instead`
- Reading: `in stead`
- Against C: False; against H: True; kind: abbreviation expanded or spelling modernised; confidence: high.
- Evidence: Half A: in is followed by a visible word space before the s of stead.
- Whole-image bounding box: `[1004, 477, 1110, 519]`. Crop: none; resolved from the indicated half.

### R1-005-05 — Terminology paragraph, prescheme

- C: `prescheme`
- H: `\emph{preschema}`
- Reading: `prescheme`
- Against C: False; against H: True; kind: misread word; confidence: high.
- Evidence: Half A: the last letter after m has the short curved terminal e form, without the separate upright and bowl of a.
- Whole-image bounding box: `[1134, 477, 1257, 523]`. Crop: none; resolved from the indicated half.

### R1-005-06 — Terminology parenthesis, after mentioning it

- C: `without mentioning it because`
- H: `without mentioning it, because`
- Reading: `without mentioning it because`
- Against C: False; against H: True; kind: text not on the page; confidence: high.
- Evidence: Half A: mentioning it ends the first line without a comma; because begins the next. The t exit stroke is not a detached punctuation mark.
- Whole-image bounding box: `[1356, 480, 1577, 550]`. Crop: none; resolved from the indicated half.

### R1-005-07 — Terminology paragraph, correction before general

- C: `\deleted{\unsure{f}}\inserted{a}`
- H: `a`
- Reading: `\deleted{\unsure{f}}\inserted{a}`
- Against C: False; against H: True; kind: omission; confidence: medium.
- Evidence: Crop 02: a clear upper a occupies the correction position. A lower descending fragment with a dark crossing remains beneath it; f is the best supported incomplete reading, but is not secure. H omits the cancelled fragment and its state.
- Whole-image bounding box: `[722, 532, 762, 577]`. Crop: [crops/02_general_correction.jpg](crops/02_general_correction.jpg).

### R1-005-08 — Terminology left margin, vertical stroke beside stroke

- C: `\draw (.4,-.25)--(.4,.45);`
- H: `omission`
- Reading: `\draw (.4,-.25)--(.4,.45);`
- Against C: False; against H: True; kind: drawing or diagram; confidence: high.
- Evidence: Half A and crop 03: a separate long near-vertical dark stroke stands to the right of the sloping word stroke. H retains only the word.
- Whole-image bounding box: `[286, 534, 310, 611]`. Crop: [crops/03_stroke_margin.jpg](crops/03_stroke_margin.jpg).

### R1-005-09 — References paragraph, opening punctuation

- C: `References:`
- H: `References.`
- Reading: `References:`
- Against C: False; against H: True; kind: misread symbol or index; confidence: high.
- Evidence: Crop 04 shows two distinct points, one above the other, immediately after References.
- Whole-image bounding box: `[532, 662, 560, 695]`. Crop: [crops/04_references_punctuation.jpg](crops/04_references_punctuation.jpg).

### R1-005-10 — References paragraph, extent of underline

- C: `\uline{but only to SGA 1960/61}`
- H: `but
\emph{only to} \emph{SGA 1960/61}`
- Reading: `\uline{but only to SGA 1960/61}`
- Against C: False; against H: True; kind: other; confidence: high.
- Evidence: Half A: the underline begins beneath but and continues beneath only to; the next line SGA 1960/61 is also underlined. H leaves but outside its emphasis.
- Whole-image bounding box: `[1375, 677, 1526, 729]`. Crop: none; resolved from the indicated half.

### R1-005-11 — References paragraph, quotation marks around new numbering

- C: ``new numbering'`
- H: ```new numbering''`
- Reading: ``new numbering'`
- Against C: False; against H: True; kind: misread symbol or index; confidence: high.
- Evidence: Half A: a single raised mark precedes new and a single raised mark follows numbering. Neither side has a pair of strokes.
- Whole-image bounding box: `[394, 845, 638, 908]`. Crop: none; resolved from the indicated half.

### R1-005-12 — References paragraph, You mentioned

- C: `You mentioned`
- H: `you mentioned`
- Reading: `You mentioned`
- Against C: False; against H: True; kind: misread word; confidence: high.
- Evidence: Half A: the initial Y has a full-height fork and long descending stem, larger than the following lower-case letters.
- Whole-image bounding box: `[828, 861, 1019, 919]`. Crop: none; resolved from the indicated half.

### R1-005-13 — p.3 comment, gap after Hyp.1

- C: `p.3 Hyp.1\quad Perhaps`
- H: `p.3 Hyp.1 --- Perhaps`
- Reading: `p.3 Hyp.1\quad Perhaps`
- Against C: False; against H: True; kind: text not on the page; confidence: high.
- Evidence: Half B: there is a blank horizontal gap between Hyp.1 and Perhaps; no dash occupies it.
- Whole-image bounding box: `[407, 1137, 570, 1214]`. Crop: none; resolved from the indicated half.

### R1-005-14 — p.3 comment, after subtle!)

- C: `subtle!) This`
- H: `subtle!). This`
- Reading: `subtle!) This`
- Against C: False; against H: True; kind: text not on the page; confidence: high.
- Evidence: Half B: the exclamation point is followed by the closing parenthesis. No separate period occurs after that parenthesis before the next line This.
- Whole-image bounding box: `[1434, 1393, 1595, 1481]`. Crop: none; resolved from the indicated half.

### R1-005-15 — p.3 comment, reason/reasons

- C: `\unsure{reasons|reason}`
- H: `reason`
- Reading: `reason`
- Against C: True; against H: False; kind: misread word; confidence: high.
- Evidence: Crop 06: the word ends in the final downstroke of n. There is no further s-shaped stroke before the blank leading to for.
- Whole-image bounding box: `[534, 1444, 644, 1493]`. Crop: [crops/06_reasons.jpg](crops/06_reasons.jpg).

### R1-005-16 — p.3 comment, later Hyp 1

- C: `Hyp 1`
- H: `Hyp.1`
- Reading: `Hyp 1`
- Against C: False; against H: True; kind: text not on the page; confidence: high.
- Evidence: Half B: the numeral 1 follows the descending p with a blank gap; there is no separate dot between them. This differs from the dotted label Hyp.1 at the comment opening.
- Whole-image bounding box: `[1035, 1448, 1127, 1505]`. Crop: none; resolved from the indicated half.

### R1-005-17 — p.5 comment, label punctuation

- C: `p.5.`
- H: `p.5`
- Reading: `p.5.`
- Against C: False; against H: True; kind: omission; confidence: high.
- Evidence: Half B: a separate small point follows the 5 before line 6 below.
- Whole-image bounding box: `[267, 1497, 343, 1560]`. Crop: none; resolved from the indicated half.

### R1-005-18 — p.5 comment, terminal punctuation

- C: `\unsure{same|some} reason`
- H: `same reason.`
- Reading: `same reason`
- Against C: False; against H: True; kind: text not on the page; confidence: high.
- Evidence: Crop 07: the final n of reason ends in an upward exit stroke; the following space has no distinct terminal period.
- Whole-image bounding box: `[1224, 1545, 1342, 1600]`. Crop: [crops/07_same_reason.jpg](crops/07_same_reason.jpg).

### R1-005-19 — p.6 comment, beginning of continuation line with the word

- C: `with`
- H: `with`
- Reading: `\unsure{W|w}ith`
- Against C: True; against H: True; kind: other; confidence: medium.
- Evidence: Crop 12: the first w-shaped letter begins with a tall upright reaching the height of the nearby h ascender, unlike the shorter w in word on the same line. Capital W is preferred, but size variation in this hand leaves lower-case w compatible.
- Whole-image bounding box: `[345, 1669, 419, 1725]`. Crop: [crops/12_with_case.jpg](crops/12_with_case.jpg).

### R1-005-20 — p.6 left margin, circled note

- C: `\node at (0,0) {\unsure{OK-}};`
- H: `omission`
- Reading: `\node at (0,0) {O.K\unsure{-|.}};`
- Against C: True; against H: True; kind: drawing or diagram; confidence: medium.
- Evidence: Crop 08: the looped O is followed by a separate low point and a branched K, comparable in shape to the uncircled O.K. below. A short separate horizontal mark follows the K. Its elongated form favours a dash, but a stretched period is possible. The enclosing oval is unmistakable; H omits this separate circled note. The margin note is anchored beside Originally in reading.tex, matching its position on the sheet.
- Whole-image bounding box: `[191, 1721, 342, 1850]`. Crop: [crops/08_circled_margin.jpg](crops/08_circled_margin.jpg).

### R1-005-21 — p.6 comment, Serre-Lang parenthesis

- C: `(in Serre-Lang's paper)`
- H: `omission`
- Reading: `(in Serre\unsure{.|-}Lang's paper)`
- Against C: True; against H: True; kind: omission; confidence: medium.
- Evidence: Half B and crop 09 show the complete parenthesis, with separate words in, Serre, Lang's, paper and both brackets. The mark between the two names is a short low oval stroke, more like a point than a centred hyphen; both readings remain compatible. H omits the parenthesis.
- Whole-image bounding box: `[1290, 1771, 1625, 1838]`. Crop: [crops/09_serre_lang.jpg](crops/09_serre_lang.jpg).

### R1-005-22 — p.6 comment, Lang's paper singular

- C: `(in Lang's paper)!`
- H: `(in Lang's papers)!`
- Reading: `(in Lang's paper)!`
- Against C: False; against H: True; kind: misread word; confidence: high.
- Evidence: Crop 10: paper ends with one hooked r stroke before the closing parenthesis. No separate s follows it.
- Whole-image bounding box: `[738, 1816, 855, 1878]`. Crop: [crops/10_lang_paper.jpg](crops/10_lang_paper.jpg).

### R1-005-23 — p.6 comment, small mark after the exclamation point

- C: `)! But`
- H: `)! But`
- Reading: `)!\unsure{.} But`
- Against C: True; against H: True; kind: omission; confidence: low.
- Evidence: Crop 10: beside the larger loop-like dot belonging to the exclamation point is a distinct smaller low grey mark to its right. It may be a terminal period or an incidental pen trace. The transcription preserves it as a doubtful point.
- Whole-image bounding box: `[853, 1815, 887, 1872]`. Crop: [crops/10_lang_paper.jpg](crops/10_lang_paper.jpg).

### R1-005-24 — Bottom left margin, O.K.

- C: `\margin{OK.}`
- H: `\marginal{O.K.}`
- Reading: `\margin{O.K.}`
- Against C: True; against H: False; kind: omission; confidence: high.
- Evidence: Crop 11: a separate low dot occurs after the O, and another detached mark follows the lower arm of K. C omits the interior point.
- Whole-image bounding box: `[158, 1912, 242, 1973]`. Crop: [crops/11_bottom_ok.jpg](crops/11_bottom_ok.jpg).

## C doubts and prior questions

### Explicit C doubt: terminology correction before general

C: `\deleted{\unsure{f}}\inserted{a}`. Reading: `\deleted{\unsure{f}}\inserted{a}`. Resolved: **False**. Crop 02 distinguishes the added a from a crossed descending remnant below. The remnant is f-like but no second complete letter or word is established.
Whole-image box: `[722, 532, 762, 577]`. Crop: `crops/02_general_correction.jpg`.

### Explicit C doubt: p.3 reason/reasons

C: `\unsure{reasons|reason}`. Reading: `reason`. Resolved: **True**. Crop 06 shows a final n downstroke and then blank space before for; no final s is present.
Whole-image box: `[534, 1444, 644, 1493]`. Crop: `crops/06_reasons.jpg`.

### Explicit C doubt: p.5 same/some

C: `\unsure{same|some}`. Reading: `same`. Resolved: **True**. Crop 07 shows an open a-form with a lower diagonal exit before the separate m; it is not a closed o. The reading uses that form, not the relationship to the previous comment.
Whole-image box: `[1152, 1543, 1228, 1594]`. Crop: `crops/07_same_reason.jpg`.

### Explicit C doubt: circled margin note

C: `\unsure{OK-}`. Reading: `O.K\unsure{-|.}`. Resolved: **False**. Crop 08 distinguishes O, a low point, and K; the short separate trailing stroke remains dash/period ambiguous. The uncertainty is narrowed to that final mark.
Whole-image box: `[223, 1753, 301, 1808]`. Crop: `crops/08_circled_margin.jpg`.

### Prior notation question: references and comments, series designators

C: `SGA I; SGA V; SGA X; SGA D; TDTE III`. Reading: `SGA I; SGA V; SGA X; SGA D; TDTE III`. Resolved: **True**. Half A has single I strokes and the two converging strokes of V; crop 05 shows two crossed diagonals between the cap strokes of X. Half B has the bowed right edge of D and three uprights in III. No series-number replacement is inferred.
Whole-image box: `[1200, 738, 1321, 790]`. Crop: `crops/05_citation_x_and_punctuation.jpg`.

### Prior notation question: p.5 H

C: `H`. Reading: `$H$`. Resolved: **True**. Half B shows two simple upright strokes joined by a single crossbar, with no doubled stem or additional alphabet marker.
Whole-image box: `[838, 1524, 889, 1574]`. Crop: `None`.

### Prior notation question: p.6 quotation marks and accents

C: ```covering''; ``revêtement''; étale`. Reading: ```covering''; ``revêtement''; étale`. Resolved: **True**. Half B shows paired quotation strokes around covering and revêtement, a circumflex over the relevant e of revêtement, and an acute on étale. The second unquoted revêtement also carries its circumflex.
Whole-image box: `[566, 1675, 1054, 1739]`. Crop: `None`.

### Prior notation question: terminology margin word

C: `stroke`. Reading: `stroke`. Resolved: **True**. Crop 03, rotated clockwise by 31 degrees, resolves the separate s, t, r, looped o, tall k, and terminal e, with the distinct vertical line beside it.
Whole-image box: `[116, 535, 310, 620]`. Crop: `crops/03_stroke_margin.jpg`.

### Prior slip retained: in stead

C: `in stead`. Reading: `in stead`. Resolved: **True**. Half A has a word space after in before stead. No normalization to instead.
Whole-image box: `[1004, 477, 1110, 519]`. Crop: `None`.

### Prior slip retained: made freely references

C: `made freely references`. Reading: `made freely references`. Resolved: **True**. Half A displays made, then freely, then references in that physical order; there is no transposition sign.
Whole-image box: `[685, 651, 948, 708]`. Crop: `None`.

### Prior slip retained: misleading used substantivally

C: `one notable misleading / is a misleading`. Reading: `one notable misleading / is a misleading`. Resolved: **True**. Half A has the word misleading at both locations. No missing word after the first misleading or after the article at the second location is indicated by the ink.
Whole-image box: `[696, 715, 975, 781]`. Crop: `None`.

### Prior slip retained: SGA D

C: `SGA D`. Reading: `SGA D`. Resolved: **True**. Half B shows a D with a left upright and a curved outer right side; it is retained without substituting a bibliographical number.
Whole-image box: `[1448, 1330, 1566, 1389]`. Crop: `None`.

## Remaining doubts

- **Terminology correction before general**: `\deleted{\unsure{f}}\inserted{a}` (low). The cancelled lower remnant is f-like, but too crowded to identify securely. No complete alternative word is supported. Alternatives: no additional complete candidate established.
- **p.6 initial of With/with on continuation line**: `\unsure{W|w}ith` (medium). The tall initial favours W, while variation in manuscript lower-case height leaves w possible. Alternatives: w.
- **Circled marginal note, trailing punctuation**: `O.K\unsure{-|.}` (medium). The trailing detached mark is horizontally extended; it could be a dash or an elongated full stop. Alternatives: ..
- **Between Serre and Lang in parenthesis**: `Serre\unsure{.|-}Lang` (medium). The name separator lies low and has a compact oval shape; a very short hyphen cannot be excluded. Alternatives: -.
- **After exclamation point following Lang's paper**: `!\unsure{.}` (low). A small separate low mark stands to the right of the exclamation dot; its punctuation status is uncertain. Alternatives: incidental pen trace; no independent punctuation.

## Inventory

| Element | Kind | Position | Visible content | Hand | Encoded |
|---|---|---|---|---|---|
| E01 | text | top right, two lines | Voorschoten, March 29 1967 / Palestrinalaan 11 | unnamed hand, main dark-ink cursive | yes |
| E02 | text | upper left below heading | Dear Grothendieck, | unnamed hand, main dark-ink cursive | yes |
| E03 | text | upper body, two manuscript lines | Enclosed I send you - finally - | unnamed hand, main dark-ink cursive | yes |
| E04 | text | upper middle, terminology paragraph | As to the terminology: | unnamed hand, main dark-ink cursive | yes |
| E05 | deletion | terminology paragraph, immediately before general | crossed f-like lower remnant | unnamed hand, main dark-ink cursive | yes |
| E06 | insertion | terminology paragraph, above the cancelled remnant | a | unnamed hand, main dark-ink cursive | yes |
| E07 | margin note | left of terminology paragraph, sloping upward to right | stroke | unnamed marginal hand, grey pencil-like writing | yes |
| E08 | drawing | left margin, right of stroke | near-vertical line | unnamed marginal hand, grey/dark stroke | yes |
| E09 | text | middle, references paragraph, with underlined but only to SGA 1960/61 | References: I have made freely references | unnamed hand, main dark-ink cursive | yes |
| E10 | margin note | left of final references lines | SGA 1 | unnamed marginal hand, grey pencil-like writing | yes |
| E11 | text | middle below references | I must admit that there are still many points | unnamed hand, main dark-ink cursive | yes |
| E12 | text | lower middle, p.3 comment; ordinary is underlined | p.3 Hyp.1 Perhaps it would have been nicer | unnamed hand, main dark-ink cursive | yes |
| E13 | text | below p.3 comment, one manuscript line | p.5. line 6 below: the emphasis on H ordinary group : same reason | unnamed hand, main dark-ink cursive | yes |
| E14 | text | lower third to bottom edge; opening In fact this is a general question is underlined | p.6 (Cor 1.11) In fact this is a general question | unnamed hand, main dark-ink cursive | yes |
| E15 | deletion | p.6 comment, after translation | for covering, crossed out | unnamed hand, main dark-ink cursive | yes |
| E16 | margin note | left of Originally revêtement line | O.K plus uncertain trailing dash/period | unnamed marginal hand, grey pencil-like writing | yes |
| E17 | drawing | around the preceding marginal note | oval enclosing O.K and trailing mark | unnamed marginal hand, grey pencil-like stroke | yes |
| E18 | margin note | bottom left alongside covering/topology discussion | O.K. | unnamed marginal hand, grey pencil-like writing | yes |
| E19 | text | extreme bottom left; represented only in an archive comment | archive numeral 4 | unnamed archival hand, grey pencil-like numeral | yes |

All inventory rows are represented in `reading.tex`, including the two deletions, inserted a, the line and oval as TikZ drawings, all four margin notes, and the archive numeral in a comment. There are no mathematical displays or diagrams to encode.

## Notation

- **Terminology and references**: I, V, X, IV; encoding `SGA I; SGA V; SGA X; EGA IV`. None. X independently resolved from the crossing strokes in crop 05.
- **p.3 comment**: SGA D; TDTE III; encoding `SGA D; TDTE III`. None as a letter reading; the bibliographical or mathematical identity is not checked.
- **p.5 comment**: plain capital H; encoding `$H$`. None; single stems and one bar.
- **References paragraph**: single quotation marks around new numbering; encoding ``new numbering'`. None.
- **Terminology and p.6 comment**: paired quotes around doublet, covering, revêtement and the topology phrases; encoding ```doublet''; ``covering''; ``revêtement''`. None.
- **p.6 French terms**: circumflex in revêtement; acute in étale; encoding `revêtement; étale`. None.
- **p.6 Serre/Lang separator**: short low oval point or very short dash; encoding `Serre\unsure{.|-}Lang`. Point preferred; hyphen remains possible.
- **Marginal approvals**: circled O.K with short trailing horizontal mark; lower O.K.; encoding `O.K\unsure{-|.}; O.K.`. Only the circled note’s trailing punctuation remains unresolved.
- **Terminology correction**: upper a over crossed descending remnant; encoding `\deleted{\unsure{f}}\inserted{a}`. The remnant is uncertain f; a and the correction state are visible.
- **p.6 continuation-line initial and punctuation after paper**: tall W/w; small point beside exclamation dot; encoding `\unsure{W|w}ith; !\unsure{.}`. Case and status of the extra point remain unresolved.

## Abbreviations

- `fund.`: fundamental (tentative; expansion not put into the transcription).
- `EGA`: Title abbreviation; full title is not supplied on this page.
- `SGA`: Seminar/title abbreviation; full title is not supplied on this page.
- `TDTE`: Title abbreviation; full title is not established from the permitted page.
- `Cor`: Corollary (tentative; the written abbreviation lacks a dot).
- `Hyp. / Hyp`: Hypothesis (tentative; both punctuation forms are retained).
- `p.`: page.
- `etc`: et cetera.
- `O.K.`: okay / approval (tentative marginal meaning).

## Authorial doubts, dates and mathematical limits

### Author checks

- Terminology: “I expect this will be … general remark in SGA I”.
- Terminology: “I don't know your final decision on this point.”
- References: “I don't know the 'new numbering' of SGA”.
- Introduction to comments: “there are still many points which are not satisfactory in the exposition”.
- p.6: “I have hesitated a little bit” with the word covering; “What do you think about this?”; final “I don't see what” continues beyond this page.

### Titles dates pages

- Date/place: Voorschoten, March 29 1967; no terminal period.
- Address: Palestrinalaan 11; no terminal period.
- No letterhead, signature, title, authorial page number, diagram, or mathematical display is present.
- Comment labels: p.3 Hyp.1; p.5. line 6 below:; p.6 (Cor 1.11).
- References include EGA IV, SGA 1960/61, SGA X Cor 3.3, SGA 1962, SGA I, SGA V, SGA D, and TDTE III.
- The light numeral 4 at the extreme bottom left is recorded as an archive-sheet comment, not as \mspage.

### Math reading decisions

- The shape of X was checked visually in crop 05; the D of SGA D and III of TDTE III were read from half B. These are palaeographical checks, not mathematical verification.
- The H in the p.5 comment is an ordinary capital, without a double-stroke alphabet.
- The statements about the purity theorem, SGA reference scope, quotient existence for ordinary finite groups, the proofs cited to TDTE III, and the distinction between the two uses of covering are carried as page content, explicitly unverified.
- No independent proof, targeted theorem check, computation, or external bibliographical verification was performed.
- There is no missing mathematical arrow or bracket to supply; the page contains prose citations and one inline group letter, with no display or diagram.
- The short manuscript dashes around finally are retained as single hyphens; H’s typographic em-dash encoding is treated as an equivalent representation of those same marks, not an additional manuscript reading.

The mathematical check-event list is empty. Visual recognition of a numeral or letter is not presented as a proof check.

## Brief feedback

- The difference taxonomy has no dedicated punctuation category; punctuation readings are recorded under misread symbol or index, omission, or text not on the page as appropriate.
- The four explicit C doubts are listed first; the remaining prior notation/slip questions are included afterward so every supplied prior issue has a disposition.
- Resolution of C’s same/some to its existing first candidate same is documented in c_doubts, rather than counted as a separate substantive word difference.
