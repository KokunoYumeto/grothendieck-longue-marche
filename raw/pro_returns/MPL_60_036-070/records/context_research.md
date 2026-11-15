# Post-freeze context research memo

## Scope and evidential status

This memo was prepared only after the parent reported the transcription frozen at **2026-11-15 22:48:34 UTC** and the context archive opened afterward. No cote 60 scan was inspected by this ancillary researcher, and no frozen page, combined transcription, or doubts file was changed. Cote 60 comparisons below use the parent's frozen text; they are not independent palaeographic endorsements.

Sources read: `context/README.md`; all of `context/notes/RESULTS_STATE.md`; relevant passages in `context/MPL_16+47+54+44_transcription.tex`, `context/MPL_16+47+54+44_notes.md`, and the doubts file; and the supplied printed Oda PDF. **Every earlier-run transcription or research note remains an unreviewed lead**, even where its own heading says “established comparison”: the README expressly says that this package has not received its second pass. The results register's explicit referee statuses are retained only for the results it names; no such status transfers to a neighbouring argument by analogy.

In the locators below, **CT** means the exact file `context/MPL_16+47+54+44_transcription.tex`; **CN** means `context/MPL_16+47+54+44_notes.md`; and a locator such as **CT 54/007** gives cote and PDF scan, not manuscript foliation. These are comparisons with supplied transcriptions, not newly checked original archive images. Oda page numbers are printed pages; PDF page numbers are supplied separately where useful.

## 1. Context comparisons with precise archive locators

### C01 — Local inertia averaging adds material absent from the supplied neighbouring package

**Cote 60:** 037, 039–047. **Context search:** `inerti`, `moyenne`, `Cohomologie à l'infini`, `boundary cohomology`, `compactif`, `fonctionnelle`; no matching inertia-average or compactification-boundary construction was located in CT/CN or the supplied Oda text. **Relation: adds**, within this limited supplied context, not a claim of historical novelty.

The contrast on 60/037 between a globally defined composition-factor recipe and a recipe “locale en (E,x)” is developed on 60/039–047 into a local representation-theoretic operation and trace average. The nearest categorical antecedent in CT is **16/049**, which discusses algebraic splittings and “the category of motives which is semi-simple !”, but this is a different, conditional motivic programme, not an earlier proof of the local averaging construction. Bears on **WG2 §2.4 #3**, chiefly by clarifying that these cote 60 pages concern local representations and virtual sheaves rather than a construction of the category of motives from Lefschetz rings.

### C02 — Exactness does not supply a tensor functor

**Cote 60:** 041, especially the insertion “foncteur exact. Il induit un hom.” **Context:** **CT 16/049**, conditional splitting/semisimplicity; **CT 47/004**, the explicitly calculated exchange of convolution and tensor product; **CN 47:8:3**, translation and tensoring, an unreviewed lead. **Relation: differs**, with a useful new test supplied by cote 60.

The inertia-invariant functor for a finite quotient in characteristic zero is exact but need not preserve tensor products or be faithful. **Own check, high confidence:** for the nontrivial character \(\chi\) of \(C_2\) over a characteristic-zero field, \(\chi^{C_2}=0\), while \((\chi\otimes\chi)^{C_2}=k\); this explicitly prevents using the averaging map as a tensor fibre functor merely from its exactness. This bears directly on **MPL_7_061-072+8_001-078 Scan 061 (§66)**, whose internal **T.01** lead requires exactness, faithfulness, and tensor compatibility separately; the present pages add an elementary separating example, without re-proving Tannakian reconstruction.

### C03 — Three different dualities must retain their own conventions

**Cote 60:** 049–051. **Context:** **CT 16/018**, degree reversal and passage to the opposite ring in its “principe de dualité”; **CT 47/011**, remark 4 involving \(\check F\), \(\omega_A[n]\), and \(\Phi(F)^\vee\); **CT 54/003, 005, 007**, de Rham, universal-extension, and Cartier dualities. **Relation: adds a different realization of duality**, not a restatement of any of these formulas.

