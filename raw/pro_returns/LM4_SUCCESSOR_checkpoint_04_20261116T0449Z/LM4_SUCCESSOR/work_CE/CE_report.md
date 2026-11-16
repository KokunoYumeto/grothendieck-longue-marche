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
