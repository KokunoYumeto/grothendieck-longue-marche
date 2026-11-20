# Scan 015 — independent reader R1

## Scope and timing

- UTC start: 2026-11-20T10:37:57.472817+00:00.
- UTC end: 2026-11-20T10:51:50.371362+00:00.
- Assigned page only. Read `brief_v06_scan015.md`, the page-local `packet.md`, and the supplied `PREAMBLE.tex` in full.
- No other page or reader output inspected. No OCR, web research, transcription engine, published text, LaTeX compilation, or mathematical restoration used. No delegation, shared-page edits, notation-table edits, or progress-log edits.
- Deliverables are the complete `reading.tex`, this `report.md`, and `result.json` in `readers/scan015/R1/`.

## Actual image-view record

The whole image was opened **once**, for layout; half **a once**, then half **b once**, for complete line-by-line comparison with both supplied witnesses. Only then were the twelve listed local crops created and each viewed once. No full half was reopened or enlarged. All images were returned successfully and inspected; no truncated viewer result required resending.

| Order | Image | Purpose |
|---|---|---|
| 1 | `source/SP44_CW_36_scans/A36-01_36_scan015.jpg` | Whole-page layout only; 1681 × 2151 pixels. |
| 2 | `source/SP44_CW_36_scans/A36-01_36_scan015_a.jpg` | Full top-half reading; 1681 × 1155 pixels, whole y origin 0. |
| 3 | `source/SP44_CW_36_scans/A36-01_36_scan015_b.jpg` | Full bottom-half reading; 1681 × 1156 pixels, whole y origin 995. |
| 4–15 | Twelve crops below, in table order | One local inspection per unresolved locus/group of adjacent edge loci. |

Layout inventory: one typescript page, manuscript page number 6 at upper right, archive pencil number 14 at lower left, three displayed formulas, one triangular diagram, ordinary prose, section 5, one typed interlinear insertion with a pen placement guide, machine cancellations, local overprints or possible overprints, pen arrows/stars/tildes and underlines. No independent drawing or prose margin note was found. The tensor oval is attached to its symbol, not an independent drawing.

## Crops and source-coordinate record

All boxes use whole-image coordinates. The supplied helper was used with `--scan 15 --reader R1`; each output is 2400 pixels wide with autocontrast, LANCZOS resizing, and `UnsharpMask(1,110,3)`. No rotation was needed. Context within a crop was not used to generate a second crop of the same locus.

| Saved crop | Whole-image box | Rotation |
|---|---|---|
| `crops/scan015/R1/first_coefficient.jpg` | `[1144, 168, 1378, 251]` | 0° |
| `crops/scan015/R1/reference_I.jpg` | `[480, 387, 820, 451]` | 0° |
| `crops/scan015/R1/parenthetic_cancel_and_end.jpg` | `[1085, 516, 1674, 607]` | 0° |
| `crops/scan015/R1/dailleurs_cancel.jpg` | `[200, 604, 645, 674]` | 0° |
| `crops/scan015/R1/first_section_cancel.jpg` | `[303, 1359, 620, 1442]` | 0° |
| `crops/scan015/R1/generic_s_insertion.jpg` | `[910, 1336, 1333, 1441]` | 0° |
| `crops/scan015/R1/tensor.jpg` | `[797, 1416, 1077, 1515]` | 0° |
| `crops/scan015/R1/section_right_underline.jpg` | `[1107, 1430, 1632, 1503]` | 0° |
| `crops/scan015/R1/conditions_cancel.jpg` | `[207, 1514, 1644, 1641]` | 0° |
| `crops/scan015/R1/en_dautre.jpg` | `[770, 1718, 1000, 1795]` | 0° |
| `crops/scan015/R1/grif_subscript.jpg` | `[957, 1916, 1500, 2011]` | 0° |
| `crops/scan015/R1/clipped_endings.jpg` | `[1487, 1920, 1681, 2080]` | 0° |

Every half-settled comparison row also has an approximate whole-image box in `result.json`; no extra crop was made merely to obtain coordinates.

## Explicit line-by-line coverage

The positions below identify source lines; typographic line breaks are joined in the continuous reading unless a paragraph/display cue exists. Every formula was compared symbol by symbol, and prose was read for accents, punctuation and cancelled as well as live letters.

