# Research contribution: abstract motives, Lefschetz operators, and Galois questions

Prepared after the transcription freeze; no page file, combined transcription, doubts, or inventory was modified. This is a research working record for incorporation in the final notes, not an independent transcription. The source references below use **CT** = `context/MPL_16+47+54+44_transcription.tex`, **CN** = `context/MPL_16+47+54+44_notes.md`, **Hua** = `context/hua_project/12.modern.tex`, and **RS** = `context/notes/RESULTS_STATE.md`; the full filenames are fixed by these definitions. CT and CN are first-return claims, Hua is an AI-produced modernization credited to Michel Hua's project, and RS entries remain at their stated status.

## Principal answers and evidence boundaries

| Requested question | Finding from the frozen selection and supplied context |
|---|---|
| Is the category constructed from cote 16's Lefschetz correspondence rings? | Scans 12/143–149 supply the abstract categorical step: split idempotents in an additive category with finite-dimensional semisimple endomorphism algebras, then extend the tensor product. They do not identify the starting category with cote 16's rings, supply Lefschetz operators, choose an equivalence relation on cycles, or construct the geometric correspondence category. CT 16/018 and 049 make the structural connection; Hua's next subsection, “L'exemple des variétés (pages 149 à 151),” describes the geometric application beyond our last supplied scan (his page 149 corresponds to scan 150). |
| Is the Lefschetz sl₂ inside the motivic Galois group, with its grading as the weight cocharacter? | Not in general, and not as an identification of those two gradings. The Lefschetz operators are degree-changing correspondences after the appropriate Tate twists; tensor automorphisms must preserve the unit and the motivic weight decomposition. The projective-line test already recorded in RS, MPL_14_087-132 M04 and MPL_15_087-138 §111, distinguishes them immediately. |
| What do manuscript A–D mean? | No definitions occur in this selection. CT 16/044–050 securely supports draft A ≈ printed A (Lefschetz on algebraic classes) and draft C = printed B (algebraicity of inverse Lefschetz operators); draft B ≈ printed D and draft D ≈ printed C are plausible operational identifications, but the supplied witness does not give their standalone definitions. CN §S1 explicitly retains that limit; RS points to the absent 14/117 notation table, MPL_14_087-132 M01. |
| Does cote 14 resume the singular-hypersurface programme of 16/047? | Not decidable from these supplied primary manuscript pages. The selected cote 12 leaves do develop weights/cohomology for singular and nonproper varieties, which is related background, but that is not a witnessed resumption in cote 14 of reformulating the standard conjectures for singular hypersurfaces. |
| His exact sequence over Q? | No such displayed sequence occurs in 12/099–149. Hua's early subsections describe the Artin quotient and a conditional identification of the component group, not a new witness from this selection; a modern exact sequence can be stated separately with its descent and fibre-functor hypotheses. |
| A statement of the period conjecture? | None found in the frozen selection, nor in the full Hua reading under “period/périod/transcendance” searches. RS MPL_18_018-062 §2 points to 18/059, “conjecture de transcendance N° 1,” as an earlier return's lead; the underlying scan is not provided here and is not independently verified. |

## Note register: one item per mathematical or documentary issue

### M01 — The universal target has a categorical qualification

**Witness:** cote 12, scan 144, final two displays; scan 145, opening continuation. **Kind:** unpursued implication / qualification. **Quotation:** “soit bijective”; “ou le cas échéant”; “une équivalence de catégories”. **Context search:** `universel|équivalence|catégorie|projecteur` → Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”; CT 16/049; CN §S15. **Relation:** adds the actual categorical construction to the earlier semisimplicity programme; agrees with Hua's categorical formulation. **RS:** bears on WG2 §2.4 #3 (unchecked plan), MPL_11_043-058+56 N031 (first-pass lead), and MPL_15_087-138 L01 (first-pass lead).

The manuscript places an equivalence-of-functor-categories formulation after its bijection formulation with “ou le cas échéant”, and associates these with uniqueness up to isomorphism and up to equivalence respectively. The categorical formulation is appropriate for the later extension by images of idempotents, because a choice of split image is unique only up to canonical isomorphism. This is a qualification or alternative formulation in 12/144–145, not a clearly documented withdrawal of the first version, and it does not prove existence before the additional hypotheses are imposed.

### M02 — Additivity must include finite biproducts

