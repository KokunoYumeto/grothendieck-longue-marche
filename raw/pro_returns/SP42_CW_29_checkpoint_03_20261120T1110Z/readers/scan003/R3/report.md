# Scan 003 — independent reader R3

## Reading and viewing record

The complete diplomatic reading is in `reading.tex`; `report.json` contains the structured findings and whole-image coordinates. The source image is 1674 × 2037 pixels. Half a is 1674 × 1098 pixels; half b is 1674 × 1099 pixels, corresponding to a lower-half origin of y = 938.

**Actual views:** one whole-image view for layout, one view of half a, one view of half b, and eleven crop views. Each source/crop was viewed once. No OCR, external research, other page, other reader, or shared deliverable was inspected. All eleven crops were made from the original image at 2400 pixels wide using LANCZOS enlargement, autocontrast and sharpening; each has a companion JSON recording its box and transformations. No rotation was needed.

**Outcome:** 27 difference records; 2 against C and 25 against H. Seven C doubts were all inspected and remain explicitly marked. S was empty. There are no mathematical proof-check events.

The substantive word correction to C is **developped**, with two p characters. A separate glyph-shape correction uses `\geqslant` for the visibly slanted lower bar. All overtyping orders, the group alphabet, Hom-subscript case and the isolated bottom mark remain uncertain where the ink does not decide them. The transposition drawing is carried into the required `\figure{\begin{tikzpicture}...}` form; this macro-only change is not counted as a discrepancy against C.

## Discrepancies

### R3-003-01: Paragraph 1, for what purpose you ... things

- **C:** `developed`
- **H:** `developped`
- **R3:** `developped`
- **Difference:** misread word; against C: True; against H: False; confidence: high.
- **Evidence:** Crop 01 shows two complete, separately spaced p letters, each with its own stem, bowl and descender, between develo and ed.
- **Whole-image box:** `[1125, 345, 1335, 380]`; crop: `crops/01_developed.png`.

### R3-003-02: Paragraph 1, first covering r(X)

- **C:** `\underline{r}(X)`
- **H:** `r(X)`
- **R3:** `\underline{r}(X)`
- **Difference:** omission; against C: False; against H: True; confidence: high.
- **Evidence:** Half a shows a short black horizontal rule immediately below the r, separate from its baseline serif.
- **Whole-image box:** `[171, 545, 254, 584]`; crop: `None`.

### R3-003-03: Paragraph 1, apparantly ... these

- **C:** `\unsure{a\deleted{l}al|a\deleted{a}ll}`
- **H:** `all`
- **R3:** `\unsure{a\deleted{l}al|a\deleted{a}ll}`
- **Difference:** deletion state (struck given live or live given struck); against C: False; against H: True; confidence: medium.
- **Evidence:** Crop 02 shows plain initial a, one middle position containing both a closed a bowl and the tall l stroke, then a separate final l. The order of the two impressions in the middle position is not recoverable.
- **Whole-image box:** `[781, 645, 847, 678]`; crop: `crops/02_all_overtyping.png`.

### R3-003-04: Paragraph 1, gives better information ... the r(X)

- **C:** `then`
- **H:** `than`
- **R3:** `then`
- **Difference:** misread word; against C: False; against H: True; confidence: high.
- **Evidence:** Half a shows the vowel with an open right side and horizontal middle stroke: e, not the closed a bowl elsewhere in the line.
- **Whole-image box:** `[417, 696, 501, 727]`; crop: `None`.

### R3-003-05: Paragraph 1, the r(X) alone

- **C:** `\underline{r}(X)`
- **H:** `r(X)`
- **R3:** `\underline{r}(X)`
- **Difference:** omission; against C: False; against H: True; confidence: high.
- **Evidence:** Half a shows a separate underline below the second r as well.
- **Whole-image box:** `[599, 695, 684, 733]`; crop: `None`.

### R3-003-06: Paragraph 2, abstract definition and some variations

- **C:** `var\inserted{\handwritten{i}}ations`
- **H:** `variations`
- **R3:** `var\inserted{\handwritten{i}}ations`
- **Difference:** insertion or placement; against C: False; against H: True; confidence: high.
- **Evidence:** Half a shows typed varations with a small blue i raised between the typed r and a; the correction is an addition, not an originally typed i.
- **Whole-image box:** `[1458, 888, 1642, 931]`; crop: `None`.

