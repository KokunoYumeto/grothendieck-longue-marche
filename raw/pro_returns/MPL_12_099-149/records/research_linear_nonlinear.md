# Research contribution: the linear/non-linear comparison and smooth integral motives

This is a research-phase contribution only: no transcription, doubts, or inventory file was changed. The frozen page fragments 12/114–115, 125, and 140–142 were read as text; supplied context was searched by the terms recorded below. `CT` means `context/MPL_16+47+54+44_transcription.tex`; `Hua XIII` means **Hua, modernised reading of cote 12**, subsection “XIII. Motifs lisses et isomotifs lisses (pages 138 à 141)” in `context/hua_project/12.modern.tex`; its page numbers are one below the scan numbers used here. `RS` means `context/notes/RESULTS_STATE.md`; all cited research-return statuses below are the runs' claims, and returned-package notes and war-game rows are unreviewed leads unless explicitly stated otherwise.

## 1. Requested comparison table

The table is a comparison proposed by the supplied planning README; the manuscript does not itself write these four equivalences. The examples below explain why none should be read as a formal equivalence between a linear and a non-linear theorem.

| Pair and manuscript anchor | Linear statement | Non-linear statement | Exact scope and limitation |
|---|---|---|---|
| Tate / anabelian Hom; 12/142, “pleinement fidèle” | For abelian varieties over a finite field, with l different from the characteristic, `Hom(A,B) ⊗ Z_l → Hom_G(T_l A,T_l B)` is an isomorphism (Tate, 1966, main theorem); over a number field the same result follows from Faltings's endomorphism theorem by applying it to `A × B` (Faltings, 1986, Theorem 4). | For smooth geometrically connected curves `X,Y` over a sub-p-adic field, with `Y` hyperbolic, dominant morphisms correspond to continuous open homomorphisms of arithmetic fundamental groups over the base Galois group, modulo inner conjugation by the geometric target group (Mochizuki, 1999, Theorem A/16.5). | The latter also has a geometrically pro-p version, while its Galois quotient remains the full absolute Galois group; no arbitrary abstract group homomorphisms or section-surjectivity assertion is included. Passing to abelianizations gives a Jacobian map but loses the conditions making a linear map come from a curve map. |
| Semisimplicity / trivial centres; 12/140, “isomotif semi-simple”; 12/114, “semi-simplicité utilisée!” | In characteristic zero, semisimplicity of a neutral Tannakian category corresponds to pro-reductivity of its group (Deligne & Milne, 1982/2012, Proposition 2.23 and its extension to the identity component). | The geometric profinite fundamental group of a characteristic-zero hyperbolic curve is centre-free, as are its open subgroups, since these correspond to hyperbolic finite covers (Tamagawa, 1997, Proposition 1.11). | Reductivity allows a central torus: the Tate category has group `G_m`; centre-freeness instead makes the conjugation map `Δ → Aut(Δ)` injective and identifies `Δ` with `Inn(Δ)`. |
| Polarizations / real structures; 12/141, the weight-one abelian-scheme functor; CT 44/2, “polarisation” | A weight-n polarization has the appropriate parity, alternating in odd weight and symmetric in even weight, with positivity after the Weil-operator convention; it is not merely a real involution (Deligne & Milne, 1982/2012, Definition 5.12). | For a smooth projective geometrically connected curve `X/R` of genus at least one, conjugacy classes of sections of `π₁(X) → Gal(C/R)` correspond to connected components of `X(R)` (Stix, 2008, Theorem 26). | The real theorem recovers a finite set of components, not individual real points, and a polarization on `H¹(X(C))` does not supply a section of the arithmetic extension. |
| Weights / cyclotomic normalizers; 12/115, “poids entre”; 12/141, “le poids” | At a good finite place, the eigenvalues of arithmetic Frobenius on `V_l J` have absolute value `q^(1/2)`, while its value on `Q_l(1)` is `q`; hence `Hom_G(Q_l(1),V_l J)=0` after any finite extension with such a place (Serre & Tate, 1968, Theorem 3). | For affine hyperbolic curves over finitely generated fields of characteristic zero, the cyclotomic-normalizer characterization of cusp inertia is substantially stronger than an open image for the normalizer alone; Tamagawa (1997, §7C) states Nakamura's result with the actual cyclotomic action condition. | The weight test excludes nonzero cyclotomic images in a Jacobian quotient; to classify a subgroup invisible there requires finite-cover detection and control of the conjugation character, precisely the extra issues reflected by RS LM6 A.22 and A.50. |

