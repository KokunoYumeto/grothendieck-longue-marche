INCOMPLETE

# Part D working report

| Task | Statements | State reached |
|---|---|---|
| Item 3 | D.1–D.4 | Exact affine homomorphism, exact joint rational-prime images, independence, general openness, and exact local inertia indices proved. |
| Lead 1 | D.1, D.5, D.8, D.18, D.20, D.23 | Core comparison proved by an exact coefficient formula recovering every rational Kummer character from the full profinite universal measure, for every Galois element. Rational-prime image is exactly 2 Zhat^r; an actual tame-inertia witness proves the loss under pure pro-ℓ specialization. |
| D(a) | D.1, D.5, D.6, D.8, D.20, D.23 | **INCOMPLETE source verification:** the mathematical comparisons are proved from opened Otsubo/IKY/IharaII primary proofs; Anderson1989 original has now been verified; the expressly requested original Ihara1986 and Coleman derivations remain unverified. |
| D(b) | D.6–D.7 | Every good pair p≤50,n≤12 computed over the correct residue field, all nondegenerate character values retained; bad pairs and genus-zero levels explicitly handled. |
| D(c) | D.2–D.4, D.8–D.10 | Rational-prime and local Kummer questions settled, general openness proved, all requested Soulé characters certified; Vandiver37 proved by the explicit nonzero residues, not inferred from regularity. |
| D(d) | D.14,D.17,D.18 | Mod4/mod3 signs are functions of χ; exact local norm indices computed; full normalized congruence Kummer coordinate identified. |
| D(e) | D.11–D.13,D.19–D.22,D.24–D.33 | Actual Galois and full-GT rational metabelian images through10 are equal for everyℓ. Exact Lie images and genuine pro-ℓ realization proved. The general lifting theorem's peripheral gap is explicit. All23 selected nonidentity CM actions are proved nongenuine despite their complete abelian-kernel lifts. D.30 also rejects the two later selected central representatives. D.31 constructs a further explicitly compared replacement on a class3 pro2 kernel with third subgroup C2^1860, every odd relative pro-p kernel, and the compatible mixed quotient. D.32 proves that D.31's recorded degree-seven action has no full relative pro2 peripheral lift. D.33 supplies an explicit new degree8 replacement on a class4 pro2 quotient with third subgroup C2^9105 and fourth subgroup C2^1620, compatible with the whole class2 tower and mixed quotient. Actual full profinite GT0/all-special images and the whole CM pair remain unresolved. |
| D after LM2(1) | D.15–D.17,D.19,D.25–D.33 | Galois CM lead proved: exact projective coordinates and joint image index2; local norm indices2,3 computed. The common level12 field and twelve nonarithmetical finiteGT0 shadows are explicit. The12 selected extra shadows survive every abelian-kernel refinement but are proved nongenuine by the two-prime class-two test. The D.31 central replacement for the same homology and CM data extends over a class3 pro2 kernel with third subgroup C2^1860, every odd kernel and the compatible mixed quotient. D.32 proves that this recorded action has no genuine full lift, and D.33 constructs another action through degree8, the full class2 tower and the mixed quotient. Its canonical projection changes the D31 action first in degree5. Realization of the CM pair by a full profinite action remains unresolved. |
| D after LM2(2) | D.18,D.23 | Genuine normalized congruence action retains all rank-one Kummer data by t=−8κ2; the full profinite universal measure recovers it by exact coefficients; outer congruence action retains only χ modulo squares. |

## Main corrections and proofs

1. The affine rank-one map is the Kummer action on compatible roots of −1/2. Its image is the parity graph of the quadratic character χ−8, of index two. On the cyclotomic kernel the rational-prime tuple has image exactly 2 Zhat^r, not all Zhat^r. A short real-conjugate argument computes every radical relation and a perfect finite Kummer pairing gives the exact image.
2. The general openness question of scan166 is proved directly. A uniform Sah cocycle argument forces a bounded power of every cyclotomically divisible element to be divisible already in the ground field. Finitely generated units in a normal arithmetic model then bound all Kummer indices uniformly. The full-unit-group and saturated surjectivity suggestions fail for Spec Z[1/2][t].
3. The local inertia image is also exact, not only open. Odd-ℓ indices are ℓ^(vℓ(p^(ℓ−1)−1)−1) for p≠ℓ and one for p=ℓ. At two they are two for p=2 and 2^(v2(p²−1)−2) for odd p.
4. The Fermat Jacobi computation keeps the manuscript's plus model. The twist factor is θ(−1)^(a+b). At p43,n6 the two traces are32 and−64, so ignoring the arithmetic descent would give a wrong result.
5. Soulé certificates at q≡1 modℓ² give nonzero modℓ values for every requested character. Their distinct cyclotomic eigenspaces ensure that the classes do not disappear in the infinite ℓ-cyclotomic extension. At37 every weight3,5,…,35 is witnessed at5477. The separate Bernoulli calculation finds(37,32), which concerns the minus class group and does not imply a Vandiver gap.
6. The exact metabelian image ranks of all special derivations in weights1…10 are0,0,1,0,3,0,5,0,7,0; invariant ranks are0,0,1,0,1,0,1,0,2,0. The extra invariant weight7 direction dies. The pro-ℓ successive-approximation claim from LM3 was independently proved, including the convergence and automorphism steps. Coprime fixed-point lifting handles S3 forℓ≥5.
7. The two normalizer coordinates have a direct modular-stack interpretation. The quotient [M0,4/S3] is the rigidification of M1,1 by±1; the cocycle/path comparison gives the projective Tate representations of x³+1 and x³−x. The projective torsion fields are K3^ab and K4^ab. Their intersection is exactly Q^ab Q(i,3^(1/4)): two abelian index2 subgroups force a commutator group of order at most2, and the explicit D4 extension realizes it. Thus the joint image has index2 in equal norms.
8. The local paired norms have one quadratic obstruction at each of2 and3. Finite enumeration verifies index2 from mod4 at2 and mod3 at3. Global roots identify their diagonal, leaving the single global relation above.
9. The cusp Tate parameter is q=λ²/256 times a rational power-series unit of constant1. The positive tangential section fixes λ roots and those unit roots, hence the genuine normalized matrix is [[χ,−8κ2],[0,1]]. Positive real q roots and the branch-cut period ratio fix the otherwise possible shear. This agrees with agent A's independent division-polynomial computation of the mod12 image of order12.
10. The original Ihara sequel gives phi_n(f_g)=y^(−kappa_n(g))f_g, with phi_n induced by the n-th power cover followed by filling all root-of-unity punctures except1. Its Introduction explicitly attaches the beta/gamma factorization to the pentagon equation. Its Supplement corrects the Jacobi indices in Ihara1986 Theorem7, exponent signs in Theorem10, and an inversion in Anderson1989 p125.
11. For a leading special term f=p(X,Y)[x,y], the exact Fox map is M(f)=XYp and the derived-module action is −XYp. Gamma factorization restricts this to a scalar times X^n+Y^n−(X+Y)^n. The special condition eliminates even n. E.3 provides actual Galois nonzero classes for everyℓ, so actual Galois and full GT both have ranks0,0,1,0,1,0,1,0,1,0 through10. The weight9 extra S3 vector fails this gamma condition.
12. Dolgushev–Guynee2024 Theorem5.2/Corollary5.4/Proposition5.5 gives the exact remaining profinite test: a finite GT0 shadow comes from a genuine element exactly when it lifts through every finer finite B3 quotient. This is stronger than lifting through pro-ℓ nilpotent quotients. The criterion is recorded as D.22 with its compactness proof.
13. Write the Ihara conjugator in the derived module as u_g[x,y]. Exact commutator calculus gives B_g=1+(s−1)(t−1)u_g and F_g=A_χ(s)A_χ(t)B_g. Reducing u_g at t=1,s^n=1, the Kummer character κ_n is coefficient0 minus coefficient(n−1). This proves the proposed full profinite comparison positively. For oddℓ, pro-ℓ tame inertia at2 fixes every root of unity and acts trivially on the normalized pro-ℓ fundamental group, but κ2,ℓ is onto. Hence retaining full χ still does not recover this Kummer datum from the pure pro-ℓ series.
14. The common nonabelian finite CM field is Q(i,(3/4)^(1/4)): full E3[4] and projective E4[3] are equal to it. Projective E3[12] recovers full4 by the rational three-torsion point's sign. A finite refinement with quotient of order576·6^97 realizes twelve extra-CM-coset automorphisms, with full-rank97 checks at both2 and3. A precise cusp gauge makes these actual finiteGT0 shadows; their incompatible restrictions to the common field prove nonarithmeticality. No full profinite lift is inferred.