### R3-003-07: Paragraph 2, la definition de Rev

- **C:** `definition`
- **H:** `définition`
- **R3:** `definition`
- **Difference:** abbreviation expanded or spelling modernised; against C: False; against H: True; confidence: high.
- **Evidence:** Half a shows no acute stroke over the first e of definition. The nearby grave accents on à are visibly separate strokes, so the absent acute is not silently supplied.
- **Whole-image box:** `[519, 989, 732, 1022]`; crop: `None`.

### R3-003-08: Paragraph 2, French quotation On peut enfin ... groupe G

- **C:** `On peut enfin l'expliciter en revenant à la definition de $\mathrm{Rev}^{\underline{R}}(S)$, et en exigeant que les revêtements des $\underline{s}(M)$ correspondants à $X$ soient principaux de groupe $G$.`
- **H:** `\emph{On peut enfin l'expliciter en revenant à la définition de $\mathrm{Rev}^{\underline{R}}(S)$, et en exigeant que les revêtements des $\underline{s}(M)$ correspondants à $X$ soient principaux de groupe $G$.}`
- **R3:** `On peut enfin l'expliciter en revenant à la definition de $\mathrm{Rev}^{\underline{R}}(S)$, et en exigeant que les revêtements des $\underline{s}(M)$ correspondants à $X$ soient principaux de groupe $G$.`
- **Difference:** other; against C: False; against H: True; confidence: high.
- **Evidence:** Halves a and b show upright monospaced type throughout the French quotation, matching the surrounding English. There is no italic change or underline on this quotation.
- **Whole-image box:** `[172, 943, 1607, 1081]`; crop: `None`.

### R3-003-09: Paragraph 2, example 1 a group ... working on Z

- **C:** `\handwritten{\unsure{\mathfrak{g}|g|\mathscr{G}}}`
- **H:** `\mathcal{G}`
- **R3:** `\handwritten{\unsure{\mathfrak{g}|g|\mathscr{G}}}`
- **Difference:** misread symbol or index; against C: False; against H: True; confidence: medium.
- **Evidence:** Crop 03 shows a blue letter with two closed loops on the left of a near-vertical right stem, the lower loop descending below the line. This favors lowercase g or fraktur g; the handwriting alone does not provide a decisive alphabet key.
- **Whole-image box:** `[785, 1145, 818, 1185]`; crop: `crops/03_group_letter.png`.

### R3-003-10: Paragraph 2, Galois covering [insertion] X

- **C:** `covering \inserted{\handwritten{corresponding with}} $X$`
- **H:** `covering $X$`
- **R3:** `covering \inserted{\handwritten{corresponding with}} $X$`
- **Difference:** insertion or placement; against C: False; against H: True; confidence: high.
- **Evidence:** Half b shows the two handwritten words corresponding / with in the left margin. A pin-shaped mark there matches the blue pin between covering and X. H describes this target in its editorial note but leaves the words in a marginal position rather than at their insertion point.
- **Whole-image box:** `[24, 1144, 778, 1275]`; crop: `None`.

### R3-003-11: Paragraph 2, actions of G and ... commute

- **C:** `\handwritten{\mathfrak{g}}`
- **H:** `\mathcal{G}`
- **R3:** `\handwritten{\mathfrak{g}}`
- **Difference:** misread symbol or index; against C: False; against H: True; confidence: medium.
- **Evidence:** Half b shows the same two-loop descending blue g-form as the first occurrence. Following the recurring-sign rule, the first candidate is reused here and the alternatives are retained at the first occurrence.
- **Whole-image box:** `[708, 1245, 742, 1284]`; crop: `None`.

### R3-003-12: Paragraph 2, your letter you ... (for example 1)

- **C:** `\unsure{explai\deleted{n}m|explai\deleted{m}n}`
- **H:** `explain`
- **R3:** `\unsure{explai\deleted{n}m|explai\deleted{m}n}`
- **Difference:** deletion state (struck given live or live given struck); against C: False; against H: True; confidence: medium.
- **Evidence:** Crop 04 shows a crowded terminal cell with the outer strokes of n and the extra central stem of m. Both occupy the same position; the chronological order of strikes remains undecidable.
- **Whole-image box:** `[930, 1295, 1075, 1326]`; crop: `crops/04_explain_overtyping.png`.