The distinction between \(\check E\) at the generic point, the dual of a point representation, and Verdier duality is essential to 60/049–051. **CN F20** already warns that the check in 47/011 has no supplied definition and cannot silently be identified with ordinary derived dual; **CN D01–D05** discuss a separate abelian-variety comparison. Bears on **MPL_14_002-044 A36** as a convention-sensitive comparison only: neither the earlier lead nor the new formula authorizes transferring an unspecified transpose, kernel inversion, or shift across these settings.

### C04 — Tate twists and cohomological shifts are separate data

**Cote 60:** 049, 051, 053. **Context:** **CT 16/021**, the insertion defining \(Z_\ell[1]=\varprojlim_\nu\mu_{\ell^\nu}\) as the Tate sheaf; **CT 16/048**, “as usual, I drop the twist for simplicity”; **CT 47/011**, the explicit virtual sign \((-1)^n\) coming from a cohomological shift. **Relation: differs in notation and adds an explicit local correction**, without contradiction.

Square brackets denote a Tate twist in CT 16/021, while 60/049 visibly deletes a cohomological `[2]` beside a live Tate twist `(1)`; neither package's brackets should be normalized from the other. Since the cote 60 argument is explicitly virtual, an even shift has the same Grothendieck class, but this does not produce a derived-category isomorphism. Bears on **MPL_14_087-132 M05**, **MPL_15_195-228+18_002-017 M03**, and **MPL_15_195-228+18_002-017 P09** as a convention check; it does not settle their separate central-grading or mixed-Hodge-index questions.

### C05 — Purity alone does not imply the self-duality used on 60/053

**Cote 60:** 053, “Supposons E de poids …, donc” followed by \(\check E\simeq E(\rho)\). **Context:** **CT 44/002**, Th. 4 explicitly asserts that an autoduality is associated with a polarization; **CT 44/008–009**, the letter calls positivity a difficult unproved point; **CT 54/003–005** pairs an abelian variety with its dual, not automatically with itself. **Relation: differs; a missing-hypothesis test**, not a correction to the transcription.

**Own check, high confidence:** a rank-one unramified sheaf with Frobenius eigenvalue a primitive cube root of unity is pure of weight zero but has a distinct contragredient eigenvalue; extending the coefficient field to contain that root is permitted by the setup on 60/037. Thus ordinary purity by itself cannot justify the displayed self-duality, whereas a specified nondegenerate pairing of the required Tate weight can. Bears on **MPL_15_195-228+18_002-017 B03** and **WG2 §2.3 #12**: retain polarization/self-duality as a separate hypothesis, and do not turn the passage into a proof of the positivity programme of cote 44.

### C06 — Epsilon symbols in the neighbouring Fourier notes are not local epsilon constants

**Cote 60:** 053–059, especially “modulo un signe” at 059. **Context:** **CT 47/008**, remark 1c and its marginal definition of \(\varepsilon\) as virtual rank; **CT 47/004**, cancellation of “l'identité” in favour of \((-1)^n s_A^*\); **CT 47/011**, the explicit complaint about an omitted \((-1)^n\); **CT 44/004**, the deleted “[au signe près ??]” preceding its Néron–Tate formula. **Relation: differs**, while restating the broad need to track signs.

The \(\varepsilon\) of CT 47/008 is expressly a virtual-rank function with values in \(H^0(S,\mathbb Z)\), whereas the normalized determinant on 60/057 is an epsilon-type quantity. No formula from the Fourier notes determines the sign left open on 60/059, and the cancelled question in 44/004 is about an intersection/height pairing, not the same sign. This gives no new proof for **WG H9** or **WG2 §2.3 #12**; the comparison is a warning against identifying homonymous symbols or unrelated parity factors.

### C07 — Boundary cohomology adds an independent object

**Cote 60:** 061, “Cohomologie à l'infini” and “au décalage d'une unité près”. **Context:** no matching construction found; **CT 47/004** and **47/011** use derived direct images and duality, but with proper abelian schemes and a different purpose. **Relation: adds**, with no supplied precedent or contradiction.

