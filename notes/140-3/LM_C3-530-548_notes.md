# LM_C3-530-548 — Notes

## 1. Source and transcription conventions

Source: the nineteen supplied image files `LM_C3-530-548_scan530.jpg` through `LM_C3-530-548_scan548.jpg`, identified in the supplied task as Grothendieck’s *La Longue Marche à travers la théorie de Galois* (1981), Montpellier manuscript cote 140-3. Readings were made from these images. No published transcription was used to supply or correct their text.

The `scanpage` numbers follow the filenames. They differ by one from the lower handwritten and printed archive numbers visible in the images. Original upper manuscript numbers are retained with `mspage`; lower handwritten numbers are separate `margin` blocks. The printed institutional footer is also retained, in its own final `margin` block on each scan, to preserve all visible text while keeping its location distinct from the manuscript body. The inventory identifies these footer blocks explicitly.

The LaTeX file is a fragment without a preamble. It uses the requested editorial macros, standard mathematical LaTeX, `tikz-cd`, and TikZ. The small vertical membership signs on scan 545 use standard `rotatebox` syntax (the host document needs `graphicx`). The host document must define the editorial macros; different definitions can display, colour, or suppress textual states without changing the transcription. The diagrams use explicit ampersand replacement to permit their placement inside the editorial macros (Stoffel, 2021, §3.4). Comments of the form `E530-01` connect passages to inventory entries and the doubt table. Numbering is not regularized: duplicate equation numbers, interrupted sentences, cancelled drafts, repeated expressions, and visibly incomplete formulas are retained.

Nested deletion and insertion macros preserve distinguishable revisions within already cancelled passages. An uncertain algebraic expression is a best reading of the ink, not an emendation justified by the expected identity. Long horizontal repetition strokes in lists are represented by rules rather than expanded into words. The conventional `mathcal{G}` rendering represents the recurrent handwritten group glyph; script ambiguities between the later constructed groups and parameter spaces are marked at their locations.

### Page-number crosswalk

| Scan file | Upper manuscript number visible | Lower number visible |
|---:|---:|---:|
| 530 | 568 | 529 |
| 531 | — | 530 |
| 532 | 569 | 531 |
| 533 | — | 532 |
| 534 | 570 | 533 |
| 535 | — | 534 |
| 536 | 571 | 535 |
| 537 | — | 536 |
| 538 | 572 | 537 |
| 539 | — | 538 |
| 540 | 573 | 539 |
| 541 | — | 540 |
| 542 | 574 | 541 |
| 543 | — | 542 |
| 544 | 575 | 543 |
| 545 | — | 544 |
| 546 | 576 | 545 |
| 547 | — | 546 |
| 548 | 577 | 547 |

## 2. Table of doubts

Locations refer to approximate manuscript lines or physical regions, with inventory anchors when available. A reading under `unsure` remains uncertain even when no alternative is offered. **High** means the proposed reading is strongly supported but a specified detail remains uncertain; **medium** means a plausible reading with incomplete letter or symbol evidence; **low** means competing readings, overlap, cancellation, or missing ink prevents a secure choice. Formula alternatives remain in LaTeX so their indices, primes, and positions can be compared. Rows describing an entire phrase or spatial feature supplement the individual marked-token rows. `illegible` counts words, never formula symbols.

