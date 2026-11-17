# C and E.1 research report — INCOMPLETE

## Outcome table

| Prompt task | Current result | Successor statements |
|---|---|---|
| C.1: actual torus fixed kernel K′=1 | Open. A nontrivial kernel must have an infinitely generated free pro-p quotient for some odd p; an abelian kernel is trivial. A two-generated projective retract shows the coarse conditions alone do not imply triviality. | C.1–C.4, C.12 |
| C.2: negative torus peripheral conjugacy | Open. Exact transporter and centralizer reformulations independently proved; the additional outside centralizer element has not been constructed. | C.8, C.11, C.13–C.14 |
| C.3: scalar cubic action | Open. Explicit integral symplectic lattice and a geometric filled-surface model prove why the quartic linear contradiction does not transfer; no full torus action or exclusion is asserted. | C.24, C.26 |
| C.4: LM4 D.42 | Complete independent proof, including primary faithfulness, the order-three assertion, both transposition signs, and the finite-group consequence. | C.15–C.17, C.23 |
| C.4: LM4 D.70 | Complete independent proof, including global involution sign, quartic lifting, exact dihedral quotient, integral square, and actual filling/fixed-character contradiction. | C.17–C.22 |
| C.4: LM4 D.74 | Independently proved, including full finite-coefficient duality and permutation-module detection; the stated unique coboundary does not prove the missing third-cusp equation. | C.5–C.7 |
| C.4: LM4 D.75 | Independently proved with the global sign theorem independently supplied in C.18. | C.8, C.13 |
| C.4: LM4 D.76 | Independently proved, including compact projectivity, free rank two, and exact generation criterion. | C.9 |
| C.4: LM4 D.77 | Independently proved and checked in A5. | C.10; code/check_D77.py |
| C.4: LM4 D.78 | Independently proved with all finite E-set coefficients and the exact cohomology comparison; original K′ question remains open. | C.11–C.12 |
| E.1: LM6 C.13–C.19 | Each independently proved in its exact category. C.16 and C.17 use the prime-two element theorem only. | E.1–E.7 |
| E.1: six fixed congruence kernels and H1 sets | Uncomputed. Exact inverse-limit and oval-stabilizer-fibre descriptions supplied; no full-completion/procongruence identification assumed. | E.8–E.10 |

## Scope and proof distinctions

The files `C_torus.tex`, `C_audit.tex`, `C_quartic.tex`, `C_further.tex`, and `E_real.tex` contain original successor exposition and proofs. They are not extracts of the earlier return. Statements labelled Open are still explicit tasks. In particular the result that a pro-odd kernel cannot be finitely generated is not a proof that it vanishes, and the model in C.2 is not an actual punctured-torus action.

We read LM4 D.42, D.70, D.74–D.78 and all LM6 C.13–C.19. For dependencies we read LM4 D.58–D.62 and D.68–D.69, and have independently reconstructed D.33, D.43, D.46 and the needed part of D.55, followed by D.68–D.70 and the D.36/D.41 transposition signs. The old text remains a claim under audit; proofs in the successor identify the exact continuous maps instead of appealing to an unrefereed row as authority.

The genus-three result does not solve the mapping-class congruence subgroup problem. Even for the five oval types, the formula `C_P(τ)=K_c^τ ⋊ closure(C_Γ(τ))` does not compute `K_c^τ`. In the free real type, density of the completed nonorientable mapping-class action in the displayed procongruence centralizer is an additional issue. The nonabelian H1 fibre is an orbit set for the full quotient centralizer; that action need not fix the trivial class. A finite D8 example verifies this qualification.

## Computations performed

- `code/check_kernel_model.py` and its `.out`: finite quotients of the projective countermodel, with orders 18, 36 and 324. The script checks multiplication, generation, the cyclic quotient, derived subgroup and kernel, and invariant-vector failure. Projectivity and all-open-subgroup assertions are proved in C.2, not inferred from these finite samples.
- `code/check_D77.py` and its `.out`: permutations in A5 give original generated group order 60, selected subgroup order 10, kernel image order 5 and incidence cokernel size 5. This is a full finite witness of the failure of the chosen triple to generate.
- `code/check_real_models.py` and its `.out`: D8 cocycle orbit action, the N4 orientation-cover graph and signed twist permutations, squarefreeness and exact real-root counts for the six degree-eight hyperelliptic models. Topological dividing-type assertions are proved in the text rather than inferred merely from polynomial root counts.

## Primary reading and citation discipline

See `source_log.md` and `CE_references.bib`. Each bibliography entry is marked verified only for the source and precise portion actually opened. In particular the Feit–Thompson theorem is used as an established theorem; its 255-page proof is not claimed to have been reaudited. Boggi–Zalesskii is used only for one element of order two in these sections. The possibly invalid nonsolvable-centralizer intersection is not used.

## Exact remaining work and attempted routes

1. For C.1, the finite-set formulation detects any nontrivial kernel element. The obstacle is to prove surjectivity for all actual finite E-sets, not just mod-two dimensions or maximal pro-p quotients. The projective countermodel satisfies the coarse numerical conditions and blocks that shortcut. An abelianity argument, or a theorem identifying the actual fixed group as a free profinite factor, would be decisive; neither has been established for the actual group.
2. For C.2, C.13 supplies exact unique transporters. The obstruction is an outside element in the centralizer of at least one full-unit transporter. Pro-p generation does not supply such an element in the full group.
3. For C.3, the cubic deck module has cyclotomic and regular summands. The integral fixed vectors on regular summands have pairings divisible by three; the quartic fixed-character contradiction is therefore not automatically available. The exact lattice and geometric construction are now C.24; the unresolved descent obstruction is C.26.
4. For E.1, inverse limits of finite fixed groups and finite nonabelian cohomology sets are exact, but no finite quotient of the actual congruence kernel has been computed that settles these inverse limits. The oval-stabilizer fibre gives an exact geometric target: uniqueness of its fixed lift would prove trivial fixed kernel. No such fixed-lift theorem has been supplied.

## Files and build status

The `D_*.tex`, `D_*_proof.tex`, `LM6_C_*.tex`, and `LM6_C_*_proof.tex` files are identifiable intermediate extracts copied from supplied AI text for audit. They are not successor proofs and should be excluded from the final archive as duplicate supplied material, with the exclusion recorded. Downloaded primary PDFs and their selected rendered pages document actual source reading.

