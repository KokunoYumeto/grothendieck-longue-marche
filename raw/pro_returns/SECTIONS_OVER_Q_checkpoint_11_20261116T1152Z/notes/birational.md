# Birational route: proofs, exact maps, and audited scope

Prepared by the birational subagent for integration. These notes do **not** settle A1 or B1.
All sections below are continuous and all geometric conjugations are named explicitly.
The October 2026 local section theorem is not used in any proved assertion in these notes.

## 1. Sources opened and precise statements

1. Jakob Stix, *On the birational section conjecture with local conditions*, Inventiones mathematicae **199** (2015), 239–265, DOI 10.1007/s00222-014-0514-3. Opened attached arXiv:1203.3236v3 LaTeX and author PDF `https://www.math.uni-frankfurt.de/~stix/research/preprints/STIX-birSCoverQthmAB20140227.pdf`. Web ref `turn1view0`; derived finds `turn18view4`. The attached source's introduction uses Theorem A/B as crossreference labels; author PDF displays Theorem A and Theorem B. The internal results used below are Proposition 1, Proposition 2, Theorem 4, Corollaries 5–7, Corollary 15 and Theorem 20 (verify final numbering from the opened final PDF when assembling bibliography).
2. Jochen Koenigsmann, *On the 'section conjecture' in anabelian geometry*, J. reine angew. Math. **588** (2005), 221–235. Opened attached arXiv:math/0305226 source and `https://arxiv.org/pdf/math/0305226`; web refs `turn15view0`, `turn18view3`. Proposition 2.4(2), combined with Definition 1.4, proves the full birational section property over every finite extension of Q_p and over R. Proposition 2.4(1) proves the weak property over p-adically closed and real closed fields. Corollary 2.6 says that a smooth complete curve over a number field with a birational section has a point in every completion. Lemma 1.7 supplies the compactness argument over local fields.
3. Florian Pop, *On the birational p-adic section conjecture*, Compositio Math. **146** (2010), 621–637, DOI 10.1112/S0010437X09004436. Opened publisher PDF `https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B741897537145744E3B12058A67D221D/S0010437X09004436a.pdf/div-class-title-on-the-birational-span-class-italic-p-span-adic-section-conjecture-div.pdf`, web ref `turn1view1`. Theorem A assumes k/Q_p finite and mu_p contained in k. Write K=k(X), K^0 the maximal elementary abelian p extension and K^{00} the maximal elementary abelian p extension of K^0. Every section of Gal(K^0/K)→Gal(k^0/k) which lifts to the double extension is associated with a unique k-rational point of smooth complete X. The mu_p hypothesis is explicit and essential for this quotient theorem. Full birational sections over arbitrary finite k/Q_p are already covered by Koenigsmann.
4. Niels Borne, Michel Emsalem, Jakob Stix, *Lifting Galois sections along torsors*, Math. Nachr. **288** (2015), 1939–1951, DOI 10.1002/mana.201400251; opened attached arXiv:1301.4429v2 LaTeX and abstract, web ref `turn15view1`, and author PDF `https://www.math.uni-frankfurt.de/~stix/research/preprints/BORNE_EMSALEM_STIX-lifting_short20150324.pdf`. In the attached version, Definition 2.1 constructs the diagonal torus torsor and Propositions 3.1, 3.4, 3.5 establish its fundamental group exact sequence, arithmetic action on the kernel, and identification with the cuspidally central quotient. The author's earlier March 2015 PDF instead numbers these Definition 1 and Propositions 8, 11, 12; its text is opened as `turn33view1`, `turn40view1`. These propositions are stated in the generality required for the affine tripod. The proper positive-genus hypothesis begins in Section 4 for the subsequent cohomological arguments, after the needed Section 3 comparison.
5. Giulio Bresciani, *On the birational section conjecture with strong birationality assumptions*, Inventiones mathematicae **235** (2024), 129–150, DOI 10.1007/s00222-023-01220-6. Opened attached arXiv:2108.13397 source and publisher `https://link.springer.com/article/10.1007/s00222-023-01220-6`, web ref `turn12view1`. Theorem A identifies geometric/cuspidal sections with sections whose base change to k(T) admits a birational lift. Theorem B quantifies over **all finitely generated extensions K/k**. Theorem C is the precise interpolation formulation of the birational conjecture. Its proof is not replaced by a claim that individual lifts interpolate.
6. Florian Pop, *Generalizations and minimalistic refinements of the t-birational Section Conjecture*, arXiv:2604.26131v1, `https://arxiv.org/html/2604.26131v1`, web refs `turn12view0`, `turn23view0`. Opened the introduction, definitions, Theorems 1.3 and 1.7, and open questions. It retains a transcendental-base lifting condition. No theorem from it is invoked here. Metadata anomaly: arXiv header says 28 April 2026, body says “Variant of April, 2027”; report this if citing this version, and do not infer publication status from the body date.