**Witness:** cote 12, scan 144, deleted bracket; scans 145–148. **Kind:** reading question / own hypothesis check. **Quotation:** deleted “On ne suppose pas qu'il existe un objet nul”; scan 148 “R=P×Q”. **Confidence:** high for the counterexample, since its additive hull has a triangular matrix endomorphism algebra with nonzero square-zero radical. **Context search:** `additive|sommes|projecteur|catégorie` → Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”; CT 16/017 (grading/projector requirement) and 16/018 (ring definition); CN §S5. **Relation:** adds a hypothesis check absent from the single-ring discussion. **RS:** WG2 §2.4 #3 (unchecked plan); MPL_11_043-058+56 N031 (lead).

The proof later requires biproducts, so its starting “additive” category must have finite biproducts, or must first receive its finite additive hull. A merely preadditive category with individually semisimple endomorphism rings need not satisfy the claimed conclusion: two objects with endomorphism ring Q and a nonzero one-way Hom form a counterexample once the missing sum is noticed. The deleted bracket on 144 is consistent with adopting actual additivity, but this is a hypothesis of the reconstruction, not a silent expansion of the frozen word.

### M03 — Why deleting a separate Hom-finiteness hypothesis is harmless here

**Witness:** cote 12, scan 145, lines 14–18. **Kind:** unpursued implication. **Quotation:** deleted “Fl(X,Y) sont des vectoriels de dim finie”; retained “Fl(X,X) ... de dim finie ... semi-simple”. **Context search:** `dimension finie|Hom|semi-simple` → CT 16/049; CN §S14; Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”. **Relation:** adds a categorical explanation to CT's one-object endomorphism discussion and supports Hua's final hypothesis list. **RS:** WG2 §2.3 #7 and WG2 §2.4 #3 (unchecked plans).

Assuming finite biproducts, Hom(X,Y) is the matrix corner e_Y End(X⊕Y)e_X, so finite-dimensionality of every endomorphism algebra already implies finite-dimensionality of every Hom. The deletion therefore removes a redundant condition under that interpretation of additivity. It does not justify dropping finiteness of endomorphism algebras, which is used again for the chain condition.

### M04 — The quotient definition is the usual corner construction

**Witness:** cote 12, scan 145, paragraph defining morphisms. **Kind:** unpursued implication. **Quotation:** “π′f=fπ, modulo les f tels que fπ=π′f=0”. **Context search:** `projecteur|\\pi|inverse|catégorie` → CT 16/015 (matrix units), 16/016 (projector grading), 16/017 (uniqueness with grading), and 16/018 (ring definition); Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”; CN §S5–S6. **Relation:** adds the categorical realization of projector corners to CT's ring operations; restates Hua's explicit corner identification. **RS:** MPL_11_043-058+56 N031 and MPL_14_087-132 M01 (first-pass leads), WG2 §2.4 #3 (unchecked).

The map f ↦ π′fπ identifies the written quotient with π′ Hom(X,X′) π: on the intertwining subspace it has precisely the written kernel, and every corner element already intertwines the projectors. Composition descends because the corner multiplication is ordinary composition with the intervening idempotent. This verifies the local definition without requiring the geometric conjectures discussed in cote 16.

### M05 — Projector splitting and semisimplicity are separate stages

**Witness:** cote 12, scan 146, middle and lower paragraphs. **Kind:** unpursued implication. **Quotation:** “n'utilise pas les hyp précédentes”; “rendre tous les projecteurs scindables”. **Context search:** `projecteurs|semi-simple|universel` → CT 16/049; CN §S14–S16; Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”. **Relation:** adds an explicit separation of the formal and conjectural stages to the earlier semisimplicity yoga. **RS:** WG2 §2.3 #7 and WG2 §2.4 #3 (unchecked plans); MPL_15_087-138 L01 (lead).

The universal property of the idempotent completion only asks that target idempotents split; the manuscript correctly weakens “abelian” to that condition in the margin. The formula H(X,π)=Im H(π) is thus valid before any semisimplicity assertion. The geometric burden remains proving that the original endomorphism rings satisfy the extra assumptions.

### M06 — Recovering the generalized-inverse argument without assuming abelianness

**Witness:** cote 12, scan 147, inserted v and oval of four identities; scan 148, direct-morphism criterion. **Kind:** unproved claim. **Quotation:** “v∈U”; “πv=v, uπ=u”; “Tout morphisme ... est ‘direct’”. **Context search:** `inverse|semi-simple|left|right` → CT 16/049; CN §S14; Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”. **Relation:** adds the algebraic mechanism sought in CT 16/049 and agrees with the substance of Hua's reconstruction. **RS:** WG2 §2.4 #3 (unchecked plan).