A private test wrapper `CE_check.tex` was created. The first system LuaLaTeX invocation failed before reading document content because its format was absent. Root has since provided a private LuaLaTeX runtime and will build the combined paper; this is not a claim of a successful typesetting check. Build corrections and final counts will be recorded by root.

This is AI-produced research work by GPT-6 Astra (OpenAI, ChatGPT Pro mode); no priority is claimed.

Update 01:38 UTC: core D.42/D.70/D.74–D.78 and LM6 C.13–C.19 audits have full successor proofs. C.25 adds the free-factor sufficient criterion. `code/check_cubic_and_factor.py` verifies cubic lattice blocks, the 12-map S3 countermodel count, all four dyadic involutive degree-two matrices, and a quartic adapted-basis norm sample. All pass. Lead 8 / LM6 A.52 audit is next at root request.

## Lead 8 arithmetic addition

`B_arithmetic.tex` (B.29–B.34) proves the exact LM6A52 cuspidality statement with its A50–A51 prerequisites, including the missing preliminary replacement N by AN and the corrected Stix inertia citation. It proves the full completion embedding of the tetrahedral F2, separately from centralizer density, using V4 then C3 and only valid p-subgroup comparisons. This reaudits the induction already present in LM4F7.4–6.

The unlabelled tetrahedral curve has an exact Q-model with branch values infinity and ±6√−3. The icosahedral basepoint is −22√5/5, so the actual rational-point G_Q√5 action normalizes K. A direct rigid-seven-subset argument excludes all cusp inertia intersections, including conjugates and single-prime support. This independently recovers the cusp-free conclusion asserted in LM4F8. Consequently **if K is abelian, K=1**, and K has no nontrivial cofinite-support procyclic subgroup with open arithmetic normalizer. B.34 leaves abelianity and existence of two noncommuting full elements Open; no pro-p or metabelian projection is promoted to a full claim.

Failed/limited alternatives recorded: (i) five-point or H1 tests can miss six antipodal pairs; seven-point cardinality resolves this cusp issue. (ii) an arbitrary open subgroup of a totally real Galois group need not have totally real fixed field; the rational point supplies full G_Q√5 normalization for K itself. (iii) stability of a nonabelian subgroup does not give an open normalizer for an arbitrary cyclic closure, so the weight argument does not settle K.

## Exact underdetermination of the two named lifts

`B_lift_ambiguity.tex` (B.42–B.45) now gives a mathematical obstruction to computing unique tripod values from the supplied existential constructions. For E58, the prosolvable residual of G_Q kills its entire H0-relative source and both exact relative frame coordinates; the proof uses the explicit Fermat cubic with nine cusps and its CM action, including p=2,3. A separate uniform finite-section argument works simultaneously for H0 and N12: all finite sections of the relative automorphism-and-frame image exclude A10000, whereas G_Q has an explicit S10000 quotient from x10000+15x9999+10x²+30. The kernel is therefore nontrivial and preserves the complete data of both constructions.

Right-multiplying any allowed full lift by this kernel preserves all relative data and gives distinct values of every faithful tripod test and all three corrected resolvents of B53. The third target C3 amalg C3 detects the cyclotomic-trivial subgroup through the explicit degree-three cover P1 minus μ3; its deck C3 cycles the cusps, so it cannot equal a pure Galois action. At most one lift in each such coset can lie inK. This proves **nonuniqueness of test values**, not the existence of a lift inK and not binary membership variation. This ambiguity result does not by itself settle the common-kernel or resolvent-identity questions; B.55 and B.57 below subsequently resolve nonidentity and refute the proposed common-kernel equality. The generic proof controls arbitrary subquotients of finite factors and closed subgroups of infinite products; it uses characteristic-zero Jordan only on prime-to-characteristic subgroups after an explicit lift.

Primary sources, finite checks, and limitations are recorded in source_log.md and code/check_lift_ambiguity.out. B.42–45 are added to results.csv.

## Actual-K structural advance after Lead8 (B.50–B.51)

`B_sylows.tex` strengthens the actual kernel constraints. Every nontrivial Sylow is nonabelian free pro-p; K is centerless and cannot be solvable of finite derived length. The rational real basepoint gives C_K(c)=1 via the exact full extension Zhat amalg C2. Coprime fixed-point lifting then excludes any G_Q√5-stable pro-odd closed subgroup. Thus nontrivial K must have a nonabelian2-Sylow, and O_2′(K)=1.

For any odd Sylow S, its geometric normalizer has nontrivial2-part; otherwise its real normalizer would contain an involution, forcing S abelian. If S has finite rank, a nontrivial pro2 subgroup centralizes it. This is the precise remaining bottleneck for an infinite-rank upgrade. A general normalizer shortcut is false, as the two-generated projective direct product F_2^(p)×F_2^(q) shows. That countermodel is not asserted to satisfy the actual arithmetic constraints ofK.

## Further torus attempts after the arithmetic work
A full labelled splitting E=(B′×C2) amalg C2 would settle K′ via C25, but the opened Herfort–Zalesskii splitting theorem is only pro-p and the full-category shortcut has explicit counterexamples. The scalar-cubic graph-of-finite-groups realization would likewise force the standard action, but that realization has not been proved. An actual finite-order scalar power automorphism was tried and excluded as a torus-loop candidate: check_scalar_power_candidate.py exhausts all343 effective conjugators in the class-four exponent-seven quotient and finds [x²,y²] not conjugate to [x,y]^4. A peripheral IA correction remains unexcluded, so this computation is a failed construction, not a refutation of the scalar-cubic existence question. The regular three-adic blocks of LM4D71 remain compatible with all the checked cup-pairing conditions.

C27 classifies the full diagonal-power negative-involution family: x↦x^u,y↦y^(−u), u²=1 preserves the torus cusp exactly for global u=±1. Opposite odd-prime signs are excluded by a finite-field Frobenius group; the2-versus-all-odd patterns are excluded by explicit order8 and order3 generators of SL2(F7), whose commutator has order14 and is not conjugate to its inverse. All pro-p images nevertheless preserve the cusp. The full surviving cases are standard and have K′=1. This is a complete family classification, not a proof of the general torus conjugacy assertion. Code and output are check_diagonal_involutions.py/.out.
# Further main-question advance: actual relative automorphisms (B.54)

