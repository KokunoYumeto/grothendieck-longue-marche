# Independent reading R1 — cote 29, scan 003

## Scope and result

Complete diplomatic text: [reading.tex](reading.tex). The structured evidence, with exact whole-image bounding boxes, is in [report.json](report.json).

This run records **26 discrepancy rows**, **7 prior C doubts** (one resolved, six retained), and **7 remaining doubts** after adding the initial-case question in the margin insertion. The S packet was empty, so there are no S rows. There are no displayed equations, diagrams, letterhead, title, or signature on this page; its formulas are inline.

## Source views and crop count

The whole image was viewed once for layout, then half a once and half b once in that order. Eleven tight crops were created and each viewed once: **3 supplied source views + 11 crop views = 14 image views**. No source was re-viewed, no place was recropped, and no OCR or outside source was used. Half b begins at whole-image y = 938. All boxes below and in the JSON are in the 1674 × 2037 whole-image coordinate system.

Each crop has adjacent JSON metadata recording the source box, 2400-pixel output width, LANCZOS scaling, autocontrast, and sharpening. The margin insertion crop was rotated +4°; all other crops were unrotated. The first clock sample was obtained after the source views; the JSON makes this timing limit explicit.

## Reading and material state

The top-right address reads “Voorschoten, May 16 1967.” and “Palestrinalaan 11.” on separate lines. The salutation is “Dear Grothendieck,”. Three typed paragraphs occupy the page. Blue handwriting supplies several mathematical glyphs, punctuation, a missing i in variations, the margin insertion linked before X, deletions, and a transposition mark over the typed shuold. A short isolated brown mark below the text is retained with uncertainty. The pencil 2 at the lower left is recorded only as an archive-sheet comment.

The reading keeps the actual slips apparantly, information then, unaccented definition, sheme, typed shuold with its correction, and is a a set. It retains the separate underlines on r, s, a, n, and m; the underlined exponent R in Rev; the handwritten mu; the small s/S-prime Hom subscript; and the baseline period in m.n. The word couples has one underline. The ellipsis sequences are four/five/four/five points at the four positions documented below.

Paragraph 1 asks whether the new setup should be understood through the behaviour of a covering over special coverings s(M), with Abhyankar's lemma as background. Paragraph 2 asks about uniqueness of extra structure for Galois coverings, commutation of the group actions, and a fully faithful geometric-realization functor. Paragraph 3 asks whether the objects in example 3a are couples and proposes n'=m.n with positive integer coordinates for m. These are a description of the letter's questions, not claims proved in this reading.

## Every discrepancy

### R1-003-01 — Paragraph 1: purpose you developed things

- C: `developed`
- H: `developped`
- Reading: `developed`
- Difference against C: False; against H: True. Kind: misread word. Confidence: high.
- Evidence: Half a: one p, with a single descender, between o and e; there is no second p position.
- Whole-image box: [1124, 339, 1341, 384]. Evidence crop: none; source half identified above.

### R1-003-02 — Paragraph 1: giving directly the covering r(X)

- C: `$\underline{r}(X)$`
- H: `$r(X)$`
- Reading: `$\underline{r}(X)$`
- Difference against C: False; against H: True. Kind: misread symbol or index. Confidence: high.
- Evidence: Half a: a short distinct horizontal rule sits below the lowercase r, before the opening parenthesis.
- Whole-image box: [169, 544, 258, 586]. Evidence crop: none; source half identified above.

### R1-003-03 — Paragraph 1: behaviour over ... these

- C: `\unsure{a\deleted{l}al|a\deleted{a}ll}`
- H: `all`
- Reading: `\unsure{a\deleted{l}al|a\deleted{a}ll}`
- Difference against C: False; against H: True. Kind: deletion state (struck given live or live given struck). Confidence: medium.
- Evidence: Crop 01: first a and last l are separate; the middle type position contains both the bowl/crosspiece of a and the ascender/foot of l. The visible overstrike is preserved, but its order cannot be established.
- Whole-image box: [780, 645, 849, 680]. Evidence crop: 01_aal_then.png.

