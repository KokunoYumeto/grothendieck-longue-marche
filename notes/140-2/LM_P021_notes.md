# LM_P021 — Notes accompanying the diplomatic transcription

## Scope, source, and pagination

This file accompanies `LM_P021_transcription.tex`. The transcription is a visual reading of the ten supplied JPEGs only; it does not use OCR, a published transcription, or external literature to complete the handwriting. Research observations below are separate from the French transcription and do not authorize corrections to it.

Bibliographic description, as supplied in the task brief: Grothendieck, A. (1981). *La Longue Marche à travers la théorie de Galois* [Unpublished manuscript, cote 140-2, archive file “pages 1–292,” supplied scans 201–210]. Université de Montpellier. This description has not been independently verified against an external catalogue.

The scan identifiers, not the footer numbers, control `\scanpage`. The upper-edge numbering is encoded with `\mspage`; the separate lower-left series is recorded here, but its authorship is not established and it has not been silently substituted for the upper-edge numbering. Printed archive footers, borders, and institutional addresses are not manuscript text.

| Scan identifier | Lower-left handwritten / printed footer number | Upper-edge number encoded as `\mspage` |
|---|---|---|
| 201 | 200 / 200 | None securely visible |
| 202 | 201 / 201 | 101 |
| 203 | 202 / 202 | None securely visible |
| 204 | 203 / 203 | 102 |
| 205 | 204 / 204 | None securely visible |
| 206 | 205 / 205 | 103 |
| 207 | 206 / 206 | None securely visible |
| 208 | 207 / 207 | 104 |
| 209 | 208 / 208 | None securely visible |
| 210 | 209 / 209 | 105 |

The fragment begins with `\scanpage{201}`, has no preamble or macro definitions, and retains formulas (1)–(29). The diagram at (16) is encoded in `tikz-cd`; its ampersand replacement is required because the environment is inside `\diagram{…}`. A temporary, unbundled LaTeX wrapper with neutral definitions of the editorial macros compiled successfully to DVI; this checks syntax, not the correctness of readings or the eventual appearance of the recipient’s macro definitions.

## 2. Table of doubts

Locations are approximate handwritten baselines, counting displays as part of the page and locating marginal/interlinear material beside the corresponding main text. Exact line numbers in the delivered TeX fragment are also supplied. “Confidence” concerns the proposed reading, not the truth of a mathematical claim; `\illegible{n}` counts are estimates. Repeated glyphs are sometimes listed repeatedly so that no local doubt is hidden by a global convention.

