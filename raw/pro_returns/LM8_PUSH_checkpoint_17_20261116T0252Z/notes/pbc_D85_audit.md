# Independent PBC audit of D.85

Status: full written-proof audit PASS; exact certificate rerun retained separately.
The audited draft is `de_sha_global_independence_draft.tex`, SHA256
`ca6b07defabbdd62f8f870f7559738aa3fbab60bb75227698ca9bfda3985d8ec`.

I read all 443 lines and checked the following new gates against the already
audited D.77, D.78, D.80--D.84 statements and their actual action conventions.

1. Global residual rank two leaves precisely the away-lattice cases already
   covered by D.82/D.84 or the finite-index lattice
   `L = Z_5 u + 5^h Z_5 r`, with `(u,r)` an integral basis and `h >= 1`.
   Subtraction of the first coordinate proves this exact lattice statement;
   division by the fixed `5^h` preserves the required `c_0` convergence.
2. The same uniformly convergent gauge gives both actual graph-complement
   operator images. Translation coinduction identifies their restriction map
   with the natural inclusion of Cartier dual coefficient modules, so the
   connecting invariant quotient computes the whole image-level kernel.
3. The integral ideal calculation
   `(x,g_h)/y(x,g_h) = x Z_5[[x]] direct-sum Z_5 g_h`
   is exact, including uniqueness: evaluate at `y=0`, cancel `y`, and then
   cancel the nonzero series `S_h=g_h/y` in the power-series domain.
   The relation maps to `f_lambda(x)+nu g_h` for all integral five-adic
   exponents; negative/infinite exponents introduce no denominator.
4. Both `x` and `y` annihilate the extra generator. Substitution contributes
   `chi`, and the actual Alexander multiplier contributes `chi^2`.
   Thus its compact character is exactly `chi^3`, and its Cartier-untwisted
   character is exactly `chi^2`. The actual `chi=2` operator difference is
   a five-adic unit, so this entire cyclic compact quotient has zero
   coinvariants, even if it is finite or zero.
5. Quotienting by that generator yields precisely D.84's actual rank-one
   connecting ideal. Right exactness of compact coinvariants applies because
   the image of a compact module is closed; no rational-rank replacement is
   used.
6. The boundary-depth minimum is unchanged by `5^h nu r`, including exact
   cancellation and infinite depths. At finite equal corank, the already
   established injection of divisible groups dualizes to a surjection of
   equal-rank free compact modules and hence is an isomorphism. At the
   simultaneous infinite endpoint, the proof instead identifies the actual
   restriction map with `I^2 -> I`; its quotient has nontrivial tame
   character and therefore zero coinvariants. This addresses the natural-map
   issue, rather than comparing infinite coranks.
7. In the finite-index global quotient `Z_5[[y]]/(g_h)`, the actual element
   with `chi=1,k_5=1,c_3=0` acts minus identity by `y` times a unit. Its fixed
   Cartier functionals are exactly constants. A primitive cubic element of
   `N_1` fixes constants, proving the global cubic class is not a coboundary.
   This remains valid although `y` is a zero divisor in the finite quotient.
8. The local cubic primitive uses only the stated local residual vectors.
   The finite-exception enlargement from D.80 puts every local primitive in
   one finite coefficient module; infinite ramification does not create an
   unbounded family of exceptions in that fixed module.
9. The explicit point is correct: `-799=-17*47`, `1-(-799)=800=2^5*5^2`;
   the pro-five sign vanishes, the away lattice has index five, the local
   unit depth is one, and the valuation direction is an exact boundary.
   D.74 applies to this actual finitely ramified point, without asserting
   existence for all abstract pairs.

No new mathematical gap or scope overclaim was found. The proof continues
to leave globally dependent residual pairs and arbitrary infinite-ramification
first-cohomology ranks open. No canonical source or author output was modified
by this audit.