## Files and actual execution

- `code/d_jacobi.py`, `d_jacobi_field.cpp`, `.out`, `.json`: compiled C++ field enumeration plus exact cyclotomic-ring arithmetic. Largest directly enumerated field was F_(47^5). Large semiprimitive fields use a proved quadratic Gauss-sum identity; the smaller such fields were independently enumerated.
- `code/d_kummer_soule.py`, `.out`, `.json`: all rational Kummer annihilators at n≤24 and all specified circular Kummer values moduloℓ≤50, with exact residues and primitive-root choices.
- `code/d_metabelian.py`, `.out`, `.json`: exact QQ matrices and nullspaces, with Lyndon-coordinate preimages for every displayed image basis.
- `code/d_local_cm.py`, `.out`, `.json`: all p,ℓ≤50 local Kummer indices; paired CM norm images mod2,4,8,16,32,3,9,27; exact D4 group and index certificate.
- `code/d_gamma.py`, `.out`, `.json`: Fox/metabelian identity verified on224 Lyndon words; actual full-GT gamma lines located in every invariant image basis through10; exact independence of the extra weight9 vector checked.
- `code/d_kummer_measure.py`, `.out`, `.json`: 3840 Fox/Schreier coefficient checks from160 explicit free words and24 levels;210 commutator-action identities for positive and negative exponents. These verify the algebraic identities used in D.23 independently of its arithmetic source theorem.
- `code/d_cm_shadow.py`, `.out`, `.json`: exact CM division-coordinate identities; Bass–Serre graph with480 vertices and576 edges;97-dimensional integral cycle model;48 candidate conjugator pairs; exact cusp, hexagon, centralizer and generation checks at2 and3; CRT certificates for24 finite automorphisms,12 in the extra CM coset.
- `code/d_ledger.py`: generates statement, reading and coverage JSON ledgers from the manuscript. This is packaging code, not a mathematical check.

## Reading audit

Actual manuscript images inspected:157,166,167,168,169,170,171,172,173,174. Scan159 is absent from the supplied image set; its transcription was read with the displayed root equations; the mathematical sign reading is separately justified by the homogeneous point and plus model. Full D instructions and both LM2 followups were read. LM2 C.d1–C.d5 were independently analyzed. LM3 special-lifting and dimension claims were independently recomputed/proved rather than treated as authority.

Opened primary papers: Otsubo2016, IKY1987, Ichimura–Kaneko1989, Lozano-Robledo2022 author preprint, Milne2007, and the indicated Tate lecture statement. Original IKY pages5–6 and Ichimura–Kaneko pages313–315 were inspected as rendered images. Otsubo Theorem8.1 supplies the full residue-degree Frobenius product. IKY A2/B supplies the exact Soulé coefficient normalization. Ichimura–Kaneko Theorems1–2 supply the functional-equation image and exact plus-Iwasawa characteristic-series obstruction. Lozano Corollaries3.4/3.7 supply the CM ray-class comparison.

Original Ihara1986, Anderson1989 and Coleman1989 records were resolved by exact title. Anderson1989 was subsequently obtained in full from the official GDZ archive: its Proposition5.5.1, Corollary8.6.3, Theorems5–6, Proposition11.6.1 and Proposition13.3.2/§§13.4–13.7 are verified, retaining the basis coboundary, even-level twist, precise tensor flip in gamma multiplication, and the exact Soulé coefficient normalization. The Ihara1986 and Coleman1989 original full texts have not yet been obtained. This leaves the expressly requested original-source verification **incomplete**, even though opened substitute primary proofs establish the mathematical comparisons. Parent additionally followed the official Coleman DOI10.2969/aspm/01710055 and the Mathematical Society of Japan volume17 contents page: both lead to the same ProjectEuclid access barrier. Official Annals Ihara metadata does not provide an accessible original PDF in the tested routes; Anderson's publisher PDF route returns an access page. No claim is marked proved solely from their metadata. The original IharaII RIMS1224 PostScript file was retrieved from the author's university, decompressed, rendered and read in full. Its Theorem1 and Propositions1–3 were checked, including the distinction between gamma multiplication and its logarithmic derivative; its Supplement's sign corrections were read. The Part I RIMS1177 catalogue entry supplies no link; direct PDF/PostScript/DVI locations all returned404. Furusho2011 Theorem0.5, Corollary0.3, Proposition5.1 and Lemma5.2 were read in the full Annals original. Dolgushev–Guynee2024 was read in full at the relevant exact theorem numbers. The additional primary Lochak–Schneps1994 braid-tower article, Schneps full-tower paper, and Nakamura RIMS1691 elliptic-monodromy preprint were opened to pursue possible profinite lift and CM constraints. None of their checked statements supplies the missing lift.