| Scan | Approximate manuscript line / exact TeX line | Proposed reading | Alternative or limitation | Confidence |
|---|---|---|---|---|
| 201 | ≈1, cancelled opening and interline; TeX L3 | `conforme` | No specific alternative proposed. | low |
| 201 | ≈1, cancelled opening and interline; TeX L3 | `complexe` | No specific alternative proposed. | low |
| 201 | ≈2, cancelled opening; TeX L4 | `invariante` | No specific alternative proposed. | medium |
| 201 | ≈5; TeX L8 | `$\mathcal E^!$` | No specific alternative proposed. | medium |
| 201 | ≈7; TeX L10 | `i.e.` | No specific alternative proposed. | medium |
| 201 | ≈7; TeX L10 | `\illegible{1}` | No reading proposed; 1 word(s) estimated, not a measured count. | low |
| 201 | ≈8; TeX L11 | `\illegible{1}` | No reading proposed; 1 word(s) estimated, not a measured count. | low |
| 201 | ≈10; TeX L13 | `\illegible{1}` | No reading proposed; 1 word(s) estimated, not a measured count. | low |
| 201 | ≈14; TeX L17 | `$\Gamma_0\subset\mathrm{Centre}$` | `$\Gamma_0\in\mathrm{Centre}$` | medium |
| 201 | ≈14; TeX L17 | `$\Gamma_0\hookrightarrow\mathcal E$` | No specific alternative proposed. | medium |
| 201 | ≈15; TeX L18 | `invariant` | No specific alternative proposed. | medium |
| 201 | ≈19, cancelled paragraph; TeX L23 | `b` | No specific alternative proposed. | low |
| 202 | ≈1, cancelled continuation; TeX L29 | `$(X,S,a)$` | No specific alternative proposed. | medium |
| 202 | ≈3, cancelled continuation; TeX L31 | `$\Gamma_0$` | No specific alternative proposed. | medium |
| 202 | ≈4, cancelled continuation; TeX L32 | `$\overline{\mathrm m}$` | `$=$` | medium |
| 202 | ≈6, cancelled passage; TeX L34 | `puissent` | No specific alternative proposed. | medium |
| 202 | ≈7, cancelled/revised passage; TeX L35 | `du ss-groupe engendré` | No specific alternative proposed. | low |
| 202 | ≈7, interline within cancellation; TeX L36 | `ss-groupe engendré` | No specific alternative proposed. | low |
| 202 | ≈8, cancelled passage; TeX L37 | `par` | No specific alternative proposed. | low |
| 202 | ≈11, cancelled quotient passage; TeX L41 | `$\Gamma/\Gamma_0$` | `$\Gamma'/\Gamma_0$` | low |
| 202 | ≈11, cancelled quotient passage; TeX L41 | `isotypiquement` | `isotopiquement` | low |
| 202 | ≈14; TeX L46 | `tt` | No specific alternative proposed. | medium |
| 202 | ≈15; TeX L47 | `$\Rightarrow$` | No specific alternative proposed. | medium |
| 203 | ≈1, interline/overwriting; TeX L62 | `est` | No specific alternative proposed. | medium |
| 203 | ≈7; TeX L69 | `on peut en trouver` | No specific alternative proposed. | low |
| 203 | ≈8, cancelled example; TeX L70 | `$\operatorname{Autext}(\pi,i)$` | No specific alternative proposed. | low |
| 203 | ≈9, cancelled example; TeX L71 | `$i\in I(\pi)$` | No specific alternative proposed. | low |
| 203 | ≈10, cancelled example; TeX L72 | `\illegible{2}` | No reading proposed; 2 word(s) estimated, not a measured count. | low |
| 203 | ≈11, cancelled example; TeX L73 | `\illegible{2}` | No reading proposed; 2 word(s) estimated, not a measured count. | low |
| 204 | ≈2, opening definition; TeX L79 | `orientable` | No specific alternative proposed. | medium |
| 204 | ≈3, cancellation; TeX L80 | `l'ensemble des orientations` | No specific alternative proposed. | low |
| 204 | ≈4, framing brackets; TeX L81 | `$[$` | `$]$` | medium |
| 204 | ≈4, framing brackets; TeX L81 | `$]$` | `$[$` | medium |
| 204 | ≈5, before (1); TeX L83 | `$\forall\nu\in\mathbb N$` | No specific alternative proposed. | medium |
| 204 | ≈6, (1); TeX L85 | `x_{g,i}` | `a_{g,i}` | medium |
| 204 | ≈20–23, lower-left margin; TeX L114 | `un isom.` | No specific alternative proposed. | low |
| 204 | ≈20–23, lower-left margin; TeX L114 | `\illegible{3}` | No reading proposed; 3 word(s) estimated, not a measured count. | low |
| 204 | ≈20–23, lower-left margin; TeX L118 | `comp.` | No specific alternative proposed. | low |
| 204 | ≈20–23, lower-left margin; TeX L118 | `\illegible{1}` | No reading proposed; 1 word(s) estimated, not a measured count. | low |
| 204 | ≈22, before (6); TeX L119 | `un` | No specific alternative proposed. | medium |
| 204 | ≈23, (6); TeX L122 | `\mathfrak S_\nu` | No specific alternative proposed. | medium |
| 205 | ≈17, (13), overwriting; TeX L160 | `$X_g$` | No specific alternative proposed. | low |
| 205 | ≈18, (13), interline; TeX L161 | `\nu^{\text{ième}}` | No specific alternative proposed. | low |
| 205 | ≈21, end of (13); TeX L164 | `\mathcal P_\nu(X_g)` | No specific alternative proposed. | medium |
| 205 | ≈17–23, lower-left margin; TeX L167 | `des espaces` | No specific alternative proposed. | low |
| 205 | ≈17–23, lower-left margin; TeX L167 | `\illegible{2}` | No reading proposed; 2 word(s) estimated, not a measured count. | low |
| 205 | ≈17–23, lower-left margin; TeX L169 | `s'en vont vers` | No specific alternative proposed. | low |
| 205 | ≈17–23, lower-left margin; TeX L170 | `a_{g,0}` | No specific alternative proposed. | low |
| 205 | ≈24, (14), overwritten argument; TeX L177 | `\illegible{1}` | No reading proposed; 1 word(s) estimated, not a measured count. | low |
| 206 | ≈1; TeX L184 | `respectant` | No specific alternative proposed. | medium |
| 206 | ≈5, (15); TeX L190 | `=` | `\supset` | medium |
| 206 | ≈8, before (16); TeX L195 | `d'homéo` | No specific alternative proposed. | low |
| 206 | ≈8, before (16); TeX L195 | `\illegible{1}` | No reading proposed; 1 word(s) estimated, not a measured count. | low |
| 206 | ≈10–11, left margin beside (16); TeX L203 | `fonct.` | No specific alternative proposed. | low |
| 207 | ≈9, before (19); TeX L234 | `\illegible{1}` | No reading proposed; 1 word(s) estimated, not a measured count. | low |
| 207 | ≈19, (22); TeX L255 | `\vert` | No specific alternative proposed. | low |
| 207 | ≈22, final interline; TeX L259 | `ou de $A_{g,S}$` | No specific alternative proposed. | low |
| 207 | ≈22–23, final cancellation; TeX L260 | `et a fortiori en termes` | No specific alternative proposed. | low |
| 207 | ≈22–23, final cancellation; TeX L260 | `du groupe` | No specific alternative proposed. | low |
| 208 | ≈16, before (27); TeX L299 | `\illegible{1}` | No reading proposed; 1 word(s) estimated, not a measured count. | low |
| 208 | ≈17, (27); TeX L301 | `A_{g,\nu}` | `A_{g,x}` | medium |
| 208 | ≈20, new definition; TeX L306 | `$\mathcal E$` | `$\mathcal X$` | low |
| 209 | ≈1, opening and revision; TeX L310 | `\mathcal E` | `\mathcal X` | low |
| 209 | ≈1, opening and revision; TeX L310 | `donnée de` | No specific alternative proposed. | low |
| 209 | ≈4; TeX L313 | `$\mathcal E$` | `$\mathcal X$` | low |
| 209 | ≈5, interline; TeX L314 | `Il revient au $\overline{\mathrm m}$ de dire que` | No specific alternative proposed. | low |
| 209 | ≈7, revised sentence; TeX L316 | `$\mathcal E$` | `$\mathcal X$` | low |
| 209 | ≈7, revised sentence; TeX L316 | `comme` | No specific alternative proposed. | low |
| 209 | ≈10, revised sentence; TeX L320 | `\illegible{2}` | No reading proposed; 2 word(s) estimated, not a measured count. | low |
| 209 | ≈10, revised sentence; TeX L320 | `$\mathcal X$` | `$\mathfrak X$` | low |
| 209 | ≈10–11, revised sentence; TeX L321 | `\illegible{3}` | No reading proposed; 3 word(s) estimated, not a measured count. | low |
| 209 | ≈14, interline; TeX L327 | `par` | No specific alternative proposed. | low |
| 209 | ≈14, interline; TeX L327 | `\mathcal E` | `\mathcal X` | low |
| 209 | ≈16; TeX L330 | `orientées` | `orientables` | medium |
| 209 | ≈18, cancellation/interline; TeX L332 | `tout auto` | No specific alternative proposed. | low |
| 209 | ≈18, cancellation/interline; TeX L332 | `$u$` | No specific alternative proposed. | low |
| 210 | ≈1; TeX L337 | `$\mathcal E$` | `$\mathcal X$` | low |
| 210 | ≈2, right edge; TeX L338 | `i.e.` | No specific alternative proposed. | low |
| 210 | ≈4; TeX L341 | `orientées` | `orientables` | medium |
| 210 | ≈7, upper-right interline; TeX L344 | `$U_\nu$` | `$\widetilde U_\nu$` | low |
| 210 | ≈10, closing delimiter; TeX L347 | `)` | `\}` | low |
| 210 | ≈11, interline and main text; TeX L348 | `d'esp. homog.` | No specific alternative proposed. | low |
| 210 | ≈11, interline and main text; TeX L348 | `orientée` | `orientable` | low |

