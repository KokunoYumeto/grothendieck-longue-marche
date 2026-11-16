# A185: source and exact-computation audit

The complete draft is `sections/point3_fermat8_prym_ranks.tex`.
It is deliberately outside the active parent input pending the root audit.

## Opened primary sources

- James S. Milne, *Abelian Varieties*, version 2.00, 16 March 2008,
  <https://jmilne.org/math/CourseNotes/AV.pdf>, I, Theorem 16.7,
  printed page 69: finite generation over a number field. The existing
  verified bibliography key is `LegMilneAV2008`. A185 uses this only
  after explicitly computing the two connecting-image orders and
  their index relation.
- James S. Milne, *Algebraic Number Theory*, version 3.08,
  19 July 2020, <https://www.jmilne.org/math/CourseNotes/ANT.pdf>,
  Theorem 4.3, printed page 70: every ideal class has an integral
  representative of norm at most
  `n!/n^n * (4/pi)^s * sqrt(abs(discriminant))`.
  For Q(sqrt(-6)) this is `(2/pi)*sqrt(24)<4`. The source was
  independently reopened during this rank calculation. The existing
  key is `AgentMilneANT`; its parent verification note should add
  this exact theorem pointer when A185 is integrated.

The source gives explicit formulas for the elliptic quotients, their
conjugates and Weil-restriction map, both isogenies, each connecting
cocycle, and every global point generating a connecting image. The
two norm-Euclidean class-group computations and all three unit bases
are proved in the source. No external rank value is used.

## Retained executable arithmetic

- `code/point3_fermat8_prym_rank_certificate.py`
- `code/point3_fermat8_prym_rank_certificate_output.txt`
- `code/point3_fermat8_prym_rank_certificate_data.json`
- the rerun companion `code/point3_fermat8_elliptic_rank_certificate.py`
  and its output/data.

The new certificate verifies the literal degree-two quotient equation,
the reciprocal involution, inverse field equations, differential, and
nonzero conjugate determinant. It verifies all three quadratic-field
scalings and source-point images. The imaginary-field residue filters
and real-quadratic candidate classes are exhaustive finite checks.
Every surviving class is attained by a displayed global point or
the kernel point. The complete real-quadratic residue enumeration
modulo `(sqrt(2))^13` is retained as an independent supplementary
check; the proof already excludes all other classes using real signs
and the prime three. No finite local solubility test is promoted to
a global point-existence assertion.

The exact image-order pairs are `(4,2)`, `(4,4)`, `(4,4)`.
The index formula gives Prym ranks `1,2,2`. The old rational elliptic
image-order pairs are all `(4,2)`, giving ranks `1,1,1`.
Thus these six factors contribute exactly eight, and A182 gives
`rank J8 = 8 + sum rank J(G_A,B) >= 14`.

No upper bound for the six genus-two ranks or the total Jacobian rank
has been established. No external computation was submitted for A185.
