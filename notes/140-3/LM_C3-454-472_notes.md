# LM_C3-454-472: editorial and research notes

## Source and scope

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-3, supplied scan files 454–472]. Université de Montpellier.

This reference records the identification supplied with the images; no published transcription or outside mathematical source was used to supply readings. The LaTeX fragment contains the manuscript text, formulas, corrections, marginalia and diagrams. The mechanically printed Montpellier reproduction footers are outside the manuscript and are excluded. The final sentence is left unfinished where the supplied last leaf ends.

Scan identifiers follow the filenames. The lower handwritten folio is one less than the scan identifier in this package. The separate upper numbering, where present, is also preserved at its position by `\mspage`. No page number or repeated equation number has been regularized.

| Scan | Upper handwritten number | Lower handwritten folio | Inventory elements |
|---|---|---|---|
| 454 | — | 453 | 21 |
| 455 | 530 | 454 | 19 |
| 456 | — | 455 | 18 |
| 457 | 531 | 456 | 23 |
| 458 | — | 457 | 29 |
| 459 | 532 | 458 | 13 |
| 460 | — | 459 | 21 |
| 461 | 533 | 460 | 8 |
| 462 | — | 461 | 11 |
| 463 | 534 | 462 | 29 |
| 464 | — | 463 | 30 |
| 465 | 535 | 464 | 29 |
| 466 | — | 465 | 19 |
| 467 | 536 | 466 | 18 |
| 468 | — | 467 | 24 |
| 469 | 537 | 468 | 24 |
| 470 | — | 469 | 10 |
| 471 | 538 | 470 | 35 |
| 472 | — | 471 | 21 |

The inventory has 402 elements. Each row has `transcribed=yes`; corrections within a text block or formula are additionally inventoried as corrections. This records coverage, not certainty of reading.

## Legibility and editorial handling

The main prose and surviving formulas are often readable, but rapid word endings, retraced Greek letters and cancelled states are appreciably less secure. The least reliable passage is the final five lines of the diagonal lower-left note on scan 460, where the dark marginal writing overlaps the main text. Attempted readings remain inside `\unsure`; they must not be treated as settled text. Other particularly difficult passages are the wording before (157) on scan 455, the action clause and overwritten third row of (160) on scan 456, the altered map names on scans 462–464, the large cancelled block on scan 467, the cancelled target and abandoned formulas on scan 468, and the rewritten variables and insertion attachments on scans 471–472.

Underlining, raised subgroup parameters, primes, and differing letter forms follow the visible strokes rather than a uniform mathematical convention. In particular, the looped kernel-group capital is explicitly uncertain between G and calligraphic C; ξ/ζ and some cancelled Ξ/Σ forms remain unresolved. The apparently ordinary T with a long top stroke has not been turned into an overlined T. An unclear word ending is not silently corrected to fit the grammar. The doubts below identify positions approximately by the manuscript text or formula number; a candidate without a secure alternative is still a doubtful reading.

The fragment intentionally has no preamble and defines none of the prescribed editorial macros. It uses standard mathematical LaTeX, `tikz-cd`, and `\rotatebox` from `graphicx` for vertical handwritten annotations. Matrix alignment is encoded with `ampersand replacement=\&` so that the diagrams can occur inside the prescribed `\diagram` and `\margin` macros. A temporary verification wrapper compiled all 19 scan sections successfully; the uncertainties in the handwriting remain documented below.

## Table of doubts