### LN01 — The Hom comparison is an analogy with specified functors

**Witness/kind:** 12/142, lines 4–5; unpursued implication. **Quotation:** “Le foncteur … est pleinement fidèle.” **Context search:** `Tate|fidèle|Hom` → CT 44/8 (Tate-module subquotient of odd cohomology), and RS `MPL_15_087-138 §3`, `MPL_18_018-062 §3` (first-pass table leads); current pages **add** an integral weight-one reconstruction proposal rather than an anabelian theorem. **Bears on:** those two RS table leads and WG2 §2.4 #3, unchecked plan.

The map on the page already includes a rational motivic morphism and compatible integral realizations, whereas Tate–Faltings asks whether every Galois-equivariant realization morphism arises geometrically. Consequently, full faithfulness of this `φ` is not itself a statement of the full Tate conjecture, and its reduction to the generic point still needs the correspondence-theoretic identification of morphisms between `h¹` of abelian varieties. The page's contravariant `H¹` convention also reverses arrows relative to the table's covariant Tate-module formula. The non-linear theorem in the table is a later theorem with different source and target categories, not a result proved by 12/142.

### LN02 — A concrete gap between Jacobian Hom and curve Hom

**Witness/kind:** 12/142, “pleinement fidèle”; own idea. **Confidence/reason:** high, because Riemann–Hurwitz and the action on a polarization give an elementary test. **Context search:** `Tate|Hom|fidèle` → CT 44/8 and RS `MPL_18_018-062 §3`; this **adds** a scope example to the supplied analogy, without changing either status. **Bears on:** `MPL_18_018-062 §3`, first-pass lead.

For a smooth proper curve `X` of genus at least two over a number field, multiplication by two on `J_X` supplies an integral Galois-equivariant endomorphism of `T_l J_X`, but cannot be induced by a dominant self-map of `X`. Indeed, Riemann–Hurwitz makes every such self-map an automorphism, whose map on `H¹` preserves the canonical symplectic form, whereas multiplication by two scales it by four. This elementary example explains why abelianization does not turn the anabelian Hom statement into the linear one.

### LN03 — Semisimplicity does not mean centre-freeness

**Witness/kind:** 12/114, marginal “semi-simplicité utilisée!”; 12/140, opening definition; own idea. **Confidence/reason:** high, because the two counterexamples are explicit elementary representations. **Context search:** `semi-simple|centre` → CT 16/5 (central projectors in `E⁰`), 16/49 (semisimple motive yoga); these pages **restate** semisimplicity in a realizational setting and **differ** from group centre conditions. **Bears on:** WG2 §2.3 #7 and WG2 §2.4 #3, unchecked plans; no assertion here settles LM4_SUCCESSOR B.34/B.38.

The category `Rep_Q(G_m)` is semisimple but its group has centre `G_m`; conversely, the affine group `G_a ⋊ G_m`, represented by matrices `[[a,b],[0,1]]`, is centre-free but its natural two-dimensional representation is a nonsplit extension. Thus neither implication holds even among characteristic-zero algebraic groups. The useful analogy is rigidity of the respective reconstruction formalism, and not an equality of the two properties.

### LN04 — A polarization need not produce a real section

**Witness/kind:** 12/141, weight-one functor, compared with CT 44/2 and 44/8–9; own idea. **Confidence/reason:** high, because the real locus of the explicit quartic is empty and the cited section theorem gives the consequence. **Context search:** `polarisation|positive|réel` → CT 44/2, Theorem 4, and 44/9 (ampleness question); RS `MPL_15_195-228+18_002-017 B03` already **states** the separation, while this example **adds** a concrete witness. **Bears on:** B03, and `MPL_60_002-035 F21–F22`, all first-pass leads.

The smooth real plane quartic `x⁴+y⁴+z⁴=0` has no real point and genus three, but its complex `H¹` has its usual polarization and a conjugation action from its real definition. Its arithmetic fundamental-group extension has no section by Stix's real section theorem. These are distinct notions of “real structure”: complex conjugation on a realization, a compact real form associated with a polarization, and a section over `Gal(C/R)` must not be identified.