B.54 constructs an actual relative pro-seven automorphism, then a full R2 input, using a finitely specified arithmetic pants seed and exact coprime fixed-point lifting. For the icosahedral twelve-cusp cover, the resulting220 tripod tests have160 zero and60 nonzero degree-three shadows. Every full lift is therefore outside both the actual mapping class image and the Galois image. This refutes a universal braid-constrained strengthening of R2; it does not characterize all relative images or produce an element of the icosahedral kernel. The general construction works for any torsion-free normal U with prime-to-seven finite quotient and at least three cusps, including root's order29160 cover for the two resolvent nonidentity witnesses in B.55.

# Exact common-kernel counterexample (B.57)

B.57 refutes the corrected P7 equality by constructing a nonempty set of full peripheral lifts with all three resolvents exactly trivial and a nontrivial tripod action. The finite witness is an explicit A9 generating pair with three nonsplit7-cycle classes; its regular A5-induced quotient has perfect base A9^60. An infinite retained quotient imposes the resolvent identities, while the actual central refinement admits the diagonal outer-transposition action by the universal-cover argument. The common kernel is therefore infinite and contains Z2. This does not decide whether the icosahedral mapping-class kernel K itself is trivial. The proof is in B_common_kernel_counterexample.tex, with exhaustive code and output in code/check_common_kernel_alt9.py and .out; the only external finite-group input is the primary ATLAS Schur multiplier ofA9.


## General pure negative sphere actions (C.28)

C.28 extends the full-coefficient D74 argument to every sphere with at least three individually preserved cusps. The localized scalar algebra is Boolean of dimension n+1; the n+1 cusp directions have exactly one nonempty linear dependence, so the peripheral incidence graph is a single cycle. Full finite-permutation coefficients then force every geometric section centralizer to be trivial. Induction through the exact full pure genus-zero Birman sequences gives the corresponding fixed-point-free assertion for any actual compatible negative involution of the pure mapping class tower. This supplies a checked input for a possible pentagon-defect argument being investigated separately; it does not assert that the defect identity holds or that GT0 acts on the five-point tower.

The C28 corollary is also proved explicitly for full pure braid groups: split Fadell–Neuwirth sequences retain the full topology, the infinity fiber cusp is the quotient of consecutive full twists, and the inverted P2=Zhat base has no fixed elements. Consequently every actual negative GT involution has trivial fixed subgroup in P4hat. The operadic action and deletion maps are sourced to the opened primary BHR2019 §§7 and11. This is the input requested for A’s separate pentagon descent proof.

## Independent audit and extension of the unit-peripheral generation test (C.29)

C.29 gives a direct finite-covering proof that any continuous endomorphism of the full fundamental group of a compact oriented surface with nonempty boundary, permuting all boundary classes by full unit powers, is automatically an automorphism. Its proof covers the single-boundary case as well: a selected width-one boundary with zero homology must be the only boundary of the cover, forcing degree one. The pants specialization independently verifies the generation assertion already made in LM4D35; no claim of a new resolution is made. This removes a redundant generation condition from A37 and the forthcoming audited full third-cusp criterion A39. The new full-GT pentagon descent A36 and canonical pentagon A37 were independently refereed in review_scratch_A36.txt.

### C.30: full unit hexagon invertibility, and the explicit source tension

The finite-cover proof C.29 has a further consequence: a full profinite unit pair satisfying duality and the hexagon is already an automorphism. Writing A=f(x,y), B=f(y,z), C=f(z,x), the hexagon at (x,y) and its substitution at (x,z) give the exact third-cusp formula

x^lambda A^(-1)y^lambda A = (x^m C)(xy)^lambda(x^m C)^(-1).

This calculation does not assume any substitution is invertible. C.29 then supplies surjectivity and Hopficity. The pentagon solution set is a closed submonoid of the profinite automorphism group, hence contains its inverses. This answers the constrained version of Lochak–Schneps (2006), Question 1.1 as written. We explicitly preserve the discrepancy with that primary source and Fresse's later discussion rather than silently treating invertibility as previously known. No novelty or priority is inferred from an old question. The unrestricted version has the elementary A5 counterexample lambda=1, f=[x,y]^2, x=(123), y=(345), independently checked by root. Root and A independently checked the exact hexagon algebra; DE is performing a further adversarial review of C.29.

### C.31: full braid torsion forces every full monoid multiplier to be a unit

The actual full object-fixing PaB operad endomorphism gives an endomorphism of every full braid completion preserving the strand permutation. Its exact action on the full twist is derived from BHR2019's profinite ribbon extension and the literal cabling formula, without assuming surjectivity. Full braid completions are torsion-free: full finite-index and Fadell–Neuwirth topology, goodness, and the finite-dimensional unordered configuration K(pi,1) give finite cd_p at every prime. If p divides lambda, the image of the p-strand rotation corrected by z_p^(−lambda/p) would have order p and nontrivial p-cycle permutation. Thus lambda is a full unit. Together with C30 this proves the full endomorphism monoid equals its unit group. The braid/topology/cohomology part received an independent DE audit at work_DE/review_C31_braid_torsion.md; all ribbon identities were checked in the primary BHR text. This does not resolve the missing full hexagon or parameter for the canonical bare-pentagon solution.

### C.32–C.33: the canonical pentagon has every local square-unit parameter

C32 proves the corresponding relative pro-p braid monoid has unit multiplier. Pure braid almost-direct-product actions give the full induced pro-p topology and p-goodness. The preimage of a Sylow p-subgroup of S_n is the pro-p completion of its discrete finite-index preimage; finite cohomological dimension excludes p-torsion. The same p-strand rotation then excludes every integral parameter divisible by p, including zero.

C33 removes the remaining local root obstruction. The integral Magnus coefficient F(a,b) of the pentagon word is symmetric. The actual prounipotent hexagon evaluated in affine matrices gives R(T)=1−T(1−a^(−1))F(a,a^(−1))=mu*a^((mu−1)/2)*T/(a^mu−1), a=1+T. For nonzero mu, R is integral. The first possible p-denominator in H=(a^mu−1)/(mu*T), at degree p−1, forces product(mu−j) divisible by p and hence D^((p−1)/2)=1 modp. Euler and Hensel give a square unit. Degrees below p require only factorial denominators prime to p; no unproved gamma integrality or cancellation is used. The exceptional D=0 is excluded separately by C32. Root and A independently verified the affine identity, Magnus comparison and exact degree p−1 argument before formalization.