| 201–202 | Cancelled geometric argument, scan 201 ≈16–21 and scan 202 ≈1–12 | The geometric realization passage is treated as cancelled across the page break. | Several long diagonal strokes and shorter cancellations overlap; the exact scope of every individual stroke cannot be recovered securely. | medium |
| 203 | ≈7–11 | Cancellation begins with the example after “belle jambe”. | Some diagonal strokes rise into the preceding line; the boundary between retained comment and cancelled example is uncertain. | medium |
| 204 | ≈7, left margin | `NB on` before the displayed membership involving `a_{g,\nu}` | The connection of “on” with the mathematical expression is not fully clear; no missing verb has been supplied. | low |
| 205–208 | (7)–(15), (20)–(27) | Superscript `!` on the pointwise stabilizers and their quotients | It is not normalized to a prime; the dot and vertical stroke are particularly clear in (7), (12), and (14). | high |
| 204–208 | (6), (8), (12), (13), (21)–(26) | `\mathfrak S_\nu` and `\mathcal P_\nu` | The mathematical letters are recognizable, but exact handwritten alphabet/style is less certain than their subscripts; the first occurrence of each is marked. | medium |
| 208 | (24), (26), last equality in each | `\ne X_g` | No complement is visibly written after `X_g`; the mathematical problem is discussed in Research note R14, not corrected in the fragment. | high |
| 209 | ≈4 | `A_1` | The visible subscript does not securely include `g`; it has not been expanded to `A_{g,1}`. | high |
| 208–210 | Conjugacy-class notation | The alternatives `\mathcal E` / `\mathcal X` are retained locally. | The glyph is overwritten in several places and must not be treated as a securely identified new alphabet. The surface glyph in (28) is also not completely secure. | low |
| 210 | (29) | `G\longrightarrow\operatorname{Aut}(U_\nu)` | No subscript is visibly attached to the `G` in this display, despite `G_\nu` in the surrounding prose. | high |