## Exact residual work and approaches tried

The actual Galois/full-GT rational comparison is now proved in D.21. The full profinite GT0/all-special images are not determined by the Lie calculation. Successive approximation proves the pro-ℓ lift because the lower-central series tends to one there; a nonnilpotent finite quotient prevents that argument in the full profinite group. Replacing the free Lie algebra by its metabelian quotient loses conditions even in weight4, so that weaker route also fails. The smallest remaining extra all-special image is weight5, and the smallest extra invariant metabelian image is weight9. The modern finite-shadow criterion makes the missing step exact: establish nonempty lifts through every finer finite quotient, or produce a finer quotient obstructing the proposed vector. The source does not prove automatic genuineness of finite shadows, and its2024 footnote2 says no fake example was known to its authors. No inference from that absence is made.

For the two CM factors the Galois answer is exact. The remaining GT0 question is the missing C2 coset, now represented by twelve nonarithmetical finite shadows in D.25. The projective E3[4] field alone is Q(ζ12), but retaining the global sign across E3[12] recovers its full four-torsion field via the rational point of order3. That field is exactly the projective E4[3] field. The finite Bass–Serre refinement of order576·6^97 tests the cusp relation, both hexagons, generation, and the reductions of both torsion centralizers. Twelve extra-coset candidates survive as actual finite shadows. D.27 proves these selected candidates nongenuine, while a different homology correction in the same CM pair survives both characteristic class-two tests; its all-finer-quotient lift remains the next step. The retrieved IharaII relations constrain cyclic covers and gamma multiplication, but its proof uses the pentagon for factorization and does not assert the same condition for GT0. Later harmonic/equianharmonicIII was resolved at the publisher by title/DOI; the attempted full-PDF route returned an access page and both current author-server routes returned503. The earlier author text in RIMS Kokyuroku1267(2002), Theorem1, and Lochak–Nakamura–Schneps2004, Theorems2–3, were opened: their additional harmonic/equianharmonic formulas are asserted for Galois and explicitly not established for the whole GT group. The 2026 Goto–Ishii Coleman–Ihara elliptic analogue and the2025 factorization paper give actual elliptic/cyclotomic Soulé comparisons, but do not supply a missing profinite lift. The new dihedral GT0-shadow paper of Bortnovskyi–Dolgushev–Holikov–Pashkovskyi2026 was opened at Definitions2.1/2.3, Proposition2.2 and Theorems5.2/5.3/5.7; its finite-shadow definitions are used in the exact D.25 conversion. No automatic genuineness is inferred from its dihedral-family results.

The general automorphism-lifting route of Bleher–Chinburg–Lubotzky, Lemma2.3/Corollary2.4, was also checked. Parent section D.24 gives a genuine lift acting trivially metabelianly but violating the peripheral condition in an A5 quotient. Thus the theorem alone does not furnish a peripheral lift; it also does not prove that a different peripheral lift is impossible.

## Additional contribution to Part E

`sections/E_proconstant.tex` proves E.30. For both abstract rational completion and continuous Q_l completion, the relative completion of the arithmetic orbifold group over B_m=S3×Gal(Q(μ_m)/Q) is S3 times the relative completion of G_Q. Its exact inverse system over m gives the completion over proconstant S3×Zhat*, and kills the entire geometric free group. The abstract rational proof uses the opened Nikolov–Segal2007 Theorem1.4 to identify the abstract abelianization of the finitely generated profinite free group. The continuous proof uses the conflict between scalar χ_l≠1 and conjugation by a unipotent element. An explicit weighted completion over algebraic G_m retains the geometric free prounipotent group; its semidirect-product universal property is proved. The arithmetic unipotent kernels are specified as completed inverse systems, not asserted to be fully computed Galois cohomology groups.

D.26 proves that every exact finite quotient G_j=B/[N,N]N^j is isolated in the gentle shadow groupoid. Its integral cusp map has Smith cokernel C2; adding multiplier variation gives a surjective integer map. All24 certified G6 automorphisms, including12 extra CM pairs, lift compatibly to lim_j G_j, with lambda=1 modulo72 retained. A single profinite cusp gauge supplies the compatible shadows. All384 generic-m hexagon checks through exponents2,4,8,16 and3,9,27,81 pass. A normal-core quotient built from an explicit N→S3 surjection does not factor through any G_j, identifying a concrete remaining nonabelian test. The report d_cm_refine_report.md records the original lifting-source search and why the abelian/dihedral sufficient families cannot supply these witnesses via quotient maps.

## D.27 nonabelian refinements and an alternate witness

The exact class-two quotient orders are576*3^4753 and576*2^4850. Complete lower-conjugator correction ranks are130 in the135-dimensional three-primary Reynolds component, and4748 in the4753-dimensional two-primary central layer. Their survivor sets among the24 original selected actions intersect only in the identity. The original Herfort–Ribes torsion theorem makes these tests necessary for genuine completed-braid actions; D.25 fixes the conjugators' Q images and the explicit lower-centralizer matrices exhaust their remaining freedom. Thus all23 selected nonidentity actions, including all12 selected extra-CM shadows, are proved nongenuine. This is compatible with their actual infinite homology-tower lifts.

A separate98-dimensional affine homology search yields an alternate action for A=I,beta=(9,8;4,9). Five exact quadratic obstructions vanish at trial48, kernel rank97 is checked, and the corrected470844-letter cusp word evaluates directly to the identity in all4753 central coordinates. It has multiplier1 and extends to H2 times_Q P3, with full relative free pro3 kernel. The witness and its exact central corrections are retained in a separate JSON file. Higher two-primary and mixed-prime refinements, and the genuine missing CM coset, remain unresolved. Agent A independently audited and freshly reran all three programs; its official Herfort–Ribes original-source ledger supplies the exact theorem anchors.