| Scan | Line / position (approx.) | Reading | Alternatives / qualification | Confidence |
|---:|---|---|---|---|
| 530 | upper, ll. 2–3 [E530-03] | `des` | de | low |
| 530 | upper middle, ll. 5–8 [E530-08] | `je` | — | medium |
| 530 | upper middle, ll. 5–8 [E530-08] | `voudrais` | — | medium |
| 530 | upper middle, ll. 5–8 [E530-08] | `autom.` | — | medium |
| 530 | middle, (2) [E530-09] | `\rho` | — | low |
| 530 | left middle, beside (2)–(4) [E530-10] | `le` | — | low |
| 530 | left middle, beside (2)–(4) [E530-10] | `équivalent` | — | medium |
| 530 | middle, ll. 10–11 [E530-11] | `autom.` | — | medium |
| 530 | middle lower, first (5) [E530-14] | `\alpha` | — | low |
| 530 | left lower, beside (4)–(5) [E530-15] | `du form.` | — | low |
| 530 | left lower, beside (4)–(5) [E530-15] | `oublié` | — | low |
| 530 | left lower, beside (4)–(5) [E530-15] | `un` | — | low |
| 530 | left lower, beside (4)–(5) [E530-15] | `qu'on pourrait` | — | low |
| 530 | left lower, beside (4)–(5) [E530-15] | `d'emblée` | demander | low |
| 530 | left lower, beside (4)–(5) [E530-15] | `donner` | prendre | low |
| 530 | left lower, beside (4)–(5) [E530-15] | `\sigma_\infty` | \sigma^{-1} | low |
| 530 | left of B display [E530-21] | `(7)` | — | low |
| 530 | bottom, (7) [E530-22] | `\prime` | — | low |
| 530 | bottom, final two lines [E530-23] | `s'explicite` | — | medium |
| 531 | upper left, before (8) [E531-03] | `que` | — | low |
| 531 | upper left, before (8) [E531-03] | `\illegible{1}` | No recoverable word reading after enlargement | low |
| 531 | upper to centre, ll. 5–10 [E531-06] | `que` | car | low |
| 531 | centre lower, cancelled (10) [E531-11] | `\alpha` | \alpha_1 | low |
| 531 | lower middle, second (9) [E531-13] | `=` | — | low |
| 531 | lower middle, second (9) [E531-13] | `\sigma` | — | low |
| 531 | lower, three-line cancelled paragraph [E531-14] | `\overline{\mathrm m}` | = | low |
| 531 | lower, three-line cancelled paragraph [E531-14] | `nous écrivons` | — | low |
| 531 | lower, three-line cancelled paragraph [E531-14] | `tels $\alpha\in$` | — | low |
| 531 | bottom, Proposition and opening statement [E531-16] | `qu'un` | qu'on | low |
| 531 | statement after qu’un [E531-17] | `B_{\rho,\sigma}` | — | low |
| 531 | statement after qu’un [E531-17] | `\rho,\sigma` | — | low |
| 531 | statement after qu’un [E531-17] | `\varepsilon_3` | — | low |
| 532 | top, (10) [E532-02] | `u` | — | medium |
| 532 | upper, heavily cancelled (12) [E532-06] | `\bmod` | — | low |
| 532 | upper, heavily cancelled (12) [E532-06] | `\nu_3` | — | low |
| 532 | upper, heavily cancelled (12) [E532-06] | `\varepsilon_3(\mu)` | — | low |
| 532 | upper, heavily cancelled (12) [E532-06] | `\Longleftrightarrow` | — | low |
| 532 | left upper, beside (12) [E532-07] | `\alpha` | — | medium |
| 532 | after β [E532-12] | `seulement` | — | medium |
| 532 | middle, before (14) [E532-14] | `aura alors` | — | medium |
| 532 | before sur L₀ [E532-21] | `$u$` | — | low |
| 532 | before sur L₀ [E532-21] | `4` | — | medium |
| 532 | before sur L₀ [E532-21] | `\Leftarrow` | = | low |
| 533 | top, lines 1–3 [E533-01] | `tout` | — | low |
| 533 | top, lines 1–3 [E533-01] | `est` | — | low |
| 533 | upper quarter, lines 4–8 [E533-02] | `élém.` | — | medium |
| 533 | upper quarter, lines 4–8 [E533-02] | `f.` | — | medium |
| 533 | upper quarter, lines 4–8 [E533-02] | `autom.` | — | medium |
| 533 | upper middle, transition [E533-03] | `on` | — | low |
| 533 | middle, first line of cancelled calculation [E533-04] | `\text{donc}` | — | low |
| 533 | middle, second line of cancelled calculation [E533-05] | `\sigma(\eta^{-1}\zeta)\underbrace{\sigma\rho}_{\varepsilon_0}` | — | low |
| 533 | middle, third line of cancelled calculation [E533-06] | `\sigma(\varepsilon_0)` | \sigma\rho | low |
| 533 | middle, third line of cancelled calculation [E533-06] | `\zeta` | — | low |
| 533 | middle lower, within cancelled area [E533-08] | `On en aura` | On a aussi | low |
| 533 | middle lower, within cancelled area [E533-08] | `\illegible{1}` | No recoverable word reading after enlargement | low |
| 533 | middle lower, within cancelled area [E533-09] | `u` | — | low |
| 533 | middle lower, within cancelled area [E533-09] | `\sigma` | — | low |
| 533 | middle lower, within cancelled area [E533-09] | `\varepsilon\bigl(\beta\sigma(\beta)^{-1}\bigr)` | — | low |
| 533 | bottom of cancelled box [E533-10] | `16` | 15 | low |
| 533 | bottom of cancelled box [E533-10] | `\rho` | — | low |
| 533 | bottom of cancelled box [E533-10] | `u` | — | low |
| 533 | near bottom [E533-14] | `**` | * | low |
| 534 | top [E534-01] | `=l_1^\nu` | — | low |
| 534 | upper quarter [E534-02] | `2` | — | low |
| 534 | above (16) [E534-03] | `\zeta` | — | medium |
| 534 | upper middle [E534-04] | `$u$` | — | medium |
| 534 | upper middle [E534-04] | `autom.` | — | medium |
| 534 | middle, boxed lemma conclusion (17) [E534-05] | `u(\sigma)^2=-1` | — | low |
| 534 | middle, next paragraph [E534-07] | `à` | : | low |
| 534 | middle, next paragraph [E534-07] | `enfin` | — | medium |
| 534 | middle, next paragraph [E534-07] | `fait par les conditions` | — | low |
| 534 | middle, next paragraph [E534-07] | `automatique` | — | medium |
| 534 | middle lower, second (17) [E534-09] | `\alpha\equiv\tau^{\varepsilon_3(\mu)}` | — | low |
| 534 | middle lower, second (17) [E534-09] | `l'expr.` | — | medium |
| 534 | middle lower, second (17) [E534-09] | `form.` | forme | low |
| 534 | lower quarter, corollary heading [E534-10] | `trouvé` | — | medium |
| 534 | below diagram [E534-12] | `l'ens.` | — | medium |
| 534 | last line, 2° [E534-14] | `\zeta'` | \eta | low |
| 535 | top, line 1 [E535-01] | `du` | de | low |
| 535 | top, line 3 [E535-03] | `f. et s.` | — | low |
| 535 | upper paragraph, lines 4–6 [E535-04] | `Les` | La | low |
| 535 | above conditions, line 4 [E535-05] | `3` | 4 | low |
| 535 | above conditions, line 4 [E535-05] | `sont équivalentes` | est équivalente | low |
| 535 | above conditions, line 4 [E535-05] | `à ceci` | ainsi | low |
| 535 | upper paragraph, line 6 [E535-06] | `celle-ci les complète` | elle-ci le complète | low |
| 535 | upper third, (A) [E535-08] | `sss` | ssi | medium |
| 535 | upper third, (A) [E535-08] | `\alpha` | — | low |
| 535 | middle, before (19) [E535-10] | `de` | des | low |
| 535 | middle, (19) [E535-11] | `i_{L_0,B}` | overwritten subscript | medium |
| 535 | middle, (20) [E535-13] | `\operatorname{Centr}` | — | medium |
| 535 | middle, following (20) [E535-14] | `normale` | invariante | low |
| 535 | middle lower, (21) [E535-15] | `i_{L_0,B}` | overwritten subscript | medium |
| 535 | lower third, following (23) [E535-21] | `déduit` | a compressed participle preceding de | medium |
| 535 | bottom, (24) [E535-23] | `\chi_\gamma` | — | medium |
| 535 | bottom right, beside (24) [E535-25] | `de` | et | low |
| 535 | line 1 | `du lacet` | de lacet | medium |
| 535 | deleted line 3 | `il f. et s. qu’on` | il faut s. qu’on | low |
| 535 | (A), second line | `deleted α` | an overwritten short mathematical token | low |
| 535 | before (19) | `de groupes` | des groupes | medium |
| 535 | (20) | `Centr` | Centre | medium |
| 535 | (24), arrow label | `χ_γ` | a corrected χ with unclear subscript | medium |
| 536 | first line [E536-02] | `Considérons` | Etudions | low |
| 536 | middle, (29) [E536-09] | `B_{\rho,\sigma}` | — | medium |
| 536 | middle, (29) [E536-09] | `G_{\rho,\sigma}` | \mathcal{G} | low |
| 536 | middle lower [E536-10] | `invariante` | invariant | medium |
| 536 | lower quarter [E536-12] | `\operatorname{Centr}` | — | medium |
| 536 | lower quarter [E536-12] | `selon` | suiv. | medium |
| 536 | bottom, (31) [E536-14] | `\chi_\gamma` | — | medium |
| 536 | (26), first arrow | `right arrow` | surjection arrow; endpoint is heavily inked | medium |
| 536 | (28), lower annotation | `S₀Gρ,σ` | the subscript 0 is small | medium |
| 536 | (29), target | `Bρ,σ·Gρ,σ` | Bρ,σ·G (the second factor visually carries a subscript) | medium |
| 536 | below (30) | `Centr` | Centre | medium |
| 536 | (31), bottom vertical label | `χ_γ` | δ_γ | low |
| 537 | top, (32) [E537-02] | `\cdot` | — | medium |
| 537 | end of line with respectivement [E537-09] | `sss` | ssi | low |
| 537 | end of line with respectivement [E537-09] | `à` | — | low |
| 537 | above si on suppose [E537-12] | `ou égale` | ou égal; abbreviation sss | medium |
| 537 | above si on suppose [E537-12] | `sss` | ssi | low |
| 537 | middle left, before m-bar [E537-15] | `pour ceci` | pour cela | low |
| 537 | middle left, before m-bar [E537-15] | `réduite` | réduit | medium |
| 537 | middle left, before m-bar [E537-15] | `sss` | ssi | low |
| 537 | lower half, following que/si [E537-18] | `la` | — | low |
| 537 | lower half, following que/si [E537-18] | `satisfaite` | word overlaps the marginal note | low |
| 537 | above deleted elle ne [E537-21] | `mais` | — | low |
| 537 | lower quarter, overwritten clause [E537-23] | `qu'elle est satisfaite si` | heavily crossed through; individual endings uncertain | low |
| 537 | lower quarter, overwritten clause [E537-23] | `\mathrm{SL}` | — | low |
| 537 | lower quarter, before général de Steinberg [E537-25] | `th.` | théorème; beginning overlaps margin | low |
| 537 | lower quarter, before général de Steinberg [E537-25] | `se peut-il produire` | opening wording and reading of produire uncertain | low |
| 537 | lower quarter, before général de Steinberg [E537-25] | `cas` | short word before universel indistinct | low |
| 537 | left margin, upper lines [E537-27] | `pour` | word locally overwritten | low |
| 537 | left margin, first centralizer map [E537-28] | `Z_\sigma` | — | low |
| 537 | left margin, first centralizer map [E537-28] | `\widehat{\gamma}_{\rho,\sigma}` | \gamma_{\rho,\sigma} | low |
| 537 | left margin, second centralizer map [E537-29] | `surjections` | surjectives | medium |
| 537 | left margin, lower centralizer map [E537-30] | `Z_\rho` | — | low |
| 537 | left margin, lower centralizer map [E537-30] | `\mathcal{G}_{0,3}^{+\wedge}` | — | low |
| 537 | left margin, lower centralizer map [E537-30] | `réduite` | réduit à | medium |
| 537 | 32, first argument | `tiny dot before ρ` | possibly incidental ink, rather than a mathematical dot | low |
| 537 | 33, second arrow | `right-pointing map` | arrowhead is faint/absent in scan | medium |
| 537 | after respectivement, deleted | `et ssi à` | fragment may end in a symbol rather than à | low |
| 537 | after σ²=1 | `la dernière condition` | initial article is obscured by marginal writing | low |
| 537 | overwritten lower clause | `mais elle` | mais is struck out; attachment of elle uncertain | low |
| 537 | lower matrix-group name | `SL` | initial letters overwritten | medium |
| 537 | margin, first map | `deleted Zσ` | overwritten symbol merges into arrow | low |
| 537 | margin, first target | `γ̂ρ,σ` | γρ,σ; the apparent hat may be part of the underline above | low |
| 537 | margin, lower source | `Zρ` | source heavily overwritten | medium |
| 537 | margin, universal quotient | `G_{0,3}^{+∧}` | plus and completion mark are cramped | medium |
| 538 | proposition 1°, deuxième ligne [E538-03] | `ég` | début de égale | low |
| 538 | proposition 1°, deuxième et troisième lignes [E538-04] | `sss` | ssi | medium |
| 538 | proposition 1°, deuxième et troisième lignes [E538-04] | `donc` | sinon | low |
| 538 | proposition 1°, fin [E538-06] | `sss` | ssi | medium |
| 538 | proposition 2°, début [E538-07] | `sss` | ssi | medium |
| 538 | proposition 2°, début [E538-07] | `donc` | sinon | low |
| 538 | proposition 2°, fin [E538-09] | `sss` | ssi | medium |
| 538 | proposition 2°, fin [E538-09] | `-\sigma^{-1}` | \sigma^{-1} | low |
| 538 | preuve, fin de ligne après SL(2,Z/3Z)′ [E538-14] | `par ex.` | — | low |
| 538 | preuve, fin de ligne après SL(2,Z/3Z)′ [E538-14] | `pour` | — | low |
| 538 | preuve, argument par les traces [E538-16] | `\in` | — | medium |
| 538 | preuve, argument par les traces [E538-16] | `*` | — | medium |
| 538 | deux dernières lignes [E538-24] | `c` | b | low |
| 538 | deux dernières lignes [E538-24] | `veut` | a | medium |
| 538 | deux dernières lignes [E538-24] | `cd` | lettres surchargées | medium |
| 538 | Proposition 2°, dernière ligne, après σ et | `−σ^{-1}` | σ^{-1}; le petit trait peut être une rature ou une tache | low |
| 538 | Preuve, fin de ligne après SL(2,Z/3Z)′, mots biffés | `par ex. pour` | pour; deux ou trois mots très comprimés et traversés par une rature | low |
| 538 | Preuve, après traces distinctes 1 et −1 | `∈(Z/3Z)^*` | le symbole introductif et la marque supérieure sont douteux | low |
| 539 | troisième et quatrième lignes [E539-05] | `sans` | sans est souligné; le signe isolé ressemble à un prime, non à un deuxième point d’exclamation | medium |
| 539 | troisième et quatrième lignes [E539-05] | `d'habitude` | d’hab. | medium |
| 539 | preuve, conjugateurs [E539-09] | `élts` | élms | low |
| 539 | preuve, forme de f [E539-11] | `t` | b | low |
| 539 | preuve, forme de f [E539-11] | `u` | n | low |
| 539 | preuve, après formule de f [E539-12] | `avec` | mot très écrasé sous la rature | medium |
| 539 | preuve, conclusion [E539-13] | `t` | b | low |
| 539 | preuve, conclusion [E539-13] | `u` | n | low |
| 539 | bas, (35), à l’intérieur de la rature [E539-19] | `\mathcal{M}` | M | low |
| 539 | bas, (35), à l’intérieur de la rature [E539-19] | `Z_\rho` | N_\rho | low |
| 539 | bas, (35), à l’intérieur de la rature [E539-19] | `G_{\rho,\sigma}` | \gamma_{\rho,\sigma} | low |
| 539 | bas, (35), à l’intérieur de la rature [E539-19] | `\}` | ) | low |
| 539 | Preuve, coefficients de f et dernière équation quadratique | `t; u` | b; n | medium |
| 539 | (35), première lettre du nom M | `𝓜` | M; distinction de l’alphabet incertaine | medium |
| 539 | (35), deuxième facteur du produit | `Zρ` | Nρ; lettre très surchargée | low |
| 539 | (35), quatrième facteur du produit | `Gρσ` | γρσ; lettre capitale probable | medium |
| 539 | (35), délimiteur après U dans le quadruplet | `}` | ); le contour est celui d’une accolade | low |
| 540 | left, diagonally beside (36) [E540-07] | `\mathrm{GL}(2,\mathbf{Z})` | — | medium |
| 540 | before int(τ_B) [E540-09] | `autom` | autom. | low |
| 540 | before int(τ_B) [E540-09] | `l'élé` | obscured abbreviation | low |
| 540 | middle [E540-11] | `\illegible{2}` | No recoverable word reading after enlargement | low |
| 540 | middle, above crossed text [E540-17] | `groupe` | donc | low |
| 540 | middle, above crossed text [E540-17] | `puis introduisons` | partly obliterated wording | low |
| 540 | after car un [E540-24] | `autom` | autom. | low |
| 540 | left marginal note, last group | `GL(2,Z)` | GL(2,Z) with a short superscript stroke | medium |
| 540 | middle, before En relation | `illegible{2}` | heavy overwriting prevents a defensible reading | low |
| 541 | under GL(2,Z) in (40) [E541-09] | `\mathcal{T}'_{1,1}` | — | medium |
| 541 | above second (40) [E541-11] | `qui est` | que ... | low |
| 541 | in left NB, after et [E541-18] | `\illegible{1}` | No recoverable word reading after enlargement | low |
| 541 | above (42), second crossed word [E541-22] | `un` | — | low |
| 541 | above (42), second crossed word [E541-22] | `du` | — | low |
| 541 | after i.e., before ρ≠ρ⁻¹ [E541-27] | `t-à-l` | abbreviated tout à l’heure | medium |
| 541 | after i.e., before ρ≠ρ⁻¹ [E541-27] | `sss` | short overwritten abbreviation | low |
| 541 | left, before que ρ commute [E541-32] | `en ce cas` | car ... | low |
| 541 | left, before que ρ commute [E541-32] | `implique` | partly obliterated phrase; could include se traduit | low |
| 541 | left, before que ρ commute [E541-32] | `équivalent` | partly obliterated phrase; could include se traduit | low |
| 541 | left, before que ρ commute [E541-32] | `en fait` | on fait | low |
| 541 | bottom, across page [E541-36] | `\varphi` | — | medium |
| 541 | (39), equality sign | `double underlined =` | an additional equals sign below the baseline | medium |
| 541 | identification inserted below GL(2,Z) | `T′_{1,1}` | calligraphic alphabet uncertain | medium |
| 541 | NB in left margin, after et | `illegible{1}` | overwritten short word | low |
| 541 | above (42), crossed articles | `un; du` | son; des | low |
| 541 | last lower-right symbol after épimorph. | `φ` | pen flourish | low |
| 542 | top left [E542-01] | `(43)` | — | low |
| 542 | top heading [E542-02] | `Système` | Soit; Situons | low |
| 542 | after heading [E542-03] | `\mathfrak{g}` | g | medium |
| 542 | upper quarter, (44) [E542-04] | `\mathfrak{g}` | g | medium |
| 542 | upper quarter, (44) [E542-04] | `*` | — | medium |
| 542 | below (44) [E542-06] | `36` | — | low |
| 542 | below (44) [E542-06] | `\mathfrak{g}` | g | medium |
| 542 | below (44) [E542-06] | `*` | — | low |
| 542 | below (44) [E542-06] | `\mathfrak{g}` | g | medium |
| 542 | below (44) [E542-06] | `\exists` | — | low |
| 542 | inside definition below Σ in (45) [E542-09] | `\mathfrak{g}` | g | medium |
| 542 | inside definition below Σ in (45) [E542-09] | `*` | — | medium |
| 542 | inside definition below Σ in (45) [E542-09] | `\eta` | \zeta | low |
| 542 | inside definition below Σ in (45) [E542-09] | `\beta\sigma(\beta)^{-1}` | — | low |
| 542 | middle [E542-11] | `\mathfrak{g}` | g | medium |
| 542 | middle [E542-11] | `*` | — | medium |
| 542 | middle [E542-11] | `construction` | word ending compressed at frame | medium |
| 542 | left vertical margin, (46bis) [E542-13] | `46\mathrm{bis}` | — | medium |
| 542 | left vertical margin, (46bis) [E542-13] | `\mathfrak{g}` | g | medium |
| 542 | below middle insertion [E542-14] | `\mathfrak{g}` | g | medium |
| 542 | first condition in (47) [E542-19] | `\mathfrak{g}` | g | medium |
| 542 | first condition in (47) [E542-19] | `*` | — | medium |
| 542 | first condition in (47) [E542-19] | `\chi(\mu)` | \chi(\beta) | low |
| 542 | after δσ(β)=1 in (48) [E542-22] | `\mathfrak{g}` | g | medium |
| 542 | after δσ(β)=1 in (48) [E542-22] | `*` | — | medium |
| 542 | after δσ(β)=1 in (48) [E542-22] | `\mathfrak{g}` | g | medium |
| 542 | after δσ(β)=1 in (48) [E542-22] | `*` | — | medium |
| 542 | after δσ(β)=1 in (48) [E542-22] | `S\mathfrak{g}` | Sg | low |
| 542 | after δσ(β)=1 in (48) [E542-22] | `\}` | — | low |
| 542 | top cancelled number and g | `(43); g` | overwritten number; calligraphic or Gothic g | low |
| 542 | superscripts on g in (44), (45), (47), (48) | `*` | overwritten star or other superscript; eff is separately visible where written | medium |
| 542 | cancelled display below (44) | `(36), g^{* eff} = {(α,β,μ)∈g* &#124; ∃` | number overwritten; final existential sign heavily retraced | low |
| 542 | definition of Σ below (45), second line | `ησ` | ζσ | medium |
| 542 | definition of Σ below (45), cancellation before η | `βσ(β)^{-1}` | ε₂(μ) or another overwritten factor | low |
| 542 | left marginal map number | `46bis` | overwritten 46 plus bis | medium |
| 542 | (47), deleted argument before μ | `χ(μ)` | χ(β) | low |
| 542 | (48), membership in the last set | `Sg*_{ρ,σ}` | g*_{ρ,σ}; visible initial stroke retained as S | medium |
| 542 | (48), after first =1 | `cancelled closing brace` | overwritten punctuation or connective | low |
| 543 | upper quarter, (49) [E543-02] | `\mathfrak{g}` | g | low |
| 543 | upper quarter, (49) [E543-02] | `*` | — | medium |
| 543 | below (49) [E543-03] | `dont l'i` | dont l'im; initial words abbreviated or unfinished | low |
| 543 | upper middle [E543-04] | `\mathfrak{g}` | g | low |
| 543 | upper middle, (50) [E543-05] | `\mathfrak{g}` | g | low |
| 543 | upper middle, (50) [E543-05] | `\mathfrak{g}` | g | low |
| 543 | upper middle, (50) [E543-05] | `\mathfrak{g}` | g | low |
| 543 | upper middle, (50) [E543-05] | `\delta_\rho` | \delta_B | low |
| 543 | right-hand source in (51) [E543-10] | `\mathfrak{g}` | g | low |
| 543 | right-hand source in (51) [E543-10] | `\varphi` | * | low |
| 543 | first coordinate of (52) [E543-14] | `\varphi` | * | low |
| 543 | first coordinate of (52) [E543-14] | `\alpha=` | — | low |
| 543 | before calculation [E543-15] | `\overset{\mathrm{dfn}}{=}` | = | low |
| 543 | lower quarter [E543-17] | `\tau` | \tau' | low |
| 543 | lower quarter [E543-17] | `\tau` | \tau' | low |
| 543 | lower quarter [E543-17] | `\tau` | \tau' | low |
| 543 | lower quarter [E543-17] | `\varepsilon u` | u | low |
| 543 | after Donc [E543-19] | `l'ens` | les | low |
| 543 | inside last insertion [E543-21] | `des` | — | low |
| 543 | inside last insertion [E543-21] | `\mathfrak{g}_{\rho,\sigma}(u,\mu)` | g_{\rho,\sigma}^{(u,\mu)} | low |
| 543 | last paragraph continuation [E543-27] | `-` | — | medium |
| 543 | last paragraph continuation [E543-27] | `l'image` | dash may be a continuation stroke; l'image compressed | medium |
| 543 | above χB(u) in last display [E543-24] | `\Longrightarrow` | = | low |
| 543 | above χB(u) in last display [E543-24] | `[` | ( | low |
| 543 | last words [E543-25] | `sera exactement` | word endings highly compressed | medium |
| 543 | (49) and throughout new triple sets | `g in a possibly Gothic alphabet` | ordinary g; \mathfrak{g} retained as an explicitly doubtful typographical choice | medium |
| 543 | (49), superscript on Σ | `*` | overwritten superscript | medium |
| 543 | (50), second condition | `δρ(ατ′^{ν₃(μ)})=1` | subscript B; rho is retraced | medium |
| 543 | (51) and (52), following the source u | `deleted φ` | deleted star or overwritten symbol | low |
| 543 | (52), first target coordinate | `deleted α=` | overwritten pair of symbols | medium |
| 543 | parenthesis introducing ε | `definition sign over =` | ordinary = followed by a retraced stray sign | low |
| 543 | expanded calculation, internal powers of τ | `τ without prime` | τ′ with a prime hidden in the superscript | low |
| 543 | expanded calculation, last equality | `εuσ(u)^{-1}=η` | uσ(u)^{-1}=η; thick retraced initial mark | low |
| 543 | last paragraph, insertion | `l'ens [deleted des] g_{ρ,σ}(u,μ)` | deleted word uncertain | medium |
| 543 | last display, relation and outer delimiter | `deleted ⇒ or =; opening [ and closing )` | opening ( angularly drawn; relation overwritten | low |
| 543 | last insertion, fiber label | `g_{ρ,σ}(u,μ) with inline arguments` | g_{ρ,σ}^{(u,μ)}; the large descending g makes vertical placement uncertain | medium |
| 544 | top left [E544-01] | `les` | an overwritten word | low |
| 544 | above (53), leading into set [E544-02] | `\mathfrak{g}_{\rho,\sigma}(u,\mu)` | g_{\rho,\sigma}^{(u,\mu)} | low |
| 544 | top, (53) [E544-03] | `\beta` | b | low |
| 544 | beneath tuple in (53) [E544-04] | `\}` | — | medium |
| 544 | beneath tuple in (53) [E544-04] | `\nu_2` | — | medium |
| 544 | below b∈Nσ in (54) [E544-29] | `\mathfrak{g}_{\rho,\sigma}(u,\mu)` | g_{\rho,\sigma}^{(u,\mu)} | low |
| 544 | middle [E544-09] | `\mathfrak{g}` | g | low |
| 544 | middle, first (56) [E544-10] | `\alpha=` | — | medium |
| 544 | below (57) [E544-14] | `ds` | dans | medium |
| 544 | lower middle, (54 or 58) [E544-17] | `54` | 58 | low |
| 544 | lower middle, (54 or 58) [E544-17] | `\mathfrak{g}_{\rho,\sigma}(u,\mu)` | g_{\rho,\sigma}^{(u,\mu)} | low |
| 544 | prefix in second (55) [E544-20] | `S_0` | — | low |
| 544 | prefix in second (55) [E544-20] | `\mathcal{M}` | M | low |
| 544 | prefix in second (55) [E544-20] | `B` | — | medium |
| 544 | second prefix in bottom maps [E544-24] | `S_0` | — | low |
| 544 | second prefix in bottom maps [E544-24] | `\mathcal{M}` | M | low |
| 544 | second prefix in bottom maps [E544-24] | `\longleftrightarrow` | \longrightarrow | low |
| 544 | second prefix in bottom maps [E544-24] | `S_0` | — | low |
| 544 | second prefix in bottom maps [E544-24] | `\mathcal{M}` | M | low |
| 544 | right of bottom maps [E544-28] | `notés` | — | low |
| 544 | fiber labels above (53), in (54), and in the formula after (57) | `g_{ρ,σ}(u,μ) with inline arguments` | g_{ρ,σ}^{(u,μ)}; alphabet may be ordinary g rather than Gothic | medium |
| 544 | (53), label over second coordinate | `β` | b | medium |
| 544 | insertion below (53) | `closing brace after tuple; exponent ν₂` | overwritten closing parenthesis; exponent retraced | low |
| 544 | (54) and (56), second coordinate | `u iσ(b), no inverse written` | an inverse might have been omitted by the writer; none supplied | high |
| 544 | (56), before ua₀⁻¹ | `α=` | retraced or cancelled α= | medium |
| 544 | bottom definitions (55)–(56) | `cancelled S₀ preceding M_{ρ,σ}[0]` | another overwritten prefix | medium |
| 544 | bottom M notation | `calligraphic M` | plain M | medium |
| 544 | right side of bottom (55) | `B_{ρ,σ}` | letter heavily retraced over a previous form | medium |
| 544 | bottom (56), ερ arrow | `left and right arrowheads visible` | the left-facing mark may be a pen-start flourish on an ordinary right arrow | low |
| 544 | right margin beside bottom (56) | `deleted notés ε′ρ` | noter ε′ρ | low |
| 545 | (57), left object [E545-03] | `S_0` | — | low |
| 545 | (57), left object [E545-03] | `simplem$^{t}$` | simplement | low |
| 545 | (58), left object [E545-06] | `S_0` | — | low |
| 545 | (58), left object [E545-06] | `\varepsilon_\sigma` | — | medium |
| 545 | (59), left object [E545-09] | `S_0` | — | low |
| 545 | (59), left object [E545-09] | `\varepsilon_2` | — | medium |
| 545 | (60), above overwritten condition [E545-14] | `S_0` | — | low |
| 545 | (60), above overwritten condition [E545-14] | `\mathrm{eff}` | — | medium |
| 545 | (60), above overwritten condition [E545-14] | `S_0\{M_{\rho,\sigma}\}` | — | medium |
| 545 | (60), above overwritten condition [E545-14] | `\varepsilon_3(\chi_B(u))` | — | low |
| 545 | oblique, right of (61) [E545-17] | `à leurs images` | Compressed words overlap the main line. | medium |
| 545 | left marginal note, before ν_ρ(a) [E545-19] | `(61)` | (64); the numerical-looking inscription is overstruck. | low |
| 545 | below (61) [E545-20] | `injective` | Word is heavily retraced; ending is compressed. | medium |
| 545 | above (61) in Remarque [E545-23] | `définissent` | définissent / définissent-looking overwritten word | medium |
| 545 | (57)–(60), initial prefixes | `S_0 (deleted/overwritten)` | The initial letter and subscript are heavily overwritten. | low |
| 545 | (58), arrow label, first component | `ε_σ` | ε_ρ beneath overwritten strokes | medium |
| 545 | (59), arrow label | `ε_2` | The subscript is overwritten. | medium |
| 545 | (60), left-hand superscript | `eff` | Overwritten eff and subscript [0] overlap. | medium |
| 545 | (60), ambient set following x ∈ | `S_0{M_{ρ,σ}}` | S_0 M_{ρ,σ} followed by a condition bar; delimiter shape is unclear. | low |
| 545 | (60), deleted condition under the insertion | `ε_3(χ_B(u))` | Inner argument and subscript are obscured by dense cancellation. | low |
| 546 | (63), small mark below left brace [E546-03] | `\varepsilon'` | — | medium |
| 546 | (63), small mark below left brace [E546-03] | `\alpha` | — | low |
| 546 | upper third, after B_{ρ,σ} sera [E546-06] | `sera` | Short cursive word under the insertion inclus. | medium |
| 546 | upper third, after B_{ρ,σ} sera [E546-06] | `inv.` | $\triangleleft$ | low |
| 546 | upper third, after B_{ρ,σ} sera [E546-06] | `d'index` | d'indice | medium |
| 546 | upper third, after B_{ρ,σ} sera [E546-06] | `convenable` | Initial letters are crowded/retraced. | medium |
| 546 | middle, before éliminer [E546-08] | `tuer` | Canceled word cannot be resolved securely. | low |
| 546 | middle, before éliminer [E546-08] | `\overline{\mathrm m}` | — | medium |
| 546 | above (64), two pieces [E546-09] | `\beta'` | — | low |
| 546 | above (64), two pieces [E546-09] | `est lié` | Final word is traversed by cancellation. | low |
| 546 | lower half [E546-13] | `qu'un` | qui un | medium |
| 546 | lower quarter, (66) [E546-14] | `\chi` | — | medium |
| 546 | below (66), line-end group [E546-17] | `\mathcal G_{0,3}^{+\wedge}` | — | low |
| 546 | lower quarter [E546-18] | `\textcircled{1}` | — | medium |
| 546 | (67), below retraced σ [E546-21] | `\varepsilon` | — | low |
| 546 | (67), below retraced σ [E546-21] | `\sigma` | — | medium |
| 546 | (63), exponent of ρ | `ε′` | Retraced exponent; prime is small. | medium |
| 546 | (63), deleted mark below left brace | `α` | Small canceled beginning of a further formula. | low |
| 546 | middle, qui est présent ... si | `m with overbar (même)` | Appears as two short horizontal strokes. | medium |
| 546 | deleted formula above (64) | `β′ = τ′^ν β′` | Left β′ is heavily retraced; right prime is visible. | low |
| 546 | (66), first character | `χ` | Retraced/overwritten sign. | medium |
| 546 | below (66), deleted group | `G_{0,3}^{+hat}` | Superscripts heavily struck through. | low |
| 546 | unnumbered group equality before (67) | `circled 1 after the completion mark` | The tiny circled superscript could be another annotation. | low |
| 546 | (67), βσ(β)^{-1} | `σ; deleted ε below it` | The lower canceled symbol is not securely distinguishable. | low |
| 547 | top, right of dans [E547-02] | `\mathcal G=\mathcal G_{1,1}^{+\wedge}` | — | low |
| 547 | lower half, first paragraph [E547-09] | `achever` | Compressed ending; possible related verb form. | medium |
| 547 | after mérite [E547-12] | `aussi` | — | low |
| 547 | after mérite [E547-12] | `\widehat{\mathbb Z}` | \mathbb Z | low |
| 547 | top line, canceled symbols | `G = G_{1,1}^{+hat}` | First glyph may be T; relational mark and superscripts are crossed out. | low |
| 547 | lower-half paragraph, after mérite | `aussi (deleted)` | The word is almost entirely covered by a horizontal strike; the final i dot remains visible. | low |
| 547 | lower half, SL expression after il correspond à | `SL(2,Z-hat)^hat` | SL(2,Z)^hat; an extra hat-like stroke is visibly above the Z. | low |
| 548 | upper text, line 2 [E548-02] | `par` | — | low |
| 548 | upper text, line 2 [E548-02] | `via` | — | medium |
| 548 | below (**) [E548-06] | `vertueux` | ['final strokes are compressed; no stronger competing reading'] | medium |
| 548 | below (**) [E548-06] | `mais` | — | medium |
| 548 | below unnumbered display [E548-08] | `est` | — | medium |
| 548 | oblique left margin, upper-middle [E548-09] | `élément` | ['éliminé (weaker candidate)', 'letter endings obscured by the main text crossing the note'] | low |
| 548 | oblique left margin, upper-middle [E548-09] | `\prime` | — | medium |
| 548 | oblique left margin, upper-middle [E548-09] | `1` | — | medium |
| 548 | oblique left margin, upper-middle [E548-09] | `\mathcal M` | — | medium |
| 548 | oblique left margin, upper-middle [E548-09] | `!` | \prime | low |
| 548 | above diagram (1) [E548-13] | `=` | \to | low |
| 548 | lower half, (1) [E548-14] | `*` | + | low |
| 548 | upper text, line 2, after L_sigma | `deleted par; via` | ['par under the cancellation is fairly plausible; the replacement may also be an abbreviated par'] | medium |
| 548 | upper text, line before the unnumbered tau(rho) display | `mais dont` | ['mais is partly crossed by the oblique marginal note'] | medium |
| 548 | upper text, line following the unnumbered tau(rho) display | `est moins commode` | ['est is partly crossed by the oblique marginal note'] | medium |
| 548 | oblique left marginal note, rigidity relation, second Pi | `widehat(Pi)_{0,3}^{prime rho}` | ['widehat(Pi)_{0,3}^{rho}, without prime'] | low |
| 548 | oblique left marginal note, group following alors que dans | `{1,tau prime}.widehat(Pi)_{0,3}` | ['the first entry is heavily overwritten; 1 is the best remaining reading'] | low |
| 548 | oblique left marginal note, final group symbol | `calligraphic M_{0,3}^{!}` | ['M_{0,3}^{prime}', 'the alphabet and the elevated mark are both uncertain'] | low |
| 548 | isolated small ink mark above diagram (1) | `=` | ['right arrow', 'possibly an abandoned nonsemantic pen mark; preserved rather than discarded'] | low |
| 548 | diagram (1), superscript before the completion hat on T_{1,1} | `*` | ['+', 'a compact correction or overwriting of a preceding sign may be present'] | low |

## 3. Abbreviations encountered

Expansions below are editorial aids only; they are not substituted into the transcription. Different written forms are retained as separate entries. Some abbreviations and their expansions are themselves tentative, especially where a terminal stroke or point is unclear.

| Written form | Proposed expansion / meaning | Scan(s) |
|---|---|---|
| `1/2 direct` | semi-direct | 536 |
| `\overline{\mathrm m}` | même | 541 |
| `autom` | automorphisme | 535, 540 |
| `autom.` | automorphisme | 530, 533, 534 |
| `can.` | canonique | 544 |
| `Centr` | centre (here; reading uncertain); centre (reading uncertain); centralisateur | 535, 536, 537, 539, 540 |
| `cf` | confer | 533, 542, 544 |
| `conj.` | conjugué | 542 |
| `cor.` | corollaire | 542 |
| `dfn` | définition; définition (reading uncertain here) | 530, 540, 541, 542, 543, 545 |
| `ds` | dans; dans (reading uncertain) | 542, 544 |
| `eff` | effectif (lecture de l’exposant); effectif; effectif / effectif(ve), used as a superscript | 534, 542, 543, 544, 545, 546 |
| `ens.` | ensemble | 542 |
| `f.` | faut | 533 |
| `f. et s.` | faut et suffit; faut et suffit (deleted; reading uncertain) | 531, 535 |
| `form.` | formule ou formulaire (lecture incertaine); forme (lecture incertaine) | 530, 534 |
| `gr.` | groupe | 532 |
| `hom` | homomorphisme; homomorphismes / homomorphisme; homomorphismes; homomorphisme (no terminal full stop visible here) | 535, 536, 537, 548 |
| `hom.` | homomorphisme; homomorphismes | 530, 540, 541, 545 |
| `i.e.` | id est | 531, 532, 533, 535, 537, 538, 539, 540, 541, 542, 544, 546 |
| `Im` | image | 535, 539 |
| `int` | automorphisme intérieur; automorphisme intérieur / conjugaison; automorphisme intérieur / conjugaison intérieure | 532, 534, 535, 536, 546, 547 |
| `inv. (?)` | invariant | 546 |
| `Ker` | noyau; kernel, noyau | 536, 539 |
| `l'ens` | l'ensemble | 543, 544 |
| `l'hom.` | l'homomorphisme | 544 |
| `lui-\overline{\mathrm m}` | lui-même | 540 |
| `l’ens.` | l’ensemble | 534 |
| `l’expr.` | l’expression | 534 |
| `m with overbar` | même | 546, 547 |
| `mod` | modulo | 538, 542 |
| `m̄` | même | 531, 532, 537 |
| `NB` | nota bene | 540, 541, 545 |
| `néc.^t` | nécessairement | 533 |
| `OK.` | validation or approval of the preceding calculation | 543 |
| `p.` | page | 542 |
| `p.ex.` | par exemple | 537 |
| `par ex. (biffé; lecture incertaine)` | par exemple | 538 |
| `pts` | points | 546 |
| `simplem^t (?)` | simplement | 545 |
| `sous-gr.` | sous-groupe | 546 |
| `sss` | si et seulement si | 540, 541 |
| `sss (lecture incertaine)` | si et seulement si (reading uncertain); si et seulement si (abbreviation uncertain); si et seulement si | 535, 537, 538 |
| `t-à-l` | tout à l’heure (reading uncertain) | 541 |
| `th.` | théorème (uncertain reading) | 537 |
| `tjrs` | toujours | 535 |
| `élts (lecture incertaine)` | éléments | 539 |
| `élém.` | élément | 533 |
| `épi` | épimorphisme | 538, 548 |
| `épi.` | épimorphisme | 542 |
| `épimorph.` | épimorphismes | 541 |

## 4. Legibility and limits

The principal uncancelled displays are generally more legible than the running prose. The least secure material is the oblique lower-left note on scan 530; the superposed cancelled calculations on scans 532–533; the extensively cancelled text and diagonal margin on scan 537; overwritten parameter-space names, superscripts, primes, and inverse signs on scans 542–545; and the diagonal marginal note on scan 548. Those regions contain tentative readings that require editorial comparison with the images. Short endings, omitted-looking points, and repetition strokes can remain ambiguous even after enlargement. No uncertainty mark should be taken as a reconstruction of an established mathematical statement.

All nineteen scans have been transcribed and inventoried, including the final page and the visible cancelled material. The text was checked for balanced braces, environments, and mathematical delimiters. A full TeX compilation could not be completed in this environment because the installed engines lack their LaTeX formats and package tree; the delivered file remains the requested preamble-free fragment, and its final editorial rendering should be checked in the host document.

## 5. Research notes (English)

These notes are separate from the diplomatic text and never determine a reading. Each item cites its scan and location in the supplied manuscript (Grothendieck, 1981). The **conjecture** category also includes explicit questions and conditional expectations; it does not turn those passages into formally stated conjectures. **Unproved claim** means that a proof is absent or deferred at the cited location, not that the statement is an open problem. Cancelled claims are identified as such. Later treatment elsewhere in the manuscript or literature remains possible. Every **own idea** is a proposed check or direction, with confidence and reasons; no novelty is asserted.

### R530-01 — unproved claim

**Location:** Scan 530, upper left margin, beside (1). (Grothendieck, 1981, scan 530.)

**Source phrase:** Ceci signifie simplement qu’on se donne un hom. surjectif

The margin identifies the generator relations with a surjection from the profinite completion of SL(2,Z). Checking the statement requires retaining the topological generation assumption added above the first sentence, together with the precise presentation and the universal property of profinite completion.

### R530-02 — unpursued implication

**Location:** Scan 530, middle, after (2). (Grothendieck, 1981, scan 530.)

**Source phrase:** passe au quotient

The qualification about τ∞ descending separates a quotient carrying the displayed generators from one whose defining kernel is invariant under the proposed involution. A comparison across the subsequent construction should keep that extra descent datum visible.

### R530-03 — own idea

**Location:** Scan 530, (1)–(4) and left middle margin. (Grothendieck, 1981, scan 530.)

One can test the two involutions τ and τ′ on small finite quotients while tracking whether the kernel of the original presentation is invariant. Such tests could expose a lost conjugation or sign in a reading, but must never be used to replace the manuscript reading.

**Confidence:** high. **Reason:** This is a finite algebraic verification procedure, proposed as a separate research check rather than textual evidence.

### R531-01 — unpursued implication

**Location:** Scan 531, (8) and second (9). (Grothendieck, 1981, scan 531.)

**Source phrase:** ρ^μ=ρ^{ε₃(μ)}

The two finite sign characters record different reductions of the multiplier: one is attached to ρ and the other to σ. Their simultaneous appearance suggests retaining separate mod-3 and mod-4 bookkeeping in any comparison of the later normalizers.

### R531-02 — unproved claim

**Location:** Scan 531, bottom, Proposition. (Grothendieck, 1981, scan 531.)

**Source phrase:** il f. et s. qu’il existe

The proposition begins an equivalence between membership in B_{ρ,σ} and conjugator data. Its statement continues on the next scan, so the quantifiers, the ambient coset of α, and the cusp-power condition must be read across that page boundary before attempting a proof.

### R531-03 — own idea

**Location:** Scan 531, (8)–(9). (Grothendieck, 1981, scan 531.)

A four-case table for the two signs, indexed by units modulo 12, would provide a compact independent check of the subsequent parity conditions. This would be an auxiliary calculation, not an emendation of the manuscript.

**Confidence:** high. **Reason:** The stated generator orders make the two finite reductions directly testable.

### R532-01 — unproved claim

**Location:** Scan 532, after (15). (Grothendieck, 1981, scan 532.)

**Source phrase:** μ est déterminé en fonction de u

The assertion is explicitly conditional on injectivity of the procyclic parameterization in (15). A proof should explain why the action on its image determines a unique continuous multiplier and why that multiplier is a unit for an automorphism.

### R532-02 — unproved claim

**Location:** Scan 532, last paragraph, continuing on next scan. (Grothendieck, 1981, scan 532.)

**Source phrase:** on a vu que α à lui tout seul

A preceding result is invoked to recover more of the multiplier data from the first conjugator when the group maps to the indicated congruence quotient. The referenced argument is not reproduced here; the continuation on scan 533 should be included before specifying the exact conclusion.

### R532-03 — own idea

**Location:** Scan 532, (15) and following paragraph. (Grothendieck, 1981, scan 532.)

If (15) is not injective, the ambiguity in μ can be described by the action of units of the profinite integers on the quotient by the kernel of that map. Comparing B_{ρ,σ} for finite and infinite procyclic images would isolate which multiplier information is actually remembered by u.

**Confidence:** medium. **Reason:** The proposal follows the stated injectivity dependence, but its exact formulation needs the quotient and continuity hypotheses fixed.

### R533-01 — conjecture

**Location:** Scan 533, upper quarter, question before the cancelled calculation. (Grothendieck, 1981, scan 533.)

**Source phrase:** Mais quelles conditions doivent satisfaire (α,β,μ)

This is an explicit question, not an asserted conjecture: which triples determine an element of B_{ρ,σ}? The following text separates existence of an automorphism with the prescribed images from the additional peripheral condition, so a reconstruction should check both requirements independently.

### R533-02 — unproved claim

**Location:** Scan 533, upper quarter, parenthetical uniqueness. (Grothendieck, 1981, scan 533.)

**Source phrase:** néc.ᵗ unique

Uniqueness is asserted for an automorphism satisfying (14). Its justification uses the stated topological generation by ρ and σ together with continuity; existence and invertibility remain separate issues.

### R533-03 — unproved claim

**Location:** Scan 533, lower quarter, beside u(ε′₀)=−u(ε₀). (Grothendieck, 1981, scan 533.)

**Source phrase:** car u(−1)=−1 cf ci-dessous

The preservation of −1 is explicitly deferred. The lemma on the following scan supplies the intended argument from the conjugacy condition on σ.

### R533-04 — own idea

**Location:** Scan 533, upper quarter, condition on ζ and η. (Grothendieck, 1981, scan 533.)

One could test the distinction between generator assignments and automorphisms in finite quotients carrying the displayed generators, recording separately relation preservation, surjectivity, and the peripheral power condition. This would test the logical independence of the conditions without changing the manuscript’s formulas.

**Confidence:** medium. **Reason:** Finite groups permit exact checking, but a finite collection of examples would not establish the corresponding profinite statement.

### R534-01 — unpursued implication

**Location:** Scan 534, upper middle, lemma. (Grothendieck, 1981, scan 534.)

**Source phrase:** u(−1)=−1

The lemma proves preservation of the distinguished central element using u(σ) conjugate to σ or σ⁻¹. It supplies the justification deferred on scan 533; distinguishing this central element from an arbitrary element of order two matters when passing between central and projective quotients.

### R534-02 — unproved claim

**Location:** Scan 534, lower quarter, corollary (18). (Grothendieck, 1981, scan 534.)

**Source phrase:** est injective, et elle a comme image

The corollary packages an automorphism and multiplier into two commutator coordinates and μ. The image conditions continue on scan 535 and include an existence requirement for an automorphism, so the displayed conjugacy and power equations alone are not asserted here to suffice.

### R534-03 — unpursued implication

**Location:** Scan 534, second (17), character ν₃. (Grothendieck, 1981, scan 534.)

**Source phrase:** qu’on écrit aussi

The multiplicative sign condition is rewritten using the additive exponent ν₃. Comparing this convention with subsequent occurrences of τ and τ′ would help audit which representative of the order-two extension is being used; the handwritten revisions should remain distinct.

### R534-04 — own idea

**Location:** Scan 534, (16) and corollary (18). (Grothendieck, 1981, scan 534.)

The identity ζ=ηl₁^ν suggests eliminating one commutator coordinate when studying the image of (18). Any such reformulation would still have to retain both the automorphism-existence requirement and the sign restrictions on conjugating elements.

**Confidence:** medium. **Reason:** The coordinate elimination follows formally from the displayed identity, whereas its usefulness and global sufficiency are not established on this page.

### R535-01 — unproved claim

**Location:** Scan 535, upper third, referenced conditions and (A). (Grothendieck, 1981, scan 535.)

**Source phrase:** conditions 1°), 2°), [3° ou 4°]