### R3-003-13: Paragraph 2, important point [cancelled character] if

- **C:** `\deleted{\unsure{f|i}}`
- **H:** `omitted`
- **R3:** `\deleted{\unsure{f|i}}`
- **Difference:** omission; against C: False; against H: True; confidence: low.
- **Evidence:** Crop 05 shows a distinct typed character between point and if, crossed repeatedly in blue. A top hook and foot favor f; the crossings obscure enough of the stem that i is retained as a weaker candidate.
- **Whole-image box:** `[823, 1492, 856, 1524]`; crop: `crops/05_deleted_letter_and_one.png`.

### R3-003-14: Paragraph 2, if ... wants

- **C:** `\unsure{\deleted{o}wne|\deleted{w}one}`
- **H:** `one`
- **R3:** `\unsure{\deleted{o}wne|\deleted{w}one}`
- **Difference:** deletion state (struck given live or live given struck); against C: False; against H: True; confidence: medium.
- **Evidence:** Crop 05 shows both an oval o outline and pointed w strokes within the first letter position, followed by distinct n and e. No reliable layer order can be assigned.
- **Whole-image box:** `[929, 1496, 998, 1528]`; crop: `crops/05_deleted_letter_and_one.png`.

### R3-003-15: Paragraph 2, end of going on before right parenthesis

- **C:** `going on\handwritten{!}).`
- **H:** `going on).`
- **R3:** `going on\handwritten{!}).`
- **Difference:** omission; against C: False; against H: True; confidence: high.
- **Evidence:** Half b shows a tall blue exclamation stroke immediately after on and before the typed closing parenthesis, with its lower terminal/dot at the line.
- **Whole-image box:** `[1565, 1476, 1639, 1532]`; crop: `None`.

### R3-003-16: Paragraph 3, consist(s) out of couples

- **C:** `consist\deleted{s}`
- **H:** `consist`
- **R3:** `consist\deleted{s}`
- **Difference:** omission; against C: False; against H: True; confidence: high.
- **Evidence:** Half b shows a final typed s after consist, crossed through by a rising blue pen stroke. The cancelled letter remains visible.
- **Whole-image box:** `[951, 1637, 1120, 1673]`; crop: `None`.

### R3-003-17: Paragraph 3, couples

- **C:** `\uline{couples}`
- **H:** `\emph{couples}`
- **R3:** `\uline{couples}`
- **Difference:** other; against C: False; against H: True; confidence: high.
- **Evidence:** Half b shows upright typed couples with one continuous underline below the word; there is no italic type.
- **Whole-image box:** `[1276, 1641, 1428, 1680]`; crop: `None`.

### R3-003-18: Paragraph 3, Hom subscript

- **C:** `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}`
- **H:** `\mathrm{Hom}_{S'}`
- **R3:** `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}`
- **Difference:** misread symbol or index; against C: False; against H: True; confidence: medium.
- **Evidence:** Crop 06 shows a small blue S-shaped curve below Hom followed by a distinct raised prime. Its size and shape favor s, but the hand also permits a reduced capital S; a confident uppercase reading is not established by the strokes.
- **Whole-image box:** `[1090, 1686, 1186, 1748]`; crop: `crops/06_hom_subscript.png`.

### R3-003-19: Paragraph 3, n prime compared with n

- **C:** `\underline{n}'\handwritten{\geq}\underline{n}`
- **H:** `\underline{n}' \geqslant \underline{n}`
- **R3:** `\underline{n}'\handwritten{\geqslant}\underline{n}`
- **Difference:** other; against C: True; against H: False; confidence: high.
- **Evidence:** Crop 08 shows a blue greater-than chevron and a separate lower stroke parallel to the chevron’s lower arm. The lower stroke is slanted, so geqslant reproduces the visible shape more closely than the horizontal-bar geq.
- **Whole-image box:** `[388, 1745, 414, 1780]`; crop: `crops/08_inequality.png`.
- **Mathematical limit:** This is a glyph-shape distinction. Both drafts encode greater-than-or-equal; no stronger mathematical claim is inferred.

### R3-003-20: Paragraph 3, first auquel cas ... etc punctuation