### LN05 — Weight obstructions have an exact detection limit

**Witness/kind:** 12/115, first corollary; unpursued implication. **Quotation:** “poids entre.” **Context search:** `poids|Tate|cyclotom|normalis` → CT 16/21 (Tate sheaf), CT 44/8 (odd-cohomology Tate-module subquotient), RS LM6 A.22/A.50 and `MPL_15_195-228+18_002-017 B04`; the present estimates **add** linear input, with no local statement about profinite normalizers. **Bears on:** LM6 A.22 (Open, run claim), LM6 A.50 (Proved, run claim), B04 (first-pass lead).

If a normalized procyclic subgroup has cyclotomic conjugation on a nonzero l-adic component and that component survives in a proper Jacobian's Tate module, the Frobenius eigenvalue mismatch in the table excludes it. This argument says nothing about a subgroup in the common kernel of all tested abelian quotients unless one proves a finite-cover detection theorem. In particular, neither the open-normalizer hypothesis by itself nor these weight estimates upgrade LM6 A.22 to a result.

### LN06 — The toric part is exactly the allowed cyclotomic contribution

**Witness/kind:** 12/115, weights and compactification; unpursued implication. **Quotation:** “compactification et … résolution des singularités.” **Context search:** `poids|Tate|Picard|Jac` → CT 44/8 and RS LM7 C.1, C.5, C.8; the pages **add** the general weight language, but do not reconstruct the marked generalized Jacobians in those entries. **Bears on:** LM7 C.1 (Known, run claim), C.5 (Proved, run claim), C.8 (Refuted, run claim), E.23 (Open, run claim).

For an open smooth curve with nonempty boundary, the abelianized geometric fundamental group has the toric boundary contribution of Tate type as well as the proper Jacobian quotient, so the previous exclusion applies only to the latter. The marked-divisor extension class is further information and cannot be recovered from its graded weights alone. This agrees with the distinction recorded by C.5 and the refutation recorded by C.8, and it provides no determination of the section fibres left open in E.23.

### LN07 — The prime-to-p point problem is not answered here

**Witness/kind:** 12/114–115, conditional semisimplicity and weights; unpursued implication. **Quotation:** “si l'on admet conjecture de … simplicité.” **Context search:** `poids|prime-to|point` → RS FLAGGED_149 B9 and the newer ANABELIAN_SUCCESSOR A.3 headline; CT 44/8 concerns only abelian realizations. **Relation:** these pages **add** background linear tools but neither restate nor prove the nonlinear point-detection statement. **Bears on:** FLAGGED_149 B9 (Open, run claim); ANABELIAN_SUCCESSOR A.3 (newer claimed result, only partly checked according to RS).

Purity or semisimplicity of the displayed cohomology groups does not show that two points separated only at a nonabelian finite-cover level remain distinguishable in the prime-to-p quotient. The newer A.3 headline and older B9 row have different scope and review status, so this package should record both rather than silently reconcile or upgrade them. No proof of either claim appears on these scans.

## 2. Smooth integral motives: local claims and failure mechanisms

### SM01 — The one-prime independence conjecture

**Witness/kind:** 12/140, lines 8–10; conjecture. **Quotation:** “Conjecturalement, il suffit … pour un l.” **Context search:** `non ramifié|un seul|lisse` → Hua XIII, opening paragraph; CT 16/54 and 16/56 use scheme-theoretic unramifiedness, a different subject. **Relation:** the frozen pages **confirm** Hua's identification of a conjecture, while their all-prime definition remains stronger. **Bears on:** WG2 §2.4 #3 and WG2 §3.2 #7, unchecked plans.

For an abelian variety over a discretely valued field, the prime-to-residue-characteristic case is the Néron–Ogg–Shafarevich criterion, including independence of l (Serre & Tate, 1968, Theorem 1 and Corollary 1). This does not establish the analogous assertion for all semisimple motives over an arbitrary normal base. The parenthetical two-prime formulation needs a local argument covering residue characteristics, not a single globally invertible prime that need not exist on an arithmetic base.

### SM02 — A reference integral structure is missing from the local definition

