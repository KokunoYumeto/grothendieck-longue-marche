## A. Conformal surgery, boundary regularity, and disc shadows

### S01 — Two discs and one duality

**67/053, central diagram and lower paragraphs; kind: unpursued implication.** The draft's “Cercles toriques orientés” and dual-line formulas supply the linear algebra later used for paired discs at nodes in 67/075–078. This **restates** the interpretation in **Hua, modernised reading of cote 67**, `hua_project/67.modern.tex`, §VI “Un brouillon : deux disques et une dualité,” p.52 (= scan53), but the cancellations and uncertain labels in this transcription prevent treating every diagram arrow as a settled equivalence of specified categories. The useful next step is to fix the morphisms and the reciprocal circle action before invoking the contracted product; compare B04 and the register's **EXIT_TOWER E.35**, which concerns a different, completed sewing construction.

### S02 — Interior uniqueness needs the fixed topological surface

**67/054–055, Théorème 1; kind: unproved claim.** “La structure conforme de X … est connue quand on la connaît dans Int(X)” is a uniqueness statement on the given topological bordered surface, not a reconstruction of its topology from an abstract open Riemann surface. The local embedding criterion on 55 supplies the necessary boundary information and is **restated with that qualification** in **Hua**, `hua_project/67.modern.tex`, §VII(1), pp.53–54 (= scans54–55). This package adds the exact distinction between the two sheaves that the argument uses, addressed in S03; it gives no universal existence theorem for arbitrary compactifications.

### S03 — The larger sheaf is data for recognizing charts

**67/054 and 056, sheaf paragraphs and Théorème 3; kind: own idea.** Scan54 explicitly says “À ne pas confondre” the extendable holomorphic germs with continuous functions holomorphic in the interior, whereas scan56 puts “est” in quotation marks when using the latter sheaf. A literal equality of these sheaves is false even on a half-disc: a continuous branch of \(\sqrt z\) is holomorphic in its upper-half interior but has no holomorphic extension across the boundary point zero. **Confidence: high**, by this elementary counterexample; the safe interpretation is recovery of the smaller sheaf through the chart criterion, which **qualifies** the unquoted formulation of Théorème 3 in **Hua**, `hua_project/67.modern.tex`, §VII(2), p.55 (= scan56), without asserting that Grothendieck intended the false equality.

### S04 — The general reflection sentence omits a live hypothesis

**67/055, paragraph invoking the “lemme de Schwartz|Schwarz”; kind: unproved claim.** The displayed Lemme 1 retains interior holomorphicity, but the following general sentence strikes out “hol.” and says only “continue … réelle sur U∩R … holomorphe.” The map \(f(x+iy)=x+2iy\) is a continuous open embedding of the closed upper half-plane, real on its boundary, and is not holomorphic, so the standalone sentence requires the interior hypothesis. This **confirms and rechecks** the correction already credited to **Hua**, `hua_project/67.modern.tex`, §VII(1), p.54 (= scan55); the counterexample refutes the isolated unqualified formulation, not the actual Lemme 1.

### S05 — Why the boundary derivative cannot vanish

**67/055–056, end of the proof; kind: unpursued implication.** The phrase “on voit tout de suite … n=1” can be made precise after reflection: the leading nonzero coefficient of the reflected map is real, and for \(n>1\) the imaginary part of \(a_n r^n e^{in\theta}\) changes sign as \(0<\theta<\pi\), contradicting the half-plane image. This is a **targeted recheck of the same argument** in **Hua**, `hua_project/67.modern.tex`, §VII(1), pp.54–55 (= scans55–56), and closes that local step under the lemma's retained hypotheses. It supplies no existence argument for a welding.

### S06 — What category belongs in Théorème 2?

