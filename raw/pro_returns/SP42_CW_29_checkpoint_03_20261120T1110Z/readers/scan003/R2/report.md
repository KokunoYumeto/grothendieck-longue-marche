# Independent reading R2 — cote 29, scan 003

Started: 2026-11-20T08:58:42.262957Z  
Finished: 2026-11-20T09:10:27.777844Z

## Complete diplomatic reading

The complete verified transcription is in [reading.tex](reading.tex). It includes the place/date and address, salutation, all three paragraphs, formulae, cancellations, inserted wording, handwritten signs, the transposition curve, the isolated lower mark, and the archival number as a comment. No text was inferred from another page.

The three substantive changes to C are **developped** (two printed p letters), the previously unrecorded **e/i overstrike in giving/giveng**, and the **slanted lower stroke of the handwritten inequality**. C’s seven existing localized doubts remain unresolved. The new e/i correction-order question makes **eight remaining doubts**.

## Source views and evidence operations

- Whole page: **1 view**, for layout.
- Full-resolution half a: **1 view**, before half b.
- Full-resolution half b: **1 view**.
- Tight evidence crops: **11 generated, 11 viewed, each once**.
- Total image views: **14**. No whole or half was viewed again; no crop was recropped.
- Each crop was resized to 2,400 pixels wide using LANCZOS, autocontrasted, and sharpened with radius 1.2, 120 percent, threshold 3. Rotation was zero throughout; no text required rotation. Each PNG has a neighboring JSON recording the original whole-image bounding box and transforms.
- All coordinates below are in the 1,674 × 2,037 whole image, not in a half.
- The supplied halves were JPEG-reencoded rather than pixel-identical to simple whole-image rectangles. Evidence crops were taken directly from the whole source, so their coordinates do not depend on pixel identity.
- Crop 07 clips the lowest edge of the Hom subscript. Its full curve had been read in half b; the crop still enlarged the upper curve and prime. No second crop was made.
- No OCR, recognition library, PDF layer, internet source, or other reader’s output was used.

## Discrepancies

There are **29 difference rows**: **3 against C** and **27 against H**, with one row affecting both. Three H rows concern unsupported italic styling of French prose; these are kept separate from its lexical/sign errors. H’s editorial prose note is not counted as manuscript text.

### R2-003-01 — Paragraph 1, “for what purpose you … things”

- C: `developed`
- H: `developped`
- R2: `developped`
- Difference: misread word; against C: true; against H: false; confidence: high.
- Evidence: Crop 01 shows two separately spaced p stems, two p bowls, and two descenders between o and e. This is developped, not a single p.
- Whole-image box: [1120, 340, 1339, 378]. Evidence crop: [crops/01_developed.png](crops/01_developed.png).

### R2-003-02 — Paragraph 1, “instead of … directly”

- C: `giving`
- H: `giving`
- R2: `\unsure{giv\deleted{e}ing|giv\deleted{i}eng}`
- Difference: deletion state (struck given live or live given struck); against C: true; against H: true; confidence: medium.
- Evidence: Crop 02 shows, in the cell after v, an i dot and upright/foot together with an e-shaped bowl and cross-stroke. Both impressions survive. The final i is the first candidate, but the sequence of the e and i impressions is not established.
- Whole-image box: [1043, 489, 1184, 531]. Evidence crop: [crops/02_giving.png](crops/02_giving.png).

### R2-003-03 — Paragraph 1, first covering r(X)

- C: `\underline{r}(X)`
- H: `r(X)`
- R2: `\underline{r}(X)`
- Difference: misread symbol or index; against C: false; against H: true; confidence: high.
- Evidence: Half a shows a separate short horizontal stroke immediately below the lowercase r; X is plain.
- Whole-image box: [170, 544, 258, 585]. Evidence crop: none; settled in the named source half.

### R2-003-04 — Paragraph 1, “behaviour over … these”

- C: `\unsure{a\deleted{l}al|a\deleted{a}ll}`
- H: `all`
- R2: `\unsure{a\deleted{l}al|a\deleted{a}ll}`
- Difference: deletion state (struck given live or live given struck); against C: false; against H: true; confidence: medium.
- Evidence: Crop 03 shows plain first a and last l, with an a bowl and an l ascender occupying the middle typewriter cell. Their impression order is not recoverable.
- Whole-image box: [783, 643, 849, 678]. Evidence crop: [crops/03_aal.png](crops/03_aal.png).

### R2-003-05 — Paragraph 1, “better information … the”

- C: `then`
- H: `than`
- R2: `then`
- Difference: misread word; against C: false; against H: true; confidence: high.
- Evidence: Half a shows the open e with its horizontal middle stroke in then, rather than an a bowl.
- Whole-image box: [417, 693, 507, 726]. Evidence crop: none; settled in the named source half.

