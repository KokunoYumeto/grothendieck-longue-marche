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


## Independent A182 audit, 2026-11-16 14:29 UTC

Read the entire saved point3_fermat8_decomposition.tex and reran its consolidated certificate, including both companion exact surface programs. PASS: all twelve literal maps, all21 differential weights/scalars, Prym cotangent factor2, good Prym reductions, torsion at every prime including residue characteristics, divisor non-two-torsion, irreducible Frobenius simplicity overQ, product isogeny and the Weil-restriction/Jacobian map for a finite-point target over any number field. No pairwise nonisogeny or absolute simplicity is needed. No rank upper bound follows from the source.

Independently opened the author PDF https://jmilne.org/math/CourseNotes/AV.pdf (version2.00,16March2008). Exact verified inputs: I16.7 at printed69 (finite generation); II1.1 printed75 (abelian finite-field point count); III6.1 printed104 (pointed Jacobian universal property); III11.1 printed118 (curve trace formula); IV3.5/3.6 printed141–142 (good-reduction/Tate representation and isogeny preservation). The exact chapter qualifications in the saved bibliography are correct.


## 2026-11-16 14:55 UTC: A186 genus-two rank arithmetic audit

The local GP certificate point3_fermat8_genus2_rank_certificate.gp was independently read and rerun using the retained local PARI2.19.1 runtime. Its output is byte-for-byte identical to the peer output and is retained as code/point3_fermat8_genus2_rank_birational_rerun.txt. The installed primary manual doc/usersch3.tex, bnfcertify entry, explicitly gives omitted flag0 and certifies the full class group and full units; flag1 would prove only quotient/subgroup statements. The certificate uses flag0. The exact S-class groups, literal S-unit squareclass basis matrices, all17 actual local square witnesses, all primewise Hilbert products, and all six kernel dimensions2 pass.

The actual monic model map is x=A X,y=A²Y from Y²=A X⁵+B X to y²=x⁵+A³B x. For the split degree5 algebra Q×K, K=Q(theta), theta⁴+c=0, the coefficient map is eta↦(Norm eta,eta). A local point x=q maps to (q,q−theta), since Norm(q−theta)=q⁴+c agrees with q modulo squares. The product Weil/Tate pairing is (Norm eta,q)_p times the product of (eta,q−theta)_P; the projection formula gives exactly the peer's product (eta,q(q−theta))_P. The even-subset model of J[2] on the five finite branch points has the dot-product Weil pairing: the complement of one branch represents its divisor class, and two distinct complements have intersection cardinality3. Thus the rows are the actual local Tate pairing, not a replacement pairing.

Opened primary sources: Poonen–Rains, author PDF https://math.mit.edu/~poonen/papers/selmer.pdf, dated17May2011 with6Aug2012 correction, Propositions4.6(c),4.9 and4.11. Corollary4.7 is on printed page16, Proposition4.9 on printed page17, and Proposition4.11 on printed page18 (the latter is the local maximal-isotropic statement in this version). The first audit message inadvertently used zero-based PDF page indices; these are the corrected printed page numbers. Poonen–Schaefer, author PDF https://math.mit.edu/~poonen/papers/descent.pdf, dated10Feb1997, printed pp1–2, states the odd-degree x−T injection and its true Kummer interpretation. The direct degree5 coefficient-module proof above retains the precise maps. With good reduction outside2,3, local Kummer classes have even outside valuations; Cl_S=0 gives the certified S-unit search space. Rational J[2] has dimension1 because x⁴+c is irreducible. Hence the rank lower bound1 from A182 and Sel2 dimension≤2 force rank1 and Sha[2∞]=0 for each of the six genus-two factors. Full A186 source was not yet saved at the time of this arithmetic/map audit.

## 2026-11-16 15:02 UTC: completed A185/A186 source audits

The complete saved A185 source and certificate pass. The two explicit involutions, their degree-two quotient maps, the differential determinant, and the conjugation/Weil-restriction descent identify the three Pryms with the displayed quadratic-field elliptic factors up to actual isogeny. The literal two-isogeny Kummer maps, candidate S-squareclasses, local exclusions and attaining points prove ranks1,2,2; the three rational elliptic factors have rank1 each. The independent certificate rerun is retained separately. No unproved class-group completeness is used in those quadratic-field squareclass bounds.