### R1-003-04 — Paragraph 1: better information then

- C: `then`
- H: `than`
- Reading: `then`
- Difference against C: False; against H: True. Kind: misread word. Confidence: high.
- Evidence: Crop 01: the vowel has the open e form and central horizontal stroke; it is retained as then.
- Whole-image box: [419, 692, 507, 731]. Evidence crop: 01_aal_then.png.

### R1-003-05 — Paragraph 1: the r(X) alone

- C: `$\underline{r}(X)$`
- H: `$r(X)$`
- Reading: `$\underline{r}(X)$`
- Difference against C: False; against H: True. Kind: misread symbol or index. Confidence: high.
- Evidence: Half a and crop 01: the r has a clear separate underline. The crop also includes the unchanged X and parentheses.
- Whole-image box: [599, 693, 685, 735]. Evidence crop: 01_aal_then.png.

### R1-003-06 — Paragraph 2: some variations

- C: `var\inserted{\handwritten{i}}ations`
- H: `variations`
- Reading: `var\inserted{\handwritten{i}}ations`
- Difference against C: False; against H: True. Kind: insertion or placement. Confidence: high.
- Evidence: Half a: the typewritten sequence is varations, with a small blue i placed above the gap after r. H reads the corrected word without retaining the actual insertion.
- Whole-image box: [1460, 885, 1645, 936]. Evidence crop: none; source half identified above.

### R1-003-07 — Paragraph 2 French quotation: la definition

- C: `definition`
- H: `définition`
- Reading: `definition`
- Difference against C: False; against H: True. Kind: abbreviation expanded or spelling modernised. Confidence: high.
- Evidence: Half a: the first e has no acute accent above it; the neighbouring grave accent on à and the circumflex of revêtements remain visibly distinguishable.
- Whole-image box: [517, 985, 736, 1027]. Evidence crop: none; source half identified above.

### R1-003-08 — Paragraph 2: typographic state of French quotation

- C: `On peut enfin l'expliciter en revenant à la definition de $\mathrm{Rev}^{\underline{R}}(S)$, et en exigeant que les revêtements des $\underline{s}(M)$ correspondants à $X$ soient principaux de groupe $G$.`
- H: `\emph{On peut enfin l'expliciter en revenant à la définition
de $\mathrm{Rev}^{\underline{R}}(S)$, et en exigeant que les revêtements des
$\underline{s}(M)$ correspondants à $X$ soient principaux de groupe $G$.}`
- Reading: `On peut enfin l'expliciter en revenant à la definition de $\mathrm{Rev}^{\underline{R}}(S)$, et en exigeant que les revêtements des $\underline{s}(M)$ correspondants à $X$ soient principaux de groupe $G$.`
- Difference against C: False; against H: True. Kind: other. Confidence: high.
- Evidence: Half a: the French quotation uses the same upright typewriter forms and baseline as its English surroundings; there is no underline or other emphasis mark enclosing this quotation.
- Whole-image box: [171, 943, 1607, 1082]. Evidence crop: none; source half identified above.

### R1-003-09 — Paragraph 2: a group ... working on Z

- C: `\handwritten{\unsure{\mathfrak{g}|g|\mathscr{G}}}`
- H: `\mathcal{G}`
- Reading: `\handwritten{\unsure{\mathfrak{g}|g|\mathscr{G}}}`
- Difference against C: False; against H: True. Kind: misread symbol or index. Confidence: medium.
- Evidence: Crop 02: the blue glyph has a small upper loop with a right overhang and a descending stem ending in a second loop. These are compatible with a handwritten g/fraktur g and less securely with a script G; the page supplies no decisive alphabet key.
- Whole-image box: [782, 1143, 820, 1188]. Evidence crop: 02_group_letters.png.
- Mathematical note: The group is not renamed on contextual grounds.

### R1-003-10 — Paragraph 2: insertion between covering and X