**Own formal implication, high confidence conditional on the usual six-operation identities:** defining \(B_f(F)=\operatorname{Cone}(Rf_!F\to Rf_*F)\) makes the compactification-boundary expression on 061 a model for an intrinsic cone, and duality gives \(D B_f(F)\simeq B_f(DF)[-1]\). The one-unit shift follows because duality reverses the cone triangle; this is a proposed formal reconstruction, not a claim that every map or independence statement is proved on the page. It does not address **LM7 E.23** or any listed motivic-moduli assertion merely because those subjects also involve boundaries or inertia.

### C08 — Lower-level correction factors are a different problem from Lefschetz gradings

**Cote 60:** 063–069, “niveau … inférieur”, the trivial solution \(\lambda=1/L\), and the imposed restriction on allowable corrections. **Context:** **CT 16/016–018** constructs graded Lefschetz-ring data; **CT 44/007** discusses Lie-theoretic “poids”, “copoids”, and terminology on a reused sheet. **Relation: differs**, with only a possible analogy of filtrations.

Neither the Lefschetz grading nor the root-system weights supply the manuscript's “niveau” condition on rational functions. Bears on **MPL_14_087-132 M05** and **MPL_15_195-228+18_002-017 M03** only as a reason to separate kinds of grading, and on **MPL_15_195-228+18_002-017 R01** as a provenance warning. No claim about central Tate cocharacters, motivic reconstruction, or a solution of the restricted correction problem follows from the shared words “poids” and “niveau”.

## 2. Conditional consistency test: does the stated additivity force the local correction to vanish?

This responds to a specific question from the parent. It is an **own mathematical inference**, not a manuscript reading and not a claim of novelty. It must remain conditional because the frozen excerpt overloads \(E_\eta(x)\): 60/047 assigns it the averaged value, whereas 60/051 subtracts \(E_\eta(x)\) from the averaged value. Earlier scans outside this package may resolve that notation.

Assume the conventional interpretation

\[
E(x)=E^I,\qquad \check E=E^\vee,
\qquad \alpha(E)=E^\natural-E^I,
\qquad \mu(E)=\alpha(E)^\vee-\alpha(E^\vee)(1),
\]

and assume that the additivity asserted on 60/051 holds on the category of local finite-dimensional \(D\)-representations in which a \(D\)-normal finite-index subgroup \(U\subset I\) acts unipotently. Then **\(\mu(E)=0\) in the Grothendieck group**:

1. The \(D\)-stable filtration constructed on 60/039 has factors \(F_i\) on which \(U\) acts trivially.
2. On each factor the averaging operation is ordinary invariants, so \(\alpha(F_i)=0\). The same holds for \(F_i^\vee\), because its inertia action still factors through the finite group \(I/U\).
3. Hence \(\mu(F_i)=0\), and additivity gives \(\mu(E)=\sum_i\mu(F_i)=0\).

This argument has no counterexample under the stated hypotheses. A two-dimensional tame unipotent test confirms rather than defeats it: with geometric Frobenius acting as \(\operatorname{diag}(q^{-1},1)\), and monodromy \(N(e_2)=e_1\), the average has the classes of \(\mathbb Q_\ell(1)\) and \(\mathbb Q_\ell\); ordinary invariants give \(\mathbb Q_\ell(1)\), so \(\alpha(E)=\mathbb Q_\ell\). For the dual, \(\alpha(E^\vee)=\mathbb Q_\ell(-1)\), and the final twist makes the two terms of \(\mu\) cancel.

**Scope caveat:** the written statement says additive in global \(E_\eta\), whereas the filtration is local \(D\)-stable; its factors need not be restrictions of global sheaves. Therefore local additivity must be justified, rather than inferred solely from globally available short exact sequences. Under the usual local-cohomology interpretation of 60/049, both the averaging operation and the alternating class of local cohomology extend to the local category, which supplies that justification, but the excerpt's notation and the exact category should be checked before declaring the manuscript's later correction terms redundant.