For a semisimple finite-dimensional ring U, choose an inner inverse v₀ with uv₀u=u and replace it by v=v₀uv₀, which also satisfies vuv=v. Then π=vu and ϖ=uv are idempotent, u identifies their split images, and their complementary summands give kernel and cokernel objects. This supplies the categorical argument without using the manuscript's intervening phrase about an action “sur un objet d'une catégorie abélienne” as a premise, which would otherwise assume the conclusion.

### M07 — The printed projection index is a genuine research correction, not a transcription change

**Witness:** cote 12, scan 148, lines 25–28. **Kind:** reading question. **Quotation:** “R=P×Q”; “v=inj₂u pr₂”. **Context search:** `inj|\\operatorname\{pr\}|morphisme` → Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”; CT 16/049; CN §S14. **Relation:** differs from Hua's silently normalized main formula, while Hua's footnote acknowledges the original second projection. **RS:** WG2 §2.4 #3 (unchecked plan).

For u:P→Q and the stated ordering R=P⊕Q, a well-typed reduction is v=i_Q u p_P, hence uses pr₁ under the ordinary indexing. The frozen text retains pr₂, exactly as Hua's footnote says the manuscript does. This is an explicit type-check repair for the proof only; it gives no permission to change the frozen formula.

### M08 — A specific disagreement with Hua's “monomorphismes” footnote

**Witness:** cote 12, scan 148, line 20. **Kind:** reading question. **Quotation:** “Tout morphisme u:P→Q est ‘direct’”. **Context search:** `monomorphismes|morphisme|direct` → Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”, footnote following the A⊕B→B⊕C normal form; CT 16/049. **Relation:** the frozen reading differs from Hua's claim about what the page says. **RS:** WG2 §2.4 #3 (unchecked plan); this local reading has no reviewed RS entry.

Hua says the page formulates the condition for monomorphisms and then corrects it to all morphisms, but the frozen reading here already says “Tout morphisme”. The mathematical normal form is appropriate for all morphisms, with kernel A and cokernel C. Record this as a disagreement between readings, not as an established manuscript error corrected by Hua.

### M09 — What the finite chain condition actually proves

**Witness:** cote 12, scan 147, final paragraph; scan 148, condition (i). **Kind:** unproved claim. **Quotation:** “conditions de chaînes”; “de dim finie”. **Context search:** `chaînes|finie|semi-simple` → Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”; CT 16/049; CN §S14–S15. **Relation:** adds the finite-length part of the categorical argument to CT's ring claim. **RS:** WG2 §2.3 #7 and WG2 §2.4 #3 (unchecked).

A strictly growing chain of direct summands of P produces successively nonzero orthogonal idempotents in End(P), so its length is bounded by dim_Q End(P). Once every morphism has the split normal form, all subobjects are such summands, making the same bound a finite-length bound in the resulting abelian category. The chain argument and the split-morphism argument are both needed for the manuscript's stated finite semisimplicity convention.

### M10 — The “grain of salt” concerns the scope of the abelian universal problem

**Witness:** cote 12, scan 148, opening paragraph. **Kind:** self-flagged. **Quotation:** “Pb universel (avec un grain de sel)”. **Context search:** `universel|équivalence|abélienne` → Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”; CT 16/049. **Relation:** adds an explicit qualification to the earlier programme. **RS:** WG2 §2.4 #3 (unchecked plan); MPL_15_087-138 L01 (lead).

An additive functor from a semisimple abelian category to any abelian category is exact because every short exact sequence splits. Thus the proposed abelian universal property follows only after semisimplicity has been established under the stated starting hypotheses, with functor categories interpreted up to equivalence and variance fixed. The aside is a genuine manuscript qualification, but it does not specify which of those caveats its author intended.

### M11 — Variance is not silently resolved by the completion

**Witness:** cote 12, scan 144, V with an uncertain opposite marker; scan 146, h:V→M. **Kind:** reading question. **Quotation:** “H ... V^{◦|*}”; “h ... V→M”. **Context search:** `contravariant|foncteur|correspondance` → Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)” and “L'exemple des variétés (pages 149 à 151)”; CT 16/049. **Relation:** differs in presentation across the manuscript and its modernization, without changing the underlying opposite-invariant construction. **RS:** MPL_15_087-138 L01 and MPL_11_043-058+56 N031 (leads); WG2 §2.4 #3 (unchecked).

The algebraic completion works for V or Vᵒᵖ, but the chosen variance must remain fixed when stating a single universal property. The frozen sheets start with the uncertain opposite marker and later display the covariant inclusion of V. This is a presentation issue for the reconstructed theorem, not evidence for changing either diplomatic occurrence.