| Scan | Approximate line or position | Reading in transcription | Alternative(s) / difficulty | Confidence |
|---|---|---|---|---|
| 454 | Upper-middle paragraph, after définissent | Cancelled toutes les | The cancellation obscures the middle strokes | low |
| 454 | Middle paragraph, after l'une | Cancelled d'elles, replaced by d'elles | The earlier state is crossed; replacement is clearer | low |
| 454 | Middle paragraph, before f | Cancelled f | Heavily overwritten single symbol | low |
| 454 | Left of (156), before tel que | Cancelled tel | Short crossed word; no secure alternative | low |
| 454 | Lower-third insertion | u in the inserted pair (f,u) | Its underlining is not securely visible | medium |
| 454 | Last display, β₀ formula | Cancelled β, replaced by β | Earlier glyph is overwritten; possible longer abandoned start | low |
| 455 | First display, cancelled beginning | det U = | Multiple crossing strokes obscure the original sequence | low |
| 455 | Middle paragraph, after bien sûr | hom. | The abbreviated word is compressed | medium |
| 455 | Same paragraph, after (135) | induits | Ending reduced to a short stroke | medium |
| 455 | Immediately before (157) | ou; d'équation | Short intervening strokes unresolved; d'équation is independently favoured but the full phrase remains uncertain | low |
| 455 | Under the second bracket in (157) | η | Small curved annotation; no secure alternative | medium |
| 455 | Parenthesis below (157) | Cancelled ou | Very short crossed word | low |
| 455 | Before the values of α,β | leurs | des | medium |
| 455 | Lower paragraph about commutativity | Cancelled et; intervenir | Cancellation obscures the former; compressed medial letters in the latter | medium |
| 455 | Last display, first commutator | u | Underlined u; the underline is not securely distinct from nearby strokes | medium |
| 455 | Last display, two cancelled exponents | −1; −1 | Positions and signs heavily overwritten | low |
| 456 | Above σ⁻¹ρ(u), end of parenthesis | mbs | mb; abbreviated ending unresolved | medium |
| 456 | (159 a), first tilded expression | ρ | The descending stroke is retraced under the tilde | medium |
| 456 | (159 b), action clause | coaction; induite | action for the first word; second word's ending is compressed | low |
| 456 | Parenthesis following (159), first line | m̄; parr | par for the latter; the short strokes and abbreviation are uncertain | low |
| 456 | Same parenthesis | draconiennes | Several medial letters are joined; retained as a candidate | medium |
| 456 | End of same parenthesis, underlined reference | VIII | VII; upper rule and underlining obscure the count of strokes | low |
| 456 | Before (160), after de l'amener | savoir | soit; both independent readings are low confidence | low |
| 456 | (160), second row, deleted argument | ρ | Superseded by clearer σ; earlier shape overwritten | low |
| 456 | (160), third row, epsilon argument/exponent | Cancelled μ and surviving (μ) | Dense corrections prevent a secure account of the original exponent and its exact attachment | low |
| 456 | Left margin beside (160) | aux signes | The beginning of the second word is faint | medium |
| 456 | Final line, parenthesis | identiquement | Long cursive word reduced to joins and end stroke | medium |
| 457 | Opening sentence | explicitent | Medial syllables and ending are rapid | medium |
| 457 | Parenthesis below the first verification | car | comme | medium |
| 457 | Second verification, before int(u) | ε | Retraced and possibly partially cancelled | low |
| 457 | Middle paragraph | différencient | Final syllables compressed | medium |
| 457 | (161 bis), equation label | Crossed bis | The apparent crossing may partly be retracing of the label | low |
| 457 | Right of (161 bis) | Cancelled int | Short crossed symbol or abbreviation | low |
| 457 | Left calculation, small underbrace annotation | i.e.; cancelled −1 | Annotation and superscript retraced | low |
| 457 | Lower calculations, repeated Greek letter | ξ | ζ; no alphabet normalization is imposed | low |
| 457 | Before σ(u)=εη⁻¹u | de = | The abbreviated linking mark is unclear | low |
| 457 | Cancelled product after σ([u,ε₀]) | ξ⁻¹uη⁻¹u | The cancellation obscures factor boundaries | low |
| 457 | Prose just before final equality | (*) | (α); small reference mark unresolved | low |
| 457 | End of same prose line | σ | Thick overtraced Greek glyph | medium |
| 458 | Proposition, after p. 526′ ff | Closing brace | Closing parenthesis; the curve is ambiguous | low |
| 458 | Proposition, cancelled phrase | T with ρ,σ subscripts | Tρ followed by comma and σ; overwritten grouping | low |
| 458 | (162 b), second source | N′σ | The letter is retraced | medium |
| 458 | (162 c), source of determinant isomorphism | T₀ | Overwritten first letter | medium |
| 458 | (162 d), first variable | λ | First stroke is retraced | medium |
| 458 | Cancelled (163 a) | normalise L₀ | Nearly the entire line is crossed | low |
| 458 | (163 b), after Γ | N′σ | N²σ; prime/superscript ambiguity | low |
| 458 | (163 c), deleted argument before μλ | δG(u) | Dense looped cancellation | low |
| 458 | (163 d), initial tilded letter | σ | ρ | low |
| 458 | (163 d), crossed expression before Γ | T̃₀ | Earlier mark partly hidden under crossing strokes | low |
| 458 | Both notes left of (163 c,d) | relie | Small first word written rapidly | medium |
| 458 | Final paragraph, before système | tt | ∀; handwritten abbreviation and quantifier are similar here | low |
| 458 | Final paragraph | Cancelled syst; surviving syst. | Both short endings are compressed; retained as abbreviations | medium |
| 458 | (165), α₀ formula | α | αρ; possible subscript is not secure | low |
| 458 | (165), before the inverse power | Cancelled β, replaced by f | Earlier glyph retraced beneath the replacement | low |
| 459 | 12, cancelled phrase | Si, d'autre part on a | Final words obscured by deletion stroke | low |
| 459 | 17, cancelled formula before Γ T₀ | Γ N′_σ ∩ | Initial crossed letters might include T₀ | low |
| 459 | Lower-left margin, line 2 | m̄ | Two short strokes; could be a different abbreviation | low |
| 459 | Lower-left margin | envisagés | Compressed ending | medium |
| 459 | Lower-left margin, final word | suite | Possibly another abbreviated word beginning suit- | low |
| 459 | Final line | syst. | Abbreviated word partly overwritten | medium |
| 460 | 1 | si | Looks like d' in isolation | medium |
| 460 | 1, cancelled symbol | φ | Possible ξ or ζ; heavy overwriting | low |
| 460 | 2, cancelled word | rempl. | Could be a longer form of remplacé, truncated or obscured | low |
| 460 | 3, above = | déf | Overwritten superscript | low |
| 460 | Above line 10, cancelled | il | Short overwritten word after inserted Donc | low |
| 460 | 17 | sera | Ending compressed | medium |
| 460 | 17 | permettra | Could be permette | medium |
| 460 | 18 | définition sec. | Main prose crossed by darker diagonal note | low |
| 460 | 18 | notion lacet | Could be action locale; much of the ink is cursive horizontal strokes | low |
| 460 | Margin, early clause | bien | donc; the word after trouvera is compressed | low |
| 460 | Margin, final five lines | Pour l'avoir R ; lui-même étant condition supplém., il/qui faut remplacer/faut envisager M… par le produit ½ direct par L₀, sur lequel on fait f_Δ=0, soit SM… | Last part is exceptionally uncertain owing to overlapping main text, cramped handwriting, and arrows | low |
| 460 | Bottom paragraph | fera | Compressed ending | medium |
| 460 | Bottom paragraph, line 3 | sous | Overlap with diagonal note; tentative word before des conditions | low |
| 460 | Bottom paragraph, line 4 | de la | Possible short words obscured by diagonal note | low |
| 461 | Above start of line 2 | y | Small isolated addition with diagonal attachment stroke; exact editorial status uncertain | low |
| 461 | 2 | sommes | serons | medium |
| 461 | 8, cancelled | les | Short crossed word | medium |
| 461 | 14, Greek letter | ζ | ξ | low |
| 461 | 14, punctuation after Greek letter | ; | Small dark glyph could be a letter remnant | low |
| 461 | 14, cancelled word | bien | donc; obscured by heavy horizontal stroke | low |
| 461 | 16 | modulo | moyennant | low |
| 461 | Last line, cancelled symbol | β | Possible originally longer expression involving β | low |
| 462 | (165), cancelled name/source | ε₀ : U | The old label and source are heavily overwritten | low |
| 462 | (165)–(166), repeated map name | calligraphic E_{L₀} | ε_{L₀}; the letter is unusually thick and retraced | low |
| 462 | Before construction, cancelled | définition | Only the initial déf- and final stroke are secure | medium |
| 463 | Crossed heading numeral | VIII | VII; cancellation obscures the tally of strokes | low |
| 463 | Heading, first subgroup parameter | 0 | ∞; small horizontal loop is insufficiently distinct | medium |
| 463 | Cancelled heading, third subgroup parameter | −J with bar | −j with bar; capitalization is uncertain in the crossed tall hooked letter | low |
| 463 | Kernel group glyph, repeated | G with tilde | Calligraphic C with tilde; distinctive looped form unresolved | low |
| 463 | Insertion above cancelled sections | ss-groupes | sous-groupes, with very compressed initial letters | medium |
| 463 | Diagram (1), vertical identification mark | wr / vertically drawn equivalence | The handwritten relation is a small curved vertical identification sign | medium |
| 463 | Deleted labels of (2) and (4) | Ξ / ζ | Original letters are heavily overwritten by replacement ψ / ψ⁰; Σ is also possible | low |
| 463 | Deleted formula (3b) and subsequent prose | Ξ | Σ; angular barred-Z form rather than the more cursive ξ used elsewhere | low |
| 463 | Deleted formula (3b), relation | ≡ | =; the cancellation adds another horizontal stroke | low |
| 463 | Deleted formula (3b), parentheses | x (G⁺) | The opening parenthesis is partly absorbed by the deletion stroke; no word mod is securely visible | medium |
| 463 | Deleted arrow label (4), subscript | 0 | It may be part of the cancellation rather than a separate subscript | low |
| 464 | 1, cancelled sign after ψ⁰ | ξ₀ | ζ₀; the former symbol is overwritten | low |
| 464 | (5), three cancelled portions | ξ; ξ; ξ(x)x | ζ; initial letters and the last crossing are obscured | low |
| 464 | (6), overwritten initial character | ξ | ζ | low |
| 464 | (6), subscript of ψ⁰ | 0 | dot from cancellation, rather than subscript | low |
| 464 | Left of “Les ψ” | Cancelled ρ | φ; small isolated overwritten sign | low |
| 464 | 5, cancelled word before “sections” | « trois » | « hom.⁰ »; cancellation passes through the whole word | low |
| 464 | 7, first pair of maps | ψ₀ | ψ∞; overwritten subscript | medium |
| 464 | 9 | correspondra | correspond… à; final strokes run together | medium |
| 464 | 9, cancellation | U et les | Several superposed strokes; last word could be “les” or “de” | low |
| 464 | Above line 9 | underlined u | “au”; heavily underlined insertion | low |
| 464 | 15 | sous-groupe-section | Final syllables run into the right border | medium |
| 464 | Left of lower display | et | Isolated small word, possibly cancelled | low |
| 464 | Last line | (a) | (α); small reference in parentheses | medium |
| 465 | 1 | réalisation | Final syllables are clearer than the initial strokes | medium |
| 465 | Upper left marginal note | permettant | End of word abbreviated by a long stroke | medium |
| 465 | 5, before “inverse” | isom | hom | medium |
| 465 | 9, “dire que c’est…” | ∈ U | The symbol looks like U; context could suggest T₀, which has not been substituted | low |
| 465 | 10, cancelled after “i.e.” | U₀= | Overwritten start of the following formula | medium |
| 465 | 16 | groupe section | First word is rapid and may have a different ending | medium |
| 465 | 22, cancelled words | Avant de qui | “Avant de quit…”; apparently an abandoned beginning | low |
| 466 | 2 | i′_T₀ | i_T₀; a very small stroke to the right of i may be a prime | medium |
| 466 | Throughout, subgroup labels | Raised (0) and [0] | Baseline argument notation is possible; their visually raised positions are retained as superscripts | medium |
| 466 | 12, right of “déterminant” | 2 | Possibly a punctuation/correction remnant; detached from the following κ(r)² | low |
| 466 | 21, after closing parenthesis | par | que; short linking word is unclear | low |
| 466 | 25, first deletion | comme | Abandoned word crossed horizontally | low |
| 466 | 25, deletion before L₀ | affine | Multiple crossing strokes obscure the middle; an underline is also visible | low |
| 467 | 1 | invarié | invariant; the last mark resembles an accent | medium |
| 467 | 1, cancelled word | On | Dense overwritten initial | low |
| 467 | Left margin beside (17) | transparente | Middle letters reduced to strokes | medium |
| 467 | (17), cancelled sign before SM | calligraphic S | G or another overwritten group symbol | low |
| 467 | (18), left underbrace annotation | ≃M | There may be a small prime-like remnant immediately before M | medium |
| 467 | 12, cancelled before SM^(0) | notée | Word crossed through its main stroke | low |
| 467 | 14, large cancelled block | opère | Initial letters overwritten | medium |
| 467 | 16, initial word | Revenons | Reprenons; initial word is retraced | low |
| 467 | 16, after “commence à” | nouveau | Several collapsed medial strokes | medium |
| 467 | Last line | explicité | explicitée; final unstressed e uncertain | medium |
| 464–466 | Kernel glyph in subgroup intersections | G under a tilde | The initial glyph may instead be calligraphic C; retained as \widetilde{\unsure{G\|\mathcal C}} pending comparison with the preceding definitions | low |
| 464 | Cancelled old map symbols in (5)–(6) | ξ, ζ | Adjacent scan 463 has a clearer angular barred glyph compatible with Ξ or Σ; these are further alternatives for the overwritten remnants, not silent substitutions | low |
| 468 | (19), last uncancelled factor | μ₂² | μ₂; the exponent region is entangled with the following cancellation | low |
| 468 | (19), cancelled parenthesis in target | (G_m³×G_m×μ₂) | Extensive oblique hatching obscures the group letters and factors; this is a tentative symbolic reading, not a reconstruction from the theorem | low |
| 468 | Above cancelled “triplets” | syst. | “sext.”; the abbreviation is compressed | medium |
| 468 | Cancelled line above (20), first marks | μ= | “pour”; the initial descender and horizontal strokes admit both readings | low |
| 468 | Cancelled line above (20), first function | det_G | δ_G; the two notations may be superposed | low |
| 468 | Right of proof heading, cancelled expression | Ker(Θ_G)\|μ_G | The terminal symbol and subscript are especially obscure; the tentative μ_G should not be assigned a mathematical meaning | low |
| 468 | First kernel display, cancelled coordinate | χ | ξ₂; the small lower-right loop may be only a crossing remnant | low |
| 468 | Three occurrences of SR with superscript | SR^° | SR⁰; the small open circular mark is retained as \unsure{\circ\|0} | medium |
| 468 | Proof prose after Θ_ρ,Θ_σ, cancelled word | donc | des; crossed horizontal stroke passes through the abbreviated medial letters | low |
| 468 | Right of “donc”, small cancellation | Θ | Overwritten round capital, possibly with an extra tail | low |
| 469 | 2, after “Corollaire.” | `Supp` | `fppf`; the compact three or four letter abbreviation is unresolved | low |
| 469 | upper-right NB, first words | `l'hom.` | No secure alternative | medium |
| 469 | upper-right NB, beneath “l'hom.” | `de` | Possible part of `déf`; no secure alternative | low |
| 469 | upper-right NB, left of the product | `can.` | `car`; the order of the compressed annotation is uncertain | low |
| 469 | upper-right NB, last line | `écris` | No secure alternative | medium |
| 469 | about 8, cancellation after “avec” | `k` | Possibly the start of `k(r)` | low |
| 469 | about 10, cancellation before “on pose” | `alors` | No secure alternative | low |
| 469 | about 12, cancelled and replaced phrase | `et on est` | No secure alternative for the cancelled state | medium |
| 469 | about 13, parenthesis before the quoted word | `en étant des` | `en ôtant les`; compressed writing prevents a secure reading | low |
| 469 | about 13, quoted word | `corrigés` | `conjugués` is less consistent with the visible strokes | medium |
| 469 | about 14, cancellation after “l'image” | `dans le` | No secure alternative | low |
| 469 | about 14, third factor of the product | `T_\sigma` | The overwritten subscript could include an additional stroke | medium |
| 469 | about 17, cancellation before `T_\rho` | `T` | An overwritten initial symbol; no secure alternative | low |
| 469 | about 20, after the product isomorphism | `c'est gagné` | No secure alternative | medium |
| 470 | 2, after the reference to (152) | `comprises` | `connues`; the descender and following dot favour `comprises` | medium |
| 470 | 4, parenthesis following the list of quantities | `n'y figurent` | `n'y étant`; several short strokes before the `y` remain unresolved | low |
| 470 | display (24), annotation beside and below `SG` | `\sim` beside an underbrace-like identification with the looped capital group symbol | An abbreviated isomorphism mark `\simeq` is possible; the capital is separately marked `G` / `\mathcal C`, and no quotient is inferred | low |
| 470 | about 17, after `f,u` | `satisfaisant` | `satisfaisants`; the final stroke does not securely establish the plural | medium |
| 470 | about 20 | `préférable` | No secure alternative | medium |
| 470 | about 21, after “plus” | `large` | The final letters are compressed into a long stroke and loop | medium |
| 471 | 1, cancelled phrase | `résultat` | `résultats`; the final stroke crosses the cancellation | medium |
| 471 | 4, overwritten mark after `(alpha,beta,f)` | `\in` | A cancelled or overwritten membership-like glyph; no secure alternative | low |
| 471 | about 7 | `conséquent` | `conséquence` | medium |
| 471 | (28), first row, between `f^{-1}` and `beta` | `\varepsilon` | A small overwritten or residual stroke is possible; the visible extra glyph is retained | low |
| 471 | about 12, second entry of the pair | cancelled `f`, replaced by `\underline u` | The earlier letter is obscured by hatching | low |
| 471 | about 13, variable before membership condition | cancelled `f`, replaced by `\underline u` | The overlapping former glyph is not fully recoverable | low |
| 471 | about 13, group after `Gamma` | cancelled `SG`, replaced by `B'_0` | Cancelled `T_0` is also possible | low |
| 471 | (29), cancellation after `U^{-1}` | `\underline u` | `f`; a densely hatched earlier factor | low |
| 471 | (29), overwritten membership group | cancelled `B'_0`, replaced by `SG` | Earlier strokes are not fully recoverable | low |
| 471 | Obs, first parameter | `\varepsilon` | `\varepsilon_1`; the apparent small stroke may be punctuation | low |
| 471 | Obs, parenthesis | `donc` | No secure alternative | medium |
| 471 | bottom paragraph, after cancelled “On peut” | `d'où` | `dire`; the phrase is altered by the inserted text above | low |
| 471 | bottom paragraph, after cancelled “que” | `aussi` | No secure alternative | medium |
| 471 | bottom-right insertion | `l'ens. des sections du` | The compact first two words and precise attachment to the unchanged “les” are uncertain | low |
| 471 | penultimate line | `sous-groupes` | `sous-groupe`; the final stroke is unclear | medium |
| 469 | final displayed group in the remark | `\widetilde G^+_{\rho,\sigma}` | `\widetilde{\mathcal C}^+_{\rho,\sigma}`; the elaborate looped capital is not securely distinguished | medium |
| 470 | display (24), group below `SG` | `\widetilde G^+_{\rho,\sigma}` | `\widetilde{\mathcal C}^+_{\rho,\sigma}` | medium |
| 472 | about 4, cancelled word before “pas” | `d'ailleurs` | No secure alternative | low |
| 472 | about 5, after “revenant” | `au cas` | `à un` is less consistent with the separate initial curve of the second word | medium |
| 472 | about 6, after “interpréter le” | `faisceau` | No secure alternative | medium |
| 472 | about 6, following word | `algébrique` | `régissant` was considered, but the apparent g-descender and following tall stroke favour `algébrique` | low |
| 472 | interlinear addition, about 7–8 | `via` | No secure alternative; attachment after “groupe étrange dessus” is probable but not secure | low |
| 472 | parenthesis, about 10 | `géométriques` | The final letters are compressed; no secure alternative | medium |
| 472 | about 13, before “schéma” | `au` | `à` | medium |
| 472 | about 16 | `se déduit` | `se décrit`; an independent visual rereading favours `déduit` | high |
| 472 | about 17, isolated character after “de” | `\rho` | No secure alternative; an independent visual rereading also identifies rho | high |
| 472 | about 17, cancelled phrase | `décrit par triples` | No secure alternative | low |
| 472 | about 18, cancelled word following `(x,u,f)` | `de` | No secure alternative | low |
| 472 | (32), cancelled mark between `x` and “dans” | `\in` | An overwritten short glyph; no secure alternative | low |
| 472 | (32), second variable | cancelled `f`, replaced by `\underline u` | Earlier and later strokes overlap | medium |
| 472 | (33), vertical identification | rotated `\simeq` | A similar vertical identification sign; not silently replaced by an arrow | medium |
| 472 | (33), isolated mark after `B'_0` | `\leftarrow` | A short pointer rather than a full morphism; an independent visual rereading agrees on its leftward direction | medium |
| 472 | (33), character of `x` | `\chi` | `\gamma` | medium |
| 472 | (33), determinant character of `u` | `\delta_G` | Earlier or retraced strokes overlap the delta and subscript | medium |