## D.28–D.29: mixed-prime and stabilized infinite extensions

D.28 constructs an actual mixed-prime quotient with rank385 elementary3 kernel over an order2304 base, and checks its action with the same two-primary homology parities and original G3 conjugators as the alternate CM witness. Its exact common quotient with the primewise system is specified, so the actions can be combined.

D.29 extends the two-primary side through the whole class-two exponent tower. Exact Z/4 and Z/8 cusp words of1,816,936 and4,448,112 letters are verified. The two-level G2-module (Z/4)^4753 has constant correction matrices from the second stage onward; the4769-dimensional relation space maps onto all15 obstructions. Corrections fix the preceding level, and every finite action stabilizes after the next step, proving an actual compatible infinite automorphism. The retained H2 action is explicitly the reduction of the new Z4 certificate; the earlier central representative is not silently identified with it. Coprime order2 centralizer lifting adds the full kernel at every odd prime. D.28 compatibility then adds its mixed quotient through the exact common fibre product. The remaining problem includes class-three-and-higher two-primary refinements and further mixed finite quotients; full genuine GT0 realization is still unproved.

## D.30: first new rank-four layer and a further compatible replacement

The exact relative-pro2 reduction has free rank4 kernel K over Q/O2(Q), of order18; N has index32. The degree6 Zassenhaus layer has dimension690, and the gamma3N subspace has dimension240. The complete lower N-centralizer calculation has Frattini dimensions225 and78, fixed dimensions117 and42, connecting rank7, and152 explicit fixed-group generators. After all their defects are added, the correction rank is654 and both earlier selected H2 central representatives are still obstructed. The retained G6 data force the Q-conjugator coordinates; the smaller K/D6 quotient is not silently substituted for that data. The cusp has order48 on both sides, excluding multiplier freedom. Thus these specific representatives are nongenuine despite their proved infinite class-two quotient actions.

A new simultaneous central correction has full rank28 (fifteen Z4 conditions and thirteen degree6 gamma3N conditions). It retains the same homology/right-centralizer/G3 data, but replaces central coordinates explicitly. A2,944,468-letter cusp word is checked in both complete Magnus models. The exact combined finite quotient has order576*2^9843, and its common quotient order576*2^753. Later stable corrections start in D8(K), so the degree6 action and conjugators remain fixed throughout the entire infinite tower. The resulting two-primary kernel has class3, third subgroup C2^240 and trivial fourth subgroup, and combines with every odd kernel and the already compatible mixed quotient. The latest replacement, further third-layer and higher two-primary information, additional mixed quotients, and the genuine missing CM coset remain unresolved. The obsolete central representatives and their rejection certificates remain separately available.

## D.31: the complete degree-seven refinement

D.31 proves an actual quotient automorphism for the fixed extra CM pair and its retained homology data. The full profinite realization of this pair remains unresolved.

## Exact quotient and computation

Let T2=B/D8(K), with the free rank-four relative kernel K of D.30. The image U of gamma3N is elementary abelian of dimension 1860. Its degree-six quotient has dimension 240 and its degree-seven subgroup dimension 1620. It is an actual Q-module: the inhomogeneous degree-six to degree-seven extension is retained, and conjugation by N is trivial. The calculation uses the actual elliptic conjugate paths when computing the separate central C1 corrections.

The cusp correction map on U has rank 1810 and cokernel dimension 50. The simultaneous 50 conditions and 15 class-two Z/4 conditions have rank 65 on the 4769-dimensional relation space. A solved seed has multiplier 1 and retains the rank-97 homology action. Its complete 4,903,248-letter cusp word evaluates to the identity in both the rank-97 class-two Z/4 Magnus model and the rank-four mod-two Magnus model through degree seven.

The exact orders are:

- T2: 576 times 2^3333.
- Common quotient C**=B/(gamma3N D8(K)): 576 times 2^1473.
- H^(2) times_C** T2: 576 times 2^11463.

The common quotient is proved by the product of the two actual normal kernels. The exponent relations [N,N]^4 and N^8 lie in D16(K), so their images in T2 vanish.

## Infinite extension and precise comparison

The seed extends to P2/(closure(gamma3N) intersect D8(K)), identified with the fibre product of the class-two pro2 completion and T2 over C**. The later stable corrections of D.29 start in D8(K). The cusp has order 48 in T2, and later multiplier increments are divisible by 144. Thus the finite action and conjugators remain fixed throughout the iteration. The resulting kernel over Q has class exactly three, third lower-central subgroup C2^1860, and trivial fourth subgroup.

The canonical map to D.30's target has kernel C2^1620. The new action descends through this map, but the descended action replaces D.30's recorded central representative. The second program proves that the symmetric matrix Z+Ms Z Ms^T is nonzero; it is the exact difference on the image of s in H^(1). The original and replacement certificates remain separate. The fixed G6 homology and CM data agree.

Every odd relative pro-prime completion and D.28's mixed quotient can be included through the previously proved exact common quotient H times_Q G3. Odd-primary conjugators are separately selected components; no statement identifies their abelianizations with that of the displayed discrete two-primary word. The compatible finite shadows are nonarithmetical on characteristic refinements retaining the G6 and CM data.

## Files and independent verification

- Section: sections/D_degree7.tex.
- Main certificate: code/d_cm_rank4_degree7.py, .out, .json.
- Explicit reduction comparison: code/d_cm_degree7_reduction.py, .out, .json.
- Statement ledger: ledger/d_degree7_results.json.

Root independently reran both complete programs with successful output. Agent A independently audited the entire theorem and programs, including generation of U, its inhomogeneous Q action, the joint correction equations, exact common quotient, stability of the inverse limit, and the explicit difference from D.30's recorded action. No genuine full profinite lift is inferred from these quotient automorphisms.



## D.32: exhaustive degree-eight obstruction for the recorded D.31 action

D.32 proves that the specific T2 action recorded in D.31 has no torsion-conjugate peripheral lift to T3 and no cusp-power-preserving automorphism lift to the full relative pro2 group. This result concerns the recorded action. It does not exclude the entire CM pair or D.30's explicitly different earlier central representative.