### M12 — Tensor extension is explicit on projectors

**Witness:** cote 12, scan 149, first two paragraphs. **Kind:** unproved claim. **Quotation:** “se prolonge ... essᵗ unique”; “symétrique ... associatif ... unitaire”. **Context search:** `bifoncteur|multiplicative|produit|projecteur` → Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”; CT 16/018 and 049. **Relation:** adds the tensor step absent from the earlier isolated-ring definition; restates Hua's main account. **RS:** WG2 §2.4 #3 (unchecked plan), MPL_14_087-132 M01 (lead).

A biadditive F extends by F((X,p),(Y,q))=(F(X,Y),F(p,q)); idempotence follows from functoriality. Associativity, symmetry, and unit constraints restrict to these images and inherit their coherence identities, so the essential uniqueness is the same split-idempotent universal property in two variables. This constructs a symmetric monoidal category but does not by itself supply duals, a faithful fibre functor, or a motivic Galois group.

### M13 — Characteristic zero is used to split Schur projectors

**Witness:** cote 12, scan 149, last paragraph and display. **Kind:** unpursued implication. **Quotation:** “de car. 0”; “opérations tensorielles covariantes”; “∧ⁿM ... Sⁿ(M)”. **Context search:** `symétrique|tensor|opération|car\.` → Hua, “L'enveloppe pseudo-abélienne (pages 143 à 148)”; CT 16/014 (integral exterior-algebra model) and 16/015 (matrix units); CN §S2–S3. **Relation:** adds a rational projector construction while differing from the integral normalization issues in CT. **RS:** WG2 §2.3 #2 and WG2 §2.4 #3 (unchecked plans).

The symmetrizer (1/n!)Σσ and antisymmetrizer (1/n!)Σsgn(σ)σ are idempotents acting on M^{⊗n}, so their images exist in the completion. For fixed n, invertibility of n! suffices; characteristic zero is the uniform convenient hypothesis for every n over a coefficient field. No vanishing of high exterior powers, ordinary rather than super symmetry, or Tannakian fibre-functor criterion follows merely from their existence.

### M14 — The precise link to the cote 16 programme

**Witness:** cote 12, scans 143–149; principally 144 heading and 145 endomorphism hypothesis. **Kind:** unpursued implication. **Quotation:** “Construction abstraite d'une théorie de motifs semi-simples”. **Context search:** `lefschetzien|correspondances|semi-simple|motifs` → CT 16/018 and 049; CN §S14–S16; Hua, “L'exemple des variétés (pages 149 à 151)”. **Relation:** adds the formal completion sought by the CT programme; does not witness its geometric input. **RS:** WG2 §2.4 #3 and WG2 §2.3 #2 (unchecked); MPL_15_087-138 L01, MPL_14_087-132 M01, MPL_11_043-058+56 N031 (leads).

CT 16/049 proposes deriving semisimplicity of correspondence classes and splitting monomorphisms from the inverse-Lefschetz condition plus an index relation. The present leaves explain what to do once suitable semisimple endomorphism rings are available, but do not prove that the graded rings of CT 16/018 meet the geometric hypotheses. Hua's geometric example occurs after this selection, so the answer is a verified structural connection, with the actual choice of correspondence category still outside the witnessed pages.

### M15 — Later numerical semisimplicity does not identify the manuscript's realization category

**Witness:** cote 12, scans 145–148. **Kind:** unpursued implication / literature comparison. **Quotation:** “algèbre ... de dim finie ... semi-simple”. **Context search:** `Jannsen|numérique|homologique|semi-simple` → CT 16/049; CN §S15–S16; Hua, “L'exemple des variétés (pages 149 à 151)”. **Relation:** restates CN's distinction and adds the exact local lemma to which these pages correspond. **RS:** WG2 §2.3 #7 (unchecked plan); MPL_15_087-138 §127 (first-pass bibliography lead).

Jannsen (1992, Lemma 2) proves the categorical implication used here, and Theorem 1 proves semisimplicity of pure numerical motives without the standard conjectures. These are separate statements from asserting semisimplicity for algebraic classes modulo a chosen homological equivalence. His Corollary 1 identifies the homological-to-numerical kernel as a nilpotent radical when Künneth projectors are algebraic; nilpotence alone does not make that kernel zero.

### M16 — Why the Lefschetz sl₂ is not the motivic weight symmetry