**Witness/kind:** 12/140, lines 26–29; unproved claim. **Quotation:** “provient d'un isomorphisme sur Z_l.” **Context search:** `presque tout|torsion|entier` → CT 16/23, almost-all-prime integral autoduality; Hua XIII, footnote on the axiom. **Relation:** the page **confirms** the issue expressly identified by Hua: its integral reference for `T_l(M)` is unstated here. **Bears on:** WG2 §2.4 #3; Hua is an AI-produced interpretive lead, not a transcription witness.

An isomotif supplies rational realizations, so “an isomorphism over `Z_l` for almost all l” presupposes an integral reference system or an equivalence class of such systems. A finite-dimensional rational Hom space and individual lattices alone do not automatically give the asserted finite generation of integral Hom. What is needed is agreement with a common reference outside a finite set of primes, together with bounded denominators at the remaining primes.

### SM03 — Why almost-all-prime compatibility matters

**Witness/kind:** 12/140, lines 26–29 and 51; own idea. **Quotation:** “Les Hom sont des modules de type fini sur Z.” **Confidence/reason:** high, because the weakened model gives an explicit non-finitely-generated subgroup of Q. **Context search:** `presque tout|type fini|torsion` → CT 16/23; Hua XIII, integral-reference footnote. **Relation:** this **adds** a test to Hua's observation, and is not a counterexample to an axiom with a properly fixed reference system. **Bears on:** WG2 §2.4 #3, unchecked plan.

If the axiom were weakened to eventual torsion-freeness alone, take the rational Tate object with lattices `E_l=l⁻¹ Z_l` at every prime and compare it to the standard lattice system. The resulting Hom subgroup consists of rationals with `v_l(a) ≥ −1` for every l, contains `1/l` for every prime, and is not finitely generated over Z. The actual almost-all-prime isomorphism requirement must exclude this construction through its reference lattices.

### SM04 — Generic restriction is formally fully faithful for the realization data

**Witness/kind:** 12/140, lines 47–53; unproved claim. **Quotation:** “est pleinement fidèle.” **Context search:** `fidèle|isomotif|lisse` → Hua XIII, middle paragraph; CT 44/8 offers subquotients but no such restriction functor. **Relation:** the page **confirms** Hua's claim, and **adds** the componentwise kernel/cokernel explanation. **Bears on:** WG2 §3.2 #7, unchecked plan.

For a connected normal base, the generic fundamental group maps onto the base fundamental group, so equivariance of a map between two unramified realization systems is already checked generically. Conditional on the stated rational motivic category and its exact realization functors, kernels and cokernels can then be taken componentwise as the page says. This argument supports the full abelian subcategory assertion but does not imply closure under arbitrary generic extensions.

### SM05 — “Épaisse” fails if it means extension-closed

**Witness/kind:** 12/140, lines 54–57, and 12/141, opening sentence; own idea. **Quotation:** “une ss-catégorie abélienne épaisse.” **Confidence/reason:** high, because the finite representation below is explicit and its inertia action can be checked directly. **Context search:** `épaisse|extensions|non ramifié` → 12/125, Lemma 1, explicitly discusses extensions; Hua XIII repeats thickness without this test; CT 16/56 distinguishes unramifiedness and étaleness but has no contrary extension result. **Relation:** this **contradicts** the extension-closed reading of the assertion and of Hua's restatement, while preserving the weaker subquotient claim. **Bears on:** WG2 §3.2 #7 and WG2 §2.4 #3, unchecked plans.

Let `S=Spec C[[t]]`, `K=C((t))`, and choose a prime l; the cyclic extension `K(t^(1/l))/K` defines a continuous quotient `G_K → C_l`, acting on `V=F_l²` by `[[1,1],[0,1]]`. The corresponding finite commutative étale K-group fits into `0→F_l→V→F_l→0`, whose endpoints extend as constant groups to the strictly henselian S, while V does not extend étale because its inertia action is nontrivial. As a generic integral motive it has rational component zero and only a finite l-primary realization, so it is a counterexample inside the torsion part admitted in 12/141. The correction suggested by this example is “closed under subobjects and quotients,” or an ambient category already restricted to unramified realizations; it is not a change to the frozen wording.

### SM06 — The finite torsion quotient is a separate assertion

