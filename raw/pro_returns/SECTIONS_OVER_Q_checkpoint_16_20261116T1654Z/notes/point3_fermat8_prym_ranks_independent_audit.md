# Independent saved-source audit of A185

Auditor: local_preprint.  Date: 16 November 2026.

Source: `sections/point3_fermat8_prym_ranks.tex`.
Executed certificate: `code/point3_fermat8_prym_rank_certificate.py`, including
its rerun of the rational elliptic companion. All assertions passed.

## Actual maps

Checked both reciprocal involutions, their product iota, the displayed
inverse function-field quadratic, and the literal elliptic equations.
The two differential rows have determinant -2r. Their restrictions to the
anti-iota cotangent space give the actual isogeny from the Prym to the Weil
restriction. Galois conjugation exchanges precisely the two displayed maps;
no unnamed elliptic identification is needed. All three field scalings and
images of the rational quartic points check.

## Descent and exact images

Checked phi, psi, their kernels, and the inverse square-root formula for psi.
The exceptional kernel class is b; the dual kernel class is -4b. The exact
quotient by the dual kernel supplies the factor2 in the index identity,
and E_b[2] of order2 supplies the second factor2 in the rank formula.

For Q(sqrt(-3)), the Euclidean norm calculation, six units, inert2, ramified3,
full eight-class support list, and both residue filters leave exactly the
four/two classes attained by the displayed points.

For Q(sqrt2), the norm-Euclidean calculation and least positive unit argument
supply the full unit group. The inert-three residue norm forces the epsilon
exponent to vanish. The appropriate real embedding then leaves four classes
on each curve, all attained by the displayed point and the kernel point.
No dyadic sufficiency claim is needed for this rank computation.

For Q(sqrt(-6)), the explicit Minkowski bound and principal ideals establish
class number2 and the localized principal-divisor lattice. This proves the
full squareclass list even for initial representatives with even valuations
outside the support. The ramified-three filters, exact dual point and its
squareclass, and independence tests establish both four-element images.

The rational elliptic finite primitive tests and actual point classes give
all six connecting images and hence the three rank-one results.

## Conclusion

Complete proof audit PASS. Exact Prym ranks are1,2,2, and the three rational
elliptic ranks are1 each. The already proved product isogeny therefore gives
known rank contribution8 and total Jacobian rank at least14. No upper bound
for the remaining six genus-two factors is inferred. No source correction
was requested.
