# The literal signed common-source candidate and its G_L map

This batch was requested by the profinite agent during the binary A6
source comparison. All files have new `a_cm_signed_common` names. No
factorization through the new binary A6 source is inferred here.

## Exact candidate

Use the literal matrix group SL2(F5) and the displayed generating pair
`FerrariSL2Five().lifts[4]`. Its quotient to the old five-point A5 model
is the already proved action on the five Klein-four subgroups. Induce
this pair through the six actual B/F Schreier paths retained in
`de_a6_gl_common_quotient.py`, then adjoin the same induced ordinary
x-exponent modulo30 map. The induced matrix coordinates are all six
SL2(F5) values; no central sign is discarded.

The faithful candidate permutation model has degree900: six regular
120-point matrix actions and the180-point induced abelian map. For
right matrix translation z -> z*g, the actual map to the old five-point
action is z -> q(z)^(-1)(0). It intertwines both literal B generators
with the old Q30. The saved equivariant point map proves the quotient
map; it is not reconstructed from its order.

Complete group certificates give B order9,331,200,000, F
order1,555,200,000, and F'=F'' order1,728,000. The selected cosets
[2,0,1] correspond to the three old epikernels[4,12,18]. Their actual
SL2(F5) projections have image order120^3, equal to the whole F'
order. Thus they identify F' with SL2(F5)^3. Together with ordinary
Fab/30, the same actual projection identifies F with
SL2(F5)^3 x (Z/30)^2. This is verified by a further complete projected
group certificate.

The candidate-to-Q30 kernel has order8. It lies in the six central
matrix coordinates and has trivial abelian coordinate, hence is
central in the pure F image. The full six-sign model, including its
B permutation action, is retained.

Program: `a_cm_signed_common_candidate.py`; all six complete group
certificates have both literal-word and full-Schreier replay outputs.
Saved total runtime:0.360814s.

## The actual factorization through G_L

`a_cm_signed_common_GL.py` reconstructs the old signed source without
the legacy runpy initializer. Its actual2124-point quotient and two
source permutations are compared byte-for-byte with the frozen source.
The ordinary A5 factor maps for indices4,12,18 are already certified
through this quotient by the complete source presentations.

Above that quotient, adjoin all six actual induced SL2(F5) values.
The possible new discrepancies are the six scalar signs. They are
retained alongside all2052 ambient binary coordinates of the old
source. The generic lifted-Schreier collector evaluates every25,965
base relation, including its complete final sift, closes the lifted
discrepancies under both original generators, and independently
replays every saved literal relation word.

The resulting joint kernel has dimension44. Its projection onto the
old44-dimensional kernel is onto, as checked against every old basis
column; equality of dimensions makes that actual projection an
isomorphism. Its inverse followed by the six-sign projection gives the
saved6-by44 matrix. This proves that the induced signed candidate
factors through G_L. Adjoining Fab/30 requires no new factorization:
the same ordinary abelian quotient is already retained in G_L and in
the displayed Q30 comparison.

The six-sign map has rank5, independently rechecked by
`a_cm_signed_common_GL_rank.py`. All six input sign coordinates remain
in that map. The order-eight kernel over Q30 is the separate actual
quotient proved above. No assertion replacing all six signs by three
coordinates enters the construction.

The full factorization program/output/NPZ and the literal relation DAG
are saved under `a_cm_signed_common_GL.*`; runtime151.667217s. Every
old input hash is checked before and after. A map through the new
binary A6 source still requires its own complete comparison and is
not claimed in this batch.
