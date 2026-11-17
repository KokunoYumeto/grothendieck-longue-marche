# Research memo: cote 12, scans 150–168 — motives, duality, positivity, and the supplied comparisons

## Scope and evidential status

This memo was prepared after the transcription freeze, using only the frozen page text, the supplied context, and primary mathematical publications. No manuscript image was inspected, and no page file, combined transcription, doubts file, inventory, or progress log was changed. Proposed changes of reading are segregated at the end as questions.

The complete context/README.md and context/notes/RESULTS_STATE.md were read. The supplied archive transcription and the two same-cote research returns are first-pass, unreviewed witnesses; a claim labelled “Proved” in the register is not independently refereed unless the register explicitly says so. None of the explicitly refereed register results supplies a proof of the motive-category assertions investigated here. The notes below do not re-prove the register's projective-line calculation or its numerical-motive theorem; they identify what these newly supplied pages add and independently check the cited primary results.

Abbreviations used only to keep the metadata readable:

- **CT** = context/MPL_16+47+54+44_transcription.tex; a locator such as CT 16/049 means cote 16, scan 49.
- **CN** = context/MPL_16+47+54+44_notes.md; its note IDs are first-pass research leads, not manuscript text.
- **N15a** = context/same_cote_15/MPL_15_087-138_notes.md.
- **N15b** = context/same_cote_15/MPL_15_195-228+18_002-017_notes.md.
- **RS** = context/notes/RESULTS_STATE.md.
- **Current witness** = pages/MPL_12_150-168+15_002-033_12_scanNNN.tex, with the scan number and, where useful, the local file line numbers.

All notes below contain a proposed paragraph of one to four sentences, preceded by metadata. “Adds,” “restates,” “differs,” and “contradicts” describe the relationship to a specified supplied witness or claim, not a retrospective reconstruction of the whole archive.

## Findings for the planning questions

| Question | Finding from the present witness | Limit |
|---|---|---|
| Is the motive category built from cote 16's Lefschetz rings? | Scans 150–151 now give an actual conditional construction from all homological correspondences; 152–154 add grading and Tate inversion. | No identification with modules over the particular universal ring of CT 16/014–018 appears. |
| Where does semisimplicity enter? | Scan 151 assumes homological = numerical and Hodge positivity; scans 159–165 develop the involution/positive-trace mechanism. | Numerical semisimplicity alone does not provide the stated faithful cohomological realization. |
| Are effective and localized internal Homs identical? | The unrestricted sentence on 156 is false even for the effective Tate category. | This does not invalidate normalized effective duals once suitable rigidity is supplied. |
| Are the “primitive” objects the Lefschetz-primitive cohomology pieces? | Scan 155 defines them by effective Tate divisibility. | They differ already for the middle cohomology of P¹ × P¹. |
| Is Lefschetz sl₂ the motivic Galois group or a natural subgroup? | The correspondence action and the tensor automorphism group have different defining conditions. | The projective-line test is already set out in N15a L03/§111, which retains its first-pass, unreviewed status. |
| Are the manuscript's A–D the printed letters? | Draft A has printed A's algebraic-class content; draft C has printed B's inverse-Lefschetz content. | Draft B/printed D and draft D/printed C are operational parallels, since standalone draft definitions are absent. |
| What does Nori–Ayoub settle? | The specified classical groups are canonically isomorphic over a characteristic-zero field with a fixed complex embedding. | Neither that theorem nor pure Nori/André semisimplicity identifies all motivated correspondences with algebraic cycles. |

## Directly integrable notes

### M01 — An actual conditional construction is now supplied

**Kind:** observation / unpursued implication.  
**Witness and quotation:** 12/150:L27–36; 12/151:L2–18: “les morphismes sont”; “Si on admet”; “D'où une catégorie … M”.  
**Context search:** catégorie, correspondance, Lefschetzien, motif; CT 16/018 defines the Lefschetz correspondence ring and CT 16/049 states the semisimple-motive programme; N15a L01 cites 15/135,137 and N15b M01 cites 15/219 and 18/011.  
**Relation:** **adds** the conditional construction missing from those same-cote excerpts; **does not contradict** their carefully restricted statement that their own excerpts merely used M.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_087-138 L01 and §2 [first-pass leads]; MPL_15_195-228+18_002-017 M01 and §2 [first-pass leads].

Scans 150–151 construct the input category using rational cycles modulo the chosen ℓ-adic homological equivalence and invoke finite-dimensional semisimple correspondence algebras before passing to M. This is substantive new evidence for the category-building programme of cote 16/049. It does not say that M is the category of modules over cote 16's universal Lefschetz ring: the present input includes correspondences between arbitrary smooth projective varieties, whereas that ring encodes particular Lefschetz operators and projectors.

### M02 — The abelian completion needs idempotent splitting and all endomorphism algebras

**Kind:** unproved construction step / literature comparison.  
**Witness and quotation:** 12/151:L5–8 and 12/159:L4: “donc est semi-simple”; “comme catégorie abélienne”.  
**Context search:** semi-simple, catégorie, correspondance; CT 16/049 and CN S14–S15 discuss splitting algebraic injections and the category; N15a L16/Proof A records correspondence categories.  
**Relation:** **adds** the relevant completion mechanism to CT 16/049's programme.  
**RS:** WG2 §2.3 #7 [unchecked plan]; MPL_15_087-138 L16 and §127 [first-pass leads].  
**Primary locator:** Jannsen (1992), Lemma 2, p. 449.