### R2-003-06 — Paragraph 1, “the r(X) alone”

- C: `\underline{r}(X)`
- H: `r(X)`
- R2: `\underline{r}(X)`
- Difference: misread symbol or index; against C: false; against H: true; confidence: high.
- Evidence: Half a shows the second r with its own horizontal underline, as at the earlier occurrence.
- Whole-image box: [597, 694, 691, 737]. Evidence crop: none; settled in the named source half.

### R2-003-07 — Paragraph 2, “some var…ations”

- C: `var\inserted{\handwritten{i}}ations`
- H: `variations`
- R2: `var\inserted{\handwritten{i}}ations`
- Difference: insertion or placement; against C: false; against H: true; confidence: high.
- Evidence: Half a shows the blue i above the missing-letter position between typed var and ations; the letter is an added correction.
- Whole-image box: [1456, 887, 1645, 935]. Evidence crop: none; settled in the named source half.

### R2-003-08 — Paragraph 2, French “la definition de”

- C: `definition`
- H: `définition`
- R2: `definition`
- Difference: abbreviation expanded or spelling modernised; against C: false; against H: true; confidence: high.
- Evidence: Halves a/b show no acute stroke above the first e of definition. The neighboring grave and circumflex marks are visible, so the unaccented spelling is retained.
- Whole-image box: [517, 985, 733, 1028]. Evidence crop: none; settled in the named source half.

### R2-003-09 — Paragraph 2, typography of the long French quotation

- C: `On peut enfin l'expliciter en revenant à la definition de $\mathrm{Rev}^{\underline{R}}(S)$, et en exigeant que les revêtements des $\underline{s}(M)$ correspondants à $X$ soient principaux de groupe $G$.`
- H: `\emph{On peut enfin l'expliciter en revenant à la définition ⏎ de $\mathrm{Rev}^{\underline{R}}(S)$, et en exigeant que les revêtements des ⏎ $\underline{s}(M)$ correspondants à $X$ soient principaux de groupe $G$.}`
- R2: `On peut enfin l'expliciter en revenant à la definition de $\mathrm{Rev}^{\underline{R}}(S)$, et en exigeant que les revêtements des $\underline{s}(M)$ correspondants à $X$ soient principaux de groupe $G$.`
- Difference: other; against C: false; against H: true; confidence: high.
- Evidence: Halves a/b show the same upright typewriter face as the surrounding English and no underline over this French passage. H’s italic emphasis is not an ink state. The separate accent discrepancy is listed independently.
- Whole-image box: [169, 943, 1619, 1081]. Evidence crop: none; settled in the named source half.

### R2-003-10 — Paragraph 2, first hand-added group acting on Z

- C: `\handwritten{\unsure{\mathfrak{g}|g|\mathscr{G}}}`
- H: `\mathcal{G}`
- R2: `\handwritten{\unsure{\mathfrak{g}|g|\mathscr{G}}}`
- Difference: misread symbol or index; against C: false; against H: true; confidence: medium.
- Evidence: Crop 04 shows two closed, rather angular loops joined at the right by a descending stem, with the lower loop below the typewritten baseline. This favors a g-shaped form, but the exact intended alphabet remains unsettled. H’s definite calligraphic capital is not established by these strokes.
- Whole-image box: [785, 1143, 823, 1190]. Evidence crop: [crops/04_group.png](crops/04_group.png).

### R2-003-11 — Paragraph 2, insertion between “covering” and X

- C: `\inserted{\handwritten{corresponding with}}`
- H: `\marginal{corresponding with}`
- R2: `\inserted{\handwritten{corresponding with}}`
- Difference: insertion or placement; against C: false; against H: true; confidence: high.
- Evidence: Half b shows “corresponding” above “with” in blue at the left, beside a long stem with looped head; a matching looped stem is placed in the gap after covering and before X. This establishes insertion into the sentence. H’s note recognizes the target but its transcript keeps the words as a margin item.
- Whole-image box: [23, 1142, 752, 1275]. Evidence crop: none; settled in the named source half.

### R2-003-12 — Paragraph 2, second group letter in “G and … commute”

- C: `\handwritten{\mathfrak{g}}`
- H: `\mathcal{G}`
- R2: `\handwritten{\mathfrak{g}}`
- Difference: misread symbol or index; against C: false; against H: true; confidence: medium.
- Evidence: Half b shows the same two-loop, right-stem blue glyph as the first group letter. The first occurrence carries the alphabet alternatives; this occurrence uses its first candidate.
- Whole-image box: [709, 1242, 746, 1286]. Evidence crop: none; settled in the named source half.

### R2-003-13 — Paragraph 2, “your letter you … (for example 1)”