The amended paragraph asserts an equivalence with an existence statement for (α,β), but the third referenced condition is uncertain (3° or 4°). The last displayed η-expression visibly reads η=ε₂(μ); an editor should compare it with the preceding conjugation formulas without supplying a missing factor. A proof would need to determine exactly which listed conditions are being combined.

### R535-02 — unpursued implication

**Location:** Scan 535, (19)–(23). (Grothendieck, 1981, scan 535.)

**Source phrase:** Il est injectif si on suppose tjrs

The injection of L₀ through inner automorphisms uses the condition L₀∩Centr(G)={1}. If that condition is dropped, the same construction naturally invites tracking the central intersection as a kernel, rather than merely omitting the exact sequence.

### R535-03 — unproved claim

**Location:** Scan 535, (24)–(25). (Grothendieck, 1981, scan 535.)

**Source phrase:** dont le noyau est noté

The terminal arrow to 1 in (25) presents the multiplier map as surjective. On this page that surjectivity receives no separate proof; a proof must identify the allowable multipliers for the particular profinite quotient being used.

### R536-01 — unproved claim

**Location:** Scan 536, (28)–(31). (Grothendieck, 1981, scan 536.)

**Source phrase:** dont l’image est invariante

The construction divides the semidirect product by the image of l↦int(l)·l⁻¹. Establishing that the quotient is well defined requires checking the claimed invariance (normality) under both factors, using the multiplier action on L₀.

