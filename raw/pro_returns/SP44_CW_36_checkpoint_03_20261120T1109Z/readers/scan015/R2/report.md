# Scan 015 — independent reader R2

## Scope and timing

- Started UTC (first recorded clock reading): **2026-11-20 10:37:59 UTC**.
- Ended UTC: **2026-11-20 10:53:55 UTC**.
- Assigned page only: scan 015, handwritten manuscript page **6**, archive pencil number **14**.
- Inputs read in full: `briefs/brief_v06_scan015.md`, `packets/scan015/packet.md`, and `PREAMBLE.tex`.
- I did not inspect any other page or reader's files, delegate, use OCR/text recognition, browse, research, compile LaTeX, or alter shared logs, notation, or deliverables.

`reading.tex` is the complete diplomatic reading. `result.json` contains the complete **38-row comparison**, **60-element inventory**, notation, abbreviations, and **9 unresolved entries**. The comparison flags count **22 rows against C**, **25 against H**, and **10 C-doubt/attention confirmations or resolutions**. A row can oppose both witnesses. Straight confirmations of C's unambiguous source forms are not counted against C.

## Actual image-view record

The view sequence was:

1. `A36-01_36_scan015.jpg`, **once**, for layout only. Dimensions obtained separately through PIL: **1681 × 2151**.
2. `A36-01_36_scan015_a.jpg`, **once**, read line by line against both C and H. Dimensions **1681 × 1155**.
3. `A36-01_36_scan015_b.jpg`, **once**, read line by line against both witnesses. Dimensions **1681 × 1156**; its origin in the whole image is **y = 995**. The overlap repeats the two-line “Ceci dit” assertion.
4. The 13 local crops below, each viewed **once**, in the listed order. At most two were emitted per viewer output; none was truncated or resent.

The whole view established the two page-number annotations, opening prose and three displays, the triangular diagram, the “Ceci dit” assertion, an indented explanatory paragraph, section 5, a typed interlinear insertion with a pen placement guide, repeated machine cancellations, pen underlines, and right-edge clipping. No separate drawing or independent marginal mathematical/textual note was present. The mark in the Grif delimiter cell is kept attached to that word, not promoted to a drawing.

Every local crop used the supplied helper with `--scan 15 --reader R2`: autocontrast, LANCZOS to **2400 px width**, and UnsharpMask `(1,110,3)`. No rotation was needed for readable text. Boxes below and all boxes in `result.json` are **whole-image coordinates**. Half-settled differences also have boxes; I did not make extra crops merely to supply coordinates.

| Actual crop filename | Whole-image box | Views |
|---|---:|---:|
| `crops/scan015/R2/first_coefficient.jpg` | `[1160, 165, 1360, 249]` | 1 |
| `crops/scan015/R2/reference_I.jpg` | `[490, 389, 760, 452]` | 1 |
| `crops/scan015/R2/mais_cancelled.jpg` | `[1080, 522, 1668, 600]` | 1 |
| `crops/scan015/R2/dailleurs_cancelled.jpg` | `[200, 603, 685, 668]` | 1 |
| `crops/scan015/R2/section_start.jpg` | `[303, 1360, 581, 1431]` | 1 |
| `crops/scan015/R2/generic_insertion.jpg` | `[904, 1330, 1312, 1434]` | 1 |
| `crops/scan015/R2/embedding_underlines.jpg` | `[791, 1426, 1625, 1510]` | 1 |
| `crops/scan015/R2/cancelled_condition.jpg` | `[203, 1506, 1650, 1646]` | 1 |
| `crops/scan015/R2/conclusion_underlines.jpg` | `[208, 1652, 1659, 1728]` | 1 |
| `crops/scan015/R2/before_Par_suite.jpg` | `[754, 1714, 1212, 1794]` | 1 |
| `crops/scan015/R2/bottom_grif.jpg` | `[948, 1920, 1489, 2014]` | 1 |
| `crops/scan015/R2/tensorise_edge.jpg` | `[1470, 1915, 1680, 2005]` | 1 |
| `crops/scan015/R2/classes_edge.jpg` | `[1331, 1991, 1680, 2082]` | 1 |

