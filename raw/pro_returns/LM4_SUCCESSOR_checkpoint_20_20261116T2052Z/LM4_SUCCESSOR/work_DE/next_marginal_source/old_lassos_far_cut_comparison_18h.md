# Based old-lasso conversion for the constant-v stabilizer path

The six old generators are the stored positive lassos about
0,1,zeta,zeta^2,zeta^3,zeta^4, based at q=1/100. We use the projection
ROT=1+(371/1000)i and downward cuts in that projected plane. The far
basepoint is q_far=10/ROT. The specified far-to-old whisker has projected
vertices (10,0),(10,2),(1/100,2),(1/100,371/100000). Its cut word is empty.
The far-cut physical order is zeta^2,zeta^3,zeta,0,zeta^4,1.

Reading the literal stored polygons gives the exact basis map

    b0 -> x4, b1 -> x6, bzeta -> x3,
    bzeta2 -> x3^-1 x1 x3,
    bzeta3 -> x3^-1 x2 x3, bzeta4 -> x5.

Both six-generator substitutions are inverse, checked in both directions.
Every old square is counterclockwise and its abelian image is the positive
physical meridian. Consequently the far word [x5,x6] is literally
[bzeta4,b1], one-based signed array [6,2,-6,-2]. This is the inverse-order
commutator relative to [b1,bzeta4]; the two define the same local normal
relation, but the exact words have not been silently identified.

All segment/cut events and positive path-to-center distances are exact
rational calculations. The certificate bounds the minimum squared distance
by more than10^-8 and the minimum cut-coordinate gap by more than1/100.
The true cyclotomic root comparison is inherited from the independently
verified 30-digit root enclosure; replacing the stored zeta^4 by the square
of the stored zeta^2 changes it by less than10^-28. The latter inequality
is checked directly. Hence the deformation preserves the same cuts, paths
and words, including the starting marking for the constant-v path.

Producer: convert_old_lassos_far_cut.py. Genuine stdout/stderr and complete
JSON certificate old_lassos_far_cut_conversion.json are retained. This
comparison establishes only the based marking. The collision-free moving-v
path and its transported local node are a separate CE certificate; no
geometric stabilizer conclusion is inferred from this basis calculation
alone.

## Literal B87 base versus the nodal base

The literal B87 point has q*=399/40000, while the stored old polygons are
based at1/100. We use exactly the first segment of the corrected certificate
`work_CE/next_symmetric_nodes/symmetric_source_bridge_pullback_corrected.json`.
It follows the real interval[399/40000,1/100] on the branch
v=1+sqrt(1-q), w=1-sqrt(1-q), and has empty fiber braid.
The same old-q connector has projected coordinates(q,371q/1000).
Its x coordinate is positive, its height is positive, and every other
positive puncture-cut abscissa exceeds1/100. Hence its old-q cut word is
also empty. Conjugating a nodal lasso through this specified connector
therefore gives its B87-based loop with the identical signed old word
under the certified marking. This is an explicit based transport, not an
identification of the two points. The read-only audit was completed before
checkpoint18; this paragraph and its exact JSON check were written after
the writer release.