**67/056, bracketed Théorème 2; kind: unproved claim.** “Équiv. de la cat. des surfaces conformes à bord compactes … courbes alg. propres lisses sur R” leaves the morphisms and connectedness conventions unspecified here. **Hua**, `hua_project/67.modern.tex`, §VII(1), p.55 (= scan56), and §IV “Surfaces à bord,” pp.39–43 (= scans40–44, outside this packet), **adds** boundary-preserving morphisms and the complex-double interpretation, including non-geometrically-connected real curves for orientable closed quotients. These are useful scope conditions, carried as contextual background rather than independently proved here; the displayed bracket is not a proof of an equivalence for every conceivable category of maps.

### S07 — Cutting and welding require different regularity tests

**67/056–057, Théorème 3 and Lemme 2; kind: self-flagged.** “Rectifiabilité suffit ?” and “rectifiable suffit ??” ask for a hypothesis on the embedded cutting complex. For a Jordan arc, the local cut surface can be uniformized using its two banks and prime ends; rectifiability is not needed for that local topological-boundary construction. This **supports**, in the Jordan-arc setting actually analyzed here, **Hua** §VII(2), pp.55–57 (= scans56–58), and the boundary extension theorem in Bishop's *Complex Analysis I*, Chapter12, Theorem12.14 [W1]; extension to the whole graph still requires the local finite-graph hypotheses to be stated, rather than importing the gluing converse.

### S08 — Endpoint normalization is revised across two pages

**67/057–058, Lemme 2(b); kind: reading question.** The frozen transcription has an inserted \(f(0)=0\) on 57 and then the live condition \(f(0)=x\) on 58, with injectivity only in the interior and separately on each bank. **Hua**, `hua_project/67.modern.tex`, §VII(2), pp.56–57 (= scans57–58), **differs** by presenting the coherent \(f(0)=x\) version directly. This is a recorded question about the draft's successive normalizations, not permission to replace the zero or add global injectivity in the frozen text.

### S09 — Regularity of the bank transition remains a question

**67/058, Scholie; kind: conjecture.** “Reflètent sans doute les propriétés de régularité correspondantes de K” proposes a relationship between the two induced analytic boundary structures and the smoothness of the embedded arc. **Hua**, `hua_project/67.modern.tex`, §VII(2), p.57 (= scan58), **restates** the relationship but does not specify a sharp equivalence of regularity classes. A proof would need explicit local hypotheses and both directions, especially at endpoints or cusps; the manuscript's request for a “Scholie plus circonstancié” remains substantive.

### S10 — Théorème 4 is an announced welding equivalence

**67/058–060, introduction and Théorème 4; kind: unproved claim.** “On doit avoir un théorème” introduces the equivalence between cut-and-marked surfaces and boundary-involution data, with unmarked circular components explicitly permitted. The quotient and its candidate sheaf are written down on 59, but conformal existence for the stated regularity class is the outstanding analytic step. This **restates** **Hua**, `hua_project/67.modern.tex`, §VII(3–4), pp.57–60 (= scans58–61), and is consistent with Bishop's primary-source statement that arbitrary circle homeomorphisms need not be conformal weldings [W2]; no claim is made that the manuscript supplies a modern quasisymmetric hypothesis.

### S11 — The two local gluing problems should be kept separate

**67/060–061, replacement versions of Lemme 3; kind: withdrawn in the same text.** The cancelled formulation on 60, which asks “ou plus régulier que ça ?,” is replaced by sewing two half-planes along an interval and folding one half-plane along the intervals adjoining zero, without supplying a regularity theorem. **Hua**, `hua_project/67.modern.tex`, §VII(3–4), pp.59–60 (= scans60–61), **reorganizes** these as an interior seam and a seam endpoint, explicitly normalizing overwritten interval bounds by the geometry. The replacement is evidence of reformulation, not a completed proof or a warrant to change the uncertain bounds in the transcription.

### S12 — The margin needs holomorphicity off the curve

