# MPL 159: monodromy and moduli checks after the transcription freeze

Prepared 18 November 2026 by the `monodromy_checks` research agent, GPT-6 Astra Pro. This is a research report, not a transcription revision. The parent recorded the transcription freeze at 01:04:49 UTC. I read the frozen text of scans 015–023 and the authorized context afterward; I did not inspect manuscript images or edit any `.tex` file.

## Scope, attribution, and principal conclusions

The context used is Michel Hua's project's **modernised reading of cote 159**, especially “L'espace, et le critère de non-dégénérescence,” “Le calcul de dimension,” “L'anomalie de la page 15, et ce que la cohérence demande,” “Le tableau analytique : monodromie, Teichmüller, uniformisation,” and “Aucune réduction du groupe structural : la densité de la monodromie.” Its provenance and AI-produced status are stated in `context/hua_project/README.md`. The two findings-register claims checked are `159-monodromy-injectivity-question` and `159-no-reduction-monodromy-dense`, reproduced in `context/notes/RESULTS_STATE.md`, lines 467–469. Hua's page numbers are one less than the scan numbers used here. Nothing in this report claims mathematical novelty or historical priority.

| Check ID | Conclusion |
|---|---|
| MC01 | Hua's claim that the manuscript leaves fixed-X injectivity unanswered contradicts the frozen text: scan018 asserts a monomorphism and scan021 concludes its proof. |
| MC02 | For a fixed compact Riemann surface of genus at least two, unbranched projective-structure holonomy is injective; an independent pointwise proof is given below. The primary literature states the stronger proper holomorphic embedding theorem. |
| MC03 | Holonomy on all marked projective structures, allowing the complex structure to vary, is not globally injective. Grafting supplies examples. |
| MC04 | The relative dimension 6g−6 on scan016 is correct for the flat bundles defined on scan015. Hua's proposed 3g−3 correction confuses that moduli problem with the section/oper moduli introduced separately on scan018. |
| MC05 | Hua's V4 counterexample to “zero-dimensional automorphism group implies trivial automorphism group” is correct. Its centralizer calculation and realization on a genus≥2 curve are rechecked here. |
| MC06 | The canonical Fuchsian uniformization map is real analytic, not holomorphic. Thus “morphisme analytique” on scan018 needs an analytic-category qualification. |
| MC07 | The Fuchsian uniformization image is not complex-algebraically constructible, both in the Betti character variety and in fixed-X de Rham moduli. This follows from a short complex-analytic argument, without assuming Riemann–Hilbert is algebraic. |
| MC08 | “The invariant domain will be unique” is false without a choice of side/orientation: a cocompact torsion-free Fuchsian group preserves both halfplanes. |
| MC09 | Riemann–Hilbert is nonalgebraic in this PGL2 setting; a dimension argument from Dumas–Kent's theorem verifies the claim on the oper locus. |
| MC10 | The Out(π) action is algebraic on Betti moduli. Riemann–Hilbert nonalgebraicity alone does not prove that its transported action on de Rham moduli is nonalgebraic. That general action claim is not settled by this check. |
| MC11 | The degree argument excluding Borel reductions is valid in characteristic zero; the normalizer case follows after a finite étale cover. |
| MC12 | To infer Zariski density, finite subgroups must also be excluded. Hua identifies and repairs this issue correctly; the finite-cover completion is independently rechecked below. |
| MC13 | “Irreducible,” “Zariski dense,” and Kleinian “nonelementary” must not be used as synonymous predicates for arbitrary representations. |

## MC01–MC03. Fixed-X holonomy and the varying-X map

### What the manuscript actually says

Frozen scan018, lines 26–34, first introduces a separate space `M_conn(X)` of stratified projective-line bundles **with** a nonstationary marked section. It says that forgetting the section is an algebraic morphism, then states “En fait c'est un mono”; the margin says every stratified isomorphism preserves the marked section. Scan018, lines 36–40, begins the argument. Scan021, line 14, concludes that two different projective connections cannot give isomorphic stratified bundles, under the explicit invertibility-of-2 condition in that calculation. Line 16 separately concludes absence of stratified automorphisms for proper smooth genus≥2 fibers.

