# Post-freeze literature and scope memo

Prepared by the literature research agent after the root reader froze all 48 page files and the combined transcription. No manuscript image was opened by this agent, no OCR was performed, and no frozen text or inventory was modified. Manuscript quotations below come from the frozen transcription, including its unresolved readings; all suggestions belong to research notes only.

The supplied `context/README.md`, `context/notes/RESULTS_STATE.md`, and the relevant complete items in `context/same_cote_33/MPL_33_098-146_notes.md` were read. Earlier notes are first-pass leads, and their inclusion in the register does not make them reviewed results. No connection establishing or refuting LM7 E.23, LM4 D.12, LM4 F.7, LM7_PUSH C.6, or the intake entry is demonstrated by these pages; the applicable registered anchors are the same-cote note IDs and the README's S19 draft-to-print comparison.

## Primary sources actually inspected

| Key | Source and exact locator | Verified comparison, stated briefly | Tool reference available to parent |
|---|---|---|---|
| A11 | [Artin, SGA 4 XI](https://www.normalesup.org/~forgogozo/SGA4/11/11.pdf), 4.3–4.4, especially printed pp. 73–75 | The equivalence explicitly concerns finite locally constant torsion sheaves; it is not an equivalence with every analytically constructible sheaf. | `turn11view0`, `turn12view2`, `turn16view0` |
| A15 | [Artin, SGA 4 XV](https://www.normalesup.org/~forgogozo/SGA4/15/15.pdf), 2.1–2.2, printed p. 192 | Smooth local acyclicity and affine-space acyclicity for torsion prime to the residual characteristics. | `turn31view0`, `turn33view0`, `turn46view5` |
| A16 | [Artin, SGA 4 XVI](https://www.normalesup.org/~forgogozo/SGA4/16/16.pdf), 2.1, printed pp. 213–214; 3.7–3.10; 4.1 | Proper locally acyclic specialization; relative purity; comparison assumes properness or constructibility. | `turn2view1`, `turn4view1`, `turn12view3`, `turn48view2` |
| D18 | [Deligne, SGA 4 XVIII](https://www.normalesup.org/~forgogozo/SGA4/18/18.pdf), 1.1.3, 1.1.6, 1.1.9; 2.9–2.10.1; 3.2.5–3.2.6 | Kummer-normalized trace, functoriality/base change/composition, geometric-fiber qualification, and smooth duality. | `turn2view0`, `turn4view0`, `turn7view0`, `turn3view1`, `turn33view1` |
| R16 | [Riou, 2014, Exposé XVI](https://numdam.org/item/AST_2014__363-364__301_0.pdf), 2.1.1; 2.3.1–2.3.7; 2.5.12–2.5.13; 3.1.1 | Gysin class, excess/base-change and composition formulas, then Gabber's absolute purity for regular pairs with invertible coefficients. | `turn5view1`, `turn7view1`, `turn7view2`, `turn11view5`, `turn49view0`, `turn49view1` |
| S03Q5 | [Stacks, Tag 03Q5](https://stacks.math.columbia.edu/tag/03Q5), Lemma 59.51.4 | Étale cohomology commutes with filtered colimits on a quasi-compact quasi-separated scheme. | `turn31view1` |
| S06YV | [Stacks, Tag 06YV](https://stacks.math.columbia.edu/tag/06YV), §21.18, Lemmas 21.18.1–4 | K-flat resolutions define pullback on the entire derived category of a ringed topos. | `turn5view2` |
| S095U | [Stacks, Tag 095U](https://stacks.math.columbia.edu/tag/095U), Lemma 59.92.2 | A proper morphism with fibers of dimension at most d has torsion cohomological dimension at most 2d. | `turn21view3` |
| S0F0C | [Stacks, Tag 0F0C](https://stacks.math.columbia.edu/tag/0F0C), Lemma 59.92.3 | Proper base change holds for unbounded complexes of Z/n-modules. | `turn21view2` |
| S0G28 | [Stacks, Tag 0G28](https://stacks.math.columbia.edu/tag/0G28), §63.10, Lemmas 63.10.1–2 | For finite-type separated maps of qcqs schemes, derived lower shriek has a uniform cohomological bound; for a torsion ring it is defined on all D. | `turn21view1` |
| S0F7A | [Stacks, Tag 0F7A](https://stacks.math.columbia.edu/tag/0F7A), §63.8 | Compactification comparison distinguishes bounded-below torsion cohomology from arbitrary complexes over a torsion ring. | `turn21view0` |

The SGA texts inspected here are mathematician-maintained retypesettings dated July 30, 2024, not an asserted facsimile collation. Riou's Numdam file is the published article. Search also identified Fujiwara's 2002 article, DOI `10.2969/aspm/03610153`, but the full article was not retrieved; its theorem should therefore be cited through the verified Riou proof unless a further primary inspection is made. The independent source statements above are deliberately brief; most detailed calculations below are our own scope tests rather than paraphrases of an external argument.

**Trace and duality scope.** D18,2.9 (pp.553–555) treats compactifiable f with an open flat finitely presented part of fiber dimension≤d and complement of fiber dimension<d; coefficients are prime-to-characteristic torsion. Normalizations use finite locally free degree and the affine-line trace, alongside coefficient functoriality, base change and composition. Thus the draft's P¹ formulation requires comparison, not verbatim identification. D18,3.2.5 (pp.585–586) gives the all-D adjunction Rf_! ⊣ f*(d)[2d] for smooth compactifiable f over qcqs S and a coefficient-ring sheaf killed by an invertible n; d may be locally constant. Inspected text references: `turn51view1`, `turn52view0`.

## Proposed research items

### L01. The nonproper comparison needs its coefficient scope

**File/scan:** 33:006, comparison paragraph and GAGA margin. **Kind:** reading question / unproved claim. **Quote:** “pour ∀ F faisceau de torsion”; “de type fini”.

The frozen paragraph states the comparison for arbitrary torsion F while deleting properness in favor of finite type, so the coefficient scope must be checked independently of the cancellation. The precise comparator A16, 4.1, assumes either a proper morphism or a constructible coefficient sheaf; A11, 4.4, separately supplies the finite locally constant categorical statement. This adds a scope question to S19 and differs from the neighboring package's tensor/projection issue at `same_cote_33/MPL_33_098-146_notes.md`, N18–N19, scans112 and120; those leads do not settle this analytic comparison.

### L02. An explicit degree-zero failure for arbitrary torsion

**File/scan:** 33:006, same paragraph. **Kind:** own idea. **Confidence:** high for the calculation; it tests the unrestricted reading, not the intended unstated conventions.

Take X=A¹_C, A=Z/n for n>1, and the algebraic étale sheaf F=⊕_{m∈Z}i_{m*}A supported at the integer points: by S03Q5, H⁰_et(X,F)=⊕_{m∈Z}A. Analytification preserves the direct sum, but the integer points form a closed discrete subset of C, so every family of point values gives an analytic section locally, and H⁰(C,F^an)=∏_{m∈Z}A. The comparison is therefore the non-surjective inclusion of the direct sum into the product. Searches for the same support construction find no counterpart in the supplied context; it adds a distinct nonproper obstruction beside the already recorded boundary-stalk test in N18, scan120, without re-proving that test.

### L03. Analytic constructibility is not automatically algebraic constructibility

**File/scan:** 33:006, GAGA margin. **Kind:** own idea. **Confidence:** high for the support obstruction; the historical meaning of “constructible analytique” remains to be identified.

For the closed analytic subset Z={m:m∈Z}⊂C, i_*A has finite stalks and is locally constant on Z and C\Z, but its support is neither finite nor cofinite and hence is not an algebraically constructible subset of A¹_C. Thus an unrestricted analytically constructible category is larger than the algebraic one, even when one permits the two analytic strata Z and C\Z; if a convention requires connected strata, the corresponding locally finite point stratification gives the same local obstruction. The source's intended analytical category needs an algebraic-stratification or another scope condition, and A11, 4.4, is a secure narrower comparator. Context searches find no exact analytic constructibility claim; this adds to S19 and is separate from N42's reused operator-algebra sheet, scan099.

### L04. Relative purity and the explicitly named absolute problem

**File/scans:** 33:012–014 and026. **Kind:** self-flagged / unproved claim. **Quote:** “Pb sans hypothèse de lissité remplacée par hyp. de régularité”.

The source distinguishes the smooth-pair statement from the regular-pair problem and invokes resolution in characteristic zero, so these should not be collapsed into one already proved theorem. A16, 3.7–3.10, is the closest historical comparator, while R16, 3.1.1, supplies the later absolute-purity theorem for regular pairs with invertible n. The context contains no occurrence of “pureté,” “Kummer,” or “fondamentale” in the same-cote notes, so this is new manuscript evidence for S19 rather than a restatement of an established register result; N20–N21, scan122, provide only a neighboring resolution/duality program.

### L05. Independence of local equations is an actual proof obligation

**File/scans:** 33:022–024. **Kind:** unproved claim. **Quote:** “on prouve que cette section ne dépend pas du choix des Y_i”.

The divisor construction passes through the quotient by units before the Kummer boundary, and the higher-codimension definition then requires independence of the regular sequence and its local factorizations. R16, 2.1.1 and2.3.1–2.3.7, gives a comparison route through Gysin classes; it should not be used to erase the draft's distinction between local and global classes. No same-point argument appears in the supplied context: this adds the geometric orientation step underlying, but different from, N29's categorical trace on scans134–136.

### L06. “Admissible” base change excludes excess intersection

**File/scans:** 33:024–026. **Kind:** unpursued implication. **Quote:** “φ′ reste section régulière”; “sans dim. excédentaire”.

The displayed product law is explicitly conditioned by expected codimension, and the base-change qualification preserves the regular immersion; neither clause licenses arbitrary pullback of a naive cycle class. The comparison target is R16, 2.3.2, where a genuine excess term occurs when codimension drops. Searches for “excess,” “intersection,” and “base change” find no matching geometric class calculation in the supplied neighboring notes; this adds a distinct qualification beside N04's nonflat *derived pullback* on scans104–106, and does not contradict it.

### L07. Compatible classes are not yet an unrestricted adic passage

**File/scan:** 33:026. **Kind:** unpursued implication. **Quote:** “La ‘bonne’ classe se trouve dans … Z_ℓ(d)”.

The coefficient-compatibility assertion organizes the finite classes into a prospective ℓ-adic orientation, but a statement inside an inverse-limit formalism must specify what Z_ℓ(d) and cohomology mean there. This adds an explicit compatible geometric class to `MPL_33_098-146 N40`, scans128,132,146, and the expectation in N24, scan128, without asserting that their trace-limit problem has been solved. The finite-level tests in the earlier notes should be cited rather than re-derived, and neither register row is a reviewed theorem of adic passage.

### L08. Characterization of the smooth trace is a theorem to prove

**File/scans:** 33:032–034. **Kind:** unproved claim. **Quote:** “Ces conditions caractérisent les hom Tr_f”.

The source proposes existence and uniqueness from base change, composition, isomorphism normalization and the Kummer normalization on P¹, followed by coefficient compatibility. D18, 2.9, is a precise comparison destination with an explicitly formulated family of trace maps and normalization conditions. This differs from `MPL_33_098-146 N29`, scans134–136: the current trace integrates a geometric morphism, whereas that later lead concerns the categorical trace of an endomorphism; the two constructions should be linked by duality rather than identified by their shared name.

### L09. Connected ordinary fibers do not suffice for a trace isomorphism

**File/scan:** 33:034(v). **Kind:** own idea / reading question. **Quote:** “à fibres conn. non vides”. **Confidence:** high for the test; conditional on “conn.” meaning ordinary rather than geometric connectedness.

For f:Spec C→Spec R and A=Z/3, the sole ordinary fiber is connected and nonempty, yet after geometric base change f becomes two points and the trace is A²→A, (a,b)↦a+b, which is not an isomorphism. Thus the literal unqualified condition requires geometric connectedness, or an equivalent convention; D18, 2.10.1, provides the geometric-fiber comparison. The context has no same-point assertion or example, so this adds a geometric qualification to S19 and does not refute N29 or N37's separate perfect-complex traces.

### L10. Derived categories organize the local-to-global orientation compatibility

**File/scan:** 33:036. **Kind:** unpursued implication. **Quote:** “S'exprime plus aisément quand on dispose de la catégorie dérivée”.

The patched diagram asks for compatibility of local purity with global trace, rather than merely two isolated isomorphisms of cohomology sheaves. Its comparison with R16, 2.3.3 and2.5.12, should track composition and twists before evaluating cohomology. This adds a geometric reason for the derived formalism to `MPL_33_098-146 N01`, scan098, and N29/N37, scans134–136/146: those first-pass notes concern the ensuing exchange and contraction mechanisms, not a proof of this particular patched diagram.

### L11. Exact flat pullback makes injective resolutions harmless

**File/scan:** 33:038. **Kind:** unpursued implication. **Quote:** “morphisme plat de topos annelés”; “résolutions injectives”; “résolutions plates”.

The first injective-resolution sentence belongs to the flat case, in which f* is already exact, so its wording is not by itself a mathematical error. The following nonflat discussion correctly changes to flat resolutions and distinguishes D⁻ from preservation of D⁺/Dᵇ under finite Tor dimension; S06YV supplies the modern all-D K-flat framework, which is broader than the draft's bounded construction. This restates the distinction later expanded in N02–N06, scans100–106, and adds an antecedent to registered `MPL_33_098-146 N08`, scans108/112, without re-deriving its finite-ring example.

### L12. Quasi-compactness supplies a uniform bound

**File/scan:** 33:042. **Kind:** unpursued implication. **Quote:** cancelled “f est à fibres de dim bornée”; inserted “Y est quasi compact”.

The amendment supplies a route to a global bound for compactifiable finite-type geometry, rather than declaring that quasi-compactness alone makes every direct-image functor finite-dimensional. S095U and S0G28 separate the geometric fiber bound from preservation of the standard bounded subcategories. This adds an earlier geometric instance to `MPL_33_098-146 N09`, scan110, and N31–N32, scans138–142; it differs from the later merely-noetherian expectation, which remains broader than the hypotheses checked here.

### L13. A geometric test for the deleted uniformity hypothesis

**File/scan:** 33:042. **Kind:** own idea. **Confidence:** high, because every component is an explicit projective space.

Let Y=⊔_{r≥0}Spec k, X=⊔_{r≥0}P^r_k over an algebraically closed field, f:X→Y the componentwise proper map, and A=Z/n with n invertible in k. The degree-zero sheaf A_X is bounded, but R^{2r}f_*A has a nonzero stalk on the r-th component, so Rf_!A=Rf_*A has no uniform upper cohomological bound. This tests the need for a global bound when preserving D⁻ or Dᵇ, without obstructing existence on D. It adds a geometric direct-image example to N31's pointwise-versus-uniform Tor example on scans138–140, instead of re-deriving that prior example.

### L14. Proper base change extends beyond the displayed D⁺ range

**File/scan:** 33:044. **Kind:** unpursued implication. **Quote:** “Lorsque f est propre ce est un Isom”.

The text derives its D⁺ comparison from cohomology-sheaf base change, while the constant Z/n coefficient ring makes inverse image exact in the stated étale setting. S0F0C verifies the corresponding unbounded proper-base-change theorem, so the all-D extension has a precise modern comparison separate from any proposal about ordinary nonproper direct image. This adds to the general mechanism discussed in N04/N07, scans104–106, and differs from N18's nonproper projection counterexample on scan120; no result-register status is changed.

### L15. Finite-ring duality does not require free cohomology modules

**File/scans:** 33:046–048. **Kind:** unpursued implication. **Quote:** “Si F loc. ct.”; “H^i_!(X,F)^∨”.

The title-only scan046 contributes no missing theorem statement, while scan048 records its cohomological consequence over a separably closed field and a relative local-constancy variant. D18, 3.2.5–3.2.6, explains why A=Z/n permits exact A-duality even for finite locally constant A-modules that are not free: A is injective as a module over itself. This is compatible with `MPL_33_098-146 N08`, N23 and N25, scans108/112,126 and126–132, because failure of projectivity or finite Tor dimension does not imply failure of exact duality into this particular ring. It adds a distinction between duality and endomorphism trace, not a new claim that every finite module is perfect.

### L16. A boundary test for the partial-range sentence

**File/scan:** 33:048, final sentence. **Kind:** own idea / reading question. **Quote:** “pour i≤i_0”; “pour j≥2d−i_0”. **Confidence:** high for the calculation; the antecedent of “la conclusion” is genuinely undecided and may mean only constructibility.

Set S=A¹_C, X=A²_C\{(0,0)}, f(x,t)=t, and F=A=Z/n with n>1: f is smooth compactifiable of relative dimension1, and every geometric fiber is A¹ or G_m, so R^if_!A=0 for i≤0. Writing p:A²→S and i_s:{0}→S, purity at the removed codimension-two point and affine-line invariance give the triangle i_{s*}A(−2)[−4]→A_S→Rf_*A→, whence R³f_*A≅i_{s*}A(−2). That skyscraper is constructible but not locally constant, so the example excludes the stronger reading that the low-range assumption with i_0=0 forces the preceding local-constancy or degreewise-duality conclusion in every j≥2; it does **not** refute the immediately preceding, and quite plausible, constructibility conclusion. This adds a scoped test beside N19, scans112/120, and N09, scan110, whose first-pass leads already distinguish derived claims from stronger bounded or locally constant variants; sources A15,2.2 and A16,3.7 provide the two inputs.

### L17. Local constancy does not imply fixed-coefficient freeness

**File/scan:** 33:010, specialization theorem. **Kind:** own idea / reading question. **Quote:** “F faisceau de torsion loc. libre”; “sont loc. libres”. **Confidence:** high for the explicit invariants calculation; conditional on interpreting “libre” as freeness over a fixed coefficient ring.

Let E be a complex elliptic curve with a connected étale double cover, let A=Z/4, and let F be the rank-one A local system whose monodromy factors through that cover and sends its nontrivial deck transformation to −1. Then H⁰(E,F)=A^{−1}=2A≅Z/2, which is not a free A-module, although it is a locally constant sheaf on Spec C. Thus the source's specialization statement is consistent with local constancy but its stronger fixed-ring freeness interpretation fails; a precise positive comparator is A16, Theorem2.1, combined with smooth local acyclicity A15, Theorem2.1. This adds a geometric example to registered first-pass lead `MPL_33_098-146 N25`, scans126–132, and differs from its already computed two-term perfect complex; the earlier result is cited, not re-derived.

**External-text caution:** in the inspected A16 retypesetting, Corollary2.2 does not visibly repeat local constancy among its coefficient hypotheses; Theorem2.1 does. The safe citation above uses Theorem2.1 and A15,2.1, without silently supplying a word to an externally printed corollary or treating that corollary's wording as authority for an impossible generality. Theorem2.1 assumes finite presentation, properness, the indicated degree of local acyclicity, and constructible locally constant coefficients; in the smooth case prime-to-characteristic coefficients give the needed acyclicity in every degree. This observation concerns the inspected retypesetting only: no original facsimile has been collated for that omission.

## Further details of the two main calculations

For L02, the direct-sum assertion is not merely a formal claim that all sections commute with sums: on the algebraic side it follows from the filtered system of finite subsums on qcqs A¹_C (S03Q5). On the analytic side, the inclusion of the closed discrete integer set has no accumulation point in C, so any assignment of values is locally a section of a finite subsum, and sheafification glues these assignments. This is exactly the failure of algebraic quasi-compactness to match analytic compactness. The analytically constructible sheaf in L03 is the analytification of the nonconstructible algebraic F in L02, but is not the analytification of an **algebraically constructible** sheaf; the statements are consistent.

For L16, factor f=p∘j, with j:A²\{0}→A² and i:{0}→A². The localization triangle is

\[
i_*Ri^!A\longrightarrow A_{\mathbf A^2}\longrightarrow Rj_*A\longrightarrow i_*Ri^!A[1].
\]

Purity gives Ri^!A=A(−2)[−4]; applying Rp_* and using Rp_*A=A_S gives the triangle in L16. The long exact sequence has H⁰(Rf_*A)=A_S and H³(Rf_*A)=i_{s*}A(−2), with no need to split the triangle. Compact-support base change computes R⁰f_!A on fibers as H⁰_c(A¹,A) or H⁰_c(G_m,A), both zero. After the Tate twist appearing on scan048, R³f_*(A(1)) is still a nonconstant constructible skyscraper; thus the twist does not change the scope test. Since the immediately preceding noun in the source is the uncertain insertion “constructiblt.|constructibilité,” the weaker conclusion remains compatible with this example and is not adjudicated here.

## APA bibliography for the verified sources

Artin, M. (1973a). Comparaison avec la cohomologie classique : Cas d'un schéma lisse. In M. Artin, A. Grothendieck, & J.-L. Verdier (Dirs.), *Théorie des topos et cohomologie étale des schémas: SGA 4, Tome 3* (Lecture Notes in Mathematics, Vol. 305, Exposé XI, pp. 64–78). Springer. Checked retypesetting: https://www.normalesup.org/~forgogozo/SGA4/11/11.pdf

Artin, M. (1973b). Morphismes acycliques. In M. Artin, A. Grothendieck, & J.-L. Verdier (Dirs.), *Théorie des topos et cohomologie étale des schémas: SGA 4, Tome 3* (Lecture Notes in Mathematics, Vol. 305, Exposé XV, pp. 168–205). Springer. Checked retypesetting: https://www.normalesup.org/~forgogozo/SGA4/15/15.pdf

Artin, M. (1973c). Théorème de changement de base par un morphisme lisse, et applications. In M. Artin, A. Grothendieck, & J.-L. Verdier (Dirs.), *Théorie des topos et cohomologie étale des schémas: SGA 4, Tome 3* (Lecture Notes in Mathematics, Vol. 305, Exposé XVI, pp. 206–249). Springer. Checked retypesetting: https://www.normalesup.org/~forgogozo/SGA4/16/16.pdf

Deligne, P. (1973). La formule de dualité globale. In M. Artin, A. Grothendieck, & J.-L. Verdier (Dirs.), *Théorie des topos et cohomologie étale des schémas: SGA 4, Tome 3* (Lecture Notes in Mathematics, Vol. 305, Exposé XVIII, pp. 481–587). Springer. https://doi.org/10.1007/BFb0070724. Checked retypesetting: https://www.normalesup.org/~forgogozo/SGA4/18/18.pdf

Riou, J. (2014). Classes de Chern, morphismes de Gysin, pureté absolue. In L. Illusie, Y. Laszlo, & F. Orgogozo (Eds.), *Travaux de Gabber sur l'uniformisation locale et la cohomologie étale des schémas quasi-excellents* (Astérisque, Nos. 363–364, Exposé XVI, pp. 301–349). Société mathématique de France. https://numdam.org/item/AST_2014__363-364__301_0/

The Stacks Project Authors. (n.d.). *The Stacks Project*. Retrieved November 15, 2026, from https://stacks.math.columbia.edu/. Stable individual locators are linked in the source table.

The original SGA volume/date/chapter page spans were verified against the [publisher's contents and bibliographic record](https://link.springer.com/book/10.1007/BFb0070714), tool reference `turn48view1`; the 2006 electronic publication date does not replace the 1973 original-volume date.

## Search record

The item-by-item searches below were performed after drafting, against all three supplied context files, using literal case-insensitive alternatives. Counts and excerpts are retrieval evidence, not claims that every matching occurrence is a mathematical match; each item's prose above states the substantive relationship and exact neighboring scans.

| Item | Literal terms searched | README matches | RESULTS_STATE matches | Same-cote matches and first relevant note headings |
|---|---|---:|---:|---|
| L01 | `comparison`, `analytic`, `locally constant`, `nonproper` | 0 | 4 | 46; N02. Flat resolutions and the quotient by quasi-isomorphisms; N03. The explicit question about general topoi; N04. Nonflat base change is a later extension; N07. Internal-Hom compatibility and its local verification; N10. A point already exhibits infinite Tor; N11. Compact-support projection and the literal formulas |
| L02 | `direct sum`, `analytic`, `boundary`, `support` | 0 | 0 | 21; N01. Exchange identities as a duality programme; N07. Internal-Hom compatibility and its local verification; N11. Compact-support projection and the literal formulas; N12. Functoriality is expressly left to verify; N13. Künneth is reduced to two projection steps; N14. One proper factor and the characteristic restriction |
| L03 | `constructible`, `analytic`, `stratification` | 0 | 0 | 1; N42. The analytic operator-algebra sheet is a separate source |
| L04 | `pureté`, `purity`, `resolution`, `résolution`, `dualité locale` | 0 | 4 | 15; N02. Flat resolutions and the quotient by quasi-isomorphisms; N03. The explicit question about general topoi; N04. Nonflat base change is a later extension; N06. The injective proof is corrected on the same sheet; N08. Finite coefficient rings force attention to unbounded resolutions; N10. A point already exhibits infinite Tor |
| L05 | `Kummer`, `fondamentale`, `fundamental class`, `local equations` | 0 | 0 | 0;  |
| L06 | `excess`, `intersection`, `base change`, `nonflat` | 0 | 0 | 6; N04. Nonflat base change is a later extension; N07. Internal-Hom compatibility and its local verification; N12. Functoriality is expressly left to verify; N14. One proper factor and the characteristic restriction; N26. The unnamed perfectness criterion; N56. Two bibliographical leads remain unverified identities |
| L07 | `adic`, `coefficient reduction`, `passage à la limite`, `compatible` | 0 | 1 | 10; N23. Why reduction to a finite field is rejected; N24. The finite-level-to-adic passage is an expectation; N28. Mapping-cylinder additivity must not be enlarged indiscriminately; N40. A controlled finite-level compatibility test; N55. The axiomatic étale-topos source is incomplete here; N56. Two bibliographical leads remain unverified identities |
| L08 | `trace`, `normalisation`, `normalization`, `contraction` | 0 | 3 | 40; N08. Finite coefficient rings force attention to unbounded resolutions; N20. Curves, singular coefficients and rationality of L-functions; N22. Fixed points require local multiplicities; N23. Why reduction to a finite field is rejected; N24. The finite-level-to-adic passage is an expectation; N25. A perfect complex with nonprojective cohomology |
| L09 | `connected`, `geometric fibres`, `geometric fibers`, `trace` | 0 | 3 | 37; N08. Finite coefficient rings force attention to unbounded resolutions; N12. Functoriality is expressly left to verify; N18. The support obstruction to ordinary direct-image projection; N20. Curves, singular coefficients and rationality of L-functions; N22. Fixed points require local multiplicities; N23. Why reduction to a finite field is rejected |
| L10 | `local trace`, `duality`, `exchange`, `composition` | 0 | 4 | 19; N01. Exchange identities as a duality programme; N04. Nonflat base change is a later extension; N15. The nonproper prime-to-characteristic expectation; N29. Duality gives the intrinsic trace; N35. The global trace pairing needs a finite object; N37. The local trace and the symmetry sign |
| L11 | `flat resolutions`, `injective`, `Tor dimension`, `unbounded` | 0 | 2 | 17; N02. Flat resolutions and the quotient by quasi-isomorphisms; N03. The explicit question about general topoi; N04. Nonflat base change is a later extension; N05. Bounds behind global hyper-Tor; N06. The injective proof is corrected on the same sheet; N08. Finite coefficient rings force attention to unbounded resolutions |
| L12 | `cohomological dimension`, `uniform`, `quasi-compact`, `noetherian` | 0 | 0 | 10; N09. The noetherian expectation for relative direct image; N31. Uniform Tor bounds versus pointwise finite bounds; N49. Normalization does not need to be finite as a module; N56. Two bibliographical leads remain unverified identities |
| L13 | `disjoint union`, `uniform`, `amplitude`, `direct image` | 0 | 1 | 10; N01. Exchange identities as a duality programme; N09. The noetherian expectation for relative direct image; N26. The unnamed perfectness criterion; N31. Uniform Tor bounds versus pointwise finite bounds; N32. The compact-support amplitude estimate; N56. Two bibliographical leads remain unverified identities |
| L14 | `base change`, `D^+`, `nonproper`, `pullback` | 0 | 3 | 16; N01. Exchange identities as a duality programme; N03. The explicit question about general topoi; N04. Nonflat base change is a later extension; N07. Internal-Hom compatibility and its local verification; N11. Compact-support projection and the literal formulas; N12. Functoriality is expressly left to verify |
| L15 | `finite coefficient`, `nonprojective`, `duality`, `injective` | 0 | 4 | 16; N01. Exchange identities as a duality programme; N06. The injective proof is corrected on the same sheet; N08. Finite coefficient rings force attention to unbounded resolutions; N15. The nonproper prime-to-characteristic expectation; N25. A perfect complex with nonprojective cohomology; N29. Duality gives the intrinsic trace |
| L16 | `locally constant`, `constructib`, `cohomological dimension`, `projection` | 0 | 1 | 20; N07. Internal-Hom compatibility and its local verification; N09. The noetherian expectation for relative direct image; N10. A point already exhibits infinite Tor; N11. Compact-support projection and the literal formulas; N13. Künneth is reduced to two projection steps; N14. One proper factor and the characteristic restriction |
| L17 | `locally free`, `localement libre`, `nonprojective`, `locally constant` | 0 | 1 | 6; N10. A point already exhibits infinite Tor; N19. The locally constant variant needs its actual scope; N25. A perfect complex with nonprojective cohomology; bibliographic Tag02M9 row |