The complete saved A186 source now also passes. The quartic irreducibility arguments, all literal S-unit generators and local point witnesses, all six displayed matrices and kernel bases, and the rational torsion comparison match the independently executed certificate. The exact coefficient morphism and Hilbert pairing above give the stated Selmer bounds; the A182 positive-rank and torsion inputs give equality. The resulting six ranks1 and the A185 contribution8 give the actual Fermat-eight Jacobian rank14. The statements retain the precise Selmer and isogeny maps.

Independently opened Stoll's primary publisher PDF, https://www.impan.pl/shop/publication/transaction/download/product/83397, *Implementing 2-descent for Jacobians of hyperelliptic curves*, Acta Arithmetica98.3 (2001),245–277. Lemma4.1 and Proposition4.2 on printed250 give the actual H¹/Kummer and Selmer identifications; Lemma4.3 on250–251 gives the point/branch values and rational two-torsion dimension; Proposition4.6 and Corollary4.7 on252–253 give the outside-S valuation condition. All cited hypotheses apply to the six literal odd-degree models.

## 2026-11-16 15:34 UTC: complete A187/A189 audits

The full saved A187 source and its independently rerun exact certificate pass. The explicit quartic-to-two-isogeny-cover maps retain the orientation of both connecting maps. The local upper bounds and attaining points from A185 therefore identify both isogeny Selmer groups with their Mordell--Weil images and kill both elliptic two-primary Tate--Shafarevich groups. The actual unscaled conjugate Prym quotient maps have pullback/pushforward composite [2], descend to the stated Weil restriction, and bound its Prym Sha by exponent two. The A182 product isogeny's actual dual quotient gives the stated safe exponent bound for J8. Finite Kummer transition maps and the continuous Selmer comparison are exact; the final section image conclusion retains its section premise. Reopened Milne's author ADT PDF: I4.15 printed62, I6.4 printed75, and I6.6/I6.7 printed77 give the precise finiteness and Kummer inputs.

The full saved A189 source and exact Chabauty certificate pass. Both polynomial doubling identities, the quadratic-disc branch signs, every reciprocal-binomial coefficient bound and infinite-tail estimate, and the global logarithm slope one versus moving-point slope three modulo four were independently checked. The completed-generator append A186.18--21 gives the exact global Z2D plus C2T coordinates, and the local log/torsion argument proves the two global preimages uniquely. The literal Fermat map and dyadic unit/valuation analysis give exactly four points. The arithmetic section comparison uses the actual H=ker(Pi->(Z/8)^2), Pi'' contained in H', fixed-sheet lift, proper Jacobian map and global T2 Selmer image; it gives the stated dyadic centre without asserting an additional full-section equality.

Primary sources independently reopened: McCallum--Poonen, https://math.mit.edu/~poonen/papers/chabauty.pdf, section4.1 Remark4.1, author p.4; Poonen, https://math.mit.edu/~poonen/papers/Qpoints.pdf, Theorem5.7.25 and Proposition5.7.26, printed143. The smooth unit-coordinate model extends its Abel--Jacobi map to the Neron model. Same-reduction point differences lie in the formal group, including after the quadratic local base change, and the formal primitive computes precisely the abelian logarithm. The proof does not assume good reduction at two.

## 2026-11-16 15:58 UTC: A192/A193/A195 exact source audits

A192 full source and independent certificate rerun pass. The map from the special affine line into the Neron special fibre has zero abelian and toric projections and lands in a smooth connected unipotent group of dimension at most two. Its successive reduced multiplication-by-two images strictly decrease dimension, so multiplication by four kills the image. The restricted integral parametrization and the actual formal coordinates of [4]a therefore identify its logarithm across both residue points, including the lowest positive-valuation case. All positive/infinity primitive formulas and infinite-tail estimates check. The cyclic-eight function-field maps are literal inverses, and the boundary indices are8,8,2. The section comparison retains the actual finite sheet and proper Selmer map. Reopened Poonen Theorem5.4.8(ii), printed128, and the perfect-field chain5.9.1, printed147; both cited hypotheses apply.

