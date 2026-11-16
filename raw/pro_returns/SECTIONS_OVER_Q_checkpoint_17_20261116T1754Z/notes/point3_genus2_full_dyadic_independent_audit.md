# Independent complete audit of A192

Auditor: local_preprint, 2026-11-16 15:42 UTC.

The complete saved source
`sections/point3_genus2_full_dyadic_locus.tex` passes mathematically.

The positive-valuation chart is smooth by its X derivative and has
special fibre A1 with its literal Y coordinate. The extended
Abel--Jacobi map starts at zero. Its abelian quotient map is constant:
properness extends it to P1, and removal of a finite inseparable
Frobenius factor reduces a nonconstant map to one detected by an
invariant differential. Its torus quotient map is constant by the
units of the affine-line coordinate ring. The image therefore lies
in the smooth connected unipotent radical of dimension at most two.

The reduced connected images of successive [2] maps are smooth over
the perfect special field. A dimension-preserving nonzero image
would make [2] surjective on that image and contradict its nilpotence
in a unitriangular embedding. Thus [4] kills the whole radical as
a morphism. This proves that [4] of the actual Abel--Jacobi map has
zero special-fibre map, including all geometric points of the affine
line, not merely its two rational residue points.

The integral recursive inverse-coordinate series defines the full
restricted Y disc. The formal coordinates of [4]AJ then lie in
2Z2<Y>. Multiplying the invariant forms by one fixed scalar makes
their coefficients integral; radial formal integration divides
coefficients only by total degrees. Substitution into these formal
coordinates gives uniform convergence in the restricted algebra.
The derivative and value at zero identify the logarithm with four
times the explicit primitive. Division by four proves the required
comparison even when Y is a unit.

Both displayed positive-valuation primitives were differentiated
independently. Their leading valuations are k and 3k-1, and every
tail term is strictly higher. The exact infinity chart gives
omega1=t dw and omega2=t dw/w; its primitives have leading
valuations 3k+1 and k+1, including k=1. The coefficient bounds in
the source control every term. Together with A189's unit disc,
these cases exhaust all local points and give the four stated
global-coordinate/local-point pairs. The completed-generator
localization injection is the exact one already proved in A189.

The cyclic-eight equation and its two inverse maps were checked
literally. The boundary indices are 8,8,2 at zero, one, infinity;
the four points in the last fibre have no Q2 rational point.
The fixed-sheet arithmetic quotient and subsequent compact
Kummer map have exactly the asserted local point/cusp scope.

Primary sources independently reopened: Poonen, *Rational points on
varieties*, Theorem5.4.8(ii), printed page128, and Section5.9.1,
equation(5.9.1), printed page147; original author PDF
<https://math.mit.edu/~poonen/papers/Qpoints.pdf>.
Opened references: `turn769view0`, `turn769view1`.

The first certificate execution passed all series calculations and
stopped at a correct inverse-map identity because SymPy `cancel`
did not combine its nested fractions. Direct `factor` returns zero
for that exact expression. The author was notified to use
`cancel(together(...))` or `factor`; this is a finite-check
simplification correction, with no source-proof change.

After the author replaced that assertion by `cancel(together(...))`,
I independently reran the complete certificate. It passes all 64
recursive-series identities, 4224 positive-disc valuation checks,
3968 infinity-disc valuation checks, both inverse maps and boundary
indices, the complete valuation partition and the genus count.
Final proof and certificate clearance: **PASS**.