**Witness/kind:** 12/141, first paragraph; unproved claim. **Quotation:** “la catégorie quotient est équivalente.” **Context search:** `torsion|quotient|isomotif` → CT 16/21 and 16/23, separating finite torsion from rational Tate modules; Hua XIII, middle paragraph. **Relation:** the page **adds** a categorical formulation to the context's realization-level distinction. **Bears on:** WG2 §2.4 #3, unchecked plan.

The kernel of rationalization should be the finite torsion systems, and morphisms become isomorphisms after killing precisely such kernels and cokernels. To obtain the stated Serre quotient one must establish exactness, essential surjectivity, and the requisite lifting of rational morphisms after multiplication by an integer. The failure of extension closure in the larger generic category in SM05 does not prevent the finite torsion objects from forming a Serre subcategory internally in the proposed category of smooth motifs.

### SM07 — Internal Hom does not make the integral torsion category rigid

**Witness/kind:** 12/141, second paragraph; unpursued implication. **Quotation:** “une ⊗-catégorie avec Hom.” **Context search:** `Hom|torsion|tensor|Tannak` → CT 16/21–23 and Hua XIII; no supplied CT statement identifies this integral category with a neutral Tannakian category. **Relation:** this **adds** a necessary distinction to the motivic-Galois planning question. **Bears on:** WG2 §2.4 #3, unchecked plan.

A category of finitely generated integral modules can have a tensor product and internal Hom while its nonzero finite torsion objects are not dualizable: `Hom(Z/l,Z)=0` already prevents a rigid dual for `Z/l`. Thus this integral category, with finite groups included, should not be used directly as a rigid neutral Tannakian category. Passing to the rational isomotif category removes that elementary obstruction but still requires the remaining fibre-functor and tensor hypotheses.

### SM08 — The construction from all proper smooth schemes is asserted

**Witness/kind:** 12/141, paragraph preceding “Relations”; unproved claim. **Quotation:** “Tout schéma propre et lisse X sur S définit des motifs.” **Context search:** `propre et lisse|R^i|motif` → Hua XIII and CT 44/8 (Tate modules obtained from odd cohomology). **Relation:** the page **adds** the integral realization system to the older cohomological proposal; Hua replaces “propre” by “projectif” in its summary, so the frozen statement is broader. **Bears on:** WG2 §3.2 #7 and WG2 §2.4 #3, unchecked plans.

The integral l-adic systems may have torsion, which the definition allows at finitely many primes, but the rational component is required to lie in the chosen semisimple category. Proper smooth base change addresses the l-adic unramifiedness; the existence and functoriality of the rational motivic object and the integral compatibility remain separate requirements. The assertion on relative étale sites is wider still and is not constructed on these leaves.

### SM09 — The component group lies in the kernel of the displayed realization map

**Witness/kind:** 12/141, the formula for `E_l`, map `u_l`, and margin; reading question. **Quotation:** “extension de … par R¹.” **Context search:** `extension|torsion|Hom` → CT 16/21–23 and Hua XIII, paragraph “Schémas en groupes”; Hua repeats the same verbal order. **Relation:** the displayed algebra **differs** from the usual reading of that order, and the comparison raises a question rather than changing transcription. **Bears on:** WG2 §2.4 #3, unchecked plan.

Writing `F=A/A⁰`, the geometric l-primary torsion sequence is `0→A⁰[l^∞]→A[l^∞]→F(l)→0`, and dualizing into the divisible group `Q_l/Z_l` gives `0→Hom(F(l),Q_l/Z_l)→E_l→H¹(A⁰,Z_l)→0`. Thus the displayed map has the finite component contribution as its kernel, whereas “extension de [finite term] par R¹” normally puts `R¹` in the kernel. The issue could be loose terminology in the margin, not an error in the displayed definition, and both the frozen wording and Hua's interpretive repetition must remain distinguishable.

### SM10 — The weight-one full-faithfulness claim has two ingredients

**Witness/kind:** 12/142, lines 4–5; unproved claim. **Quotation:** “On se ramène au cas … Spec K.” **Context search:** `pleinement fidèle|schémas en groupes` → Hua XIII; CT 44/8 links abelian varieties and cohomology but supplies no integral reconstruction proof. **Relation:** this **adds** an integral assertion to that context. **Bears on:** WG2 §2.4 #3, unchecked plan.