- **C:** `auquel cas....etc.....`
- **H:** `auquel cas…etc…`
- **R3:** `auquel cas....etc.....`
- **Difference:** other; against C: False; against H: True; confidence: high.
- **Evidence:** Half b shows four separately typed periods between cas and etc, then five after etc. The source does not use single ellipsis glyphs.
- **Whole-image box:** `[499, 1745, 973, 1781]`; crop: `None`.

### R3-003-21: Paragraph 3, sh[u o]ld with handwritten transposition

- **C:** `sh\handwritten{\tikz[overlay,baseline]{\draw[line width=.4pt] (0,-.02) .. controls (.08,.23) and (.17,.25) .. (.20,.06) .. controls (.22,-.12) and (.36,-.15) .. (.39,-.02);}}uold`
- **H:** `should`
- **R3:** `sh\handwritten{\figure{\begin{tikzpicture}[overlay,baseline]\draw[line width=.4pt] (0,-.02) .. controls (.08,.23) and (.17,.25) .. (.20,.06) .. controls (.22,-.12) and (.36,-.15) .. (.39,-.02);\end{tikzpicture}}}uold`
- **Difference:** drawing or diagram; against C: False; against H: True; confidence: high.
- **Evidence:** Crop 09 shows the typed order s h u o l d. A blue stroke rises over u, falls between u and o, and curls below o: a transposition mark. The complete mark is approximated in TikZ in reading.tex, without silently reordering the typed letters.
- **Whole-image box:** `[1502, 1749, 1632, 1793]`; crop: `crops/09_transposition.png`.

### R3-003-22: Paragraph 3, proposed replacement quote punctuation

- **C:** `....sauf si $\underline{n}'=\underline{m}.\underline{n}$, auquel cas.....`
- **H:** `…\emph{sauf si $\underline{n}' = \underline{m}\cdot\underline{n}$, auquel cas…}`
- **R3:** `....sauf si $\underline{n}'=\underline{m}.\underline{n}$, auquel cas.....`
- **Difference:** other; against C: False; against H: True; confidence: high.
- **Evidence:** Half b shows four typed periods before sauf and five after the second cas. These visible runs are retained with their counts.
- **Whole-image box:** `[240, 1793, 992, 1833]`; crop: `None`.

### R3-003-23: Paragraph 3, product between underlined m and n

- **C:** `\underline{m}.\underline{n}`
- **H:** `\underline{m}\cdot\underline{n}`
- **R3:** `\underline{m}.\underline{n}`
- **Difference:** misread symbol or index; against C: False; against H: True; confidence: high.
- **Evidence:** Crop 11 shows the round period in the low typewriter period position, aligned near the letter feet, not raised to the mathematical midline. The surrounding m and n each have separate short underlines.
- **Whole-image box:** `[562, 1794, 632, 1832]`; crop: `crops/11_baseline_product.png`.

### R3-003-24: Paragraph 3, end of the sentence after the indexed family

- **C:** `is a a set`
- **H:** `is a set`
- **R3:** `is a a set`
- **Difference:** omission; against C: False; against H: True; confidence: high.
- **Evidence:** Half b shows is a at the right end of the penultimate text line and a set at the start of the last line. Both a tokens are plainly typed.
- **Whole-image box:** `[170, 1795, 1603, 1879]`; crop: `None`.

### R3-003-25: Bottom margin, isolated brown stroke

- **C:** `\margin{\handwritten{\unsure{,|'}}}`
- **H:** `omitted`
- **R3:** `\margin{\handwritten{\unsure{,|'}}}`
- **Difference:** omission; against C: False; against H: True; confidence: low.
- **Evidence:** Crop 07 shows one small brown comma-shaped stroke below the text. The isolated position gives no baseline for deciding comma versus apostrophe, or whether it was an incidental pen mark.
- **Whole-image box:** `[451, 1896, 471, 1923]`; crop: `crops/07_bottom_mark.png`.

### R3-003-26: Paragraph 3, quotation beginning Hom and ending etc

- **C:** `$\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}(M',M)$ est vide sauf si $\underline{n}'\handwritten{\geq}\underline{n}$, auquel cas....etc.....`
- **H:** `\emph{$\mathrm{Hom}_{S'}(M',M)$ est vide sauf si $\underline{n}' \geqslant \underline{n}$, auquel cas…etc…}`
- **R3:** `$\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}(M',M)$ est vide sauf si $\underline{n}'\handwritten{\geqslant}\underline{n}$, auquel cas....etc.....`
- **Difference:** other; against C: False; against H: True; confidence: high.
- **Evidence:** Half b shows the French prose in the same upright typewriter face as the surrounding English; no separate italic or underlined quotation styling is drawn.
- **Whole-image box:** `[176, 1690, 1522, 1781]`; crop: `None`.

