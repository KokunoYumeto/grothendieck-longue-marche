# D50–D52: full source lifting and the two leading images

## Final mathematical result and source maps

D50 proves the complete multiplier-one peripheral lifting theorem from the actual free pronilpotent rank-two group to its full profinite source, with all prescribed boundary conjugators retained. It also proves the modular-source version for the actual extension `B = (C2*C3)^hat`, with pure kernel `F`, and retains the entire pro-ell gentle pair for every ell at least five. Its exact maps are the characteristic maximal pro-ell projection, the actual product `F/R_nil(F) -> product_p F^(p)`, the fibre product of the corresponding modular extensions over the same `S3`, and the normalized full pair `f = s Phi(s)`.

The finite theorem uses an arbitrary normal kernel `A` satisfying `[E,A]=A`. It does not assume that `A` is perfect. For every actual subgroup `J -> D`, with `M=J intersect A`, it retains every `J`-invariant irreducible representation of `M`, including nonfaithful representations. The finite pair group consists of `(g,B)` with the exact intertwining equation and determinant in the roots of unity of exponent `exp(J)`. Dividing by the actual graph of `M` gives a central finite cover of `D`. The graph intersects the scalar kernel trivially because of the first coordinate. This is the precise map that permits nonfaithful representations.

The pants formula is derived directly by central primitive idempotents and the regular character. It counts all homomorphisms for every actual subgroup image; subgroup-lattice Möbius inversion then counts all epimorphisms. The actual pair-cover conjugators preserve each boundary trace. The joint image is full because its Goursat common quotient is central under the actual `E` action, and hence kills `[E,A]=A`.

For the full free source choose `A = gamma_infty(E)` in every combined finite quotient. For the modular source include the actual `S3` quotient and choose the stable lower-central residual of its pure kernel. The central refinements retain nilpotence of the relevant quotient or pure subgroup. Compactness of the three full boundary conjugators supplies simultaneous source generation and all retained nilpotent coordinates. The closed lower-central intersection equals the finite-nilpotent residual; the proof uses every finite quotient and exactness of images of descending compact subgroups.

D51 constructs three actual full special automorphisms with the exact weight-five derivation coordinates `(X+Y)X^2`, `(X+Y)XY`, and `(X+Y)Y^2`, each times `[x,y]`. The complete special image therefore has dimension three over every `Q_ell`, ell at least five. D52 constructs an actual full gentle pair with pair coefficient `P9 = X^2Y^2(X+Y)^3`; its normalized automorphism has derivation coefficient `-P9`. This sign is proved from `y -> f^-1 y f`. The already proved actual Galois gamma line and this extra direction give dimension two. The exact degree-nine pentagon map excludes this pair from the full pentagon group.

## Preserved weaker route and failed proof shortcuts

The first direct scalar-cover argument was formulated for a perfect kernel and then for the stable derived residual, giving a prosolvable-to-full result. That route is retained as a corollary in D50. The preserved initial audited draft already contains the stronger full pronilpotent argument; its later changes only repaired display line breaks and explicitly identified the nilpotent residual with the closed lower-central intersection. That audited draft is preserved as `research/D_pronilpotent_lift_initial_audited_draft.tex` (SHA256 `4592fd1cfc7195e671c95c997cda35da02edd812aa9af36fc223378801013693`).

The stronger proof does not merely replace the word “perfect” by “lower central”. Its exact replacement is the action statement in the joint Goursat quotient: the common quotient is central as an `E`-module, so `[E,A]=A` suffices. Every scalar refinement really is central over `D`, so a central extension of the finite nilpotent quotient stays nilpotent. The earlier induced elementary-two refinements in D49 have permutation action and are not central in their full induced group; those refinements are not substituted into this argument.

No unrestricted Gaschütz lift is used. No equality of rational ranks is inferred from finite congruence tests. No arbitrary finite quotient is asserted to be stable under the constructed automorphism. The full source element is obtained first; characteristic projections and actual source precomposition give the comparisons subsequently.

## Literal witnesses and exact computation

The source vectors are frozen in `code/de_special_source_witnesses.py`, `.json`, and `.out`. Their original exact source is `code/de_source/d_metabelian.json` (SHA256 `a0a28d4d1d5dc05741605cfe3dc1fc11bbd779a13400593d5bd2da2dd6cc1f4c`). The three weight-five rescalings are `2, 3/2, -1`; the weight-nine rescaling is `3`. The common denominator of all four literal source/companion vectors is two. The program independently expands standard Lyndon brackets in the free associative algebra, verifies every coefficient of the special identities, verifies weight-nine antisymmetry, cabling and the full cyclic sum, and computes the canonical metabelian quotient by the right-y Fox map `M(h)=XY p`.

The first witness export before adding the independent cyclic-sum assertion is preserved under `de_special_source_witnesses_initial.*`; its literal vectors did not change. Parent's isolated replay passed in 0.387 seconds with the exact rescalings and denominator.

Geometry's independent finite scalar-cover certificate is `code/bc_scalar_cover_count.py`, `.json`, and `.out` (standard library only, authoritative saved-stdout runtime 0.314 seconds). It checks 420 quaternion projective-phase cases, 848 binary-tetrahedral surface cases, all 15 subgroups and all nine onto the specified `C3`, 1088 proper-subgroup formulas, 136 epimorphism counts, 3672 complete boundary-conjugator choices, 331776 actual degree-two pair-cover products, and the nonfaithful `D8/C4` graph/pullback. Its proof audit is `research/BC_scalar_cover_audit.md`.

## Primary-source comparison

Turaev, *Sections of fiber bundles over surfaces*, arXiv:0904.2692v1, was opened directly. Lemma 2.1, section 2.3 and Theorem 1.2 supply the parallel representation-theoretic surface framework. D50's decisive genus-zero formula is independently proved in the manuscript, including the determinant condition, every proper subgroup, and the actual boundary paths; the main lifting theorem does not import an unproved transfer from a positive-genus formula.

## Audit state and file ownership

- `sections/D_pronilpotent_lift_agent.tex`: final SHA256 `b27a2116165d03c975e4022125e92fcbf3e599f25d217b350f32a8ec26ef3ff9`; full root and geometry proof audits passed; frozen.
- `sections/D_full_weight5_agent.tex`: SHA256 `6f0a686cb8325d660c7f8bc5d7df117b016f42d6865b4f572645f12b900b907c`; full root and geometry proof audits passed; frozen.
- `sections/D_full_weight9_agent.tex`: final SHA256 `65f6eaa5e1310a8112b5f575cadc5304407ff4f1d7ee9cf7e3b29dc2038ab302`; full root and geometry proof audits passed; frozen. The reviewed draft is preserved as `research/D_full_weight9_audited_before_tex_repairs.tex`, SHA256 `18f6e76cbd75bb382a34b9058c30f578d4282b799ea69f0c4bf5f9e7fdfe3b7f`. The two repairs only restore a missing `qquad` backslash and inline math delimiters around `F`.

There is no unproved realization or full-source transfer left in these D1/D2 arguments. Both full proof audits have passed; parent has replayed the final witness export with its additional cyclic-sum assertion, compared all 42 printed coefficients of twice the weight-nine source, and is integrating the results. The CM-entanglement question in Part E uses different specified finite coordinates and remains a separate active research task, with its actual maps to be proved there.