## Exact computation

The direct reconstruction retains all 4,903,248 letters of the recorded cusp word. Its Magnus coefficients vanish through degree seven; its degree-eight error has 32,296 monomials. The restricted Hall layer D8(K)/D9(K) has dimension 8230. The group T3 has order 576 times 2^11563 and maps to T2 with kernel C2^8230.

The fixed-conjugator correction map has rank 7753. The cusp order changes from 48 to 96. The t48 column has 6561 monomials; the compatible multiplier change by144 gives the same column and raises the rank to7754.

The full lower centralizer is constructed through successive central extensions, using complete polycyclic sequences. The counts for N/D3 through N/D8 are 6,16,50,152,494,1666 in logarithmic base-two order. The connecting ranks are 1,6,3,13,7. At the final stage all generators have degree at least four, so the centralizer is elementary abelian; its degree-four through degree-seven dimensions are 37,102,348,1179. Including every generator's defect raises the rank to7777. The saved functional annihilates this entire image and pairs to1 with the target.

The exact G2 homology calculation has ordinary lower-central ranks 87,67,43,19,4,0 in degrees three through eight. The other restricted-power terms vanish as well, proving D8(K) is contained in Phi(N). Thus T2 retains G2. Normalizing a possible s-conjugator into F and projecting its lower centralizing difference to G2 puts that difference in the computed N-centralizer by D.25. The r-centralizer contributes no additional obstruction classes because order-three complements lift and are conjugate across a two-kernel. All multiplier changes retaining the lower action are included.

## Structural promotion to the full relative source

The preimage of the order-two subgroup of Q0 has index nine. Its Bass-Serre graph has nine edges, three order-two vertex stabilizers, and one free loop. The full induced pro2 topology gives the exact free pro2 product C2 coproduct C2 coproduct C2 coproduct Z2. Herfort-Ribes1985 section2 explicitly allows the class of finite two-groups; Theorems A-prime and B-prime apply. Every involution of the full relative group is conjugate to s. The graph normalizer quotient C3 permutes the three Sylow involution classes cyclically and yields C_P2(s)=<s>.

An r-image agreeing with the recorded lower action is conjugate with its prescribed lower conjugator by the coprime complement theorem. Hence every full relative automorphism lifting the recorded action and mapping the cusp to a power would supply one of the finite conjugator solutions already excluded. This proves the actual relative-source obstruction. It leaves all previously proved quotient automorphisms intact.

## Runnable certificate

Run code/d_cm_degree8_seed.py, then code/d_cm_degree8_centralizer.py; the latter invokes the complete central-layer calculation. The shared exact polynomial arithmetic is code/d_cm_degree8_magnus.py. The independent graph check is code/d_cm_degree8_sylow.py. All mathematical outputs and saved exact vectors are JSON/stdout files beside the programs. The seed and linear programs consume only those saved JSON certificates, not binary caches.

The first functional-extraction assertion caught a free-coordinate selection error in a partially reduced remainder. The corrected routine selects the highest unreduced pivot, and the complete rerun verifies annihilation and target pairing. All rank and centralizer counts were reproduced. Root independently reran the exact seed, full centralizer, and Sylow programs and audited the complete proof. All JSON fields agree apart from timing; the functional, full rank7777, and1666 lower generators pass.

## D.33: the compatible degree-eight replacement

The weighted free pro-2 basis of N has counts 9,20,25,24,15,4 in K-degrees 2 through7. Its actual words and Frattini matrix are retained. Weighted class-four collection, matched by independent tensor ranks, gives gamma3(N) modulo D9(K) of dimension9105=240+1620+7245 and gamma4 dimension1620. The common quotient B/(gamma3N D9K) has order576*2^2458. Its exact kernel from H^(2) is (Z/4)^2437 times (Z/2)^2271. The finite fiber product has order576*2^18708.

The infinite quotient is P2/(gamma3(N^(2)) intersect D9(K^(2))). Its kernel overQ has class4, gamma3=C2^9105, gamma4=C2^1620, and gamma5=1. Its canonical map to D31 has kernelC2^7245. The recorded new action changes the D31 image of s first in degree5; no lift of the old obstructed representative is claimed.

## Exact correction and verification

The correcting group is the full image of D5(K) intersect Frattini(N), namely (Z/4)^4708 times (Z/2)^9150. It is abelian in both finite targets. Its gamma3 correction rank is8981, leaving124 functionals. The joint upper map has rank4738 in4753+124 coordinates; the lower system has rank4826=4687+139. Thus every coupled obstruction is removed by actual order-four corrections, with multiplier144 retained.

The complete12921196-letter B cusp word collapses to2128528 K letters and836592 N letters. Every K Magnus coefficient through degree8 and every N class-two coefficient modulo4 vanishes. Multiplier1 and Frattini generation are retained.

The restricted stable Bockstein has rank15/15 when lower changes use only the4708 high words. These start in D10(K); upper changes and multiplier288 start in D16(K). The actual18077708-letter continuation passes the full Z8 model and retains T3 exactly. One-level-lookahead therefore gives the compatible infinite class-two continuation without changing the degree-eight action. The limiting two-adic multiplier lies in1+32Z2, with all odd components1. The unchanged homology and separately retained G3 data give the common-quotient comparison with D28's mixed J action.

## Remaining exact source kernel

The exact retained source kernel is gamma3(N^(2)) intersect D9(K^(2)). D45 proves that the recorded action cannot lift across the full kernel. A basic triple commutator in three distinct weight-three free generators is a nonzero element of it. The proof therefore records a concrete further relative-pro-2 kernel; the compatible family is not claimed to lift to the full source.

## Reproduction and audit status

All new programs use textual certificates. The reconstruction helper writes no binary word cache. Every included program has its own actual stdout. All eight integrated programs passed clean reruns. Root mathematical audit passed. Agent A completed its independent mathematical audit and all copied-input reruns; every JSON certificate agrees after removing elapsed_seconds, and both full-word checks passed. The T3 action is fixed by continuation; the initial H^(2) central coordinates may change at the first lookahead.


# D.34–D.35: the actual elliptic cover and its automorphism source