Literature searches performed: “Stix On the birational section conjecture with local conditions 2015 Theorem A B”; “Pop birational p-adic section conjecture theorem 2010 Koenigsmann”; “section conjecture tripod 2026”; “birational section conjecture 2026 2025”; “Bresciani strong birationality theorem A”. Searches returned no proof of A1/B1 used here. The main new item found for this investigation is Pop's t-birational refinement; it has an additional lifting input and hence supplies no missing section of the original extension.

## 2. Exact result answering A2 and L1

Let k be a number field, X/k a smooth geometrically connected hyperbolic curve, Xbar its smooth projective completion, and K=k(X). Fix an algebraic closure Kbar and its subfield kbar. The generic point induces continuous surjections

    q_X:G_K→π_1(X),     q_X|geom:G_{K kbar}→π_1(X_kbar).

They commute with projection to G_k. They induce the map on section classes

    q_X*:Sec(K/k)→Sec(X/k),

with conjugations by G_{K kbar} and π_1(X_kbar), respectively. Its image is Stix's set Sec^bir(X/k).

For a section s in this image, Stix Proposition 1 proves that each s_v is a point or cuspidal section, and supplies its center x_v in Xbar(k_v) at finite v. At infinite v the étale section specifies a connected component. In the resulting modified adelic set, Stix Theorem B proves the following alternative: either s is globally cuspidal, or the set of v for which x_v is integral on X has Dirichlet density one.

Stix's definition in §2.2.3 is precise: s is birationally adelic when **there exists one birational lift τ** such that the section q_Vτ on every nonempty open V⊂X is adelic on V or is cuspidal. “Adelic on V” requires ordinary local sections everywhere and integral local points at all but finitely many finite places, relative to a model of V outside a finite set. Theorem A proves the bijection between X(k) and noncuspidal birationally adelic section classes when k is totally real or imaginary quadratic. For k=Q the hypothesis holds on the field. For the tripod, Corollary 6 gives the sharper directly applicable conclusion that every adelic section of U is a rational point section, since the unit t is nonconstant. Neither assertion changes density-one integrality to cofinite integrality.

The exact comparison of sets is

    Sec^ba(X/k) ⊂ Sec^bir(X/k) ⊂ Sec(X/k),

where the first map forgets the specified adelic requirements on the chosen lift and the second forgets birational liftability. This inclusion follows directly from the definitions. No converse is claimed by the invoked theorem. A proof of equality of these sets is not supplied here.

### Local comparison without an illicit completion base change

A birational section over k does not canonically base change to G_{k_v(X)}: k_v/k is generally transcendental and the map

    G_{k_v(X)} → G_{k(X)} ×_{G_k} G_{k_v}