This directly contradicts **Hua, findings register, `159-monodromy-injectivity-question`**, and **Hua, modernised reading of cote 159, “Le tableau analytique…”**, lines 985–1008, which say the question is posed without an answer. The modern file's opening comments, lines 65–66, and concluding lines 1553–1554 repeat that mistaken assessment. The frozen spelling is `M_conn`, not the modern file's `M_ann`; no transcription change is proposed.

### Independent pointwise proof over C

Fix a compact Riemann surface X of genus g≥2 and an unbranched projective structure. Normalize the vector-bundle presentation of its projective bundle to the extension used in scans018–022,

\[
0\longrightarrow K_X\longrightarrow E\longrightarrow\mathcal O_X\longrightarrow0,
\qquad \det E=K_X.
\]

A second transverse section of P(E), in the quotient convention, is a surjection E→L. Its normal bundle is

\[
\operatorname{Hom}(\ker(E\to L),L)=K_X^{-1}\otimes L^2.
\]

Transversality to the horizontal foliation identifies this normal bundle with T_X=K_X^{-1}; hence deg L=0. Since deg(K_X^{-1}⊗L)=−(2g−2)<0, the composite K_X→E→L vanishes. The quotient factors through O_X→L, which is still surjective. A surjection of line bundles is an isomorphism, and the section is the original section. Consequently every flat-bundle isomorphism between two such objects preserves their oper sections. The two projective structures are isomorphic.

This proves injectivity on isomorphism classes for a fixed X without using the uncertain local coefficient readings on scan020. A horizontal projective automorphism preserving the section is also trivial over C: in a local flat trivialization it is a constant Möbius transformation fixing the developing map's open image. This rechecks the complex-point consequence of scan021(b).

**Limit:** this is not a proof of the full functorial scheme-monomorphism assertion over every nonreduced base, nor a complete audit of the local calculation on scans019–021. It also does not remove the genus assumption or cover branched projective structures.

### Primary literature and the distinction from global holonomy