As a result, every canonical full pentagon word from A37 has a peripheral conjugator with that prescribed word at every maximal pro-p quotient; the local roots combine into a full unit. The missing full hexagon is still not inferred, and the mixed-prime obstruction of A39 remains relevant. No literature priority is claimed for C29–C33; the old explicit source questions and scope differences are documented.

### C.34: the prescribed-root version of the full hexagon question is false
The explicit A39 mixed-sign S4 example directly refutes Furusho2010 Question14 when read literally for the specified root. For f=1 and the root with 2-component−1 and every odd component+1, mu=7mod24 and m=3mod12. Sending x to(234), y to(1234) gives the hexagon image x, not1. The original pair generates S4, and the corresponding peripheral powers have distinct orders2 and4. The existential assertion is deliberately preserved: for f=1 the global roots±1 work. This distinction matters now that C33 supplies local roots at every prime. The new script checks the actual hexagon, while openly crediting A39's existing pair.

## Later main-A advance: full canonical duality and all tetrahedral generation tests (C.35)

The canonical R1 word of every negative involution in full GT0 satisfies the full two-cycle by R1 uniqueness. A short calculation in SL2(F3) then proves that its normalized substitution generates every A4 quotient. This is not restricted to full GT and uses no pentagon hypothesis. In the four automorphism orbits of A4 generating pairs, the two mixed-order cases are immediate. Binary duality excludes the collapsing quaternion lift in the (3,3,3) case. In the (3,3,2) case, one negative hexagon forces f(A,B)=1; the canonical norm and duality then force u(A,B) central, so the projective generating pair is unchanged.

The full proof is C.35 in C_further.tex. The standalone check_C35_matrices.py verifies each literal 2x2 identity and the four orbits covering all96 generating pairs; it imports no discovery calculation. The earlier A4 and SL2(F3) exhaustive scripts are retained as intermediate research certificates. They are not required to assert sufficiency of finite data, and no full word is constructed from an admissible finite table. Full generation, the third cusp, and the equality of the explicit dihedral multiplier square with the ordinary c2 expression remain unsettled.

The finite-base exploration preceding C.35 is recorded in research_relative_base.txt. The single-sign Heisenberg target cannot couple the dihedral and ordinary coordinates because every nontrivial sign-character P4 cocycle space has dimension at most2. The two-sign class2 target has a surviving invariant central direction. That direction also survives exact involution peripherality and lifts as a c-fixed element at relative pro-p levels; its pentagon lift remains unproved. These calculations identify limits of those particular local arguments, not full counterexamples.

## C.36: the requested dyadic modulo-three relative generation level

C.35 also gives the third-cusp equation in every A4 quotient for every full unit multiplier: the generated pair and the C3 abelian class determine the relevant conjugacy class. More substantially, the canonical normalized substitution is an actual automorphism of F/O²(U3), U3=F′F³, for every unit multiplier. The ten-dimensional Frattini module over F2 splits into the two-dimensional invariant part and four distinct two-dimensional C3²-simple modules. Each nontrivial module is detected by an A4 quotient, so C.35 makes all four restrictions invertible; the invariant part is identity. Frattini and the defining full relative quotient then give the automorphism. The original full coboundary identity supplies intertwining with c. This settles the indicated generation condition at the specified relative dyadic level, while leaving its third cusp unproved. Root and A independently reviewed this argument.

## Post-checkpoint05: all icosahedral generation tests and a full coinvariant identity

C.37 proves that the canonical R1 word of every negative involution of the full GT0 group passes every individual A5 generation test, including all unit-powered substitutions. The proof covers all19 Aut(A5) generating-pair orbits. It combines the actual commuting involutions alpha and v=Inn(u^-1)iota, full binary duality in SL2(F5), C.28's three-class cusp incidence, and a direct high-degree cohomology proof that tau=alpha*v has exactly one full section class. Root, A, and DE independently reviewed the proof; DE independently reconstructed the finite classification with S5 permutations and no imports from the matrix certificate. The formal source and register now include C.37.

C.38 identifies the closed normal subgroup generated by tau(g)g^-1 with the normal closure of the third cusp z. Consequently the full coinvariant quotient is Zhat. The cusp itself is a single commutator [g,r] with a local involutory section r, and hence is conjugate to a twisted commutator h*tau(h)^-1. This does not give generation by the selected g,r or a free-product recognition theorem.

The distinction between individual and joint finite generation remains essential. A separate finite consistency certificate exhibits c-fixed, binary-dual values in the nineteen binary icosahedral factors that pass every individual generation test while merging two kernel coordinates and changing third-cusp order. For example the (3,5,2) and (5,3,2) pair orbits map to (3,5,5) and (5,3,5), with all other coordinates unchanged. This table cannot be a full canonical word for c, because full C_F(c)=1. It records a precise limit of the finite necessary conditions, not an actual counterexample to the main full question. The exact code/output are check_a5_finite_constraints.py/.out.

C.39 adds every individual S4 generation test and actual automorphisms at all dyadic relative levels F/O²(ker(F→S3)). Its scope is every negative involution in the full peripheral group P: no GT0 symmetry, duality, hexagon, or pentagon is used. The finite certificate checks all30 S4 subgroups and all216 generating pairs. The relative proof passes through an arbitrary finite2-by-S3 quotient and its normal2-kernel Frattini quotient; it explicitly does not assume that this finite quotient inherits an endomorphism. The two simple F2[S3] modules give C2×S3 and S4 as the only split obstructions, excluded by abelianization and the finite generation theorem. No relative third-cusp assertion follows. The register now has63 rows.

Independent reviews of A50 and A51 are complete and saved as review_A50.txt and review_A51.txt, with exact rerun outputs. A50's cohomology wording was repaired to expose the actual infinite normal subgroup or, more economically, the H1 noninflation argument. A51's strict second scalar layer and its subsequent stabilization pass the actual-refinement audit, including relative perfectness and finite-kernel sequencing.

A53's final structural theorem for every finite abelian residual layer has independently passed the complete actual-refinement review, saved in review_A53.txt. It proves bounded scalar stabilization with m=max(1,e2+1,2e3+1) under H1(C,Vdual)=0, and establishes that hypothesis for every finite abelian quotient of a relative-pronilpotent residual using the actual normal pro-p-prime factors. The class-two and wedge-center induction works at every stage. This settles scalar depth in the stated scope; it supplies neither prescribed equivariant frames nor a full negative norm solution.

## Correctly marked symmetric-four quotient: C.40

