# LM_P05 — Editorial and research notes

## Scope and source identification

Source identification supplied with the task: Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Handwritten manuscript; Montpellier archive, cote 140-2, pages 1–292; supplied scans 41–50]. The transcription is based on the ten supplied JPEGs, `LM_P05_scan041.jpg` through `LM_P05_scan050.jpg`, not on a published transcription or an external mathematical source. No external literature was consulted for these notes.

The scan number is the primary locator. The printed archive footer lies outside the manuscript frame and is not transcribed. Two handwritten numbering sequences are visible; their different positions are not conflated:

| Scan | Upper-centre number, encoded with `\mspage` | Lower-left numeral, encoded with `\margin` |
|---|---|---|
| 41 | — | 40 |
| 42 | 19 | 41 |
| 43 | — | 42 |
| 44 | 20 | 43 |
| 45 | — | 44 |
| 46 | 21 | 45 |
| 47 | — | 46 |
| 48 | 22 | 47 |
| 49 | — | 48 |
| 50 | 23 | 49 |

The hand responsible for the lower-left foliation is not established here, so these numerals are retained as marginal material rather than attributed to Grothendieck's own pagination. The faint `795` on scan 50 is likewise retained without an attribution. Paragraphs that continue across a scan boundary are not completed editorially.

## 1. Table of doubts

Manuscript line numbers are approximate: displays, sloping additions and the prism make a unique line count impossible. The last column gives a precise line in the delivered `LM_P05_transcription.tex`; several doubts may occur on that line. Repeated occurrences of the same doubtful reading in one local passage are grouped, while distinct unreadable stretches are listed separately. Confidence concerns the reading, not the truth of the mathematics: **medium** means visually plausible but insecure; **low** means very tentative or unreadable. No alternative is supplied merely because it would make the mathematics work.