## 3. Abbreviations met

Expansions here are interpretive aids only. They are not inserted in the transcription. Several items are ordinary mathematical notation rather than verbal abbreviations; they are included because their abbreviated form matters for reading the pages.

| As written / represented | Probable expansion or function | Qualification |
|---|---|---|
| `ss-groupe`, `ss-groupes` | sous-groupe, sous-groupes | Retained as abbreviated in prose. |
| `int` | automorphisme intérieur, conjugaison | In expressions such as `int(g)`. |
| `i.e.` | id est | The final occurrence at scan 210, line ≈2 is uncertain and not completed. |
| `OPS` | on peut supposer | Interpretation of the compact handwritten abbreviation. |
| `mod` | modulo | In “mod π-conjugaison”. |
| `top.` | topologie / topologique | Expansion depends on the local grammar. |
| `hyp` | hypothèse | In “par hyp”. |
| `préc.` | précédent / précisé | The cancelled passage does not determine the expansion beyond doubt. |
| `NB` | nota bene | Sometimes underlined. |
| `cqfd.` | ce qu’il fallait démontrer | At the end of the argument on scan 203. |
| `p.ex.` | par exemple | In the cancelled example on scan 203. |
| `isom.` | isomorphe / isomorphisme | The example is partly illegible. |
| `iso.` | isomorphisme | Scan 209. |
| `Aut` | automorphismes | For a surface, the page’s topological context supplies the relevant meaning; for `π`, it concerns group automorphisms. |
| `Aut top` | automorphismes topologiques | The cancelled passage on scan 202. |
| `Autext` | automorphismes extérieurs | The surrounding arguments/subscripts in scan 203 are doubtful. |
| `pts` | points | No expansion in the French fragment. |
| `str.` | strictement | Increasing/decreasing sequences. |
| `autom.` | automorphisme(s) | Scan 204 and the automorphism criterion on scan 209. |
| `conv.` | convergence | Topological descriptions. |
| `can.` | canonique | In “homomorphisme can.” and “application can.” |
| `card` | cardinal | Formula (1). |
| `Norm` | normalisateur | Ambient group is retained where it is explicitly written. |
| `Mon` | monomorphismes; here plausibly injections | This interpretation is based on the adjacent description by tuples of distinct points. |
| `Sym` | produit symétrique | The notation is written next to the full French phrase. |
| `ens.` | ensemble | Scan 207. |
| `conj.` | conjugaison | Upper-right insertion on scan 210. |
| `homéom.` | homéomorphe / homéomorphisme | A cancelled phrase on scan 209. |
| `d’homéo` | d’homéomorphismes, possibly | The end of the line before (16) is doubtful. |
| `comp.` | compacte / sur les compacts, possibly | Lower-left marginal topology note on scan 204; surrounding text is not secure. |
| `tt` | tout | Tentative reading in scan 202, “Γ tt entier”. |
| `fonct.` | fonction / foncteur, possibly | Very uncertain isolated marginal reading beside (16). |
| `esp.`, `homog.` | espace, homogène | Both belong to a doubtful interlinear phrase on scan 210. |
| `\overline{\mathrm m}` | même | The sign is not expanded in the fragment; on scan 202 a literal equality sign remains an alternative reading. |
| `ssi` | si et seulement si | Automorphism criterion across scans 209–210. |