Jannsen's categorical lemma supplies the exact modern criterion: a linear pseudo-abelian category whose every endomorphism algebra is finite-dimensional and semisimple is semisimple abelian. Thus the natural completion here is the idempotent completion of the additive correspondence category; semisimplicity of End(h(X) ⊕ h(Y)) is relevant to morphisms between different objects, not merely the individual rings separately. This makes the manuscript's short passage concrete without claiming that its universal property was completely written out.

### M03 — The rational dimension assertion has a genuine extra hypothesis

**Kind:** observation / scope restriction.  
**Witness and quotation:** 12/151:L5: “l'équiv. hom. = équiv. numérique … dim finie sur Q”.  
**Context search:** finitude, numérique, homologique, dimension; CT 16/044 expressly separates the characteristic-zero rational-dimension argument from the characteristic-p uncertainty; CN S15–S16 and N15a L16.  
**Relation:** **restates** the earlier distinction, now as an explicit hypothesis in the construction.  
**RS:** WG2 §2.3 #7 [unchecked plan]; MPL_15_087-138 L16 and §127 [first-pass leads].  
**Primary locator:** Jannsen (1992), p. 450, discussion following Corollary 1.

Finite-dimensional ℓ-adic cohomology gives an embedding of rational homological classes into a finite-dimensional Qℓ-space, but that observation alone does not bound their Q-dimension. The manuscript explicitly invokes equality with numerical equivalence before claiming rational finite dimensionality, so that assumption should remain attached to the conclusion. This is the same coefficient-field distinction that Jannsen flags on p. 450.

### M04 — Numerical semisimplicity does not remove the manuscript's equivalence assumption

**Kind:** literature comparison / unpursued implication.  
**Witness and quotation:** 12/151:L5,14–20: “équiv. numérique”; “fidèle, par définition … des Hom”.  
**Context search:** Jannsen, numérique, homologique, semi-simple; CT 16/049; CN S15–S16; N15a L16.  
**Relation:** **restates** the modern distinction already present in the context, and **adds** an explicit current-page reason why it matters.  
**RS:** WG2 §2.3 #7 [unchecked plan]; MPL_15_087-138 L16 [first-pass lead].  
**Primary locator:** Jannsen (1992), Theorem 1, p. 448; Corollary 1, pp. 449–450.

Jannsen proves numerical motives semisimple abelian without the standard conjectures; under algebraic Künneth projectors, the homological-to-numerical kernel is nilpotent. Nilpotence is not vanishing. The present realization is faithful because its correspondence relation was defined by that cohomology, so replacing this category by the numerical quotient preserves the stated realization only after the required equivalence comparison.

### M05 — The projectors are additional data, not consequences of a Lefschetz element alone

**Kind:** observation.  
**Witness and quotation:** 12/152:L18–19; 12/153:L2–20: “Nous supposons maintenant”; “on suppose donné”.  
**Context search:** projecteur, graduation, pi_i, Lefschetz; CT 16/016 requires compatibility with the weight projectors, and CT 16/017 explicitly answers “Non” to the proposed reconstruction from L alone.  
**Relation:** **restates** the necessity of grading data and **adds** its categorical implementation.  
**RS:** WG2 §2.3 #2 and WG2 §2.4 #3 [unchecked plans]; MPL_15_087-138 §123 [first-pass lead].

The functorial, orthogonal, finite-support projectors are imposed before the category is graded, and their compatibility with products is imposed separately. This agrees with cote 16/017's explicit rejection of recovering the full structure from L alone. In the geometric application, supplying cohomological Künneth projectors as algebraic correspondences is a further algebraicity requirement, rather than a consequence of the abstract decomposition notation.

### M06 — Künneth compatibility does not by itself fix the symmetry convention

**Kind:** own idea / scope clarification.  
**Witness and quotation:** 12/152:L9–10: “associatif et commutatif”; “donc aux opérations tensorielles”; 12/153:L21: “λ-anneau gradué”.  
**Context search:** commutativité, signe, Künneth, tensor; CT 47/004 contains a geometric Künneth formula, but no corresponding sign convention; N15a L03–L08 concerns tensor-group naturality, not this symmetry issue.  
**Relation:** **adds** a missing convention; no contradiction of a specified convention is alleged.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_087-138 L03, L07 [first-pass leads].  
**Confidence:** high: the flip on two odd cohomology classes is an explicit test.  
**Primary locator:** Jannsen (1992), Corollary 2 proof, pp. 450–451.

Under ordinary cohomological conventions, the geometric interchange of X and Y realizes with the Koszul sign (−1)^{ij} on Hⁱ(X) ⊗ Hʲ(Y). To obtain an ordinary symmetric fibre functor to ungraded vector spaces, the source symmetry is correspondingly modified; Jannsen makes this step explicit. The sentence about tensor operations therefore needs a stated symmetry convention, especially before interpreting the associated λ-operations or a Tannakian group.

### M07 — Tate inversion is a localization with cancellation, not an added geometric theorem

**Kind:** observation / unpursued implication.  
**Witness and quotation:** 12/154:L2–25: “soit pleinement fidèle”; “catégorie pseudo-lim”.  
**Context search:** Tate, effectif, poids, graduation; CT 16/048 explicitly says it drops Tate twists; N15a L02 records the correspondence degree/twist relation; N15b P09 concerns different mixed-Hodge indices on 18/009.  
**Relation:** **adds** explicit formal inversion and **differs** from suppressing twists in the letter.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 §107 [first-pass excerpt only]; MPL_15_195-228+18_002-017 P09 [first-pass lead].