- C: `\unsure{explai\deleted{n}m|explai\deleted{m}n}`
- H: `explain`
- R2: `\unsure{explai\deleted{n}m|explai\deleted{m}n}`
- Difference: deletion state (struck given live or live given struck); against C: false; against H: true; confidence: medium.
- Evidence: Crop 05 shows a heavily superposed terminal cell with m-like paired downstrokes and an n-like right contour. A dark blue/black correction is present, but the order of the m/n readings is not visually secure.
- Whole-image box: [927, 1297, 1075, 1325]. Evidence crop: [crops/05_explaim.png](crops/05_explaim.png).

### R2-003-14 — Paragraph 2, canceled character after “important point”

- C: `\deleted{\unsure{f|i}}`
- H: `omission`
- R2: `\deleted{\unsure{f|i}}`
- Difference: omission; against C: false; against H: true; confidence: low.
- Evidence: Crop 06 shows a separate typed character with surviving foot and an apparent upper f-like hook, crossed by blue strokes before the intact “if”. The f candidate is favored; the cancellation obscures enough of the body that i is retained.
- Whole-image box: [822, 1491, 855, 1524]. Evidence crop: [crops/06_point_if_wne.png](crops/06_point_if_wne.png).

### R2-003-15 — Paragraph 2, “if … wants”

- C: `\unsure{\deleted{o}wne|\deleted{w}one}`
- H: `one`
- R2: `\unsure{\deleted{o}wne|\deleted{w}one}`
- Difference: deletion state (struck given live or live given struck); against C: false; against H: true; confidence: medium.
- Evidence: Crop 06 shows a round o contour and internal w strokes superposed in the first cell, followed by plain ne. Neither impression can be securely assigned as the canceled one.
- Whole-image box: [927, 1495, 997, 1525]. Evidence crop: [crops/06_point_if_wne.png](crops/06_point_if_wne.png).

### R2-003-16 — Paragraph 2, “what is going on…”

- C: `\handwritten{!}`
- H: `omission`
- R2: `\handwritten{!}`
- Difference: omission; against C: false; against H: true; confidence: high.
- Evidence: Half b shows a long blue exclamation stroke between on and the closing parenthesis, with a point below. The closing parenthesis and full stop remain separate.
- Whole-image box: [1602, 1475, 1627, 1525]. Evidence crop: none; settled in the named source half.

### R2-003-17 — Paragraph 3, final s of “consists”

- C: `consist\deleted{s}`
- H: `consist`
- R2: `consist\deleted{s}`
- Difference: deletion state (struck given live or live given struck); against C: false; against H: true; confidence: high.
- Evidence: Half b shows a typed s after consist and a slanted cancellation through it. H gives only the surviving word and loses the canceled letter.
- Whole-image box: [950, 1634, 1124, 1674]. Evidence crop: none; settled in the named source half.

### R2-003-18 — Paragraph 3, “couples”

- C: `\uline{couples}`
- H: `\emph{couples}`
- R2: `\uline{couples}`
- Difference: other; against C: false; against H: true; confidence: high.
- Evidence: Half b shows one long straight underline below the complete upright typed word couples. It is not italic type.
- Whole-image box: [1274, 1638, 1429, 1682]. Evidence crop: none; settled in the named source half.

### R2-003-19 — Paragraph 3, subscript under Hom

- C: `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}`
- H: `\mathrm{Hom}_{S'}`
- R2: `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}`
- Difference: misread symbol or index; against C: false; against H: true; confidence: medium.
- Evidence: Half b shows the full small blue S-shaped subscript and a separate prime. Crop 07 enlarges the upper curve and prime, but the lowest part of the curve meets the crop’s lower edge. The small scale permits either lowercase s or reduced capital S; a definite capital is not compelled.
- Whole-image box: [1090, 1689, 1182, 1747]. Evidence crop: [crops/07_hom_subscript.png](crops/07_hom_subscript.png).

### R2-003-20 — Paragraph 3, relation between n prime and n

- C: `\handwritten{\geq}`
- H: `\geqslant`
- R2: `\handwritten{\geqslant}`
- Difference: misread symbol or index; against C: true; against H: false; confidence: high.
- Evidence: Crop 08 shows a right-pointing angle and a separate short lower stroke rising from left to right, parallel to the lower arm of the angle. The lower stroke is slanted, not horizontal.
- Whole-image box: [385, 1745, 416, 1786]. Evidence crop: [crops/08_relations_periods.png](crops/08_relations_periods.png).
- Mathematical note: This is a visual choice of the slanted inequality glyph; it does not change the mathematical inequality.

### R2-003-21 — Paragraph 3, typography of the first French fragment