### R536-02 — unpursued implication

**Location:** Scan 536, (30)–(31). (Grothendieck, 1981, scan 536.)

**Source phrase:** ce qu’on va supposer par la suite

The displayed kernel calculation isolates L₀∩Centr(G) as the precise obstruction to embedding the original group into Gρ,σ. It suggests a version of the construction retaining that central kernel when hypothesis (20) is unavailable.

### R536-03 — own idea

**Location:** Scan 536, (28) and (30). (Grothendieck, 1981, scan 536.)

One could formulate this quotient as a pushout for the compatible inner action of L₀, then compare its universal property with the displayed diamond. The relevant category and closure of the diagonal subgroup must be specified in the profinite setting.

**Confidence:** medium. **Reason:** The diamond and quotient by int(l)·l⁻¹ have the expected amalgamation shape, but a categorical claim needs an explicit universal-property proof.

### R537-01 — unproved claim

**Location:** Scan 537, (32)–(33), before the large cancellation. (Grothendieck, 1981, scan 537.)

**Source phrase:** images qui contiennent

The images of the two centralizers are asserted to contain the two index-two multiplier kernels respectively. A proof must use the relevant conjugacy classes in the original profinite group and the action of the extension on ρ and σ.

### R537-02 — unproved claim

**Location:** Scan 537, cancelled lower paragraph, Steinberg reference. (Grothendieck, 1981, scan 537.)