## 4. Legibility and limits

The main definitions and most numbered displays on scans 204–208 are appreciably more legible than the first proof and the final heavily revised paragraphs. The least reliable areas are the overwritten opening of scan 201, the overlapping cancellations and insertions in the top half of scan 202, the crossed example on scan 203, the lower-left notes on scans 204–205, and the conjugacy-class notation and interlinear revisions on scans 209–210. Exact alphabet/style, short abbreviations, and the scope of individual cancellation strokes remain less secure than many full words.

The fragment deliberately preserves apparent inconsistencies: the initial `i∈N*` sequence versus the subsequent bounds starting at zero; the possible `x_{g,i}` in (1) alongside `a_{g,i}` elsewhere; `(X',S',b)` after the introduction of `a'`; the `X` versus `X_g` occurrences in configuration-space notation; `A_1` on scan 209; the unindexed `G` in (29); and the visible `≠ X_g` orbit conditions. These are not invitations to normalize the text. The opening proof refers to prior material not supplied here, and the final “On trouve encore” continues beyond the supplied excerpt.

The cancellation scopes and several margin insertions are best-effort reconstructions of the physical page, not a definitive account of revision order. No attempt has been made to infer an authorial sequence of drafts beyond what the visible placement and strokes support. No quantitative accuracy claim is made.

## 5. Research notes — separate from the transcription

These observations are in English. They concern only the supplied pages and distinguish source assertions from possible lines of investigation; no external literature was used to establish them, and no idea is claimed to be new. No securely legible formal “je conjecture” statement occurs in this excerpt; the clearest explicit doubt belongs to a cancelled argument. For an item described as an unproved claim, the meaning is “not established in the supplied pages,” not “unproved elsewhere in the manuscript.”

**R01 — Scans 201–203, opening proof; kind: unproved claim.** The passage starts “Démontrons d)” and ends “cqfd.”, but the statement of (d), the extension involving `π` and `E`, and the hypotheses on `Γ′, Γ″` are not supplied. A reliable proof audit therefore requires the preceding statement, particularly the hypotheses ensuring the fixed-subgroup assertion used on scan 202. The text here should not be promoted into a standalone theorem with reconstructed hypotheses.