- C: `\inserted{\handwritten{corresponding with}}`
- H: `\marginal{corresponding with}`
- Reading: `\inserted{\handwritten{\unsure{Corresponding|corresponding} with}}`
- Difference against C: True; against H: True. Kind: insertion or placement. Confidence: medium.
- Evidence: Crop 03 reads the two margin lines as Corresponding / with. The initial open C rises substantially above the following o/r forms, favouring a capital but allowing a large initial lowercase. A looped insertion sign above the margin wording matches the sign between covering and X at whole-image [727,1180,746,1228] (half b; also crop 02). Thus the words belong at that insertion point. H acknowledges the pointer in its editorial note but leaves the text as a separate marginal item.
- Whole-image box: [18, 1130, 170, 1281]. Evidence crop: 03_corresponding_with.png.

### R1-003-11 — Paragraph 2: actions of G and ... commute

- C: `\handwritten{\mathfrak{g}}`
- H: `\mathcal{G}`
- Reading: `\handwritten{\mathfrak{g}}`
- Difference against C: False; against H: True. Kind: misread symbol or index. Confidence: medium.
- Evidence: Crop 02: the second blue glyph repeats the upper loop, right stem and lower loop of the first. The first-occurrence uncertainty governs this repetition.
- Whole-image box: [708, 1241, 744, 1286]. Evidence crop: 02_group_letters.png.

### R1-003-12 — Paragraph 2: your letter you explain/explaim

- C: `\unsure{explai\deleted{n}m|explai\deleted{m}n}`
- H: `explain`
- Reading: `\unsure{explai\deleted{n}m|explai\deleted{m}n}`
- Difference against C: False; against H: True. Kind: deletion state (struck given live or live given struck). Confidence: medium.
- Evidence: Crop 04: the final type position is congested, with superposed vertical strokes and arches compatible with n and m. A dark blue reinforcement is visible. The image does not establish a unique correction order, so neither a clean explain nor a clean explaim is asserted.
- Whole-image box: [929, 1291, 1078, 1334]. Evidence crop: 04_explain_overstrike.png.

### R1-003-13 — Paragraph 2: important point [cancelled character] if

- C: `\deleted{\unsure{f|i}}`
- H: `omitted`
- Reading: `\deleted{f}`
- Difference against C: True; against H: True. Kind: omission. Confidence: high.
- Evidence: Crop 05: beneath the blue cancellation there is a typed ascender with a right-hooked top, a mid-height horizontal crossbar, and a baseline foot. This is f; it is not merely the stem and dot of i. The cancellation state is definite.
- Whole-image box: [826, 1491, 855, 1526]. Evidence crop: 05_point_if_one.png.

### R1-003-14 — Paragraph 2: if one/wne wants

- C: `\unsure{\deleted{o}wne|\deleted{w}one}`
- H: `one`
- Reading: `\unsure{\deleted{o}wne|\deleted{w}one}`
- Difference against C: False; against H: True. Kind: deletion state (struck given live or live given struck). Confidence: medium.
- Evidence: Crop 05: the first position contains the closed oval of o together with the internal diagonals/stems of w; ne is clear. The order of the two impressions cannot be recovered from these black strokes.
- Whole-image box: [929, 1495, 998, 1529]. Evidence crop: 05_point_if_one.png.

### R1-003-15 — Paragraph 2 end: what is going on!

- C: `going on\handwritten{!}).`
- H: `going on).`
- Reading: `going on\handwritten{!}).`
- Difference against C: False; against H: True. Kind: omission. Confidence: high.
- Evidence: Half b: a tall blue vertical stroke followed by a small lower mark occurs immediately before the typed closing parenthesis; this is an inserted exclamation mark.
- Whole-image box: [1563, 1476, 1641, 1535]. Evidence crop: none; source half identified above.

### R1-003-16 — Paragraph 3: consist[s] out of

