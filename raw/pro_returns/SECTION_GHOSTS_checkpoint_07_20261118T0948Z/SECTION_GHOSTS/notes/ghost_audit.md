# Ghost-construction audit

Date: 18 November 2026. Model: GPT-6 Astra, independent delegated proof review in SECTION_GHOSTS. No local section theorem is used.

## Early determinations

1. The finite-support reconstruction (SECTIONS_OVER_Q A.32 = GT_TOWER_CHECK C.1.1) has an elementary complete proof. It holds when **any one** of A, B, A/B has finite support, a stronger condition than requiring the union of the supports to be finite.
2. The original A.44 arithmetic recursion is internally sound. Its previously unverified radical-field calculation, simultaneous Chebotarev/CRT condition, new-prime local solubility, and ordinary local limits all survive the present proof review, including primes 2 and 3. A separate reconstructed proof is being written in `sections/part_B_audit.tex`.
3. Lead L2 contains a false compactness assertion. The family of original A.44 ghosts is noncompact already at class one: projection modulo fifth powers has infinitely many distinct images `3 q_0^24`, while all later factors vanish. This does **not** refute the fixed-abelian-cocycle compactness claim C.1.6. It refutes its transfer to a varying family of ghosts. The repaired statement must keep the abelian pair fixed.
4. C.2.13–C.2.16 and C.2.18 assert exclusions for deliberately **selected** outputs of A.65 and A.72. They do not assert that every output of either original recursion is excluded. Thus their quantifiers cannot settle prompt B3.
5. A.207 is an exclusion of everywhere locally point-or-cusp-matching class-four sections, and explicitly asserts existence of an unrestricted global class-four section. It is not an unrestricted class-four failure. The same distinction appears in C.2.2 (class two).

## Sources opened at their cited locations

- Milne, J. S. (2020). *Algebraic number theory* (v3.08). https://www.jmilne.org/math/CourseNotes/ANT.pdf . Verified: Theorem 8.31, printed p. 147, Chebotarev; Theorem 7.32, printed p. 120, Newton; sharper unique-root bound immediately after the theorem, printed p. 121. Tool references `turn708818462view0`, `turn825516894view0`, `turn825516894view1`.
- Faltings, G. (1983). Endlichkeitssätze für abelsche Varietäten über Zahlkörpern. *Inventiones Mathematicae, 73*, 349–366. https://math.uchicago.edu/~drinfeld/Deligne%27s_conjecture_Manin_conf/Faltings_argument/Faltings.pdf . Verified: Satz 7, printed p. 365 (PDF p. 17), rational-point finiteness for curves of genus at least two. Tool references `turn708818462view1`, `turn825516894view2`.

The search terms were `Milne algebraic number theory Theorem 8.31 Chebotarev 2020 pdf` and `Faltings 1983 Endlichkeitssatze abelsche Varietaten Zahlkorpern Satz 7 365 pdf`. These searches verify the named inputs; they are not a priority search for the reconstructed propositions.

## Files read so far

- `sections_over_q_cp17/sections/ghost_agent.tex`: A.42 and A.44, read in full.
- `gt_tower_check_cp10/part_c_results.tex`: C.1.1 and C.1.2; C.2.1 and beginning of C.2.2.
- `gt_tower_check_cp10/part_c_general_exponent.tex`: C.2.10–C.2.11, read in full.
- `gt_tower_check_cp10/part_c_fixed_depth.tex`: C.2.12, read in full; its cohomological prerequisites are delegated to the cohomology reviewer and not independently certified here.
- `gt_tower_check_cp10/part_c_class3.tex`: C.1.14–C.1.15 and C.2.4, read in full.
- `gt_tower_check_cp10/part_c_class3_original.tex`: C.2.6, read in full.
- `gt_tower_check_cp10/part_c_local_rigidity.tex`: C.1.16–C.1.17, read in full, no defect found in targeted review; root handles the final scope of this result.
- `gt_tower_check_cp10/part_c_prefix_topology.tex`: C.1.21 and C.2.9, read in full.
- `gt_tower_check_cp10/part_c_unbounded_finite_failures.tex`: C.2.13, read in full.
- `gt_tower_check_cp10/part_c_finite_failure_bound.tex`: C.2.14–C.2.16, read in full; the weighted-augmentation collection proof appears sound, with the commutator convention checked.
- `gt_tower_check_cp10/part_c_a72_class3.tex`: C.2.18, read in full.
- `sections_over_q_cp17/sections/point3_class_four_1129_obstruction.tex`: A.207, read in full; its unavailable dependencies A.61, A.62, A.186 etc. have not thereby been certified.

## Main-question approaches considered and their unresolved gates

