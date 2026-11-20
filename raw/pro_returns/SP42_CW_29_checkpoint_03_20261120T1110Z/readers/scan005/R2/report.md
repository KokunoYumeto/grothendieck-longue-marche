# Scan 005 — independent reader R2

## Scope and source use

This report covers scan 005 only. The complete diplomatic reading is in `reading.tex`; machine-readable evidence and decisions are in `report.json`; crop coordinates and transforms are in `crop_metadata.json`. Only the supplied brief, the scan 005 packet, the whole image and its two supplied halves, and R2’s own evidence files were inspected. No OCR, outside research, other page, or other reader was used.

Actual image views: **1 whole image + 1 half a + 1 half b + 14 distinct crops = 17**. Each crop was created and viewed once. There were no recrops and no repeated source views. The source is 1678 × 2043 pixels; half a begins at y = 0 and half b at y = 941. The latter alignment was checked by pixel comparison only. All reported bounding boxes are whole-image coordinates `[left, top, right, bottom)`. Crops are JPEG quality 95, subsampling 0, resized to 2400 pixels across with LANCZOS, autocontrast and an unsharp mask. The sloping margin label alone was rotated clockwise 33 degrees.

The start before the brief was not clocked. The earliest actual recorded timestamp was **2026-11-20T09:25:52Z**. Completion: **2026-11-20T09:35:51Z**.

## Reading outcome

The sheet is a wholly handwritten letter. Its main dark-ink text comprises a two-line heading/address, salutation, three initial prose paragraphs, an introduction to comments, and comments labelled p.3, p.5, and p.6. Four lighter marginal annotations are distinct from the main prose: a sloping “stroke” label with a vertical line, “SGA 1,” a circled O.K followed by a doubtful terminal mark, and a lower “O.K.” The small bottom-left 4 is archival and remains a comment. There is no displayed formula, mathematical diagram, letterhead, signature, or authorial page number on this sheet.

The full letter concerns dispatch of a manuscript, terminology, seminar references, an assumption concerning ordinary finite groups, and the translation “covering” for “revêtement.” Its final sentence continues beyond this page. The reading retains “in stead,” “made freely references,” both noun uses of “misleading,” the citation “SGA D,” and all visible corrections. The p.3 word is singular **reason**; the p.5 word is **same**. The comma after “mentioning it,” missing from C, is clearly present.

Collation records **24 substantive places**: 7 against C’s preferred reading/state and 20 against H. A place can differ from both. There are **5 retained local doubts**. Alternative candidates and equivalent encoding are handled as described in `report.json`; a resolution of a C doubt is not automatically counted as a new difference.

## Substantive discrepancies

### R2-005-01 — Date line: terminal punctuation

- C: `Voorschoten, March 29 1967`
- H: `Voorschoten, March 29 1967.`
- R2: `Voorschoten, March 29 1967`
- Against C: **False**; against H: **True**; confidence: **high**; kind: text not on the page.
- Ink evidence: Half a: the terminal 7 has its descending diagonal and a short cross-stroke; the space immediately following is blank, with no period.
- Whole-image bbox: `[1337, 109, 1431, 160]`; source: `half_a`.

### R2-005-02 — Address line: terminal punctuation

- C: `Palestrinalaan 11`
- H: `Palestrinalaan 11.`
- R2: `Palestrinalaan 11`
- Against C: **False**; against H: **True**; confidence: **high**; kind: text not on the page.
- Ink evidence: Half a: the address ends with two separately written 1 strokes; there is no following punctuation mark.
- Whole-image bbox: `[1169, 173, 1276, 223]`; source: `half_a`.

### R2-005-03 — Terminology paragraph: punctuation after terminology

- C: `terminology:`
- H: `terminology.`
- R2: `terminology:`
- Against C: **False**; against H: **True**; confidence: **high**; kind: misread symbol or index.
- Ink evidence: Crop 01: two separate, vertically offset dots follow the descending y; this is a colon, not a single period.
- Whole-image bbox: `[683, 482, 705, 510]`; source: `crops/01_terminology_punctuation.jpg`.