| Scan | Approximate manuscript position | Reading / gap | Alternative(s) | Confidence | TeX line |
|---|---|---|---|---|---|
| 41 | l. 6, cancelled phrase | `tels que` | No secure alternative | medium | 7 |
| 41 | ll. 7–9, square | `\mathcal G'_{i'}` | `\widehat G'_{i'}` | low | 9 |
| 41 | ll. 7–9, square | `\mathcal G_{\tau i'}` | `\widehat G_{\tau i'}` | low | 10 |
| 41 | ll. 12–13, tuple | `f_{D^*}` | No secure alternative | medium | 18 |
| 41 | ll. 12–13, tuple | `\alpha_{D^*D}` | No secure alternative | low | 18 |
| 41 | ll. 13–14, transition | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 19 |
| 41 | ll. 13–14, transition | `ci-dessus` | No secure alternative | low | 19 |
| 41 | ll. 20–21, overwritten equation | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 25 |
| 41 | ll. 20–21, overwritten equation | `\rho(\beta_{i'})` | `p(\beta_{i'})` | low | 26 |
| 41 | bottom, boxed correction | `\rho` | `p` | low | 30 |
| 42 | l. 1 | `résumé` | `résumant` | medium | 37 |
| 42 | l. 1 | `homs` | No secure alternative | medium | 37 |
| 42 | l. 1 | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 37 |
| 42 | ll. 2–4, first diagram | `\rho_i` | `f_i` | low | 39 |
| 42 | ll. 8–12, revised sentence | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 46 |
| 42 | ll. 15–20, prism | `f_{i'}` | `f^0_{i'}` | low | 66 |
| 42 | ll. 15–20, prism | `\beta_{i'}` | No secure alternative | medium | 70 |
| 42 | left margin beside prism | `condition sur les couples` | No secure alternative | low | 72 |
| 42 | left margin beside prism | `à dire` | No secure alternative | medium | 72 |
| 42 | left margin beside prism | `\mathcal E'_{i'}` | No secure alternative | low | 72 |
| 42 | left margin beside prism | `tombe dans` | No secure alternative | low | 72 |
| 42 | left margin beside prism | `\rho_i(\mathcal E_i)` | No secure alternative | low | 72 |
| 42 | right margin beside prism | `On` | No secure alternative | low | 74 |
| 42 | right margin beside prism | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 74 |
| 42 | right margin beside prism | Unreadable, estimated 3 word(s); gap 2 | No reading proposed | low | 74 |
| 42 | right margin beside prism | `\varphi(\rho(D_{i'}^*))\simeq\varphi(\widetilde U)` | No secure alternative | low | 74 |
| 42 | right margin beside prism | Unreadable, estimated 3 word(s); gap 3 | No reading proposed | low | 74 |
| 42 | right margin beside prism | Unreadable, estimated 1 word(s); gap 4 | No reading proposed | low | 74 |
| 42 | l. 21, before equation | `pour` | No secure alternative | low | 76 |
| 42 | ll. 22–25, final paragraph | `aussi` | No secure alternative | medium | 80 |
| 42 | ll. 22–25, final paragraph | `l'autre carré` | No secure alternative | low | 80 |
| 43 | ll. 7–8, image subgroup | `\Gamma'_{i'}` | No secure alternative | low | 87 |
| 43 | ll. 11–12, heading | `bordélique` | No secure alternative | medium | 93 |
| 43 | ll. 11–12, heading | `précise` | `précisée` | medium | 93 |
| 43 | ll. 13–14, revisions | Unreadable, estimated 2 word(s); gap 1 | No reading proposed | low | 95 |
| 43 | ll. 13–14, revisions | `indexés` | No secure alternative | low | 95 |
| 43 | l. 17, exact sequence | `k` | `\kappa` | medium | 101 |
| 43 | last line, isomorphism | `\overset{k_i}{\simeq}` | `\xrightarrow[\sim]{k_i}` | low | 110 |
| 44 | ll. 2–3, introduction | `par` | No secure alternative | low | 121 |
| 44 | upper left margin | `pas` | No secure alternative | medium | 132 |
| 44 | upper left margin | `\gamma_i` | No secure alternative | low | 132 |
| 44 | upper left margin | Unreadable, estimated 2 word(s); gap 1 | No reading proposed | low | 132 |
| 44 | l. 9, subgroup condition | `\subset` | `=` | medium | 138 |
| 44 | upper right margin | `\operatorname{Im}(fk'_{i'})` | No secure alternative | low | 148 |
| 44 | upper right margin | `même` | No secure alternative | low | 148 |
| 44 | upper right margin | Unreadable, estimated 2 word(s); gap 1 | No reading proposed | low | 148 |
| 44 | upper right margin | `L'_{i'}` | No secure alternative | low | 148 |
| 45 | l. 9, corrected noun | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 180 |
| 45 | l. 9, corrected noun | `quintuplets` | `quintuples` | medium | 180 |
| 45 | upper left margin, rotated | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 192 |
| 45 | upper left margin, rotated | `abéliens` | No secure alternative | low | 192 |
| 45 | upper left margin, rotated | `\bar k` | No secure alternative | low | 193 |
| 45 | upper left margin, rotated | `T_K` | `\mathcal T_K` | low | 193 |
| 45 | lower left margin, oblique | `\simeq` | `\longrightarrow` | low | 196 |
| 45 | lower left margin, oblique | `f_{D^*}^{\,*}` | No secure alternative | low | 196 |
| 45 | lower left margin, oblique | `indice de ramification` | No secure alternative | medium | 197 |
| 45 | lower left margin, oblique | `entier` | No secure alternative | medium | 197 |
| 45 | lower left margin, oblique | `positif` | No secure alternative | low | 197 |
| 45 | lower left margin, oblique | Unreadable, estimated 5 word(s); gap 1 | No reading proposed | low | 197 |
| 45 | ll. 16–18, morphisms | `$0$-morphisme` | `homomorphisme` | low | 205 |
| 46 | ll. 4–6 | `\Pi_U,\Pi'_U` | No secure alternative | medium | 218 |
| 46 | ll. 12–15, choice of reference object | `d'isom.` | No secure alternative | low | 226 |
| 46 | ll. 12–15, choice of reference object | `mod.` | No secure alternative | medium | 226 |
| 46 | ll. 12–15, choice of reference object | `=` | No secure alternative | low | 226 |
| 46 | ll. 21–22, final insertion | Unreadable, estimated 2 word(s); gap 1 | No reading proposed | low | 234 |
| 47 | ll. 2–3, after composites | `d'où noyaux` | No secure alternative | low | 243 |
| 47 | ll. 2–3, after composites | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 243 |
| 47 | ll. 2–3, after composites | `K` | `k` | medium | 243 |
| 47 | ll. 14–15, diagram (D) | `\varepsilon_i` | No secure alternative | low | 254 |
| 47 | ll. 14–15, diagram (D) | `k` | `\kappa` | medium | 255 |
| 47 | last line, cancellation | `du hom` | No secure alternative | low | 263 |
| 48 | ll. 9–11, diagram D′ | `\pi` | `\pi'` | medium | 278 |
| 48 | ll. 9–11, diagram D′ | `k'` | `\kappa'` | medium | 278 |
| 48 | ll. 9–11, diagram D′ | `I` | `I'` | low | 279 |
| 48 | right of boxed homomorphism, (a) | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 286 |
| 48 | left margin beside (a) | Unreadable, estimated 2 word(s); gap 1 | No reading proposed | low | 287 |
| 48 | ll. 15–16, choice of isomorphism | `tenant du` | No secure alternative | low | 288 |
| 49 | ll. 1–3, continuation of (b) | `\nu_{i'}` | `\gamma_{i'}` | low | 305 |
| 49 | ll. 5–7, diagram (c) and box | `\Gamma` | `\Gamma'` | medium | 311 |
| 49 | ll. 5–7, diagram (c) and box | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 314 |
| 49 | ll. 5–7, diagram (c) and box | `\beta` | No secure alternative | low | 315 |
| 49 | l. 8, cancelled equation | `\beta` | No secure alternative | low | 319 |
| 49 | l. 9, quantifier in (d) | `I` | `I'` | low | 323 |
| 49 | ll. 16–18, final diagram | Unreadable, estimated 1 word(s); gap 1 | No reading proposed | low | 338 |
| 50 | ll. 5–7, exact-sequence diagram | `p'_{i'}` | `f'_{i'}` | medium | 359 |
| 50 | ll. 14–15, first tuple | `\alpha_{i'}` | `\alpha_i` | medium | 375 |
| 50 | ll. 16–17, second tuple | `f'` | `g'` | low | 379 |

