# Concrete corrections to the root research draft

Review scope: R001–R082 of `research_root_draft.md`, checked against the frozen page TeX and supplied context. The last reviewed root-draft SHA-256 is `ed8c9a62b500680bbafbffa690c269f45375ec3428cc7963fea933aa5a726da0`, captured at **2026-11-15T12:13:52.607536+00:00**; every correction below was observed as applied in that snapshot, and no correction remains pending from this review. The research reader edited this review record and its own comparison notes only.

## Corrections and dispositions

1. **R001 — applied: remove the unsupported adjunction identification.** Scans043:5–23, 51–61 and044:3–18 contain fraction, replacement, and cylinder-like diagrams, including `[i]^{-1}[\unsure{u}]=[i']^{-1}`, without a labelled adjunction or a declared identification with `λ_!⊣λ^*`. The revised note reports the diagrams as material to collate with localization and no longer calls their arrows adjunction arrows.

2. **R002 — applied: remove invented source notation `T`.** Scan045:99–102 gives the unnamed rules `(x,y)↦(x+y,λ(y))` and `(x,−x)↦(0,λ(x))`; it does not name a map `T`. The revised note quotes those two rules and keeps its explicit substitution check separate.

3. **R004–R006 — applied: restore the written unit, subscript, and isomorphism mark, and specify the adjunction comparison.** Scan046:20 has `L_iφ(ℤ_𝓜)=0`, scan046:44 cancels `J_𝓜^+=ℤ_𝓜`, and scan047:52 has `l\xleftarrow{\sim}φκ(l)≃Lφκ(l)`. The first two abbreviations and the missing tilde have been corrected; R006 now compares `φ⊣κ` with PS VII §134(1)–(3), pp.557–558, and identifies the written link `λ^*(U)≃κ(U)` on scan055:79–101 for degree-zero `U`, rather than identifying the pair directly with the localized square (7)–(8).

4. **R012, R015, R048, R055, R060 — applied: remove the mistaken PS VI §§117–118 references.** In `ps6.tex`, §117 at lines2471–2473 concerns schematic/formal homology, and §118 at2691–2694 concerns Lie functors and homotopy groups; the archive cotes117–118 named by README are not these section numbers. The revised comparisons use PS VII §135, pp.561–564, and §138, pp.583–585, where the category-of-elements, relative homology, and projective/injective restriction formulas actually occur, or omit the erroneous citation.

5. **R018 — applied: retain the unheaded end connectors.** Scan051:87 draws `0` joined without an arrowhead to `x`, then arrows to `J⊗x` and `x[1]`, followed by an unheaded connector to `0`. The revised note calls this the lower diagram and retains the two end connectors instead of quoting every connector as an arrow.

6. **R019 — applied: retain the nonzero degree-zero homology allowed by the source.** The target complex on scan052 has projective terms, `H_i(L'_•)=0` for `i>0`, and projective `H_0(L'_•)`; the former description as simply an acyclic complex suppressed that last possibility. The revised note reports all three conditions.

7. **R025 — applied: report the written bicomplex proof without adding a boundedness gap.** Scan054:63–76 explicitly labels “Dém.”, uses `P_•^x→x`, and explains the two comparison quasi-isomorphisms by `Λ_•(P_i^x)` resolving `φ(P_i^x)` and `Λ_j(P_•^x)` resolving `Λ_j(x)` through exactness of `Λ_j`; the neighboring complex tests explicitly use `i∈ℕ` at scan053:35. The revised note reports these written resolution arguments and removes the unsupported assertion that unresolved totalization/boundedness conventions constitute a missing proof step.

8. **R032 — applied: retain the uncertain kernel coefficient.** The full frozen formula at scan058:30 is `\unsure{\widetilde W_h^P(I)}\otimes F=\operatorname{Ker}(F^{(I)}\longrightarrow F)`. The revised note preserves that left-hand coefficient instead of letting the isolated kernel expression serve as an unqualified identification with the nearby `J⊗x` construction.