**Witness:** cote 12, scans 144–149, scope of the abstract construction; no sl₂ or weight cocharacter appears there. **Kind:** unpursued implication / bounded comparison. **Quotation:** “catégories multiplicatives”; “motifs semi-simples”. **Context search:** `sl₂|Lefschetz|graduation|cocaractère|poids` → CT 16/014 (integral model), 16/015 (matrix units), 16/016 (projector grading), 16/017 (grading requirement), 16/018 (Lefschetz ring), and 16/049 (semisimple motive programme); CN §S2–S6; Hua, “Structures supplémentaires sur le groupe de Galois motivique (pages 14 à 16)”. **Relation:** distinguishes the two structures joined conjecturally by the plan. **RS:** MPL_14_087-132 M04 and MPL_15_087-138 §111 (first-pass leads), MPL_15_087-138 L07 (lead), WG2 §2.3 #2 and WG2 §2.4 #3 (unchecked).

The cited earlier returns already give the projective-line obstruction, so this package does not claim a new counterexample. On H⁰(P¹)⊕H²(P¹), Lefschetz sl₂ has Cartan eigenvalues −1,+1 and raising/lowering maps between the summands, whereas the motivic weight cocharacter has exponents 0,2 and tensor automorphisms preserve the unit summand. The two diagonal actions differ by a scalar shift, and nontrivial sl₂ root operators cannot be the root operators of a central weight cocharacter. Any separate published SL₂ action through correspondences therefore requires its own target and twists; it is not an inclusion of this SL₂ into the Tate motivic Galois group G_m.

### M17 — The correct draft-versus-published lettering table has uncertainty columns

**Witness:** cote 12, scan 99, marginal “conj. standard”; absence of an A–D definition in this selection. **Kind:** reading question. **Quotation:** “Kleimann ... conj. standard”. **Context search:** `\b[ABCD]\s*\(|index|inverse|conjecture` → CT 16/044 (A + index ⇒ B and characteristic-zero comparison), 16/048 (D and algebraic complementary-degree isomorphisms), and 16/049 (inverse and splitting consequences); CN §S1, “Compare definitions before letters”; RS MPL_14_087-132 M01. **Relation:** restates the context's explicit evidence limit. **RS:** WG2 §2.4 #3 (unchecked); MPL_14_087-132 M01 (lead, original absent).

The two secure operational matches are draft A with the Lefschetz assertion for algebraic classes, and draft C with algebraicity of the inverse Lefschetz operation, printed A and B respectively. The implications on CT 16/044 and 048 suggest draft B=printed D (homological=numerical) and draft D=printed C (Künneth projectors), but are not standalone definitions. Keep the latter two provisional until the 14/117 notation table or another defining witness is inspected; the printed names themselves are verified in Grothendieck (1969, §§2–4) and Kleiman (1968, introduction and §3).

| Draft letter in CT 16/044–050 | Operational evidence in supplied CT | Printed convention | Confidence in identity |
|---|---|---|---|
| A | Lefschetz restriction on algebraic classes; critical-degree product reductions | A | High for content, not for every quantifier in every draft |
| B | A + index ⇒ B; in characteristic zero A equivalent to B | D: homological equivalence = numerical equivalence | Provisional; direct definition missing |
| C | Algebraic complementary-degree inverses; lowering operator and product/hyperplane stability | B: Lefschetz lowering algebraic | High |
| D | Implies rational characteristic polynomials; used with algebraic complementary-degree isomorphisms to imply C | C: algebraic Künneth projectors | Provisional; direct definition missing |
| Index relation I | Positivity of the relevant primitive pairing | I or Hdg | Compare actual pairing and signs; letter not a substitute for definition |

### M18 — The singular-hypersurface question remains an evidence gap

**Witness:** cote 12, scans 105–109, singular/nonproper cohomology; scan 143 cover. **Kind:** unpursued implication / scope limitation. **Quotation:** scan 107 “résolution des singularités”; scan 143 “Construction abstraite”. **Context search:** `singul|hypersurf|Serre|standard` → CT 16/047, last letter paragraph; CN §16:47:4–6; RS WG2 §2.4 #3; Hua, “Poids de la cohomologie ℓ-adique d'une variété singulière ou non propre (pages 104 à 108)”. **Relation:** adds related singular-cohomology machinery; does not establish the proposed cote 14 continuation. **RS:** WG2 §2.4 #3 (unchecked).

CT 16/047 rejects a smooth-hypersurface reduction and asks for a formulation involving singular varieties. The present weight calculations concern singular varieties and their cohomology, but neither name that hypersurface reduction nor show cote 14 taking it up. No underlying cote 14 pages are supplied, and its title or RS references cannot answer a question about its actual argument.