**R02 — Scan 201, ≈19–21, cancelled argument; kind: unproved claim.** The cancelled paragraph invokes “le résultat (b)”—the letter remains doubtful—concerning “existence et … unicité” of realizations in the cyclic case. The cited result is not proved on these pages, and the relationship between that uniqueness and simultaneous realization of the two groups needs to be recovered from earlier material. Its cancelled status matters: it is evidence of an attempted route, not of the final proof strategy.

**R03 — Scan 202, ≈4–8, cancelled argument; kind: conjecture.** The explicit doubt “Mais il n’est pas clair à priori” concerns compatibility of the two actions and, in the revised wording, finiteness of the subgroup they generate in the topological automorphism group. This is a question/doubt in a discarded argument, not a formal affirmative conjecture. A useful investigation would isolate what additional compatibility datum would make the joint realization possible.

**R04 — Scan 202, ≈13–25; kind: unproved claim.** The surviving proof constructs the centralizer `\widetilde Γ` and uses “π^{Γ₀}=(1)” to obtain injectivity, then gives an argument for surjectivity onto `Γ`. What is not justified locally is the fixed-subgroup premise and the precise sense in which `int(g).Γ₀` is compared with `Γ₀`: an embedded subgroup, a parametrized action, or a homomorphism can lead to different centralizer/normalizer statements. Recovering that convention is necessary before checking the passage from normalizing `Γ₀` to centralizing it.

**R05 — Scan 203, ≈3–7; kind: unproved claim.** The note says that without having “supposé Γ fini” it would remain true that the two groups generate a subgroup disjoint from `π`. The finite-group assumption therefore appears to be doing work beyond triviality of this intersection. The crossed example below may illustrate the limitation, but its `Autext` expression and final centralizer object are too uncertain to use as a reliable example.

**R06 — Scans 204–205, initial sequence, (1), and (7); kind: own idea.** The displayed sequence is indexed by `N*` and begins with `a_{g,1}`, whereas (1) and (7) visibly use indices from zero through `ν−1`; the first letter of the points in (1) is also doubtful between `x` and `a`. Before deriving an actual tower from these definitions, an editorial audit should locate where the indexing convention was changed or supplied. **Confidence: high for the visible indexing discrepancy, medium for the letter discrepancy; reason:** the bounds and the initial list are legible, while the first letter in (1) is overwritten.

**R07 — Scan 204, (5) and lower-left margin; kind: unproved claim.** The restriction map is called an “isomorphisme canonique,” and the margin appears to strengthen this to a statement about topological groups. A proof would have to show that homeomorphisms of the finitely punctured surface extend uniquely over the missing points, and then verify continuity of extension and restriction for exactly the topologies intended. The marginal description of the topology is not legible enough to settle that final requirement from this excerpt alone.

**R08 — Scans 204–205, (6)–(12); kind: unproved claim.** The text asserts a “homomorphisme can. surjectif” to the permutation group and passes to the component quotients. A proof should realize each permutation of the marked set, identify the pointwise stabilizer as the kernel, and justify why the identity component fixes the finite set pointwise. The passage to the second exact sequence should be checked at the level of components rather than assumed from formal functoriality of `π₀`.

**R09 — Scan 205, (13)–(14); kind: unproved claim.** The “homéomorphismes canoniques” identify homogeneous quotients with unordered and ordered configuration spaces. Establishing them requires transitivity on the corresponding finite configurations and an identification of the quotient topology with the indicated open-subspace topology. Local sections of evaluation maps would be a possible proof mechanism, but none is constructed here.

**R10 — Scan 206, (16), ≈12–13; kind: unpursued implication.** The right-hand vertical map is explicitly described as “restriction de I_ν à I_{ν′}”. Taking `ν′=ν−1` suggests studying the fibers of a one-point-forgetting map and how adjacent stabilizers encode them. These pages do not assert a fibration theorem; local triviality and its consequences would need separate arguments.