**67/061, margin dated 12.1; kind: reading question.** The frozen reading is “continue|analytique dans U\C,” followed by holomorphicity on all of \(U\), so the mathematical conclusion depends on the disputed word. **Hua**, `hua_project/67.modern.tex`, §VII(3–4), p.60 (= scan61), **supplies** holomorphicity off the rectifiable curve; with that hypothesis the finite-length removability result applies, while mere continuity is refuted by the same elementary nonholomorphic map as in S04. Younsi's proof of the finite-length removability theorem, §3.2, Theorem3.5 [W3], supports the repaired claim; it does not settle the ink reading.

### S13 — Capping with a pointed disc has a regularity proviso

**67/061–063, projective boundary structures and Proposition; kind: unproved claim.** The reduction from a projective boundary structure to a toric one by choosing a centre explains the proposed equivalence with a marked pointed disc, but scan63 still says “rectifiable (?).” **Hua**, `hua_project/67.modern.tex`, §VIII “Un disque pointé, et la structure torique de son bord,” pp.60–62 (= scans61–63), **adds** an analytic-boundary regime in which extension and sewing are controlled. This identifies a sufficient local regime and the residual welding problem, without claiming that the undefined rectifiable category has been proved equivalent.

### S14 — An explicit family with the same shadow

**67/063–064, “ombre de D”; kind: own idea.** “N'a rien d'injectif” is witnessed, in a fixed plane chart at zero and with \(r>0\) small enough to stay in that chart, by the discs \(f_\varepsilon(\overline{\mathbb D})\), where \(f_\varepsilon(z)=r(z+\varepsilon z^2)\) and \(|\varepsilon|<1/2\): these maps are injective and all have derivative \(r\) at zero, hence the same tangent shadow, while the images vary. **Confidence: high**, since factoring \(f_\varepsilon(z)-f_\varepsilon(w)\) proves injectivity and uniqueness of normalized Riemann maps distinguishes the images. This **adds an explicit example** to **Hua** §VIII “L'ombre d'un disque,” pp.62–63 (= scans63–64), and bears on **MPL_152+120 Q1-07**, whose actual comparison text is absent from the supplied context and is therefore not claimed solved.

### S15 — The disc exception to a canonical toric boundary structure

**67/065, metric paragraph; kind: unproved claim.** The words “dans tous cas le bord est muni d'une structure torique canonique” are too broad for the unpointed disc: an invariant boundary rotation structure would have to be preserved by the whole disc automorphism group, but its rotations select a centre and that group moves centres. This **rechecks the exception already identified by Hua**, `hua_project/67.modern.tex`, §VIII “Systèmes admissibles,” p.64 (= scan65), without disputing the hyperbolic case explicitly used afterward. The projective-plane margin is too uncertain to use as a precise additional theorem.

### S16 — Admissibility is a comparison of two boundary structures

**67/065–066, definition; kind: unpursued implication.** “Les deux structures toriques … coïncident” makes admissibility a coupled condition involving both a disc and its complement, so it is not merely a condition on each disc's first derivative. This **restates** **Hua**, `hua_project/67.modern.tex`, §VIII “Systèmes admissibles,” pp.64–65 (= scans65–66), and explains why the noninjectivity example S14 alone does not refute injectivity on admissible systems. It bears on **MPL_152+120 Q1-07** by identifying the extra hypothesis any comparison must preserve, not by filling the missing external comparison.

### S17 — Intrinsic metric discs are not identified with admissible discs

**67/066, Questions; kind: self-flagged.** “Comment cette condition d'admissibilité se reflète-t-elle … géométrie interne de X ?” is followed by the specific comparison with geodesic discs for the “Bergmann|Bergman” metric. **Hua**, `hua_project/67.modern.tex`, §VIII “Systèmes admissibles,” p.65 (= scan66), **restates** the question using a generic canonical metric, whereas this transcription preserves the narrower, uncertain metric name. Neither source supplies an equality of the two classes of discs; a proposed test should compute both boundary actions for a concrete surface.