**Source phrase:** général de Steinberg p.ex.

The cancelled draft invokes a theorem of Steinberg in a discussion of conjugacy of σ and −σ in SL(2,Ẑ). This is not a retained result: identifying the exact theorem and verifying its hypotheses over the integral/profinite coefficient ring would be necessary before accepting the proposed application.

### R537-03 — conjecture

**Location:** Scan 537, cancelled final question. (Grothendieck, 1981, scan 537.)

**Source phrase:** universel SL(2,Z)^∧ = G_{1,1}^{+∧} ?

The cancelled draft asks about the corresponding phenomenon in the universal completion. The opening words are difficult to read, but the universal group and question mark are clear; it should be tracked as a cancelled question, not as a conjecture confidently maintained by the author.

### R537-04 — own idea

**Location:** Scan 537, cancelled main paragraph and marginal note. (Grothendieck, 1981, scan 537.)

Finite congruence quotients could be used to test the draft’s competing assertions that an element and its inverse are conjugate. One should separately test SL and its central quotient, and distinguish such finite obstructions from a proof about the full profinite completion.

**Confidence:** high as a proposed check, not as a claim of a new result. **Reason:** Conjugacy in a group always descends to its quotients, whereas the converse is the substantive issue being explored.

### R538-01 — unproved claim