These two results give exact structural maps for the remaining relative pro-two lifting problem. D.34 identifies the retained rank-four group with the three-punctured genus-one curve w³=z(z−1), including its positive Γ(2) monodromy, all eighteen deck transformations, all three cusp words, and all 54 cusp conjugacy maps. D.35 proves actual odd-deck equivariant boundary lifts and then proves that the whole compact CM torus is already realized by genuine Galois action centralizing every deck transformation. D45 proves the recorded finite-action fibre empty. The prescribed CM pair remains open for a replacement action.

## Exact geometric and group maps

The regular Q0 dessin has cycles 2^9, 3^6, and 6^3. It has genus one and three punctures. The explicit deck maps are δ(z,w)=(z,ζw), s(z,w)=(1−z,w), and r=δr0 with r0(z,w)=(1/(1−z),−w/(1−z)). The standard positive generators x=(sr)^−2 and y=sxs both act by δ, so the cyclic-three cover is identified by its actual monodromy character. The normalized invariant map is 4(z²−z+1)³/(27z²(z−1)²).

The fixed K basis gives cusp words a1 a4^−1 a2, a1^−1 a3 a2^−1, and a3^−1 a4. The certificate stores every deck-cusp conjugator and all 324 section cocycles, with 1296 exact conjugation checks on the four generators. The Q0 action is faithful already on H1(K,F2). Conjugation therefore embeds the relative group P2 as the full inverse image of Q0 in Aut(K2). Restriction and conjugation give explicit inverse maps between automorphisms of P2 over Q0 and automorphisms of K2 whose outer classes centralize Q0.

The cusp centralizer is exactly the procyclic group generated by t, isomorphic to Z2×C3. This proves that a(c0)=c0^λ2 corresponds exactly to t↦t^(λ2,1), retaining both exponent components. Filling the cusps gives the actual map onto T2E0 and an integral exact sequence. The central order-three idempotent canonically splits cusp homology from the compact Tate lattice. The compact centralizer is O=Z2[ζ3], and its norm equals the common cusp multiplier.

D33's retained degree-eight action has compact Tate matrix (3,8;8,11) modulo16, equal to 11I+8Z for Z=(-1,1;−1,0). All D33 stable corrections retain it. The isomorphism E0→E3 is translation by (0,1) after (z,w)↦(4^(1/3)w,2z−1). Its exact arithmetic comparison includes the cubic Kummer factor ζ^(−κ4,3), with κ4,3=2κ2,3. This comparison is stated with the actual field of definition and is not silently applied to an unmarked congruence coordinate.

## Actual full free-pro-two boundary lifts

D35 gives both directions of the change to a marked surface basis, with c0 conjugate to [a,b]cd and the other cusp loops inverse-conjugate to c and d. Four explicit free-group automorphisms, their inverses, and four independent cusp shears prove the full peripheral homology image. The handle matrices generate SL2(Z2); a mod16 enumeration gives its expected order3072. Actual Galois automorphisms provide every common cyclotomic multiplier, so all allowable integral homology blocks occur.

The homology kernel is pro-two. The order-nine odd deck subgroup has an actual complement in P2. Coprime complement conjugacy inside the peripheral automorphism group corrects any prescribed commuting homology map to a genuine boundary automorphism centralizing that complement pointwise. Thus every O-unit has an actual odd-deck lift with multiplier its norm. This argument is an existence proof for the complete free pro-two group, with finite checks used only for the displayed generators and lattice maps.

## Genuine full-deck realization of the compact torus

The exact point counts on E3:y²=x³+1 are 12 at both7 and13. Their arithmetic Frobenius polynomials have CM root pairs {−1+2ζ,−3−2ζ} and {3+4ζ,−1−4ζ}. Both roots occur because complex conjugation interchanges the primes over each rational prime. Their reductions generate all16 elements of (1+2O)/(1+8O). The subgroup 1+8O consists of squares from1+4O, so the actual closed Galois image is all1+2O. The cubic Kummer extension of4 is independent of the pro-two division field, proving that the E0 image over Q(ζ3) is allO×.

Every deck map is defined over Q(ζ3), so this actual Galois action centralizes the full outer Q0 action and supplies every compact torus unit in the fixed subgroup C_o^iota. In particular η=(−3−8ζ²)/7 has norm1 and gives the exact D33 Tate16 reduction. This realizes that component; it does not identify the full D33 finite action or prescribe its second CM factor.

The residual involution s has an explicit quotient: the w-line, with z²−z−w³=0. Its three interior branch points satisfy1+4w³=0; infinity is the fourth fixed point and is removed. The quotient has punctures0,∞ and three order-two cone points. Its orbifold group and covering character give exactly the free pro-two product C2 coproduct C2 coproduct C2 coproduct Z2 used in D32.

## Exact remaining fibre

Let C_o be the pure peripheral outer centralizer of the odd deck subgroup. The full deck centralizer is exactly C_o^iota. Normalized relative automorphisms fit into an exact sequence with this group and kernel generated by Int(c0), isomorphic toZ2. Reduction to R=P2/D9(K2) therefore gives a map from C_o^iota to Aut_{Q0,t}(R) modulo that inner cyclic subgroup. The fibre over D33's recorded action is exactly the set of outer classes of its actual normalized relative lifts. D45 and its transport supplement prove this particular fibre empty, retaining the full torsion, sphere-projection and source cusp-inner maps. The single compact torus remains genuinely realized with other finite coordinates.

## Sources and actual verification

The opened Wilkes2020 original gives the PD2-pair orientation and standard-form classification, with exact Theorem3.3 and section1.3 anchors. No equivariant lifting theorem is inferred from that classification. The author-hosted Milne2021 text supplies the exact Frobenius/Tate comparison; the point counts and unit generation are computed here. The original Herfort–Ribes1985 pro-C free-product centralizer theorem remains the verified input for cusp centralizers.

Run d_cm_rank4_structure.py and then d_cm_rank4_odd_lift.py. Both integrated programs have passed and have actual nonempty stdout and text JSON certificates. The first reuses the exact D33 reconstructed words and takes about15 seconds. The second verifies both marked basis changes, all displayed automorphisms, the four cusp shear directions, SL2 mod16, the norm-one unit, all affine points at7 and13, and the complete principal-unit group modulo8. Independent root and agent A mathematical audits passed, including the arithmetic strengthening and exact fixed-action fibre. Agent A reran both current copied sources; their JSON certificates agree after removing elapsed_seconds only. The audit is recorded in a_independent_audits.md.