- C: `consist\deleted{s}`
- H: `consist`
- Reading: `consist\deleted{s}`
- Difference against C: False; against H: True. Kind: omission. Confidence: high.
- Evidence: Half b: the typed final s remains visible and has a diagonal pen stroke through it; the earlier letters consist are live.
- Whole-image box: [950, 1637, 1123, 1676]. Evidence crop: none; source half identified above.

### R1-003-17 — Paragraph 3: couples

- C: `\uline{couples}`
- H: `\emph{couples}`
- Reading: `\uline{couples}`
- Difference against C: False; against H: True. Kind: other. Confidence: high.
- Evidence: Crop 10: there is one continuous thick horizontal underline under the upright word couples. It is a single rule, not double underlining and not italic type.
- Whole-image box: [1275, 1637, 1432, 1683]. Evidence crop: 10_couples_underline.png.

### R1-003-18 — Paragraph 3: Hom subscript

- C: `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}`
- H: `\mathrm{Hom}_{S'}`
- Reading: `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}`
- Difference against C: False; against H: True. Kind: misread symbol or index. Confidence: medium.
- Evidence: Crop 06: the hand-added subscript is a small open S-shaped curve, followed at its upper right by a separate prime mark. Its size does not securely distinguish lowercase s from reduced capital S.
- Whole-image box: [1155, 1714, 1187, 1747]. Evidence crop: 06_hom_subscript.png.

### R1-003-19 — Paragraph 3: n prime relation n

- C: `\underline{n}'\handwritten{\geq}\underline{n}`
- H: `\underline{n}' \geqslant \underline{n}`
- Reading: `\underline{n}'\handwritten{\geqslant}\underline{n}`
- Difference against C: True; against H: False. Kind: other. Confidence: high.
- Evidence: Crop 07: the blue sign consists of a right-pointing angle and a separate lower diagonal rising to the right. The lower stroke is slanted, so geqslant records its shape more closely than geq.
- Whole-image box: [386, 1745, 415, 1785]. Evidence crop: 07_relation.png.
- Mathematical note: This is a glyph-shape distinction; it does not change the inequality direction or meaning.

### R1-003-20 — Paragraph 3: first auquel cas ... etc ...

- C: `auquel cas....etc.....,`
- H: `auquel cas…etc…`
- Reading: `auquel cas....etc.....,`
- Difference against C: False; against H: True. Kind: misread symbol or index. Confidence: high.
- Evidence: Crop 09: there are four typed periods after the first cas and five after etc, followed by a comma. The individual points are separated and countable.
- Whole-image box: [708, 1750, 974, 1787]. Evidence crop: 09_ellipsis.png.

### R1-003-21 — Paragraph 3: shuold with transposition mark

- C: `sh\handwritten{\tikz[overlay,baseline]{\draw[line width=.4pt] (0,-.02) .. controls (.08,.23) and (.17,.25) .. (.20,.06) .. controls (.22,-.12) and (.36,-.15) .. (.39,-.02);}}uold`
- H: `should`
- Reading: `sh\handwritten{\tikz[overlay,baseline]{\draw[line width=.4pt] (0,-.02) .. controls (.08,.23) and (.17,.25) .. (.20,.06) .. controls (.22,-.12) and (.36,-.15) .. (.39,-.02);}}uold`
- Difference against C: False; against H: True. Kind: insertion or placement. Confidence: high.
- Evidence: Crop 08: the typed letters are s h u o l d. A blue connected mark rises over u and falls/curves below o, indicating transposition. Both the typed error and the correction mark are retained.
- Whole-image box: [1500, 1746, 1630, 1792]. Evidence crop: 08_transposition.png.

### R1-003-22 — Paragraph 3: second sauf si quotation ellipses

- C: `....sauf si $\underline{n}'=\underline{m}.\underline{n}$, auquel cas.....`
- H: `…\emph{sauf si $\underline{n}' = \underline{m}\cdot\underline{n}$, auquel
cas…}`
- Reading: `....sauf si $\underline{n}'=\underline{m}.\underline{n}$, auquel cas.....`
- Difference against C: False; against H: True. Kind: misread symbol or index. Confidence: high.
- Evidence: Half b: four separate points precede sauf si. Crop 09: five separate points follow the second cas. They are not reduced to a conventional three-dot ellipsis. The second French quotation is upright type; H also adds emphasis absent from the page.
- Whole-image box: [237, 1788, 999, 1838]. Evidence crop: 09_ellipsis.png.

