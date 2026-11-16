# F, G, H research and verification log

Status: working research return, 15 November 2026. The numbered task rows remain Open wherever the requested general theorem or arithmetic measurement has not been obtained. The additional proved statements are not substitutes for those missing conclusions.

Register correction after checkpoint 01: the current F/G/H JSON has exactly 37 rows, one for each actual numbered statement F.1–F.19, G.1–G.8, H.1–H.10. The 13 earlier duplicate rows labelled only by a lead have been merged into the answers and notes of their numbered statements. The current generator checks exact equality with the statement IDs in the TeX. Earlier checkpoint metadata is superseded by this corrected register.

## Main mathematical progress

**F.** The localic inverse limit is the intersection sublocale. For closed subsets of regular Hausdorff spaces the ordinary limit is the closed subset and the residual limit is empty. For a Hausdorff point germ, arbitrary covering descent has an exact criterion: in every neighbourhood U, the intersection of all clopen neighbourhoods of the point in U must itself be a neighbourhood. This also characterizes whether that point-germ covering category can be the locally constant objects of any Grothendieck topos. For residual germs of closed subsets of regular Hausdorff spaces, comparison with the literal limit holds exactly when the subset is open.

Lead 14 is false in its assertion that locally connected, semilocally simply connected stages always have a replacement topos realizing all covering germs. Discrete tails of the natural numbers give a category with no countable coproduct of its terminal object. Every locally constant category of a Grothendieck topos contains that coproduct, namely the constant countable object. The proof explicitly chooses simultaneous representatives on tails and diagonalizes against the countably many injections. The weaker obstruction that P(N)/Fin is not a complete Boolean algebra is also proved, but is not used to make the stronger conclusion.

A countable surjective tower of discrete groups is a positive case: its prodiscrete limit G has classifying topos BG, and its locally constant objects are exactly the actions with one common open kernel, hence the filtered colimit of the stage action categories. All continuous G-sets are generally a larger category. A compact Cantor subset of the line gives a separate failure of full faithfulness for arbitrary covering descent, despite finite covering descent.

F.19 proves the complementary finite statement without local connectedness: every compact subset of a locally compact Hausdorff space has finite-cover continuity over its neighbourhood germ. The proof extends a finite principal permutation bundle through a finite join model, using an explicit neighbourhood retraction of a finite polyhedron; properness of finite coverings supplies full faithfulness.

Countable intersections of open subspaces of a locally compact Hausdorff space are spatial as localic intersections; F.15 gives a direct compact nested-neighbourhood proof. This proves Lead 21(A) for manifolds. The intrinsic stack formulation is obtained by atlas descent, but the unrestricted torus formula is false: the stack BC2 times a disk retains BC2 in its punctured germ. A geometric point fibre of a representable blow-up and the fibre over a residual gerbe must be distinguished. Closed nested blow-up stages have the stated closed intersection limit. The derived singular-chain calculation is proved with its degree shift and the zero strict limit.

Finite locally constant descent is derived from SGA 4 VI with coherent topoi and coherent transition morphisms. The strict henselian normal-crossings étale limit is identified, its finite fundamental group is the product of r copies of the cyclotomic profinite integers, and it is a classifying topos in local dimension one. In higher dimension a proper nonempty open prevents it from being a classifying topos. Tangential comparison retains arbitrary Z^r-actions on the complex side and finite continuous profinite actions on the étale side.

Lead 17 is proved in the stated complex manifold and number field settings. The cuspidal homotopy fixed point set is a torsor for the completed Kummer group, not merely the rational tangent vectors. The latter embed densely and properly. The finite invariant systems are Mittag-Leffler, so the claimed H1 inverse limit has no lim1 correction. Stix's packet injection is checked with its proper-point injectivity hypothesis.

The literal condition in F.5 is tautological for a hyperbolic étale K(pi,1): every section already defines a homotopy fixed point of the curve. This does not logically refute an equivalence with the section conjecture, which might be true. The claimed identification of all homotopy fixed points with ordinary rational points is false when a rational cusp is present; its cuspidal packet is disjoint from rational-point sections. The actual cuspidal section conjecture is the missing surjectivity statement.

**G.** An independent exact tensor/Lyndon implementation verifies the ambient degree-eight plane. In the prompt's normalization, alpha(A8)=1, nu(A8)=-31/20, alpha(B8)=0, nu(B8)=1. With C8=A8+(31/20)B8, the saturated integral lattice is Z5 C8 plus Z5 B8. B8 vanishes in the free metabelian Lie algebra. Both directions belong to Enriquez's geometric Lie algebra, so every 5-adic scalar satisfies those universal constraints, including the irrational 5-adic square root of 6. This refutes deduction of rationality from those constraints alone, not rationality of the actual arithmetic scalar. The finite nonmetabelian Magnus measurement is specified. G.9 now proves the actual first-coordinate ideal is Z5 and that the actual arithmetic image is saturated in its one-dimensional rational span. Its second coordinate remains unknown.

The Malkin source for the proposed motivic route has now been checked directly. Theorems 11 and 16 concern the Hodge realization. The discussion preceding Lemma 3 explicitly makes the transfer depend on the motivic formalism and hypothetical regulator injectivity. G.8 records this exact source limitation, without concluding that rationality itself is false.

**H.** The attached q2 integral model has been rerun as a standalone program with isolated output filenames, checking 110592 cocycle identities and 2304 projection identities. Over F2 dual numbers, only four of the eight enumerated minimal automorphisms lift, and the dual-number parameter epsilon fails the idempotent condition. Every additive-polynomial automorphism f with f(1)=1 acts compatibly on all abelian Fermat stages, by the integral matrix/cocycle formulas. The example T+epsilon(T^2-T) is nontrivial as a polynomial group scheme automorphism although it is invisible on F2[epsilon]-points; F4[epsilon]-points detect it. A complete class-two Heisenberg calculation shows that the same coordinatewise action cannot extend across a quotient whose commutator pairing is ordinary multiplication. The missing comparison is an integral nonabelian Fermat-stage model at the prime 2. No rational BCH model is silently reduced modulo 2. Actual profinite signed actions are affine linear on all abelian stages, and their joint full-prime kernel is the kernel on the metabelian quotient of the full free subgroup. Individual retained-source images and kernels remain undetermined.