**Location:** Scan 538, Proposition 1° et 2°. (Grothendieck, 1981, scan 538.)

**Source phrase:** L’image δρ(Zρ) contient γ′ρσ

The proposition characterizes when the centralizer images equal the indicated index-two subgroups and when they fill the quotient. A proof should track the quotient character and the existence of conjugators between each distinguished generator and its inverse; the page states the equivalences without an independent proof.

### R538-02 — unpursued implication

**Location:** Scan 538, Corollaire 1 et sa preuve. (Grothendieck, 1981, scan 538.)

**Source phrase:** Si G contient comme quotient SL(2,Z/3Z)′

A finite quotient is used to obstruct conjugacy in the original profinite group. The final determinant equation exposes a concrete arithmetic obstruction; testing how this obstruction behaves under other finite quotients could clarify which part of the centralizer image is forced by a small quotient.

### R538-03 — own idea

**Location:** Scan 538, Preuve, dernière ligne. (Grothendieck, 1981, scan 538.)

**Source phrase:** c²+cd+d²=−1, impossible

Own idea: organize the conjugacy obstruction through the determinant map on the centralizer algebra of ρ, then compare its image across congruence quotients. This is a proposed way to systematize the written computation, not a claimed theorem or novelty.

**Confidence:** medium. **Reason:** The displayed conjugators f=cρ+d and their determinants motivate such a reformulation; broader validity would require additional hypotheses.