| Source locus (whole y) | Coverage and result |
|---|---|
| Upper-right number, y 66–94 | Pen 6; represented as manuscript page number. |
| L01, y 180–234 | `Soit P^m(X) la partie primitive de la cohomologie H^m(X,Q...) , i.e. le`: all words, m degrees, single P/H/Q and coefficient index read. Coefficient index required a crop. |
| L02, y 265–296 | `noyau du composé`: full continuation read; no extra punctuation supplied. |
| D01, y 315–382 | H^m(X), H^m(X-tilde), H^m(Y), H^0(S,R^m f_*(Q...)), three right arrows, pen tilde, star, four outer cohomology degrees, parentheses and final period read. |
| L03, y 395–446 | `On trouve donc grâce à I) un homomorphisme (dit ... de Griffiths ...)`: accents and typewriter double quotation strokes read; I/1 crop settles literal capital-I form. |
| D02, y 453–524 | P^m(X) → H^1(S,R^{m-1}f_*(Q...)): m, 1 and m−1, star, index, arrow and all parentheses read. |
| L04, y 529–593 | Entire parenthesis from `en fait` through `ici)`, including P^1_k, cancelled `nous at/et`, possible point after `peu`, and absence of visible final period. |
| L05, y 607–662 | `D'ailleurs`, cancelled `l'hom/lthom`, and full live phrase through `canonique` read. |
| Diagram, y 672–835 | Typed Y, X_S, S; typed i, f, g; right, down-right and down-left pen arrows, all arrowheads, and the comma right of S. |
| L06, y 859–904 | `induisant`. |
| D03, y 911–991 | Full i* map: three H^1 occurrences; the two R^{m−1} expressions and inner H^{m−1}; g/f stars; three coefficient indices; all parentheses, equality, arrow, colon and period. |
| L07, y 997–1047 | `Ceci dit, l'image inverse par l'homomorphisme de Griffiths plus haut de`; long underline begins at l'image and reaches de. |
| L08, y 1071–1124 | `Im i* est réduite à zéro.`: Im i* is unruled, star is a pen addition, est–zéro is ruled. |
| L09, y 1144–1194 | Indented `Ceci se fait par des calculs explicites essentiellement triviaux,` read completely. |
| L10, y 1213–1260 | `compte tenu de la structure cohomologique connue d'une variété éclatée.` read completely; accents and period checked. |
| L11, y 1300–1350 | `5. Mettant ensemble 3) et 4), on trouve ceci:`. |
| Interline, y 1338–1377 | Typed `supposant m=2n,`; m, equals, 2, n and comma. Pen guide targets before soit; its right hook is not another punctuation mark. |
| L12, y 1363–1429 | Cancelled `Sous`, `Avec les notations de 4),`, inserted phrase target, `soit s le point générique de P^1_k,`: source s cell has a t-like extra component and no detached bar. |
| L13, y 1434–1507 | `et supposons que l'immersion`, full Y–X base-change formula, `de la section hyperplane`: bar/index structures, arrow, typed-x tensor core, circle layer, both k's and final barred s checked. De is within the right prose underline; formula is unruled. |
| L14, y 1513–1579 | `générique`, cancelled `dans`, `satisfasse aux conditions a) et b) de 2).`, first cancelled-condition line. Underline on générique has faint onset; the next long rule begins at a of satisfasse, with separate short rules under et and de. |
| L15, y 1578–1645 | Cancelled `suppose de plus m=2n`, then `Alors pour tout z ∈ Z^n(X) dont la restriction à`: membership is pen; formula unruled; prose rules resume on each side. |
| L16, y 1651–1728 | Y_bar_s, `est algébriquement équivalent à zéro, z est cohomologiquement équiva-`: no feminine final e, no rule under Y or the lone z, no supplied spelling correction. |
| L17, y 1731–1798 | Continuation `lent à zéro (mod torsion).`, cancelled `En d'autr`, `Par suite, le groupe quotient du`: source line-end hyphen joined in the live word; cancellation ends in r without an e cell. |
| L18, y 1802–1856 | `groupe des cycles cohomologiquement équivalents à zéro`, cancelled `mod torsion`, `sur`. |
| L19, y 1867–1923 | Y_bar_s, comma, `modulo ceux qui sont algébriquement équivalents à zéro (groupe qui`. |
| L20, y 1937–2010 | `mérite le nom de groupe de Griffiths`, Grif opening mark and Y subscript, `de` final Y subscript with lower x-out, closing parenthesis/comma, cancelled `contient`, clipped `tensorisé`. |
| L21, y 2005–2074 | `par Q, contient comme sous-espace le sous-espace P^{2n}_{alg}(X) formé des classes`: Q rule, capital P, both 2n and alg, parentheses, hyphens and clipped final s read. |
| L22, y 2080–2133 | `de cohomologie primitives sur X qui sont algébriques, - vectoriel qui a`; algébriques underline, single source dash and unfinished final phrase retained. |
| Lower-left archive mark, y 2082–2127 | Pencil 14, recorded only as an archive-number comment. |

The useful main-review boxes supplied from these existing views were: the image-inverse assertion `[205, 997, 1642, 1124]`; the `Ceci se fait ... triviaux / compte tenu ... variété éclatée` paragraph `[210, 1144, 1639, 1260]`. No new view was made to provide them.

## Comparison outcome and C doubts

The complete, locus-separated comparison is in `result.json`: **37 rows**, including **20 against C**, **22 against H**, and **10 C-doubt/note rows**. These totals include source-layer and underline-scope changes, not just lexical substitutions. There are **72 inventory items**. `reading.tex` is the complete page rather than an amendment list.

H’s global chi-shaped-machine-ell convention is credited throughout. Its bold/underlined Q and P house typography is not counted as an alphabet error. Equivalent emph/uline markup alone is not an error; actual rule extent is compared. Missing H handwriting wrappers alone are not counted. H’s clearly editorial remarks are not transcribed as authorial text; its cancelled-condition reading is evaluated as a witness claim.