Over the generic field, the rational `h¹` component identifies homomorphisms up to isogeny and the full family of l-adic integral conditions must recover the actual homomorphism and its action on components. Over the base, extending a generic homomorphism between already existing abelian schemes is a different problem from extending an abelian variety itself; the former is supported by the normal-base extension lemma in Faltings (1986, §2, Lemma 1). The one-line reduction on the manuscript does not prove essential surjectivity.

### SM11 — The essential-image formulation is visibly qualified

**Witness/kind:** 12/142, lines 7–21; withdrawn in the same text. **Quotation:** deleted “évidemment|exactement,” followed by “Il faut” and “La question si … suffisante.” **Context search:** `image essentielle|poids 1|suffisante` → Hua XIII, latter half; CT 44/8–9 gives conjectural abelian representatives. **Relation:** the page **adds** a caution absent from any unqualified reconstruction slogan, and Hua largely **restates** it. **Bears on:** WG2 §2.4 #3, unchecked plan.

The same scan withdraws an emphatic formulation of the essential image and separates the necessary weight-one condition from its unsettled sufficiency. This is a local revision on scan 142 itself, not a retraction across two different scans. The later mixed-characteristic examples below answer the sufficiency question negatively in the generality proposed, while not affecting the necessity claim.

### SM12 — The dimension-one criterion has a prime restriction

**Witness/kind:** 12/142, lines 17–19; unpursued implication. **Quotation:** “critère de Néron-Ogg-Chafarevitch” (last spelling doubtful in the frozen file). **Context search:** `Ogg|réduction|ramifié` → CT 44/9, final acknowledgment of a letter to Ogg, and Hua XIII. **Relation:** the manuscript **adds** mathematical content to that earlier correspondence pointer, but does not identify the letter. **Bears on:** WG2 §2.4 #3, unchecked plan.

Serre–Tate's precise valuation criterion uses l different from the residue characteristic; their Theorem 1 is stated with perfect residue field and a footnote explains the announced removal of that restriction. It is not a criterion saying that the p-adic Tate module must be unramified at residue characteristic p. The page's use of `S_l=S[1/l]` respects this distinction.

### SM13 — A later theorem realizes the proposed obstruction

**Witness/kind:** 12/142, lines 20–26; conjecture. **Quotation:** “mais peut-être pas … local régulier de dim 2 d'inégales caractéristiques.” **Context search:** `contre-exemple|dim 2|plat|réduction` → Hua XIII, concluding discussion (left open there); no corresponding example appears in CT. **Relation:** later literature **adds** the missing construction, without claiming the manuscript proved it. **Bears on:** WG2 §2.4 #3; RS `MPL_131 RN038` is a related first-pass extension/polarization lead only.

Vasiu and Zink (2010, Lemma 27 and Theorem 28) construct nonextendible abelian schemes on punctured spectra of mixed-characteristic regular local rings by the finite-flat-group/quotient mechanism suggested here. One cited example is `R=W(k)[[x,y]]/(p−(xy)^(p−1))`; their lemma embeds a Cartier-dual group into an abelian scheme and takes a quotient over the punctured spectrum that does not extend. This is a direct modern realization of the indicated failure mechanism, with the later paper supplying the proof.

### SM14 — Those examples satisfy the manuscript's all-prime nonramification condition

**Witness/kind:** 12/142, lines 14–17, interpreted with 12/140; own idea. **Quotation:** “∀l … non ramifié sur S_l.” **Confidence/reason:** high, because the deduction uses purity for finite étale covers and the literal open subset `S[1/p]`. **Context search:** `non ramifié|dim 2|image inverse` → Hua XIII; no CT counterexample; this **adds** the exact comparison that Hua leaves open. **Bears on:** WG2 §2.4 #3 and WG2 §3.2 #7, unchecked plans.

Let `A_U` be one of the nonextendible examples of SM13, where `U=S\{m}` and `S=Spec R`; for every l different from p its finite étale torsion covers on U extend uniquely to S by regular-local purity (Stacks Project, Tag 0BMA(1)). For l=p, the required open subset `S[1/p]` lies in U, where the abelian scheme already exists, so its p-adic representation is unramified relative to that open. Hence the generic abelian variety meets all the manuscript's l-adic conditions but cannot extend to S, since an extension would restrict to the unique model `A_U`. This deduction answers the unrestricted sufficiency question, and does not claim a new counterexample beyond the cited literature.

### SM15 — Low ramification gives a genuine positive range