## Explicit coverage of every source line and object

The labels below are used in the comparison. Line breaks are coverage locators, not automatically paragraph boundaries.

| Block / source baseline | Text or notation read and accounted for |
|---|---|
| Top margin | Handwritten `6`; not confused with the archival number. |
| T1, line 1 | `Soit P^m(X) la partie primitive de la cohomologie H^m(X,Q_...) , i.e. le`; capitals, degree m, Q lower rule, coefficient subscript, comma, and `i.e.` all examined. |
| T1, line 2 | `noyau du composé`; no supplied colon. |
| D1 | All four H terms, degrees m/m/m/0, tilde over X, three rightward arrows, S, R^m, f lower star, coefficient, closing parentheses, and final point. |
| T2 | `On trouve donc grâce à I) un homomorphisme (dit "de Griffiths")`; reference glyph and both pairs of quotation strokes examined. |
| D2 | P^m(X), arrow, H^1, S, R^{m−1}, f lower star, coefficient, and every closing parenthesis. |
| T3 | Complete parenthesis from `en fait` through `ici)`; P^1_k, cancelled two words after `mais`, small spot after `peu`, and absence of a visible final full stop. |
| T4 | `D'ailleurs`, cancelled five-cell fragment, and live `on a un homomorphisme d'immersion canonique`. |
| G1 | Objects Y, X_S, S; typed labels i/f/g; directions Y→X_S, Y→S, X_S→S; handwritten arrowheads; typed lower-right comma. |
| T5 | `induisant`. |
| D3 | i upper star and colon; H^1(S,R^{m−1}g_*(Q_...)); equality; H^1(S,H^{m−1}(X,Q_...)); rightward arrow; H^1(S,R^{m−1}f_*(Q_...)); all parentheses, degrees, stars, coefficient repetitions, and terminal point. |
| T6, line 1 | `Ceci dit, l'image inverse par l'homomorphisme de Griffiths plus haut de`; long pen underline from `l'image` to `de`. |
| T6, line 2 | Bare `Im i*`, separate rule under `est réduite à zéro`, and point. The two halves overlap on these T6 lines. |
| T7, indented line 1 | `Ceci se fait par des calculs explicites essentiellement triviaux,`; indentation preserved as a paragraph cue. |
| T7, line 2 | `compte tenu de la structure cohomologique connue d'une variété éclatée.` |
| T8 | `5. Mettant ensemble 3) et 4), on trouve ceci:`; numbering, parentheses, comma and colon. |
| T9, insertion above first line | Typed `supposant m=2n,`, its comma, and the pen guide attaching it after `4),` before `soit`; the guide's hooked end is not a second comma. |
| T9, line 1 | Cancelled `Sous` plus a visible extra x-out cell; `Avec les notations de 4), soit [s/t-looking cell] le point générique de P^1_k,`. |
| T9, line 2 | `et supposons que l'immersion`; Y with barred, overprinted subscript; pen arrow; X and mixed x/oval sign, lower k, `k(bar s)`; `de la section hyperplane`; exact ruled and unruled spans. |
| T9, line 3 | `générique`, cancelled `dans`, `satisfasse aux conditions a) et b) de 2).`, and first line of cancelled `(Alors pour On`; partial and short rules all recorded. |
| T9, line 4 | Cancelled `suppose de plus m=2n` plus trailing x-out cell; live `Alors pour tout z ∈ Z^n(X) dont la restriction à`; membership, exponent n, and separate underline spans. |
| T9, line 5 | `Y_bar s est algébriquement équivalent à zéro, z est cohomologiquement équiva-`; bare formula/variable tokens, partial initial rule, lack of final e in `équivalent`, and line-end hyphen. |
| T9, line 6 | `lent à zéro (mod torsion).`, cancelled `En d'autr`, and `Par suite, le groupe quotient du`; `équiva-/lent` joined in the reading. |
| T9, line 7 | `groupe des cycles cohomologiquement équivalents à zéro`, cancelled `mod torsion`, and `sur`. |
| T9, line 8 | `Y_bar s, modulo ceux qui sont algébriquement équivalents à zéro (groupe qui`. |
| T9, line 9 | `mérite le nom de groupe de Griffiths Grif(Y_bar s) de Y_bar s),`, the lower cancelled glyph, cancelled `contient`, and edge-clipped `tensorisé`; opening-delimiter remnant checked locally. |
| T9, line 10 | `par Q, contient comme sous-espace le sous-espace P^{2n}_{alg}(X) formé des classes`; Q rule, both lexical hyphens, 2n, alg, parentheses, and clipped terminal s of classes. |
| T9, line 11 | `de cohomologie primitives sur X qui sont algébriques, - vectoriel qui a`; final underline, comma, dash, absence of a supplied noun, and unfinished ending. |
| Bottom left margin | Pencil-like archive `14`, recorded only in an archive-number comment. |