H.9 makes the integral-model obstruction concrete. The rank-five naive Hall class-two scheme cannot carry even the required modular rho action at 2: the verified matrix sends e2 to e1+e4, but the former has square zero and every lift of the latter has nonzero central square e1 wedge e4. All 1024 central lifts were tested. H.10 supplies two smooth integral Heisenberg models with the same rational fibre and designated abelian quotient, whose special fibres have opposite answers to the nonlinear-lift question. Thus the model cannot be recovered from the generic fibre and first stage alone.

## Executed computations

| Program | Scope and output |
|---|---|
| `code/fgh_degree8.py` | Independent rational tensor algebra, derivation brackets, Lyndon decomposition, metabelian evaluation, saturated lattice certificate. JSON and stdout saved. |
| `code/fgh_q2_recheck.py` | Standalone rerun of attached integral q2 implementation, with provenance header and renamed outputs. Cocycle, projection, finite-field and dual-number checks all passed. |
| `code/fgh_topology_checks.py` | Normalized C2 bar differential H1=Z/2 and finite Cantor-coordinate checks. These finite checks are not claimed to prove inverse-limit assertions. |
| `code/fgh_additive_lifts.py` | Exact arithmetic in F4[epsilon]/epsilon^2; additivity, inverse, 3840 matrix compatibilities, 2304 cocycle fixed values, and the class-two commutator obstruction. All passed. |
| `code/fgh_hall_models.py` | All 1024 central lifts in the rank-five Hall model, and 2304 generating-coordinate checks for the alternative integral model. The modular action obstruction and model dependence are certified. |

## Source access and exact locations

| Source | Access and exact use |
|---|---|
| SGA 4 VI | Primary French reedition by the Orgogozo project opened: Theorems 8.2.3 and 8.3.13, Proposition 8.3.6; the online English text was also read. Earlier Stein/Zenodo routes were blocked, but the Polytechnique primary French text succeeded. The extra finite locally constant descent argument is supplied explicitly. |
| SGA 1 XIII | Primary French retyped PDF downloaded and read, Corollary 5.3, retyped p.316/original p.430; tame Kummer description 5.3.0 and the preceding Abhyankar lemma. |
| Stacks Project | Tags 0EYL and 0GL2 opened directly; inverse-limit étale sites and finite locally constant descent. |
| Leroy 1979 | Original 37-page scan (two printed pages per scan page) downloaded from Carmona's repository; printed pp.15–16 and 26–29 visually checked. Provisional TeX transcription of chapters 2–4 read. Theorem 2.4; 3.3.2–3.3.4; Definition 3.4.1; 4.1.1; van Kampen theorem in section 4.5. The transcription's provisional status is retained. |
| Stix, arXiv:0809.0017 | Attached primary TeX read: Theorem 14 and appendix. This numbering belongs to the supplied version. |
| Schmidt–Stix 2016 | Author PDF opened, Lemma 2.7(a), the K(pi,1) assertion for affine or positive-genus smooth curves. |
| Enriquez, arXiv:1003.1012 | Primary PDF opened, Proposition 4.19, equation (48), subgroup inclusion immediately after (49), and Proposition 4.20. |
| Malkin, arXiv:2010.07238 | Primary PDF opened, Theorems 11 and 16 and the conditional realization discussion preceding Lemma 3, printed pp.12–13. |
| Mochizuki–Tsujimura 2024 | Primary PDF downloaded and opened for independent A.1 audit: Theorem A; Definition 2.2(i); Proposition 2.3(v),(ix); Proposition 2.4(vii). Uniqueness needs a Z_l quotient of the inertia intersection; the extra open cyclotomic hypothesis is only in the existence clause. |
| Hoshi–Mochizuki, Topics IV | Primary PDF opened, Corollary 1.15(iii),(iv), to distinguish existence from bounded-distance uniqueness. |
| Nakamura 1994 | Primary Tokyo journal PDF opened, Lemma 2.1.4, printed pp.96–97: the finite-cover proper-homology criterion for cuspidal elements, including pro-l groups. Used in the independent A.11 normalizer audit. |

Primary downloads are kept outside the deliverable in `fgh_sources/`; they should not be included as redistributed full papers in the final archive.

## Independent parent-section audits

The A.1 full profinite centralizer proof was checked against the exact local uniqueness theorem. The cusp composite valuation is primitive; its localization after inverting p recovers the horizontal valuation; local commutator tame image supplies the needed nonzero Z_l quotient. The global/local base change and the open-Delta transfer were checked. The attempted A.2 route does not force cuspidality: a primitive valuation produced by existence can be a Gauss/type-II valuation.

The A.3 proof was independently challenged at the Weil restriction, induced CM type, Kummer image, and splitting steps. No substantive gap was found under the hypotheses written there. In particular the F-action on Lie(A) is faithful in characteristic zero, the dimension count forces an induced Q(i)-type, and the unique rational splitting follows from weight separation. The A.4 explicit curve/isogeny/cusp-divisor arguments were also checked; the two genus-one intermediate covers with isomorphic source curves are distinguished by their dual isogeny kernels. The Fermat plane quartic admits no genus-two quotient, since such a quotient would be an unramified involution, whereas a plane involution necessarily has fixed points.

A.11, A.12, and A.14 were reviewed at the weighted first-degree detector, finite-cover topology, punctured map, and pushdown steps. The separate prime-three arithmetic input was delegated to the D/E agent and was not audited here. The weighted first-degree comparison is valid when the proper-homology detector is taken in a finite cover with induced pro-l topology; both arithmetic characters are compared at one good Frobenius after the same finite extension.

## Additional Part A contributions

**A.13**, in sections/A_cover_maps.tex, gives all three cusp-compatible elliptic maps from the Q8 quartic, the stable D4 degree-two map to the CM(-2) elliptic curve of j=8000, and the impossibility of a second independent cusp-compatible elliptic map for stable D3. Code a_cover_maps.py executed eleven exact map and j-invariant identities. The parent reviewed and incorporated the statement.