## Abbreviations met

Expansions and explanations appear only in this list. Variant written forms are retained. A proposed expansion does not resolve a doubtful reading.

| As written | Proposed expansion or explanation |
|---|---|
| i.e. | id est; c'est-à-dire |
| déf | définition |
| hom. | homomorphisme(s); some occurrences are uncertain readings |
| resp.ᵗ | respectivement |
| det | déterminant |
| int | conjugaison intérieure |
| $\overline{\mathrm m}$ | même |
| mbs / mb (uncertain) | membres |
| parr / par (uncertain) | possibly par rapport; uncertain abbreviation |
| 1/2 direct | semi-direct |
| cf | confer; voir / comparer |
| ff | et les pages suivantes |
| comm. | commutatif / commutatifs |
| loc.ᵗ | localement |
| tt / tte | tout / toute |
| syst. | système(s); some abbreviated endings are uncertain |
| p.ex. | par exemple |
| rempl. | remplacé / remplacement (uncertain cancelled form) |
| sec. | Possibly section; expansion uncertain in the partly obscured phrase |
| prop. | proposition |
| p. | page |
| supplém. | supplémentaire |
| Rem. | remarque |
| isom. | isomorphisme |
| épi | épimorphisme |
| ss-groupes | sous-groupes (reading of the insertion is uncertain) |
| mono / mono. | monomorphisme |
| can. | canonique; some occurrences are uncertain readings |
| isom | isomorphisme |
| Remq | Remarque |
| pt | point |
| dim | dimension |
| dfn | définition |
| trivialᵗ | trivialement |
| géom. | géométrique |
| NB | nota bene |
| Dém. | Démonstration |
| Supp (uncertain) | supposons; alternative reading `fppf` is unresolved |
| fppf (alternative reading) | fidèlement plat et de présentation finie |
| loc. cit | loco citato; lieu cité |
| etc | et cetera |
| $p^{\mathrm t}$ | point |
| produit 1/2 direct | produit semi-direct; the manuscript uses the fraction |
| f. et s. | faut et suffit |
| Obs | observation |
| ens. | ensemble |