A193 full source and isolated certificate rerun pass, the latter retained initially at /tmp/a193_birational_uj2iamft during the checkpoint write freeze. The three local Kummer classes are independent by valuation, exact norm and depth-three unit tests. The local dimension, complete Nakayama and independent logarithms give the literal Z2^2 plus C2 basis. All finite Selmer inequalities are equivalences through that basis. The Schreier relations, compact module Z2[v]/(v^4+1), splitting and arithmetic normality give the exact geometric quotient and class4n. All selected sheets over t=14641/14587 fail n4. An editorial clarification was sent for the logarithm sentence: the completion kills the odd-primary torsion subgroup; its two-torsion T is retained, as the actual proof already requires.

A195 full source and independent consolidated certificate rerun pass. The supported norm rank is5 and the base restriction rank7, making the entire H1 of the cubic augmentation ideal come from its last mu3 line. Naturality of the actual coefficient sequence places every supported Bockstein in the last-line H2 image. The divided w=1+X+X^2 identity gives the actual obstruction, including the top theta9 cup term. Its bottom image is the nonzero tame cup kappa(A) cup kappa(U), with valuation8 and unit character2. Thus the finite supported weight-two class is nonzero. The integral inflation argument applies to the actual two diagonal weights and is injective; absolute finite-coefficient inflation still kills the class. This proves least detecting integral index exactly2 with every source and target retained. The additional independent coefficient audit checks all54 divided-w identities and486 equivariant coefficient squares.


## 2026-11-16 16:39 UTC: A196/A198/A200/A202 audits

A196 full source and independent exact certificate pass, including
the original tangential quotient, normalized4-by-4 matrices, exact
class3, actual coefficient obstruction and order3, finite root-torsor
maps, compatible-conjugacy normalization, and finite supported
solution-set compactness. The local ninth-power append also passes:
v(A)=1, v(B-1)=5, and Y=1 modalpha gives v(Y^9-1)>=6, excluding all
ordinary points; the exact three cusp Kummer lines are excluded as
well. This retains the actual local norm-section scope.

A198 full source and finalized certificate pass. The principal
boundary lattice has index16; the branch Weil map gives the kernel
and the actual Psi construction gives the Tate cokernel. All four
reference constants, tangent inertia lines, dyadic two-choice
framing, and coefficient-three torsion correction check. The exact
convergent determinant/log relation defines the norm-one class;
its571 valuation vector is excluded by all point/cusp cases. The
literal Schreier quotient has order2^21 and class12, and the
fixed-sheet argument transfers the local obstruction downstairs.

A200 full source and independent certificate pass. Both supported
Tate H2 layers have exponent3, so H2(D2) has exponent9. The exact
nonzero3*xi class forces xi to have order9, and integral inflation
retains it. All four image rows, the literal scalar endomorphisms,
the zero parameter, supported first failure, and individual-versus-
coherent norm maps are proved with their actual coefficient maps.

A202 full source and independent certificate pass after reading
A72's actual component and X=1 construction. The enlarged first
CRT precision remains compatible with the fixed splitting field;
later factors are1 modulo2^(E+1), preserving exact depthE. Every
dyadic cover sheet has v2(x-3)=E-3, so the precise finite detector
n=E-2 excludes it with order2^(4E-5), class4E-8. The separate global
class-two and joint finite-Q local statements retain their stated
maps. No simultaneous locally matching class-two lift is inferred.


## 2026-11-16 16:56 UTC — A205 independent full audit

Read all saved source of sections/selmer_central_local_matching.tex.
PASS: actual lift/conjugacy torsor, Hall-weight centralizer proof, real
centralizer translation homomorphism, complete finite local allowed sets,
fixed-support compactness, coefficient-power inverse-limit comparison,
even-weight finite Euler characteristic, zero H3 inverse transition,
fractional-coboundary isomorphism, H1(Zhat(4))=Z/240, exact CRT map and
finite candidate witnesses. Independently reran the certificate during
CP16 write freeze in /tmp/a205_birational_audit_jn8wqd14, with no work/
writes. Output PASS:14214 power-ideal unit cases,240 CRT classes,72
restriction-order checks and13824000 fourth-layer global classes.
Root and Legendre were notified.