**A.22**, in sections/A_fixed_subcovers.tex, proves induced pro-l topology for covers with l-group Galois closure and transfers R1 to their exact fixed subgroups. In particular every D8/Q8 genus-three cover and every D8 genus-two reflection quotient has its pro-2 fixed subgroup equal to selected cusp inertia, for every packet and every open Delta0. The same-open-subgroup step is proved independently: an IA automorphism of a free pro-l group has no nontrivial finite orbit. The attached LM8 G.10 proof was read, including its separate nonzero degree-two and higher-metabelian cases. Code a_fixed_subcovers.py checked all 24 generating pairs in each order-eight group and all reflection cusp orbit lengths.

**A.24**, in sections/A_generic_packets.tex, is an unbounded generic-packet theorem for the stable S3 covers. For any original packet and any prime Kummer direction with nonzero restriction to Delta, at most three l-adic twists fail the exhibited first-Johnson test on the genus-three two-cusp cover. For every other twist the actual full pro-l fixed subgroup is exactly inertia. The stable genus-two quotient has the same result outside a countable exceptional set at every prime, and outside the same finite set at l=2. The proof distinguishes ordinary Johnson degree from natural geometric weight, proves tangential hyperelliptic equivariance even if the based involution squares to an inner cusp automorphism, and keeps the exact factor 1/3 integral at l=3. The other-cusp constraint makes the six-by-six Johnson matrix symplectically self-adjoint, so its determinant is the square of a cubic Pfaffian polynomial; this sharpens the original bound of six to three. The Lie kernels are proved in all degrees by maximum-jet elimination and a primitive leading-word centralizer argument. Code a_generic_packets.py checked C3 Lie ranks 6,21,112,588 in degrees 1–4 for a matrix with opposite eigenvalue pairs, and D3 centralizer ranks 4,5,20,60,204 in degrees 1–5. These finite checks do not compute an arithmetic Johnson matrix. Particular exceptional packets remain unresolved.

## Concrete remaining gaps

The subsequent parent-requested contribution **A.25**, in sections/A_D3_monodromy.tex, completes the odd-prime normalizer problem for the stable genus-two S3 quotient. Its degree-three map to E cannot have smooth reduction above 2, since that would give a tame cubic cover of a supersingular elliptic curve branched only once; the S3 Galois closure would have an impossible etale double quotient. Its compact-type stable fibre therefore has two elliptic components. The origin-fibre divisor excludes component degrees (3,0), leaving (1,2). Every remaining proper homology vector projects nontrivially to both. Betts–Dogra's primary non-abelian Picard–Lefschetz theorem (Definition 3.1.5 and Theorem 3.1.6, arXiv:1909.05734v2, pp.23–24) supplies the actual separating inertia derivation. An explicit rank-two free-Lie quotient proves that it violates the necessary normalizer equation. Code a_D3_monodromy.py executed the curve-map identities and the nonzero degree-three obstruction.

**A.26**, in sections/A_fixed_first_layer.tex, places the local monodromy inside every required open Delta0 by the actual local commutator [Frob,tame]. It proves zero proper homology for every fixed element on stable D3, and exactly the primitive boundary homology line for stable C3, including all exceptional packet parameters. The three reflection quotients jointly detect proper homology only; they are not claimed to be jointly injective on the full nonabelian groups.

**A.27**, in sections/A_D3_fixed_all.tex, settles the full stable D3 fixed subgroup for every original packet at every odd prime. The divisor f*O=3P forces the cusp to specialize to the stable node, so its pointed model has a rational bridge and two nonzero edge lengths. The actual based degree-two monodromy differs from the ordinary affine model only by lambda ad(Omega): both actions have zero first Johnson degree and kill the boundary, and the free-Lie centralizer forces that inner form. An all-degree tensor normal form gives ker(m1T1+m2T2+lambda adOmega)=Lie(omega1,omega2) for lambda=0 and Q_l Omega for every lambda nonzero. The proof uses the first nonboundary core and the injective prefix operator lambda L_Omega+m_i R_omega_i. One actual ordinary Frobenius conjugate reduces the lambda-zero kernel to Q_l Omega. Primitivity then permits subtraction of an actual integral cusp power, proving the full group statement. Code a_D3_fixed_all.py checked 511 triangular basis words, exact rational CM coordinate identities, the boundary-plane intersection, and 30 finite kernel ranks through degree six, including lambda=-m1 and -m2. These checks support the unbounded proof rather than replacing it.

The separate common-kernel problem for the two extreme derivations Dplus,Dminus is still unproved. Its finite tests through degree six, and the individual slope tests through degree eight, are retained as exploratory evidence; A.27 uses the full separating derivation instead. The all-packet full fixed subgroup on stable C3, and the stable D3 pro-2 exceptional packets, remain outside A.27 itself.

**A.28**, written by the parent in sections/A_C3_stable_graph.tex, was independently audited here. Tame cyclic cubic normalization at 2, together with good Jacobian reduction, forces three split elliptic tails and a rational center containing both cusps. The actual monodromy and one CM conjugate force the leading class of a fixed element into Lie(t,Omega), with no claim that the three reflection maps detect the whole nonabelian group.

**A.29**, in sections/A_C3_one_exception.tex, sharpens the remaining genus-three problem to at most one original odd-prime packet class. Any nonzero actual first-Johnson matrix suffices after A.28: D(Omega)=[t,Omega_A], and an exact tensor pairing projection reduces its kernel on Lie(t,Omega) to the centralizer of t. Actual integral cusp-power subtraction then proves the full fixed subgroup. Two zero-Johnson packets differ by kappa/3 times the identity, so the odd-prime cusp-cohomology calculation forces them to coincide. Vanishing is defined on an actual open subgroup of Delta, not only the smaller global commutator group. The parent independently audited and integrated this proof.