### S18 — A product topology does not identify the capping map

**67/067, map \(TB_{g,\nu}\to T_{g,\nu}\); kind: self-flagged.** “Je présume qu'elle est fibrante … c'est la projection canonique” is stronger than the displayed dimensions or abstract homeomorphism types of the spaces. **Hua**, `hua_project/67.modern.tex`, §VIII “L'espace de Teichmüller à bord, et une conjecture,” pp.65–66 (= scans66–67), **retains the conjectural status** rather than proving that the particular capping operation is the product projection. The fibre and local-triviality questions remain separate from the shadow-surjectivity obstruction below and from the operator-group comparison **LM4 C.12**.

### S19 — Independent dependence on pants lengths is unverified

**67/067–068, pants argument; kind: self-flagged.** “Dont chacun ne dépend que des ℓ_i correspondants, pas des autres ℓ_j,” the marginal question mark, and “Ce point étant supposé acquis” isolate the key unproved independence assertion. **Hua**, `hua_project/67.modern.tex`, §VIII, pp.66–67 (= scans67–68), **restates** this dependence and links it to the later Bers-letter model in §III, pp.18–21 (= scans19–22, outside this packet). The fact that three marked points determine a sphere does not determine its embedded capping discs; the manuscript therefore supplies neither this independence nor the claimed fibre parametrization.

### S20 — The unrestricted shadow-surjectivity conjecture fails

**67/068–069, Conjecture; kind: unproved claim, refuted in the stated unrestricted target.** The claim that \((D_i)\mapsto(o(D_i))\) “est bijective” onto all tangent-disc systems fails already on the sphere marked at \(0,1,\infty\): the disc at zero omits both 1 and infinity, so its conformal radius in the coordinate \(z\) is at most 4 by the Koebe quarter theorem. Thus even arbitrary disjoint discs, and consequently admissible ones, cannot realize a shadow radius greater than 4. This is a **targeted recheck of Hua's argument**, not a new discovery: `hua_project/67.modern.tex`, §VIII, footnote to the p.67 Conjecture (= scans68–69), with the quarter-theorem normalization checked in [W4]; it refines **MPL_152+120 Q1-07** only to the extent of this explicit local statement, and leaves injectivity onto the feasible image open.

### S21 — A corrected target must respect simultaneous realizability

**67/069, principal-bundle consequence; kind: own idea.** The proposed full \((\mathbb R_{>0})^I\)-action by independent dilation of all shadows cannot preserve the bounded feasible image in S20. A possible revised question is whether the shadow map is injective, locally invertible, or proper onto a specifically characterized region of simultaneously realizable shadows. **Confidence: medium** as a research direction, because boundedness alone settles none of those properties; this **adds a separated set of targets** to **Hua** §VIII, pp.67–68 (= scans68–69), and to the unresolved **MPL_152+120 Q1-07** comparison without asserting that the remaining fibre is not abstractly homeomorphic to \(\mathbb R^\nu\).

### S22 — Marked genus zero is less symmetric than an unmarked sphere

**67/069–070, canonical-section discussion; kind: own idea.** “Cela semble étrange … pas de métrique canonique sur X” does not itself obstruct a canonical choice depending on the marked surface: for a sphere with three distinct marked points, average the pullbacks of a fixed round metric over the six coordinates that send those points to \(0,1,\infty\), then normalize area. **Confidence: high** for this isomorphism-invariant smooth metric construction, because the six coordinates are permuted by every isomorphism of the marked triple. It **qualifies** the symmetry objection restated by **Hua**, `hua_project/67.modern.tex`, §VIII, pp.68–69 (= scans69–70), but neither makes that metric a constant-curvature metric nor proves that its tangent discs form an admissible system or a section of the conjectural bundle.

### S23 — The global lemma does not eliminate the welding converse