9. **R033 — applied: identify the cube and the actual status sources.** Strong W(7) is the cube comparing two cover squares in `DER_XIIb-a.tex`:764–807, not a “two-section diagram”. `RESULTS_STATE.md`:74 explicitly lists TOTASPH A.9, while the A.13 review is reported by `NEW_RESULTS.md`:25 (#8); the revised note states that provenance, and its reviewed Δ_inj counterexample attribution remains supported by `NEW_RESULTS.md`:28 (#11).

10. **R040 — applied: remove the nonexistent contents-page ranges.** `PURSUING_STACKS_CONTENTS.md` provides section numbers and titles, not the page ranges formerly attributed to it. The revised note refers to its titles and attributes the “pages259 à381” and “trois pages de table des matières” information to scan064 itself.

11. **R047, R067, R075, R076 — applied: remove the invented README reuse warning.** The complete `context/README.md` describes the handwritten notes as “s.d.” at line9, mentions listing paper at17–18, and restricts the context to research notes, but contains no specific reused-sheet/material-provenance caution. The revised entries attribute the sheet evidence to the frozen text and the reuse instructions to the supplied task, without attributing that warning to README.

12. **R052 — applied: narrow the missing-step description to the written question.** Scan070:27–29 places a question mark on `RHom(a,RΓ(B,F))≃RΦ(F)` and writes “si Γ transforme injectifs en injectifs”, followed by unfinished expressions. The revised note removes “the missing step is exactly” and reports preservation of injectives as the explicit check on the page without claiming that it exhausts all justification needed.

13. **R058 — applied: restore the domain in the definition of `N`.** Scan074:50 writes `N={F∈\underline M^{\unsure{\flat|b}} \mid a⊗_kF∈M}`. The revised note preserves the ambient domain and its unresolved completion sign.

14. **R059 and R082 — applied: separate the frozen binomial fragment from the clean PS expression.** Scan074:92 reads exactly `n!\,\unsure{P_n(t)}=t(t-1)\ \inserted{P}\,(t-n+1)`, while PS VI §119 explicitly gives `P_n(t)=t(t-1)\dots(t-n+1)/n!` at `ps6.tex`:2962; the clean product can be quoted as PS text. R059 now retains the frozen uncertainty and insertion, and R082 explicitly takes the PS choice `P(t)=t(t−1)/2` for its calculation instead of attributing an explicit handwritten assignment of that function to scan074.

15. **R068 — applied: retain the uncertain Hom subscript in the box.** Scan079:22 writes `j_!x=\operatorname{Hom}_{\unsure{M^\flat|M}}(x,1_M)^\vee`. The revised note keeps that uncertainty together with the source’s finite-projectivity qualification at24–26.

16. **R072 — applied: remove the unsupported withdrawal status and name the two displayed domains.** Scan084:30–43 retains the upper candidate `β:λ_!J→\underline{δ^1}` and computes both `βλ_!(δ_i)` as `δ_0α`; scan084:58–65 then writes `β:J→λ^{\unsure{*|\prime}}(\underline{δ^1})` and asks for `βδ_i=δ_iα`. The revised note states those domains and formulas and no longer calls the uncancelled upper candidate withdrawn.

17. **R077 — applied: specify the tensor permutation used in the explicit example.** Scan077:71–83 writes the unit and both adjunction counits with their tensor orders; the revised note supplies `τ:X⊗X^∨→X^∨⊗X,\ v⊗f↦f⊗v` before giving coordinates. This makes the transport of `η_ℚ(1)=Σe_i⊗e_i^*` and both evaluation maps explicit; the image, cokernel, and kernel calculations require no numerical correction.

## Exact primary-source spans supporting the comparisons

The spans below are read locations in the supplied TeX, with manuscript/printed pagination kept separate. They establish witness locations, not a calendar ordering of undated authorial layers.

| Comparison | Supplied source and exact lines | Source location and relevant text |
|---|---|---|
| Scan074 splitting equation | `ps_chapters_VI_VII/ps6.tex`:2930–2949 | VI §119, p.501: truncated power series, `a↦1+at+P(a)t²`, `P(a+a′)=P(a)+P(a′)+aa′`, and `P(t)=t(t−1)/2+ct`. |
| Scan074 binomial operations and comparison | `ps6.tex`:2955–2980, 3000–3017 | VI §119, pp.502–503: the clean `P_n` product, binomial algebras, and the question about `Symbin_ℤ(L_*^∨)→Maps(L_*,ℤ)`; §120’s analyzer discussion is3129–3223, pp.506–507. |
| The absolute homology adjunction | `ps6.tex`:3241–3313 | VI §121, pp.508–509: (2′) free-abelian/forgetful origin, (3) `LH_•⊣K_π`, and (5) `LH_•K_π(L)→L`, followed by “which is definitely false!” for general invertibility; this is the exact displayed morphism to compare before transferring a verdict to the manuscript’s `λ` counit. |
| The coefficient adjunction and localized question | `ps7.tex`:133–181, 187–217 | VII §134, pp.557–559: `p_!^{ab}⊣p^*`, derived homology and the integrator; (7) is the localization square and (8) the suspected localized equivalence. |
| Category-of-elements/relative homology | `ps7.tex`:325–488 | VII §135, pp.561–564: functorial homology and `LH(A/X,ℤ)≃LH(A,ℤ^(X))`, including the direct-sum computation. |
| Projective restriction and the retracted shortcut | `ps7.tex`:1340–1541, 1590–1714 | VII §§138–139, pp.583–590: localization/colocalization, finite-projectivity restriction at p.586, the cone example and “big blunder” at p.589, then return to resolutions. |
| First explicit strong W(7 bis) located | `companion/chunks/DER_XIIb-a.tex`:700–760 | XII §V.2.1, ms.75–76, printed p.55: “Axiome du carré cocartésien” and both biconditionals for the cover square. |
| First explicit strong W(7) cube located | `DER_XIIb-a.tex`:764–807 | XII §V.2.1, ms.76–77, printed p.56: “Axiome du cube”, “deux parmi ces conditions impliquent la troisième”. |
| Claimed W∞ application | `DER_XIIb-a.tex`:824–842 | Proposition6 and Théorème2, ms.78, printed p.57; the theorem is followed by “Je n’ai pas écrit la vérification en forme”. Commentary begins at845 and is a separate supplied-context claim. |
| First filteredness question located | `companion/chunks/DER_II-a.tex`:1280–1320 | II §2, ms.36, printed p.21: Corollaires2.17–2.18 and “cela implique-t-il que X soit filtrante ?”. |
| Corrective layer and renewed conjecture | `DER_II-a.tex`:1344–1416 | II ms.36–36ter, printed pp.22–23: Proposition2.19 with “Faux”, Contrexemple2.20, and the renewed `X totalement W∞-asphérique ⇒ X filtrante` conjecture at1412–1416. |
| Totality definition and comparison morphism | `DER_XIIb-a.tex`:1184–1238 | XII §V.2.3, ms.88–91, printed pp.63–64: the all-target `U′/p_!H` test and `f/F:V/F→V′/f_!F`. |
| Layered final-object/filtered examples | `DER_XIIb-a.tex`:1540–1630, 1920–1933; `companion/chunks/DER_XIIapp.tex`:303–325 | XII ms.98–101 and109; appendix ms.5, printed p.4. The successive conjectural/corrective notes are witnesses whose composition order is not fixed by chapter or printer dates. |

## Parallel corrections in this reader’s comparison draft

The same source-fidelity corrections have been applied to `research_ps_comparison_draft.md` items2,3,4,6,10,12,15,18,28,42: uncertain letters and exponents, unheaded connectors, the restricted tensor quantifier, actual adjunction comparisons, attribution of the written proof, and the scan074/PS product distinction. Items15 and42 now retain `\unsure{\widetilde W_h^P(I)}` rather than identifying it with `J`; item3 retains the unheaded top connector on scan045; item18 retains `C^{\unsure{n+1}}`. The coverage manifest’s draft SHA-256 is `b25212d1077e7622abf522404c719ad2faf399a220d23eb26563d27837096d14`; the frozen combined transcription remains `3f85b51570feeb779ae2fd3d9e338ea8f90078fbce6e6e406722a402d6bc8c79`.