### R2-005-04 — Terminology paragraph: in stead

- C: `in stead`
- H: `instead`
- R2: `in stead`
- Against C: **False**; against H: **True**; confidence: **high**; kind: abbreviation expanded or spelling modernised.
- Ink evidence: Crop 02: in is a separate two-letter group; the s of stead begins after a pen lift and a visible word gap. The separation is preserved.
- Whole-image bbox: `[1006, 477, 1110, 525]`; source: `crops/02_in_stead.jpg`.

### R2-005-05 — Terminology paragraph: prescheme

- C: `prescheme`
- H: `\emph{preschema}`
- R2: `prescheme`
- Against C: **False**; against H: **True**; confidence: **high**; kind: misread word.
- Ink evidence: Half a, corroborated by the surrounding text in crop 02: the final letter is a short open e with a rightward exit, not an a bowl and right stem.
- Whole-image bbox: `[1138, 480, 1258, 538]`; source: `crops/02_in_stead.jpg`.

### R2-005-06 — Terminology paragraph: comma after mentioning it

- C: `mentioning it because`
- H: `mentioning it, because`
- R2: `mentioning it, because`
- Against C: **True**; against H: **False**; confidence: **high**; kind: omission.
- Ink evidence: Crop 14: a distinct curved, descending comma lies below and to the right of it; it is detached from the t and is not a continuation of its cross-stroke.
- Whole-image bbox: `[1524, 497, 1571, 550]`; source: `crops/14_it_comma.jpg`.

### R2-005-07 — Terminology paragraph: correction before general

- C: `\deleted{\unsure{f}}\inserted{a}`
- H: `a`
- R2: `\deleted{\unsure{f}}\inserted{a}`
- Against C: **False**; against H: **True**; confidence: **medium**; kind: omission.
- Ink evidence: Crop 03: an upper oval and right stem form a; below it a descender and short crossing strokes remain visibly cancelled. The lower letter is f-like but not securely recoverable. H loses the cancellation and the raised replacement state.
- Whole-image bbox: `[724, 532, 758, 581]`; source: `crops/03_cancelled_letter.jpg`.

### R2-005-08 — Left margin beside terminology: labelled vertical stroke

- C: `\margin{\figure{\begin{tikzpicture}[scale=.8]\node[rotate=35] at (-.65,0) {stroke};\draw (.4,-.25)--(.4,.45);\end{tikzpicture}}}`
- H: `\marginal{stroke}`
- R2: `\margin{\figure{\begin{tikzpicture}[scale=.8]\node[rotate=33] at (-.65,0) {stroke};\draw (.43,-.30)--(.40,.34);\end{tikzpicture}}}`
- Against C: **False**; against H: **True**; confidence: **high**; kind: drawing or diagram.
- Ink evidence: Half a and crop 04: the sloping label has s-t-r-o-k-e; a separate long, nearly vertical line stands to its right. H includes the label but omits the drawn line. Minor TikZ geometry changes from C are not counted independently.
- Whole-image bbox: `[119, 538, 308, 617]`; source: `crops/04_stroke_margin.jpg`.

### R2-005-09 — References paragraph: heading punctuation

- C: `References:`
- H: `References.`
- R2: `References:`
- Against C: **False**; against H: **True**; confidence: **high**; kind: misread symbol or index.
- Ink evidence: Crop 05: a clear upper dot and lower dot follow the final s.
- Whole-image bbox: `[539, 664, 556, 689]`; source: `crops/05_references_punctuation.jpg`.

### R2-005-10 — References paragraph: underline begins with but

- C: `\uline{but only to SGA 1960/61}`
- H: `but \emph{only to} \emph{SGA 1960/61}`
- R2: `\uline{but only to SGA 1960/61}`
- Against C: **False**; against H: **True**; confidence: **high**; kind: other.
- Ink evidence: Half a: a continuous rule starts directly under but and runs through only to; the continuation SGA 1960/61 on the next line also has a rule. H does not include but in its emphasis span; the difference is scope, not italic-versus-underline encoding.
- Whole-image bbox: `[1376, 674, 1525, 730]`; source: `half_a`.