**A.30**, in sections/A_C3_collino_fixed.tex, has passed the parent's independent proof audit. It removes that last possible genus-three packet by an exact arithmetic unit. For q=q0+[i]q1 to Y^2=X^3+3X, degree(q)=4 and Norm_q(w)=zeta(2+sqrt(3))^-2. The Collino cycle pushes to zeta^2(2+sqrt(3))^-4; q_*-2(q0)_* kills the polarization line and retains the nonzero Kummer class -4 kappa_(2+sqrt(3)). A universal canonical negative hyperelliptic class-two extension is compared to the actual Collino regulator directly on symmetric separating twists. Luo–Watanabe Theorem8.7, Brendle–Margalit–Putman TheoremA, and relative-completion Torelli density give the geometric identity. Arithmetic Hochschild–Serre injectivity follows because the primitive exterior square has no geometric invariants. Ordinary-to-tangential comparison alters only scalar ad(t), and Sah's identity makes the unit Kummer class nonzero on every open Delta subgroup. The resulting actual nonzero Johnson map invokes A.29, including ell=3. This proof uses compatibility of cycle classes under Betti–etale comparison; it does not assume that equality of arbitrary Hodge extensions implies equality of their etale realizations. Code a_C3_collino_unit.py, .json, and .out retain all exact map, norm, degree, cusp-fibre and scalar-removal checks. The parent is integrating this statement after independently checking the universal bridge, scalar removal, and Kummer nonvanishing.

1. A full characterization for arbitrary space-filter germs and arbitrary closed subsets remains beyond the exact point-germ, residual, stability, and surjective-tower cases proved here.
2. The actual arithmetic degree-eight nonmetabelian coordinate and all repeated-character embeddings through degree fourteen remain unmeasured. G.9 now determines the first-coordinate ideal and the saturation index.
3. The integral nonabelian tower at 2 must be specified before the Heisenberg obstruction can settle H.3 for that tower.
4. Images and individual kernels of the five retained profinite normalizer/conjugator sources require their actual joint automorphism constraints, not just the ambient scheme automorphisms.

## 13:20 UTC — A.31 closes the stable symmetric covers at two

The independently audited section `sections/A_S3_twoadic_fixed.tex` proves the full pro-2 fixed subgroup equals selected cusp inertia on stable C3 and all stable D3 reflection quotients, for every original packet. The new input is the global orbit span of a fixed logarithm: it has abelian image, so its local semistable realization is crystalline. A literal logarithmic PD specialization of the AIK coefficient association gives tangential semistability over ramified local fields; arbitrary cusp packets are handled by a B_st Kummer gauge. Fontaine N is applied only inside D_st, and CM operators act on D_cris leading spans. The unbounded A.27/A.28 kernels then apply, and the rational A.30 regulator is nonzero also at two. Root independently checked and integrated A.31. The auxiliary Sylvester/gauge certificate executed successfully.

Next: actual G degree-eight secondary coordinate. The linear A.30 universal-H1 comparison does not immediately apply: the B8 coordinate has a nonzero universal Chevalley–Eilenberg differential dual to the bracket of the two extreme degree-four generators. Its CM specialization becomes additive after those extreme components vanish. This precise secondary-class obstruction is being checked before any further statement.

## 13:36 UTC — G.9 determines the actual first-coordinate ideal and index

The exact Ishii–Goto conductor-four normalization has a finite Kummer certificate at 101. With i=10 and zeta5=95, the element product_(a=1)^4 (1−i zeta5^(4a))^(a^3) is97 and its twentieth power is36, whereas zeta5 has twentieth power1. This excludes the unique cyclotomic degree-five Kummer line and proves the raw Soulé character primitive on G_{K(mu5∞)}. Mod5 the coefficient action is trivial, so its restriction to Delta is divisible by5; a commutator with cyclotomic value6 gives exact image5Z5.

An integral sequence of genuine Galois group operations preserves that entire ideal while killing Johnson degrees2,4,6. Pick k with cyclotomic value2 modulo5 and apply u↦kuk^-1 u^(-r), using a profinite exponent with prescribed5-component. The excluded lower weights have residual eigenvalues2,4,2,3,2; the target character has residue1. Every multiplier is a unit, and odd degrees vanish by the actual CM involution. Thus chi4(J8)=5Z5, with no logarithmic denominators or rational saturation inference.

The coefficient alpha=d^3 chi4/267840 was independently rederived from Nakamura1995 (4.8), TheoremA/Corollary4.12, the published factor12 erratum on Nakamura2013 p492, and Ishii–Goto Theorem1.7. The exact calculation is chi_ell44=(126/5)chi4, 12kappa33=d^3 chi_ell44, and h33=−kappa33/((1−5^6)(3!)^2). The sign follows from Nakamura's inverse boundary z and his T_i beta coordinate. G.4 independently identifies h33 with the specified Magnus alpha.

Therefore alpha(J8)=Z5, lambda−31/20 lies inZ5, v5(lambda)=−1, and5lambda=4 modulo5. The actual line image is Z5(C8+delta B8), saturated with index1. The value delta=nu on an actual alpha1 element remains unknown, so G.1 and the explicit-generator portion of G.2 remain Open. The index in the full rank-two ambient lattice is infinite.

The program code/fgh_primitive_degree8.py and its JSON and stdout were executed and retained; de_sections supplied the independent code/de_soule_conductor4.py residue certificate. Primary web references opened: Ishii–Goto arXiv2412.18846v2 Definition2.14, Remark2.15(2), Theorem1.7 (turn373view0–2); Nakamura1995 publisher PDF Sections4.3–4.9 and Corollary4.12 (turn376view0–2, turn378view0); Nakamura2013 published p492 (turn375view1, turn378view1). Ishii2026 Theorem1.2 and Lemma1.5 were also opened (turn374view0–2) to check the rational generation input behind R20; no unbounded freeness claim is used.

The parent's A.32 was independently audited: the extension of the stable-reduction argument to the nonstable genus-two covers uses only potentially good Jacobian, supersingular target, and f*O=3P. The abstract Sp(V_F) invariant kernel is a local equivariant crystalline construction, which avoids treating non-CM global operators as local morphisms. Its exact quadratic intersection and the faithful invariant quotient argument were checked; the parent received a full audit pass.

## 13:52 UTC — A.33 audit and the remaining nonstable regulator

A.33 passed the parent independent proof audit and was integrated before checkpoint04. It settles the full pro-2 fixed subgroup on both nonstable genus-three covers by the actual unramified degree-two embedding into A.32. For odd primes, the tame three-tail graph and the dense non-CM SL2 action reduce every possible leading fixed class to Lie(t,Omega). The exact symplectic matrix and all curve-map identities were executed in code/a_nonstable_C3_fixed.py.