## Research notes — English; separate from the transcription

These notes are interpretive leads, not additions to the manuscript. Each entry cites the supplied scan and a local passage, with a short quotation when it concerns Grothendieck's words. “Unproved claim” means a proof is not supplied at the cited location; it does not assert that the claim is unproved elsewhere. A question may be taken up on a later leaf. Entries labelled “own idea” state their confidence and reason and make no claim of novelty.

1. **Scan 454, lower half — unproved claim.** The passage asserts a unique decomposition, “existe un unique”, of a section into an element of `SG` and an element of `T_0`. To make the assertion precise, one would need to check in the ambient category that the displayed determinant isomorphism on `T_0` supplies a splitting, and that the claimed uniqueness holds at the level of sections being used. The statement depends on the hypotheses outside this excerpt as well as the displayed conditions.

2. **Scan 455, middle — unproved claim.** The phrase “on a admis, bien sûr” flags the compatibility of the two determinant characters with the embeddings into `G` as an assumption used in the calculation. An independent reconstruction should isolate this compatibility rather than infer it from the formal determinant manipulations.

3. **Scan 456, middle — conjecture / expectation.** “n'est guère concevable que si” introduces a proposed necessity of the normalization of `L_0` by `T_0` and a factorization condition on the relative element. The excerpt is exploratory here; a proof would have to derive these structural properties from the preceding identity under explicitly stated group and base hypotheses.