The T3/T4 boundary has normal adjacent baseline spacing, the same left margin, and no visible indentation/blank baseline. I therefore do not insert C's extra paragraph break there. T7 has clear indentation; the section heading and the indented section-5 paragraph are separate blocks. No word is split solely to reproduce a typewriter line ending.

## Comparison findings and remaining uncertainties

The full row-by-row evidence, exact witness readings, flags, local descriptions and whole-image boxes are in `result.json`; this section highlights the main decisions without replacing that list.

### Coefficients, capitals, indices, and diagram

All six coefficient subscripts have the repeated crossed mechanical form. I use `\unsure{\chi|\ell}` first, then `\chi`, and remove C's assertion that these are handwritten ell glyphs. H is explicitly credited for its global machine-ell/chi-shaped convention; this alphabet convention alone is not counted as an H error. Q has one typed contour and a separate low rule. P, H, R, and Z do not show a secure displaced double impression on this page. The capital-I form in `grâce à I)` is secure from the local crop and remains C's exact reading.

The triangle's object/label readings and all three directions agree with C; H omits the typed comma at lower right. The diagram is drawn in full, including that comma. The superscript star of the later `Im i*` is a pen completion; C's source layer is updated, while H's missing wrapper alone is not scored as an error.

The `soit` token has a dominant s body and an extra central t-like component, without a separate overbar. The first barred Y-subscript repeats that same component. Its recurrence, rather than only the mathematical variable name, is why the first-occurrence structural uncertainty applies. By contrast, s inside `k(bar s)` is clean on this page. I do not select an old/live order. Both occurrences have separate comparison boxes.

The tensor-like sign is read as a typed x core inside a pen oval. The physical serifed x remains visible in the output; its mathematical role does not determine the source layer.

### Cancellations and insertions

The two cancellations after `mais` and `D'ailleurs` remain unresolved at their obscured cells: `nous et|nous at` and `l'hom|lthom`. The section-5 initial deletion has a readable `Sous` and one extra visible x-out cell. The cancelled long condition reads `(Alors pour On suppose de plus m=2n`, with a trailing x-out cell and no supplied closing parenthesis. The tall round O plus following n supports `On`, rather than the alternative `où`; H's tentative note beginning `si on suppose` does not match the preceding recoverable words.

Before `Par suite`, the final cancelled cell is read as r without a separate following e-cell, giving `En d'autr`. The live word `équivalent`, after the singular feminine restriction, has no final e and is retained exactly as C already had it. The cancelled `dans`, `mod torsion`, and `contient` are all retained. The lower cancelled cell below the final Y-subscript remains `x|k`; x is the visible cancellation-cell reading, not a claim to recover an old lexical x.

The interlinear `supposant m=2n,` is typed. Its connecting guide is pen. Its comma belongs to the inserted words; the guide's far-right hook is not additional punctuation. The hook in the `Grif` opening-delimiter cell is different: it has a visible transverse component, so a possible underlying t is left as a structural alternative. That is a low-confidence unresolved addition, not an asserted correction chronology.

### Underlining and edge readings

I preserve the bare `Im i*` between the two rules in the upper assertion. In section 5, the immersion formula and the conclusion's z-membership formula have no underline. The rule after the immersion includes `de`; the next line begins its rule inside `générique`, represented as `gén\uline{érique}`. Another begins inside `satisfasse`, represented as `s\uline{atisfasse aux conditions}`. The first conclusion predicate begins its rule at the final t of `est`, hence `es\uline{t ...}`. These are pen rules below typed words; the words themselves are not described as handwritten.