For the remaining odd-prime problem, the primitive Collino class has S3-sign symmetry. Write the non-CM isotypic summand as V_F tensor M, where M is the two-dimensional standard representation of the deck S3. The sign piece in its exterior square is Sym^2(V_F) tensor exterior^2(M), whereas the algebraic divisor piece is exterior^2(V_F) tensor Sym^2(M) and has no sign constituent. Galois conjugation on the explicit reflection maps exchanges the two cubic-root labels, so exterior^2(M) descends as the odd quadratic character of Q(sqrt(-3)). Thus an even-adjoint Selmer vanishing cannot be substituted for this coefficient.

Primary source opened: Tilouine--Urban, arXiv:1811.11166v3, https://arxiv.org/pdf/1811.11166, section5.4 and Remark5.16, printed pages38--39 (web refs turn394view0--3). This source treats the odd quadratic adjoint twist separately: the rank-one Selmer assertion (Sel) and nonzero p-adic regulator assertion (Reg)_p are distinct, and Remark5.16(2) explicitly does not derive the latter from the former. No identification of this curve's Collino class with their Beilinson--Flach class is proved here. The source is being used to identify the exact limitation of that route, not to assert that every later result leaves it open.

A stronger elementary obstruction to repeating A.30 is being checked. The three elliptic maps q_i=(zeta^i w+zeta^(-i)/w, v/w^2) to F_a have both cusps over O and satisfy q_0+q_1+q_2=O. For every integer linear combination q, Norm_q(w) is constant over Q(zeta3), has norm1 under conjugation, and should be an S-unit only at2,3. Since2 is inert and3 ramified in Q(zeta3), norm1 would force this constant to be a root of unity. The good-reduction extension and specialization of q are the steps under review; this has not been promoted to a numbered theorem. Even if proved, it only rules out all elliptic pushforward Kummer detectors of the A.30 type; it does not prove that the actual primitive Collino or Johnson class vanishes.

### Completed norm obstruction for the nonstable elliptic projections

Here is the proof behind the preceding tentative norm argument. Put L=Q(zeta3), a=6 or -6, C: v^2=w^7+a w^4+w, F: Y^2=X^3-3X+a, and q_i=(zeta3^i w+zeta3^(-i)/w,v/w^2). The three points q_i(P) lie on one horizontal line, so q_0+q_1+q_2=O. Each q_i maps P_0 and P_infinity to O. Every nonzero integer linear combination q therefore has those same cusp images. The divisor formula for the norm gives div(Norm_q(w))=q_*(2P_0-2P_infinity)=0, so c_q=Norm_q(w) is a constant in L^times.

The reflection j(w,v)=(1/w,-v/w^4) satisfies q_i composed with j = -q_(-i). Hence q composed with j = -bar(q). Norms are unchanged by negating the target when the resulting function is constant, while j^*w=w^-1. It follows that bar(c_q)=c_q^-1.

The discriminants of the defining polynomials, computed exactly, are 3^6(a^2-4)^3 for C and -27(a^2-4) for F. Thus both curves have smooth proper models outside 2,3, with the two cusp sections disjoint there. On such a model div(w)=2P_0-2P_infinity has no vertical component. The map q extends through its homomorphism J_C to F and the Abel--Jacobi map based at P_infinity. The homomorphism remains nonzero on every good special fibre: choose an auxiliary prime different from the residue characteristic, use smooth proper specialization on Tate modules, and the faithfulness of the Tate-module representation of a nonzero abelian-variety homomorphism. Since the image of the Abel--Jacobi curve generates its Jacobian, the extended curve map remains nonconstant. It is consequently finite on each fibre. The relative norm has no vertical divisor, by the pushforward formula for divisors of a norm. Therefore c_q is a unit at every place outside 2,3.

Both primes 2 and 3 have a unique prime above them in L: 2 is inert and 3 ramified. These primes are fixed by conjugation. From c_q bar(c_q)=1 their valuations are zero too. Thus c_q is an algebraic integer unit in the imaginary quadratic field L, and hence a root of unity. In particular the Collino pushforward, whose two norm factors are c_q and c_q, is c_q^2 and has zero rational Kummer class.

This applies to all elliptic quotients in the F-isotypic factor. End(F_overlineQ)=Z by A.32, and the independent maps q_i span Hom(J_C,F) tensor Q, so an arbitrary such quotient becomes an integer combination after composing multiplication by some N. Pushforward through [N] raises a constant to its N^2 power. If that power is torsion, the original constant is torsion. Quotients to elliptic curves isogenous to F are handled by composing with an isogeny and the same degree argument. This proves failure of every elliptic pushforward Kummer detector on the non-CM isotypic factor. It makes no claim that the primitive higher regulator itself is zero.

The S3 representation explains the same limitation: the primitive cycle changes sign under the reflection (which exchanges the Weierstrass points and inverts w), and is invariant under the rotation modulo root-of-unity decomposable cycles. The divisor classes in the non-CM F^2 factor form Sym^2 of the standard two-dimensional multiplicity representation, which has no sign constituent. The missing component is therefore transcendental in this precise correspondence sense.

### Next concrete route: the quaternion cover at two

The primary article van Bommel--Docking--Dokchitser--Lercier--Lorenzo Garcia, Reduction of Plane Quartics and Cayley Octads, Table7.1, printed p50, explicitly records type (0eee) for the Fermat quartic at2 and refers to Liu's book Exercise10.4.39 for its stable model. This means a rational center and three elliptic tails. The main article's general conjectural reduction criteria are not being used as a theorem at2: it explicitly cites this separate known computation. Primary PDF opened at https://discovery.ucl.ac.uk/id/eprint/10205747/7/Dokchitser_Reduction%20of%20Plane%20Quartics%20and%20Cayley%20Octads_Pre-print.pdf (turn398view0, turn399view2). The required next input is the distribution of the four cusps Z=0 on that stable model, followed by its actual affine monodromy and CM torus action. No pointed-geometry or fixed-group claim has yet been inferred from the unpointed type alone.


## 2026-11-15 14:45–14:50: quaternion cover fixed group completed

A.35 (sections/A_Q8_proper_fixed.tex) proves the cyclic-eight tripod model U^8 = -64 B(B-1)^2, the common-node specialization of all four cusps at 2, and trivial proper pro-ell fixed group for every odd ell. Its surface-envelope kernel is proved directly in the quotient, using three nonoverlapping monic rewrite rules. The integral group step uses a separate compact (ell,variables)-adic topology and a separated degree filtration, not an unverified rational-to-integral lifting. Root independently audited the full proof and primary sources.

