# LM_C4-191-209 — Transcription notes

## Scope and editorial conventions

This edition transcribes the nineteen supplied images, scans **191–209**, from Alexander Grothendieck's *La Longue Marche à travers la théorie de Galois* (1981). The supplied scan number is one greater than the page number printed in the archive footer: scan 191 bears printed page 190, and scan 209 bears printed page 208. The visible author foliation runs from 743 to 752, with an additionally crossed and uncertain 745 on scan 196. The repeated institutional footer and the small lower-left archive pagination are archival apparatus and are not included in the manuscript fragment.

The transcription preserves the surviving text, cancellations, additions, marginal notes, abbreviations, punctuation, mathematical numbering and doubtful forms. Interlinear additions are placed at their indicated target; paragraph boundaries and scan boundaries are retained, while ordinary line wrapping is not reproduced. The chosen fonts for handwritten mathematical alphabets are typographic approximations; particular ambiguous glyphs are marked locally, and the straight-bar fundamental-group sign is consistently represented by uppercase `\Pi`, including `\Pi_1`. Script G and the Teichmüller T are rendered `\mathcal{G}` and `\mathcal{T}`. The source's different L-T, LT and TL forms remain different.

The `.tex` file is a fragment without a preamble. Its editorial macros are exactly those specified in the task; their presentation is left to the receiving edition. The diagrams use `tikz-cd`, with `ampersand replacement=\&` so they can be enclosed safely in the requested `\diagram{…}` macro; diagram (32) also draws its four quotient braces with ordinary TikZ paths inside the diagram. Standard mathematical support such as `amsmath` and `amssymb` is required by the notation. A doubt macro records an uncertain reading, not a proposed correction: in `\unsure{A|B}`, A is the preferred reading and B an alternative. Nested doubt and deletion macros sometimes preserve uncertainty about whether a visible mark was cancelled at all.

## Table of doubts

Line numbers are approximate handwritten body lines, excluding the institutional footer. Locations inside formulas and marginal or interlinear additions are identified separately. Confidence concerns the ink reading, not the mathematical plausibility of the result. Rows may group repeated occurrences of the same ambiguity; clear but surprising literal forms are also recorded where they could otherwise invite silent correction.