### Readings retained without harmonization

These are not proposed corrections; they identify places where a subsequent editor should resist silently imposing one convention.

| Scan | Position | Retained feature | Confidence / limitation |
|---|---|---|---|
| 41–42 | Boxed elements on 41; revised description on 42 | The first membership is written as `\beta_{i'}\in\mathcal E'`; the next page gives `\beta_{i'}\in\mathcal E`. | medium; the prime on 41 is retained rather than removed to suit the formula. |
| 43–44 | Last isomorphism on 43; conditions on 44 | The displayed order `\mathcal E_i\cap\pi` and `T(\bar K)` on 43 is not reversed to agree with the later use of `k_i`. | medium on the ordering; the isomorphism/arrow glyph itself is marked doubtful. |
| 44 | Paragraph below the separator | The replacement of the `\beta_{i'}` by their inverses is explicit. | high on the statement; no retrospective change is made on earlier scans. |
| 45–46 | Tuples and cancelled continuation | The earlier tuple includes `K`; the later displayed tuples do not, and the continuation concerning `k,k'` is struck through. | medium; case and the crowded tuple require caution. |
| 44 and 50 | Ramification indices | `\mathbb N^*` is retained on 44, `\mathbb N` on 50. | high on the visible distinction; the author's convention for `\mathbb N` is not supplied here. |
| 46–47 | Prose abbreviations | `lui-=` and `de =` are not expanded to complete French words. | medium; the separate `De` sign on 46 remains explicitly doubtful. |
| 50 | Final line | `0`-morphismes is retained. | high on the visible numeral; it is not replaced by a more familiar categorical degree. |

## 2. Abbreviations met

Expansions below are interpretive aids only; they have not been substituted into the transcription. Variants with and without stops are retained in the fragment where read.