is not being identified with an isomorphism. Stix expressly warns about this in §2.2. Instead apply Koenigsmann Corollary 2.6 to each finite section-neighbourhood and use compactness of the local points of its proper completion. The intersection of finitely many neighbourhoods is another neighbourhood, and its local point maps into all the finite list of local spaces. Thus these closed compatibility conditions have the finite intersection property. Their compact inverse limit supplies a compatible pro-point. Its image in Xbar(k_v) is the local center, and its lift to every finite étale neighbourhood gives exactly the local point/cusp section. This argument invokes no October 2026 local theorem.

The local full birational theorem itself is: for a finite extension k/Q_p and a smooth complete geometrically connected curve X/k, every continuous section of G_{k(X)}→G_k has image in a decomposition group of a k-rational point of X. Koenigsmann Proposition 2.4(2), Definition 1.4 and Lemma 1.7 give this statement. Pop Theorem A gives the specified quotient refinement under mu_p⊂k; it does not remove the global number-field step.

## 3. A1: point and cusp classes have actual birational lifts

For x∈P^1(Q), choose the parameter z=t−x for x finite and z=1/t for x=∞. A prolongation of the z-adic valuation to Q(t)^sep gives an exact sequence of profinite groups

    1→I_x≅Zhat(1)→D_x→G_Q→1.

It splits: in the algebraic Puiseux closure of Qbar((z)), fix compatible roots z^(1/n) and let G_Q act on coefficients and fix these roots. Each algebraic series has coefficients in a finite number extension; the action is continuous on every finite extension. Restriction realizes a continuous splitting inside the absolute Galois group of the henselization, hence inside G_{Q(t)}.

For x∈U(Q), q_U kills I_x and takes every such splitting to the point-section class s_x. For x one of 0,1,∞, the map D_x→D_x^U is an isomorphism: it is the identity on residue G_Q and an isomorphism on tame inertia Zhat(1). The inertia injection in the hyperbolic model follows from the free profinite geometric fundamental group and the primitive peripheral generator. Consequently every section in a cusp packet, including every profinite tangential Kummer parameter, lifts through this isomorphism. A geometric conjugator in π_1(U_Qbar) lifts under the surjection G_{Qbar(t)}→π_1(U_Qbar), so this also supplies lifts of chosen conjugate representatives.

This proves the actual containment

    {point classes and cusp classes} ⊂ image(Sec(Q(t)/Q)→Sec(U/Q)).

It does not construct a lift for an arbitrary section. The unresolved extension is

    1→ker(q_U)→G_{Q(t)}×_{π_1(U),s}G_Q→G_Q→1.

No section of this extension has been produced here for a section outside the point/cusp classes.

## 4. Finite étale transfer and exact scope of Belyi

Let f:Y→X be a finite étale morphism of smooth geometrically connected curves over k. Choose compatible geometric base points; f_* identifies π_1(Y) with an open subgroup H of π_1(X), and π_1(Y_kbar)=H∩π_1(X_kbar). For a section r of Y, its image s=f_*r is a section of X. A conjugator needed to choose s as a specified representative is taken in π_1(X_kbar); it changes the chosen fibre point, hence replaces H by its corresponding conjugate.

For a point section s_x, the inclusion s_x(G_k)⊂H is exactly a G_k-fixed element of the finite fibre f^−1(x)(kbar). This is a k-point y∈Y(k). Choose the compatible fibre path at y. Both r and s_y then have image s_x in π_1(X), and injectivity of f_* proves equality. On section classes, the full inverse image of the class of s_x consists exactly of the point classes at Y_x(k).

For a cusp c of X, normalize the smooth completion of X in Y. The intersection H∩D_c is the decomposition group at the corresponding point above c. When it contains the image of r, its projection to G_k is surjective. Its residue-field image is G_{k(d)}, so this forces d to be k-rational. Thus r lies in a rational cusp packet of Y. These statements use the ordinary finite étale fibre correspondence and normalization of curves, not a classification theorem for arbitrary sections.