**67/070–071, §5 and Lemme 4A; kind: unproved claim.** “La formulation … est un peu alambiquée” motivates replacing the local lemmas by global slit-disc uniformization, said to contain the same essential technical content as Théorème 4. **Hua**, `hua_project/67.modern.tex`, §IX, pp.69–70 (= scans70–71), **clarifies** the distinction: uniformizing a given Jordan slit is a forward construction, while reconstructing a slit from an arbitrary boundary map is the converse welding problem. The replacement helps organize the questions but does not prove their equivalence with all of the category-level data in Théorème 4.

### S24 — Three boundary marks explain normalized uniqueness

**67/071–072, Lemme 4A and NB1; kind: unpursued implication.** “Agit de façon simplement transitive” on cyclically ordered triples explains uniqueness after choosing the three prime ends represented by \(1,\zeta,\bar\zeta\). This **rechecks** the normalization in **Hua**, `hua_project/67.modern.tex`, §IX, pp.70–71 (= scans71–72): an automorphism fixing three distinct boundary points is the identity, while opposite cyclic order would require reversing orientation. It does not identify the two banks as a single injectively parametrized boundary, nor justify the converse B).

### S25 — “Rectifiable homeomorphism” needs a definition

**67/072–073, Lemme 4B and Scholie(a); kind: own idea.** “Tout … homéom rectifiable” cannot mean merely that the graph of an increasing interval homeomorphism has finite length, since for every partition its polygonal length is bounded by total horizontal variation plus total vertical variation, namely 2. **Confidence: high** for this elementary obstruction to that interpretation; **Hua**, `hua_project/67.modern.tex`, §IX, pp.71–72 (= scans72–73), **adds** the alternative interpretation “absolutely continuous in both directions” while leaving the rectifiable-slit converse unproved. Even a satisfactory sufficient welding class must be distinguished from the class producing rectifiable seams, so the four-way Scholie cannot be accepted merely by expanding the adjective.

### S26 — The normalized value is a post-freeze reading question

**67/073, condition 2); kind: reading question.** The frozen text gives `f(\unsure{\omega|0})=0`, while **Hua**, `hua_project/67.modern.tex`, §IX, p.72 (= scan73), reads the draft as \(f(0)=0\) and replaces it mathematically by \(f(1)=0\). The latter **differs from the diplomatic reading** and is consistent with the slit tip being reached from the boundary prime end 1 rather than an interior point of the injective map. This records the reason for a future ink review; it does not change the frozen glyph or treat the contextual correction as manuscript evidence.

### S27 — The power-series item retains all boundary and injectivity conditions

**67/074, Scholie(d); kind: unpursued implication.** “Celle-ci ayant les propriétés 1) 2) 3) de B)” is essential: radius of convergence at least 1 and \(|f|\leq1\) alone allow constant functions or \(z^2\), neither a normalized slit uniformization. **Hua**, `hua_project/67.modern.tex`, §IX, p.73 (= scan74), **restates** the full boundary-extension condition, so this item is an encoding of an already constrained map rather than an independent coefficient characterization. Finding explicit inequalities on coefficients that guarantee all the required boundary identifications would be an additional problem not solved here.

### S28 — Stability requires conditions on the cuts