- C: `$\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}(M',M)$ est vide sauf si $\underline{n}'\handwritten{\geq}\underline{n}$, auquel cas....etc.....`
- H: `\emph{$\mathrm{Hom}_{S'}(M',M)$ est vide sauf si $\underline{n}' \geqslant ⏎ \underline{n}$, auquel cas…etc…}`
- R2: `$\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}(M',M)$ est vide sauf si $\underline{n}'\handwritten{\geqslant}\underline{n}$, auquel cas....etc.....`
- Difference: other; against C: false; against H: true; confidence: high.
- Evidence: Half b shows upright typed “est vide sauf si” and “auquel cas” without an underline or a change of face. H’s italic wrapper is unsupported; symbol and dot-count differences are separate rows.
- Whole-image box: [177, 1691, 1492, 1786]. Evidence crop: none; settled in the named source half.

### R2-003-22 — Paragraph 3, dots around “etc”

- C: `auquel cas....etc.....`
- H: `auquel cas…etc…`
- R2: `auquel cas....etc.....`
- Difference: other; against C: false; against H: true; confidence: high.
- Evidence: Crop 08 shows four individual periods after cas and five after etc, followed by a comma. The three-dot ellipses in H collapse the visible counts.
- Whole-image box: [498, 1746, 974, 1785]. Evidence crop: [crops/08_relations_periods.png](crops/08_relations_periods.png).

### R2-003-23 — Paragraph 3, “this shuold be”

- C: `sh\handwritten{\tikz[overlay,baseline]{\draw[line width=.4pt] (0,-.02) .. controls (.08,.23) and (.17,.25) .. (.20,.06) .. controls (.22,-.12) and (.36,-.15) .. (.39,-.02);}}uold`
- H: `should`
- R2: `sh\handwritten{\tikz[overlay,baseline]{\draw[line width=.4pt] (0,-.02) .. controls (.08,.23) and (.17,.25) .. (.20,.06) .. controls (.22,-.12) and (.36,-.15) .. (.39,-.02);}}uold`
- Difference: insertion or placement; against C: false; against H: true; confidence: high.
- Evidence: Crop 09 shows the typed order s-h-u-o-l-d and a blue transposition curve that rises over u and runs down and below o. Both typed order and added curve are retained instead of silently executing the correction.
- Whole-image box: [1503, 1750, 1637, 1791]. Evidence crop: [crops/09_shuold.png](crops/09_shuold.png).

### R2-003-24 — Paragraph 3, product between underlined m and n

- C: `\underline{m}.\underline{n}`
- H: `\underline{m}\cdot\underline{n}`
- R2: `\underline{m}.\underline{n}`
- Difference: misread symbol or index; against C: false; against H: true; confidence: high.
- Evidence: Crop 08 shows the separating dot at the typed baseline, at the same vertical level as the following cas periods, rather than at the letters’ mathematical midline.
- Whole-image box: [562, 1794, 634, 1833]. Evidence crop: [crops/08_relations_periods.png](crops/08_relations_periods.png).

### R2-003-25 — Paragraph 3, dots delimiting the replacement French phrase

- C: `....sauf si $\underline{n}'=\underline{m}.\underline{n}$, auquel cas.....`
- H: `…\emph{sauf si $\underline{n}' = \underline{m}\cdot\underline{n}$, auquel ⏎ cas…}`
- R2: `....sauf si $\underline{n}'=\underline{m}.\underline{n}$, auquel cas.....`
- Difference: other; against C: false; against H: true; confidence: high.
- Evidence: Half b shows four periods before sauf; crop 08 shows five periods after the second cas. These are explicit typed dots, not a uniform ellipsis convention.
- Whole-image box: [239, 1793, 1009, 1834]. Evidence crop: [crops/08_relations_periods.png](crops/08_relations_periods.png).

### R2-003-26 — Paragraph 3, typography of the replacement French fragment

- C: `sauf si $\underline{n}'=\underline{m}.\underline{n}$, auquel cas.....`
- H: `…\emph{sauf si $\underline{n}' = \underline{m}\cdot\underline{n}$, auquel ⏎ cas…}`
- R2: `sauf si $\underline{n}'=\underline{m}.\underline{n}$, auquel cas.....`
- Difference: other; against C: false; against H: true; confidence: high.
- Evidence: Half b and crop 08 show upright type throughout the replacement French fragment, with no underline below its prose. H adds italic emphasis.
- Whole-image box: [319, 1793, 1009, 1834]. Evidence crop: [crops/08_relations_periods.png](crops/08_relations_periods.png).

### R2-003-27 — Paragraph 3, “is a a set”

- C: `is a a set`
- H: `is a set`
- R2: `is a a set`
- Difference: omission; against C: false; against H: true; confidence: high.
- Evidence: Half b shows an a at the right end of the penultimate typed line, after is, and a second a at the start of the last line before set. Crop 10 confirms the first a.
- Whole-image box: [170, 1792, 1602, 1883]. Evidence crop: [crops/10_indices.png](crops/10_indices.png).