| As written / retained | Probable expansion or function | Qualification |
|---|---|---|
| `hom`, `hom.`, `homs` | homomorphisme, homomorphismes | In the groupoid passages the object described may be a functor; the abbreviation is not expanded according to that interpretation. |
| `syst.` | système | Used for systems of diagrams or groups. |
| `ens`, `ens.` | ensemble | Usually an index set. |
| `gr.` | groupe, groupes | In the revised object description on scan 43. |
| `iso`, `iso.` | isomorphisme, isomorphismes | Also occurs inside difficult marginal additions. |
| `isom` | isomorphisme | Retained separately from `iso`. |
| `épi` | épimorphisme | In the factorization passage. |
| `aut.`, `autom.`, `autom` | automorphisme, automorphismes | Exact abbreviation and stop vary. |
| `int.`, `intérieurs` | intérieur, intérieurs | The adjective is not to be confused with an independently specified convention for the operator `int`. |
| `int` in `int(g)` | automorphisme intérieur associé à `g` | The excerpt does not separately define the direction of the conjugation convention. |
| `comm.` | commutatif, commutative, commutativité | Expansion depends on the phrase; it is not fixed in the fragment. |
| `ss-groupe` | sous-groupe | Scan 47. |
| `NB`, `NB.` | nota bene | Marginal or parenthetical comment. |
| `i.e.`, `i.e. :` | id est | Preserved as written rather than translated. |
| `mod.` | modulo | The reading itself is uncertain on scan 46. |
| `=` in `lui-=` / `de =` | probably *même* | A shorthand interpretation only, not an expansion in the transcription. |
| `Im` | image | Mathematical operator. |
| `Ker` | noyau | Mathematical operator written with the abbreviation `Ker`. |
| `id` | identité | Mathematical operator. |
| `Spec` | spectre | Mathematical notation, not expanded in the fragment. |

No expansion or external identification is imposed on `T`, `K`, `\Pi`, or the bracketed groups beyond what can be read on these pages.

## 3. Legibility and editorial limitations

The main prose and most large displayed formulas are substantially more legible than the marginal revisions. The least secure passages are the overwritten last equation on scan 41, both margins and several labels of the prism on scan 42, the short left and right notes on scan 44, and the long rotated/oblique notes on scan 45. The short annotation beside (a) on scan 48 is not recovered. Isolated primes, a Latin `p` versus a handwritten `\rho`, `k` versus `\kappa`, and the form of a superscript on a map are recurrent risks; doubtful instances have not been decided from the expected mathematics.

The transcription is a provisional diplomatic reading, not a critically established text. `\illegible{n}` counts are estimates of word-sized units; a crossed-out formula may occupy a single such unit without being literally one word. `\unsure{...}` does not certify that the first alternative is correct. A continuous unmarked phrase is the adopted visual reading, but its presence should not be treated as a guarantee against transcription error.

The crowded prism on scan 42 is described inside `\diagram` instead of being supplied with invented connections. For several small squares, the readable objects and arrows are drawn in `tikz-cd`, while the location and visible direction of an interior curved arrow are described in brackets; an unambiguous 2-cell with reconstructed endpoints is not substituted for it. Circles and separating strokes are recorded with `\figure`. Ordinary boxes are represented with standard LaTeX boxes; the multiple outlines around the homomorphism on scan 48 and the element on scan 49 are retained.

The delivered `.tex` is intentionally a fragment: no preamble, document class, or definitions of the requested editorial macros are included. A temporary wrapper with simple definitions for those macros, standard mathematical LaTeX, and `tikz-cd` successfully processed the fragment to DVI. This checks syntax only, not the handwriting readings; the wrapper and test output are not part of the ZIP. `ampersand replacement=\&` is used in diagrams so that their matrices remain valid inside the `\diagram{...}` macro argument.

## 4. Research notes — English; separate from the transcription

All items below are local to these ten scans. “Unproved claim” means that a proof is not supplied in the readable passage, not that the claim is false or unproved elsewhere. No idea below is represented as new or as an established result. The only fully readable explicit research question is identified below; the incomplete question in the margin of scan 44 is not silently reconstructed.

### R01 — Scan 41, approximately ll. 12–21
**Kind: unproved claim / explicitly qualified expectation.**

The phrase “sauf erreur” qualifies the reduction of the two compatibilities to the kernel-map equation and the displayed equation involving the conjugating elements. A verification needs the directions of the commutation isomorphisms and the convention for `int` fixed before cancelling factors. The distinction between `p` and `\rho` in the overwritten bottom line must first be settled from the image or further source evidence, not from the desired identity.

### R02 — Scan 42, left margin beside the prism
**Kind: unproved claim.**

“Comme les … sont injectifs” is used to argue that the local map is determined by the global map and a conjugating element. A proof should separate uniqueness, which uses injectivity, from existence, which requires a conjugated image to lie in the specified subgroup. If continuity is part of the intended category, it also belongs in the existence argument rather than following from the displayed abstract factorization alone.