More explicitly, the conventional reading of the displayed local-duality identity on 049 gives
\[
\mu(E)=(E^\vee)^\natural\bigl(1-\mathbb Q_\ell(1)\bigr)
       +[R\Gamma(I,E^\vee)](1).
\]
Both terms are additive on the usual finite-dimensional continuous local category. On a finite-inertia factor \(F\), \([R\Gamma(I,F)]=[F^I]-[F^I(-1)]\); devissage then gives the same identity with \(F^I\) replaced by \(E^\natural\), and the two displayed summands cancel. This supplies a route to proving local additivity and vanishing from the local-cohomology interpretation, rather than treating the manuscript's global assertion alone as sufficient.

Recommended final-note status: **own implication / consistency test, high confidence under the stated interpretations; attribution to the intended manuscript construction remains conditional**. It is not evidence that Grothendieck explicitly withdrew the correction term, nor that the frozen reading should be changed. It bears directly on **Hua, findings register, 60-inertia-average-duality**, whose supplied excerpt leaves the correction unspecified; none of CT's preceding materials resolves the ambiguity.

## 3. Oda 1969: verified statements and limits

The printed PDF was text-extracted solely for search, and the exact statements below were checked visually on the supplied printed pages **69, 70, 89, 100, 101, 118, 126, and 131** (PDF pages **8, 9, 28, 39, 40, 57, 65, and 70**). No OCR was applied to any manuscript scan. The PDF has a NUMDAM cover followed by the article, so its PDF-page offset is different from the archive scans.

| Printed locator | Exact scope and content relevant here | What it does not establish |
|---|---|---|
| **Corollary 1.3(ii), pp. 69–70; especially p. 70** | For an isogeny \(\lambda:X\to Y\) of abelian schemes over a prescheme \(S\), with the dual abelian schemes existing, there is a canonical isomorphism \(\ker(\lambda^t)\simeq D_S(\ker\lambda)\), functorial in the isogeny; the displayed bidual compatibility carries a minus sign. | This is Cartier duality of finite group schemes, not Verdier duality of an arbitrary ramified \(\ell\)-adic local system. |
| **Theorem 3.19, p. 89** | For a finite commutative group scheme of \(p\)-power rank over the perfect characteristic-\(p\) field of §3, \(M(DG)\simeq D(MG)\) canonically as left Dieudonné modules, compatibly with biduality. The module dual is Definition 3.5, \(\operatorname{Hom}_{W(k)}(M,C(k))\), with \(F,V\) interchanged semilinearly, not an unspecified ordinary vector-space dual. | It cannot identify \(D\), \(\check{\phantom E}\), and \(\vee\) in cote 60 without translating categories and conventions. |
| **Proposition 3.23, p. 100** | For an abelian scheme over a perfect field of characteristic \(p\), the Dieudonné module of the dual abelian variety's \(p\)-divisible group is canonically the \(W(k)\)-linear dual of that of the original, with the indicated \(F,V\) action and signed bidual diagram. | It does not identify an abelian variety with its dual without additional data. |
| **Proposition 3.24, pp. 100–101** | A homomorphism \(\lambda:X\to X^t\) gives a Dieudonné-module homomorphism, a tensor, and a \(W(k)\)-bilinear form; if \(\lambda\) is symmetric, these corresponding objects are skew-symmetric. Invertible sheaves yield these Riemann data, with \(b(Fx,y)=b(x,Vy)^\sigma\); the construction is additive. | Skew-symmetry is not the positivity/ample-polarization theorem sought for arbitrary intermediate Jacobians in cote 44. It also does not fix the sign of an \(\ell\)-adic functional equation. |
| **Proposition 5.1, p. 118; proof continues p. 119** | For an abelian scheme over a field \(k\), the Hodge-to-de Rham spectral sequence degenerates. The proposition itself does **not** impose characteristic zero or perfectness. | It is not a degeneration theorem for every smooth proper scheme in characteristic \(p\), and it supplies no canonical splitting of the Hodge sequence. |
| **Theorem 5.10, p. 126** | Over a perfect field of characteristic \(p\), part (i) constructs the map from \({}_pI(X)\) when \(H^0(X,\mathcal O_X)=k\); part (ii) adds normality for injectivity and Cartier-operator compatibility. Part (iii), stated for a proper smooth \(k\)-scheme, identifies the image with \(\bigcap_n\ker(d\circ V^n)\) and the corresponding intersection with \(H^0(X,\Omega^1)\). | For general smooth proper \(X\), the comparison is an image description, not an automatic identification with all of \(H^1_{\mathrm{dR}}(X)\). |
| **Corollary 5.11, p. 131** | For an abelian scheme \(X\) over a perfect field \(k\) of characteristic \(p\), \(M(X[p])\simeq H^1_{\mathrm{dR}}(X)\) canonically as left Dieudonné modules; \(VM(X[p])=\ker F\) maps to \(H^0(X,\Omega^1_{X/k})\), and the displayed Dieudonné exact sequence corresponds to the Hodge exact sequence. | This reconstructs filtered degree-one de Rham cohomology from the finite group scheme and its Dieudonné structure, not from the abstract group of geometric points, and not from generic \(\ell\)-adic inertia data. |
| **Corollary 5.12, p. 131** | For a smooth proper \(k\)-scheme with \(X(k)\ne\varnothing\), over a perfect characteristic-\(p\) field, there is a canonical injection \(D M({}_p\operatorname{Pic}_{X/k})\hookrightarrow H^1_{\mathrm{dR}}(X)\) with image \(\bigcap_n\ker(d\circ V^n)\). It is an isomorphism for abelian schemes. | Dropping the abelian hypothesis does not preserve the surjectivity in Corollary 5.11. |