### R539-01 — unpursued implication

**Location:** Scan 539, Corollaire 2, premières lignes. (Grothendieck, 1981, scan 539.)

**Source phrase:** Si σ²=1, alors Zσ → γρσ est surjectif

The corollary separates the involutory case from the case detected by a quotient SL(2,Z/4Z). The role of retaining the central sign is emphasized by the parenthetical read as “sans ′ !”; a comparison with the corresponding primed quotient would require checking precisely which central information is lost.

### R539-02 — own idea

**Location:** Scan 539, Preuve du corollaire 2, dernière équation. (Grothendieck, 1981, scan 539.)

**Source phrase:** t²+u²=−1, impossible

Own idea: compare the mod-4 determinant obstruction for σ with the mod-3 determinant obstruction for ρ on the preceding scan. These may give two independently computable tests for the two quotient characters, but that interpretation must be checked against the definitions and is not an assertion of novelty.

**Confidence:** medium. **Reason:** The two adjacent proofs use distinct congruence quotients and different quadratic determinant forms.

### R539-03 — unpursued implication

**Location:** Scan 539, Constructions barrées (34) et (35). (Grothendieck, 1981, scan 539.)

**Source phrase:** S₀𝓜ρσ ⊂ Bρσ × Zρ × Zσ × Gρσ

The canceled draft combines kernels and centralizers with a compatibility condition among their quotient maps. It is a possible precursor to a fiber-product construction, but it must be treated as a discarded formulation and compared with the later replacement before drawing consequences.

### R540-01 — unpursued implication

**Location:** Scan 540, (36), marginal NB. (Grothendieck, 1981, scan 540.)

**Source phrase:** « G′ est un quotient de GL(2,Z)^∧ »

The marginal identification suggests comparing the involution τ with the determinant −1 component of the completed integral linear group. The kernel of the asserted quotient is not specified on this page, and would have to be retained in any such comparison.

### R540-02 — own idea

**Location:** Scan 540, (37)–(38), lower paragraph. (Grothendieck, 1981, scan 540.)

Compare the external semidirect product N_σ={1,τ_B}.Z_σ with its image in G_{ρ,σ} when σ becomes an involution in a quotient. The proof here reduces the normalizer image to two cosets, so degeneration of the inversion action should be studied separately from surjectivity onto that image.

**Confidence:** medium. **Reason:** This is suggested by the explicit two-coset argument and by the injectivity sentence continued on the next page; no new theorem is asserted.

### R541-01 — unpursued implication

**Location:** Scan 541, lower parenthesis after injectivity criterion. (Grothendieck, 1981, scan 541.)

**Source phrase:** « ρ=−1 »; « un quotient de Z/4Z »

The marginal revision examines the degenerate case in which ρ becomes central of order at most two. A systematic account could track the effect of this collapse on the normalizer map and on the two residue-sign conditions used later.

### R541-02 — unproved claim

**Location:** Scan 541, vertical marginal (43) and final sentence. (Grothendieck, 1981, scan 541.)

**Source phrase:** « épimorphismes »; « On a fait ce qu’il fallait »

The marginal diagram calls both maps N_ρ→γ_{ρ,σ} and N_σ→γ_{ρ,σ} epimorphisms. A proof needs the centralizer-image criteria from the preceding discussion together with the extra coset supplied by τ′ or τ_B; it is not written out in this marginal diagram.

### R541-03 — own idea

**Location:** Scan 541, (39) and both (40) displays. (Grothendieck, 1981, scan 541.)

Compare the involutions τ and τ′=σ⁻¹τ through their actions on the two designated cyclic subgroups. The integral matrix written for τ′ suggests a useful simultaneous-normalizer formulation, but any assertion about arbitrary profinite quotients must retain possible collapse of these generators.

**Confidence:** medium. **Reason:** The page explicitly computes the two inversions and checks injectivity through noncollapse; the general formulation would require proof.

### R542-01 — unproved claim

**Location:** Scan 542, middle, after (45). (Grothendieck, 1981, scan 542.)

**Source phrase:** l'image inverse de ... (cf cor. p. 570). ≃ B_{ρ,σ}

The identification of the effective inverse image with B_{ρ,σ} is referred back to the earlier corollary. A formal verification should specify exactly which conditions constitute effectivity and prove that the commutator coordinates recover the automorphism and its multiplier.

### R542-02 — unproved claim

**Location:** Scan 542, middle insertion and marginal map (46bis). (Grothendieck, 1981, scan 542.)

**Source phrase:** Par construction ... une application surjective

The surjectivity claim should be checked against the precise definition of the effective subset. It may be definitional for the inverse image, while surjectivity from the restricted Sg subset could require additional control of conjugators.

### R542-03 — own idea

**Location:** Scan 542, (44)–(48). (Grothendieck, 1981, scan 542.)

One can study the coordinate map by describing the fibers of α↦[α,ρ] and β↦[β,σ] as cosets of the corresponding centralizers. This may turn the conditions defining the effective set into a fiber-product description; the subsequent pages in this packet should be checked before treating this as an omitted implication.

**Confidence:** medium. **Reason:** The coordinate expressions suggest centralizer ambiguity directly, but no novelty or established result is asserted.

### R543-01 — unproved claim

**Location:** Scan 543, (51)–(52). (Grothendieck, 1981, scan 543.)

**Source phrase:** On a une section ... donnée par

The claimed section is written explicitly using uτ′^{ν₂(μ)}, and the page begins to verify its commutator coordinates. A complete verification should also check membership in the defining subset, the multiplier condition, and whether 'section' is meant only as a map of sets or with an additional group structure.

### R543-02 — own idea

**Location:** Scan 543, calculation after (52). (Grothendieck, 1981, scan 543.)

The calculation may be checked independently from the inversion action of τ′ on σ and the sign ε₂(μ). This is especially useful for distinguishing a genuine missing factor from an overwritten glyph in the last equality; any algebraic reconstruction must remain outside the diplomatic text.

**Confidence:** medium. **Reason:** The final factor and some primes are genuinely ambiguous in the scan.

### R543-03 — unpursued implication

**Location:** Scan 543, last paragraph. (Grothendieck, 1981, scan 543.)

**Source phrase:** l'ens ... des (α,β,μ) donnant l'image

The transition to the entire fiber suggests that the section is being used to describe all conjugator choices by multiplying by centralizer elements. This is carried on to the following scan, so it should be read as a local transition rather than a claim of an unaddressed problem.

### R544-01 — unproved claim

**Location:** Scan 544, (53)–(54). (Grothendieck, 1981, scan 544.)

**Source phrase:** qu'on écrit aussi

The complete fiber is expressed using centralizer and normalizer parameters. A proof needs to show that any two conjugators of ρ or σ differ by the appropriate centralizer, and then track the sign of the normalizer parameter. The displayed absence of an inverse in one reformulation should be checked mathematically without altering the diplomatic reading.

### R544-02 — unproved claim

**Location:** Scan 544, conditions (56)–(57) and subsequent fiber formula. (Grothendieck, 1981, scan 544.)

**Source phrase:** soit encore ... on voit que

The restrictions defining the smaller effective set are converted into equality of the three quotient images and two sign conditions. To verify sufficiency as well as necessity, one must track the embeddings iρ and iσ and the relations for τ′ when replacing a₀ by a.