### R03 — Scan 42, right margin beside the prism
**Kind: unproved claim; reading-dependent.**

The note appears to propose taking the two families of `\gamma`'s “égaux à 1,” but the choice-of-object explanation is only partly readable. The issue worth checking is whether the required choices can be made simultaneously with the kernel identifications and all the other comparison isomorphisms. This is a provisional research lead, not a secure reconstruction of the marginal assertion.

### R04 — Scans 42–43, final paragraph of 42 and first paragraph of 43
**Kind: unproved claim.**

The manuscript distinguishes commutativity on an image subgroup from commutativity on “\(\Gamma\) tout entier,” invoking the “relation plus précise \((*)\).” A proof should identify that referenced relation unambiguously and check which faces of the prism give each equality. An equality on the image of a structural homomorphism must not be promoted to an equality on all of the target merely by redrawing the diagram.

### R05 — Scan 43, lower half; scan 44, opening definition
**Kind: unpursued implication.**

The proposed object data combine a map to `\Gamma`, an indexed family of subgroups, and identifications involving `T(\bar K)`. It remains worth spelling out the exact dictionary between these data and the preceding groupoid presentation, including which identifications are part of the object rather than choices. The direction of the last displayed isomorphism on scan 43 is a transcription issue to resolve before using that dictionary.

### R06 — Scan 44, condition 2°, approximately ll. 8–11
**Kind: unproved claim.**

The target index is asserted to be “unique!” A proof needs a hypothesis on the indexed subgroup family that forces this uniqueness; no such hypothesis is stated in the displayed condition itself. Earlier manuscript context may supply it, so the claim should be checked against that context rather than rejected or repaired here.

### R07 — Scan 44, the same uniqueness condition
**Kind: own idea. Confidence: high for the conditional diagnostic, not for its applicability to the intended geometric objects.**

As a test of the displayed definition alone, allow two distinct indices to name the same subgroup with the same kernel identification. The inclusion condition would then be unable by itself to choose a unique index. The reason for this test is to locate the missing distinctness or geometric restriction, not to claim a counterexample to a category whose earlier hypotheses have not been supplied.

### R08 — Scan 44, left marginal note beside the ramification condition
**Kind: unproved claim.**

The note says that the integer “est aussi unique.” A proof must show that the scalar action of the allowed integers on the identified kernel distinguishes those integers, after the comparison maps and conjugations have been fixed. The readable page does not give that argument separately.

### R09 — Scan 44, upper left margin
**Kind: conjecture (explicit question; incomplete reading).**

A question beginning “Mais \(\alpha\) … ?!” is visible, but its intervening words are not recovered. It would be unsafe to turn this into a claim that `\alpha` is redundant, determined, or arbitrary. The research task is first to recover the question itself from better source evidence.

### R10 — Scan 44, paragraph below the horizontal separator
**Kind: unpursued implication.**

“Je m'aperçois qu'il vaut mieux remplacer” introduces the change from the conjugating elements to their inverses and a reversed orientation of the commutation isomorphism. The associated composition and change-of-choice formulas should be derived afresh under that stated convention. This is a reason to keep the earlier formulas diplomatic, not a licence to rewrite them retrospectively.

### R11 — Scan 44, bottom, continuing on scan 45, top
**Kind: unproved claim.**

The text proposes recovering the intermediate groupoid by “factorisation canonique” and describes a factor as “fidèle.” A proof should construct both factors, verify the stated effects on `\pi_0` and `\pi_1`, and specify the sense in which the construction is canonical. Its compatibility with the comparison data is also needed if it is to replace the four-cornered diagram at the level of morphisms.

### R12 — Scan 45, upper left rotated margin
**Kind: unproved claim; partly reading-dependent.**

The relative fundamental-group datum is said to form a “syst. local,” with a Kummer identification expressed using a pullback. The precise typeface and some symbols in the marginal formula remain uncertain. A proof would need to establish the descent/transport of the kernels and the naturality of the identification, not just identify each kernel separately.

### R13 — Scan 45, lower left oblique margin
**Kind: unpursued implication.**

The margin associates the ramification datum with an application from a component set to `\mathbb N^*`. This suggests checking how the componentwise integers transform under composition and under changes of representatives. The presence of the later character factor on scan 50 makes that compatibility a substantive check, rather than a matter of multiplying labels without regard to the comparison maps.