4. **Scan 456, middle parenthesis — unpursued implication.** “encore de la marge” compares the displayed conditions with stronger earlier conditions whose exact referenced Roman numeral is uncertain. One research task is to compare the two lists and determine which assumptions are actually used, without treating the present heuristic comparison as an equivalence theorem.

5. **Scan 456, lower half — conjecture / expectation.** Grothendieck says “il doit y avoir des façons plus convaincantes et exigeantes” to introduce the equation. This motivates examining whether the following conjugation formulas give an intrinsic characterization of the lacet relation; the next leaf takes up that calculation, so this is a local research question rather than a claim that the manuscript never returns to it.

6. **Scan 456, formulas (158)–(160) — own idea (medium confidence).** Test the relative conjugation identity in an explicit rank-two matrix model while keeping every determinant and sign convention fixed from the manuscript. This could separate genuinely necessary normalization assumptions from assumptions convenient for the chosen presentation; the reason for medium confidence is that the local formulas suggest such a test, but the full definition of the ambient group is not supplied on these leaves.

7. **Scan 457, middle — conjecture / expectation.** “ça doit être un calcul formel” introduces the proposed recovery of the lacet relation from the conjugation formulas. The page then carries out a calculation and ends “OK !”; a critical study should distinguish the preliminary expectation from this local verification and check the overwritten inverses and signs without silently repairing the transcription.

