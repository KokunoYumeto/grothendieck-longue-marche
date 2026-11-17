# Independent audit of B.93 and B.94

Date: 2026-11-16. Reviewer: DE component. Status: **PASS in the stated discrete scopes**.

## B.93: full residual coefficient span

We read the complete proposed formal source `work_A/B93_proposed.tex`. The
independent replay `check_E_span_independent.py` reconstructs all 106 ordered
unit pivots, the ten private binomial witnesses, the twelve full kernel
vectors, and both original-domain semilinear involution matrices. The
finite-support argument for multiplication by each nonzero binomial is
valid: a nonzero finitely supported group-ring element cannot be invariant
under right translation by the certified infinite-order element.

We checked every displayed private-row/core entry against the original
certificate and checked the four displayed rho words against the actual
source half-chain records. The 116-dimensional free image has 56 exchanged
pairs and four negative fixed summands. The latter give precisely the four
actual first-sheet source values, with no inference from a peripheral
conjugacy class alone. The intrinsic induced common refinement supplies an
honest comparison with B.92; it does not identify two different relation
kernels.

The bounded integer old-zero extension was independently checked in
`check_intrinsic_old0_independent.py`: rank 116, a determinant-minus-one
minor, twelve integral anti-kernel generators, and the source typings of
the only four nonzero diagonal values. This is an ancillary bounded check,
not the proof of B.93's full coefficient assertion.

## B.94: exact retained-deck normalization

We read the complete proposed formal source `work_A/B94_proposed.tex` and
independently ran `check_G_span_independent.py`. This verifier imports no
producer. It represents each residual free generator by the literal pair
(retained F5 word, deleted peripheral slot), rather than sharing the
producer's integer-index arithmetic.

It checks:

1. All 64 original paired Fox columns and all 2680 terms normalize and
   expand back exactly under the stated G = (R x R) semidirect F5 action.
2. The actual involution on every normalized row is the stated negative
   swap with retained coefficient d_z.
3. All 64 full G-valued mate relations, coefficient cycles, inverses, and
   semilinear multiplication identities hold.
4. Every column has exactly one unit after residual augmentation; the 64
   selected rows are distinct and their physical slots exhaust the entire
   eight-by-eight product. A separate reconstruction of the selected
   augmented matrix gives the diagonal matrix of those units.
5. All eight fixed-node cocycles reduce to the recorded cone factors in
   C2 * C2 * F2. Four lie in the selected cone class and have the previously
   verified actual source half-chains. Four lie in the other cone class and
   have no fixed coefficient point.

The genuine output and review data are
`check_G_span_independent.out` and
`symmetric_G_span_independent_review.json`. The first draft of this
independent verifier incorrectly required every physical-mate orientation
delta to be +1. Its failed code/output/error are retained with the
`_initial` suffix. The correction uses the actual two branch orientation
signs; 26 nonfixed matches have delta -1. All eight fixed matches have
delta +1, as required by the theorem. This was a verifier assumption
correction, not a change to a geometric or formal result.

## Separated augmentation argument

The fixed-prime proof in B.94 is correct. A free word's maximal-block
Magnus monomial has as many successive variable runs as there are blocks;
omitting any block cannot produce that monomial. This proves residual
finite-2 separation without invoking an unproved Magnus injectivity
theorem. Finite support is separated by a finite product of the detecting
finite 2-groups. The same holds for R x R.

The augmentation ideal of F2[V] is nilpotent for a finite 2-group V by
central-order-two induction. Over (Z/2^k)[V], its Nth power lies in twice
the ring and its Nkth power is zero. Choosing k so that a nonzero integer
coefficient survives therefore proves intersection_n I_E^n = 0. This
does not assert nilpotence of the integral augmentation ideal of V.

The retained action preserves I_E, so the two-sided ideal a = I_E Z[G]
has powers direct_sum_t I_E^n d_t. No finite quotient of E invariant under
the whole retained group is needed. For a left coefficient relation,
the i-th selected row is

    a_i u_i + sum_j a_j m_ji = 0,

where u_i is a genuine signed group unit and m_ji is in a. Thus, once all
a_j lie in a^n, multiplication on the right by u_i^{-1} puts every a_i
in a^{n+1}. Separation forces the relation to be zero. This proves
injectivity; it does not invert the selected matrix or a general element
with unit augmentation.

## Fixed coefficients and no omitted generic-fiber operators

For a fixed physical node, the coefficient involution is x -> F(x)a.
Its retained projection has a fixed point exactly when beta(w)t = w.
The explicit lift x = (alpha_beta(w)(u), 1, w) satisfies the full equation,
by the cocycle identity. The retained fixed subgroup is trivial, since
the selected cone centralizer in C2 * C2 * F2 is just that cone. Therefore
the full coefficient fixed subgroup is diagonal R, fixing the side of the
four source left ideals. The four other-cone cases have no fixed basis
points and contribute only induced two-element orbits.

Before mixed node relations are imposed, the whole generic fiber is
(R_A * R_B) semidirect F5. Its mixed commutator kernel N acts trivially on
N_ab = P. Hence all generic-fiber conjugations factor through
G = (R_A x R_B) semidirect F5. There is no untracked generic-fiber operator
after this coefficient enlargement. B.91's remaining lifted node
transports are the old-base transports and their arbitrary iterates.

Neither audit establishes old-base invariance, full kappa vanishing,
source equality, nonlinear fixed lifting, nor a completed coefficient
identification.