### R2-003-28 — Isolated small mark below the last line

- C: `\margin{\handwritten{\unsure{,|'}}}`
- H: `omission`
- R2: `\margin{\handwritten{\unsure{,|'}}}`
- Difference: omission; against C: false; against H: true; confidence: low.
- Evidence: Crop 11 shows a small brown stroke with a thick upper head and a tapering lower-left tail. Without a text baseline it could function as comma or apostrophe, or be an incidental stroke; it is retained with uncertainty.
- Whole-image box: [454, 1901, 472, 1927]. Evidence crop: [crops/11_bottom_mark.png](crops/11_bottom_mark.png).

### R2-003-29 — Bottom-left pencilled archive number

- C: `% archive sheet number: 2`
- H: `omission`
- R2: `% archive sheet number: 2`
- Difference: omission; against C: false; against H: true; confidence: high.
- Evidence: Half b shows a pale pencilled 2 at the bottom-left. The supplied page packet identifies this as the archival sheet number, so it is recorded only in a comment.
- Whole-image box: [31, 1984, 66, 2018]. Evidence crop: none; settled in the named source half.

## Every inherited C doubt

All seven inherited doubts were inspected locally. None is silently normalized.

1. **Paragraph 1, “apparantly … these”** — `\unsure{a\deleted{l}al|a\deleted{a}ll}`. Status: retained. Crop 03 confirms an a bowl and l ascender in the same middle cell; the first a and final l are plain. No impression sequence is established. Box [783, 643, 849, 678]; [crops/03_aal.png](crops/03_aal.png).

2. **Paragraph 2, group acting on Z** — `\unsure{\mathfrak{g}|g|\mathscr{G}}`. Status: retained. Crop 04 confirms two closed loops and a right joining stem with descender. The g-shaped reading is favored, but fraktur, ordinary lowercase, and a script-capital intention cannot be separated from these strokes alone. Box [785, 1143, 823, 1190]; [crops/04_group.png](crops/04_group.png).

3. **Paragraph 2, “you explaim”** — `\unsure{explai\deleted{n}m|explai\deleted{m}n}`. Status: retained. Crop 05 shows the heavy m/n superposition in the final cell. The correction is real; its chronological order remains uncertain. Box [927, 1297, 1075, 1325]; [crops/05_explaim.png](crops/05_explaim.png).

4. **Paragraph 2, “point … if”** — `\deleted{\unsure{f|i}}`. Status: retained. Crop 06 shows a clear separate canceled type character, a foot, and a probable f-like upper hook. Blue cancellation strokes obscure the body sufficiently that i remains a weaker candidate. Box [822, 1491, 855, 1524]; [crops/06_point_if_wne.png](crops/06_point_if_wne.png).

5. **Paragraph 2, “if … wants”** — `\unsure{\deleted{o}wne|\deleted{w}one}`. Status: retained. Crop 06 confirms a round o and w zigzag in the same initial cell followed by ne. It does not establish which impression came last. Box [927, 1495, 997, 1525]; [crops/06_point_if_wne.png](crops/06_point_if_wne.png).

6. **Paragraph 3, Hom subscript** — `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}`. Status: retained. Half b contains the full small S-shaped sign and a separate prime; crop 07 enlarges its top and prime but clips the lowest curve at its lower edge. The case remains ambiguous rather than being resolved by the name of a base category. Box [1090, 1689, 1182, 1747]; [crops/07_hom_subscript.png](crops/07_hom_subscript.png).

7. **Isolated mark below the last line** — `\unsure{,|'}`. Status: retained. Crop 11 confirms the thick head and tapering lower-left tail of a brown stroke. There is no neighboring text baseline to distinguish comma from apostrophe, or prove that the mark was intentional punctuation. Box [454, 1901, 472, 1927]; [crops/11_bottom_mark.png](crops/11_bottom_mark.png).

## Remaining doubts

The first candidate is retained in the diplomatic text; correction-order alternatives remain explicit.

- **Paragraph 1, giving/giveng overstrike**: `giv\deleted{e}ing`; alternatives: `giv\deleted{i}eng`. Confidence: medium. Both an i (dot and stem) and e (bowl/cross-stroke) occupy the fourth letter cell. Their order is not secure.

- **Paragraph 1, all/aal overstrike**: `a\deleted{l}al`; alternatives: `a\deleted{a}ll`. Confidence: medium. The a and l overlap in the middle cell; no visible sequence settles the surviving form.

- **Paragraph 2, hand-added group letter**: `\mathfrak{g}`; alternatives: `g`, `\mathscr{G}`. Confidence: medium. Two loops and a descender favor a g-shaped letter, without an alphabet key on this page.

