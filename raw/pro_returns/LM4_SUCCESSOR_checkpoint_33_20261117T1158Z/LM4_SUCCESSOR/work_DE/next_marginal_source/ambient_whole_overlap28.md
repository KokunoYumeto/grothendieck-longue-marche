# The whole ordinary intersection of the actual unfilled edge groups

Research, checkpoint28. This is a separate upgrade of the unchanged
`ambient_vertex_overlap28.md`. The additional argument was proposed by
root and independently checked here. It proves an ordinary global
intersection by comparing **directions**, not by assuming the two
standard vertex stabilizers determine all shifted intersections.

Use exactly the actual groups and markings of that note:

    V=R^0 *_K p(R^0),
    Hi=E1 *_<f> Bi,       Hj=Bj *_<eta(f)> p(E1),
    Bi=<f,a^-1 p(k)a>,    Bj=<eta(f),eta(a)^-1 k eta(a)>.

The prior proof gives E1 intersect Bj=1 and its theta mate. We now prove

    Hi intersect Hj=1.                                          (1)

There is no completed or post-N_* assertion in (1).

## 1. The actual retraction controls shared directions

The complete B117 retraction r:L->K, with L=<K,k>, fixes K and kills k.
It satisfies

    r(H)=<f> subset H,
    r(Bj)=<eta(f)> subset Bj,
    H=E1 intersect L.

Take b in Bj intersect E1 K. Write b=e k0, with e in E1 and k0 in K.
Since b and k0 both lie in L, e=b k0^-1 belongs to E1 intersect L=H.
Write it as h. Then

    b r(b)^-1 = h k0 (r(h)k0)^-1 = h r(h)^-1.

The right side belongs to H because r(H) is contained in H. The left
side belongs to Bj because r(Bj) is contained in Bj. The prior exact
intersection Bj intersect H=1 forces b=r(b). Thus b belongs to K.
The converse inclusion is immediate, so

    Bj intersect E1 K = Bj intersect K = <eta(f)>.                (2)

Equivalently, among the left cosets of K in R^0, the sets

    {eK:e in E1},       {bK:b in Bj}

have exactly one common member, the coset K itself. If eK=bK, then
b belongs to E1K, so (2) makes bK=K. Applying the actual theta, which
preserves K through eta, gives the same assertion at the right vertex
for the coset sets of Bi and p(E1).

This is stronger than merely knowing E1 intersect Bj=1. It is the
additional control required for the global argument.

## 2. The two actual invariant subtrees meet in exactly one edge

Let T be the ordinary Bass--Serre tree of V, and let e be its standard
edge K, with endpoint vertices R^0 and p(R^0). Map the standard tree of
the embedded subamalgam Hi into T using its actual two vertex maps.
At its left vertex, the map of incident edge cosets is injective because
E1 intersect K=<f>; at its right vertex it is injective because
Bi intersect K=<f>. The map is therefore locally injective. A locally
injective tree map is globally injective, since a finite reduced path
cannot map to a path with a cancellation. Its image Ti is an embedded
Hi-invariant subtree containing e.

The same construction gives an embedded Hj-invariant subtree Tj, using
Bj intersect K=<eta(f)> and p(E1) intersect K=<eta(f)>.
The edges of Ti incident to the standard left endpoint are exactly eK
for e in E1, while those of Tj are bK for b in Bj. By (2), the only
common such edge is the original edge K. At the right endpoint the
same holds by theta.

The intersection of two subtrees of a tree, when nonempty, is a subtree:
the unique path between two common vertices belongs to both. Here Ti
and Tj both contain e. If their intersection had any further vertex or
edge, the unique path from it to e would leave e through one of its
endpoints along a common departing edge. The preceding coset argument
excludes both possibilities. Hence

    Ti intersect Tj = e, including its two endpoints.             (3)

No unexamined fiber-product cycle or shifted double coset is omitted:
(3) follows from connectedness of the actual embedded subtrees and the
complete incident-direction comparison at the two endpoints.

## 3. Global intersection and exact scope

Any g in Hi intersect Hj preserves both Ti and Tj, and hence preserves
the edge (3). The ambient amalgam action has no edge inversions, so g
fixes both endpoints. At the left endpoint this puts g in E1 intersect
Bj, which is trivial. This proves (1).

The proof uses ordinary simplicial trees, their unique finite geodesics,
and the ordinary retraction/normal-form results already established.
It does not claim an analogous intersection for completed closures,
where the vertex-intersection and direction arguments would require
independent compact proofs. It also does not show that the two local
normal-closure fillings interact trivially, that the subgroup generated
by Hi and Hj is their free product, that Dloc embeds in V_*, or that
ker(a_loc) is kappa-invariant. Intersections of conjugates and relations
in the generated overgroup still matter for those filling questions.

The entire actual two-sheet quotient of B134 remains unchanged. No new
producer or finite/double-coset census is needed for this upgrade; its
finite literal inputs and all-power vertex-tree proof are exactly those
retained with `ambient_vertex_overlap28.md`.