C.40 now proves the actual canonical third-cusp equation in every S4 quotient for every negative GT0 involution, at the universal dihedral unit d=2kappa+1 with its global sign fixed by d=1 modulo4. This goes beyond generation. The common S3 word values are forced by the full R1 equation, the dihedral result, and full duality. In GL2(F3), the actual words therefore lie in a completely enumerated necessary-condition set: for each of six head choices, its two components have64 and16 possible paired arrays, and every array has the required projective third cusp. The exact matrix table is asserted in the code. Proper images are covered by the A4 theorem, the dihedral definition, or centrality of D8's derived subgroup. Root and A independently read the proof and reran the complete certificate.

The marked result also proves that theta_d fixes every S4 epimorphism-kernel orbit and acts as an automorphism on the actual joint finite S4 quotient. The basis-power automorphism transfers that conclusion to canonical psi. No identification with a direct product of nine S4 groups is made, and neither full nor relative marking is inferred. C.40 and its dependencies are registered; the component now has64 rows.


## Recovery and seventh-hour results

The replacement environment was restored from checkpoint06. C41 and C42 have been mathematically reconstructed from the previously accepted proof retained in conversation; their text is not claimed byte-identical to the lost version. The exact C41 covering-graph certificate was reconstructed and independently rerun, reproducing60 vertices,120 edges, cycle rank61, invariant-chain dimension64, boundary rank28 and invariant-cycle dimension36. The first-step bound excludes all three nonidentity fixed head values only when the actual parameter vanishes in that enlarged quotient. C42 records the known Scheiderer degree-one separation with the direct split-HS verification and the additional finite canonical-head consequence.

C43_regular_pants.tex saves the root-accepted orbit-duality extension separately pending integration. It keeps the swapped cusp pair in the relative augmentation module until localization, proves the one fixed-cusp action has trivial full section centralizers, and supplies uniqueness of the common-normalizer transporter. No free-product recognition or generation conclusion is inferred. The finite r-frame can be adjusted through A16 when the base transporter exists; failure for one chosen finite frame is not an obstruction to all choices.


## Eighth-hour integration and exact integral frame data

C.43 is now integrated in C_further.tex and the component register (67 rows), after root reread the complete reconstructed source. The common-normalizer consequence retains its full-word scope and the variable-r-frame caveat.

The actual GR(4,3) coefficient and affine certificates have been executed after recovery. They lift the four free cusp cocycles, retain the literal old A56 s- and r-frame reductions after the complete basis/coboundary correction, and check the integral conjugacy and norm identities. The exact remaining scalar-center gate is documented independently. Central halves in the six free order-four coordinates repair the new frame squares existentially while changing newer A56 central frame values; older family data can be retained. This must be distinguished from the separate restricted fixed-witness failure and from a full profinite involution.


## Ninth-hour regular-pants advance

C.44 proves that the unique full section conjugator g for the regular pants action has unit exponent in the full procyclic quotient. The exact module K/Phi2(K)=F2[[Zhat]] gives theta D_a=1; evaluation at every odd-prime character supplements the dyadic augmentation and forces a full Zhat unit. A Frattini argument then proves actual generation and conjugacy on F/O²(K), with the full procyclic head retained. The claim is in the automorphism group of this relative quotient; neither original peripheral marking nor full F generation is inferred. Root independently read and accepted the complete proof before integration. The component register now has68 rows.

The C44 conclusion is strengthened, with root approval, to every relative pro-p quotient and the relative pronilpotent quotient F/R_nil(K). Once the full unit is established, the cyclic-cover module argument works at each prime; the exact product of distinct-prime Sylows combines the generation results. The formal proof includes this product comparison and retains the unmarked automorphism scope.

## Post-checkpoint10: exact equivariant-lifting boundary and matrix rigidity

**A.70 is proved and independently reviewed by root and the involutions
agent.** The actual source-central quotient of
`E0 = Fhat2 semidirect c` over `N = ker(Fhat2 -> (Z/12)^2)` has order13,824,
with orientation normal forms `x^a y^b [x,y]^d` for a,b modulo24 and d
modulo12. Its power-seven automorphism fixes the external reflection,
preserves all three named reflection classes and all three pair-product
cusp classes, and is an involution on the entire actual central quotient.
It has no full reflection-equivariant peripheral lift, even of infinite
order: after normalizing the external reflection, the full fixed-group
theorem forces literal powering of x,y, and the S4 test gives incompatible
orders2 and4 at the third cusp. This is an exact finite-base failure of an
unrestricted equivariant analogue of the central criterion. Its multiplier
is mixed, so ordinary R2 and the same-action multiplier-one restriction
remain untouched. A separate, explicitly typed corollary gives
multiplier-one identity central data between two different actual full
negative actions with no full multiplier-one intertwiner. The ordinary
arithmetic lift matches the entire class-two quotient, not merely its
abelian head.

**A.71 proves the precise finite-ring and profinite form of classical
three-trace rigidity.** A full peripheral automorphism with common
multiplier+1 or-1 acts on every residually absolutely irreducible
representation into SL2 of a finite commutative ring by conjugation inGL2.
The proof compares the complete multiplication table in the basis
`I,X,Y,XY`, proves the local matrix-unit innerness directly, and obtains a
single conjugator in an inverse limit by compact common refinements.
Kernel stability is a conclusion, with no prior stable-head or semilinear
action assumption. In particular all PSL2 finite heads and all their
residually irreducible rank-two ring deformations cannot provide the
suggested noncentral obstruction. The finite-field input is classical
(McCullough & Wanderley,2013,Theorem8.2, recording Macbeath); no priority
claim is made. The result does not apply to the canonical unmarked word
before its third cusp has been proved.

The nonsplit M10 extension was fully verified as a broader embedding
obstruction, but was not promoted to an actual-source counterexample.
All its inverse-compatible generating pants heads have passport(4,4,4)
and fail the central SL2(F9) three-sign gate. The direct determinant,
class, matrix, and permutation certificates and the corrected
transported-head count formulation are preserved in
`research_equivariant_R2/`. The exact group13,824 checker tests every
element and generator edge. Formal input is `A70_A71.tex`; component
register now has70 rows.

The independent main-construction review `review_mixed_scalar_704.txt`
accepts the actual mixed-cup scalar upper bound, source attainment and
next stability:704 total third-center dimensions,128 previously retained
and576 new. The new action and frame equations are explicitly separate;
that review does not infer them from the scalar count.