The resulting map statement proves that the preimage of the point/cusp locus of Sec(X/k) is the point/cusp locus of Sec(Y/k). Applied to finite étale covers of U/Q, this is the precise transfer needed by A1. A Belyi map β:C→P^1 over Q makes C\β^−1{0,1,∞} a finite étale cover of U. The transfer controls sections of that **open** curve. A section of the proper C requires a lift through π_1(C\β^−1{0,1,∞})→π_1(C) before this argument applies. The map on arithmetic Galois groups for a number-field extension K/Q is restriction G_K→G_Q; it takes Q-sections to K-sections and does not construct extensions of arbitrary K-sections. No conclusion for all sections over every number field is deduced from A1 over Q alone.

## 5. Central lifting on the tripod has an elementary global splitting

Let k be any characteristic-zero field, U=P^1_k\{0,1,∞}, D⊂U finite and reduced, and W=U\D. Put T_D=Res_{D/k}G_m. By restriction of scalars, the function t−a on W×_kD defines a k-morphism f_D:W→T_D. Here a is the tautological coordinate on D and t is the coordinate on W. The morphism

    (j,f_D):W→U×_kT_D

induces a continuous homomorphism over G_k from π_1(W) to π_1(U×T_D)=π_1(U)×_{G_k}π_1(T_D). Let N=ker(π_1(W)→π_1(U)). Let N_cc be the closed normal subgroup generated by [N,π_1(W_kbar)]. Then N/N_cc is abelian and its geometric π_1(U_kbar)-action is trivial. The map factors through

    π_1(W)^{cc,U}=π_1(W)/N_cc.

It induces an isomorphism

    π_1(W)^{cc,U} ≅ π_1(U)×_{G_k}π_1(T_D).             (CC)

Proof over kbar: list the m geometric points a_i of D. The free profinite group π_1(W_kbar) has generators γ_0,γ_1,δ_1,…,δ_m; the peripheral element at ∞ is the inverse of their product. The quotient by [N,π_1(W_kbar)] has precisely the relations making each δ_i central, hence it is Fhat_2×Zhat^m. The map f_D sends δ_i to the i-th basis vector of π_1((T_D)_kbar)=Zhat(1)^m, while γ_0 and γ_1 have zero winding in these coordinates. Therefore the induced map is an isomorphism on geometric kernels. It is the identity on G_k, so the exact-sequence diagram gives the arithmetic isomorphism (CC). Equivalently, this is BES Proposition 3.5 applied to its diagonal torsor; that torsor is globally trivial because t−a is an equation of the diagonal on D×U.

The k-point 1∈T_D(k) supplies a continuous section of π_1(T_D)→G_k. Therefore

    e↦(e,s_1(p_U(e)))

is a continuous splitting π_1(U)→π_1(W)^{cc,U}. For every continuous section s of U its composite is a central lift. These splittings are compatible as D varies: for a disjoint union of divisors, the torus and its distinguished identity point are products, and forgetting a divisor is the corresponding projection. Thus compatible arbitrary central lifts on the fixed tripod are unconditional and require no local classification theorem.

This assertion concerns the explicitly defined quotient. Full lifting requires a lift through the additional continuous surjection π_1(W)→π_1(W)^{cc,U}. The construction (CC) does not give that lift.

## 6. A central lift which has no birational lift

Take k=Q, D={3}, and W=U\{3}. In (CC), take the central section

    r_cc=(s_2,s_1),

where s_2 is the point-section at t=2 of U and s_1 is the point-section at 1 of G_m. Its additional Kummer coordinate t−3 has class 1 in Qhat^×. No birational section τ of G_{Q(t)}→G_Q maps to this r_cc.