**Witness/kind:** 12/142, dimension-two question; unpursued implication. **Quotation:** “peut-être pas au général.” **Context search:** `dim 2|réduction|plat` → Hua XIII, unclosed question; no matching positive range in CT. **Relation:** this **adds** a later restriction of the failure range. **Bears on:** WG2 §2.4 #3, unchecked plan.

Vasiu–Zink (2010, Corollary 4) prove extension over a regular local mixed-characteristic base when `p∉m^p`, equivalently when its absolute ramification index is at most `p−1`. Thus the correct research question is sensitive to local ramification, not just to dimension and characteristic. Their positive theorem and counterexamples should be recorded together.

### SM16 — The pullback problem is a structural gap

**Witness/kind:** 12/142, lines 28–36; self-flagged. **Quotation:** “il n'est pas du tout clair comment définir l'image inverse.” **Context search:** `image inverse|fibres|lissité` → Hua XIII, final paragraph; CT 16/56 gives base change for schemes, not pullback for these generic-point-defined motives. **Relation:** the page **confirms** Hua's diagnosis and **differs** from the formal pullback stability asserted for admissible sheaves on 12/125. **Bears on:** WG2 §3.2 #7 and WG2 §2.4 #3, unchecked plans.

A map from a closed point of S has no map from its residue field into the generic field K, so an object defined only over K plus unramified realizations does not automatically have a motivic fibre there. The examples in SM14 show why sheaf-theoretic extension of all the l-adic data is insufficient to construct an abelian-scheme model. This is precisely the manuscript's own obstruction to turning the definition into a relative theory with pullback and six operations.

### SM17 — The uncertain characteristic-zero criterion stays uncertain

**Witness/kind:** 12/142, lines 19–20; reading question. **Quotation:** `critique|néronique` in the frozen transcription. **Context search:** `critère|caractéristique nulle|réduction` → Hua XIII (does not resolve the name); CT 44/9 mentions Ogg but supplies no identification. **Relation:** the context **does not resolve** the reading. **Bears on:** WG2 §2.4 #3, unchecked plan.

The clear mathematical distinction between the dimension-one and characteristic-zero clauses does not identify the illegible name in the second parenthesis. Neither the later purity theorem nor the first clause's named Néron–Ogg–Shafarevich criterion licenses inserting a name into the frozen text. A future comparison with another manuscript witness should record a reading proposal separately.

### SM18 — The reduction to a prime index still needs proof

**Witness/kind:** 12/142, lines 25–26; unproved claim. **Quotation:** “il y en aurait aussi avec un indice premier.” **Context search:** `indice premier|sous-groupe fini|plat` → Hua XIII omits this reduction; CT 16/56 discusses finite étale algebras but does not give this subgroup reduction. **Relation:** the frozen page **adds** an unproved strengthening beyond Hua's summary. **Bears on:** WG2 §2.4 #3, unchecked plan.

A reduction from a finite generic subgroup to a prime-order step must preserve the base hypotheses and the failure of flat extension, rather than merely factor the order of the group over an algebraic closure. In particular, a finite Galois module need not have a Galois-stable subgroup of prime order, and a field extension that creates such a subgroup can change the regularity or ramification of the base model. The later examples cited above establish failure of extension but are not, by themselves, a verification of this additional prime-index reduction.

## 3. Primary bibliography, in APA form

Deligne, P., & Milne, J. S. (1982). Tannakian categories. In P. Deligne, J. S. Milne, A. Ogus, & K.-y. Shih, *Hodge cycles, motives, and Shimura varieties* (Lecture Notes in Mathematics, Vol. 900, pp. 101–228). Springer. Corrected author-hosted version dated August 15, 2012: https://www.jmilne.org/math/xnotes/tc.pdf . Checked: Proposition 2.23, Theorem 4.17, Definition 5.12.

Faltings, G. (1986). Finiteness theorems for abelian varieties over number fields. In G. Cornell & J. H. Silverman (Eds.), *Arithmetic geometry* (pp. 9–26). Springer. https://www-fourier.univ-grenoble-alpes.fr/~lefourns/contenu/Zywina/Faltings.pdf . Checked: §1(a)–(b), §2 Lemma 1, §5 Theorems 3–4; this is the English translation of the 1983 research paper, not a secondary account.

