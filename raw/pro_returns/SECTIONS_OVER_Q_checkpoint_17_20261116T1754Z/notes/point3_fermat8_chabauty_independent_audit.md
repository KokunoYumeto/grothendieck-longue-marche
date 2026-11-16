# Independent complete audit of A189

Auditor: local_preprint. Completed 2026-11-16, 15:29 UTC.

Source: `sections/point3_fermat8_dyadic_chabauty.tex`.
Result: **PASS**. The author's four literal-plus editorial corrections
were saved before this clearance; no mathematical correction was needed.

## Divisors, branches, and convergence

The initial tangent pair represents twice the specified rational divisor.
Both subsequent doubling steps are justified by the literal divisor of
`y-L`; the monic normalization and negation of the new points have the
correct signs. I independently executed the final certificate and checked
its exact polynomial identities, rational valuations, and all reported
finite series tests.

The smooth integral curve chart is justified by the unit x derivative,
not by an invertible derivative in y. The generic Abel--Jacobi morphism
therefore extends to the Neron model. This remains true after the actual
quadratic local base extension. The two symmetric endpoints are
`P_plus` and the hyperelliptic negative of `P_minus`; their difference
in y is twice `V(c)`, of valuation three, so they have the same smooth
reduction. The constructed square root in `1+8 Z2` makes the two endpoint
branches agree modulo four with their prescribed y coordinates. Their
negatives differ by a quantity of valuation one, which proves the branch
identification.

The coefficient bound `v2(b_n) >= 1-2n` follows for every coefficient
from the central binomial formula and integrality of the inner
polynomial. With `v2(d)=6`, it gives convergent symmetric integrals,
`S=1 mod4`, `N=0 mod16`, and nonzero first logarithm coordinate.
The asserted slope is consequently `1 mod4`. At a point with
`x=3+h`, `v2(h)>=3`, the two denominator bounds in the ordinary-disc
integrals give a unit first sum and a second sum of valuation minus one.
Thus the first logarithm coordinate is nonzero for `h!=0`, and the
slope is `3 mod4`. These are all-coefficient estimates; finite
truncations are only a reproducible arithmetic cross-check.

The local logarithm factors through the two-primary completion via a
torsion-free open formal subgroup and its finite quotient. The exact
global completed generators from A186 therefore suffice for the slope
comparison. The rational order-two class remains nonzero in the local
completion because its arbitrarily deep divisibility would produce
unbounded two-primary torsion in a group with a torsion-free open
subgroup. This also proves the claimed uniqueness of the two global
completed classes.

## Curve and arithmetic fundamental-group maps

The displayed Fermat-to-genus-two map satisfies the equation literally.
The valuation minimum argument forces both Fermat coordinates to be
units over Q2; the three boundary fibres have no Q2 point. The image
therefore has `x=3 mod8`. The established local intersection forces
`u/v=+1` or `-1`, and then `v^8=1`; Q2 has no fourth root of unity
because minus one is not a square, so the four listed points exhaust
the local Selmer-compatible locus and hence the rational points.

For the section assertion, equality of the finite Kummer classes gives
the actual fixed sheet after lifting a finite geometric conjugator.
The inclusion `Pi'' subset closure[H,H]` gives the displayed arithmetic
cover quotient. Compactification and the literal curve map provide its
homomorphism to the genus-two Tate module. The ordinary fixed-sheet
and cusp inertia-orbit comparisons yield the actual proper local
centres, including real components. At two there is no boundary point,
so the lifted centre is ordinary and the dyadic calculation applies.
The conclusion remains precisely the dyadic centre three and the
specified compact two-adic coefficient image.

## Primary sources independently reopened

- McCallum--Poonen, *The method of Chabauty and Coleman*, author PDF
  <https://math.mit.edu/~poonen/papers/chabauty.pdf>, Section 4.1 and
  Remark 4.1, author page 4: the abelian logarithm is computed by the
  formal antiderivative on the kernel of reduction to the Neron special
  fibre, including bad reduction. Opened reference `turn759view0`.
- Poonen, *Rational points on varieties*,
  <https://math.mit.edu/~poonen/papers/Qpoints.pdf>, Theorem 5.7.25 and
  Proposition 5.7.26, printed page 143: existence of the Neron model and
  extension of the generic map from the actual smooth integral chart.
  Opened references `turn759view1`, `turn760view0`, `turn760view1`.

## Independent execution

`python work/code/point3_genus2_chabauty_certificate.py`

PASS: both exact divisor doublings; centre 249 modulo 256; valuations
`(0,6,0,2,-3)`; square-root ratio difference valuation four; fourteen
reciprocal-square-root coefficients; all 128 ordinary-disc truncation
tests; and the exact eighth-power residue map to the genus-two disc.