- **Paragraph 2, explaim/explain overstrike**: `explai\deleted{n}m`; alternatives: `explai\deleted{m}n`. Confidence: medium. The final cell is darkly superposed; the m/n correction order is not established.

- **Paragraph 2, canceled letter after point**: `f`; alternatives: `i`. Confidence: low. The upper hook favors f, but the center of the character is obscured by blue cancellation.

- **Paragraph 2, wne/one overstrike**: `\deleted{o}wne`; alternatives: `\deleted{w}one`. Confidence: medium. The circular o and internal w strokes coexist in one cell; neither has demonstrable priority.

- **Paragraph 3, Hom subscript case**: `s'`; alternatives: `S'`. Confidence: medium. The small S-shaped handwritten curve can be a lowercase s or a reduced capital; the prime is secure.

- **Bottom isolated mark**: `,`; alternatives: `'`, `incidental nontext stroke`. Confidence: low. The brown head-and-tail stroke has no baseline or syntactic context.

## S witness

S.json is an empty array. There are no S rows to confirm or overturn.

## Complete element inventory

There are no freestanding mathematical displays, diagrams, or drawings. Formulae occur inline in the three typed paragraphs. The only graphic annotation is the small transposition curve, retained as an inline TikZ correction. Actual corrections and cancellations have separate entries below.

| Element | Kind | Position | Hand and content |
| --- | --- | --- | --- |
| E01 | text | top right, y 78–158 | typewriter; Voorschoten, May 16 1967. / Palestrinalaan 11. — transcribed: yes |
| E02 | text | upper left, y 201–228 | typewriter; Dear Grothendieck, — transcribed: yes |
| E03 | text | upper body, y 249–777 | typewriter with unnamed annotating hand; I am trying to work out your letter with indications. — transcribed: yes |
| E04 | text | middle body, y 800–1525 | typewriter with unnamed annotating hand; My main difficulty is that I don’t see that for a Galois covering — transcribed: yes |
| E05 | text | lower body, y 1548–1879 | typewriter with unnamed annotating hand; Some other points: in the final formulation of example 3 — transcribed: yes |
| E06 | deletion | paragraph 1, fourth cell of giving, x 1110–1136, y 495–527 | overlapping typewriter impressions; e/i overstrike in giving/giveng; both possible correction orders retained — transcribed: yes |
| E07 | deletion | paragraph 1, x 803–827, y 645–678 | overlapping typewriter impressions; a/l overstrike in aal/all — transcribed: yes |
| E08 | insertion | paragraph 1 end, x 908–931, y 730–774 | unnamed annotating hand, blue; question-mark hook completing the question after set-up — transcribed: yes |
| E09 | insertion | paragraph 2, x 1518–1536, y 888–918 | unnamed annotating hand, blue; i inserted in varations — transcribed: yes |
| E10 | insertion | paragraph 2, x 418–435, y 985–1011 | unnamed annotating hand, dark blue; grave stroke in en revenant à — transcribed: yes |
| E11 | insertion | paragraph 2, x 784–802, y 1040–1067 | unnamed annotating hand, blue; grave stroke in correspondants à X — transcribed: yes |
| E12 | insertion | paragraph 2, x 785–823, y 1143–1190 | unnamed annotating hand, blue; first g-shaped group letter — transcribed: yes |
| E13 | insertion | left margin x 23–160, y 1142–1275, targeting x 734, y 1205 | unnamed annotating hand, blue; corresponding / with, paired loop-and-stem insertion marks — transcribed: yes |
| E14 | insertion | paragraph 2, x 709–746, y 1242–1286 | unnamed annotating hand, blue; second g-shaped group letter — transcribed: yes |
| E15 | insertion | paragraph 2, x 1256–1281, y 1229–1273 | unnamed annotating hand, blue; question-mark hook after correct — transcribed: yes |
| E16 | deletion | paragraph 2, final cell of explaim/explain, x 1051–1076, y 1302–1325 | typewriter with dark blue/black correction; exact sequence uncertain; overlap of terminal m/n — transcribed: yes |
| E17 | deletion | paragraph 2, x 440–548, y 1447–1479 | typewriter cancellation by overtyped x strokes; makes — transcribed: yes |
| E18 | deletion | paragraph 2, x 822–855, y 1491–1524 | typed character canceled by unnamed annotating hand in blue; f, with i retained as weaker alternative — transcribed: yes |
| E19 | deletion | paragraph 2, x 929–953, y 1497–1525 | overlapping typewriter impressions; o/w overstrike before ne — transcribed: yes |
| E20 | insertion | paragraph 2 end, x 1602–1627, y 1475–1525 | unnamed annotating hand, blue; exclamation mark after on — transcribed: yes |
| E21 | deletion | paragraph 3, x 871–1309, y 1598–1629 | typewriter cancellation by overtyped x strokes; with this formulation — transcribed: yes |
| E22 | deletion | paragraph 3, x 1093–1122, y 1635–1673 | unnamed annotating hand over typewriter letter; final s of consists — transcribed: yes |
| E23 | text | paragraph 3, x 1274–1429, y 1638–1682 | typewriter, single underline; couples — transcribed: yes |
| E24 | insertion | paragraph 3, x 626–666, y 1686–1734 | unnamed annotating hand, blue; mu before the typed underlined n subscript in G(M) — transcribed: yes |
| E25 | insertion | paragraph 3, x 720–746, y 1673–1724 | unnamed annotating hand, blue; question mark after G(M)=mu_n — transcribed: yes |
| E26 | insertion | paragraph 3, x 1157–1182, y 1720–1747 | unnamed annotating hand, blue; s-shaped subscript and prime under Hom — transcribed: yes |
| E27 | insertion | paragraph 3, x 385–416, y 1745–1786 | unnamed annotating hand, blue; slanted greater-than-or-equal sign — transcribed: yes |
| E28 | insertion | paragraph 3, x 1536–1594, y 1750–1791 | unnamed annotating hand, blue; transposition curve over/under the typed uo in shuold — transcribed: yes |
| E29 | insertion | paragraph 3, x 1463–1488, y 1821–1844 | unnamed annotating hand, blue; membership sign between outer i and I — transcribed: yes |
| E30 | margin note | below body, x 454–472, y 1901–1927 | unnamed hand or incidental brown stroke; isolated comma/apostrophe-like mark — transcribed: yes |
| E31 | text | bottom-left, x 31–66, y 1984–2018 | unnamed pencilled hand; 2, recorded as archive sheet number comment — transcribed: yes |