- **A fixed support valuation versus denominators at all weights.** The A.65 construction makes a valuation divisible by products of `(q^k−1)` for finitely many weights. No nonzero ordinary integer can satisfy the naive infinite divisibility condition. This does not prove impossibility, because the numerators of the actual obstruction can vanish or cancel. There is no converse divisibility theorem in the inspected argument.
- **Compactness of all survivors.** False for a varying ghost family (A.101 below). This does not decide whether a fixed pair can survive every class.
- **Diagonal prime choices through all weights.** The existing A.65 parameters change earlier support exponents when the target weight increases. They do not extend an arbitrary finite prime/exponent prefix through all weights. The original A.44 prefix extension theorem makes failure dense, but provides no extension theorem for survival. A branch through successively chosen level-dependent ghosts has not been constructed.
- **A rank-zero elliptic cover at three.** The pro-three subgroup induced on the degree-27 cover has the correct pro-three topology, but a full pronilpotent section of the base does not automatically yield all pro-ell geometric quotients of that cover for ell different from three. The corresponding open subgroup and completion must be compared. Root is proving this comparison explicitly.
- **The class-three local remainder.** The finite residue formulas can test integrality coordinate by coordinate, but global continuous vanishing additionally needs the quotient family to tend to zero. This is not a determination of which prime recursions obey those conditions, and no point of the original A.44 closed remainder has been constructed by this review.

## Current status

The main fixed-pair limit statement is not resolved by this audit. No all-depth ghost, nor proof of universal finite support, has been produced. The firm correction is the noncompactness of the varying ghost family and the precise quantifier/local-matching distinctions above.

## A smaller class-three gate obtained during this audit

Statements B.101–B.102 in `sections/part_B_audit.tex` now prove a substantive reduction for B1, subject to the independently checked global weight-two and strict-localization inputs documented by the cohomology reviewer:

- At most **one** of the twenty-four global integral class-two classes can lift to class three for any ordinary pair with valuation `(1,0)` at three and `(0,1)` at two. The original A.44, A.65, and A.72 constructions have these valuations.
- There is exactly one class-two class passing the two necessary local tests at `(rational place, coefficient prime) = (3,2)` and `(2,3)`. Twisting by `k eta`, with `eta=(chi²−1)/24`, changes the first residue by `k/3 mod8` and the second by `k/8 mod3`. The CRT therefore pins one `k mod24`. The cohomology reviewer independently substituted both residue polynomials and checked the absence of an abelian conjugacy stabilizer.
- For the original A.44 family, the fresh positive-A support test reduces to the sequence `n_j(gamma_j − q_j alpha_j u_j)/(q_j²−1)`; the fresh positive-B support test reduces to `n_j(gamma'_j + beta_j v_j)/(r_j²−1)`. Here the primitives and Frobenius coordinates come from the single pinned class-two section. All the other normalized-residue terms are integral and tend to zero, including the genuine action correction `−n_j/24` on B support.
- Coordinatewise integrality of the two sequences is the fresh-support local test; their convergence to zero, together with the old-place integrality conditions, is the full continuous class-three test. Finite local vanishing alone does not supply that convergence.

The new finite checks were actually run: the map `k -> (k/3 mod8, k/8 mod3)` was enumerated on all 24 values and proved bijective; the exact two-place residue identities and both fresh-support normal forms were verified symbolically. They are appended to `code/ghost_audit_checks.py` and its regenerated output.

### Why this still does not solve the recursive survival problem

At a fixed support prime q, only coefficient primes dividing q²−1 can support a nonzero local third obstruction. Nevertheless the global class-two reduction in each of those coefficient primes can depend on later prime choices, until the factorial tail is divisible by the necessary coefficient power. One cannot impose only the local unit equation at q and conclude that the corresponding global central Frobenius mismatch is zero.

A concrete finite gate arises already for coefficient five after the first original prime pair q0,r0. The abelian mod-five pair is then frozen as `(3 q0^24, −2 r0^24)`, because all subsequent exponents are divisible by five. Later ordinary support inertia is zero in the central mod-five coordinate, but stage-one root choices can still change the integral local primitives at q0,r0 and thus their prescribed central inertia reductions. To continue a putative all-zero construction one must prove simultaneous solvability of the two local class-three conditions in this finite global central-primitive problem, then do the same for all powers and all later support primes while ensuring the zero-limit condition. Neither the CRT/Chebotarev arithmetic recursion nor the dense-failure proof supplies this survival-extension lemma. No assertion of its truth or falsity has been established here.

### Additional constructive route examined

Choosing old coefficient-prime input roots on shells with `v_ell(q_j−1)=v_ell(n_{j+1})` can reduce the denominators in B.102. For an odd ell already dividing n_j and not dividing j+5, this makes the valuation of q_j²−1 equal that of n_j. It therefore removes a simple divisibility obstruction, but the quotient need not tend to zero: its scalar factor then has valuation zero. One would still need successively stronger central Frobenius congruences. For a *fixed* already frozen finite class-two field, identity Frobenius is compatible with the same type of radical/cyclotomic fibre-product argument used in the dense-failure construction (which instead prescribes nonzero central Frobenius). This observation alone is insufficient, because at the first stage involving a new coefficient prime the earlier abelian data are changing and that class-two field is not yet fixed.

The literature reviewer checked Wickelgren's Theorem 19 and Remark 20(ii) in the author version of *On 3-nilpotent obstructions*: the two components require compatible defining systems. Separate triple-Massey vanishing does not prove the needed simultaneous lift. No minimally ramified global approximation theorem resolving the finite gate was identified. This is an explored route, not a nonexistence proof for such a theorem.