### R3-003-27: Paragraph 3, replacement quotation sauf si ... auquel cas

- **C:** `sauf si $\underline{n}'=\underline{m}.\underline{n}$, auquel cas.....`
- **H:** `\emph{sauf si $\underline{n}' = \underline{m}\cdot\underline{n}$, auquel cas…}`
- **R3:** `sauf si $\underline{n}'=\underline{m}.\underline{n}$, auquel cas.....`
- **Difference:** other; against C: False; against H: True; confidence: high.
- **Evidence:** Half b shows upright type throughout this second French phrase, with no additional emphasis mark around the quotation. The separate punctuation and multiplication-dot discrepancies are recorded above.
- **Whole-image box:** `[316, 1793, 993, 1833]`; crop: `None`.

## C doubts and remaining uncertainty

- **Paragraph 1, apparantly ... these:** `\unsure{a\deleted{l}al|a\deleted{a}ll}`. Unresolved. The middle position has a complete a bowl superposed with the tall l stem. Crop 02 confirms overtyping but does not determine order. Box `[781, 645, 847, 678]`; `crops/02_all_overtyping.png`.
- **Paragraph 2, group on Z:** `\unsure{\mathfrak{g}|g|\mathscr{G}}`. Unresolved. Two blue closed loops lie left of a near-vertical connecting stem; the lower loop descends. Lowercase/fraktur g is favored but the hand supplies no alphabet key. Box `[785, 1145, 818, 1185]`; `crops/03_group_letter.png`.
- **Paragraph 2, you explai...:** `\unsure{explai\deleted{n}m|explai\deleted{m}n}`. Unresolved. Crop 04 shows three crowded terminal uprights compatible with superposed m and n. Which impression came first remains unresolved. Box `[930, 1295, 1075, 1326]`; `crops/04_explain_overtyping.png`.
- **Paragraph 2, point [deleted character] if:** `\deleted{\unsure{f|i}}`. Unresolved. The partly visible hook favors f; the blue crossings obscure the stem and center sufficiently to retain i as a weaker candidate. Deletion itself is certain. Box `[823, 1492, 856, 1524]`; `crops/05_deleted_letter_and_one.png`.
- **Paragraph 2, if ... wants:** `\unsure{\deleted{o}wne|\deleted{w}one}`. Unresolved. Crop 05 shows oval o and w strokes within one character position, followed by n and e. Their order of impression cannot be established. Box `[929, 1496, 998, 1528]`; `crops/05_deleted_letter_and_one.png`.
- **Paragraph 3, Hom subscript:** `\unsure{s|S}`. Unresolved. The small S-shaped handwritten curve is unambiguously followed by a prime; lowercase versus reduced capital is not reliably distinguishable. Box `[1152, 1715, 1186, 1748]`; `crops/06_hom_subscript.png`.
- **Bottom isolated mark:** `\unsure{,|'}`. Unresolved. A single curved brown stroke exists below the text, but lacks a textual baseline; comma, apostrophe and incidental pen-mark interpretations cannot be distinguished. Box `[451, 1896, 471, 1923]`; `crops/07_bottom_mark.png`.

## Inventory

