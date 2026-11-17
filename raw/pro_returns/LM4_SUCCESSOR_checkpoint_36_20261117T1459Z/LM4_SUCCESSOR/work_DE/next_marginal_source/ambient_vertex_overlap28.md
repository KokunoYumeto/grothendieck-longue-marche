# Actual two-vertex markings and a trivial vertex overlap

Research, checkpoint28. All groups in this note are the actual **unfilled**
ones. The frozen B134 quotient still imposes BOTH cross sheets and all ten
initial target relators. This note proves ordinary vertex intersections;
it does not identify the full intersection of the two edge-image groups,
and does not assert a corresponding compact branching result.

## 1. Put both edge-image groups on the standard ambient edge

Use the actual amalgam `V=R^0 *_K p(R^0)`, where p restricts to the based
involution eta on K. Put `E1=C<K,k>C`, `a1=CaC`,

    w0=a a1^-1,  v0=p(w0),
    s'=w0^-1 p(k) w0,   s=v0^-1 k v0.

The two actual unfilled edge groups are

    Hi=<E1,s'>,          Hj=theta(Hi)=<p(E1),s>.

Since a1 belongs to E1,

    Hi=<E1,a^-1 p(k)a>.

Applying theta, and using theta(a)=eta(a), gives the equally literal

    Hj=<p(E1),eta(a)^-1 k eta(a)>.

Thus no new whisker or inner automorphism is discarded. Let

    Bi=<f,a^-1 p(k)a> <= p(R^0),
    Bj=<eta(f),eta(a)^-1 k eta(a)> <= R^0.

The already proved all-power branch calculation identifies Bi as the
free group on its two displayed generators and gives `Bi intersect K=<f>`.
The symmetric statements hold for Bj, with edge `<eta(f)>`. The ordinary
subamalgam normal form therefore gives

    Hi=E1 *_<f> Bi,
    Hj=Bj *_<eta(f)> p(E1),                                      (1)

with each expression embedded in the actual V. In particular

    Hi intersect R^0=E1,       Hi intersect p(R^0)=Bi,
    Hj intersect R^0=Bj,       Hj intersect p(R^0)=p(E1),          (2)
    Hi intersect K=<f>,       Hj intersect K=<eta(f)>.

These are the vertex and edge stabilizers at the standard ambient edge,
not a conclusion about all conjugate vertex stabilizers of Hi intersect Hj.

## 2. Reduce the requested left-vertex overlap to the exact B117 tree

Let `L=<K,k>`. B117 gives the full actual graph model
`R^0=A(Omega) semidirect H`, with the two color classes Omega0,Omega1,

    L=A(Omega0) semidirect H,
    E1=A(Omega1) semidirect H,
    H=<h,k | [h^2,k]=1>,       f=h k^-1.

Indeed conjugation by C exchanges the colors and preserves H, so the
second equality is the literal C-conjugate of the first. The color-zero
retraction fixes L and sends E1 onto H. Consequently

    E1 intersect L=H.                                           (3)

Both generators of Bj lie in L. It is therefore enough to prove
`Bj intersect H=1` inside the proper ordinary amalgam

    L=H *_T P,
    T=<k>,       P=<k> x F(a,d,e,V4),       V4=f^-1 Bf.           (4)

No general subgroup-intersection recognition theorem is used for (3).

## 3. Exact fork words in the actual marked free basis

Put

    z=eta(a),        ell=a f a^-1,
    q=eta(ell),      U=<k,q>.

Then `z Bj z^-1=U`. From the actual five-word eta dictionary, define

    gamma=a f V4 f^-1 a^-1 f,        D=d e d^-1,
    w=gamma D f^-1 d^-1.

The literal free-word identities are

    q=w f^-1 w^-1,
    z=gamma V4^-1 f^-1 a^-1.                                   (5)

All these words use the B117 leaf basis, not an abelianized or freely
chosen marking. The three P/T cosets represented by

    1, D, V4^-1                                                (6)

are distinct, because their F(a,d,e,V4) coordinates are respectively
1, d e d^-1, and V4^-1. The exact small certificate checks (5) directly
from the full previously certified eta dictionary.

## 4. An injective subdivided Bass--Serre tree, with all powers checked