Mochizuki, S. (1999). The local pro-p anabelian geometry of curves. *Inventiones Mathematicae, 138*(2), 319–423. https://doi.org/10.1007/s002220050381 . Author-hosted primary text: https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf . Checked: Theorem A/16.5; author's June 2019 comments contain two typographical corrections, https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves%20%28comments%29.pdf .

Serre, J.-P., & Tate, J. (1968). Good reduction of abelian varieties. *Annals of Mathematics, 88*(3), 492–517. https://doi.org/10.2307/1970722 . Primary text: https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf . Checked: §1 Theorem 1 and Corollary 1, §2 Theorem 3.

Stix, J. (2008, July 28). *On the period-index problem in light of the section conjecture* [Preprint]. https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXperiodindexSC-28July2008.pdf . Checked: Appendix A, Theorems 21 and 26; cited in the version actually opened.

Tamagawa, A. (1997). The Grothendieck conjecture for affine curves. *Compositio Mathematica, 109*, 135–194. https://doi.org/10.1023/A:1000114400142 . Primary text: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1992BA14A2D63FA076DB39A34EC45E83/S0010437X97000614a.pdf/div-class-title-the-grothendieck-conjecture-for-affine-curves-div.pdf . Checked: Proposition 1.11, §7C's statement of Nakamura's cyclotomic-normalizer theorem; no claim here that an open normalizer alone satisfies its hypothesis.

Tate, J. (1966). Endomorphisms of abelian varieties over finite fields. *Inventiones Mathematicae, 2*, 134–144. https://doi.org/10.1007/BF01404549 . Primary text: https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf . Checked: §1 main theorem.

The Stacks Project Authors. (2026). *Purity of branch locus*, Lemma 58.21.3(1), Tag 0BMA. https://stacks.math.columbia.edu/tag/0BMA . Only the finite-étale-cover extension assertion in clause (1) is used.

Vasiu, A., & Zink, T. (2010). Purity results for p-divisible groups and abelian schemes over regular bases of mixed characteristic. *Documenta Mathematica, 15*, 571–599. https://doi.org/10.4171/DM/307 . Primary text: https://arxiv.org/pdf/0909.0969 . Checked: definitions of (quasi-)healthy, Corollary 4, Lemma 27 and Theorem 28; the theorem, not an unchecked search snippet, supplies the examples.

## 4. Retrieval references for root's independent opening

The final notes should use the APA references above; these IDs document the research retrieval and allow the root to open the same sources before using them.

| Source | Primary retrieval ref | Relevant retrieved passage |
|---|---|---|
| Tate (1966) | `turn161978589view1` | lines 6–16, main Hom theorem |
| Faltings (1986) | `turn940556331view0` | lines 49–59 extension lemma; lines 525–536 Theorems 3–4 |
| Mochizuki (1999) | `turn306296110view0`, `turn332193155view2` | Theorem A, lines 37–49 |
| Deligne–Milne | `turn992336115view0`, `turn332193155view3`, `turn732519463view2` | Proposition 2.23; Definition 5.12 |
| Serre–Tate | `turn161978589view0` | lines 60–79; lines 207–217 |
| Stix | `turn306296110view2`, `turn442407097view0` | Theorem 26 lines 796–804; front matter title/version |
| Tamagawa | `turn731390474view1`, `turn940556331view1`, `turn940556331view3` | Proposition 1.11; §7C |
| Vasiu–Zink | `turn306296110view1`, `turn732519463view1`, `turn310179831view2` | Lemma 27/Theorem 28; Corollary 4 |
| Stacks purity | `turn731390474view0` | clause (1), lines 23–25 |

## 5. Assembly cautions

1. The thickness counterexample concerns extension closure in **generic motives**, not the internal torsion Serre quotient of a category already required to be smooth. This distinction prevents a spurious contradiction.
2. The Vasiu–Zink result and the all-prime comparison are separate: the former is published, while SM14 is our explicit deduction relating it to the exact definition in 12/140–142.
3. Hua XIII differs from the frozen text at least in its replacement of proper by projective and its normalization of the isomotif's base from S to K; those are research reading questions, not authority to change the transcription.
4. No status in LM6/LM7/FLAGGED_149 is upgraded by this contribution. The weights do not establish nonlinear subgroup detection or section-surjectivity.