### R1-003-23 — Paragraph 3: product m.n

- C: `\underline{m}.\underline{n}`
- H: `\underline{m}\cdot\underline{n}`
- Reading: `\underline{m}.\underline{n}`
- Difference against C: False; against H: True. Kind: misread symbol or index. Confidence: high.
- Evidence: Half b: the point between the underlined m and n sits at the typewriter baseline, at the same level as adjacent full stops, not at the midline of a centred multiplication dot.
- Whole-image box: [565, 1797, 632, 1835]. Evidence crop: none; source half identified above.
- Mathematical note: The baseline punctuation is retained without changing the author's apparent multiplication intention.

### R1-003-24 — Paragraph 3 final line: is a a set

- C: `is a a set`
- H: `is a set`
- Reading: `is a a set`
- Difference against C: False; against H: True. Kind: omission. Confidence: high.
- Evidence: Half b: the penultimate line ends is a, and the final line begins a set. Both a tokens are present; they are separated only by the original line break.
- Whole-image box: [172, 1795, 1597, 1880]. Evidence crop: none; source half identified above.

### R1-003-25 — Bottom margin: isolated short mark

- C: `\margin{\handwritten{\unsure{,|'}}}`
- H: `omitted`
- Reading: `\margin{\handwritten{\unsure{,|'}}}`
- Difference against C: False; against H: True. Kind: omission. Confidence: low.
- Evidence: Crop 11: there is an isolated brown, roughly comma-shaped two-part stroke under the final line. With no baseline or adjacent words, comma versus apostrophe cannot be resolved, nor can an incidental mark be excluded.
- Whole-image box: [454, 1900, 469, 1924]. Evidence crop: 11_bottom_mark.png.

### R1-003-26 — Paragraph 3: typographic state of first French quotation

- C: `$\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}(M',M)$ est vide sauf si $\underline{n}'\handwritten{\geq}\underline{n}$, auquel cas....etc.....,`
- H: `\emph{$\mathrm{Hom}_{S'}(M',M)$ est vide sauf si $\underline{n}' \geqslant
\underline{n}$, auquel cas…etc…}`
- Reading: `$\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}(M',M)$ est vide sauf si $\underline{n}'\handwritten{\geqslant}\underline{n}$, auquel cas....etc.....,`
- Difference against C: False; against H: True. Kind: other. Confidence: high.
- Evidence: Half b: the first quoted French clause has the same upright typewriter letterforms as the surrounding English. It has no underline or other emphasis mark. The individual handwritten mathematical additions are retained in reading.tex.
- Whole-image box: [174, 1690, 1499, 1839]. Evidence crop: none; source half identified above.

## Every prior C doubt