# D.36: the second cover and an exact joint comparison

D36 gives an explicit second marked elliptic cover and computes the actual joint arithmetic image of its projective three-torsion with the first cover's four-torsion. It also identifies the precise discrepancy retained by D33 and gives the gauge map showing that this discrepancy persists under the specified Ihara normalization. The full GT0 transfer remains unresolved.

## The quartic cover and its source map

The curve v⁴=z(z−1) is rationally isomorphic to E4:Y²=X³−X through X=z/v²,Y=v/(z−1), with inverse z=X²/(X²−1),v=Y/(X²−1). Its four omitted points map to E4[2]. Translation by the rational point(0,0) gives the pointed isomorphism with the point above z=0 as origin. The deck v↦iv gives multiplication by i, while z↦1−z gives T_(0,0)[−1]. Both directions and both deck maps are verified algebraically.

The actual fundamental-group source is K4=ker(F2→C4), with both standard loops mapping to1. Restriction and filling all peripheral subgroups give the compact Tate module. The proof records the tangent comparison: with the positive z tangent, the quartic lift has leading coefficient ζ8, so restriction of the base Galois action differs from the actual E4 action by [i]^((χ8−1)/2). Over L=Q(ζ12) this factor is a global sign and disappears on projective three-torsion. The cubic leading coefficient−1 is rational; its earlier cubic Kummer twist is retained separately.

## A shared marked cover

The actual common cyclic cover is v¹²=z(z−1). Its maps to the cubic and quartic covers use v⁴ and v³. It has genus5, four punctures and free fundamental rank13. The program supplies every Schreier basis word, peripheral vector and integral filling matrix. Its compact rank10 lattice maps onto the two elliptic rank2 lattices with all four Smith invariants equal to1 and kernelZ⁶. The two deck-equivariant matrices are written explicitly in D36.10.

The S3 normal core of the cyclic12 character has deck C4²×C3, order48. It is a quotient of the full Fermat12 deck C12², order144, by the subgroup generated by(4,8). These covers are kept separate. The common cyclic cover's compatible cubic tangent differs from D34's chosen tangent by the explicit δ deck map; over L this does not affect the normalized scalar sign.

## Exact arithmetic graph

Over L, every E0 four-torsion unit of norm1 is uniquely τ ε, where τ is its order-three lift of the mod2 unit and ε=±I. The cubic Kummer formula identifies ε with the actual full E3[4] action. The nontrivial automorphism of L(r0)/L, r0=(3/4)^(1/4), is -I on E3[4] and multiplication by i on projective E4[3]. This is checked directly using the quartic division roots a=(w+2/w)/2,b=(w−2/w)/(2i), w=1/r0.

The joint image is therefore a graph of order6. Its joint fixed field is L(cuberoot4,r0); the intersection of the two torsion fields is the quadratic subfield L(r0). The program enumerates all six units and verifies every order-three gauge transformation of the sign.

## The recorded finite discrepancy

D33's cover-Tate16 matrix reduces to -I modulo4. Its normalized cover sign is therefore−1. Its retained LM2 coordinates give T4=I and W3=[i]. The program reads the checked Tate matrix and computes the fixed-fibre matrices; the concrete representative W3 is -D4, giving exactly the same projective class as multiplication by i. No equality of these two matrix representatives is asserted.

The gauge Int(x^k) multiplies the cubic-cover Tate action by ζ3^k. It also multiplies A,beta,V on the left, leaving T=A^−1V and W=beta^−1V unchanged. Dividing by the unique order-three factor cancels that same ζ3^k, so the normalized cover sign remains−1. D35's norm-one actual Galois element realizes the full retained Tate16 matrix and W3=[i], while its actual normalized E3[4] matrix is−I. This specifies exactly which coordinates have been realized and which finite action remains to be lifted.

## Primary-source routes checked

NTY2010 Proposition4.4 gives a full-GT cover-Tate formula. Its Proposition4.13 and Theorem4.16 make the relevant power-conjugacy and fixed-fibre comparison for Galois elements, and the introduction explicitly leaves broader power-conjugacy unresolved. LNS2026 Theorem1.1 supplies full-GT mapping-class-group automorphisms while retaining an additional gluing-compatibility issue. Neither checked theorem supplies the required GT0 naturality map.

The program d_cm_elliptic_pair.py has passed a complete integrated run, with nonempty stdout and a text JSON certificate. It uses exact rational identities, integral Schreier homology, Smith normal form, and finite ring enumeration. Independent root and agent A mathematical audits passed. Agent A reran a fresh copied source; every JSON field agrees except elapsed_seconds. The arithmetic-section sign and exact source scopes were independently checked. The next concrete finite route is the full Fermat12 cover joined with the congruence quotient, with its exact quotient order and mixed homology equations to be verified before any further conclusion.


# D.37: an actual mixed Fermat12 shadow and its two compact cover actions

The new result is a fully generating finite GT0 shadow on a quotient that contains the congruence data and the common Fermat12 homology. Its actual normalized cubic-cover Tate4 matrix is -I, and its actual quartic-cover Tate3 matrix is I. Both are obtained from the same cyclic12 compact action through the exact maps of D36. The resulting pair violates D36's arithmetic degree-six graph. The retained LM2 fixed-fibre coordinates are T4=I and W3=[i], with the exact conjugator and gauge maps kept throughout.

## Exact quotient and source maps

Let B=C2*C3, F=ker(B→S3), Q=SL2(Z/12)/{±I}, N=ker(B→Q), and F12=ker(F→(Z/12)^2), with the positive loops x,y mapping to the ordered basis. Set L=N∩F12. The explicit affine representation sends s to the swap matrix with zero translation and r to the order-three matrix (0,-1;1,-1) with translation e1. Direct multiplication gives x=t^-2 the translation e1 and y=sxs the translation e2, so its kernel is exactly F'. Joining its mod12 reduction with Q gives H=B/L of order6912.

The kernel of H→Q is the twelve-element subgroup {(a,b):a,b even,a+b=0 mod3}, isomorphic to C2²×C3. The corresponding graph has6912 edges,5760 vertices and1153 fundamental cycles. Thus L is free of rank1153. Its affine mod4 and mod3 reductions have orders2304 and1728, and H is their full fibre product overQ. The subgroup F12 has rank145 and L has index8 in it.