## Notation and abbreviations

- **Paragraph 1, all r(X) and s(M) occurrences**: lowercase r and s each with a short individual underline; plain X, M, and S. LaTeX: `\underline{r}(X),\ \underline{s}(M),\ S`. Uncertainty: none.

- **Paragraph 1, behaviour quotation**: two short raised oblique strokes at each end. LaTeX: ```behaviour''`. Uncertainty: none.

- **Paragraph 2, Rev expression**: upright Rev; raised plain capital R with its own underline; parentheses around S. LaTeX: `\mathrm{Rev}^{\underline{R}}(S)`. Uncertainty: none; no accent over Rev and no doubled capital.

- **Paragraph 2, group on Z and commuting group**: blue glyph with two closed loops, right stem, and descender. LaTeX: `\unsure{\mathfrak{g}|g|\mathscr{G}}`. Uncertainty: alphabet/case unresolved at first occurrence; first candidate reused at second.

- **Paragraph 3, M pair and multiplier**: a, n, m individually underlined; primes are raised separate strokes. LaTeX: `M=(\underline{a},\underline{n});\ \underline{n}\prime;\ \underline{m}`. Uncertainty: none.

- **Paragraph 3, G(M)**: blue handwritten mu followed by lower typed n with its own underline. LaTeX: `G(M)=\handwritten{\mu}_{\underline{n}}`. Uncertainty: none.

- **Paragraph 3, Hom expression**: upright Hom, small blue S-shaped lower-right letter, separate prime; M prime then M in parentheses. LaTeX: `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}(M',M)`. Uncertainty: case of the subscript only.

- **Paragraph 3, comparison**: blue right-pointing angle plus rising oblique lower stroke. LaTeX: `\underline{n}\prime\handwritten{\geqslant}\underline{n}`. Uncertainty: none; lower stroke is slanted.

- **Paragraph 3, multiplier equality**: baseline typed period between underlined m and n. LaTeX: `\underline{n}\prime=\underline{m}.\underline{n}`. Uncertainty: none; retain period rather than mathematical centered dot.

- **Paragraph 3, final indexed family**: both small letters i have dots and no descenders; handwritten membership sign; plain serif capital I. LaTeX: `\underline{m}=(m_i)_{i\handwritten{\in}I}`. Uncertainty: none; crop 10 independently confirms both i letters.

- **All mathematical capitals and functor names on this page**: typed X,S,M,G,Z,I,R,Rev,Hom individually single-struck. LaTeX: `X,S,M,G,Z,I,\mathrm{Rev},\mathrm{Hom}`. Uncertainty: none; no double-struck heading or functor letter.

- **Paragraph 3, dotted French fragments**: four dots after first cas; five after etc; four before replacement sauf; five after replacement cas. LaTeX: `cas....etc.....; ....sauf si ... auquel cas.....`. Uncertainty: none.