**67/074–075, passage to \(X'''\); kind: unproved claim.** “Une courbe … stable (au sens de Mumford-Deligne)” requires every normalized component to satisfy \(2g_v-2+n_v>0\), where branches of nodes and remaining marked points are counted. If arbitrary cuts were permitted, a contractible separating curve could instead create an unstable rational component, so the implicit Teichmüller cutting convention must be made explicit or followed by stabilization. This **adds a hypothesis check** to **Hua**, `hua_project/67.modern.tex`, §X, pp.73–74 (= scans74–75), and bears on the stable-graph setting of **EXIT_TOWER A.5**, carried here only as a register claim.

### S29 — A propagation tensor is first-order sewing data

**67/075 and 078, nonzero tangent tensors; kind: unpursued implication.** The proposed “structure de propagation” gives a nonzero element of the tensor product of the two tangent lines, and the polar-disc construction uses its inverse dual pairing. **Hua**, `hua_project/67.modern.tex`, §X, pp.74 and77 (= scans75 and78), **identifies** the relation with local plumbing \(zw=t\), but a tensor by itself does not choose the full germs of the two local coordinates needed for a global sewing. This distinction is relevant to **LM6 F.43** and **EXIT_TOWER E.35** through the normal-line torsors discussed in B04; it does not turn the manuscript into a proof of those later register claims.

### S30 — Dimension matching is conditional evidence

**67/076–077, moduli morphisms and dimensions; kind: unproved claim.** “On trouve sûrement un morphisme” and “Sûrement aussi” precede the real-analytic and algebraic moduli assertions, while the dimensions match only if the proposed disc data have the expected real dimension. For a stable stratum with \(e\) nodes, the familiar count \((3g-3+\nu-e)+e\) explains the contribution of nonzero smoothing tensors, but it does not construct the moduli objects, their morphisms, or their fibres. This **qualifies** the dimension explanation in **Hua**, `hua_project/67.modern.tex`, §X, pp.75–76 (= scans76–77), and bears on **EXIT_TOWER A.5/E.35** as geometric motivation, not as a reproof.

### S31 — The requested inverse depends on the disc conjecture

**67/078, Question and proposed inverse; kind: self-flagged.** “Ces flèches sont elles des iso” is immediately followed by “Si la détermination conjecturale … était connue,” so the inverse construction is explicitly conditional. **Hua**, `hua_project/67.modern.tex`, §X, p.77 (= scan78), **retains** that dependency, and S20 shows that at least the unrestricted shadow target used by the argument must change. The surviving question is whether suitably restricted normal data and actual admissible discs determine an inverse, not whether a dimension count already proves an isomorphism.

### S32 — A geodesic representative does not make the seam geodesic

**67/079, seam paragraph; kind: self-flagged.** “Peut-être pas … ?? … à examiner de plus près” separates the surgically produced circles from the geodesics in their free homotopy classes. **Hua**, `hua_project/67.modern.tex`, §X, p.78 (= scan79), **restates** that distinction; the usual uniqueness of a hyperbolic geodesic representative applies to essential nonperipheral classes and does not verify geometric properties of the original seam. Any inverse construction preserving specified cuts must account for this replacement and for the excluded classes.

### S33 — Fixed plumbing charts and varying admissible discs are different questions

**67/079–080, rescaling argument; kind: withdrawn in the same text.** “Tout à fait vaseux” becomes “c'est probablement tout à fait faux !” when the proposed inverse rescales paired polar discs by \(\lambda\) and \(\lambda^{-1}\). **Hua**, `hua_project/67.modern.tex`, §X, pp.78–79 (= scans79–80), **adds** the valid local observation that changing cutoff radii in fixed plumbing charts does not change the overlap relation \(zw=t\), but that does not show that globally reselected admissible discs use those same charts. This narrower distinction is the refinement supported here: fixed-chart radius independence is compatible with the manuscript's doubt about the global inverse.

### S34 — The four-holed sphere and tangent map remain proposed tests

**67/080–082, final paragraphs; kind: self-flagged.** “Le cas-clef” is \((g,\nu)=(0,4)\), followed by “il faudrait … comprendre l'application sur les groupes fondamentaux” and “vérifier si … est étale … son application tangente.” **Hua**, `hua_project/67.modern.tex`, §X, pp.79–81 (= scans80–82), **interprets** the two six-real-parameter descriptions as length/twist and plumbing data, while these scans provide neither a Jacobian nor a fundamental-group calculation. They therefore identify concrete tests relevant to **EXIT_TOWER E.35/E.45** and **PUSH_ORDER5_FRAME Itemsfromt 2**, but give no pentagon relation, rigid five-point frame, or higher-genus restriction-image result.