| C locus | Independent outcome | Status against C |
|---|---|---|
| `nous et / nous at` | Prefer `nous at`, retain `nous et`; no full resolution. | Changed preferred reading. |
| `l'hom / lthom` | Both remain possible after crop. | Unchanged doubt. |
| Cancelled `Alors pour On / Alors pour où` | Capital-O oval and n support `On`; `suppose de plus m=2n` readable on next line. | Doubt resolved. |
| `En d'autre / En d'autr` | Final occupied cell is r; no further e cell. | Resolved to `En d'autr`. |
| Lower cancelled `x / k` | Visible x cancellation cell, no recoverable old k. | Resolved to literal x-out; original underlying symbol is not claimed. |
| Right-edge `tensorisé` | Final e and accent are incomplete at the edge; preferred reading remains marked. | Unchanged doubt. |
| Right-edge `classes` | Final s has recoverable upper-left/lower curved structure. | Doubt resolved. |
| Reference I) | Capital-I form retained. | Straight C confirmation; not a C change. |
| Masculine `équivalent` | No final e. | Straight C confirmation; not a C change. |
| `- vectoriel qui a` | No missing noun supplied. | Straight C confirmation; not a C change. |

Further material decisions: all six coefficient subscripts are mechanical crossed glyphs rather than wholly pen ells; the prose point-name and first Y subscript have separately recorded t-like components; the tensor sign preserves a typed lowercase x and an uncertain O/pen-circle layer; the rule before `la section` includes `de`; `satisfasse` has an initially unruled s; and short independent rules occur beneath `et` and `de` in the condition reference. H omits several recoverable cancellations and overextends several underline scopes.

The cancellation of Sous extends into one following blank cell. It is not represented as a recovered old lexical x. Conversely, the isolated lower x beneath the last Y subscript is recorded as a visible cancellation character because no underlying old letter can be recovered. No old word was invented from a count of cancellation cells.

Paragraph handling: the indented `Ceci se fait` is a new paragraph. No blank-line/indent cue separates the parenthesis from D'ailleurs; these are encoded continuously. Their rhetorical paragraph status remains uncertain and is not counted as a semantic witness error. The final equation-like P expression remains inline in its prose line.

## Unresolved items

Ten unresolved entries are in the JSON and marked in the complete reading where appropriate:

1. Literal chi/ell alphabet of the mechanically repeated coefficient glyph.
2. a/e within cancelled `nous at/et`.
3. Punctuation versus incidental point after `peu`.
4. Apostrophe/t in cancelled `l'hom/lthom`.
5. Order or interpretation of the t-like component in the generic-point s.
6. Separately, order or interpretation of the t-like component in the first barred Y subscript.
7. Typed O versus pen circle around the secure typed x tensor core.
8. Faint underline onset at g/é of générique.
9. Pen opening parenthesis versus t-shaped mark after Grif.
10. Right-edge completion/accent of tensorisé.

No extra local images were sought after the single-crop inspection of these loci. The preferred plain s in the two overprint cells is not a claim that the additional upright is absent; the structural alternatives preserve that unresolved observation. The source may support a correction, but the direction is not inferred from the mathematically expected variable.

## Mathematical reading and checks

The page states a definition of primitive cohomology through a kernel, a Griffiths homomorphism into a first cohomology group of a higher direct image, and an induced i* map associated with the displayed triangle. It then asserts that the inverse image of Im i* is zero. The next paragraph calls the necessary explicit calculations `essentiellement triviaux` and invokes the known cohomological structure of a blown-up variety; those calculations are not supplied here.

Section 5 combines references 3) and 4), with the typed interlinear condition m=2n, and assumes conditions a) and b) of 2) for the generic hyperplane immersion. It claims algebraic triviality on that hyperplane entails cohomological triviality modulo torsion. The later quotient is named the groupe de Griffiths, tensorized with Q, and said to contain algebraic primitive classes. The final sentence is incomplete on this page.

Following the notation served as a diagnostic, not a substitute for visible ink. In particular, H’s geometric-point bar on the prose point name was inspected rather than accepted from the role of a generic point. The actual absence of a detached bar and presence of a t-like component are recorded. Similarly, tensor meaning did not justify dropping the visible typed-x component. The source’s masculine équivalent, abandoned On phrase and incomplete vectoriel phrase remain unrepaired.

**No actual proof, re-proof, computation, formal certificate or imported background result was checked.** The referenced earlier conditions are outside this assigned page. `check_events` is therefore empty. Reading the zero-inverse-image claim and the author’s assessment `triviaux` does not verify either.

## Structural verification and brief feedback

Structural verification only: complete JSON with all comparison boxes and inventory entries, unique comparison IDs, valid inventory kinds, in-bounds source boxes, twelve saved crop metadata files, balanced LaTeX braces and dollar delimiters, paired TikZ environment, and macros from the supplied preamble or permitted standard packages. No LaTeX compilation was run.

The brief is workable. A recommended encoding for an isolated non-lexical baseline mark and for a t-like component without secure correction order would improve consistency between readers. Giving each supplied half’s whole-image y origin would also remove a small bookkeeping step. No further image access is requested by this reader.