## 2026-11-16 17:22 UTC — A207 independent full audit

Read the complete saved source
sections/point3_class_four_1129_obstruction.tex and independently reran
its exact certificate in /tmp/a207_birational_audit_mbr_0mpe. PASS: the
A62 initial homogeneous prescription, all 138 actual-exponent preimage
cases, the 1128 common-value ratio checks, the precise Hensel/CRT
transfer and its later preservation, the actual order128/class4
geometric quotient, the fixed-sheet proper Selmer comparison, and all
eight 1129-adic sheets. Their four quartic square vectors are
1010,0101,1100,0011, while the actual global Selmer image is contained
in {0000,1111}. Every denominator and root difference is a unit, so
the calculation applies to the whole prescribed residue disc. The
separate class-four global-lift statement retains its A61 map; no
locally matching class-three premise is asserted. The source and
certificate scope pass without correction. Parent and Legendre were
notified. The independent rerun output is retained in the work notes.

## 2026-11-16 17:35 UTC — A210 full audit and A211 completed maps

A210 full saved source and independent exact certificate rerun PASS.
I checked the literal A62 support exponents, the same tangential Ihara
gauge throughout the tame relation, integral central coordinate and
dihedral inertia parity, the actual geometric kernel and its arithmetic
stability, the supported quadratic difference, all local cover sheets,
and the full two-adic abelian alignment. The actual local C16 correction
is odd and all global C24 corrections give the even image6k. No
mathematical correction was needed. The five literal quad/qquad TeX
slips were sent to Legendre for repair. Independent output is retained
in point3_dihedral_1129_birational_audit_output.txt.

A211 source is saved as sections/two_inert_secondary_capitulation_coordinates.tex.
Its integral group-ring identity proves Norm_h(r0)=1; actual Hilbert90
normalizes f into F while preserving b,u,c exactly. The divisor descends
as J=j_hD, with full ordinary class [D] killed3 and tau-minus. The exact
class is k11 Delta11+k59 Delta59 and psi2=2(k11,k59). The complete
necessary unit cube-class space is the literal restriction span
<epsilon,u11,u59>, certified through all actual automorphism matrices
and minors -38080,246784,8. Local peer's complete source audit passes,
and I independently reran the entire certificate successfully. The
actual Omega-unit norm equation selecting these coordinates is retained;
the three psi2 values and their comparison with Theta_h eta remain open.


## A212 full independent source audit — 2026-11-16 17:48 UTC

PASS. I read the full saved temporary A.D8 proof and its exact certificate, then reread A40.4–5 and the actual punctured-disc/cusp isomorphism A49.6. The ordinary-contact formulas retain the chosen tangential cocycle: principal units supply the integral coboundaries for positive contact, and the negative-contact ratio gives the literal cyclotomic half-cocycle of -1. Divisibility of every nonzero ordinary valuation by24 forces trivial D8 inertia outside2,3. After abelian alignment, all supported central quadratic twists are classified by the actual arithmetic/geometric conjugation map, whose image is the subgroup generated by -2,-3. The global generator reduces to kappa_2(2), so the24 integral lift classes give exactly the two geometric images with multiplicity12 each. At3, the ordinary point lies in the zero cusp disc and its tangent mod2 agrees with3; A49 gives its actual D8 section image. The twist by2 remains distinct under the exact local conjugation map, so A40's distinguished lift has the stated global finite image. No existence of an all-place matching lift is inferred.

Independent isolated certificate rerun at `/tmp/a212_birational_audit_umr3_3zj` passed all3 symbolic Hall substitutions,12,480 contact-parity cases,1,024 literal conjugation checks, supported/local character quotients, and the12/12 correction multiplicities. Retained output: `notes/point3_dihedral_frame_birational_audit_output.txt`. No mathematical correction found.

Audited hashes:
- `sections/point3_dihedral_frame_classification.tex`: `06837c2040018223bafb20944547f84967cda66c735281d99a5317595fd979e1`
- `code/point3_dihedral_frame_certificate.py`: `aaff0f44216d46ce7cb1b20e6e9db5e0e77cdba43a8a8c16875bf60944cdde7a`