There is an actual comparison chain J12→G6→H→Q, where Jm=B/[L,L]L^m and G6=B/[N,N]N^6. The first inclusion of kernels uses L⊂N and12 divisible by6; the second uses the exponent-six abelian kernel of H→Q. The geometric plus Fermat12 model maps to v^12=z(z−1) over Q(ζ24) by z=−x0^12/x∞^12 and v=ζ24 x0x1/x∞². The specified positive-interval roots reproduce the exact tangent of D36; the twist is not suppressed.

## Complete finite equations and actual generation

All48 matrix conjugator pairs have been tested, with144 possible joint-base lifts each. Exactly576 choices satisfy the base cusp relation, and every one induces a base automorphism checked on all6912 states and both generators. The complete homology correction matrix has rank1152 at both2 and3. At2,288 choices survive over24 matrix pairs, including12 extra pairs. At3,192 survive over all48 pairs, including24 extra pairs. Exactly96 base choices satisfy both tests, over24 matrix pairs,12 of them extra. These counts concern linear cusp solvability; the final generating witness is separately checked.

The selected witness retains D33's exact G6 conjugators before the common Ihara gauge. Its mod2 target includes D27's recorded right-s-centralizer correction, retained by all later corrections in Φ(N^(2)); its mod3 target is the separately retained centralizer representative, with twice cycle39. It does not silently reduce D33's long pro2 word at3. Appending these exact constraints gives ranks1247 and1248, with affine dimensions1059 and1058. The selected base coordinates are A=(I,(6,0)) and beta=((3,4;8,3),(6,0)).

The mod2 kernel map has rank1153 on trial1. At3 the successive ranks are1099,1045,1135,1063,1081,1135,1153, so trial7 gives the generating map. Every fundamental cycle is converted to a literal B word and checked integrally; direct substitution independently reproduces every induced kernel column. The resulting J6 action is an actual automorphism.

The exponent4 upper equation then passes on its first attempt and retains that exact J6 action. Its correction rank is1152 and affine dimension1154. CRT with the recorded mod3 solution gives an actual J12 automorphism, of quotient order6912·12^1153. The cusp has order288, and the GT-shadow N_ord is144. A673392-letter corrected cusp word vanishes in all6912 graph coordinates modulo12. All1153 kernel images are checked again. The integral beta abelianization is(882,180), so the common gauge k=−702 gives an actual commutator f; both m=0 hexagons are multiplied in the faithful model and pass. The gauge leaves T=A^-1V and W=beta^-1V unchanged. D25's retained G6 rigidity makes the extra CM pair an invariant of this finite shadow.

## The actual two-cover evaluation

The six-edge S3 graph gives the exact free-basis conversion x=b1,y=b2^-1. The normalized f becomes a99308-letter word in x,y. For each n=3,4,12, its Schreier coordinates give the action through y↦f^-1 y f and x↦x. Every Schreier-generator image is also checked by direct word substitution. The compact filling matrices are exactly those of D36.

The outputs are cubic Tate4=-I and quartic Tate3=I. Both are checked against the single compact C12 matrix through the integral projection matrices. The cubic Teichmueller factor is1, hence its normalized sign is−1; the quartic projective i-exponent is0. These violate the arithmetic graph, giving a second direct nonarithmeticality certificate. This calculation evaluates the actual cover and fixed-fibre maps separately on one finite source; it does not infer GT0 naturality from a theorem proved only for Galois elements.

## Exact relative quotients and the mixed kernel

Put L4=ker(B→H4) and L3=ker(B→H3), of ranks385 and289. The sequences L→L4→C3 and L→L3→C2² give exact coinvariant isomorphisms (L_ab/4)_C3≅L4_ab/4 and (L_ab/3)_C2²≅L3_ab/3. The complementary group orders are units, so averaging proves these statements and splits the coefficient kernels.

Therefore J12's universal relative pro2 quotient overQ is B/[L4,L4]L4^4, while its universal relative pro3 quotient is B/[L3,L3]L3³. Both are actual quotients of the corresponding full relative sources. Their maximal common quotient isQ. The map from J12 onto their fibre product has exact kernel (Z/4)^768⊕(Z/3)^864. These maps show exactly what the separate prime-relative tests forget in this finite quotient.

## Reproducibility and scope

All six installed programs were run under their final names, with actual nonempty stdout and JSON certificates: d_cm_fermat_joint_base.py, d_cm_fermat_mixed_linear.py, d_cm_fermat_mixed_generate.py, d_cm_fermat_mixed_compatible.py, d_cm_fermat_exponent4.py and d_cm_fermat_cover_matrices.py. Dependencies are NumPy, the earlier exact D25/D27/D36 JSON certificates, and the preceding programs' output. Their import chain regenerates the required intermediate calculations. The full integrated runs passed, with times approximately11.5,16.6,21.2,54.3,56.6 and1.0seconds.

Agent A independently checked the base quotient, reran its complete certificate, and audited both maximal-relative-quotient proofs. The final cover and witness audit is pending. No full profinite lift of this shadow has been proved. The exact comparison with D33 stops at G6; matching its larger degree-eight action remains a separate finite compatibility calculation. The whole missing CM pair and the full profinite metabelian realization tasks remain unresolved.

## D44-D45: the recorded action is excluded

D.44 extends the recorded action through all anabelian even marked bases with their entire relative pronilpotent kernels. The exact common quotient and projection kernels are proved, and the actual A5^4 semidirect S4 source detects residual kernel A5^4.

D.45 proves that the entire recorded normalized D39 action and all D40-D44 extensions retaining it have no genuine full profinite GT0 lift. The full retained loop homology forces multiplier1; all112 central and38 complete lower-centralizer columns are annihilated by a four-term degree9 functional that takes value1 on the actual sphere target. The elliptic projection has a literal corrected finite lift. The prescribed CM pair remains open for a replacement action.

## Full profinite cyclic-cover strengthening

D20 now uses the opened Enriquez Theorem8.1 with its full proof. The exact comparison sends his positive Schreier marking to the present negative marking, checks genuine intertwining on every free profinite generator, and checks the two-step cover composition on H_mn. This proves the stated full-GT distribution equality while retaining the established Galois normalization and the separate scope of gamma multiplication. Furusho2003 was also read in full; its extra relation IV remains unevaluated on the present candidates. The original-source verification gap in D(a) is unchanged.