**R11 — Scans 205–206, (14)–(16); kind: own idea.** One can investigate the fundamental groups of the ordered and unordered configuration spaces appearing here and ask how the tower maps organize braid-type groups and their actions on punctured-surface fundamental groups. This is a proposed connection, not a literature identification or a claim that the manuscript proves such a relationship. **Confidence: medium; reason:** the spaces and forgetful maps are explicit, but the needed path-lifting or fibration statements are absent.

**R12 — Scan 207, (19)–(22); kind: unproved claim.** The phrase “on voit de suite” introduces self-normalization of point stabilizers, followed by analogous assertions for finite-set and pointwise stabilizers. A proof can be sought by reconstructing the marked set from fixed points or finite orbits and then showing that a normalizer must preserve that reconstructed set. The distinction between the setwise stabilizer and the pointwise stabilizer must remain explicit in this argument.

**R13 — Scan 208, (23), (25), and the first two descriptions in (26); kind: unproved claim.** The asserted strengthening recovers `S` even from the identity component `A_{g,S}^{\circ}` and yields injectivity of the conjugacy-class map. A proof would need enough isotopies supported away from `S` to move every point outside `S`, and enough such motions to rule out finite nontrivial outside orbits. This should be checked in the actual topology on the homeomorphism group, not merely as an abstract action argument.

**R14 — Scan 208, last equalities of (24) and (26); kind: own idea.** The transcription retains `S={x∈X_g | A_{g,S}.x≠X_g}` and its identity-component analogue, because that is the visible reading. For nonempty finite `S`, every stabilizer orbit of a point outside `S` remains in `X_g−S`, and every orbit of a point of `S` remains in `S`, so the displayed right-hand condition holds for every point of `X_g`, not just for points of `S`. Comparing instead with `X_g−S` is a possible intended formulation, but is only an editorial hypothesis and has not been substituted. **Confidence: high in this conditional inconsistency check; reason:** preservation of `S` alone gives the orbit containment, independently of transitivity or any outside theorem.

**R15 — Scan 208, (27); kind: unpursued implication.** The equality of the three normalizers packages the setwise, pointwise, and identity-component stabilizers as different ways of detecting the same finite subset. This suggests investigating which information about `S` is retained after discarding the quotient permutation action and keeping only the connected subgroup. The valid fixed-point description, rather than the problematic final orbit equality, should be the starting point.

**R16 — Scan 209, (28) and ≈14–17; kind: unproved claim.** The text claims “une équivalence de catégories” between the indicated Teichmüller pairs and surfaces. A full statement needs the class of morphisms, the topology on the conjugacy class, and a proof of full faithfulness as well as reconstruction of objects; those details are not supplied here. In particular, the phrase should not be silently enlarged to a claim about all continuous group homomorphisms.

**R17 — Scans 209–210, final/initial lines; kind: unproved claim.** The assertion “u est intérieur ssi il conserve la classe” is accompanied by the statement that the center is trivial. A proof of the forward criterion is formal, while the converse should use the reconstructed surface and (28) to identify a class-preserving topological automorphism with conjugation by a homeomorphism. Triviality of the center requires a separate faithfulness/local-motion argument; the trailing “i.e.” does not provide one in the supplied excerpt.

**R18 — Scans 209–210, automorphism criterion; kind: own idea.** The conditional innerness statement suggests asking whether the distinguished conjugacy class of point stabilizers is intrinsically recognizable from the topological group alone. If it is not shown to be characteristic, the excerpt does not by itself imply that every topological automorphism is inner. **Confidence: high in this logical distinction, medium in the proposed characterization program; reason:** preservation of the class is an explicit extra condition in the manuscript’s criterion.

**R19 — Scan 210, ≈3–19 and (29); kind: unproved claim.** The proposed punctured analogue uses a subgroup represented by `A_{g,ν}∩A_{g,ν+1}` and again concludes with “une équivalence”. A proof would need to identify this intersection as the relevant point stabilizer in the punctured surface, recover the homogeneous-space topology, and verify the claimed topological group isomorphism. The notation changes between `G_ν` and `G` in (29), and the final sentence “On trouve encore” is unfinished within the supplied material.