- **Paragraph 1, giving correction**: e-shaped bowl/cross-stroke and i dot/stem in the same cell. LaTeX: `\unsure{giv\deleted{e}ing|giv\deleted{i}eng}`. Uncertainty: correction order unresolved; absent from both drafts.

- **Paragraph 3, transposition mark**: blue rising loop above u followed by descending curve below o in typed shuold. LaTeX: `inline TikZ proofreading curve retained from C after visual verification`. Uncertainty: none; no freestanding diagram or drawing occurs.

Abbreviation: **etc** = “et cetera”; this expansion appears only in the report.

## Content, author questions, and mathematical limits

An unsigned typed letter page, addressed to Grothendieck from Voorschoten and dated May 16 1967, with blue handwritten corrections and mathematical characters. Paragraph 1 asks whether the construction can be understood through the behavior of a covering over the s(M). Paragraph 2 questions uniqueness of extra structure for Galois coverings, commuting group actions, and a claimed full-faithfulness result. Paragraph 3 asks about example 3a and proposes a divisibility-shaped condition in place of a componentwise-looking inequality. These covering-theory claims are carried as the letter’s unverified questions, not proved here. All text, formula occurrences, corrections, and margins were read from the three authorized source views. Eleven local crops were created and viewed once each. Crop 07 reaches the lower edge of the small Hom subscript; the complete curve was visible in half b, and its case remains unresolved. S.json contains no rows.

The author explicitly raises the following questions or reservations:

- `I doubt whether I have grasped the essential points.`

- `Is this intuitively a reasonable way of thinking over your new set-up?`

- `It seems to me that one must require that the actions of $G$ and $\mathfrak{g}$ commute; is this correct?`

- `this I don't understand at all`

- `do the objects in example 3a ,with this formulation, consist\deleted{s} out of \uline{couples} $M=(\underline{a},\underline{n})$ and $G(M)=\handwritten{\mu}_{\underline{n}}$ \handwritten{?}`

- `The final sentence proposes the displayed equality condition after “it seems to me that this shuold be”; the typographical transposition is retained in reading.tex.`

### Actually performed mathematical check

**003-R2-M01 — targeted proof check.** Conditional arithmetic check only: if n_i and n_i-prime are positive integers and n_i-prime=m_i*n_i with each m_i a positive integer, then n_i-prime>=n_i because m_i>=1. Conversely 3>=2 does not imply that 3 is a positive integral multiple of 2. Thus the two written forms can differ under this componentwise interpretation. Positivity of n_i and the componentwise interpretation are explicit assumptions of this check, not facts established on this page. This does not verify the intended Hom criterion, uniqueness of extra structure, commuting actions, or full faithfulness.

All other covering-theory and categorical statements are unverified background quoted from the page. Visual verification of a symbol was not counted as a mathematical proof.

### Reading decisions

- Every agreed formula was inspected, including the individual underlines and the plain typed capitals. No double-struck alphabet is visible.

- The g-shaped handwritten group letter is not promoted to a definite calligraphic capital on contextual grounds.

- The Hom subscript remains s/S; its prime is visible and secure.

- The handwritten inequality has a slanted lower stroke, so reading.tex uses geqslant. This is a graphic distinction only.

- The product separator is a typed baseline period and is retained as a period.

- Both indices in the final family are i, and the terminal set letter is I. The handwritten membership sign is retained.

- The conditional arithmetic comparison in event 003-R2-M01 was actually checked; no categorical or geometric assertion about the coverings was verified.

- Prior-question slips apparantly, then, definition, sheme, shuold with the transposition curve, and a a were each confirmed from the image and retained.

- The newly found developped spelling and e/i overstrike in giving are ink decisions. Neither is a mathematical emendation.

### Dates and page identifiers

- No manuscript title or signature appears on this page.

- Typed place/date: Voorschoten, May 16 1967.

- Typed address: Palestrinalaan 11.

- Pencilled bottom-left 2 is recorded as an archive sheet number comment; no author page-number macro is introduced.

## Points for main-reader adjudication

The two-loop group glyph, Hom subscript case, and all overlapping-letter correction orders require the main reader’s decision if a unique reading is desired. The e/i overstrike in giving is absent from both drafts and should receive particular attention. The isolated brown lower mark is recorded conservatively; its textual status cannot be proved from this page. The developped spelling and slanted inequality stroke are visually clear.

## Brief feedback

- No separate PREAMBLE file occurs among the six permitted packet inputs; I used the existing C macros and standard TikZ, without introducing custom notation macros.

- The meaning of marked_in_H is not defined in the brief. I set it true only for the insertion corresponding with, which H explicitly comments on; H’s ordinary emphasis commands were not treated as uncertainty flags.

Structured details are in [report.json](report.json); every reported coordinate refers to the whole image.