## Same-action prescribed-frame limit (A.74)

A.74 is proved, with the research proof and exact finite certificate read
and accepted by root. It gives identity multiplier-one data on the entire
actual orientation-central quotient SL2(F5) × Zhat², with a central
order-two, norm-compatible prescribed cusp/reflection conjugator. No full
map intertwining c with itself can retain that frame image. The finite
full-source-central quotient has order960. The identity lifts when frames
may vary. This is a limit on prescribed equivariant conjugators, not an
obstruction to a negative cocycle h c(h)=1 or the main conjugacy problem.

The earlier dyadic order2048 test is preserved as a weaker source-central
example; its frame need not centralize in the orientation-central quotient.
The theta1 order13824 attempt is explicitly rejected for the stronger
reflection-labelled interpretation because it fails the xc conjugacy class.


## Post-checkpoint11: exact four-triple normality limitation

B.77 identifies the partial presentation from the actual four transported b-triples as (F9 semidirect Z) * F10. The eight replaced peripheral words form an explicitly verified triangular Nielsen basis. A single S4 quotient proves that local pair normalization does not normalize the entire special-source deletion kernel, also after full completion. The actual retained base1 monodromy excludes that finite quotient, so this does not determine the full pencil or the main centralizer. Complete proof, source hashes and certificate are in B_four_triple_gap.tex and four_triple_normality_gap.json. The final B.76 relative-special-fiber counterexample was independently reread and accepted.

## Post-checkpoint12: complete pencil audit and one-tangency limitation

The complete source-marked sum-pencil presentation B.79 was independently read and accepted: all26 local types, all82 transported relation generators, the unavoidable three-strand projection resolution, and the source boundary C=R*y10 are retained exactly. The inherited LM4 F.21 theorem excludes nilpotent separating quotients, so the drafted class-two program was not executed. One authorized full S5 solver attempt, imposing every actual monodromy and the entire source stabilizer condition, returned UNKNOWN at its five-minute limit; it gives no finite-degree exclusion or counterexample.

B.80 refutes the stronger proposed relative principle with only one exceptional retained source point. The retained parabola y=x², deleted tangent line y=2x−1, and source y=0 have an explicit connected eight-sheet D8 cover. On the actual source deletion kernel its image is C2, whereas the ambient deletion kernel has image V4. The finite quotient also separates the actual compact images in full profinite completions. The source infinity point meets only retained infinity transversely; the deleted line is tangent to the parabola away from the source. This is a counterexample to the general shortcut, not to the fifth-root marginal with its extra F21 normal-generation property.

The complete action-only obstruction A.79 was independently reread and accepted, including the all-frame centralizer-surjectivity argument, exact order-four detector, and finiteness of every actual source-central refinement by transfer. Reviews are preserved in review_A79_formal.txt and review_B79_sum_pencil.txt.


## Fifteenth-hour actual controlled filling kernels (B.83)

B.83 is proved and independently accepted by root and the DE agent. In the actual ordered fifth-root surface, let H_* be the source subgroup generated by two constant-family meridians and the three specified base lifts at 1, zeta and zeta^4, and let T be obtained by adjoining the actual product-one meridian b. The normal closure J_* of the two constant-family meridians is the complete actual ambient constant-family filling kernel inside T, with T/J_* = Z x F3. The corresponding both-family source kernel I_* is the complete both-family filling kernel inside T, with T/I_* = Z^2. The same equalities hold for the actual closed images in full completions.

The proof controls whole mixed source-operator orbits. Both initial b-strips are complete kernels, and every correcting conjugator for the three actions and their inverses lies in that already b-normal initial kernel. The stage induction retains its middle conjugation; the earlier invalid relaxation to arbitrary final-subgroup normalizers is expressly not used. The actual function (vw-1)/(w-1)^2, constant -1 on the source, and the actual base maps give left inverses to the universal quotient maps. This proves the discrete and compact intersections without assuming the full induced topology on the abstract subgroup T.

The result concerns this specified source subgroup only. Global source-kernel normality, the full fifth-root marginal, and the main centralizer remain open. The independent common-marking certificate verifies all 24 pencil braids, all 132 twelve-generator action comparisons, both source-adapted basis maps, and the collision-free deformation from rational coefficients to the true fifth roots. The final formal fragment is B_product_one_controlled.tex; DE's independent review is work_DE/next_marginal_source/review_B83.md.


## Sixteenth-hour coupled diagonal/product kernel (B.86)

B.86 is proved and independently accepted by root and DE. The actual source words define L=<d,C,P1,P2,P3,Q4>, with C=b c1^-1 b^-1 and Q4=a^-1 P4 a. The complete normal closure N of C inside L lies in the actual constant-family source kernel J_c. This controls arbitrary mixed diagonal/product conjugations, using a quantified Schreier argument whose retained directions are all proved to have complete diagonal strips in H. The actual exponent kernel K is exactly L intersect H, and L/K=Z; the same conclusions hold for the actual closed images in full completions. The signed winding of (v-w)/(w-1), constant -2 on the source, gives the exact detector without changing the transported orientation of d.

The proof reconstructs its three filled-node relations from actual common-marked peripheral pairs, and uses the actual corrected source element P1^-1 g2 P1 for the positive triple. It does not identify N with J_c intersect L and does not prove whole-J_c normality. The separate zero-source word Z'=a^-1 b^-1 z b a remains of unproved membership in H; the failed membership test in one specified 169-word subgroup gives no global nonmembership assertion and is not used. The accepted formal fragment is B_coupled_diagonal_products.tex.


## Exact negative zero-source membership (B.88)

B.88 refutes the specific membership Z'=a^-1 b^-1 z b a in the actual source H, also in its actual compact image. The two actual based maps f1=v and f2=v(w-1)/(1-v) to the three-punctured sphere agree pointwise on the source. Their paired UT3(F2) quotient is onto D8 x D8 of order64 and sends H exactly onto the diagonal. The primitive peripheral coordinates force the two images of Z' to differ by the nontrivial central element, independently of every whisker and orientation. The executed checker verifies all32 possible central-coordinate choices; no wider membership search is used.

This closes only the separate zero-word gate discussed at the end of B.86. Both geometric maps factor through the both-family filled surface Y_b, so the detector kills the entire ambient filling kernel R and cannot separate the source deletion-kernel image I from R. The full marginal remains open. B.86's final limitation now points to this exact negative result; its coupled-kernel proof and its signed diagonal character are unchanged. Root and DE read the complete source and checker and accepted them.