| Element | Kind | Position | Visible content | Hand |
| --- | --- | --- | --- | --- |
| E01 | text | upper right, first line | Voorschoten, May 16 1967. | typewriter |
| E02 | text | upper right, second line | Palestrinalaan 11. | typewriter |
| E03 | text | upper left beneath address | Dear Grothendieck, | typewriter |
| E04 | text | upper body, paragraph 1 | I am trying to work out your letter with indications. | typewriter |
| E05 | text | middle body, paragraph 2 | My main difficulty is that I don’t see that for a Galois covering... | typewriter |
| E06 | text | lower body, paragraph 3 | Some other points: in the final formulation of example 3... | typewriter |
| E07 | deletion | paragraph 1, over ... these | a/l overtyped in middle position of all/aal | typewriter |
| E08 | insertion | paragraph 1, same overtyped position | replacement a/l; order uncertain | typewriter |
| E09 | insertion | paragraph 1, end of set-up | question mark | unnamed hand (blue ink) |
| E10 | insertion | paragraph 2, varations | i added above the line | unnamed hand (blue ink) |
| E11 | insertion | paragraph 2, French quotation | grave-accent strokes on the two à forms | unnamed hand (blue/dark ink) |
| E12 | insertion | paragraph 2, a group ... working on Z | two-loop group letter | unnamed hand (blue ink) |
| E13 | insertion | left margin, paired insertion marker before X | corresponding / with and matching pin-shaped reference marks | unnamed hand (blue ink) |
| E14 | insertion | paragraph 2, G and ... commute | second two-loop group letter | unnamed hand (blue ink) |
| E15 | insertion | paragraph 2, after correct | question mark | unnamed hand (blue ink) |
| E16 | deletion | paragraph 2, final position in explai... | overtyped n/m | typewriter |
| E17 | insertion | paragraph 2, same final position | replacement m/n; order uncertain | typewriter |
| E18 | deletion | paragraph 2, and makes this makes | first makes crossed by repeated typed x strokes | typewriter |
| E19 | deletion | paragraph 2, point ... if | isolated f/i crossed in blue | typewriter and unnamed hand (blue ink) |
| E20 | deletion | paragraph 2, first position in ...ne wants | overtyped o/w | typewriter |
| E21 | insertion | paragraph 2, same position | replacement w/o; order uncertain | typewriter |
| E22 | insertion | paragraph 2, after going on | exclamation mark before right parenthesis | unnamed hand (blue ink) |
| E23 | deletion | paragraph 3, after G(M); | with this formulation crossed with repeated typed x strokes | typewriter |
| E24 | deletion | paragraph 3, consists out of | final s crossed by a pen stroke | typewriter and unnamed hand |
| E25 | insertion | paragraph 3, G(M)=... | handwritten mu above the underlined n subscript | unnamed hand (blue ink) |
| E26 | insertion | paragraph 3, after G(M)=mu_n | question mark | unnamed hand (blue ink) |
| E27 | insertion | paragraph 3, under Hom | S-shaped subscript and prime | unnamed hand (blue ink) |
| E28 | insertion | paragraph 3, between n prime and n | greater-than-or-equal with slanted lower stroke | unnamed hand (blue ink) |
| E29 | drawing | paragraph 3, over and below uo in shuold | transposition curve | unnamed hand (blue ink) |
| E30 | insertion | paragraph 3, final index between i and I | membership sign | unnamed hand (blue ink) |
| E31 | margin note | lower blank area beneath positive integers | isolated comma/apostrophe-shaped mark | unnamed hand (brown ink) |
| E32 | text | extreme lower left margin | 2, archive sheet number only | unnamed hand (pencil) |
| E33 | insertion | punctuation positions in paragraphs 2 and 3 | blue punctuation dots/marks at itself:, commute;, conditions;, points:, G(M); and write: | unnamed hand (blue ink) |

The three body paragraphs contain inline formulas, with no separate display or diagram. Both typed deletion passages (“makes” and “with this formulation”), the single cancelled s, the isolated crossed character, three overtyped positions, and all handwritten insertions are retained. The tiny archive number is recorded as a comment, not as an author page number.

## Notation and abbreviations