### Oda comparison with the supplied archive context

**CT 54/007** ends with “Cette extension peut-elle se déduire de la connaissance de \(p^A\) ??”. **CN D05** already identifies Corollary 5.11 as the relevant later comparison; this is an earlier unreviewed lead whose cited theorem has now been independently checked in the supplied printed witness. Thus the current comparison **restates and verifies the published support for that lead under its perfect-field/abelian hypotheses**, while cote 60 itself adds no reconstruction theorem for \(A[p]\).

**CT 54/005–007** proposes orthogonality of Frobenius kernels and writes the transposed Frobenius–Verschiebung diagram. **CN D03** points to Oda's Cartier duality: the printed theorem confirms the isogeny-kernel duality with its variance and sign, but the annihilator interpretation remains a deduction requiring the Frobenius twists. **CT 54/003** qualifies its canonical extension “du moins en car. 0 !”; Proposition 5.1 and Corollary 5.11 provide precise positive-characteristic comparisons for abelian varieties, without manufacturing a canonical splitting.

Oda's remark after Corollary 5.11 says that the result was conjectured in Grothendieck [15]; the bibliography identifies [15] as *On the de Rham cohomology of algebraic varieties*, IHÉS No. 29 (1966). This supports the printed conjecture attribution; it does **not** date the undated cote 54 sheet, establish a direct transmission history for it, or identify cote 60's inertia-average question with that conjecture.

**Verified bibliographic entry (APA form):** Oda, T. (1969). The first de Rham cohomology group and Dieudonné modules. *Annales scientifiques de l'École Normale Supérieure, 4e série, 2*(1), 63–135. The supplied cover gives the primary item URL `http://www.numdam.org/item?id=ASENS_1969_4_2_1_63_0`. The DOI listed in CN is a bibliographic lead; this memo did not independently query its resolver.

## 4. RESULTS_STATE mapping and exclusions

The table distinguishes actual bearing from shared vocabulary. Only the supplied register excerpts were available for most named returns; their full original research files were not consulted. None of the following first-pass statuses is upgraded to reviewed by this memo.

### Directly relevant or useful as a limited comparison

