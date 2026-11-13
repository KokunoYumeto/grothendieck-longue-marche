# Controlled filling inside the original planar domain

## Proved lemma

Let O be an open subset of the plane, D an open Euclidean disk, and U a connected component of O∩D. For every basepoint in U, the actual inclusion

\[
U\hookrightarrow O
\]

induces an injective homomorphism on fundamental groups. Consequently every loop in U which is null-homotopic in O has a based disk filling entirely inside U, and thus entirely inside the prescribed ambient disk D.

## Proof with the actual intermediate maps

Let γ be a based loop in U which is null-homotopic in O. Its compact image has an open neighborhood in U. A sufficiently fine polygonal approximation γ' and the straight homotopy on each small parameter interval remain in that neighborhood, fixing the basepoint. Choose the finitely many vertices generically if necessary, so that the polygonal image is a finite planar graph.

Take a sufficiently small compact connected planar regular neighborhood N of this graph inside U. It can be constructed as a finite union of small vertex disks and thin edge rectangles, followed by rounding corners. Its boundary consists of one outer Jordan curve and finitely many inner Jordan curves. Its bounded complementary components D_i are the open Jordan disks enclosed by the inner curves.

The closed outer Jordan disk containing N is contained in D. Indeed, the outer boundary is a compact subset of the convex disk D, and its entire bounded interior lies in the convex hull of that boundary: any point outside the convex hull is separated from it by a line and can be joined to infinity without meeting the boundary. The convex hull of a compact subset of the open Euclidean disk stays in that disk. In particular every inner disk D_i lies in D.

Fill into N precisely those D_i which are entirely contained in O, and call the resulting compact planar surface N'. Since each of their boundaries already belongs to N, this means adjoining the complete closed inner disk. Thus

\[
\gamma'\subset N\subset N'\subset O\cap D.
\]

The set N' is connected and meets U, so it is contained in the same component U. For every inner disk still unfilled, choose one point p_i∈D_i\O. These points are distinct and lie in the interiors of the remaining complementary disks.

The actual inclusion

\[
N'\hookrightarrow\mathbb R^2\setminus\{p_i\}
\]

is a homotopy equivalence, as can be seen by an explicit strong deformation retraction. For each remaining closed inner Jordan disk, choose a Schoenflies disk coordinate carrying p_i to the origin and its boundary to the unit circle. In the punctured disk use the radial homotopy

\[
(r,\theta)\longmapsto((1-t)r+t,\theta),\qquad 0<r\le1.
\]

For the exterior of the outer Jordan disk, use its Schoenflies exterior coordinate and the same formula for r≥1. All these homotopies fix their boundary circles pointwise. Together with the identity on N', they paste on the finite closed cover of the punctured plane to a strong deformation retraction onto N'. Every basepoint in N' remains fixed.

The null-homotopy of γ' in O is also a null-homotopy in the punctured plane, because every chosen p_i lies outside O. Applying the displayed deformation retraction gives a based disk filling of γ' in N'. Prepending the based polygonal approximation homotopy gives a filling of γ in U. This proves the asserted injectivity and the controlled filling statement.

## Exact scope for the frontier problem

The filled hull of a loop's image need not itself lie in O: a circle followed by its reverse in an annulus is already a null loop whose image surrounds an excluded point. The lemma above avoids that assertion. It produces a filling in the actual O and in any chosen open Euclidean disk containing the loop within one component of O∩D.

When original evaluation loops shrink uniformly to a fixed frontier point, choose disks with radii tending to zero that contain those loops. Their original ambient-null restrictions are null in O by C32, and each connected loop lies in one component of the intersection. The lemma therefore supplies disk fillings with the same vanishing ambient diameter. It does not provide a continuous selection of the fillings, a simultaneous configuration or edge isotopy, or an equivariant fragmentation of an arbitrary original loop.