### M19 — The Artin quotient and the component quotient must not be conflated

**Witness:** cote 12, scans 140–142, smooth (iso)motives; scans 143–149, abstract construction; no displayed Galois-group exact sequence. **Kind:** reading question / bounded comparison. **Quotation:** scan 140 “isomotif ... lisse”; scan 149 “symétrique ... associatif ... unitaire”. **Context search:** `Galois|fondamental|composantes|pi_1|exact` → Hua, “Le groupe fondamental (pages 6 à 9)” and “Le groupe fondamental profini, et le Frobenius (pages 9 à 13)”; `context/README.md`, “What our planning document asks of these folders”, motives question; CT 16/049. **Relation:** current leaves add no group sequence to Hua's earlier-cote account. **RS:** WG2 §2.4 #3 (unchecked); MPL_18_018-062 MB10 (lead).

Hua credits the earlier cote 12 pages with an Artin quotient G→π₁ and explains that identifying π₀(G) with π₁ needs the assertion that finite motivic representations are Artin. That contextual assertion is not a sequence written in this selected range. Over Q, Γ_Q denotes the profinite constant group scheme in such a sequence, and a compatible fibre functor must be fixed before writing its group maps.

### M20 — A modern exact sequence supplies a comparison theorem, not a manuscript witness

**Witness:** cote 12, scans 143–149, abstract tensor construction. **Kind:** unpursued implication / literature comparison. **Quotation:** “foncteur ... symétrique ... associatif ... unitaire”. **Context search:** `Galois|exact|Nori|Ayoub|Artin` → Hua, “Le groupe fondamental (pages 6 à 9)”; RS MPL_18_018-062 MB10 and MPL_15_195-228+18_002-017 S15; `context/README.md`, “What our planning document asks of these folders”. **Relation:** adds a published comparison beyond the supplied manuscript evidence. **RS:** those two entries are first-pass leads; WG2 §2.4 #3 remains an unchecked plan.

For a rational Tannakian motivic theory with effective Galois descent and compatible fibre functors, Kahn (2025, Theorem 5.10) yields 1→G_mot(Q̄)→G_mot(Q)→Γ_Q→1. His framework includes rational Nori motives, with the relevant descent established in §10. The identification of the geometric kernel with the identity component, or a splitting over Q, is an additional assertion and is not supplied by this exactness theorem or these frozen pages.

### M21 — The period-conjecture search is negative here and positive only as a lead elsewhere

**Witness:** cote 12, all selected scans 099–149; particularly 143–149 for the formal construction. **Kind:** reading question / negative source finding. **Quotation:** scan 143 “Construction abstraite de Catégories de motifs”. **Context search:** `périod|period|transcendan|comparaison|générique` → no period-conjecture statement in the frozen combined transcription or the full Hua reading; RS MPL_15_087-138 T26 and MPL_18_018-062 §2. **Relation:** restates the earlier evidence limit for this package; adds an explicit lead to 18/059 from the register. **RS:** both entries are first-pass leads, not independently reviewed witnesses.

No statement about genericity of a Betti–de Rham comparison point or algebraic independence of periods appears in this selected range. RS identifies 18/059 as naming “conjecture de transcendance N° 1”, which is an exact retrieval target for the later package but not a text inspected in this research pass. The absence claim is limited to the searched material, not to Grothendieck's archive.

### M22 — A precise modern period formulation clarifies what would count as a witness

**Witness:** cote 12, scan 143 cover and scans 144–149; no period assertion. **Kind:** unpursued implication / literature comparison. **Quotation:** “Construction abstraite”. **Context search:** `périod|period|comparaison|transcen` → RS MPL_15_087-138 T26 and MPL_18_018-062 §2; no matching period-torsor statement in Hua, including “Motifs sur une base, et le groupe de Galois motivique (pages 5 et 6)”. **Relation:** adds a criterion for recognizing a future witness; does not attribute that criterion to these scans. **RS:** cited entries are first-pass leads; WG2 §2.4 #3 is unchecked.

For a motive M over Q, the period torsor Isom^⊗(ω_dR,ω_B) on the tensor category generated by M has a comparison point over C. Grothendieck's period conjecture says that point is Zariski generic over Q, or equivalently that the polynomial relations among its periods are precisely the motivic relations (André, 2010, §1.4). This comparison is stated only to specify the missing assertion, not to infer it from the existence of a tensor category or a fibre functor.

### M23 — Pure Nori and André motives realize a qualified semisimple comparison