Proof. Such τ would give a birationally liftable section of W and hence a Selmer section, by Koenigsmann and Stix Proposition 1. Its image on U is s_2. The 3-adic center on U is 2: point sections over Q_3 are injective for the hyperbolic curve, and the point/cusp images are disjoint; alternatively this particular separation is checked by the coordinates t and 1−t as follows. At an ordinary point x, the completion Q_3^×→Qhat_3^× is injective, so κ(x)=κ(2) forces x=2. At cusp 0 one has κ(1−t)=1, contradicting κ(−1)≠1; at cusp 1 one has κ(t)=1, contradicting κ(2)≠1; at cusp ∞ one has κ((1−t)/t)=κ(−1), contradicting κ(−1/2)≠κ(−1). Thus the center is the ordinary point 2. The local center in W is also 2, since the deleted point 3 would map to the point 3 in U. Consequently the t−3 Kummer coordinate at 3 is κ(−1). The prescribed central coordinate is κ(1). Their modulus-two images differ because −1≡2 mod 3 is a nonsquare. Contradiction.

The finite certificate is `work/code/birational_central_certificate.py` and its output. The elementary assertion Q_3^×→Qhat_3^× is injective follows from Q_3^×≅3^Z×mu_2×(1+3Z_3), with the last group identified with additive 3Z_3 by the 3-adic logarithm; each factor injects into the inverse limit of power quotients. No October 2026 local theorem is used.

This example refutes the inference that an arbitrary chosen central lift extends to a birational lift. It does not refute A1(2): the point section s_2 has birational lifts whose central coordinate is −1.

## 7. Correction to R9, A8, and L20

The attached AP D.27 proves precisely a criterion for **canonical central lifts**. At each modulus n it requires the prescribed local Kummer classes to be in the restricted product and orthogonal to all H^1(k,Z/n) characters. Poitou–Tate exactness then supplies a global class, and finite fibres give compatible classes over all n. Its text expressly states that this "does not solve its nonabelian lifting problem." The prompt's R9 sentence and A8 lead promote that conclusion to a full lift of π_1(W); the cited proof does not make that promotion.

The comparison maps are

    π_1(W) → π_1(W)^{cc,U} → π_1(U).

The second arrow has the global splitting proved above. Reciprocity supplies a section of the middle group with prescribed local abelian coordinates. A full section is a lift through the first arrow. The exact unresolved kernel is N_cc, not the already split torus kernel N/N_cc. Thus the reciprocity criterion is a necessary compatibility test for the proposed canonical coordinates, and it is sufficient for a canonical central lift; sufficiency for a full section remains unproved here. An invalid proof of sufficiency is not a counterexample to sufficiency.

The second ingredient in L20 is also stronger than mere individual nonemptiness. Countable inverse systems with nonempty terms can have empty inverse limit: S_n={m∈N:m≥n}, transition inclusions. For continuous maps into finite groups, the set Hom_cont(G_Q,F) need not be finite or compact in pointwise topology. A valid compactness argument must provide compatible finite fibres or sequential surjectivity, neither of which follows merely from the arbitrary central splittings (CC). BES/AP norm obstruction gives a concrete geometric failure of arbitrary central-lift compatibility between different étale neighbourhoods; see AP D.24.

## 8. The configuration-space morphisms behind L20

Put F=(U×_Q U)\Δ=M_{0,5}, with p_1(t,z)=t and p_2(t,z)=z. Choose compatible geometric base points. The smooth fibration p_1 has geometrically connected fibre P^1\{0,1,∞,t}; the homotopy exact sequence gives

    1→Fhat_3→π_1(F)→π_1(U)→1.

For a chosen section s:G_Q→π_1(U), define the profinite fibre product

    Π_s=π_1(F)×_{π_1(U),p_1,s}G_Q.

The projection to G_Q is a continuous extension with kernel Fhat_3. It carries the continuous morphism h_s:Π_s→π_1(U) given by p_2 on the first component; h_s commutes with G_Q projections.

