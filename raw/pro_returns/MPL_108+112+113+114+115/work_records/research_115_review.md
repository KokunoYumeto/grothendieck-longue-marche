# Independent focused review of the cote 115 research notes

## Scope and outcome

Reviewed `research_115_page_notes.md` and `research_115_page_notes.json` against the frozen cote 115 TeX and the relevant supplied companion passages. The focused targets were 115-R02, R03, R06, R07, R11, R13, R17, R20–23, R29–41, and 115-C01–C06; the prose bodies and Markdown/JSON agreement were also checked across all 52 items. This was a review of mathematical typing, claim strength, elementary checks, and note format, with no new literature search, no image access, and no transcription changes.

**Outcome:** no further concrete mathematical defect was found after the C04 notation correction described below. Confidence in this focused review is high for the stated elementary calculations and category-theoretic constructions; it is not a claim that every associated historical interpretation or supplied research return has been independently proved.

## C04 correction

The first version of 115-C04 described incoming arrows as `A(-,x)` for `x∈B`, which is undefined when `x` is not an object of `A`. For a fully faithful functor `f:A→B`, the correctly typed components are

\[
P_x(a)=B(fa,x),\qquad Q_x(b)=B(x,fb),
\]

with composition landing in `B(fa,fb)` and then identified with `A(a,b)` by full faithfulness. The current note has been corrected to `B(-,x)|_A` and `B(x,-)|_A`, which is coherent with the customary identification of `A` with its fully faithful image. This is a correction to research prose only; the distinct frozen H^x variance conflict remains recorded in R28.

## Mathematical checks

| Items | Result and reason |
|---|---|
| R02–R03 | Confirmed the `[1]` counterexamples. For the stated Hom-kernel reading, the chosen left side is a singleton and right side empty; the questioned ordinary adjunction reverses the required Hom arguments. The notes retain the correct qualification about unsettled notation. |
| R06–R07 | Confirmed the separately continuous/cocontinuous conventions and the relative internal-Hom targets. The projection names are interpreted as forgetting the indicated factor, in agreement with the frozen diagram. |
| R11 | Confirmed the terminal-object preservation obstruction. At `S=∅`, the proposed product-category representable takes value `Hom(T,M)`, which need not be a singleton; hence it need not be separately continuous. |
| R13 | Confirmed the unrestricted exponent claim fails already in Set: with two-element L and M, `L^M` has four elements whereas L has two. |
| R17 | The uniqueness comparison is the ordinary density/free-completion argument, with preservation read in the indicated opposite categories and separately for the bifunctor. No derived assertion is inferred. |
| R20 | Confirmed the discrete-two-object example: the initial presheaf is reflexive but is neither representable nor a retract of a represented presheaf. |
| R21 | Confirmed the unit `2→1` for `A=e` changes connected components and therefore fails the expressly stated ordinary W∞ test. |
| R22 | Confirmed `y₀→y₁` is a weak equivalence between contractible element categories, while its conjugate has component `∅→1` at 0 and is not an isomorphism. |
| R23 | Confirmed the contraction coend, its evaluation formulas, and the reversal `A(b,a)` on represented inputs relative to the Hom-kernel pairing. |
| R29–R30 | The triple morphism directions and compatibility equation define a category: identity and composition satisfy compatibility by substitution. The frozen prime/subscript notation conflict remains appropriately distinguished from the coherent abstract definition. |
| R31–R32 | Composition in B defines the comparison functor under the correctly typed two-sided Hom interpretation. Swapping P,Q and transposing the pairing gives the stated equivalence with the opposite envelope over the opposite base. |
| R33–R34 | Full faithfulness of the incoming restricted Yoneda functor supplies the stated sufficient density condition: compatible outgoing components are forced by testing all incoming maps. In the presheaf special case, representables detect the required equality, proving fullness of the graph embedding. |
| R35 | The intersection of the two graph images involves reflexive/conjugate pairs; it is correctly distinguished from the different intersection drawn in the ordinary functor-category ambient on scan014. |
| R36 | Both left Kan extensions have the correct variance, and the displayed pairing is well typed and respects the coend relations. Its composite is `b→fa→fa′→b′`; the warning that graph embeddings need not both commute with this extension is appropriate. |
| R37–R38 | Confirmed the small-projective/retract argument giving Kar(A) for the cocontinuous/representable intersection. The notes correctly avoid identifying that intersection with the larger reflexive locus of the triple-envelope. |
| R39 | Confirmed the `[1]` example distinguishes an ordinary categorical pushout of the two singleton pieces from their full ambient union. The source's gluing sketch is not overpromoted to a universal property. |
| R40–R41 | The ordinary free-cocompletion statement includes the needed cocompleteness hypothesis. The unrestricted additive-to-Set assertion fails because a cocontinuous `Ab→Set` must send 0 to the empty set, and every arrow `X→0` then forces its value at X to be empty. |
| C01–C03 | The unavailable exact STRATA C.1 statement remains explicitly unavailable. The substitution `A=U`, `B=Tᵒᵖ` correctly matches `Aᵒᵖ×Bᵒᵖ` with `Uᵒᵖ×T`, and the collage construction retains precisely the required internal and crossing morphisms. |
| C04 | The corrected incoming and outgoing Hom expressions are well typed; the distinction between a paired-object envelope and a single crossing bimodule is mathematically sound. |
| C05 | Checked against the companion: E is the ordinary crossing-arrow category with commuting-square morphisms. Precomposition gives the split fibration to U, postcomposition the split opfibration to T, and the crossing arrows supply the natural transformation. |
| C06 | Confirmed the Set example `G↦G×S ⊣ F↦F^S` and its empty/singleton special cases. Its status as a bounded ordinary comparison rather than an identification of unavailable STRATA C.1 is appropriate. |

## Format and synchronization

At the time of the review, R01 had two body sentences and each of the other 51 bodies had three. Frozen anchors, source metadata, and the C02 comparison table were treated as metadata/support rather than additional prose-body sentences. All 46 R-note bodies and all six C-note content strings in the JSON occurred exactly in the Markdown; no mismatch was found.

## Confidence-label recommendation

R29, R31, and R32 supply independent elementary checks but had `confidence: null` and no explicit confidence word. Their reasons already occur in the prose; the following labels make the own-check convention explicit without changing the mathematics:

- **R29:** High: identity and composition satisfy compatibility by substitution.
- **R31:** High under the coherently typed Hom interpretation: composition defines the pairing and both component maps.
- **R32:** High: swapping components and transposing the pairing gives inverse constructions.

R17 likewise lacked a confidence label, but presents standard density background rather than a new result. If a uniform label is desired: **High under the stated separate preservation and opposite-category conventions: restriction to representables determines the extension.** Root will make the confidence-field changes; this review did not modify the notes or any frozen TeX.