**Witness:** cote 12, scans 145–149, semisimple completion and tensor structure. **Kind:** unpursued implication / literature comparison. **Quotation:** “abélienne semi-simple”. **Context search:** `Nori|André|semi-simple|correspondance` → RS MPL_14_087-132 M23, MPL_15_195-228+18_002-017 M07 and S15; CT 16/049; Hua, “L'exemple des variétés (pages 149 à 151)”. **Relation:** verifies the exact external comparison underlying those leads, without converting motivated correspondences into algebraic ones. **RS:** all cited returned-package entries are first-pass leads.

For the rational characteristic-zero setting with a chosen complex realization, Arapura (2013, Theorem 6.4.1) identifies pure Nori motives with André's category of motivated motives. This provides a semisimple Tannakian realization of the formal architecture, using motivated correspondences. It does not prove that every motivated correspondence is represented by an algebraic cycle, so it does not establish the full standard-conjecture input envisaged in cote 16.

### M24 — The Nori–Ayoub theorem is a group comparison, with no automatic cycle conjecture

**Witness:** cote 12, scans 144 and 149, universal additive and monoidal constructions. **Kind:** unpursued implication / literature comparison. **Quotation:** “équivalence de catégories”; “foncteur bi-additif”. **Context search:** `Nori|Ayoub|Galois|Hopf|universel` → RS MPL_18_018-062 MB10, MPL_15_195-228+18_002-017 M07 and S15; Hua, “Motifs sur une base, et le groupe de Galois motivique (pages 5 et 6)”. **Relation:** adds a checked theorem to the earlier lead; differs from a blanket identification with the manuscript's unconstructed category. **RS:** cited entries are first-pass leads, not independently reviewed internal theorems.

Choudhury and Gallauer (2017, Theorem 9.1) construct inverse Hopf-algebra isomorphisms comparing Nori's and Ayoub's motivic Galois groups; the rational case applies over a field embedded in C with the chosen Betti realization. The theorem does not identify their mixed category with the semisimple category sought on these selected sheets, nor prove Tate, Hodge, or the standard conjectures for algebraic correspondences. It is a precise affirmative answer to one modern group-comparison question, while the geometric identification remains separate.

### M25 — Symmetric monoidal is not yet Tannakian

**Witness:** cote 12, scan 149, end of the supplied range. **Kind:** own idea / hypothesis audit. **Quotation:** “symétrique ... associatif ... unitaire”. **Confidence:** high; the missing properties are independent of additive idempotent completion. **Context search:** `dual|fibre|signe|Künneth|tensoriel` → Hua, “L'exemple des variétés (pages 149 à 151)” and “Duaux, formes bilinéaires, involutions (pages 155 à 157)”; CT 16/018 and 049; CN §S15. **Relation:** adds an explicit boundary to the current construction; Hua's later sections support that the omitted structures are treated later. **RS:** WG2 §2.4 #3 (unchecked); MPL_15_195-228+18_002-017 S15 and MPL_14_087-132 M23 (leads).

At scan 149, the construction has not provided rigidity, End(1)=Q, a neutral fibre functor, or the compatibility between cohomological Koszul signs and ordinary tensor symmetry. Hence extracting a motivic Galois group here would require additional hypotheses or subsequent pages. The later Hua subsections describe precisely some of those further stages, but their content cannot be folded back into the frozen selection as if already written here.

## Direct algebra checks behind the research notes

These are explicit reconstructions, not additions to the diplomatic text, and not claims of novelty. They may be incorporated as a short proof appendix if the final notes retain the required per-item format.

1. **Corner morphisms.** Put A={f | qf=fp}. The map A→q Hom(X,Y)p, f↦qfp, is surjective because every element g=qgp satisfies qg=gp=g; its kernel is exactly {f | fp=qf=0}. This verifies M04.
2. **Inner inverse.** In a matrix algebra over a division ring, split the vector space into ker(u) and a complement, and choose a complement of im(u); inverse on the image and zero on its complement gives v with uvu=u and vuv=v. Products of matrix algebras yield the same construction componentwise. Then vu and uv are idempotents and the four relations in 12/147 follow, giving the split normal form without assuming abelianness in advance.
3. **The additive-hull warning.** A preadditive Q-linear category with objects X,Y, End(X)=End(Y)=Q, Hom(X,Y)=Q, Hom(Y,X)=0 has individually semisimple endomorphism rings but no biproduct; its additive hull has a triangular endomorphism algebra for X⊕Y, which is not semisimple. Thus “every End is semisimple” must apply after actual finite additivity is available.
4. **Lefschetz test.** On basis (1,h) of H*(P¹), set e(1)=h, e(h)=0, f(h)=1, f(1)=0; [e,f]=diag(−1,1). By contrast the weight cocharacter is diag(1,t²), and the tensor category generated by Q(−1) has diagonal G_m action; the unit is fixed. This only recalls the already registered P¹ test, not a newly claimed result.