8. **Scan 457, upper third — unpursued implication.** “où f ne figure plus” points to an elimination of the auxiliary factor from the displayed conjugation conditions. One may investigate which parts of the resulting description are independent of that factor and which still depend on the chosen determinant splitting; the subsequent pages may address this question.

9. **Scan 458, proposition — unproved claim.** The proposition asserts “un unique syst.” and a unique factorization for every system satisfying the earlier relations. A complete proof must show that each of the enumerated conditions supplies exactly the compatibility used in the preceding calculations, including the locally chosen scalar in (163 d); the definitions and relations cited from previous leaves must be available for that proof.

10. **Scan 458, (163 d) — unpursued implication.** The phrase “∃ loc.ᵗ section” makes the factorization condition local. An investigation could ask how the local scalar choices transform on overlaps and whether the conclusion is a statement about sheaves, global sections, or a quotient; no descent theorem is established solely by this notation.

11. **Scan 458, (163 d) — own idea (low confidence).** Compare the visibly retained `L_0` after the tilded epsilon with the explicitly written `u_0∈ΓT_0` in the next line. These might reflect an intermediate revision or a convention outside the excerpt; a worked example and comparison with surrounding manuscript definitions could clarify the issue. The confidence is low because this is an editorially sensitive, overwritten passage, so the potential discrepancy is retained in the transcription rather than corrected.

12. **Scan 459, upper/middle paragraph — conjecture / question.** Grothendieck asks “sous quelles conditions la connaissance de $(\alpha,\beta,f)$ … permet de récupérer les quantités (152)”. The question separates reconstruction from admissibility: the input triple must both determine an object and satisfy conditions ensuring that an object exists. The question should be tracked through the subsequent pages rather than read as an assertion of a completed equivalence.

13. **Scan 459, equation (164) and margin — unproved claim.** The text reduces uniqueness to $T_0\cap T_\rho\cap N'_\sigma=\{1\}$ and the margin claims the stronger intersection $T_0\cap T_\rho=\{1\}$ in the cases indicated by II and III. A proof needs the actual embeddings and subgroup intersections from those earlier cases; the present page does not supply them.

14. **Scan 459, equation (164) — own idea.** If the intersection is nontrivial, the displayed indeterminacy suggests treating the reconstruction choices as a torsor under the common intersection. **Confidence: medium:** the text explicitly describes right multiplication by a section of that intersection, but transitivity and the relevant base or sheaf topology would need verification before asserting a torsor statement.

15. **Scan 460, middle paragraph — unpursued implication.** “Les conditions cherchées … ne dépendent que de $\alpha,\beta$, pas de $f$” follows here from the displayed transformation laws. This invites a formulation of admissibility on the pair $(\alpha,\beta)$, with $f$ serving as an independent adjustment parameter, provided the group action and the relevant section conditions remain valid after that adjustment.

16. **Scan 460, lower paragraph — conjecture / expectation.** “On voudrait qu'elles s'expriment par la validité de la formule du lacet” expresses a desired criterion, not an established theorem at this point. Grothendieck says that sufficiency will be addressed in II and III; the qualifier and the future reference should be retained in any interpretation.

17. **Scan 460, diagonal margin — unproved claim / qualification.** The marginal note begins “cette condition n'est pas suffisante” and requires the constructed $\underline u\in B'_0$ to lie in $T_0$. It gives the additional condition $B=0$ with $B=ac+bd+bc$ in the indicated matrix notation and refers to an earlier proposition; verifying this requires the original definitions of $B'_0$ and $T_0$ and the cited earlier result. The final lines of this note are too uncertain to support a stronger interpretive claim.

18. **Scan 461, opening paragraph — conjecture / qualification.** Grothendieck writes that the conditions may be “plus restrictives que nécessaires” and that he may have to return to the issue “dans un contexte plus général”. The conditions are therefore presented as useful working hypotheses for the indicated matrix-group cases, without a claim of optimality.