- **Paragraph 1: apparantly ... these — retained:** `\unsure{a\deleted{l}al|a\deleted{a}ll}`. Crop 01 confirms a/l superposition in the middle slot; no impression order is recoverable. Box [780, 645, 849, 680]; crop `01_aal_then.png`.
- **Paragraph 2: group on Z — retained:** `\unsure{\mathfrak{g}|g|\mathscr{G}}`. Crop 02 shows two loops linked by a descending right stem. The same form recurs in the commuting-actions clause; no alphabet key appears on this page. Box [782, 1143, 820, 1188]; crop `02_group_letters.png`.
- **Paragraph 2: you explaim/explain — retained:** `\unsure{explai\deleted{n}m|explai\deleted{m}n}`. Crop 04 shows superposed final arches/stems with dark blue reinforcement; the order cannot be established. Box [929, 1291, 1078, 1334]; crop `04_explain_overstrike.png`.
- **Paragraph 2: point ... if — resolved:** `\deleted{f}`. Crop 05 exposes the hooked ascender and mid-height crossbar of typed f beneath a blue deletion. Box [826, 1491, 855, 1526]; crop `05_point_if_one.png`.
- **Paragraph 2: if ... wants — retained:** `\unsure{\deleted{o}wne|\deleted{w}one}`. Crop 05 shows both an oval and w-like internal strokes in the first type position. Box [929, 1495, 998, 1529]; crop `05_point_if_one.png`.
- **Paragraph 3: Hom subscript — retained:** `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}`. Crop 06 confirms an S-shaped handwritten subscript and separate prime; size alone cannot settle case. Box [1155, 1714, 1187, 1747]; crop `06_hom_subscript.png`.
- **Bottom isolated mark — retained:** `\margin{\handwritten{\unsure{,|'}}}`. Crop 11 shows a short brown segmented stroke, with no textual baseline. An incidental physical mark remains possible. Box [454, 1900, 469, 1924]; crop `11_bottom_mark.png`.

## Remaining doubts and adjudication points

- **Paragraph 1: apparantly ... these:** `\unsure{a\deleted{l}al|a\deleted{a}ll}` (medium). Crop 01 confirms a/l superposition in the middle slot; no impression order is recoverable.
- **Paragraph 2: group on Z:** `\unsure{\mathfrak{g}|g|\mathscr{G}}` (medium). Crop 02 shows two loops linked by a descending right stem. The same form recurs in the commuting-actions clause; no alphabet key appears on this page.
- **Paragraph 2 margin insertion: initial letter of Corresponding:** `\unsure{Corresponding|corresponding} with` (medium). Crop 03 shows a large initial open C rising above following small letters, but an enlarged initial lowercase c cannot be excluded. The word and insertion point are secure.
- **Paragraph 2: you explaim/explain:** `\unsure{explai\deleted{n}m|explai\deleted{m}n}` (medium). Crop 04 shows superposed final arches/stems with dark blue reinforcement; the order cannot be established.
- **Paragraph 2: if ... wants:** `\unsure{\deleted{o}wne|\deleted{w}one}` (medium). Crop 05 shows both an oval and w-like internal strokes in the first type position.
- **Paragraph 3: Hom subscript:** `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}` (medium). Crop 06 confirms an S-shaped handwritten subscript and separate prime; size alone cannot settle case.
- **Bottom isolated mark:** `\margin{\handwritten{\unsure{,|'}}}` (low). Crop 11 shows a short brown segmented stroke, with no textual baseline. An incidental physical mark remains possible.

The material new issue for adjudication is the large initial C/c in the inserted Corresponding with. The insertion wording and anchor are secure. The other unresolved matters are visible overstrike order, handwritten alphabet/case, and the isolated bottom mark. The cancelled letter before if is read as f after enlargement. The change from geq to geqslant is graphic, not semantic.

## Inventory