- **Paragraph 1, both r(X) and both s(M):** `\underline{r}(X),\underline{s}(M)`. lowercase r and s with separate short underlines. Uncertainty: none; the underlines are visible in half a.
- **Paragraph 2, Rev superscript:** `\mathrm{Rev}^{\underline{R}}(S)`. single-struck capital R with its own underline above baseline. Uncertainty: none; no accent over Rev.
- **Paragraph 2, group on Z and commuting actions:** `\unsure{\mathfrak{g}|g|\mathscr{G}}`. blue two-loop descending letter. Uncertainty: alphabet unresolved; same first candidate reused at second occurrence.
- **Paragraph 2, functor r:** `\underline{r}`. lowercase r with short underline. Uncertainty: none.
- **Paragraph 3, M=(a,n):** `M=(\underline{a},\underline{n})`. typed a and n each separately underlined. Uncertainty: none.
- **Paragraph 3, G(M):** `G(M)=\handwritten{\mu}_{\underline{n}}`. blue mu, typed underlined n as subscript. Uncertainty: none.
- **Paragraph 3, Hom:** `\mathrm{Hom}_{\handwritten{\unsure{s|S}'}}`. small blue S-shaped subscript with prime. Uncertainty: s favored; S retained.
- **Paragraph 3, first morphism condition:** `\underline{n}'\handwritten{\geqslant}\underline{n}`. typed underlined n prime, handwritten chevron with parallel sloping lower bar, typed underlined n. Uncertainty: none; exact slanted shape verified in crop 08.
- **Paragraph 3, replacement condition:** `\underline{n}'=\underline{m}.\underline{n}`. underlined n prime equals separately underlined m and n separated by low typed period. Uncertainty: none; period position verified in crop 11.
- **Paragraph 3, last family and index:** `\underline{m}=(m_i)_{i\handwritten{\in}I}`. both small index letters are dotted i with flat foot; terminal I is a capital; membership handwritten. Uncertainty: none; crop 10 confirms both i letters and the membership sign.
- **Paragraphs 1–3, capitals and functor names:** `X,S,M,G,Z,I,R;\mathrm{Rev};\mathrm{Hom}`. single typewriter impressions for X, S, M, G, Z, I, R, Rev and Hom. Uncertainty: none; no doubled/blackboard strokes observed.
- **Paragraph 1, behaviour:** ```behaviour''`. two high quotation strokes at each end. Uncertainty: none.

Abbreviations are not expanded in the text: **etc.** = et cetera; **Rev** tentatively denotes revêtements; **Hom** is morphism-set notation.

## Content and mathematical limits

An unsigned visible page of a typed English letter dated at Voorschoten, with a French quotation and handwritten mathematical/punctuation additions. Paragraph 1 asks whether describing a covering by its behaviour over special covers gives the intended intuition. Paragraph 2 asks about the definition of Galois coverings, commuting actions and full faithfulness of geometric realization. Paragraph 3 asks whether example 3a consists of pairs M=(a,n), and suggests replacing the displayed inequality by a componentwise-multiple condition. These are the letter writer’s questions and claims, not mathematical conclusions verified in this run. All words in the three paragraphs and all agreed C/H signs were visually read from the two supplied halves. S.json is an empty array, so there are no S rows to confirm or overturn.

### Author’s expressed doubts and questions

- I doubt whether I have grasped the essential points.
- Is this intuitively a reasonable way of thinking over your new set-up?
- My main difficulty is that I don’t see that for a Galois covering the extra structure is uniquely determined.
- It seems to me that one must require that the actions of G and the handwritten group letter commute; is this correct?
- this I don’t understand at all
- question mark after G(M)=mu_n
- it seems to me that this shuold [with a transposition mark] be ... sauf si n′=m.n

### Mathematical reading decisions

- No categorical or algebraic assertion was proved or used as a lemma in this run; check_events is empty.
- The relation before the proposed replacement is greater-than-or-equal with a slanted lower stroke, not strict greater-than. This was settled by ink in crop 08.
- The replacement expression has a visible prime, an equals sign, and a baseline period between separately underlined m and n. It is retained without converting the period into a raised dot.
- Both i indices in (m_i)_{i in I}, the membership sign and the final capital I were checked in crop 10; no index was supplied from mathematical expectation.
- The glyphs do not by themselves settle the alphabet of the group letter or the case of the Hom subscript. These remain marked at their first occurrences.
- No display, diagram or mathematical arrow occurs. The only drawing is the small handwritten transposition mark, reproduced as an inline TikZ approximation.

## Titles, dates and page marks

- No title or signature is visible on this page.
- Voorschoten, May 16 1967.
- Palestrinalaan 11.
- Pencil 2 at the extreme lower left is retained only as archive sheet number; no author page number is asserted.
- The entire sheet is a letter typescript with handwritten additions.

## Brief feedback

The brief refers to an attached PREAMBLE, but no PREAMBLE file was among the permitted packet inputs. I used only the named macros already present in C or prescribed by the brief, plus standard TikZ. No external preamble or other page was inspected.

The report counts absence of genuine insertion/deletion/underline state, literal punctuation counts, and unsupported italic styling as differences. Ordinary line wrapping, missing handwritten wrappers alone, equivalent deletion macros, and H’s editorial prose inventory are not counted.