19. **Scan 461, remark — unproved claim.** “$\mu$ est déjà défini en termes de $\alpha$ seul” and the subsequent comparison with $\beta$ identify different amounts of information carried by the two parameters. A verification would need the definitions of the characters and the lacet formula, including the sign parameter $\varepsilon$; the remark itself does not repeat that derivation.

20. **Scan 461, final lines — unpursued implication.** Even after imposing $\varepsilon=1$, the text says that $\alpha$ determines $\beta$ only modulo $\beta\mapsto\beta T_\sigma$. This points to a quotient-valued invariant of $\alpha$; whether that invariant is representable, functorial, or locally liftable is not pursued on this page.

21. **Scan 462, opening paragraph and (166) — unproved claim.** The action on $L_0$ is said to factor “via $\chi$”, followed by the scalar-action equation (166). This reduces the described semidirect product to a one-dimensional additive action, but the identification of $L_0$ and the compatibility of the indicated parametrization with conjugation need the earlier construction cited in the inserted page reference.

22. **Scan 462, (166) — own idea.** Restricting to the kernel of $\chi$ should make the displayed action on the additive kernel trivial. **Confidence: medium:** substituting $\mu=1$ in (166) gives trivial action on every parametrized element, provided the parametrization is indeed an isomorphism over the intended base; this is a consequence to verify, not a novelty claim.

23. **Scan 463, opening paragraph — unproved claim.** The opening paragraph replaces the word “sections” with an insertion read as “ss-groupes” and qualifies the third as “une section partielle seulement” over the index-two subgroup that is the kernel of $\varepsilon_3$. The stated difference between a full and a partial section depends on that subgroup and character; the constructions and their verification follow after this page.

24. **Scan 463, left margin — unpursued implication / authorial reservation.** The note “Finalement ça ne servira pas à grand chose” qualifies the general discussion of sections. It records the author's assessment of its usefulness and should not be treated as a mathematical cancellation of every statement in the bracketed passage.

25. **Scan 463, (1)–(4) — unproved claim.** The reduction of sections to homomorphisms satisfying (3) uses the cover $R_{\rho,\sigma}\to\mathcal T_{\rho,\sigma}$ with kernel $\mu_2$ and then a product extension by $SG$. The deleted congruence in (3b) is replaced by “remonte (1)”. A complete proof must check both the lift condition and descent across $\mu_2$; these are distinct requirements in the displayed conditions.

26. **Scan 463, (1)–(4) — own idea.** A precise reformulation could describe the full section problem as a descent condition on the homomorphisms to $SG$ obtained from the product extension. **Confidence: medium:** the page explicitly identifies the kernel $\mu_2$ and states the correspondence with homomorphisms, but the exact embedding of that kernel and the multiplication conventions must be recovered before writing the descent equation.

27. **Scan 464, lower third — unproved claim.** “Reste à vérifier que … est épi”: the outstanding step is surjectivity of the proposed subgroup section onto the quotient group. A proof must construct a lift for every local quotient section and check its compatibility with the central kernel; the next scan continues this argument.

28. **Scan 464, (7)–(8) — unpursued implication.** The equivalent normalizations “f=1” and “U∈ΓT₀” identify the chosen section as the inverse image of the torus under Θ. It is worth tracking exactly which choice of torus this construction depends on and whether the later alternative subgroup sections are related by conjugation; these pages alone should not be read as establishing independence of that choice.

29. **Scan 465, after (13) — unproved claim.** “Comme il se doit, on a bien là un hom” asserts multiplicativity of the displayed map ψ₀⁰. Checking this directly requires the multiplicativity of κ and i_T₀ and the commutation needed to rearrange their values in G; the text then explicitly checks the value on μ₂.

30. **Scan 465, (11)–(13) — unpursued implication.** The graph formula for the inverse image of the chosen section gives a concrete criterion for descent through the diagonal μ₂. The line “sa valeur sur μ₂ est l’identité” is the key compatibility; one should compare it with the abstract condition (6) on the preceding scan before generalizing the construction.

31. **Scan 466, opening continuation — unproved claim.** The remark says that, “au pt de vue du pur calcul”, one could choose an arbitrary homomorphism and use (13). Because the target appears to be written “SG” and the notation for the chosen homomorphism may contain a prime, this generalization needs its exact hypotheses checked against the preceding definitions before any mathematical conclusion is drawn from it.

32. **Scan 466, (16) and closing paragraph — unpursued implication.** The stated decomposition of M^[0] as the half-direct product of M^(0) and L₀ exhibits how allowing B′₀ in place of T₀ adds a normal unipotent factor. “C’est encore une construction qui a un sens dès que…” invites investigation of the minimal normalization assumptions on T₀ and L₀; the sentence continues on the next scan.

33. **Scan 467, cancelled paragraph below (18) — unproved claim (cancelled).** The crossed passage says that L₀ “opère trivialᵗ sur SG” and links this to Θ. The cancellation is mathematically significant: this is a rejected line of reasoning, not an accepted assertion from which consequences should be drawn.

34. **Scan 467, after (18) — own idea.** A concrete matrix test with a diagonal torus and an upper triangular unipotent subgroup could help distinguish the action on SG from any induced quotient action and diagnose the cancelled triviality assertion. **Confidence: medium**, because the construction is a useful diagnostic but the exact ambient group and base hypotheses must be recovered from the earlier manuscript before claiming that this matrix model is an admissible instance.

35. **Scan 467, final paragraph — unpursued implication.** Grothendieck says that he is beginning “à … m’y perdre” and returns to the “signification \"géom.\"” of the two groups through the coordinates of p. 529. The next coordinate description should therefore be read as an attempt to clarify the geometry behind the semidirect products, rather than as mere repeated algebraic bookkeeping.