## Primary bibliography and exact checked passages

The word budgets of the retrieved sources were respected by limiting attributed summaries to the local statements used; the longer proof checks above are direct reconstructions from the manuscript and elementary algebra.

- André, Y. (2010). An introduction to motivic zeta functions of motives. In A. Carey, D. Ellwood, S. Paycha, & S. Rosenberg (Eds.), *Motives, quantum field theory, and pseudodifferential operators* (Clay Mathematics Proceedings, Vol. 12, pp. 3–17). American Mathematical Society; Clay Mathematics Institute. https://www.claymath.org/wp-content/uploads/2022/03/cmip012c.pdf — checked §1.4, period torsor and genericity, pp. 6–7; volume title and all four editors checked against the title page.
- Arapura, D. (2013). An abelian category of motivic sheaves. *Advances in Mathematics, 233*, 135–195. https://doi.org/10.1016/j.aim.2012.10.004 — checked Theorem 6.4.1 in the author preprint: https://pure.mpg.de/pubman/item/item_3121497_1/component/file_3121498/Arapura_an%2Babelian_oa_2013.pdf .
- Choudhury, U., & Gallauer Alves de Souza, M. (2017). An isomorphism of motivic Galois groups. *Advances in Mathematics, 313*, 470–536. https://doi.org/10.1016/j.aim.2017.04.006 — checked introduction and Theorem 9.1, arXiv version 3: https://arxiv.org/pdf/1410.6104 .
- Grothendieck, A. (1969). Standard conjectures on algebraic cycles. In *Algebraic geometry (International Colloquium, Tata Institute of Fundamental Research, Bombay, 1968)* (pp. 193–199). Oxford University Press. https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf — checked §§2–4 for printed A, B, C, Hdg and their relationships.
- Jannsen, U. (1992). Motives, numerical equivalence, and semi-simplicity. *Inventiones Mathematicae, 107*, 447–452. https://doi.org/10.1007/BF01231898 — checked Theorem 1, Lemma 2, and Corollary 1: https://epub.uni-regensburg.de/26642/1/jannsen10.pdf .
- Kahn, B. (2025). Galois descent for motivic theories. *Theory and Applications of Categories, 44*(20), 588–616. https://www.tac.mta.ca/tac/volumes/44/20/44-20.pdf — checked revised published text, Theorem 5.10 and §10: https://webusers.imj-prg.fr/~bruno.kahn/preprints/stacks-TAC.pdf .
- Kleiman, S. L. (1968). Algebraic cycles and the Weil conjectures. In *Dix exposés sur la cohomologie des schémas* (pp. 359–386). North-Holland; Masson. https://agrothendieck.github.io/divers/kleimanweil.pdf — checked introduction for standard A, B, C, D, I meanings and distinctions.

## Web reference IDs for the root's independent verification

The root should open the URLs or these refs itself before citing in the assembled notes.

| Primary source | Retrieved reference | Used passage |
|---|---|---|
| Jannsen | `turn825452626view0` | Theorem 1; Lemma 2; Corollary 1 |
| Grothendieck standard conjectures | `turn825452626view1`; `turn770717324view0` | §§2–4 |
| Kleiman | `turn580338250view2` | Introduction, pp. 359–360 |
| Arapura | `turn657373715view1` | Theorem 6.4.1 |
| Choudhury–Gallauer | `turn395782289view1`; `turn753696430view1` | Introduction; Theorem 9.1 |
| Kahn | `turn395782289view0`; `turn753696430view0` | Theorem 5.10, §10 |
| André | `turn580338250view1`; `turn753696430view2` | §1.4, pp. 6–7 |


## Recordable context-search provenance

All M01–M25 queries were run through `scripts/search_context.py`; complete match locators are retained under `records/research_searches/M01.json` through `M25.json`. `records/motives_linear_search_manifest.md` gives the compact 50-note M/LN/SM manifest, and `records/research_searches/motives_linear_manifest.json` gives exact inspected file, line, cote/scan, subsection, and whether the inspected location is a literal query hit or adjacent follow-up. The negative findings M18, M21, and M22 concern missing substantive statements, not absence of every lexical match; SM15 and SM18 similarly have no matching positive-range or prime-index-reduction statement in the supplied context.