## Eighteenth-hour uniform old-base cohomology and exact overlap obstruction (B.96)

B.96 is proved and independently accepted by root, A and DE. Every actual old-base translate of the full retained-deck node module is F-stable, free of rank64 over Z[G], has H1 isomorphic to F2[R]^4, and has H2 zero. Its H1 image lies in the actual source left ideal J_I. The sum of these individual images, over all old-base words, is exactly J_I. This is a uniform two-coset proof, using the actual source F19=F8*F11 filling and all eleven returned source operators; it is not an extrapolation from a finite orbit depth.

The odd-loop certificate distinguishes positive geometric push from pullback. The four pullback anti-chains give the actual four second-sheet source peripheral words, with the displayed inverses; the positive push gives their actual branch-square source images. All sixteen cone reductions, eight complete product-tree chains and their boundaries, both free-group discrepancy equations and all displayed source words were independently checked. The source naturality argument uses the intrinsic right defect, so it does not assume a free-factor marking is literally preserved.

For the direct sum D_old of the individual translates, the actual addition map onto the full node-relation module Lbar has kernel K_old. Its long exact C2 cohomology sequence gives a canonical residual map H2(K_old) to I_F2[R]/J_I with image U/J_I. This identifies precisely where any extra obstruction can enter. It neither identifies K_old with B.92's differently marked relation kernel nor proves that this residual map vanishes. Pairwise overlap tests alone do not control intersections with the whole preceding sum. The full marginal and nonlinear fixed-lifting questions remain open.

The accepted fragment is B96_old_translate_cohomology.tex. Private QA renders and inspects all five pages, with no clipping, overlap, overfull boxes or undefined references. The initial unavailable pdflatex format and the pre-correction line-break PDF/log are retained; the accepted LuaLaTeX build uses the main paper preamble. No new bibliography is required.


## Nineteenth-hour complete selected head kernel (B.99)

B.99 is proved and independently accepted by root, A and DE. In the actual common marking, the K-row stabilizer of (6,6,y1) at node (8,0) is exactly the kernel of the constant-v=zeta² section head. Fill the four old q-root fibers other than 1 to obtain X0, whose q projection is the actual F5-by-F2 bundle. Its other projection, to v, has generic fiber F4 and precisely one filled finite critical value v=-1. The actual old-base map is (b,d,1,a,1,c), and the complete generic-fiber kernel is the F4 normal closure of the full signed orbit of [c,d] under the two explicitly displayed automorphisms. Pulling it back gives the complete selected stabilizer, with no bounded-depth inference.

The unfilled constant section is injective; the local commutator vanishes only after the X-to-X0 filling. An extending continuous far section, exact old-to-far cut conversion, the empty q=399/40000 to q=1/100 connector, and both inverse geometric pushes are all retained. The independent producer reconstructs all seventeen rational polynomial segments and resolves simultaneous crossings in the opposite order. A separate exact margin certificate proves the rational-to-cyclotomic deformation: v-critical distances at least 1/1000, initial cut gaps greater than 1/3, and true base displacement less than 2e-28.

The statement concerns an augmented-row/head kernel. It neither gives full-column monomiality nor settles the full source-translate overlap, B.96 residual map or either main problem. The attempted giant full-chain expansion was interrupted and is preserved honestly; the completed literal-word calculation only shows that this particular transformed relator has a different cyclic length. The earlier failed straight-path projection assertion and an overly coarse radical interval check are also preserved with genuine outputs.

The accepted input is B99_section_head_kernel.tex. Private LuaLaTeX QA renders and inspects all four pages; the final build has no overfull boxes or undefined references. The initial long-path layout failure is retained. No bibliography entry is added.


## Late nineteenth-hour reviewed research: all diagonal kernels and exact full-chain coordinates

The complete B.99 kernel description has been transported to all eight actual physical diagonal rows. Three exact four-strand bridges and the actual q-preserving swap identify their kernels in the same old B6. All four literal six-to-four maps, both bridge directions, eight cone equations and every operator diagram were independently replayed by DE. Each kernel has a finite substitution description: two inactive peripheral meridians plus the full signed orbit of one transported node relator under two explicitly verified free-group automorphisms. These auxiliary substitutions are not claimed to be full-surface monodromies. The complete research proof is research_all_diagonal_head_kernels_19h.txt; root reserves B.101 for a later formal integration.

The previously interrupted giant full-chain calculation is now completed in an exact alternative integral basis, without expanding its67,823,551 naive rectangles. Root A-paths tensored with positive B edges form a genuine free abelian basis of the complete product-tree module. The actual119,780-letter geometric commutator image has33,162 normal-form terms; the original node has42. The reusable G-action sends each such term to at most two terms because the retained action permutes the positive Schreier basis literally. Therefore this exact image is not any signed G-unit multiple of the original, since33,162>84. This is a complete coefficient calculation, not an augmented-row or cyclic-word inference. It gives no whole-span nonmembership or overlap/κ conclusion.

The full input, persistent word DAGs, complete boundary telescoping and all117 original calibration coefficients were independently replayed by DE. A independently passed the basis and actual edge-action proof. Generic G-module identity, inverse and product operations on all33,162 terms also pass without rectangle expansion. Files are code/factored_product_tree_chain.py, code/root_path_chain_operations.py and their genuine outputs, next_symmetric_nodes/geometric_stabilizer_factored_chain.json, and research_factored_full_chain_normal_form_19h.txt. The earlier interrupted attempt remains preserved.

Finally, the independent primary/algebra review review_actual_nodal_Smith_comparison_19h.txt passes A's ordinary Brown–Loday/Hopf and exact Tate edge-map comparison. It keeps the full E-cover coefficients, the homology degree shifts, the right-defect sign and the possible H2(C2,Z2) contribution. Neither fixed-graph dimension nor the newly proved nonasphericity determines κ. The actual geometric relative-model gate was reviewed separately by DE; root reserves B.102. No further formal CE row was added beyond B.99.


## Checkpoint20 accepted addition: B.101

B.101 proves the complete discrete head kernels for all eight actual diagonal rows. The four literal six-to-four maps, three based physical bridges, swap comparison and two signed substitution operators are fully specified. Each kernel is the preimage of B.99's complete two-operator node-relator kernel. Both involution cone classes are included. The algebraic auxiliary substitutions are not asserted to act as full-surface monodromies, and no full-column overlap or main marginal equality follows. Root, A and DE independently approved the complete formal text.