A.36 (sections/A_Q8_cusp_fixed.tex) completes the full punctured quaternion fixed subgroup for every prime and packet in Part A. The Q8 action forces a rooted rational four-mark tree at the common node. Transitivity and stability reduce its possibilities to a four-mark component or two two-mark leaves; the cyclic-eight automorphism excludes the former and identifies the pair lying over B=0,infinity. For odd ell, the first ordinary tame derivation has fixed two-cusp letters and conjugates every other generator by a nonzero multiple of their sum. Arbitrary tangent packets add lambda ad(p). The first-slot operator lambda L_p + c R_s is injective outside the two-letter algebra for every lambda, and the cyclic-eight target map is injective on that leading algebra. A.34 plus actual integral cusp subtraction finishes. Prime2 uses A.22. Root full independent audit passed.

Executed code/a_Q8_cusp_fixed.py: exact edge coefficients, inertia matrix determinant -64, and finite kernel checks through degree5 for lambda=0,1,-2 all PASS. The proof is unbounded; these checks are supporting certificates only. The earlier actual Ceresa-at5 route is no longer a dependency. Bloch1984 primary p104 verifies a nonzero rational extreme Ceresa class at5, but no all-prime assertion was inferred. Primary source copies are in research_sources/ outside the deliverable; bibliography URLs and theorem/page references are retained.

Remaining D8 avenue: the conic quotient has four harmonic branch values {a/(2s),infinity,1,-1}. A cyclic4 map to a harmonic four-punctured line is explicit for all three C4 cases. A source two-cusp rational leaf with no adjacent surviving genus would be treated by the same first-slot argument. It remains necessary to prove the pointed source geometry: potential genus tails attached at the marked leaves would leave extra first-degree proper directions. Do not infer complete fixed groups from the finite covering map alone.


## A.41 registered after checkpoint six

The general compact-type rational-path criterion is now Proved and integrated following full independent root audit. It combines the multicore all-weight monodromy kernel with an exact global tensor intersection and a connected diagonal-conjugacy lemma, avoiding a CM hypothesis. DE independently audited both global lemmas. The registered statement is for coefficient prime different from the selected residue characteristic. See sections/A_compact_type_fixed.tex, notes/fgh_A41_audit.md, and code/a_compact_type_fixed.py/.json/.out.


## A.42 registered: all coefficient primes in the compact-type criterion

Root and DE independently audited the full crystalline extension and passed it. The statement is integrated after A.41; its exact arithmetic group comparison uses a true tensor change of fibre, with leading monodromy and component blocks inside the same log-crystalline realization. A.17/A.23 metadata now cites the proved D.56 instead of a supplied local preprint, as requested by the parent. A.7 remains Open.


## A.43 registered: odd dihedral covers of unbounded genus

The actual two-branch Kummer model gives a rational marked centre with n elliptic tails for C_n:v^2=w^(2n+1)-w, every odd n. Full fixed inertia at all coefficient primes follows from A.42. Root independently audited the proof and reran the exact certificate. The statement includes the general tame two-branch Kummer construction over two colliding torsion cusps on a positive-genus good-reduction curve. It does not classify normalizers in the new higher-genus family.


## A.44 registered: the four-cusp two-power family

The curves v^2=w^(2m)-1, m=2^s, now have full fixed inertia at every coefficient prime by a CM/p-rank-zero/Abel-path proof. All four selected cusps are covered. Root independently audited the proof and primary Serre--Tate statements and reran the exact certificate. No normalizer conclusion beyond the stated fixed-group result is implicit.


## A.48 and A.49 registered after checkpoint seven

A.48 completes every normalizer in the two-power dihedral family at every prime, by the labelled CM-type stabilizer and wild component-genus bound. A.49 supplies complete fixed-group and normalizer examples in every proper genus: tame Kummer covers over two colliding p-torsion points on the supersingular original elliptic curve, with all extra origin-fibre cusps accounted for on the actual rational core. Both received full independent root proof/source audits and certificate reruns. The universal Task A.5 remains Open; the proved families are not asserted to be cofinal.


## A.50 registered: Heisenberg cover normalizers

The degree27 genus10 model y^2=x^3-x, z^3=psi3(x) now has all-prime procyclic normalizer recognition, after independent root and PBC proof/source/code audits. Actual punctured maps detect E_i and E_0^3; the residual surface has no CM factor, proved by exact genus-four quotient counts at61 and313 with persistent distinct ordinary Frobenius fields. Its full pro3 fixed subgroup is covered by A.22. The all-prime fixed-group argument through quaternion multiplication is being audited separately as A.51.


## A.51 registered: all-prime Heisenberg fixed groups

Root and DE independently audited the full exact cellular/Hodge/reduction proof and reran the certificate. The same residual surface B has F-Hermitian polarization diag(-1/6,1/3) and an explicit rational antilinear Hodge endomorphism giving quaternion(-3,2). Its division algebra at3 excludes both toric rank and special etale3-Tate rank. Every individual cusp difference is killed by9; A.42 then supplies full fixed inertia at every prime and packet. Together A.50/A.51 complete this genus10 Heisenberg cover. The universal Task A.5 remains Open and no cofinality claim is made. Included sources and registers are now frozen for checkpoint08.


## A.54 registered: the higher Heisenberg cover and a precise split-prime frontier

The actual degree125 genus51 cover z^5=psi5(x) has J isogenous to E times A2^5 times B8^5. The genus-eleven quotient is an explicit CM-isogeny pullback, with constant −35−120i; its primitive cyclic20 factor is exactly the same B8. Two exact quadratic Frobenius fields over Q(zeta20), at41 and61, are nonsplit, unequal, and unchanged under every positive Frobenius power. The global specialization-centralizer argument proves B8 has no geometric CM factor. Labelled quartic CM types then give all normalizers for ell not congruent1 modulo5; A22 gives the full pro5 fixed group. Root, DE and PBC independently audited the proof and reran the exact certificate; all PASS. The split-prime normalizers reduce through actual punctured maps to the genus2 three-cusp curve w5=t(t−1), and remain open. Other full fixed subgroups also remain open. This does not solve universal TaskA5 or give cofinality.