For x∈U(Q), the k-morphism i_x:U\{x}→F, t↦(t,x), identifies π_1(U\{x}) with the subgroup p_2^{-1}(s_x(G_Q)) of π_1(F). To verify this, use the exact sequence of p_2; i_x induces the identity on the geometric fibre group Fhat_3 and the identity on G_Q. It is therefore an isomorphism onto this inverse-image subgroup. The ambiguity in i_x* is conjugation by the geometric fibre group, after a fibre path is chosen.

It follows that the set of chosen lifts of s to π_1(U\{x}) is identified with the set of continuous sections r:G_Q→Π_s satisfying h_s r=s_x, with the same compatible choices of paths. This is the rigorous content of the interchange of the two points in L20.

The extension Π_s itself always has a tangential splitting along the boundary z=0; in the family its normal line is trivial and z is a global parameter. Its second projection is a cusp section of U. Existence of some splitting of Π_s therefore does not identify s with a rational parameter. Carrying all rational point sections under h_s is an additional property, and the interpolation of these individual lifts is precisely the further input appearing in Bresciani Theorem C.

The relative double cover y^2=z(z−1)(z−t) is finite étale over F. Its smooth compactification over the t-coordinate is the Legendre elliptic curve. Taking its first étale homology in the fibres and pulling back along s produces the Legendre Tate representation. This supplies the exact geometric map connecting the configuration extension and the representation, without reconstructing an actual t-coordinate from Π_s.

## 9. Every birational section supplies the (G) data

Let τ:G_Q→G_{Q(t)} be a continuous birational section. The Kummer class of t−c lies in H^1(G_{Q(t)},Zhat(1)). Pullback defines

    u_c=τ^*κ(t−c)∈H^1(G_Q,Zhat(1))=Qhat^×       (c∈Q).

There is a compatible system of local pro-points at every place for all finite normalizations of P^1 whose fundamental groups contain τ(G_Q). To construct it, take the fixed field of τ(G_Q), take its finite subextensions over Q(t), apply Koenigsmann Corollary 2.6 to their smooth projective models, and use compactness. Every finite collection is dominated by its compositum, again a section-neighbourhood, so the finite intersection property holds. At the real place this selects an actual real point of P^1(R) in addition to the connected-component data of the individual étale sections.

Write x_v for the image in P^1(Q_v). Fix c and n. Let a_n∈Q^× represent the modulus-n class of u_c. The Kummer torsor z^n=(t−c)/a_n over P^1\{c,∞} has a τ-fixed point in its geometric fibre, by definition of the pullback class. Its normalization therefore occurs among the section-neighbourhoods. When x_v≠c,∞, the compatible local pro-point gives z_v∈Q_v^× on that torsor, hence x_v−c=a_n z_v^n. This proves loc_v(u_c)=κ(x_v−c) at every modulus, including the real sign for even n. Thus τ supplies an actual configuration satisfying the literal hypothesis (G).

Root's counterexample to (G), with x_2=∞ and x_v=2 at every other place, cannot occur in this comparison image: the section on U would have center 2 on a density-one set; the finite-support result R2 then forces s=s_2, and its local center at 2 is 2. This exhibits an additional constraint on the comparison image, but does not prove that all its elements are diagonal.

A13 therefore has a rigorous comparison map and a false proposed target rigidity statement. We do not infer A1 from the false statement or present the requested implication as substantive progress.

## 10. L21: the exact inertia comparison

For a point x∈U(Q) and a birational lift τ lying in D_x, the full cyclotomic kernel H_Q=ker(χ:G_Q→Zhat^×) acts trivially on I_x≅Zhat(1). Thus

    I_x ⊂ C_{G_{Qbar(t)}}(τ(H_Q)),   q_U(I_x)=1.

This already proves the actual morphism connecting the two fixed-group pictures in scan 49. The equality of the birational fixed group with I_x follows from the supplied R15 by an inverse-limit argument: for every hyperbolic open V deleting x, q_Vτ is cuspidal and its fixed group is I_x's image; the peripheral inertia map is injective. Fix one such V_0 and match a centralizer element to a∈I_x at that level. For every smaller V the inertia comparison is an isomorphism, so their images agree. Since G_{Q(t)}=lim_V π_1(V), the elements agree in the full group. This is exactly the checked transition argument in CK B7 and LM6 F.13. This paragraph derives the equality from R15; it does not independently reprove R15.