### R14 — Scans 45–46, paragraph on morphisms and its cancelled continuation
**Kind: unproved claim.**

The text describes comparison isomorphisms of the two functors and “deux conditions de compatibilité sur les deux carrés.” A complete formulation should write both conditions with their actual sources, targets, and order of whiskering. The cancelled reference to `k,k'` should be examined as evidence of a revision in the required data, not silently restored as an extra axiom.

### R15 — Scan 46, middle and lower paragraphs
**Kind: unproved claim.**

Changing the chosen isomorphisms or reference objects is said to change the resulting homomorphisms by “autom. int.” or to determine replacements “à aut. int. près.” A proof should give the comparison element explicitly and verify the effect of composing two changes of reference data. This is also the check needed before passing to an exterior description in the following pages.

### R16 — Scans 47–48, exterior-group discussion and explicit question
**Kind: conjecture (explicit question).**

The central question is: “mais comment en termes de groupes extérieurs exprimer les données de Kummer \(k_i\) ?” The challenge stated here is not merely to retain the homomorphism classes, but to express the additional Kummer data in that language. The subsequent return to systems of diagrams should be checked for an intrinsic answer to this question rather than presumed to supply one automatically.

### R17 — Scans 47–48, the same exterior-group question
**Kind: own idea. Confidence: medium; motivated by the explicit retention of the kernel identifications in the diagram presentation.**

A candidate formulation would retain an exterior homomorphism together with conjugacy classes of the kernel injections and explicitly transported `T(\bar K)`-identifications. The test is whether this extra marking makes the notion independent of reference-object choices while still recovering the displayed comparison data. Neither existence of such a satisfactory category nor equivalence with the manuscript's presentation is claimed here.

### R18 — Scans 48–49, items (a)–(d)
**Kind: unproved claim.**

The phrase “s'explicite par” introduces the global homomorphism, index map, local homomorphisms and two families of commutation data. The converse construction from those data to a groupoid-level morphism is worth writing out, together with the change-of-choice identifications in (a) and (b). The numerical grading of morphisms should be retained as written until the surrounding convention is established.

### R19 — Scan 49, last paragraph
**Kind: unproved claim.**

“\(c,d\) ensemble définissent” leads to the product `\beta_{i'}=p(\alpha_{i'})\alpha`. Verification requires pushing the inner-conjugation datum through `p` and keeping the order of the two factors. A calculation in a noncommutative test case would be more diagnostic of an orientation error than an abelian example.

### R20 — Scan 50, middle, boxed formula
**Kind: unproved claim.**

“on trouve” precedes `f^0_{i'}=d_{i'}\chi(\beta_{i'})\operatorname{id}_{T(\bar K)}`. A derivation should compare the Kummer identifications with the base conjugation in the exact-sequence diagram, checking whether the chosen convention gives the displayed character factor or an inverse. The page calls `\chi` the “caractère canonique”; no additional identification of that character is imposed in the transcription.

### R21 — Scans 44 and 50, ramification-index notation
**Kind: own idea. Confidence: low as a mathematical issue; the author's convention for `\mathbb N` is not established by this extract.**

The visible shift from `\mathbb N^*` to `\mathbb N` suggests a notation check before allowing or excluding a zero scalar in the kernel formula. If the latter set includes zero in the author's convention, testing the zero-kernel-map case would clarify whether some earlier condition rules it out. This is not evidence that the manuscript contains a contradiction.

### R22 — Scans 44, 49–50, conventions and composition
**Kind: own idea. Confidence: medium; the explicit inversion revision and the ordered product of conjugators make this a useful diagnostic.**

One could test the formulas in finite quotients for which the relevant action on a finite quotient of `T(\bar K)` is defined, checking identity morphisms, successive conjugations, and composition of ramification scalars. Such tests could expose a missed inverse, an order reversal, or a misplaced prime. They would not establish a general profinite statement or justify changing a doubtful handwritten symbol.

### R23 — Scan 50, final paragraph and final line
**Kind: unpursued implication / announced next step.**

The page ends by proposing to determine “les 0-morphismes de l'un dans l'autre.” Their actual formula is not present in the supplied ending. The continuation should be checked for the comparison of two index maps and for compatibility with the two commutation data before any composition law or equivalence claim is extracted from this announcement.