| Register ID | Bearing of cote 60 and limit |
|---|---|
| **MPL_7_061-072+8_001-078 Scan 061 (§66)**, internal **T.01** | Direct: 60/041 separates exactness from the faithfulness and tensor conditions required of a fibre functor; C02 supplies the finite-character test. |
| **MPL_15_195-228+18_002-017 B03** | Direct conceptual bearing: 60/053 uses self-duality after a weight assertion; C05 isolates the additional pairing hypothesis. No real-section reconstruction follows. |
| **MPL_14_002-044 A36** | Limited convention comparison: 60/049–051 requires identifying the actual dual/transpose, not importing a checked glyph from another setting. |
| **MPL_14_087-132 M05** | Limited comparison: weight gradings, Lefschetz degree, and the “niveau” of correction factors are distinct; no central cocharacter is constructed here. |
| **MPL_15_195-228+18_002-017 M03** | Same limited distinction of gradings and Tate conventions; the parabolic/Levi construction described in that lead is absent here. |
| **MPL_15_195-228+18_002-017 P09** | Relevant convention caution for twists and indices; the mixed-Hodge associated-graded question is not settled by 60/049 or 063–069. |
| **MPL_15_195-228+18_002-017 R01** | Direct method/provenance comparison: the reused commutative-algebra typescripts in the present package cannot serve as evidence for the handwritten motivic or functional-equation claims merely because their words overlap. |
| **MPL_14_002-044 M29a** | Limited comparison: 60/039–043 explicitly works with non-semisimple representations and passes to classes; that is consistent with the lead's warning about extrapolating pure semisimplicity to mixed extensions. It does not settle that lead's particular mixed example. |
| **MPL_14_087-132 M09** | Limited negative bearing: the exact invariant operation on 60/041 does not establish semisimplicity of motives or the kernel statement in the lead. |
| **MPL_14_087-132 M01** | Negative answer to construction question: 60/039–047 does not construct a pure-motive category from graded correspondence rings. |
| **MPL_14_002-044 M01** | Same scope boundary: these pages do not replace an already-given motivic category by a new construction. |
| **MPL_15_195-228+18_002-017 M01** | Same scope boundary for the motive-category construction question. |
| **MPL_14_002-044 §2** | Its planning questions receive a negative/scope answer from this excerpt, not a new proof. |
| **MPL_15_195-228+18_002-017 §2** | Same: local averaging and functional equations do not answer the Lefschetz-ring construction question. |
| **MPL_14_002-044 §107** | Register-comparison methodology only; no additional theorem is inferred from this summary row. |
| **MPL_15_195-228+18_002-017 P01** | Oda supplies one precisely scoped realization comparison relevant to the wider programme; 60/039–069 does not establish the six descriptions in that lead. |

### Entries receiving no mathematical update from these pages

| Register ID(s) | Reason for exclusion |
|---|---|
| **LM7 E.23** | The open classification of continuous sections of geometric metabelian/marked arithmetic quotients is not the local linear inertia calculation here. No section-map image or fibre is computed. |
| **LM7_PUSH D.44** | The refereed modular-descent/gentle-normalization result concerns a different group-theoretic problem. Its reviewed status cannot validate the present averaging argument. |
| **MPL_14_087-132 M04**; **MPL_14_002-044 M27** | No inclusion of an \(\mathfrak{sl}_2\) group into a motivic group, or naturality action on Lefschetz operators, is established here. |
| **MPL_14_087-132 M23**; **MPL_14_002-044 M28a**; **MPL_15_195-228+18_002-017 M07**; **MPL_15_195-228+18_002-017 S15:** | No Nori–André equivalence, Nori/Ayoub comparison, or period-group comparison is proved or altered. |
| **MPL_14_002-044 M29** | No identification of numerical and homological cycle-class quotients occurs. |
| **MPL_14_087-132 M25** | No finite-object period-torsor formulation or period transcendence statement occurs. |
| **MPL_15_195-228+18_002-017 A17** | No classification of filtered motivic points is supplied. |
| **MPL_15_195-228+18_002-017 A25** | No rigidity theorem for a map to a motivic moduli space is supplied. |
| **MPL_15_195-228+18_002-017 B04** | “Inertia” alone does not connect the present linear averaging with that lead's non-Tate cuspidal criterion; the relevant anabelian hypotheses and conclusion are absent. |
| **MPL_15_195-228+18_002-017 M08** | No fullness or essential-image theorem for Hodge realization is supplied. |
| **MPL_15_195-228+18_002-017 P14** | No section or centrality proof for the Tate character is supplied; twisting in a functional equation is insufficient. |
| **MPL_15_195-228+18_002-017 R12** | The separate reused Lie-algebra generalization is not addressed by the current reused commutative-algebra pages. |
| **MPL_14_002-044 §3**; **MPL_15_195-228+18_002-017 §4** | These are earlier comparison tables; no asserted equivalence of the listed linear and nonlinear programmes follows from the present computations. |
| **MPL_14_002-044 §101**; **MPL_15_195-228+18_002-017 §133**; **MPL_15_195-228+18_002-017 §136** | These concern the earlier package's unverified steps and title/page-count inventories. The current package has its own standing-question inventory; it does not change those earlier records. |
| **MPL_14_002-044 §108**; **MPL_15_195-228+18_002-017 §138**; **MPL_147_048-137 §230**; **MPL_121_049-073+153+155 §141**; **MPL_142_001-093 §316** | Bibliography summaries are finding aids, not mathematical results established by these pages. Their references were not inherited as verified sources. |
| **MPL_33_002-049 §96** | An earlier register-coverage inventory, with no mathematical statement newly proved here. |