[GKM, §11.4, Theorem 11.4.1](https://www.math.ucdavis.edu/~kapovich/EPR/GaKaMa.pdf), pp.688–689, gives fixed-X properness and an embedded image. Properness is imported from that primary theorem; the independent argument above proves pointwise injectivity.

For the varying-X space, [Baba–Gupta, §2.4](https://arxiv.org/pdf/1402.5445) supplies holonomy-preserving 2π-grafting. Grafting a nonempty simple closed geodesic of a uniformizing structure gives a distinct structure with the same holonomy; fixed-X injectivity then forces the marked conformal surface to change. Their stronger fiber-density theorem is not used.

Thus a reference concerning global holonomy fibers cannot be used to refute the manuscript's fixed-X assertion. Conversely, the manuscript's fixed-X assertion does not assert global injectivity.

## MC04. The dimension issue is a distinction of moduli problems

Frozen scan015, lines 7–14, specifies a curve, a projective-line bundle, and its flat/stratified structure. It does **not** include a marked transverse section. Scan018, line 26, introduces that extra section separately. This is enough to refute the identification of the two fibers made in **Hua, modernised reading, “L'anomalie de la page 15…”**, particularly lines 905–918.

For a fixed smooth proper connected X over C, let ad(P) be the rank-three adjoint local system. Killing-form duality gives h2=h0, and Euler characteristic gives

\[
h^1_{DR}(X,\mathrm{ad}P)=6g-6+2h^0_{DR}(X,\mathrm{ad}P).
\]

At h0=0 the relative deformation space is unobstructed and has dimension 6g−6. The formula is exactly scan016, lines 14–43; its last paragraph, line 47, explicitly calls 6g−6 the **relative** dimension over the moduli of curves. Adding the 3g−3 deformation parameters of X gives 9g−9 for the total flat-bundle moduli on this locus. These are local stack/deformation dimensions; a coarse space at nontrivial finite stabilizers requires separate care.

By contrast, unbranched projective structures on fixed X form an affine space/torsor under H0(X,K_X²), of dimension 3g−3. Their varying-X total space has dimension 6g−6. The two counts are therefore:

| Moduli problem | Fixed-X dimension | Total dimension over genus-g curves |
|---|---:|---:|
| Flat PGL2 bundle, with h0(ad)=0 | 6g−6 | 9g−9 |
| Flat PGL2 bundle with transverse oper section | 3g−3 | 6g−6 |

The underbrace at scan016, line 41, loosely calls H1 the tangent space to the total named moduli object. That label needs the qualification **relative to the curve**; it does not justify changing the explicitly stated relative dimension. The numerical correction proposed in Hua's subsection is therefore refuted for the moduli problem actually defined in the frozen text.

## MC05. Finite automorphisms: Hua's V4 correction survives checking

Credit: **Hua, modernised reading, “L'espace, et le critère de non-dégénérescence,”** lines 810–820, supplies this counterexample. The following is a recheck, not a new result.

In PGL2(C) let a(z)=−z and b(z)=1/z. They generate V4={1,a,b,ab}. A Möbius map commuting with a preserves its fixed-point pair {0,∞}, so it has the form cz or c/z. Commutation with b then requires c²=1. Therefore

\[
C_{\mathrm{PGL}_2}(V_4)=V_4.
\]

A closed surface group of any genus g≥2 surjects onto V4 through its abelianization modulo 2. The corresponding finite étale cover and its PGL2 representation give an algebraic flat projective bundle on a complex projective curve. Its flat automorphism group is V4, which has dimension zero but is nontrivial. Its monodromy cannot lie in Ga, whose characteristic-zero finite subgroups are trivial, or Gm, whose finite subgroups are cyclic.

Thus scan015(a) is stronger than (b) and (c), even for a smooth projective genus≥2 curve. Merely restricting X to such a curve does not repair the proposition: the extra **projective-structure/oper** hypothesis is essential to the later density argument. On the complex flat-bundle side, (b)⇔(c) follows because a positive-dimensional centralizer contains a one-parameter torus or unipotent group, and the centralizer of either in PGL2 is itself.

The locus defined on scan015 by excluding Ga/Gm reductions may consequently have finite stabilizers. It is not automatically a fine moduli space of objects without automorphisms. Scan017, lines 5–14, expressly restricts to trivial stabilizer, a genuinely smaller condition. This does not affect the 6g−6 relative dimension computation.

## MC06–MC08. Canonical uniformization: analytic category, constructibility, and the two domains

### Real analytic versus holomorphic

Frozen scan018, lines 12–24, calls the canonical uniformizing-representation map analytic and injective. The inputs from [McMullen, §2](https://people.math.harvard.edu/~ctm/papers/home/text/papers/kahler/kahler.pdf) are real analyticity, failure of holomorphicity, and total reality of the Fuchsian locus.

There is a direct check for the representation-valued map. Embed the Betti character variety in affine space using regular functions defined over R. Fuchsian characters have real coordinates. Were the canonical map holomorphic, every coordinate would be a real-valued holomorphic function and therefore locally constant. The map could not be injective on positive-dimensional Teichmüller space. Transport through the biholomorphic analytic Riemann–Hilbert correspondence does not change this obstruction.

Accordingly, the manuscript statement is valid with “real analytic” and standard orientation-preserving markings. If “analytique” means a complex-analytic morphism, it is false. A holomorphic Bers slice is a different construction requiring the choice of the other conformal boundary component; it must not silently replace canonical Fuchsian uniformization.

### Negative constructibility statement, proved in both structures

Frozen scan018, line 24, says it is suspected that the image is **not** constructible. Hua's modern subsection, lines 979–983, instead paraphrases a positive constructibility/algebraicity supposition. That is a disagreement with the frozen text, not a reason to alter that text.

Here the negative mathematical assertion can be checked directly. Suppose the infinite Fuchsian image were a complex-algebraically constructible set in either the Betti variety or fixed-X de Rham moduli. A constructible set in a finite-type complex variety is a finite union of locally closed algebraic sets. If infinite, one of these pieces has positive dimension and contains a positive-dimensional connected smooth complex analytic germ. In the Betti case, restrict real-coordinate regular functions to this germ. In the de Rham case, first compose the germ with analytic Riemann–Hilbert and then restrict the same coordinate functions. In either case these are real-valued holomorphic functions, hence constant. Since the affine coordinates separate points and Riemann–Hilbert is injective, the germ would be a point, a contradiction.

This argument uses complex analyticity, not algebraicity, of Riemann–Hilbert. It proves nonconstructibility in both algebraic structures. It does not rely on treating nonconstructibility as invariant under an arbitrary nonalgebraic bijection.

### Two invariant homogeneous domains

Choose a torsion-free cocompact Fuchsian group Γ⊂PSL2(R). Both H+ and H− are Γ-invariant homogeneous domains in P1(C), the action on each is free, and each quotient is compact. They are distinct. The quotients are conjugate Riemann surfaces; McMullen's same §2 explicitly describes both halfplanes and their quotients.

This is a direct counterexample to scan018's parenthetical “il sera unique” with no further qualification. A chosen orientation-compatible marking and side selects the uniformizing domain relevant to the marked surface. A bare outer isomorphism of fundamental groups, without preserving the oriented surface class, does not encode that choice. No claim is made here to classify every domain permitted by the manuscript's word “homogène.”

## MC09–MC10. Riemann–Hilbert nonalgebraicity is separate from the Out(π) action

Frozen scan017, line 16, tentatively says the Riemann–Hilbert isomorphism is not algebraic. This can be confirmed in the setting of genus≥2 curves and PGL2.

[Dumas–Kent, Theorem A and §5](https://arxiv.org/pdf/0807.4509) supplies Bers-slice Zariski density and containment in fixed-curve holonomy. The finite SL2-to-PGL2 quotient transfers density to the liftable component.

**Deduction checked here:** projective structures on fixed X form the algebraic affine space Q(X) of dimension 3g−3; the map forgetting the oper section to algebraic de Rham moduli is algebraic, as the manuscript states. If Riemann–Hilbert were algebraic there, its composite with this map would be an algebraic map from Q(X) with Zariski-dense image in a 6g−6-dimensional component. An algebraic image cannot have larger dimension than its source. Since g≥2, this is impossible. The oper monodromies have trivial centralizer, so restricting to the automorphism-free locus does not evade the contradiction. This is a deduction from Dumas–Kent's primary theorem, not a new literature theorem or a reproof of their density theorem.

Frozen scan018, lines 5–10, separately transports Out(π) to de Rham moduli and suspects that action is not algebraic. On Betti moduli, each automorphism of π acts algebraically: it replaces finitely many generating matrices by finite words, and multiplication/inversion in an algebraic group are regular; the operation is equivariant for conjugation and descends to the quotient. Inner automorphisms act trivially there.

However, conjugating an algebraic action by a nonalgebraic analytic isomorphism does not by itself show that the resulting action is nonalgebraic. The identity remains algebraic, and mapping classes induced by holomorphic automorphisms of X act by algebraic pullback on de Rham moduli. I have **not** proved here which remaining mapping classes act algebraically or that the whole transported action fails to be algebraic in a particular precise sense. The manuscript's action claim should remain a separately identified question unless a direct theorem or proof is supplied.

## MC11–MC13. No reductions and Zariski density

### The Borel argument

The calculation in frozen scans021–022 and **Hua, modernised reading, “Le calcul de degrés”** is correct under the stated properness, smoothness, connectedness, genus≥2, and characteristic-zero assumptions. A horizontal section would give an affine reduction with a flat extension

\[
0\to M\to F\to\mathcal O_X\to0,
\qquad E\simeq F\otimes L.
\]

The flat line bundle M has degree zero in characteristic zero. Taking determinants gives deg L=g−1. The composite K_X→E→L is zero because deg(L⊗K_X^−1)=−(g−1)<0. Thus E→L factors through a surjection O_X→L, forcing deg L=0, a contradiction. This excludes a Borel reduction. Characteristic zero is used materially: the integer-degree conclusion for flat line bundles cannot simply be carried over to positive characteristic.

For a reduction to the normalizer N(T), pass to the degree-at-most-two finite étale cover that kills N(T)/T. On a connected cover of degree d, Riemann–Hurwitz gives g′=1+d(g−1)≥2. The pulled-back transverse projective structure then has a torus, hence Borel, reduction, a contradiction.

### The finite case is necessary and can be supplied

Credit: **Hua, modernised reading, “Le calcul de degrés,” paragraph “Une lacune, et comment la combler”**, already identifies the missing finite-subgroup case and supplies the cover argument. Its refinement of **Hua, findings register, `159-no-reduction-monodromy-dense`** is independently checked here.

For an arbitrary subgroup of PGL2(C), absence of a Borel reduction and absence of an N(T) reduction do not alone imply Zariski density. For example, a finite tetrahedral group A4 is contained in neither but is certainly not Zariski dense. For the holonomy of an unbranched projective structure, however, a finite image can be killed by a finite étale cover. The pullback structure remains transverse and the covering curve still has genus≥2, while trivial holonomy gives a Borel reduction. This contradicts the already checked degree argument.

One can avoid a full list of exceptional finite groups. For a proper algebraic subgroup H⊂PGL2 in characteristic zero, either H is finite, or H° is a positive-dimensional proper connected subgroup. If H° is a Borel or a one-dimensional unipotent group, H lies in a Borel by normalizing H°. If H° is a torus, H lies in N(T). These cases exhaust the proper possibilities. The three exclusions therefore prove the scan022 proposition and the scan023 complex-monodromy density conclusion. The finite-cover step fills an omitted explicit case; scan022's “Le même argument montre” may be intended to encompass it, so one should not claim the author demonstrably failed to envisage it.

Finally, Hua's “La densité de Zariski, et où la situer” uses irreducibility, Zariski density, and nonelementarity as if interchangeable. They are different notions for general representations. A finite tetrahedral representation is irreducible but not Zariski dense. A dense subgroup of PSU(2) is complex-Zariski-dense in PGL2(C), yet fixes a point of hyperbolic three-space and is elementary in the Kleinian convention of [GKM, §1.3](https://www.math.ucdavis.edu/~kapovich/EPR/GaKaMa.pdf). GKM's main theorem imposes the stronger nonelementary condition on projective-structure holonomy. These examples correct terminology; they do not contradict the density theorem for the oper structures under discussion.

## Primary-source register and verification limits

1. **Gallo–Kapovich–Marden**, *The monodromy groups of Schwarzian equations on closed Riemann surfaces*, Annals of Mathematics 151 (2000), 625–704; [PDF](https://www.math.ucdavis.edu/~kapovich/EPR/GaKaMa.pdf), §§1.3 and 11.4. Properness is imported, not independently reproved.
2. **Dumas–Kent**, *Bers slices are Zariski dense*; [PDF](https://arxiv.org/pdf/0807.4509), Theorem A and §5. Main theorem imported; dimension deduction checked here.
3. **McMullen**, *The moduli space of Riemann surfaces is Kähler hyperbolic*; [PDF](https://people.math.harvard.edu/~ctm/papers/home/text/papers/kahler/kahler.pdf), §2. Only the indicated uniformization facts are used.
4. **Baba–Gupta**, *Holonomy map fibers of CP1-structures in moduli space*; [PDF](https://arxiv.org/pdf/1402.5445), §2.4. Only the grafting comparison is used.

Goldman's 1987 grafting-classification paper was located bibliographically (correct DOI: 10.4310/jdg/1214440978), but direct full text was blocked by the publisher's access page. It is therefore not represented here as a primary proof personally read. No secondary survey is used as the sole basis of the conclusions above.

The independent work actually completed consists of the fixed-X section-uniqueness argument, the dimension/category comparison, the V4 centralizer calculation and realization, the real-coordinate holomorphic obstruction and constructibility proof, the explicit two-halfplane counterexample, the deduction of RH nonalgebraicity from Dumas–Kent, the word-map argument for Betti Out(π), and the degree/finite-cover completion of density. No numerical experiment, formal proof assistant, or symbolic certificate was run for this report. Proposed check events are kept in the separate file `monodromy_check_events.tsv`; the main notes and main event ledger were not changed.