## 11. State of the remaining main work

* A1(1): unresolved. The proven subsets are geometric/cuspidal sections, birationally adelic sections via Stix, and sections with transcendental-base birational lifting via Bresciani. None of the maps constructed here produces either enhanced lifting property for an arbitrary s.
* A1(2): unresolved. Arbitrary central lifts are constructed uniformly and an explicit chosen central lift is proved unable to arise birationally. The kernel N_cc between the full group and the central quotient remains in the embedding problem.
* B1: unresolved. The local center construction and all rational-function Kummer coordinates exist. Their global compatibility has not produced a Q-rational valuation. Root's refutation of (G) removes that proposed general rigidity lemma.
* A8 full lifting equivalence: unresolved. Exact reciprocity reconstructs the canonical central class. The required first arrow π_1(W)→π_1(W)^{cc,U} remains unsplit over that class.
* A9 full single-puncture lifting: unresolved. The configuration-space reformulation and central splittings are proved; simultaneous full lifts and interpolation remain unproved.
* A13: comparison construction proved; no conditional theorem is asserted because literal (G) is false.
* A11: unresolved. Stix's local-center and density-one statements apply over every number field, its rationality result over the stated totally real/imaginary quadratic fields, and Bresciani's theorem over all finitely generated characteristic-zero fields with its additional t-lifting input.

Next mathematical attack from this branch: prove or refute full lifting of the prescribed canonical central class through N_cc for a single added puncture, or establish Bresciani's interpolation condition for the full family of rational puncture lifts. Merely producing more arbitrary central classes cannot resolve either requirement, as the explicit t=2, deleted-point-3 example proves.

## 12. Carlson--Corwin, 6 November 2026: exact comparison with B.9--B.14

Primary source opened in full: Magnus Carlson and David Corwin, *Cuspidal sections for varieties of arbitrary dimension*, arXiv:2611.09080v1, <https://arxiv.org/html/2611.09080v1>. Bibliography key `BIR_CarlsonCorwin2026`.

Theorem 3.7 proves independence of the **closure** of the cuspidal set from a normal-crossings compactification. Under a proper birational map X'→X that is an isomorphism on U, Lemma 3.10 gives C(U,X')⊂C(U,X) by the actual nearby-scheme map. Lemma 3.11 proves the reverse inclusion after closure: local boundary equations identify the nearby fundamental group with that of a quasi-trivial torus; rational arcs through the boundary lift by properness and give a dense translate of rational Kummer classes. Proposition 4.12 gives C_X⊂closure(C_X,f) for a hyperbolic-polycurve tower. Above an interior point of its base, its proof identifies the fibre's nearby fundamental group with the total nearby group by the bijection of local boundary branches. Remark 3.5 corrects Stix (2013), (18.3): the kernel uses **strict** nearby points. Proposition 4.11 expresses tower independence through explicit products of curve section loci and proves its equivalence to the curve section conjecture under injectivity.

The comparison with our examples is concrete. The map in B.12 from the blown-up crossing sends its two inertia generators to the same peripheral generator; this is the same direction as the nearby map in Lemma 3.10. Its anti-diagonal kernel persists. The distinct flags in B.10 still have identical inertia images under their two explicit field-to-model maps. Proposition 4.12 constructs maps on sections, with no inverse map reconstructing those flags from inertia. For B.14, the displayed iterated-Puiseux splitting remains an actual lift; the new source gives no construction of such a splitting for every section over the bad base cusp. Consequently the paper updates the known cuspidal comparison, while the exact unresolved lifting problem remains the one already displayed in B.14--B.15. No additional numbered claim is needed.