36. **Scan 468, (19)–(22) — unproved claim.** The proposition claims both injectivity and an exact coordinate description of the image. The proof on this scan establishes the kernel calculation by restricting Θ_ρ and Θ_σ to the residual SR subgroup, where they are identified with the two projections. The proof of the image description continues beyond this scan; the kernel argument alone does not establish it.

37. **Scan 468, marginal NB — unpursued implication.** The margin gives explicit recovery formulas for μ, ε, and ε′ from U, a, and b. This explains why the corollary can drop the last three coordinates of (19). To justify the corollary as a statement about group functors rather than individual points, these recovery formulas and the squared ratio condition must be compatible with base change; the present page states the formulas but does not separately discuss that functorial issue.

38. **Scan 468, cancelled χ in the first kernel formula — unpursued implication.** χ is deleted from the intermediate kernel and reappears in the full final kernel. This suggests that it is redundant once Θ_G is fixed, but the transcription does not silently fill in an identity relating them. Such an identity should be checked in the earlier definition of χ before using the deletion as a mathematical simplification.

39. **Scan 469, opening proof and normalization — unproved claim.** The proof uses “on prendra $r$ avec $k(r)=\lambda$” after adjoining or choosing a square root of $\det U$. On this page the availability of such an $r$ and the relevant locality are used rather than demonstrated; checking them requires the definition of $R_{\rho,\sigma}$ and its map $k$, with the uncertain abbreviation after “Corollaire.” kept unresolved.

40. **Scan 469, final remark — unpursued implication.** The statement “On ne peut remplacer $G\mapsto PG$” identifies the surviving kernel as the subgroup $\mu_2$ of the special group. This draws attention to the difference between the faithful description using $G$ and the projective description; the remark does not develop a replacement quotient presentation here.

41. **Scan 469, final remark — own idea.** Check the asserted projective kernel scheme-theoretically over bases of characteristic two, where describing it merely as the two scalar signs would lose information. Confidence: medium, because the page explicitly writes $\mu_2$ and works with group objects, but the base assumptions are outside this four-page portion.

42. **Scan 470, discussion after (25) — unproved claim.** “Cette condition assure l'unicité” refers to the factorization $\underline U=f^{-1}\underline u$ with $f\in SG$ and $\underline u\in T_0$. The uniqueness assertion here relies on the splitting or intersection properties established elsewhere; a direct proof would compare two factorizations and use $SG\cap T_0=\{1\}$.

43. **Scan 470, closing paragraph and (26) — unpursued implication.** He says that in some contexts “il est préférable” to replace membership in $T_0$ by membership in $B'_0=T_0.L_0$. This relaxes the normalization and points toward a family of factorizations rather than a single representative; the next page explicitly takes up the loss of uniqueness.

44. **Scan 470, (23)–(26) — own idea.** Treat the enlarged set of factorizations as an $L_0$-torsor, and formulate the original $T_0$ condition as a choice of representative or section. Confidence: medium, because the displayed semidirect decomposition suggests the relevant action, but a proof must check which side acts and how $f$ transforms.

45. **Scan 471, existence statement (27)–(31) — unproved claim.** The claim introduced by “il f. et s.” makes relation (31) sufficient as well as necessary for reconstructing a system $(x,\underline u)$ with $\underline u\in B'_0$. No proof of the full converse is supplied on this page; it requires reconstructing the coordinates, checking their determinant and sign constraints, and showing that the prescribed commutator relation gives a section of the required group object.

46. **Scan 471, Obs and inserted sentence — unproved claim.** The observation says that the two parameters are uniquely determined, and the insertion adds “Alors le couple $(x,\underline u)$ est unique.” Checking these distinct uniqueness claims requires the relevant trivial-intersection or factorization statements; the overwritten first parameter in the observation remains textually uncertain.

47. **Scan 471, final paragraph — unpursued implication.** The page explicitly distinguishes $\mathcal M_{\rho,\sigma}[0]$ from $\mathcal M_{\rho,\sigma}(0)$ in the asserted correspondence with pairs. This distinction merits tracking throughout the later construction: enlarging the normalization subgroup changes which group represents the solution data.

48. **Scan 471, (31) — own idea.** Work out the relation and reconstruction in an explicit rank-two matrix model before attempting a general group-object proof. Confidence: medium, because the determinant, torus, and unipotent notation suggest that such a model could expose the order of factors and possible exceptional base characteristics, but the present pages alone do not establish the model's hypotheses.

49. **Scan 472, upper parenthesis — conjecture.** The explicitly deferred task is “il me faudra revenir en termes” followed by an inserted “plus” and the probable reading “géométriques”. This is an announced need for a geometric interpretation of the group structure on solution triples, not a proved geometric identification or a precise conjectural theorem on this page.

50. **Scan 472, middle paragraph — unproved claim.** The enlarged group is said to be “isomorphe au schéma (en groupes) des solutions communes” of (27) and (31). The page proceeds to a presentation by triples and then by pairs, but the compatibility of the indicated cocycle structure with these identifications is not checked here.

51. **Scan 472, (32)–(33) — unpursued implication.** Eliminating $f$ from the triple presentation leaves a condition equating the character of $x$ with the determinant character of $\underline u\in B'_0$. This suggests reading the displayed subgroup as a fiber product over the multiplicative group, provided the character and group-map conventions from the earlier manuscript support that interpretation.

52. **Scan 472, (33) — own idea.** Compare the fiber-product presentation with the earlier semidirect-product construction of $S\mathcal M_{\rho,\sigma}$ and identify the kernel of its projection to $\mathcal M_{\rho,\sigma}$. Confidence: medium, because (32) lets one eliminate $f$ and (33) exhibits the character constraint, but the group law and action must still be tracked with their actual factor order.