## A.55 registered: the split-prime Heisenberg frontier is closed

A.55 supersedes the split-prime normalizer gap recorded under A.54. Every prime is now settled for the actual genus51 Heisenberg cover. The genus2 target admits actual cyclic p^n auxiliary covers from étale Picard torsion with exact special order. Their normal Kummer models have one radicial main component. Raynaud Theorem1 makes every exceptional Jacobian have strictly interior Newton slopes; removing the main norm factor gives a p-rank-zero Prym. The exact integral invariant-transfer lattice forces a nonzero Prym image once n exceeds the divisibility of the proposed normalized generator. Root and DE independently read the complete proof, opened the original theorem and reran the exact certificate; all PASS. The result is a normalizer theorem. Full fixed subgroups of the Heisenberg-five cover away from coefficient5 remain open, and universal TaskA5 remains Open.

## A.56 registered after root and DE audits

The potentially-good-curve normalizer criterion for special p-rank at least two is now canonical in `sections/A_good_reduction_normalizers.tex`. For actual degree-d covers of the punctured Gaussian elliptic curve it settles every coefficient prime p>d with p=1 mod4. The connected--étale specialization is used as a saturated quotient, with no arithmetic splitting assumption. Exact finite certificates and both independent audit records are retained. A separate rank-one strengthening is being written as A.57 and is not incorporated into this statement.

## A.57: potential good curve reduction and all sufficiently large coefficient primes

Registered after independent full root and DE audits. Every affine hyperbolic curve of proper genus at least two has cuspidal pro-p normalizers if its proper curve has potential good reduction at a place above p, with no special-rank condition. The new rank-one case uses Raynaud Proposition1 to obtain a globally etale quotient of the normalization, Crew's unramified p-rank formula, and Raynaud's zero-rank exceptional components. Every cyclic p-power cover then has a p-rank-zero Prym, so an actual integral transfer detector excludes all proposed proper homology lines, including divisible ones. For arbitrary degree-d covers of the original punctured elliptic curve this settles EVERY p>d. The universal fixed-subgroup problem and the residual bad-reduction primes p<=d remain separate.

## A.58: the remaining Heisenberg5 fixed groups are complete

Registered after independent full root and DE proof/certificate audits. Exact residue-five charts on the actual genus51 curve produce one ordinary elliptic main component, five genus6 and ten genus2 Artin--Schreier tails. Their genera exhaust51, proving compact type. The25cusps form five rational clusters of five, away from all positive-genus tails. A42 therefore proves the selected full pro-prime fixed subgroup equals its cusp inertia at every coefficient prime and for every permitted packet/open derived subgroup. Together with A54--55 this completes both requested assertions for this degree125 cover. Earlier notes leaving its other fixed groups open are superseded by this exact calculation.


## A.59: every nilpotent geometric Galois closure

Registered after root and DE full proof/source/certificate audits PASS. Every finite cover with nilpotent geometric Galois closure has cuspidal arithmetically normalized procyclic subgroups at every coefficient prime. Arbitrary covering subgroups split across coprime direct factors; the exact normal cores provide the two required actual cover maps. Good reduction and the induced pro-prime topology then give the assertion. No universal fixed-group or cofinality conclusion is asserted.


## A.60: complete genus148 Heisenberg-seven cover

Registered after root and DE full proof/source/certificate audits PASS. The actual degree343 cover has an explicit seven-adic compact-type model with one supersingular elliptic main component and seven genus21 Artin--Schreier tails. The genera exhaust148. All49cusps lie on a rational marked tree overO, away from every positive-genus tail. A42 supplies all-prime full fixed inertia, while A59 supplies all-prime normalizer recognition. The missing degree-seven Taylor coefficient was explicitly verified, and no general inert-prime statement is inferred from numerical pattern.


## A.61: uniform inert-prime Heisenberg family

Registered after complete independent root, DE and PBC audits and exact reruns PASS. For every prime p congruent to3 modulo4, the actual degreep^3 exponent-p Heisenberg cover has genus1+p^2(p−1)/2 and p^2 cusps. The uniform divided-operator argument identifies the actual critical function and kills the invisible degree-p Taylor coefficient. Explicit charts give one supersingular elliptic main component and p Artin--Schreier tails of genus p(p−1)/2; their genera exhaust the whole genus. Every cusp lies on the rational marked tree overO. A42 gives full fixed inertia at every coefficient prime and packet, and A59 gives all normalizers. This supersedes the earlier restriction of the exact wild model to p=3 and7; it does not assert cofinality or solve universal TaskA5.


## A.62: the full odd-prime Heisenberg family

Registered after full independent root and PBC audits and exact reruns PASS. The ordinary-prime case uses an actual unramified translation comparison modulo p², proving that the divided differential descends through the separable degree-p CM isogeny. Its descended odd function has one pole of orderp and derivative mu*x, hence one triple and p−3 simple zeros. Actual charts give p quartic and p(p−3) quadratic Artin--Schreier tails and one ordinary elliptic main component; genus exhaustion proves compact type. All p² cusps form p rational clusters ofp marks. A42 andA59 supply both all-prime assertions. Together A61/A62 now settle the exponent-p Heisenberg family for EVERY odd primep. Universal TaskA5 remains Open and no cofinality is asserted.


## A.63: all ordinary Heisenberg isogeny enlargements

Registered after root and DE full audits and exact reruns PASS. Every p=1 mod4 and every m≥1 has both all-prime assertions for the actual degree p³m² enlargement. Connected torsion translates fix reduced tail U; the noncentral kernel of the residual AS action supplies a free cusp orbit with identical specialization on each tail. Main/rational components and node fibres are handled explicitly. A42 gives fixed inertia; A11 transfers normalizers through the actual open immersion. Odd critical torsion is allowed and an exact order13 example at residue41 is retained. Universal TaskA5 remains Open.


## A.64: prime-outside-closure and all odd Heisenberg enlargements

Registered after root and PBC full audits and exact reruns PASS. An enlargement integer with a prime outside the actual closure order gives all-prime fixed inertia; the tame model includes residue2, and source cluster sizes are c or1+e(c−1). Combined with A63 and the separate inert pure-p-power O-fibre argument, every odd Heisenberg cover has both assertions for every isogeny enlargement. Universal TaskA5 remains Open; no finite-refinement, fixed-lift or cofinality claim is made.