The displayed Hom formula is justified by the preceding full-faithfulness assumption: moving both objects far enough into the effective category does not change their morphism space. It gives a formal category in which Λ(−1) is invertible and its inverse has degree −ρ. It does not prove that a geometric correspondence realizing every desired duality or projector already existed before this localization.

### M08 — Subobjects remain effective because the inclusion is full and idempotents split

**Kind:** own idea / proof of the displayed marginal assertion.  
**Witness and quotation:** 12/154:L26: “Un sous motif d'un motif effectif est effectif”.  
**Context search:** sous motif, effectif, sous-objet, idempotent; CT 16/049 treats algebraic splitting, and N15a L16 distinguishes the numerical quotient; no identical effectivity assertion was located in the supplied full context.  
**Relation:** **adds** the formal reason under the manuscript's semisimple assumptions.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 §107 [first-pass excerpt, full return absent]; MPL_15_087-138 L16 [first-pass lead].  
**Confidence:** high under the stated semisimple, full-faithfulness and idempotent-completion hypotheses.

If an effective object M has a subobject in the localized semisimple category, that subobject is the image of an idempotent of End(M). Full faithfulness puts the same idempotent in the effective category, where its image already exists. This proves the margin in the present framework; it is not a general assertion about arbitrary nonsemisimple effective categories.

### M09 — The niveau decomposition uses semisimplicity

**Kind:** observation / unproved implication made explicit.  
**Witness and quotation:** 12/155: “sous-catégorie épaisse … donc … se décompose canoniquement”.  
**Context search:** niveau, primitif, épaisse, semi-simple; CT 16/009 and 16/033 use primitive pieces for a chosen L; N15b A09 cites the different Hodge-filtration “niveau” formula of 15/205.  
**Relation:** **adds** a category-theoretic decomposition and **differs** from both those uses of primitive/level language.  
**RS:** WG2 §2.3 #2 and WG2 §2.4 #3 [unchecked plans]; MPL_14_002-044 §107 [first-pass excerpt only].  
**Confidence:** high under semisimplicity.

A thick subcategory does not canonically split objects of an arbitrary abelian category, but here semisimplicity separates the relevant simple constituents from all the others. Their sums define the maximal summand of the specified niveau and its canonical complementary summand. The word “donc” thus relies on the semisimple category established conditionally earlier, not on thickness alone.

### M10 — A Tate primitive is not necessarily Lefschetz primitive

**Kind:** own idea / counterexample to a possible identification.  
**Witness and quotation:** 12/155: “motifs primitifs de niveau j”; the definition excludes nonzero submotives obtained by the specified effective Tate twist.  
**Context search:** niveau, primitif, primitive; CT 16/009 and 16/033 define polarization-dependent primitive cohomology; N15b A09, witness 15/205, warns that its own level index is not fixed.  
**Relation:** **differs** from CT's Lefschetz-primitive decomposition; **contradicts** an unqualified identification of these two meanings, not an explicit manuscript claim that they coincide.  
**RS:** WG2 §2.3 #2 and WG2 §2.4 #3 [unchecked plans]; MPL_14_002-044 §107 [first-pass lead].  
**Confidence:** high: the intersection calculation is explicit and uses only Tate motives.

On X = P¹ × P¹, write a and b for the two ruling classes and take the polarization a + b; then a² = b² = 0 and (a + b)(a − b) = 0, so a − b is Lefschetz primitive in H²(X). Nevertheless its motive is Q(−1), and therefore has niveau 0 in scan 155's convention with ρ = 2. Thus the categorical “primitive of niveau 2” excludes this Tate summand, although the usual primitive cohomology includes it.

### M11 — The primitive tensor functors describe an operation, with coherence still required

**Kind:** own idea / scope clarification.  
**Witness and quotation:** 12/155: “La structure multiplication … est connue quand on connaît les foncteurs” θ^{i,j,k}.  
**Context search:** produit, tensor, primitif, graduation; CT 16/014–018 concerns graded correspondence rings and N15a L04–L08 concerns grading/tensor compatibility.  
**Relation:** **adds** a distinction between the tensor bifunctor and its full symmetric monoidal structure.  
**RS:** WG2 §2.3 #2 and WG2 §2.4 #3 [unchecked plans]; MPL_15_087-138 L07 [first-pass lead].  
**Confidence:** high; ordinary and Koszul symmetries give the same underlying graded tensor bifunctor.

The θ-functors recover the primitive summands of a tensor product and therefore encode the underlying additive bifunctor once the decomposition is fixed. A complete symmetric monoidal structure also includes compatible associativity, unit and commutativity constraints. Ordinary and Koszul commutativity on graded vector spaces already show why those constraints are not determined merely by the summand functors.

### M12 — The normalized effective dual and the ordinary dual have different weights

**Kind:** observation / literature comparison.  
**Witness and quotation:** 12/156: “M* = Hom(M, Λ(−i))”; 12/157: “check M = Hom(M, Λ(0))”.  
**Context search:** dualité, dual, Hom, twist; CT 16/048 calls H^{2n−i}(X) a natural dual while explicitly omitting twists; N15a L02 identifies the role of twists.  
**Relation:** **adds** the exact two-dual distinction suppressed in CT 16/048.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_087-138 §123 [first-pass lead]; MPL_15_195-228+18_002-017 P09 [first-pass lead, concerning a different twist formula].  
**Primary locator:** Deligne and Milne (1982/2012), §1.6, formula (1.6.10), and Definition 1.7, pp. 8–10.

For ρ = 2, set L = Λ(−1); in a rigid category the two constructions are related by M* = M∨ ⊗ Lⁱ for M of degree i. Hence M* has degree i, whereas the ordinary dual M∨ has degree −i. The effective existence of the former is a separate condition, and it should not be confused with effective existence of the latter.