- **E01 — text, typewriter; top right, [982,74,1500,160]:** Voorschoten, May 16 1967. / Palestrinalaan 11. Transcribed: yes.
- **E02 — text, typewriter; upper left, [168,198,537,232]:** Dear Grothendieck, Transcribed: yes.
- **E03 — text, typewriter; paragraph 1, [169,246,1640,780]:** I am trying to work out your letter with indications. ... new set-up? Transcribed: yes.
- **E04 — deletion, typewriter; paragraph 1, [780,645,849,680]:** Overtyped a/l in the middle of aal/all; cancelled impression order uncertain. Transcribed: yes.
- **E05 — insertion, typewriter; paragraph 1, same position:** Replacement a/l impression; order uncertain. Transcribed: yes.
- **E06 — insertion, unnamed other hand; paragraph 1 end, [906,730,932,775]:** ? Transcribed: yes.
- **E07 — text, typewriter; paragraph 2, [172,793,1643,1538]:** My main difficulty is that ... what is going on! Transcribed: yes.
- **E08 — insertion, unnamed other hand; above varations, [1514,886,1533,913]:** i Transcribed: yes.
- **E09 — insertion, unnamed other hand; French quotation, over a at [417,986,434,1006]:** Grave accent on à in en revenant à; encoded as à. Transcribed: yes.
- **E10 — insertion, unnamed other hand; French quotation, over a at [786,1040,806,1061]:** Grave accent on à in correspondants à; encoded as à. Transcribed: yes.
- **E11 — insertion, unnamed other hand; paragraph 2, [782,1143,820,1188]:** g/fraktur g/script G Transcribed: yes.
- **E12 — insertion, unnamed other hand; left margin [18,1130,170,1281], linked before X [727,1180,746,1228]:** Corresponding / with, with matching looped insertion signs Transcribed: yes.
- **E13 — insertion, unnamed other hand; paragraph 2, [708,1241,744,1286]:** Repeated handwritten group letter Transcribed: yes.
- **E14 — insertion, unnamed other hand; paragraph 2, [1258,1230,1280,1276]:** ? after correct Transcribed: yes.
- **E15 — deletion, typewriter / unnamed other hand; paragraph 2, [929,1291,1078,1334]:** n/m overstrike at the end of explai-; order uncertain. Transcribed: yes.
- **E16 — insertion, typewriter / unnamed other hand; paragraph 2, same position:** n/m replacement with dark blue reinforcement; order uncertain. Transcribed: yes.
- **E17 — deletion, typewriter; paragraph 2, [438,1446,550,1479]:** makes, cancelled by typed crossing strokes Transcribed: yes.
- **E18 — deletion, typewriter / unnamed other hand; paragraph 2, [826,1491,855,1526]:** f, crossed with blue pen Transcribed: yes.
- **E19 — deletion, typewriter; paragraph 2, [929,1495,998,1529]:** o/w in the first position before ne; impression order uncertain. Transcribed: yes.
- **E20 — insertion, typewriter; paragraph 2, same position:** w/o replacement impression; order uncertain. Transcribed: yes.
- **E21 — insertion, unnamed other hand; paragraph 2 end, [1599,1476,1617,1525]:** ! Transcribed: yes.
- **E22 — text, typewriter; paragraph 3, [173,1543,1643,1884]:** Some other points: ... a a set of positive integers. Inline formulas; couples singly underlined. Transcribed: yes.
- **E23 — deletion, typewriter; paragraph 3, [869,1590,1306,1631]:** with this formulation, crossed with repeated typed x impressions Transcribed: yes.
- **E24 — deletion, typewriter / unnamed other hand; paragraph 3, [1093,1640,1121,1674]:** Final s of consists, crossed by pen Transcribed: yes.
- **E25 — insertion, unnamed other hand; paragraph 3, [621,1685,667,1729]:** mu in G(M)=mu_n Transcribed: yes.
- **E26 — insertion, unnamed other hand; paragraph 3, [722,1671,749,1722]:** ? after G(M)=mu_n Transcribed: yes.
- **E27 — insertion, unnamed other hand; paragraph 3, [1155,1714,1187,1747]:** s/S prime, subscript to Hom Transcribed: yes.
- **E28 — insertion, unnamed other hand; paragraph 3, [386,1745,415,1785]:** Slanted greater-than-or-equal sign Transcribed: yes.
- **E29 — insertion, unnamed other hand; paragraph 3, [1539,1747,1583,1789]:** Transposition mark crossing u/o in shuold; reproduced as inline TikZ. Transcribed: yes.
- **E30 — insertion, unnamed other hand; paragraph 3, [1460,1821,1481,1846]:** Membership sign between subscript i and I Transcribed: yes.
- **E31 — margin note, unnamed other hand; below last text line, [454,1900,469,1924]:** Isolated comma/apostrophe-like brown mark; status uncertain. Transcribed: yes.
- **E32 — text, unnamed other hand; bottom left, [31,1985,59,2015]:** Archive sheet number 2; transcribed only as a comment. Transcribed: yes.

## Notation and prior notation questions