The very short rules in `et` and `de` occupy their right-hand portions. The preferred spans are `e\uline{t}` and `d\uline{e}`, but the full-word alternatives are marked in place because the beginnings lie near the preceding letter's final stroke. The labels a), b), and 2) are unruled. These endpoints merit main-reader adjudication from the supplied single crop.

The final s in `classes` is identifiable from its surviving upper-left and lower-left curves, so C's in-place uncertainty is resolved there. The terminal e and accent in `tensorisé` remain clipped enough that its uncertainty is retained. The source ends `- vectoriel qui a`; no noun or continuation is supplied, and confirming this unambiguous C text does not count as a C change.

There is a small low spot between `peu` and `importe`. The reading marks it as a doubtful period, with incidental ink/scan contamination retained as the unresolved alternative. This low-confidence observation is expressly not a firm punctuation correction.

## Mathematical reading notes and checks

**36-015-S1.** The page introduces the primitive part as the kernel of the displayed composite from H^m(X), through H^m(tilde X) and H^m(Y), to H^0(S,R^m f_*(Q_chi)). Every map direction, degree and coefficient was read. I did not establish the correctness of that characterization independently.

**36-015-S2.** It then states a Griffiths homomorphism to H^1(S,R^{m−1}f_*(Q_chi)), supplies the immersion triangle over S, displays the induced i* map and the equality with the constant H^{m−1}(X,Q_chi) coefficient, and asserts that the inverse image of Im i* under the first homomorphism is zero. The text says the result follows from “calculs explicites essentiellement triviaux” and the known cohomology structure of a blown-up variety. Those are the author's words, not a verification performed here. The aside about replacing S by P^1_k is preserved, including its cancellations and “peu ... importe ici”.

**36-015-S3.** Section 5 inserts m=2n before the generic-point setup, imposes the cited a)/b) conditions on the hyperplane immersion, and states that a cycle whose restriction is algebraically equivalent to zero is cohomologically equivalent to zero modulo torsion. It then begins the assertion about the rationalized Griffiths quotient containing the primitive algebraic cohomology subspace P^{2n}_{alg}(X), ending mid-sentence on this page. The hypotheses in other sections were not consulted.

Mathematical context served only to flag the generic-point bar/layer, the tensor-like sign, the coefficient alphabet, and the moved m=2n assumption for literal inspection. It did not supply missing letters, change an index, repair the source agreement, or prove an implication. **No mathematical check event was carried out**; `check_events` is intentionally empty. The only validation below is document structure, not a mathematical certificate.

## Inventory and provenance

The complete inventory in `result.json` includes every text block, all three displays, the complete triangle, both page-number annotations, every individual pen arrow/star/tilde, all cancellation groups, the insertion and its guide, each separate underline stroke/span, the mixed product-sign layer, and the two uncertain overprint/remnant loci. There is no separate drawing. Hand attribution stays at “pen”, “pencil-like handwriting”, or “typewriter-looking overlapping components”; the page alone does not establish a person's identity.

Ordinary macro/house-style differences are not treated as readings. In particular, H's underlined bold coefficient style, its global explanation of the machine ell, and `emph` for authorial emphasis are credited. Actual underline extent is compared separately. Explanatory H commentary is not classified as authorial text; only the H note's actual claim about the cancelled words is collated.

## Structural validation and brief feedback

Structural-only validation passed: balanced braces; three paired display delimiters; one paired `tikzcd` environment; even dollar delimiters (including the standard overlay construction); allowed preamble/standard macros; parseable JSON; unique comparison IDs; all 38 whole-image boxes within 1681×2151; 60 inventory entries marked transcribed; and 13 crop JPG/metadata pairs. **No LaTeX compilation was performed.**

The first-occurrence shorthand for a repeated uncertain overprint can visually simplify a later physical cell. I have therefore documented both locations explicitly, with separate boxes, and applied the shorthand only to visibly recurring structure. The tiny underline endpoints are the other place where a crop and a retained character-span alternative are more faithful than a forced whole-word choice. No workflow change is requested.