| Scan | Approximate line / locus | Reading in transcription | Alternatives / reason for doubt | Confidence |
|---|---|---|---|---|
| 191 | 3, before cancelled prefix | des | de; final abbreviated stroke is inconclusive | medium |
| 191 | 3, cancelled prefix | méta- | final hyphen lies in the cancellation; the replacement reads L-T- | medium |
| 191 | 6 | mixtures | internal t/u/r strokes are compressed; no alternative confidently supported | medium |
| 191 | 13, before groupe | deleted L- | a small dense cancellation; only an L-like stroke can be distinguished | low |
| 192 | 1, before G | ambiant | compressed middle strokes; no second reading securely supported | medium |
| 192 | isolated cancellation below paragraph | 2 | could be a cancelled letter or pen trial; the numeral-like lower loop is visible | low |
| 193 | (8), first symbol | K_i with superscript calligraphic G | κ_i with the same superscript; tall straight stem and angular arms favour Latin K | medium |
| 193 | after nous | deleted Soit | second half is obscured by the cancellation | medium |
| 193 | below une, right-hand cancellation | 0-conn. | ending obscured; may be an earlier version of 0-connexe | low |
| 193 | below soit M, left-hand cancellation | 0-connexe | most of the ending is covered by the horizontal cancellation | low |
| 193 | after the surviving lisse | en | de; a low loop followed by a short terminal stroke favours en, without a clear d ascender | medium |
| 193 | On doit pouvoir… | prouver | compressed middle strokes, no secure alternative | medium |
| 193 | before final G in groupe fini | deleted K | heavily cancelled single symbol | low |
| 194 | beginning of first line | deleted ou | small overstruck word before dash | low |
| 194 | line 4, after parenthesis | deleted tel | et; crossing obscures the middle | low |
| 194 | line 4 | soit une | est un; short word and final article stroke are ambiguous | medium |
| 194 | line 5, after laquelle | sera | ser.; the final stroke is abbreviated | medium |
| 194 | line 6 | quasi-projectif | quasi-projective; the ending is obscured by a descender from the line above | medium |
| 194 | (10) and (11), before G;a | U | M; the two tall returns could belong to either capital, so mathematical expectation has not settled the reading | medium |
| 194 | below (11), after la | deleted L | a single heavily obliterated sign | low |
| 194 | final line, in Π_1(…,a) | M | overwritten capital with dense strokes; possible underlying U not separable | medium |
| 195 | 7, opening of second paragraph | quelcon-que | quelconque; a separated central dash is visible within the handwritten word | medium |
| 195 | both inline Π_1 expressions following (12) | a | o; the basepoint glyph has a small closed loop without a fully distinct tail | medium |
| 196 | Top centre | Cancelled manuscript number `745` | Several overwritten diagonal strokes obscure the middle digit; `745` is the best visual reading. | low |
| 196 | 2 | Deleted `schéma` | Cancellation passes through nearly the whole word; replacement `multiplicité` is clearer. | medium |
| 196 | 6, right | Deleted `schéma` | The second occurrence is also heavily crossed out. | medium |
| 196 | 9 | `conceptuelles` | Compressed medial strokes and final `-elles`; no better complete alternative. | medium |
| 196 | 14 | `1`-multiplicités | `L`-multiplicités: the leading upright and the following dash are separate, favouring numeral `1`; the word is not normalized on conceptual grounds. | medium |
| 197 | (13), first fundamental-group argument | `U` | `M`; the initial glyph is heavily retraced. | low |
| 197 | (13) and following line | Separate base subscript `Q` beneath the already subscripted `U` or `M` | Placement is lower than `g,ν`; the transcription preserves that nested placement without adding a comma. | medium |
| 197 | 3 | `de` type | `du` type; the terminal stroke of the article is inconclusive. | medium |
| 197 | 4 | `universelle` followed by a closing quotation mark | No opening quotation mark can be securely located; one has not been supplied. | high |
| 197 | 5, inline fundamental group | Cancelled `Q` before surviving base subscript `Q` | A clean `ξ` is another possible reading of the crossed, vertically looped mark. | low |
| 197 | 9, after `(13),` | Deleted `et` | A tiny cancelled conjunction or correction mark; the letter content is doubtful. | low |
| 197 | 9, long cancelled clause | `(qui se ramène d'ailleurs essentielle-` | `se` and `ramène` are partly crossed; final `essentiellement` is another possible reading, but its ending is not securely visible. | low |
| 197 | 16, group name after `LT-groupe` | `M` in script alphabet | Script `A`; the glyph has several superposed strokes. | low |
| 197 | Lower displayed map | `k_i` | Greek `κ_i`; the handwritten stem and branches do not conclusively distinguish them. | medium |
| 197 | Lower displayed map, cancelled codomain | Script `G` | `Π`; cancellation severely obscures the former letter. | low |
| 197 | Bottom line | `K_i` with superscript script `G` | Greek `κ_i` with that superscript; the first glyph looks more angular and taller than the individual-map label. | medium |
| 198 | 3 | Deleted `et on aura` | `et on a`; the last word is intersected by a long cancellation stroke. | low |
| 198 | Between (14) and (15) | `hom` | `lacet`; a peer rereading found the first tall stem followed by low waves more compatible with `hom`, without the crossed `t` otherwise visible in `lacets`. No terminal abbreviation point is secure. | medium |
| 198 | (15), both occurrences | `k` | Greek `κ`. | medium |
| 198 | 9, object normalized in `M` | `L` | `T`; a clear lower foot supports `L`, while the upper cross stroke may retain an overwritten `T`. | low |
| 198 | 12, before `sur L` | Deleted `dans` | `donc` was considered; the apparent through stroke and terminal letter favour cancelled `dans`, but the deletion state is also uncertain. | medium |
| 198 | 15 and 16 | `caractère` | Very compressed internal strokes, especially the accent; the sense has not been used to remove the doubt. | medium |
| 199 | 12 | `faite` | `faîte`; the small mark over the vowel may be an angular dot rather than a circumflex. | medium |
| 199 | 16 | `standarts` | `standards`; the final tall stroke resembles `t`, and the potentially nonstandard spelling has been retained as the first reading. | medium |
| 199 | 17, before `corps K` | `bon`, alternatively cancelled `bon` | A heavily retraced three-letter word: the dense horizontal stroke could be connected handwriting or cancellation. Both the lexical reading and the deletion state remain uncertain. | low |
| 199 | 17, cancellation after `K` | `de car. 0` | The digit is largely intersected by the deletion stroke. | medium |
| 200 | 3, small cancelled mark after `K;` | `le` | `u`; the tiny looped fragment is very uncertain even at maximum enlargement. | low |
| 201 | Heading, line 1 | T-L-groupe | The small join between T and L is overwritten; a dash is the best reading. | medium |
| 201 | Heading, line 2, above punctuation | a) | The elevated subheading marker is small and partly merged with the punctuation; treated as an insertion. | medium |
| 201 | 7 | distingué | Beginning is overtraced; ending is clearer. | medium |
| 201 | 8, cancelled before groupe | L- | The small cancellation may conceal a different initial symbol; L- is a tentative visual reading. | low |
| 201 | 8–9, after profini | ) | ]; the lower return of the closing delimiter is angular. The opening delimiter appears rounded. | medium |
| 201 | 11 | groupe | Initial letters are overtraced; cancellation is not certain. | medium |
| 201 | 12, before Π s'identifie | etc. | et; the first loop and final small mark are difficult. | low |
| 201 | 18, before groupe | le, possibly cancelled | The short horizontal stroke may be a cancellation or part of the overtraced word. Both states are represented in the doubt macro. | low |
| 201 | 21 | schém. | schéma; the terminal mark looks like a point. | medium |
| 202 | Equation (25), opening delimiter | ( | {; opening looks rounded, while the closing delimiter is a brace. The mismatch has not been silently normalized. | medium |
| 202 | Equation (25), last condition | ∀ | tt; the sign after “presque” has two vertical strokes and a cross stroke. | medium |
| 202 | Cancelled line below (25) | On dit qu'un | On dit qu'on; the short word after the apostrophe is crossed by the deletion line. | medium |
| 202 | Equation (26), target alphabet | blackboard G with subscript mQ | ordinary G; the doubled/closed stroke in the capital is not completely clear. | medium |
| 202 | 6, replaced word following à | un | ces; the cancellation obscures the central strokes. | low |
| 202 | 12, target of the component homomorphisms | Q_l | The Q is heavily overtraced; a prior capital cannot be securely separated from its doubled stroke. | medium |
| 202 | 13, agreement after sont | continus | continues; final strokes are compressed. | medium |
| 202 | 15, cancelled before une factorisation | one unreadable word | No defensible full reading survives the heavy overstrike at enlarged inspection. | low |
| 203 | Diagram (30), multiplicative target | double-struck Gₘ | Plain Gₘ; the doubled-looking left stroke may be a retracing. The alphabet is marked uncertain as in scan 202. | medium |
| 203 | 3 | définisse | définit; the final strokes run together. | medium |
| 203 | Equation (29), cancelled before M | G | A small overtraced capital, tentatively G. | low |
| 203 | Diagram number (30) | 30 | Numerals are overtraced; an earlier numeral cannot be isolated securely. | medium |
| 203 | NB after diagram (31) | ops | qps; the three compressed letters have no clear separating points. No expansion is made in the transcription. | low |
| 203 | Heading 4° | irrédondance | irrédundance; the vowel after d is compressed. | medium |
| 204 | 1, cancelled before M | G | Densely overtraced capital; a G-like curved outline remains. | low |
| 204 | Remarque, after tels que | g(Π₀) | gℓ(Π₀); the stroke between g and Π resembles a looped opening parenthesis, but a separate ℓ cannot be excluded. | medium |
| 204 | Remarque, line after commensurables | Càd. | C.à.d.; internal points and accent cannot all be separated from the strokes. | medium |
| 204 | Left marginal note, quotient denominator | Π₀ | The quotient stroke and two upright strokes can be distinguished after rotation, but are crowded. | medium |
| 205 | 1 | faite | fait; the final short return may belong to the t rather than a separate e. | medium |
| 205 | 2 | différente | différent; the ending is compressed immediately before the comma. | medium |
| 205 | 3, cancelled interlinear phrase | définissant la LT-structure | définissant la LT-struct.; the cancellation crosses the letter bodies and obscures the ending. | low |
| 205 | 5 | néc. with superscript t | néc.; a short raised stroke is visible after the abbreviation. | medium |
| 205 | 6, example | SL(2,Z) | The opening parenthesis is not separately distinguishable from the L's final stroke; retained with a doubt mark instead of silently supplied. | low |
| 205 | 11 | importants | The initial letters are densely retraced, but the surviving outline supports this reading. No distinct deleted earlier word can be recovered. | medium |
| 205 | 12, after son adh. | G₀ with circumflex | G₀ with star; the mark is overwritten and neither the hat nor a star can be excluded. The notation is not replaced by a closure bar. | low |
| 205 | Diagram (32), first top object | 1 | The numeral is retraced; no different underlying symbol can be recovered. | medium |
| 205 | Diagram (32), upper G | circumflex / star, subscript 0 possibly deleted | Both the upper decoration and the lower right blot are heavily retraced. The transcription marks uncertainty about both the symbol and whether the 0 was cancelled; the annotation beneath is more clearly = G₀ with circumflex. | low |
| 206 | 3, left | idem | Could be « item »; the second letter has a tall t-like stroke and the e is compressed. | medium |
| 206 | 2, far right | Donc | The last letters are compressed; no expansion is supplied. | medium |
| 206 | 8, deletion before « Je suis » | La situation | Most of the second word lies on the crossing stroke. | medium |
| 206 | 11 | 1-multiplicité | The first vertical stroke and dash are weak; the mathematical sense is not used to resolve the reading. | medium |
| 206 | 15 | int. | Could be « int! »; the tall final mark is separated from the dot. | low |
| 206 | 15, deletion after Q | Γ / k; en fait | The initial symbol is heavily crossed; the words are partially covered by a horizontal deletion stroke. | low |
| 206 | 15, inserted formula | N with an isomorphism arrow to Γ | Could be an isomorphism sign rather than an arrow; a right-pointing head appears visible. | low |
| 206 | 16, deletion before « le groupe » | est | The ink is overwritten several times. | low |
| 207 | 2 | la | Possibly « leur »; the short word has several compressed waves. | low |
| 207 | 5, Galois-group subscript | barred Q with a small subscript 0 | Possibly just barred Q with an extra pen loop; the small circle is retained as a doubt. | medium |
| 207 | 17, overwritten condition number | 2 replaced by 3 | The visible lower curve belongs to 3; the overwritten upper character resembles 2. | medium |
| 207 | 18 | formulée | The ending is compressed at the right edge. | medium |
| 207 | final line | factorisa- | Continuation « tion » occurs at the next page; the terminal hyphen is faint/at the crop edge. | medium |
| 208 | 1, far right | donc | Extremely compressed but apparently uncancelled. | medium |
| 208 | paragraph after (35), line 3 | les | Overlapped by the sloping marginal note. | medium |
| 208 | underlined naming phrase | structures | The final letters are compressed; singular « structure » is possible. | medium |
| 208 | left margin, end | cette structure | The marginal note overlaps the main text at « cette »; singular ending is not completely distinct. | medium |
| 208 | « un hom », inline formula | right-pointing arrow | The ink could be only a horizontal stroke; its head is weak. | medium |
| 208 | bottom interlinear addition | simplement | The ending might be abbreviated; the long final stroke is not fully resolved. | medium |
| 208 | deletion after « sur Q. » | défini | Central letters are crossed by a thick line. | medium |
| 208 | deletion before underlined G_Q | calligraphic G / M | A heavily overwritten symbol; the candidate is retained with explicit doubt. | low |
| 209 | 1, deleted target before G(Q) | M / G | The character is heavily overwritten and possibly contains more than one correction. | low |
| 209 | 2, map whose image defines underlined Pi_Q | Pi (without subscript 0) | A 0 is not visible; Pi_0 is not supplied on mathematical grounds. | high |
| 209 | 3, deletion after ainsi | un | Several low loops survive below a heavy stroke. | low |
| 209 | (36), overwritten middle group | M replaced by G | A clear inner M appears under the new outer G; the original and replacement are both recorded. | medium |
| 209 | penultimate paragraph, deleted opening | Je vais / vois réfléchir / rappeler | The added « que » overlaps the cancelled word and makes the reading particularly insecure. | low |
| 209 | final paragraph, inserted opening | Notons que | Notons is clear; que overlaps the deleted word and cannot be separated from it securely. | medium |
| 209 | final paragraph and (39), multiplicative group | double-stroked G | A second vertical stroke is visible, but it may belong to the author’s ordinary G rather than distinguish an alphabet. | medium |

## Abbreviations and signs met

Expansions are interpretive and appear only here, not in the transcription. Variants of punctuation are retained where they occur in the source.

| As written | Possible expansion or interpretation |
|---|---|
| p.ex. | par exemple |
| $\overline{\mathrm m}$ | même |
| Aut | automorphismes |
| Autext | automorphismes extérieurs |
| hom | homomorphismes |
| alg. | algébrique / algébriquement, according to context |
| car. | caractéristique |
| t.f. | type fini |
| dim | dimension |
| /k | sur k |
| rev. | revêtement |
| néc. | nécessairement |
| pt | point |
| géom. | géométrique |
| alg | algébriquement (without a visible period in this occurrence) |
| tjrs | toujours |
| ext. | extension |
| `p. ex.` | par exemple |
| `hom.` | homomorphisme |
| `i.e.` | id est |
| `NB` | nota bene |
| `dfn` above an equality | définition; the three-letter abbreviation has not been expanded in the transcription |
| `Sch` | schémas, as a category label |
| Overlined wavy `m` | même |
| `L`, `LT`, `TL` in group labels | Structural labels used by the manuscript; the differing orders `LT` and `TL` have been retained |
| etc. (uncertain) | et cetera |
| schém. (uncertain) | schéma |
| hom / hom. | homomorphisme(s) |
| tt (possible alternative in (25)) | tout |
| ReNB | renewed nota bene; the manuscript's combined marker is retained |
| ops / qps (uncertain) | possibly “on peut supposer” / “qu'on peut supposer” |
| hyp. | hypothèses |
| Càd. / C.à.d. (uncertain punctuation) | c'est-à-dire |
| néc. with possible superscript t | nécessairement |
| NB. | nota bene |
| adh. | adhérence |
| dfn above equality | définition / by definition |
| struct. (possible cancelled ending) | structure |
| gr. | groupe |
| int. (uncertain) | intègre |
| T. | Teichmüller |
| autom. | automorphismes |
| ss-groupe | sous-groupe |
| p. | page |
| épi | épimorphisme |

## Legibility and limits

The main prose and most formulas are readable, but the handwriting is highly compressed and the revisions are substantially less secure. Whole-page inspection was followed by enlarged, overlapping readings, comparison against the transcription, and an independent rereading of each assigned group of pages. The final scan received the same treatment as the opening scans. These checks do not eliminate the unresolved readings recorded above.

The least reliable material is the densely cancelled wording and group symbols on scans 193 and 197, the overtraced word and abbreviation on scans 201–202, the hat/star and possible cancelled subscript in diagram (32) on scan 205, the overlapping marginal and interlinear writing on scan 208, and the deleted opening replaced by “Notons que” on scan 209. The two U/M arguments on scan 194, the possible 1/L prefix on scan 196, and several small basepoints, prepositions and abbreviation endings remain explicitly doubtful.

Several apparent irregularities are deliberately preserved: the gender mismatch after the substitution of *schéma* on scan 194; the bare hatted Z in the lower-left corner of (30); the literal final power of the generator in (22), without supplying an additional image map; and bare Π in the second line of scan 209, without adding a subscript 0. Heavy retracing alone has not been treated as evidence for a bold alphabet or a recoverable earlier reading. The manuscript's bracket and parenthesis mismatches are not silently repaired.

## Research notes — English

These are local research prompts grounded in the supplied pages. They distinguish conjectures or expressed expectations, unproved claims, implications not pursued in the excerpt, and explicitly labelled ideas of the transcribers. A proof obligation or suggested example is not asserted to be established, novel, or absent from the rest of the manuscript or the literature. No external transcription or later mathematical formulation was used to decide a reading; the reference below identifies the manuscript evidence rather than a literature review.

### R191.1 — Scan 191, extension (6) and automorphism example (7)

**Kind: unproved claim.** The passage says that an invariant L-structure on Π makes the extension group an L-T-group, and proposes « Aut_L(Π) » and « Autext_L(Π) » as an example. Checking the exactness of (6) in that example requires identifying the inner automorphism subgroup and checking whether the surrounding definition of a « groupe à lacets » supplies the needed hypothesis on the centre; the excerpt itself does not give that verification (Grothendieck, 1981, scan 191, eqs. 6–7).

### R191.2 — Scan 191, « classe de sous-groupes discrets commensurables »

**Kind: unpursued implication.** The formulation makes a commensurability class of discrete subgroups part of the structure rather than selecting just one subgroup. A natural question for the subsequent pages is which constructions depend only on this class and which require a representative; the wording here supplies the question but no independence proof (Grothendieck, 1981, scan 191, lines 1–3).

### R193.1 — Scan 193, after (8)

**Kind: unproved claim.** The extension of L- and LT-group terminology to the profinite case is called « essentiellement évidente ». A proof would have to specify the continuous outer homomorphisms, the relevant equivalence of germs, and the compatibility of their topology with the proposed definitions; those details are not given on this page (Grothendieck, 1981, scan 193, eq. 8 and following lines).

### R193.2 — Scan 193, last paragraph and (9)

**Kind: conjecture.** Grothendieck writes « On doit pouvoir prouver alors que » before describing M by a smooth quasi-projective curve U with a finite group G acting on it. The exact class of « multiplicités » and the role of the connectedness and separatedness hypotheses must be checked before treating this as a global quotient assertion; the page proposes it without proof (Grothendieck, 1981, scan 193, eq. 9 and preceding paragraph).

### R194.1 — Scan 194, first paragraph

**Kind: conjecture.** The proposed intrinsic reformulation is « il doit être vrai qu'il existe un rev. étale fini », with a scheme as covering object and a Galois refinement envisaged. Establishing this requires more than a local presentation: one needs a global finite étale cover with the stated representability and quasi-projectivity properties, under the exact hypotheses in the preceding page (Grothendieck, 1981, scan 194, first paragraph).

### R194.2 — Scan 194, (11) and final paragraph

**Kind: unproved claim.** The text says « on trouve une L-structure » from the natural loop structure on the subgroup Π₀. A verification would need to show how the peripheral homomorphisms are transported through the finite extension and why the resulting germ classes are invariant under the whole fundamental group; the subsequent independence assertion begins on this page (Grothendieck, 1981, scan 194, eq. 11 and following paragraph).

### R195.1 — Scan 195, opening paragraph

**Kind: unproved claim.** The L-structure is asserted to « ne dépend pas du choix » of the finite étale Galois cover or of the lift of the geometric basepoint. A proof could compare two choices after passage to a common finite étale refinement and then track the change-of-basepoint conjugations at the level of outer germs; the page declares the resulting structure to be used tacitly (Grothendieck, 1981, scan 195, opening paragraph).

### R195.2 — Scan 195, (12) and following paragraph

**Kind: unpursued implication.** In the arithmetic exact sequence, the geometric fundamental group appears « muni d'une L-structure invariante » under the arithmetic group. This invites a precise comparison between the resulting outer arithmetic action and the normalizers of individual loop images studied later in the excerpt; the statement here does not yet supply the local character calculation (Grothendieck, 1981, scan 195, eq. 12).

### R195.3 — Scan 195, last paragraph

**Kind: conjecture.** « Je suis particulièrement intéressé au cas “universel” de type (g,ν) » announces a shift from a single field-based object to a universal moduli setting. The following pages must be checked for the precise base object and for what the quotation marks around « universel » qualify; no universal representability assertion should be inferred from this sentence alone (Grothendieck, 1981, scan 195, last paragraph).

### R195.4 — Scans 193–195, finite-cover construction

**Kind: own idea. Confidence: medium. Reason:** the asserted independence is formulated for outer germs and the text explicitly permits changing finite covers. An efficient test case would compare two explicit finite group quotient presentations of the same one-dimensional object and calculate how their peripheral subgroup classes agree after common refinement. This is a proposed verification strategy, not a claim that such a presentation always exists or that the strategy is new (Grothendieck, 1981, scans 193–195).

### Scan 196, lines 3–7 — conjecture

Grothendieck replaces `peut` by “doit pouvoir” in the proposal to introduce a corresponding modular multiplicity over `Q`, and even over `Z`. Establishing this expectation would require a precise moduli problem associated with the discrete reference group `Π_0`, together with an account of descent, automorphisms, and what sort of representing object is intended (Grothendieck, 1981, scan 196).

### Scan 196, lines 8–17 — unpursued implication

The stated “difficultés conceptuelles” concern the contrast between a fibre category and a “2-catégorie” with the inserted qualification “en groupoïdes.” This signals that specifying objects and ordinary morphisms alone may not determine the proposed modular construction; the coherence and descent of the additional morphisms deserve a separate formulation. The prefix of `1`-multiplicités is palaeographically doubtful, so this note should not be used to settle that reading (Grothendieck, 1981, scan 196).

### Scan 197, statement (13) — unproved claim

“On aura donc une suite exacte” introduces the extension with kernel `Π̂_{g,ν}` and the two fundamental groups of the universal curve and modular base. A proof in the intended category would need to identify the geometric fibre group and verify the exactness and any necessary base-point conventions for the universal object. Those justifications are not supplied on this page (Grothendieck, 1981, scan 197).

### Scan 197, lines 7–10 — conjecture

“Je voudrais dégager une propriété commune” explicitly announces a search for a property shared by the universal case and a multiplicity over a field finitely generated over `Q`. The subsequent normalizer action and cyclotomic-image hypothesis should be tracked as the proposed realization of this aim, while distinguishing the definition of the hypothesis from a proof that all the intended examples satisfy it (Grothendieck, 1981, scan 197).

### Scan 197, lines 11–14 — unproved claim

The first case is said to reduce “essentiellement au second” by taking a “point générique” of `M_{g,ν}`. Making that reduction precise would require checking what the passage to the generic field preserves about the relevant fundamental groups, lacet data, and cyclotomic action, and how the multiplicity's automorphisms enter the comparison (Grothendieck, 1981, scan 197).

### Scan 198, statement (16) and following NB — unproved claim

The inclusion `N(L)/L ⊂ N` and the remark “On voit aisément” that its image is open are stated without a local proof. A proof should identify the kernel of the normalizer's projection to `N`, including any assertion that the normalizer of `L` inside `Π` is `L`, and explain why the relevant orbit or stabilizer condition gives openness (Grothendieck, 1981, scan 198).

### Scan 199, lines 3–10 and statement (18) — unproved claim

The cyclotomic hypothesis is called intrinsic to the `LT`-group “indépendamment du choix de Π.” To substantiate this, one would need to compare the characters associated with different defining subgroups, for example after passage to a common refinement, and verify that the comparison preserves the stated open-image condition (Grothendieck, 1981, scan 199).

### Scan 199, statement (19) — unproved claim

The open-image hypothesis is asserted to imply that “Tout sous-groupe ouvert” of `N(L)/L` acts nontrivially on `L`. A proof would have to use the exact topology on these groups and the relationship between the cyclotomic character and the action on the full lacet group, rather than merely a nontrivial action on one quotient (Grothendieck, 1981, scan 199).

### Scans 199–200, statements (20)–(22) — unproved claim

“On sait” introduces the claimed quasi-unipotence of the restriction of every indicated homomorphism to `L`. A full proof must clarify the class of fields and the continuity convention on `u`, especially since `de car. 0` is visibly cancelled and the displayed formulation does not restate continuity. The final phrase contains `ℓ_i^n` after previously discussing `u(ℓ_i)`; that notational transition is preserved in the transcription and should be checked in the intended interpretation (Grothendieck, 1981, scans 199–200).

### Scan 200, statement (22) — own idea; confidence: medium

A possible route to the quasi-unipotence claim is to study the Zariski closure of the image of the procyclic group `L`, then test whether its torus quotient can survive the normalizer's cyclotomic action. The reason for considering this route is that the unipotent part and a finite semisimple part would match the desired conclusion, while a positive-dimensional torus is the potential obstruction. The continuity and finite-index steps require proof; this is a proposed check, not an established deduction from the abbreviated formulation.

### Scans 199–200, open-image hypothesis and (21) — own idea; confidence: high for the test construction

To test the role of the arithmetic hypothesis, take `M=L=Ẑ` with trivial quotient and, for an odd prime `ℓ`, consider the continuous character obtained from `Ẑ → Z_ℓ` followed by `a ↦ (1+ℓ)^a` in `Q_ℓ^×`. Its infinite image in a one-dimensional torus cannot become unipotent on an open subgroup, whereas its normalizer action is trivial and the manuscript's open-image assumption fails. This provides a concrete limiting example to check, rather than a challenge to the claim with its full hypotheses.

### Scan 201, lines 9–13 — unpursued implication

The condition that Π₀ be a “discrétification” is followed by “Π s'identifie à son complété profini.” A later investigation should separate the existence of such a subgroup from the additional compatibility with the loop structure; here it is part of the chosen data, not a construction (Grothendieck, 1981, scan 201).

### Scan 201, equations (23)–(24) — own idea

The displayed adelic target suggests testing the subsequent admissibility conditions first for a torus and for the additive group. **Confidence: medium** that this is a useful diagnostic, because these examples distinguish multiplicative character compatibility from unrestricted additive representations; no existence or novelty claim is intended (Grothendieck, 1981, scan 201).

### Scan 202, equation (25) — unproved claim

“Alors on a” introduces the restricted-product description of G(A_Q). A proof would need to identify points over the displayed adelic ring with tuples integral at all but finitely many primes for the chosen affine finite-type integral model (Grothendieck, 1981, scan 202).

### Scan 202, condition 1°, lines 11–16 — unproved claim

“Cela équivaut à dire” identifies continuity with coordinatewise continuity plus a uniform finite exceptional set of primes. A proof should explain why compactness of the profinite source gives a single finite set S, rather than a finite exceptional set depending on the source element (Grothendieck, 1981, scan 202).

### Scan 202, lines 18–19 — unproved claim

The condition “ne dépend pas du ‘modèle sur Z’” is stated without a comparison argument. One should compare two chosen models after discarding finitely many primes and check that the resulting changes can be absorbed into S (Grothendieck, 1981, scan 202).

### Scan 202, final NB — unproved claim

“(28) est un hom. de groupes profinis” requires the relevant integral point group to be profinite and the factorization to preserve continuity. The natural verification would use its finite reductions and the topology inherited from the local field points (Grothendieck, 1981, scan 202).

### Scan 203, opening ReNB and (29) — unproved claim

“Sauf erreur” qualifies the assertion that condition 1° permits a model for which the entire image factors through G(Ẑ). A proof would need integral models containing the compact local images at the finitely many exceptional primes, together with a construction that combines those models while preserving the specified generic fiber (Grothendieck, 1981, scan 203).

### Scan 203, condition 3° and (31) — unpursued implication

The factorization through “G(Q)” on a finite-index subgroup of Π₀ imposes a simultaneous rationality condition across the adelic components. Its dependence on the chosen discretification and its stability under changes of that subgroup deserve separate verification; the displayed square alone does not provide either result (Grothendieck, 1981, scan 203).

### Scan 203, NB after (31) — own idea

The phrase “Quitte à changer de notations” should be checked against every item of the data when replacing Π₀ by Π₀′. **Confidence: medium**, because a finite-index subgroup generally has a corresponding open subgroup as its profinite completion, so the reduction may require restricting other groups as well as renaming Π₀; this is a question about the reduction, not a correction to the text (Grothendieck, 1981, scan 203).

### Scan 204, NB, lines 3–9 — unproved claim

The assertion that “il y en a un (unique) plus petit” provides a proposed minimal subgroup scheme when condition 4° fails. A proof should establish existence of the smallest subgroup through whose adelic points the map factors, then verify that character compatibility and rationality on the chosen discrete subgroup survive the restriction (Grothendieck, 1981, scan 204).

### Scan 204, Remarque — unproved claim

The phrase “le sous-groupe ... formé des g” treats the elements preserving the commensurability class of Π₀ as a subgroup. The relevant verification should state precisely the action denoted g(Π₀) and check closure under products and inverses before using this group in the stronger admissibility condition (Grothendieck, 1981, scan 204).

### Scan 204, final paragraph — conjecture

“Il est possible qu'il faille renforcer la condition 3°” asks whether rationality must hold on the larger group G₀, rather than only on a finite-index subgroup of Π₀. The closing “L'avenir le décidera !” explicitly leaves the necessity of this strengthening open at this point; its reconsideration on the next scan should be tracked separately (Grothendieck, 1981, scan 204).

### Scan 204, Remarque — own idea

Compare representations satisfying rationality on Π₀ with those satisfying rationality on its full commensurator G₀, starting with examples where the commensurator strictly exceeds the normalizer. **Confidence: medium**, because the definition uses commensurability rather than equality, making the extension of rationality a real additional constraint; this is a proposed test, not an established distinction for every example (Grothendieck, 1981, scan 204).

### Scan 205, opening paragraph — unpursued implication

“Réflexion faite” introduces a revised framework in which the L-structure need not be “une structure à lacets.” The parenthesis invokes a “sens évident” of discretification for L-structures, but these pages do not give a formal definition there; subsequent work should specify the topology, distinguished subgroups, and compatibility required before applying the revised construction (Grothendieck, 1981, scan 205).

### Scan 205, data preceding (32) — unpursued implication

The inserted “son adh.” and the requirement “soit distingué dans M” make normality of the closure of the discrete subgroup part of the chosen data. It would be useful to separate conditions ensuring that closure-normality from the weaker condition that G₀ normalizes Π₀; the text does not assert that the latter alone proves the former (Grothendieck, 1981, scan 205).

### Scan 205, final paragraph — unproved claim

“G s'identifie à un quotient du complété profini de G₀” invokes a completion map whose quotient property is not proved here. A proof should use continuity into the profinite target and density of the discrete subgroup, while keeping possible kernels separate from the stronger assertion of an isomorphism (Grothendieck, 1981, scan 205).

### Scan 205, diagram (32) — own idea

Compare the topology on G₀ induced by M with the full profinite topology on G₀, and test whether every finite quotient is detected by an open subgroup of M. **Confidence: high** that this isolates the potential kernel in the completion-to-closure map, because the source explicitly asserts only a quotient at this stage; no general equality or novelty claim is intended (Grothendieck, 1981, scan 205).

### Scan 206, lines 1–3 — unpursued implication

The qualification « je n'exige pas pour le moment qu'il soit isomorphe à ce complété lui-$\overline{\mathrm m}$ », followed by the same qualification for $\mathcal T$ and $\mathcal T_0$, keeps the comparison with a full profinite completion deliberately weaker than an isomorphism. One should identify the kernels of the completion maps in the intended examples and check which later constructions actually depend on their vanishing; this is a question prompted by the wording, not an assertion that the kernels are nontrivial (Grothendieck, 1981, scan 206).

### Scan 206, case (a), lines 10–17 — unproved claim

In the case « $\mathcal G_0=\Pi_0$ d'où $\mathcal G=\Pi$ », the inserted assertion identifies the quotient denoted $\mathcal N$ with $\Gamma$ and calls it « le groupe fondamental » of the base scheme or multiplicity. A proof would have to specify the hypotheses on the relative object and the base and verify that the group sequence used here matches the geometric fundamental-group sequence; the exact abbreviated condition on the base is doubtful in the transcription (Grothendieck, 1981, scan 206).

### Scan 206, cases (a)–(b) — own idea

Confidence: medium. The contrast between a trivial discrete Teichmüller quotient in (a) and a full or finite-index Teichmüller quotient in (b) suggests testing examples with an intermediate discrete monodromy subgroup before imposing universal moduli interpretations. The reason is structural: the page presents two « situations extrêmes » while its group data do not visibly restrict all examples to either extreme (Grothendieck, 1981, scan 206).

### Scan 207, (33)–(34) — unpursued implication

The page assumes that the cyclotomic character is « trivial sur $\mathcal G$, a fortiori sur $\Pi$ » and that its induced character on $\Gamma$ has open image. These are hypotheses on the full group structure, and it would be useful to track separately which later conclusions require triviality on $\mathcal G$ and which need the stronger openness condition (Grothendieck, 1981, scan 207).

### Scan 207, bottom, continuing into scan 208 (35) — unpursued implication

The stronger condition is explicitly called « Compatibilité avec discrétification de Teichmüller $\mathcal G_0$ ». It asks for rationality on the larger discrete subgroup rather than only on a finite-index subgroup of $\Pi_0$; the effect on the possible algebraic envelopes deserves comparison, with the precise earlier condition checked on the preceding pages (Grothendieck, 1981, scan 207).

### Scan 208, left margin — conjecture

The marginal qualification « Quitte par la suite à introduire des conditions plus draconiennes » explicitly leaves the proposed Galois–Teichmüller structures open to strengthening. The present axioms therefore should not be read as a settled characterization; a useful follow-up is to determine which intended examples or counterexamples motivate the extra conditions (Grothendieck, 1981, scan 208).

### Scan 208, (35) and the definition of « hom de Lie » — own idea

Confidence: medium. Test whether the class of homomorphisms satisfying the strong rationality condition is unchanged when the chosen discrete subgroup is replaced by a commensurable subgroup with the same closure. This is worth testing because (35) imposes rationality on the entire chosen discrete subgroup, while the group-theoretic data are also discussed up to completion and finite index (Grothendieck, 1981, scan 208).

### Scan 208, final two paragraphs — unpursued implication

The change of notation « Je vais désigner par la suite par $\underline{\mathcal M}_{\mathbb Q}$ le schéma en groupes » attaches algebraic group notation to a particular admissible homomorphism. Comparing these groups for different such homomorphisms would clarify whether an inverse-system or universal-envelope construction is intended; no universal property is supplied on this page (Grothendieck, 1981, scan 208).

### Scan 209, (36) and « distingués » — unproved claim

The algebraic subgroups generated by the indicated images are asserted to be « distingués » in $\underline{\mathcal M}_{\mathbb Q}$. A proof would have to carry the relevant normality from the discrete/profinite groups to the algebraic subgroups and use the irredundancy condition on the ambient target; the passage should be checked carefully because the stated generating image of $\underline\Pi_{\mathbb Q}$ is written with bare $\Pi$ (Grothendieck, 1981, scan 209).

### Scan 209, (37)–(38) — unproved claim

The text says that the nested groups give « quatre suites exactes de schémas en groupes » and writes the final one in (38). The verification must specify the quotient group-scheme construction and the sense of exactness, and must check that the quotient of the intermediate group is the asserted kernel in (38), rather than merely checking exactness on rational points (Grothendieck, 1981, scan 209).

### Scan 209, final paragraph and (39) — unproved claim

The statement « le caractère $\chi_G$ … est épi, et se factorise » is not proved on the supplied final page. A proof would need to connect the open cyclotomic image assumed in (34) with the algebraic image of the character and show that the algebraic subgroup generated by $\mathcal G_0$ lies in its kernel; scheme-theoretic surjectivity should be distinguished from surjectivity on $\mathbb Q$-points (Grothendieck, 1981, scan 209).

### Scan 209, (37)–(39) — own idea

Confidence: medium. Form $K_{\mathbb Q}=\ker(\chi_{\underline\Gamma})$ and pull (38) back along $K_{\mathbb Q}\to\underline\Gamma_{\mathbb Q}$; the proposed object is $E_{\mathbb Q}=\underline{\mathcal N}_{\mathbb Q}\times_{\underline\Gamma_{\mathbb Q}}K_{\mathbb Q}$. Checking the induced extension by $\underline{\mathcal T}_{\mathbb Q}$ and its relation to the cyclotomic kernel in the original profinite group may separate the two restrictions. The reason for trying this construction is that (38) and (39) supply precisely these composable maps; no splitting or identification of kernels is asserted (Grothendieck, 1981, scan 209).

## Reference

Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript, cote 140-4, archive file “pages 650bis–787”; supplied scans 191–209, author folios 743–752, printed archive pages 190–208]. Université de Montpellier.

Bibliographical identification and date follow the supplied task metadata. In-text citations use the supplied scan numbers so that every note can be checked directly against the attached images.