### All seven planning entries

| Plan ID | Assessment from the current package |
|---|---|
| **WG2 §2.4 #3** | The present handwritten pages are about local averaging, duality, and functional equations. They do not construct motives from Lefschetz rings or fix the draft's standard-conjecture lettering. |
| **WG H9** | Cote 44's height/intersection formula remains a separate programme. No height pairing or Mordell–Weil lattice formula is derived in 60/037–069. |
| **WG2 §2.3 #2** | No calculation of the integral/rational universal Lefschetz algebra is added. |
| **WG2 §2.3 #7** | No new semisimplicity or nilpotent-kernel theorem for motives is added. |
| **WG2 §2.3 #12** | C05 supplies a useful hypothesis distinction between purity and polarization; it does not prove the stated intermediate-Jacobian or height claims. |
| **WG2 §6. #9** | The requested LEFSCHETZ_RINGS proof/computation programme is not carried out in this excerpt. |
| **WG2 §2.2 #4** | No extension of the hyperplane-section induction for the standard conjectures is supplied. |

## 5. Hua finding: supported scope and necessary qualification

**Identifier:** Hua, findings register, **60-inertia-average-duality**. **Status supplied:** “conjecture (unsearched)”; the intake says new to the project, not verified. The available row is truncated after “plus…”, so its unprovided remainder cannot be audited from this register.

The frozen text supports the broad sequence: inadequacy of the first additive but nonlocal proposal (**60/037**), a normal finite-index inertia subgroup acting unipotently (**039–043**), averaging traces (**045**), a virtual sheaf (**047**), and a virtual duality expression with \(\mu_x\) (**049–051**). It also explicitly distinguishes nonadditivity of \(\alpha_x\) from additivity of \(\mu_x\) (**051**). These are substantial manuscript supports for the lead, but not an automatic endorsement of every inference in its description.

The row's displayed **`(1)[2]` requires qualification**: `[2]` is cancelled on **049**, and the surviving boxed formulas on **051** are virtual. An even shift is invisible in the Grothendieck group; a modern derived formulation with `[2]` may be compatible with the virtual identity, but this package does not construct a canonical derived object or prove that stronger isomorphism. Moreover the conditional devissage test in §2 above may force the proposed correction class to vanish under the usual local interpretation; that question should accompany any endorsement of the finding.

## 6. Questions to preserve without touching the frozen transcription

1. **60/047 versus 051:** determine from earlier/later archive pages whether \(E_\eta(x)\) denotes ordinary invariants, an averaged fibre, or a notation whose meaning was changed during drafting; the frozen text retains the actual collision.
2. **60/049–051:** decide whether additivity of \(\mu_x\) is asserted on the full local representation category or only for globally arising short exact sequences, and then test the devissage consequence.
3. **60/053:** identify the intended self-duality or polarization hypothesis behind the implication from “poids” to \(\check E\simeq E(\rho)\); purity alone does not suffice.
4. **60/057–059:** retain the sign left open and avoid importing the virtual-rank epsilon of 47/008 or the height-pairing sign of 44/004.
5. **60/061:** compare the uncertain displayed connecting index with the cone's long exact sequence in the research notes only; no expected index should overwrite the frozen reading.

All five are research questions about scope or conventions. None licenses changing a letter, sign, or macro in the frozen transcription after the context has been read.