## A.65: every intermediate odd Heisenberg cover

Registered after root and DE full proof/source/certificate audits PASS. All intermediate covers of H_p, for every odd p, have both all-prime cusp assertions. The new noncentral quotient has degree p², genus1+p(p−1)/2 and p cusps. The ordinary proof chooses a Gaussian place with nonzero reduced translation; the inert proof resolves the actual morphism and dominates every positive target component, forcing rational cusp paths over the unique main O-point. This covers all geometric closures of exponent p and class at most two. Universal TaskA5 remains Open.


## A.66: one Heisenberg factor and a coprime abelian factor

Registered after root and DE full proof/source/certificate PASS. Every closure quotient of H_p×B, p odd and B abelian of order prime to p, has both all-prime cusp assertions, including all intermediate subgroups. The actual proper elliptic-isogeny base change preserves the unique connected radicial main, the compact-type tree and every rational cusp joining path. Two nonabelian Sylow products and the universal TaskA5 remain outside the theorem.


## A.67: every tetrahedral closure and intermediate

Registered after full root and DE proof/source/certificate PASS. Actual degree3 isogeny coordinates and a V4 Kummer extension identify every A4 closure via the unique standard F2[C3] cohomology summand. Residue3 gives a rational marked centre with four supersingular elliptic tails; the wild C3 quotient is treated through exact residue fields and genus exhaustion. The complementary elliptic factor has j=4608±2688sqrt3 and supplies the coefficient2 normalizer input. Both assertions hold at all primes. The separate K_{4,h} isogeny-pullback barrier and the universal TaskA5 remain explicit.


## A68: nonstable genus-seven dihedral covers and intermediates

Integrated after full root and DE proof/source/certificate PASS. The actual genus-two quotient B:W²=(T+2)(T⁴−4T²−4), T=w²+w^-2, gives J_C~J_C4×J_B². Exact Igusa J=(24,−24,1248,7344,−256) and original Liu Thm1 show two supersingular elliptic components at2. Four explicit principal divisors kill all cusp differences by8. Norm and I=Phi(D16) prove every proper intermediate has the same rational-companion-path hypothesis. Both cusp assertions hold at every prime; universal A45 remains Open. Original candidates, source verification, exact finite certificates and all independent audit outputs remain retained.


## A69: uniform nonstable two-power dihedral family

Integrated after full root, DE and PBC proof/source/exact-code audits PASS. The actual C_m cover has D_(2m) closure, four cusps of indexm/2 and m-primary cusp differences. Potential good Jacobian comes from the precise ramified nilpotent-cover theorem. The primitive cyclotomic anti-Prym has special rank0 or is ordinary; the latter forces a full orbit of ordinary elliptic components, whose smooth fixed points cannot lift to the individually fixed generic cusps, and whose remaining branches force genus at leastm rather thanm−1. Actual norm maps and Frattini inertia give all intermediates. A41/A42 prove all-prime full fixed groups, A59 all normalizers. Universal A45 remains Open. No pattern extrapolation, marked-fibre slope extrapolation or arbitrary dihedral classification is used.


## A70–A74 and the next modular candidates

A70–A74 are registered after full independent audits: all actual two-power dihedral closures; their odd abelian extensions; all generalized-quaternion closures; all semidihedral closures; and one preservation statement for the latter three families with odd abelian factors. Exact candidates, canonical certificates, independent reruns and integration ledgers are retained. All statements preserve the universal A45 Open scope.

A75 is a complete notes-only candidate for every modular two-group closure and intermediate. Its new step is the unmarked proper-model fixed-point contradiction, not an extrapolation of the earlier marked-tree argument. A76 classifies the entire cyclic-index-at-most-two class, including small orders, and repeats the actual odd-abelian preservation. Both exact certificates have executed PASS; A75 has DE full independent PASS, and root review is pending. Neither is in checkpoint15 canonical sources.

Checkpoint15 assigned15 pages were actually viewed with at most two image outputs per call; all passed. Independent C44, C45 and D90 ledgers are complete; C44 is integrated by its owner/root, while C45/D90 remain notes-only under the current freeze.


## A75–A77 registered after checkpoint15 release

All three complete proofs passed root and DE independent proof/source/code audits. Canonical certificates were rerun and agree in every mathematical JSON field. A75 settles modular closures; A76 gives the complete cyclic-index-at-most-two class with odd abelian factors; A77 extends to actual closures with commutator order at most two. Drafts, original outputs and exact editorial diffs are retained. Universal A45 remains Open; no general two-group special-rank theorem is inferred.


## A.78–A.79 registration, 2026-11-16 01:34 UTC

Registered after full root, DE and PBC proof/source audits. A.78 proves the actual mixed-characteristic single-section Kummer comparison and global rank-zero consequence. A.79 proves the cyclic-derived arithmetic family and full actual coprime abelian preservation. All candidate sources, exact editorial diffs and source ledgers are preserved. No numerical premise is used. Universal A.45 remains Open. See notes/fgh_A78_A79_integration.json and the root/DE/PBC audit ledgers.


## A.80 registered, 2026-11-16 02 UTC

Full root and DE proof/source/code audits passed; PBC independently checked the complete partial-distance and Tate arguments. The actual natural genus-two wreath intermediate now has both required all-prime assertions. Its new kernel proof permits a positive-genus cusp path with a non-CM Prym block. Exact candidates, source ledgers, independent audits and every original certificate are preserved. Canonical copies were reexecuted with whole-result equality. Scope remains this actual intermediate; universal A.45 is Open. See notes/fgh_A80_integration.json.


## A.81 registered, 2026-11-16 02 UTC

Full root and DE audits passed for the actual genus-two double-cover/non-CM Prym family. The statement includes the explicit fixed-group equality and exact open-normalizer containment condition. The wild 2-power enlargements of A80 form an unbounded degree family on the same proper genus-two curve. All changed actual-closure, model, path and prime/packet gates are proved; no new numerical premise was introduced. Universal A45 remains Open. See notes/fgh_A81_integration.json and the preserved statement/registration diffs.