Canonical fragment: `work_CE/B101_all_diagonal_head_kernels.tex`. Private component: `work_CE/qa_B101/B101_check.pdf`, four pages; all four rendered pages inspected. Final LuaLaTeX log has no overfull boxes, undefined references or LaTeX warnings. Initial double-superscript and accidental lambda-token replacement failures, plus the aborted occurrence-count repair, are preserved with their genuine outputs. Exactly one owned result row, B.101, was added; no global register was edited.


## Checkpoint20 full-coefficient and nonlinear work

The actual35 full21 Fox matrices and both sheets of128 node cycles are complete. The finite32-by359 boundary retains all231 source faces and128 actual nodal faces, with319438 exact coefficients and every next-boundary checked. Its genuine128-node involution retains raw orientation signs and every physical-mate free-word conjugator; all full boundary and double-involution identities pass. These are full finite-model data, not old-word depth samples. DE independently replayed the stable inputs and matrix companions. The independent B100 sphere check confirms the two complete ten-term cycles and their distinct private node rows; only their induced rank-two spherical block has zero Tate cohomology.

The exact source-face elimination gives unique completion and a finite node-domain kernel. The saved reindexing note identifies this actual kernel with B96's full old-base orbit kernel, using the two cosets and actual source corrections. It proves no obstruction vanishing.

The nonlinear comb basis is proved by an actual spanning tree. All128 short node words were fully re-expanded and checked, with128 explicit individual primitive witnesses. The existing geometric stabilizer image has46944 nonlinear basis letters, abelianizing to the complete33162-term B103 dictionary. The large generator expansion was not performed; the exact prefix invariant supplies that rewrite. The note also gives the selected-cone decomposition through a compatible Bass–Serre transversal and retains every actual G/source translate in the filled quotient. It does not infer a simultaneous basis, a global centralizer, or a profinite comparison.

Complete formal reviews of B103, B104 and B105 passed. Owned source, data and research paths with hashes are in `work_CE/checkpoint20_status.json`. Both main problems remain open.

The late nonlinear transport addendum keeps the actual section defect. For the comb section q_g=v*u*t, multiplication has the nonabelian cocycle omega(g,h)=v[u,tau_beta(t)(h_B)]v^-1. The complete transport of a comb generator is a conjugate of the product of two explicit comb generators; its abelianization gives the earlier two-term coefficient action. The involution has its own literal section defect and an exact finite comb-word formula. Seven universal free-word identities pass in `code/check_nonlinear_comb_transport.py`, with genuine output and the full certificate retained. Associativity proves the three-variable cocycle identity. No strict nonlinear coefficient action, simultaneous relation basis, normal-closure decision or fixed-lifting conclusion is inferred. The complete proof is in §§7–8 of `research_nonlinear_comb_and_cones_20h.txt`. A and DE independently passed the full proof; DE separately replayed all seven identities without importing the producer. The compatible-transversal and left-coset qualifications remain explicit.


## Checkpoint21 structural research, with no new owned formal row

The product-tree lemma is proved in the actual countable CW scope: every cubical subcomplex of two trees has the homotopy type of a graph. Relative leaf-strip collapses give genuine free-factor inclusions between finite rectangle components, so compatible bases prove freeness of the full fundamental group rather than mere local freeness. Root, A and DE passed the complete proof. B105's nonzero spherical block excludes a direct homotopy equivalence of the unchanged actual nodal complex with such a subcomplex; the missing comparison must be at the level of the group and account for redundant two-relations separately.

The first unit-circle neck has an actual common rank-five subgroup. A cotangent inequality selects the four A punctures and one retained branch in one disk, transported through the same regular neck into both bad regional vertices. The one-family filling detects that subgroup as a free factor in an actual rank-seven fiber. This map is used only on the ordinary orientation kernel; characteristic fiber quotients and the finite-index core supply full induced topology in the orbifold vertices. For simply connected inner and outer cut regions joined through this one neck, the actual discrete orbifold pushout is a genuine amalgam over that rank-five subgroup. The complete proof passed root, A and DE. It does not justify the other necks or a profinite amalgam.

The proposed common supported point-push extension has an exact winding obstruction: outside the unit circle winding about0 equals winding about retained1, while inside the latter is zero. A common supported class cannot flip a square-root lift. The standard middle-neck selections are mixed. An initial generic disk-transport inference was withdrawn because it did not control the vanishing arc; the correction and its provenance are preserved. A subsequent literal half-plane/quadrant argument does control actual vanishing arcs and proves that the three natural middle rank-five maps are noninjective. DE owns the complete all-three proof and A's independent review passes.

For the first mixed neck, CE proves explicit shrinking radial arcs on both sides, keeping the retained branch strictly on the correct side. The exact radical bounds and DE's independent Fraction polygon/cut calculation give the two normal relations `[a,b]` and `[a,w b w^-1]`, where `w` is the product of the three middle meridians. The quotient by precisely these two relations is an HNN extension of `Z(a) x F(b,d)`, with `w b w^-1=d`, freely multiplied by a rank-two free group. Its cyclic kernel has a bipartite infinite path commutation presentation. This is only a two-node block; it does not identify the full shared edge group or the actual full nonlinear kernel. Both main problems and the full residual obstruction remain open. All research, genuine outputs, independent checks and the initial alternate convention are preserved in the checkpoint21 inventory.

## Checkpoint23 research continuation

The complete CE record is `work_CE/status_hour23.txt` and its machine status
`work_CE/checkpoint23_status.json`. Independent actual annular source/F5
replay and B112/B114 formal audits pass. The selected lower-disk lift required
a correction from the lower to upper y collar; both the failed interpretation
and the valid lower cut record are preserved, and the corrected actual gap
cone is `a C a^-1`. DE's literal eta is independently replayed. The whole
one-neck group now has a fully marked9/36 presentation with six actual source
words. The full height quotient keeps every translate of both cross relations;
a proposed zero-level coarse simplification was exactly refuted. Two authorized
complete subgroup intersections are trivial, with separate independent folds.
New uniform regional proofs give cone/K centralizer intersection1, exact
cone-loop/K normalizer the primitive gap-branch cyclic group, and relative
edge avoidance in both discrete and full categories. These are pre-cross
quotient results only. Both main decisions and the final one-neck centralizer
remain Open; no additional orbit or finite-group census was run.