- **Paragraph 1, both r(X) occurrences; paragraph 2 geometric realization:** Lowercase typed r with a short underline. Encoding: `\underline{r}(X);\ \underline{r}`. None; H loses the two paragraph-1 underlines.
- **Paragraphs 1 and 2, s(M):** Lowercase typed s with a short underline; ordinary M. Encoding: `\underline{s}(M)`. None.
- **Paragraph 2 French quotation:** Rev has no accent; its raised single-struck R has an underline; ordinary S in parentheses. Encoding: `\mathrm{Rev}^{\underline{R}}(S)`. None. All capitals inspected individually; no doubled letter introduced.
- **Paragraph 2, group on Z and commuting actions:** Blue double-looped descending glyph. Encoding: `\unsure{\mathfrak{g}|g|\mathscr{G}}`. Alphabet/case unresolved. First candidate repeated at second occurrence.
- **Paragraph 3, couple and final formulas:** a,n,m each have their own short underline; mu is handwritten. Encoding: `M=(\underline{a},\underline{n});\ G(M)=\mu_{\underline{n}};\ \underline{n}'=\underline{m}.\underline{n}`. None in the vector underlines or mu.
- **Paragraph 3, Hom:** Upright typed Hom; small blue S-shaped subscript plus distinct prime. Encoding: `\mathrm{Hom}_{\unsure{s|S}'}(M',M)`. s versus reduced S unresolved.
- **Paragraph 3, first condition:** Right-pointing blue angle plus lower rising diagonal. Encoding: `\underline{n}'\geqslant\underline{n}`. None; inequality direction and lower stroke are clear.
- **Paragraph 3, second condition:** Typed prime after underlined n; baseline point between underlined m and n. Encoding: `\underline{n}'=\underline{m}.\underline{n}`. None. Baseline point is not silently raised.
- **Paragraph 3, last tuple:** Both small indexed letters are i, with dots and no descending j stroke; the final I is a capital. Membership sign is hand-added. Encoding: `\underline{m}=(m_i)_{i\in I}`. None from half b.
- **Paragraph 1 quotation:** Two separate quote strokes at each side of behaviour. Encoding: ```behaviour''`. None.
- **Paragraphs 1–3 formula capitals:** X,S,M,G,Z,I,R and H in Hom are ordinary typewriter capitals, each individually inspected. Encoding: `X,S,M,G,Z,I;\mathrm{Rev};\mathrm{Hom}`. No candidate double strike found; handwritten group letter is treated separately.
- **Paragraph 3, couples:** Upright letters and one horizontal underline. Encoding: `\uline{couples}`. Single underline resolved by crop 10.
- **Paragraph 3, ellipses:** First cas: four points; etc: five points; before second sauf: four points; final cas: five points. Encoding: `cas....etc....., ... ....sauf si ... cas.....`. None after crop 09 and half b.

## Abbreviations

- `etc`: et cetera; this expansion is explanatory only and does not replace the printed abbreviation.

## Mathematical checks and limits

For the one-coordinate positive-integer example n=2, n'=3, n'>=n holds but n'=m n has no positive-integer solution because 3/2 is not an integer. Thus, if the inequality is interpreted componentwise, it is weaker than the displayed divisibility condition. This checks only the distinction between the formulas; it does not verify the Hom assertion or the unavailable definition of example 3a.

No independent proof was attempted for the Galois-covering, commutation, full-faithfulness, or Hom claims. All authorial questions listed in the structured report remain questions. A visual verification of symbols is not counted as a proof check.

## Brief feedback

- The brief references an attached PREAMBLE, but no PREAMBLE definition is among the permitted input files. I used the macros already present in C and standard LaTeX/TikZ.
- The transposition symbol is an inline correction mark, not a separate figure; I preserved its inline TikZ representation so the typed shuold and its correction remain in position.
- The semantics of marked_in_H are not explicitly defined. It is true only for the insertion phrase that H explicitly records as marginal and discusses in its note; no H uncertainty macro appears in the other disputed readings.