### R544-03 — unpursued implication

**Location:** Scan 544, bottom fiber product and two sign maps. (Grothendieck, 1981, scan 544.)

**Source phrase:** Introduisons donc le groupe ... et les homomorphismes composés

The fiber product packages the common quotient image while retaining two independent sign characters. Matching these signs to the multiplier characters naturally gives an equalizer subgroup; the following scan explicitly continues this construction, so this is a local implication rather than an unresolved conjecture.

### R544-04 — own idea

**Location:** Scan 544, (53) through bottom fiber product. (Grothendieck, 1981, scan 544.)

An explicit finite-quotient example could test the fiber parameterization and the role of the involution when one of ρ or σ degenerates. Such a calculation would help separate the generic injective-normalizer case from the exceptional cases discussed earlier, without assuming that the coordinate sets carry the same group law as the fiber product.

**Confidence:** medium. **Reason:** The parameterization depends on normalizer embeddings and signs whose degeneracies were discussed on scans 540–541.

### R545-01 — unproved claim

**Location:** Scan 545, paragraph below (61), first (62). (Grothendieck, 1981, scan 545.)

**Source phrase:** on a fait ce qu’il fallait ... soit injective et ait comme image

The natural parametrization is asserted to be injective with image SG^{eff}_{ρ,σ}, giving a bijection. A verification should separately check well-definedness, the inverse reconstruction of (u,a,b), and each sign/character compatibility imposed in (60); the statement here provides no expanded verification.

### R545-02 — own idea

**Location:** Scan 545, (60)–(62). (Grothendieck, 1981, scan 545.)

View the effective parameter space as an equalizer of two pairs of sign characters on the fiber product introduced on the preceding page. This suggests checking its index component by component, including possible dependence between the two signs, before treating it as a subgroup of index four.

**Confidence:** medium. **Reason:** The page explicitly uses a “sous-groupe des coïncidences,” but surjectivity or independence of the sign pairs is not established here.

### R545-03 — unpursued implication

**Location:** Scan 545, Remarque and second (62). (Grothendieck, 1981, scan 545.)

**Source phrase:** définissent même une application

The formulas extend to the ambient M_{ρ,σ}[0] before imposing the equalizer conditions. Comparing the extended map with the effective restriction could clarify which conditions govern the existence of the coordinates and which govern the stated image; the formulas continue on the next scan.

### R546-01 — conjecture

**Location:** Scan 546, upper paragraph after (63). (Grothendieck, 1981, scan 546.)

**Source phrase:** Ceci suggère une définition d’un groupe ... des pts adéliques d’un schéma en groupes convenable sur Z

Grothendieck proposes a larger group containing B_{ρ,σ} with index 1, 2, or 4, and expects it, in “bons cas,” to be the adelic points of a suitable group scheme over Z. This remains a proposed construction and conditional expectation on this page; a study should specify the group functor, its representability, and the topology meant by adelic points.

### R546-02 — unproved claim

**Location:** Scan 546, (64)–(66). (Grothendieck, 1981, scan 546.)

**Source phrase:** De sorte qu’on aura

Replacing β by τ′^νβ is asserted to remove the ε factor from the conjugation formula while placing the sign into χ(β′). Verification depends on the precise convention for conjugation and the action of τ′; it should be checked directly in the chosen extension before comparing with the quotient formulas (67).

### R546-03 — own idea

**Location:** Scan 546, (66)–(67). (Grothendieck, 1981, scan 546.)

Compare the two coordinate conventions before and after the quotient by ±1, including the apparent missing prime on the first Π factor in the second pair of coordinates. Such a comparison may distinguish a notational slip from a deliberate change of the ambient parameter space, without changing the diplomatic reading.

**Confidence:** medium. **Reason:** The ink gives a prime on the first Π factor in the first pair, no visible prime there in the second pair, and then identifies the quotient by ±1.

### R547-01 — unpursued implication

**Location:** Scan 547, (68)–(70). (Grothendieck, 1981, scan 547.)

**Source phrase:** où le signe ... a disparu. Il apparaît dans les formules

The change β ↦ β′ relocates the sign from the conjugation identities to the character constraint χ(β′)=ε_2(μ). This gives two presentations of the same intended action, and comparison should track the chosen lift to the extended group rather than discarding the character condition.

### R547-02 — conjecture

**Location:** Scan 547, paragraph beginning Il me semble. (Grothendieck, 1981, scan 547.)

**Source phrase:** Il me semble en avoir assez ... les achever

Grothendieck expresses the expectation that the preceding calculations suffice to restart and complete the constructions with more suitable notation. This is an announced methodological step; it does not by itself establish that all compatibility and quotient hypotheses required by the rewritten construction hold.

### R547-03 — own idea

**Location:** Scan 547, lower-half group comparison. (Grothendieck, 1981, scan 547.)

Check the extra hat-like mark above Z in the second SL expression before interpreting it mathematically. The full profinite completion of SL(2,Z) and its congruence image over Z-hat must be kept distinct in any commentary; the present transcription deliberately preserves the uncertain ink.

**Confidence:** high. **Reason:** Two different completions can be suggested by the two possible readings, while the earlier expression on this same page has an unambiguous outer completion mark.

### R547-04 — unproved claim

**Location:** Scan 547, bottom, (71). (Grothendieck, 1981, scan 547.)

**Source phrase:** ou ce qui revient au même

The equivalence of τ outside G^+ and τ′ outside G^+ uses their relation by an element of G^+. Checking that relation survives the quotient is a useful nondegeneracy check before the reformulated presentation on the next scan.

### R548-01 — unproved claim

**Location:** Scan 548, oblique left marginal note, central section. (Grothendieck, 1981, scan 548.)

**Source phrase:** « la relation de rigidité »; « le centralisateur de σ n'est pas réduit à 1 »

The marginal note contrasts fixed subgroups for the extension containing tau with the centralizer in the extension containing tau prime. A proof needs the exact ambient groups and their specified actions, so the uncertain prime in the second fixed-subgroup expression must be settled before using the assertion. The note supplies the claimed contrast but no proof on this page.

### R548-02 — unproved claim

**Location:** Scan 548, lower half, paragraph introducing (1) and (2). (Grothendieck, 1981, scan 548.)

**Source phrase:** « ce que nous exprimerons par la donnée des trois générateurs topologiques »

The equivalence between a surjective homomorphism from the completed group in (1) and the displayed generators and relations in (2) merits an explicit argument using the universal property of profinite completion. The topological generation and continuity requirements are part of that equivalence and should not be lost when extracting a presentation.

### R548-03 — own idea

**Location:** Scan 548, upper paragraph and oblique marginal note. (Grothendieck, 1981, scan 548.)

**Source phrase:** « qui prend le pas sur τ »

One could compare the two involutions as choices of coordinates for the same subsequent construction, keeping track of which formulas simplify and which fixed-subgroup statements change. This is a proposed check of the manuscript's transition, not a claim that the resulting comparison is new or already established.

**Confidence:** medium. **Reason:** The page explicitly favors the inversion formulas for tau prime while the margin records a disadvantage, making the tradeoff a concrete object of study.

### R547-L1 — own idea

**Location:** Scans 546–548, proposed enlargement, change of involution, and reformulated genus-one presentation. (Grothendieck, 1981, scans 546–548.)

A comparison with Enriquez’s later genus-one Grothendieck–Teichmüller construction could begin by matching the ambient completions, multiplier maps, and designated conjugacy classes before comparing individual formulas. Enriquez (2012) constructs an explicit profinite genus-one group and relates it to a prounipotent group-scheme version; this provides a specific comparison target, not evidence that the manuscript’s proposed adelic realization has been established. **Confidence:** medium. **Reason:** the genus-one setting and arithmetic automorphism data overlap, but no identification of the two constructions is proved here.

### R530-L2 — own idea

**Location:** Scans 530–535, automorphism–multiplier pairs, conjugating coordinates, and the lacet relation. (Grothendieck, 1981, scans 530–535.)

One could compare these coordinates with the later Grothendieck–Teichmüller framework in Drinfeld (1991), first recording which relations belong to the profinite setting and which belong to its prounipotent counterpart. Drinfeld’s article uses the prounipotent version of a group introduced by Grothendieck, but that broad connection does not identify the specific groups or quotients in this packet. **Confidence:** low to medium. **Reason:** the comparison is structurally motivated, while the exact functors, kernels, and compatibility relations have not been matched.

## References

Drinfeld, V. G. (1991). On quasitriangular quasi-Hopf algebras and on a group that is closely connected with Gal(Q̄/Q). *Leningrad Mathematical Journal, 2*(4), 829–860. (Original Russian article published 1990, *Algebra i Analiz, 2*(4), 149–181.) https://www.mathnet.ru/eng/aa199

Enriquez, B. (2012). *Elliptic associators* (Version 3) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.1003.1012

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-3; supplied scans 530–548]. Université de Montpellier. Source identification follows the supplied task; all manuscript citations above refer to the attached image files and the scan-file numbering in the crosswalk.

Stoffel, A. (2021). *tikzcd: Commutative diagrams with TikZ* (Version 1.0) [Package documentation]. CTAN. https://tug.ctan.org/graphics/pgf/contrib/tikz-cd/tikz-cd-doc.pdf

The two later sources were consulted for the comparison notes and bibliographic grounding only. They were not used to fill, correct, or disambiguate the manuscript transcription. The research notes are a set of leads, not an exhaustive survey or a claim that every statement has been checked against the rest of the manuscript.