### R2-005-11 — References paragraph: quotation multiplicity around new numbering

- C: ``new numbering'`
- H: ```new numbering''`
- R2: `\unsure{``|`}new numbering''`
- Against C: **True**; against H: **False**; confidence: **medium**; kind: misread symbol or index.
- Ink evidence: Crop 06: both quotation clusters have a short branch beside the main down-stroke. Paired strokes are preferred, but the fused shapes can also be read as single hooked ticks. The uncertainty is attached only to the first quotation sign; the closing sign follows the preferred paired reading.
- Whole-image bbox: `[398, 851, 637, 896]`; source: `crops/06_numbering_quotes.jpg`.

### R2-005-12 — References paragraph: You

- C: `(You mentioned`
- H: `(you mentioned`
- R2: `(You mentioned`
- Against C: **False**; against H: **True**; confidence: **high**; kind: misread word.
- Ink evidence: Half a: the first letter after the parenthesis has the tall forked capital Y form; it rises above the following ou.
- Whole-image bbox: `[806, 857, 886, 905]`; source: `half_a`.

### R2-005-13 — p.3 comment: gap following Hyp.1

- C: `p.3 Hyp.1\quad Perhaps`
- H: `p.3 Hyp.1 --- Perhaps`
- R2: `p.3 Hyp.1\quad Perhaps`
- Against C: **False**; against H: **True**; confidence: **high**; kind: text not on the page.
- Ink evidence: Half b: there is open space between the numeral 1 and the initial P of Perhaps. No horizontal dash is written in that gap.
- Whole-image bbox: `[417, 1150, 554, 1213]`; source: `half_b`.

### R2-005-14 — p.3 comment: punctuation after subtle!)

- C: `subtle!) This`
- H: `subtle!). This`
- R2: `subtle!) This`
- Against C: **False**; against H: **True**; confidence: **high**; kind: text not on the page.
- Ink evidence: Half b: the exclamation stroke and its lower dot are inside the closing parenthesis; the space to the right of the parenthesis has no further period.
- Whole-image bbox: `[1442, 1388, 1592, 1467]`; source: `half_b`.

### R2-005-15 — p.3 comment: reason, singular

- C: `\unsure{reasons|reason}`
- H: `reason`
- R2: `reason`
- Against C: **True**; against H: **False**; confidence: **high**; kind: misread word.
- Ink evidence: Crop 08: after the medial s, the o and final n form the remaining two humps; the last down-stroke terminates the n. There is no following separate s or s-shaped terminal turn.
- Whole-image bbox: `[540, 1440, 635, 1491]`; source: `crops/08_reason_ending.jpg`.

### R2-005-16 — p.3 comment: second Hyp 1

- C: `Hyp 1`
- H: `Hyp.1`
- R2: `Hyp 1`
- Against C: **False**; against H: **True**; confidence: **high**; kind: text not on the page.
- Ink evidence: Half b: the p descender is followed by a space and the numeral 1. No independent point is visible between p and 1.
- Whole-image bbox: `[1039, 1452, 1118, 1511]`; source: `half_b`.

### R2-005-17 — p.5 comment: page label

- C: `p.5.`
- H: `p.5`
- R2: `p.5.`
- Against C: **False**; against H: **True**; confidence: **high**; kind: omission.
- Ink evidence: Half b: a separate point follows the handwritten 5 before the gap to line 6.
- Whole-image bbox: `[272, 1496, 335, 1559]`; source: `half_b`.

### R2-005-18 — p.5 comment: punctuation before same reason

- C: `:`
- H: `:`
- R2: `\unsure{.:|:}`
- Against C: **True**; against H: **True**; confidence: **medium**; kind: omission.
- Ink evidence: Crop 09: besides the upper and lower points of a colon at approximately x=1144, a further faint baseline point is visible around x=1122. It is provisionally retained as a preceding period; a speck or incidental pen touch remains possible.
- Whole-image bbox: `[1113, 1556, 1156, 1584]`; source: `crops/09_same_reason.jpg`.

### R2-005-19 — p.5 comment: no terminal point after reason

- C: `\unsure{same|some} reason`
- H: `same reason.`
- R2: `same reason`
- Against C: **False**; against H: **True**; confidence: **high**; kind: text not on the page.
- Ink evidence: Half b and crop 09: the final n has a continuous rising exit stroke. There is no detached terminal dot to its right.
- Whole-image bbox: `[1230, 1557, 1337, 1596]`; source: `crops/09_same_reason.jpg`.

### R2-005-20 — p.6 comment: Serre-Lang parenthesis

- C: `(in Serre-Lang's paper)`
- H: `omission`
- R2: `(in Serre-Lang's paper)`
- Against C: **False**; against H: **True**; confidence: **high**; kind: omission.
- Ink evidence: Half b: the live parenthesis immediately follows the struck for covering. It contains in, the two names separated by a short horizontal mark, apostrophe-s, and singular paper; the closing parenthesis is clear. No cancellation crosses this parenthesis.
- Whole-image bbox: `[1285, 1765, 1623, 1830]`; source: `half_b`.

### R2-005-21 — p.6 comment: Lang paper, singular

- C: `(in Lang's paper)`
- H: `(in Lang's papers)`
- R2: `(in Lang's paper)`
- Against C: **False**; against H: **True**; confidence: **high**; kind: misread word.
- Ink evidence: Crop 12: paper ends in the shoulder and descending terminal of r, followed by blank space and the closing parenthesis. There is no further s-shaped letter.
- Whole-image bbox: `[739, 1818, 859, 1880]`; source: `crops/12_lang_paper_ending.jpg`.

### R2-005-22 — p.6 comment: small mark after exclamation point

- C: `(in Lang's paper)! But`
- H: `(in Lang's papers)! But`
- R2: `(in Lang's paper)!\unsure{.} But`
- Against C: **True**; against H: **True**; confidence: **medium**; kind: omission.
- Ink evidence: Crop 12: the exclamation has its own loop-like lower point, and a second detached short mark lies immediately to its right. It is retained provisionally as an additional period; a stray pen touch is not excluded.
- Whole-image bbox: `[857, 1813, 896, 1873]`; source: `crops/12_lang_paper_ending.jpg`.

### R2-005-23 — Left margin beside Originally: circled annotation

- C: `\margin{\figure{\begin{tikzpicture}[scale=.7]\draw (0,0) ellipse (.6 and .45);\node at (0,0) {\unsure{OK-}};\end{tikzpicture}}}`
- H: `omission`
- R2: `\margin{\figure{\begin{tikzpicture}[scale=.7]\draw (0,0) ellipse (.70 and .63);\node at (0,0) {O.K\unsure{-|.}};\end{tikzpicture}}}`
- Against C: **True**; against H: **True**; confidence: **medium**; kind: drawing or diagram.
- Ink evidence: Crop 10: a closed surrounding oval encloses a looped O, a tall branched K, a detached low point after O, and a detached short horizontal mark after K. The final mark is dash-like, with a period still possible. The whole annotation, including the circle, is absent from H.
- Whole-image bbox: `[193, 1718, 339, 1852]`; source: `crops/10_circled_note.jpg`.

### R2-005-24 — Lower left margin: dotted O.K.

- C: `\margin{OK.}`
- H: `\marginal{O.K.}`
- R2: `\margin{O.K.}`
- Against C: **True**; against H: **False**; confidence: **high**; kind: omission.
- Ink evidence: Crop 11: one detached dot lies after the looped O and another detached mark lies after the two arms of K. Both punctuation marks are preserved.
- Whole-image bbox: `[158, 1915, 243, 1975]`; source: `crops/11_lower_ok.jpg`.

## All C questions and prior observations

The four formal doubts are listed first; the supplied notation and preserved-slip observations are also checked explicitly. S.json was an empty list, so there are no S rows to confirm or overturn.

### Formal C doubt: cancelled letter before general

C: `f` → R2: `\deleted{\unsure{f}}\inserted{a}`. Resolved: **False**.
Crop 03 confirms a separate upper a and lower cancelled strokes. The lower cross-strokes and descender fit f, but its full outline is not independently recoverable; no additional complete cancelled word is warranted.
BBox: `[724, 532, 758, 581]`; crop: `crops/03_cancelled_letter.jpg`.

### Formal C doubt: p.3 reason ending

C: `reasons | reason` → R2: `reason`. Resolved: **True**.
Crop 08 shows final n and no subsequent s-shaped character. The decision is based on the terminal strokes, not agreement with the grammar.
BBox: `[540, 1440, 635, 1491]`; crop: `crops/08_reason_ending.jpg`.

### Formal C doubt: p.5 same/some

C: `same | some` → R2: `same`. Resolved: **True**.
Crop 09: the vowel after s has an open bowl and a distinct short right down-stroke, like the a in the following reason; o would not account for that separate right stroke.
BBox: `[1155, 1549, 1227, 1592]`; crop: `crops/09_same_reason.jpg`.

### Formal C doubt: circled marginal annotation

C: `OK-` → R2: `O.K\unsure{-|.}`. Resolved: **False**.
Crop 10 permits the letters O and K and the internal point to be read separately. The detached rightmost horizontal mark remains uncertain between dash and elongated point. Doubt has therefore been narrowed to the last punctuation mark.
BBox: `[216, 1749, 306, 1816]`; crop: `crops/10_circled_note.jpg`.

### Prior notation question: SGA I; SGA V; SGA X; SGA D; TDTE III

C: `SGA I; SGA V; SGA X; SGA D; TDTE III` → R2: `SGA I; SGA V; SGA X; SGA D; TDTE III`. Resolved: **True**.
Halves a and b: I is an isolated upright with short horizontal ends; V has two converging diagonals; X has crossing diagonals; D in the p.3 comment has one left upright and a rounded right boundary; III in TDTE III has three uprights with horizontal joining strokes. The bbox gives the most consequential D occurrence; other placements are itemized in notation.
BBox: `[1445, 1338, 1558, 1393]`; crop: `none; supplied half`.

### Prior notation question: p.5 group letter

C: `H` → R2: `$H$`. Resolved: **True**.
Half b: the letter consists of two single uprights and a connecting cross-stroke. There is no doubled outline or blackboard-bold construction.
BBox: `[843, 1519, 884, 1565]`; crop: `none; supplied half`.

### Prior notation question: covering / revêtement / étale

C: ```covering''; ``revêtement''; étale` → R2: ```covering''; ``revêtement''; étale`. Resolved: **True**.
Half b: paired quotation strokes surround the quoted terms; revêtement has a small circumflex above ê on each occurrence, and étale has a detached acute stroke. These are part of the wholly handwritten text, not additions to typing.
BBox: `[565, 1674, 1029, 1745]`; crop: `none; supplied half`.

### Prior notation question: sloping stroke label

C: `stroke` → R2: `stroke`. Resolved: **True**.
Crop 04, rotated clockwise 33 degrees: separate s, crossed t, low r, loop o, tall branched k, and terminal e are readable. The independent line to the right is retained in TikZ.
BBox: `[119, 538, 308, 617]`; crop: `crops/04_stroke_margin.jpg`.

### Prior preserved slip: in stead

C: `in stead` → R2: `in stead`. Resolved: **True**.
Crop 02 confirms the visible separation of in and stead.
BBox: `[1006, 477, 1110, 525]`; crop: `crops/02_in_stead.jpg`.

### Prior preserved slip: word order

C: `made freely references` → R2: `made freely references`. Resolved: **True**.
Half a: made precedes freely, which precedes references; no transposition strokes or insertion marks occur over these words.
BBox: `[681, 650, 951, 710]`; crop: `none; supplied half`.

### Prior preserved slip: misleading used as a noun

C: `one notable misleading / is a misleading` → R2: `one notable misleading / is a misleading`. Resolved: **True**.
Half a: one notable misleading appears in the parenthesis and the following line reads is a misleading. The word misleading is not followed by reference at either occurrence.
BBox: `[625, 718, 974, 789]`; crop: `none; supplied half`.

### Prior preserved slip: SGA D

C: `SGA D` → R2: `SGA D`. Resolved: **True**.
Half b: the final character has a straight left stem and a rounded right bowl, with no second upright or numeral-like terminal. D is preserved without a bibliographical substitution.
BBox: `[1445, 1338, 1558, 1393]`; crop: `none; supplied half`.

## Retained local doubts

- **Terminology paragraph, cancelled lower character before general**: `\deleted{\unsure{f}}`. Alternative(s): `no other complete letter or word securely supported`. Confidence: low. Crossing strokes obscure the original lower outline; the f-like descender is not enough for certainty.
- **References paragraph, quotation marks around new numbering**: `\unsure{``|`}new numbering''`. Alternative(s): ``new numbering'`. Confidence: medium. The short side branches favour two fused ticks, but a single hooked tick can produce a similar shape. Only the opening carries the recurring-sign doubt.
- **p.5 comment, before same reason**: `\unsure{.:|:}`. Alternative(s): `:`. Confidence: medium. The faint extra baseline point preceding the clear colon may be an incidental pen touch or speck.
- **p.6 comment, after (in Lang's paper)!**: `!\unsure{.}`. Alternative(s): `! with no additional period`. Confidence: medium. A separate right-hand mark is visible beside the exclamation point but its intentional status is uncertain.
- **Circled marginal note, terminal punctuation**: `O.K\unsure{-|.}`. Alternative(s): `O.K.`. Confidence: medium. The detached last mark is elongated horizontally; it may be a dash or a stretched period. The letters and internal point are retained without whole-note uncertainty.

The material adjudication points are the lower cancelled character, the fused quotation strokes, the two possible extra punctuation marks, and the final mark inside the circled annotation. No whole word, sentence, or entire annotation is left uncertain when only one component is doubtful.

## Complete inventory

| ID | Kind | Position / first words or objects | Encoded in reading.tex |
|---|---|---|---|
| E01 | text | top right, x=1007–1404, y=88–215; Voorschoten, March 29 1967 / Palestrinalaan 11 | Two heading/address lines in reading.tex, each ending in \\. |
| E02 | text | upper left of text area, x=310–585, y=230–287; Dear Grothendieck, | Salutation with comma and explicit line break. |
| E03 | text | upper body, x=328–1520, y=320–441; Enclosed I send you | Complete first prose paragraph. |
| E04 | text | upper body, x=337–1622, y=459–634; As to the terminology: | Complete terminology paragraph, including comma after it and the correction at general. |
| E05 | deletion | within terminology paragraph, x=724–758, y=548–581; cancelled f-like lower character | \deleted{\unsure{f}} |
| E06 | insertion | above cancellation, x=724–758, y=532–560; a | \inserted{a} |
| E07 | drawing | left margin beside terminology, x=119–308, y=538–617; sloping stroke label and separate near-vertical line | \margin{\figure{...TikZ node stroke plus line...}}; lighter marginal writing, identity not established. |
| E08 | text | middle body, x=334–1556, y=640–984; References: | Complete references paragraph; underlining spans but only to SGA 1960/61; local quotation doubt retained. |
| E09 | margin note | left margin, x=111–247, y=926–980; SGA 1 | \margin{SGA 1}; lighter marginal writing. |
| E10 | text | middle/lower body, x=329–1538, y=1007–1146; I must admit | Complete introductory paragraph to the comments. |
| E11 | text | lower body, x=277–1591, y=1150–1515; p.3 Hyp.1 | Complete p.3 comment; ordinary underlined; SGA D and TDTE III retained; singular reason. |
| E12 | text | lower body, x=271–1342, y=1496–1603; p.5. line 6 below: | Complete p.5 line, plain mathematical H, same reason, and doubtful extra point before colon. |
| E13 | text | bottom body, x=260–1628, y=1588–1993; p.6 (Cor 1.11) | Complete p.6 comment through unfinished I don't see what; question phrase underlined; both paper parentheticals retained. |
| E14 | deletion | within p.6 comment, x=1092–1265, y=1757–1823; for covering | \deleted{for covering}; cancellation crosses only these words. |
| E15 | drawing | left margin beside Originally, x=193–339, y=1718–1852; oval around O.K followed by doubtful dash/point | \margin{\figure{...TikZ ellipse and O.K\unsure{-\|.}...}}; lighter annotation, identity not established. |
| E16 | margin note | lower left margin, x=158–243, y=1915–1975; O.K. | \margin{O.K.}; both points represented. |
| E17 | text | extreme bottom left, x=26–51, y=1986–2017; 4 | % archive sheet number: 4; archival numeral, not authorial pagination. |

Main prose and marginal annotations are recorded as unnamed hands; identity and whether every lighter annotation is by the same person are not established from this page. No handwriting attribution is inferred from another page. Both actual cancellations and the replacement a have their own inventory entries. Each inventory entry has been matched to the transcription.

## Notation and abbreviations

- **References paragraph: EGA IV**: `EGA IV`. none; I is followed by V; half a; bbox [1202,672,1322,714].
- **Terminology paragraph and references paragraph**: `SGA I`. none; upright Roman I with short end strokes; half a; bboxes [1036,542,1127,582] and [889,926,982,967].
- **References paragraph: purity citation**: `SGA X, Cor 3.3`. none; crossing diagonals of X read visually; half a; bbox [1205,738,1414,789].
- **References paragraph: old seminar numbering**: `SGA V`. none; two diagonals form V; half a; bbox [1021,927,1113,972].
- **p.3 comment: final seminar letter**: `SGA D`. none as a letter reading; identification of the cited seminar is not supplied or checked; half b; bbox [1445,1338,1558,1393].
- **p.3 comment: TDTE**: `TDTE III`. none; three uprights, with short horizontal joining strokes, represent III; half b; bbox [705,1371,872,1419].
- **p.5 comment: group symbol**: `$H$`. none; single-stroke capital, not doubled; half b; bbox [843,1519,884,1565].
- **References paragraph: new numbering quotes**: `\unsure{``|`}new numbering''`. paired marks preferred, single ticks remain stroke-compatible; first occurrence bears the doubt; crop 06.
- **References paragraph: séminaire**: `séminaire`. none; a detached accent stroke is visible above the first e region, before the two i dots; crop 07.
- **p.6 comment: French terms**: `revêtement; étale`. none; circumflex and acute read in half b; no typescript is present.
- **p.5 comment: punctuation before same**: `\unsure{.:|:}`. whether the first point is written punctuation or an incidental touch; crop 09.
- **p.6 comment: after (in Lang's paper)!**: `!\unsure{.}`. additional period preferred; incidental touch remains possible; crop 12.
- **Circled marginal note**: `O.K\unsure{-|.}`. final dash versus elongated period; crop 10.
- **Lower marginal note**: `\margin{O.K.}`. none; both detached points visible; crop 11.

Abbreviation expansions are explanatory only and are never inserted into the diplomatic text:

- `fund.`: fundamental (tentative expansion from the phrase tame fund. group; not expanded in reading.tex).
- `p.`: page.
- `Hyp. / Hyp`: hypothesis (the second occurrence is written without a period).
- `Cor`: corollary (no period supplied in the transcription).
- `etc`: et cetera.
- `SGA`: series siglum; no expansion established from the permitted page.
- `EGA`: series siglum; no expansion established from the permitted page.
- `TDTE`: series siglum; no expansion established from the permitted page.
- `O.K.`: approval annotation; retained in abbreviated form.

## Authorial reservations, dates and mathematical status

A handwritten letter headed Voorschoten, March 29 1967, Palestrinalaan 11, addressed to Grothendieck. The opening reports dispatch of a manuscript on the tame fund. group in two covers together with borrowed papers. The terminology paragraph adopts scheme in stead of prescheme but awaits a decision on doublet. The References paragraph discusses EGA and the old SGA seminar numbering. The p.3 and p.5 comments explain the placement of Hyp 1 in connection with ordinary finite groups. The p.6 comment asks about covering as a translation of revêtement and its possible confusion with covering in a topology; this page ends mid-sentence at I don't see what. Four marginal annotations and the archival numeral 4 are preserved. No signature, letterhead, typed text, displayed formula, or mathematical diagram appears on this page.

Authorial reservations and questions, quoted at the preferred reading:

- I expect this will be a general remark in SGA I
- I don't know your final decision on this point.
- I don't know the ``new numbering'' of SGA
- I must admit that there are still many points which are not satisfactory in the exposition.
- Perhaps it would have been nicer to avoid a little longer this assumption.
- the proof is long and subtle!
- I have hesitated a little bit with the word ``covering'' for ``revêtement''
- What do you think about this?

Dates and page/citation labels:

- Date: March 29 1967.
- Place and address: Voorschoten; Palestrinalaan 11.
- No authorial page number or formal title on this sheet.
- Archival numeral: 4, represented only by a comment.
- Cited manuscript pages: 3, 5, 6.
- Cited labels: Hyp.1 / Hyp 1, Cor 1.11, Cor 3.3.
- Cited seminar years: 1960/61 and 1962.

Mathematical reading decisions:

- The assertions about quotients for ordinary finite groups, the TDTE III proofs, and the purity theorem are carried as unverified statements of the letter. No external theorem or bibliographical verification was performed.
- SGA D is retained from the rounded D-shaped glyph; no mathematically or bibliographically expected replacement is inserted.
- TDTE III is read as three Roman uprights, and H is a plain capital. This was visual notation verification only.
- The contrast between the translation covering and covering in the étale topology was followed as prose; no equivalence or non-equivalence theorem was checked.
- No computation, proof, independent re-proof, or use of a mathematical statement as a proved premise occurred. Therefore check_events is empty.

**check_events is empty.** Visual reading of indices, quotation marks, capitals, and a citation is not represented as a mathematical proof check. No assertion about purity, quotient existence, or the cited seminar content was independently established.

## Brief feedback

- The brief does not specify how against_c / against_h should be set when the final preferred reading agrees with a witness but a local uncertainty remains. Here the flags compare the preferred letters and visible state; retained alternatives are recorded separately.
- The timing rule was followed conservatively: the exact pre-brief start was not captured, so the first actual clock timestamp is supplied separately.

## Crop question log

- `crops/01_terminology_punctuation.jpg`: colon or period after terminology → colon; two separate dots.
- `crops/02_in_stead.jpg`: word separation in stead → two words; final e of prescheme also visible in surrounding text.
- `crops/03_cancelled_letter.jpg`: lower cancelled character and upper replacement → upper a clear; lower f retained doubtful.
- `crops/04_stroke_margin.jpg`: sloping marginal letters and separate line → stroke plus line.
- `crops/05_references_punctuation.jpg`: colon or period after References → colon; two dots.
- `crops/06_numbering_quotes.jpg`: one or two strokes in each quotation cluster → paired favoured, single retained as alternative.
- `crops/07_seminaire_accent.jpg`: small accent over séminaire → accent confirmed.
- `crops/08_reason_ending.jpg`: reason or reasons → reason; no separate terminal s.
- `crops/09_same_reason.jpg`: same or some; adjacent punctuation → same; no final point; possible extra point before colon retained doubtful.
- `crops/10_circled_note.jpg`: circled note letters and strokes → O.K with final dash/point doubt; oval retained.
- `crops/11_lower_ok.jpg`: internal punctuation of lower OK note → O.K.; two points.
- `crops/12_lang_paper_ending.jpg`: paper or papers, and adjacent punctuation → paper; possible extra point after exclamation retained doubtful.
- `crops/13_assumption_punctuation.jpg`: period or comma after assumption → period, in agreement with C and H; no descending comma tail.
- `crops/14_it_comma.jpg`: presence of comma after mentioning it → clear separate descending comma; C omission.