### M13 — The stated preservation of effective internal Hom has a Tate counterexample

**Kind:** own idea / counterexample to an unrestricted written assertion.  
**Witness and quotation:** 12/156: “si Hom(M,N) existe dans M, il existe aussi dans M-hat et est le même”.  
**Context search:** Hom, effectif, Tate, dualité; CT 16/048 supplies the omitted-twist comparison and N15a L02 the twist bookkeeping; no effective-to-localized internal-Hom preservation theorem occurs in the supplied context.  
**Relation:** **adds** a new test and **contradicts** the sentence if read for arbitrary effective M,N.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 §107 [first-pass excerpt on effectivity, full text absent]; no reviewed register result establishes the disputed preservation statement.  
**Confidence:** high: this is an explicit calculation in the manuscript's own Tate/weight setting.

For the effective Lefschetz object L of degree 2, the restricted functor P ↦ Hom(P ⊗ L, 1) is zero on every effective P, so its effective internal Hom is represented by 0. After Tate inversion, Hom-internal(L,1) is L⁻¹, because L⁻¹ ⊗ L ≅ 1, and is nonzero. Thus existence of the effective representing object does not imply preservation by localization; the zero object represents the restricted functor but is not a realization-compatible dual of L.

### M14 — Representability alone does not justify the following “easy verification”

**Kind:** own idea / countermodel to an implication from the stated abstract axioms.  
**Witness and quotation:** 12/156: “Hom(M,N(−i)) ≃ M* ⊗ N”; “vérification facile”.  
**Context search:** Hom, dualité, catégorie, effectif; CT 16/018 proposes a ring duality, CT 16/048 proposes algebraic complementary-degree isomorphisms; neither supplies the needed abstract rigidity.  
**Relation:** **adds** a missing hypothesis; **contradicts** a deduction from mere representability, not the formula in a rigid motive category.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 §107 [first-pass excerpt only].  
**Confidence:** high for the countermodel; its relevance is restricted to the explicit axioms before the later positive-pairing assumptions.  
**Primary locator:** Deligne and Milne (1982/2012), Definition 1.7 and (1.6.10), pp. 8–10.

Take finite N²-graded Q-vector spaces with degree a + b, the usual tensor product, and L of bidegree (2,0); this category is semisimple, has the required grading and faithful tensor realization, and tensoring with L is fully faithful. Every restricted internal Hom exists, but for the one-dimensional M of bidegree (0,1), M* = [M,L] = 0 while [M,M ⊗ L] = L. Consequently the claimed formula requires genuine duality or an equivalent nondegeneracy condition in addition to representability, as reflected in the separate rigidity axiom of Deligne–Milne.

### M15 — The mono/epi question is settled once a genuine finite dual exists

**Kind:** self-flagged implication / own clarification.  
**Witness and quotation:** 12/157:L9–16: the correction from “injectif” to “épim.” and the marginal “?”.  
**Context search:** dualité, mono, épimorphe, inverse; CT 16/049 asks for algebraic left and right inverses; CN S14 explains the semisimple block argument.  
**Relation:** **adds** the duality condition needed for this current-page statement.  
**RS:** WG2 §2.4 #3 and WG2 §2.3 #7 [unchecked plans]; MPL_15_087-138 L16 [first-pass lead].  
**Confidence:** high once M* realizes as the finite-dimensional dual with its Tate normalization.

A nondegenerate finite duality exchanges monomorphisms with epimorphisms, so the inserted correction is the expected variance. For M = N, the two realizations have the same finite dimension, and an injective or surjective map M → M* is therefore an isomorphism under the exact faithful realization. This answers the marginal question under genuine duality, without deriving that duality from the insufficient representability premise of scan 156.

### M16 — The self-adjoint condition is the same-parity condition

**Kind:** self-flagged implication / algebraic clarification.  
**Witness and quotation:** 12/158:L20–32: “u'' = A⁻¹u'B”; “autoadjoint (?)”.  
**Context search:** symétrie, involution, transposé, dualité; CT 16/018 discusses transposition/opposite-ring duality, while CT 16/049 invokes positivity; no identical change-of-form formula was located there.  
**Relation:** **adds** the exact criterion underlying the final question mark.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 B03 [first-pass lead, 15/203,215,217 polarizations].  
**Confidence:** high; substitute α₁(x,y) = α(Ax,y) in the symmetry equation.  
**Primary locator:** Deligne and Milne (1982/2012), (4.3.6)–(4.3.7), pp. 37–38.

If α and α₁ are nondegenerate forms of the same symmetric or alternating parity, the unique A defined by α₁ = α ∘ (A ⊗ 1) is invertible and α-self-adjoint. The written conjugation formula then follows directly from the definition of adjoint. Self-adjointness does not by itself imply positivity: the latter is the additional positive-cone condition tested on scan 163.

### M17 — Positive trace is the semisimplicity mechanism