Let X be the ordinary Bass--Serre tree of (4). The element k fixes the
H-vertex aH, because a commutes with k. The element q fixes the H-vertex
wH, since q=w f^-1 w^-1. The path I from aH to wH is the reduced
amalgam path given by

    a f V4 f^-1 a^-1 f D f^-1 d^-1.

All displayed leaf blocks are nontrivial, and every f or f^-1 block is
outside T by the h-exponent character of H. This is a genuine geodesic
between distinct vertices.

The FIRST edge at aH is `a f T`, not `aT`. For every nonzero integer n,
its translate by k^n is different: equality would require

    f^-1 a^-1 k^n a f=f^-1 k^n f in T.

That never occurs. The homomorphism `H -> C2(C)*Z(k)` sending h to C
and k to k sends this word to `k C k^n C k^-1`, a reduced word outside
<k>. This verifies endpoint coset-injectivity for all nonzero powers of k,
not just that k itself moves one edge.

At wH the LAST edge is wT. Its translate by q^n can equal it only if
`f^-n in T`, which the h-exponent character excludes for every nonzero n.
This verifies the other endpoint coset-injectivity for all q-powers.

Now start with the abstract free product Z(k)*Z(q) and subdivide each
edge of its standard Bass--Serre tree into the number of edges of I.
Send its fundamental subdivided edge to I, its endpoint vertices to aH
and wH, and extend equivariantly using the homomorphism from the abstract
free product to L given by the actual words k,q. This is well-defined
because the endpoint factors fix their assigned vertices. At each
endpoint, distinct incident cosets map to distinct edges by the two
all-power verifications above. At subdivision vertices, the path I has
no backtracking. Thus the map is locally injective everywhere.

A locally injective map between simplicial trees is injective: the image
of any finite reduced path remains reduced, so distinct vertices cannot
have the same image. The abstract free-product action on its tree is
faithful, so the original group homomorphism is injective as well. Write
Y for the resulting embedded U-invariant subtree of X. At every interior
subdivision vertex its U-stabilizer is trivial, and its degree within Y
is exactly two. This construction supplies those facts directly; they
are not inferred from an abstract rank count or from the existence of
one reduced word.

## 5. The specified off-core branch has trivial stabilizer

The P-vertex gamma P is an interior subdivision vertex of the displayed
fundamental segment I. Its incoming H-neighbor is gamma H, and its
outgoing H-neighbor is gamma D H. By (5), the path from gamma P to zH
starts with the different edge leading to gamma V4^-1 H, and then follows
the reduced tail f^-1 a^-1. The three directions are distinct by (6).

Since Y has exactly its two core directions at gamma P, this third edge
is outside Y. A subtree of a tree is convex. Hence the entire reduced
path from gamma P toward zH stays outside Y after that first edge; it
cannot re-enter without making a cycle. The unique nearest point of zH
in Y is therefore gamma P.

If g in U fixes zH, it preserves the U-invariant subtree Y and must fix
that unique nearest point. The U-stabilizer of gamma P is trivial, so
g=1. Equivalently

    U intersect zHz^-1=1,
    Bj intersect H=1.                                          (7)

Combining (3) and (7) proves the requested actual left-vertex overlap:

    E1 intersect <eta(f),eta(a)^-1 k eta(a)>=1.                  (8)

Applying theta gives the exact right-vertex mate

    p(E1) intersect <f,a^-1 p(k)a>=1.                           (9)

## 6. Exact limitation and next ambient gate

Equations (2), (8) and (9) imply that Hi intersect Hj has trivial
stabilizers at the TWO STANDARD endpoint vertices of the ambient edge.
This does not determine its stabilizers at other vertices. Those involve
additional double cosets between Hi and Hj and intersections of shifted
vertex groups. Nor does it determine cycles in the Bass--Serre fiber
product. In particular no conclusion `Hi intersect Hj=1`, no global free
intersection claim, and no proper embedding of Dloc into V_* is made.

The proof is ordinary. Its tree immersion and nearest-point argument are
not asserted for profinite branching or for the closures of Bj, Hi, Hj.
The full compact topology statements already proved for other specified
subgroups remain unchanged. All actual relator families rho and theta(rho)
are still imposed when passing to V_*; no one-sheet reduction is reused.

Exact finite input: `check_ambient_vertex_fork28.py/.out/.err` and
`ambient_vertex_fork28.json`. The output checks the literal fork against
the complete actual eta dictionary. Sections4–5 prove the all-power tree
statement; the finite check is not a substitute for that argument.
