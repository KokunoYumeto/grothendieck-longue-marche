# A192 source and arithmetic audit

The complete source is `sections/point3_genus2_full_dyadic_locus.tex`.
The literal finite certificate is `code/point3_genus2_full_dyadic_certificate.py`,
with retained `_output.txt` and `_data.json`. It verifies both recursive series,
the exact primitive derivatives, all stated valuation inequalities in 64
positive depths and 32 coefficients, both function-field maps, their
compositions, ramification and genus. These finite checks supplement the
all-depth coefficient proofs in the source.

## Opened primary sources

Poonen, *Rational Points on Varieties* (AMS GSM186, 2017), author PDF:
https://math.mit.edu/~poonen/papers/Qpoints.pdf

* Section5.9.1, equation(5.9.1), printed147 (PDF160): over a perfect field,
  the connected algebraic group has its affine subgroup and abelian quotient,
  and its affine subgroup has its unipotent radical and torus quotient.
* Theorem5.4.8(ii), printed128 (PDF141): the actual unitriangular embedding
  of a unipotent algebraic group. Its characteristic-two powers make
  multiplication by two nilpotent in the commutative case here.
* Theorem5.7.25 and Proposition5.7.26, printed143: Neron model and the
  smooth-source mapping property, already opened and audited in A189.

The first two passages were reopened from the primary PDF on16November2026.
The existing verified bibliography key is `LegPoonenRationalPoints`.
The logarithm comparison from A189 is McCallum--Poonen, *The method of
Chabauty and Coleman*, Section4.1 and Remark4.1, author PDF p4,
https://math.mit.edu/~poonen/papers/chabauty.pdf .

## New comparison proved in the source

The smooth model Y^2=8X^5-27X has special fibre A1_Y. Its Abel--Jacobi map
relative to(0,0) factors on the special fibre through a connected unipotent
subgroup of dimension at most two. The successive reduced connected images
of[2] lower dimension until zero, proving the literal morphism[4]a_s=0.
The restricted parametrization X=-Y^2 A(8Y^8/27^5)/27 therefore puts the
formal coordinates of[4]a in2 Z2<Y>. The radial total-degree denominator
bound proves uniform formal-log convergence. Equality of derivatives and
the value at zero identifies the actual logarithm on the entire closed
disc, including the unit-Y residue class. The infinity chart is already
a single smooth formal residue disc; its first annulus is included.

No equality of an antiderivative and the abelian logarithm is inferred
solely from convergence of an inverse coordinate series. The section
conclusion retains the actual cyclic-eight fixed sheet and the full
metabelian locally point/cusp-matching domain.