**Kind:** literature comparison.  
**Witness and quotation:** 12/159:L4; 12/161:L29–36: “algèbres de Riemann”; Tr(u'u) ≥ 0 with equality only for zero.  
**Context search:** semi-simple, Hodge, positif, index; CT 16/049 explicitly asks for C(X) plus I(X × X) to imply semisimplicity, and CN S14–S16 discusses that mechanism.  
**Relation:** **adds** an abstract axiomatic implementation of the earlier request.  
**RS:** WG2 §2.3 #7 and WG2 §2.4 #3 [unchecked plans]; MPL_15_087-138 L16 [first-pass lead].  
**Primary locator:** Kleiman (1968), Theorem 3.11, Corollary 3.12 and Lemma 3.13, pp. 380–381.

Kleiman's positive-involution criterion proves the finite correspondence algebra semisimple from the positive trace form, matching the mechanism asserted here. The algebra must be stable under the relevant adjoint, and the positivity hypothesis must apply to its nonzero elements. This is the conditional cohomological route of cote 16/049, distinct from merely taking the numerical quotient.

### M18 — Positivity on mixed Hom spaces selects compatible forms

**Kind:** own idea / clarification by counterexample.  
**Witness and quotation:** 12/161:L29–36; 12/163:L19–32: “Tr uu'A”; “A est dans le cône positif”.  
**Context search:** positif, polarisation, transposé; CT 16/049 concerns a positive involution; CN S14 and N15a T07–T09 concern polarizations and their compatibility.  
**Relation:** **adds** why the manuscript's two-form axiom is stronger than a separate positive involution on each End space.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 B03 [first-pass lead].  
**Confidence:** high: replacing a form by its negative leaves its own adjoint unchanged but reverses the mixed trace test.  
**Primary locator:** Deligne and Milne (1982/2012), definition of compatible Weil forms and Proposition 4.6(d), p. 38.

The forms α and −α give the same involution on End(M), so endomorphism-trace positivity alone cannot distinguish their signs. In the mixed Hom test with source form α, target form −α and u = id, the adjoint is −id and the trace is negative for a nonzero realization. This explains why the two-form positivity axiom on 161, rather than separate positive involutions, is what forces the positive cone on 163.

### M19 — The possible redundancy of degree-zero normalization has a conditional proof

**Kind:** own idea addressing a self-flagged step.  
**Witness and quotation:** 12/161:L19–27: “définies positives”; the uncertain phrase “Sans doute on le supprimera”; compare 12/153:L22.  
**Context search:** positif, unité, normalisation, polarisation; CT 16/049 concerns trace positivity; N15a T07–T09 treats choices of polarization; no proof of this exact degree-zero redundancy was found.  
**Relation:** **adds** a proof under explicit hypotheses; the uncertain phrase is not assigned a repaired grammatical reading.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 B03 [first-pass lead].  
**Confidence:** high for the scalar argument; medium for attaching it to the uncertain cancellation phrase.

Assume the family on the tensor unit is nonempty and nondegenerate: if its scalar form is a, tensor stability supplies a², and mixed positivity for id from the form a to the form a² forces a > 0. Since degree-zero objects are finite sums of the unit, applying mixed positivity to all maps 1 → h⁰(X) then proves positive definiteness of the forms on h⁰(X). Thus the degree-zero normalization follows under these explicit hypotheses, which should be stated before treating the tentative deletion as justified.

### M20 — Restriction to a summand and independence of embedding require nondegenerate restriction

**Kind:** unproved step / own clarification.  
**Witness and quotation:** 12/165:L4–12,30–36: “Choisissons un hom injectif”; “μ'μ = id”; “OK !”.  
**Context search:** injection, inverse, positif, dualité; CT 16/049 and CN S14 treat algebraic splitting; N15a L16 distinguishes numerical and homological categories.  
**Relation:** **adds** the positive-form normalization needed for the trace calculation.  
**RS:** WG2 §2.3 #7 and WG2 §2.4 #3 [unchecked plans]; MPL_15_087-138 L16 [first-pass lead].  
**Confidence:** high under positive, realization-compatible forms and semisimplicity.

Restriction of a positive form to a subobject is nondegenerate, and with the induced form the inclusion is an isometry whose adjoint is a retraction. These are the conditions that make λ'λ = μ'μ = id and justify the displayed cyclic-trace computation. Without nondegeneracy of the restricted forms, a splitting in the underlying semisimple category alone would not identify an arbitrary retraction with the adjoint.

### M21 — Tate compatibility is an explicit extra normalization

**Kind:** self-flagged implication / scope clarification.  
**Witness and quotation:** 12/167:L7–22: “il y a lieu de vérifier”; “la forme canonique 1”.  
**Context search:** Tate, normalisation, polarisation, forme; CT 16/048 suppresses twists; N15a L02 and T18 concern their formal role; N15b P09 concerns a separate mixed-Hodge twist convention.  
**Relation:** **adds** a positivity normalization for the Tate line, beyond the formal Hom identifications.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 P09 and B03 [first-pass leads].

The displayed isomorphism of bilinear-form spaces does not by itself identify the selected positive classes. Tensor stability reduces that issue to placing the canonical form on Λ(−1) in the chosen class, exactly as the manuscript says. The geometric verification is asserted rather than supplied on this page, so the extension to non-effective motives remains conditional on this stated normalization.

### M22 — The Lefschetz action is not automatically a tensor automorphism action

**Kind:** contextual comparison / scope restriction.  
**Witness and quotation:** 12/152:L9–10; 12/153:L13–21, tensor structure and grading.  
**Context search:** sl₂, Lefschetzien, correspondance, Tate; CT 16/014–018 constructs operator rings; N15a L03 and §111 already give the projective-line naturality obstruction.  
**Relation:** **restates** the explicit obstruction proposed in that first-pass note and **adds** its relevance to the newly explicit tensor structure.  
**RS:** WG2 §2.3 #2 and WG2 §2.4 #3 [unchecked plans]; MPL_15_087-138 L03 and §111 [first-pass leads, direct calculation in the supplied note].  
**Primary locator:** Beauville (2008), §1.1 and Theorem 3.3, pp. 2 and 6–7.

An operator induced by an algebraic correspondence and an element of Aut⊗(T) satisfy different conditions: the latter must act naturally on every object and respect the unit and all tensor products. N15a's projective-line calculation already rules out identifying the specified Lefschetz action with such a natural subgroup action. Beauville's precise modern analogue lands in the group of invertible correspondences, which supports that comparison without identifying it with the motivic Galois group.

### M23 — The Cartan grading has an object-dependent shift

**Kind:** literature comparison / exact operator distinction.  
**Witness and quotation:** 12/153:L13–20, additive tensor weights.  
**Context search:** poids, graduation, sl₂, Cartan; CT 16/014–018; N15a L04–L08, especially L07's Beauville comparison.  
**Relation:** **restates** N15a L07 and **adds** a direct comparison with the present weight axioms.  
**RS:** WG2 §2.3 #2 and WG2 §2.4 #3 [unchecked plans]; MPL_15_087-138 L07 [first-pass lead].  
**Primary locators:** Beauville (2008), Theorem 3.3 and proof, pp. 6–7; Deligne and Milne (1982/2012), Definition 5.1, p. 48.

Beauville's Cartan operator on a g-dimensional abelian variety is Σ(i − g)πᵢ, and his diagonal torus is t⁻ᵍΣtⁱπᵢ. By contrast, the functorial tensor grading in scan 153 acts with degree i; in a Tannakian formulation it gives a central grading cocharacter. The factor t⁻ᵍ identifies the exact shift but is not a single global replacement for the weight grading on every motive and all its subobjects.

### M24 — The standard-conjecture letters must be aligned by content

**Kind:** contextual comparison / reading safeguard.  
**Witness and quotation:** 12/151, equivalence and Hodge hypotheses; 12/152–153, projector hypotheses; no A–D letters occur in these current passages.  
**Context search:** A(X), B(X), C(X), D(X), conjecture, inverse, projecteur; CT 16/040,042,044–050; CN S1; N15a L09–L10 and its lettering table; N15b introductory lettering table.  
**Relation:** **restates** the secure and provisional matches; the current pages **add** separated hypotheses but do not supply missing draft definitions.  
**RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_087-138 §2 and §127, MPL_15_195-228+18_002-017 §2 and §138 [first-pass leads].  
**Primary locators:** Grothendieck (1969), §3, p. 196; Kleiman (1968), §§2, 2.3, 2.9, 3.6 and 3.9, pp. 369–371,379–380.

Draft A has the algebraic-class Lefschetz content of printed A, while draft C has the inverse-operator content of printed B. The A-plus-index comparison aligns draft B with printed D, and the projector/characteristic-polynomial criterion aligns draft D with printed C, but these latter matches remain provisional because the supplied letters do not independently define draft B and D. Scans 151–153 should therefore be cross-referenced by their explicit equivalence, positivity and projector hypotheses, not assigned manuscript letters retrospectively.

### M25 — S15: the Nori–Ayoub result has fixed field, realization and coefficient data

**Kind:** literature comparison.  
**Witness and quotation:** 12/150–152, universal factorization and realizations.  
**Context search:** Nori, Ayoub, S15, universel, realization; CT 16/049 is the earlier motive-category programme; N15a T23/S15 and N15b M07/S15 contain the modern comparison leads.  
**Relation:** **restates** the theorem with checked scope and **differs** from the manuscript's conditional homological-correspondence construction.  
**RS:** MPL_15_087-138 S15: and MPL_15_195-228+18_002-017 S15:, M07 [first-pass leads]; WG2 §2.4 #3 [unchecked plan].  
**Primary locator:** Choudhury and Gallauer Alves de Souza (2017), conventions p. 5 and Theorem 9.1, p. 41 of arXiv v3.

For a characteristic-zero field with a fixed embedding into C, Choudhury and Gallauer construct mutually inverse Hopf-algebra maps comparing Nori's and Ayoub's classical motivic Galois groups; their theorem allows principal-ideal-domain coefficients, including Q. This is a comparison of those specified constructions and compatible Betti realizations. It does not identify the current homological-correspondence category with either one or by itself construct a motivic t-structure.

### M26 — Pure Nori/André semisimplicity leaves an algebraic-cycle comparison

**Kind:** literature comparison / unpursued implication.  
**Witness and quotation:** 12/151:L5–20; 12/159:L4: conditional semisimplicity and faithful realization.  
**Context search:** Nori, André, motivated, algebraic, semi-simple; CT 16/049; N15a T24/S15 and N15b M07/S15.  
**Relation:** **restates** the modern pure-category theorem and **adds** the comparison now exposed by the explicit current definition of morphisms.  
**RS:** MPL_15_087-138 S15:, MPL_15_195-228+18_002-017 M07 and S15: [first-pass leads]; WG2 §2.3 #7 and WG2 §2.4 #3 [unchecked plans].  
**Primary locator:** Arapura (2013), Theorem 6.3.3, Corollary 6.3.4 and Theorem 6.4.1, pp. 57 and 60 of arXiv v4.

Arapura proves the rational pure Nori category semisimple and equivalent to André's motivated category. To identify it with the present correspondence construction, one must still compare algebraic homological classes with motivated classes: the natural inclusion A_homʳ(X) ⊂ A_motʳ(X) is not made surjective by that theorem. This is a concrete remaining algebraicity issue, not an objection to the proved Nori–Ayoub or pure Nori–André comparisons.

### M27 — Faithfulness, fullness and neutrality are separate questions

**Kind:** observation / scope clarification.  
**Witness and quotation:** 12/151:L16–20 and 12/152:L2: “exact fidèle”; “de Hodge, de … De Rham … de Betti”.  
**Context search:** fidèle, pleinement, Hodge, Betti, foncteur; CT 16/044 discusses Betti comparison; N15b M08, witnesses 15/213,215, explicitly asks about full faithfulness and the essential image.  
**Relation:** **differs** from the later fullness questions by asserting only faithfulness; **adds** the coefficient-field qualification for reconstruction.  
**RS:** MPL_15_195-228+18_002-017 M08 and P01 [first-pass leads]; MPL_15_087-138 S15: [first-pass lead]; WG2 §2.4 #3 [unchecked plan].  
**Primary locators:** Deligne and Milne (1982/2012), Theorem 2.11 and Definition 2.19, pp. 20,24; Arapura (2013), §7.1.

A faithful realization need not be full, so scan 152 does not answer the later Hodge-fullness or essential-image questions. Moreover Tℓ is Qℓ-valued while the motive category is Q-linear; its existence gives a fibre over Qℓ, not automatically a Q-valued neutralization. Ordinary neutral Tannakian reconstruction also requires the appropriate rigid symmetric tensor structure, in addition to exactness and faithfulness.

## Separate reading questions — no proposed transcription changes

### RQ1 — The final letter in the faithfulness criterion

**Witness:** 12/150:L23, frozen as “M|H soit fidèle”.  
**Context searched:** fidèle, conservatif, universel; CT 16/049; N15a L01 and N15b M01; no matching earlier sentence found.  
**Relation and RS:** adds a question to WG2 §2.4 #3 [unchecked plan]; the letters remain unresolved.

Does the letter designate H or M, and which universal completion is assumed in this preliminary paragraph? Faithfulness on a generating additive category extends to its idempotent completion, but it does not automatically extend through arbitrary abelian envelopes: localization from finitely presented Q[t]-modules to Q(t)-vector spaces is exact and faithful on finite free modules yet kills Q[t]/(t). This is a question about the hypotheses and the frozen letter, not a proposed choice between its two readings.

### RQ2 — Tate signs are not harmonized

**Witness:** 12/153:L24; 12/154:L3,13–16; 12/155 and 12/157 uncertain twist signs.  
**Context searched:** Tate, poids, graduation; CT 16/048; N15a L02; N15b P09, witness 18/009.  
**Relation and RS:** adds a reading question; MPL_15_195-228+18_002-017 P09 [first-pass lead] is a related convention problem, not evidence selecting these signs.

The frozen notation starts by fixing Λ(−1) but then writes M(1) = M ⊗ Λ(1), while the following page discusses full faithfulness of M ↦ M(−1). The mathematical comparisons in this memo explicitly choose L = Λ(−1) of positive degree, but that normalization must not be used to alter the diplomatic reading or resolve any uncertain sign.

### RQ3 — The primitive projection has a total-degree index to check

**Witness:** 12/155, margin θ^{ijk}(M,N) = κ_{i,k}(M ⊗ N)(k).  
**Context searched:** niveau, primitive, κ, projection; CT 16/009,033; N15b A09 at 15/205.  
**Relation and RS:** adds a reading/type-check question to WG2 §2.3 #2 and §2.4 #3 [unchecked plans].

If κ_{r,k} denotes the kth niveau summand of an object of degree r, then M ⊗ N has total degree i + j, making the displayed first index a point to re-examine. The text is retained exactly; the type check supplies a question for the next visual review, not a corrected subscript.

### RQ4 — Nonemptiness and nondegeneracy of the families

**Witness:** 12/161:L2–9, “un ensemble Φ_X de formes fondamentales”.  
**Context searched:** forme, polarisation, non dégénérée; CT 16/049; N15a T07–T09 and N15b B03.  
**Relation and RS:** adds a hypothesis question; WG2 §2.4 #3 [unchecked plan], MPL_15_195-228+18_002-017 B03 [first-pass lead].

Are nonemptiness and nondegeneracy already intended by “formes fondamentales” from preceding pages? Empty families would make the closure and mixed-positivity implications vacuous, while adjoints and the degree-zero argument require nondegenerate forms. No additional adjectives are inserted into the source.

### RQ5 — Diagram arrows and the trace identities

**Witness:** 12/165:L15–35, diagram and λ'λ = μ'μ = id.  
**Context searched:** injection, inverse, transposé; CT 16/049 and CN S14.  
**Relation and RS:** adds a diagram-reading question to WG2 §2.4 #3 [unchecked plan].

The surrounding prose chooses inclusions from M into the ambient cohomological motives, whereas the frozen diagram directs the paired arrows toward M. The trace computation distinguishes each inclusion from its adjoint retraction, so the arrowheads and prime marks should be reviewed separately from the algebraic argument. This memo does not reverse an arrow.

## Search record and boundaries

Searches covered the full CT and CN files, both N15 files, all current cote-12 page fragments, and the entire RS. They used the following families:

- Construction: catégorie, category of motives, motif, correspondance, Lefschetzien, universel, fidèle, conservatif.
- Lefschetz and grading: Lefschetz, sl₂, sl_2, Cartan, poids, graduation, projecteur, pi_i, primitif, niveau.
- Duality: Hom, internal, dual, dualité, effectif, Tate, sous-objet, épaisse, twist.
- Positivity: semi-simple, Riemann, Castelnuovo, Hodge, index, positif, polarisation, involution, transposé, symétrie.
- Modern comparisons: Jannsen, Nori, Ayoub, André, motivated, S15, Hodge fullness.
- Lettering: A(X), B(X), C(X), D(X), conjecture, inverse, characteristic polynomial.

The only CT occurrences of “niveau” were ordinary prose about Chern characters, not the categorical niveau of scan 155. The CT primitive matches are specifically 16/009 and 16/033. The supplied full context contains no theorem that effective internal Homs survive Tate inversion unchanged. The full cote-14 return mentioned by RS §107 is absent; its truncated status entry is not used as a proof or as a source of readings.

The reused typed pages 12/160,162,164,166,168 concern Brauer-theoretic material and were excluded from motive claims. Their source identification and any mathematical issues in that text belong to the parent's separate reused-sheet work. The parent also handles periods, arithmetic quotients, linear/nonlinear bridge tables, title sheets and the complete self-flagged index.

## Primary references and checked locators

Only primary mathematical publications or author versions were used for the substantive literature comparisons. Existing notes supplied leads; the indicated primary statements were checked independently. Bibliographic entries below are APA style; page numbers for preprints are their printed internal numbers.

**Arapura, D. (2013).** An abelian category of motivic sheaves. *Advances in Mathematics, 233*, 135–195. https://doi.org/10.1016/j.aim.2012.10.004  
Checked author version: [arXiv:0801.0261v4](https://arxiv.org/pdf/0801.0261), dated October 9, 2012. Theorem 6.3.3 and Corollary 6.3.4, p. 57; Theorem 6.4.1, p. 60; §7.1. The definition of motivated cycles and the comparison construction begin on p. 60.

**Beauville, A. (2008).** *The action of SL₂ on abelian varieties* [Preprint]. arXiv. https://arxiv.org/abs/0805.1541  
Checked [v1 PDF](https://arxiv.org/pdf/0805.1541), dated May 11, 2008: §1.1, p. 2, defines correspondence composition and its realization action; Theorem 3.3 and proof, pp. 6–7, give the group morphism, Cartan image and diagonal torus. This memo uses that inspected version rather than assigning unverified journal pagination.

**Choudhury, U., & Gallauer Alves de Souza, M. (2017).** An isomorphism of motivic Galois groups. *Advances in Mathematics, 313*, 470–536. https://doi.org/10.1016/j.aim.2017.04.006  
Checked [arXiv:1410.6104v3](https://arxiv.org/pdf/1410.6104), dated May 18, 2017: introduction pp. 2–3; conventions p. 5; Theorem 9.1, p. 41. The latter states that the constructed Hopf maps are inverse isomorphisms for PID coefficients.

**Deligne, P., & Milne, J. S. (1982).** Tannakian categories. In P. Deligne, J. S. Milne, A. Ogus, & K.-Y. Shih, *Hodge cycles, motives, and Shimura varieties* (Lecture Notes in Mathematics, Vol. 900, pp. 101–228). Springer.  
Checked [corrected author text](https://www.jmilne.org/math/xnotes/tc.pdf), dated August 15, 2012, retaining original section/theorem numbering: §1.6 and Definition 1.7, pp. 8–10; Theorem 2.11, p. 20; Definition 2.19, p. 24; (4.3.6)–(4.3.7), pp. 37–38; compatibility of Weil forms and Proposition 4.6(d), p. 38; Definition 5.1, p. 48. These are formal categorical comparisons, not a claim that the manuscript already supplied all their axioms.

**Grothendieck, A. (1969).** Standard conjectures on algebraic cycles. In *Algebraic geometry: International Colloquium, Tata Institute of Fundamental Research, Bombay, 1968* (pp. 193–199). Oxford University Press.  
Primary text: [StandardConjs.pdf](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf). Checked the indexed text of §3, p. 196, stating A(X)(a),(b) and B(X). The direct PDF exposed no text lines; a focused primary-domain query exposed the definitions. No manuscript-image reading was used.

**Jannsen, U. (1992).** Motives, numerical equivalence, and semi-simplicity. *Inventiones Mathematicae, 107*, 447–452. https://doi.org/10.1007/BF01231898  
Checked [institutional primary PDF](https://epub.uni-regensburg.de/26642/1/jannsen10.pdf): Theorem 1, p. 448; Lemma 2, p. 449; Corollary 1 and the coefficient-field qualification, pp. 449–450; Corollary 2 and the sign modification, pp. 450–451. The nilpotence statement is Corollary 1, not a “Theorem 2”.

**Kleiman, S. L. (1968).** Algebraic cycles and the Weil conjectures. In *Dix exposés sur la cohomologie des schémas* (pp. 359–386). North-Holland.  
Checked [primary PDF](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf): §2 and 2.3, pp. 369–370; Theorem 2.9, p. 371; Proposition 3.6, p. 379; §3.9, p. 380; Theorem 3.11, Corollary 3.12 and Lemma 3.13, pp. 380–381. These locate the printed letters and the positive-involution route to semisimplicity.

## Register impact

The most substantial addition to WG2 §2.4 #3 is now direct evidence for the conditional construction in cote 12/150–154, accompanied by explicit distinctions between the correspondence input, the Lefschetz operator subring and tensor reconstruction. M13 and M14 identify two new, narrowly scoped formal problems in scan 156; M10 prevents conflating its neighbouring categorical primitive decomposition with cote 16's polarization-dependent one. M19 offers a conditional proof of one tentative normalization simplification.

The following earlier findings are restated with new witnesses or checked primary scope, not promoted to newly proved archive-wide conclusions: numerical semisimplicity and the nilpotent-kernel distinction; the projective-line obstruction to the proposed Lefschetz subgroup; Beauville's shifted grading; the provisional A–D alignment; Nori–Ayoub group comparison; pure Nori/André semisimplicity. No open tower/normalizer or finite-category register problem is solved or changed by this memo.
