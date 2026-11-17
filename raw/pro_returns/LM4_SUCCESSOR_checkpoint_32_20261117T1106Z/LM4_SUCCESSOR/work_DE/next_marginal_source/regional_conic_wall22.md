# Actual regional conic geometry and the antipodal wall

Research, checkpoint22. No regional group product or global centralizer
conclusion is inferred here. The actual based relation producer is owned
by CE; this note records the structural geometry used to assess it.

## 1. Two exact forms of the inner bad piece

In B.106's quotient, the inner bad fiber is `|t|>1`. Put `h=1/t`.
Its ordinary open domain is

    0<|q|<1, |h|<1,
    h^2 != q, h != h_u(q), -h_u(q)  (u in mu5\{1}),

where

    h_u(q)=(u^2+(1-2u)q)/(q+u^2-2u).

The involution is `h -> -h`. In its orbifold quotient `y=h^2`,
the cone divisor is `y=0`, with order two, and the five removed
graphs are `y=q` and `y=h_u(q)^2`. The branch graph `y=q` is
disjoint from the four other graphs in the open bidisk. It remains
removed. The old vertical divisor q=0 remains removed as well.

There are six ordinary pair nodes among the four squared graphs,
and four double contacts of those graphs with the cone divisor.
The pair (1,4) and pair (2,3) have the same critical q value but
two distinct ordinary nodes. The generic orbifold fiber is
`C2*F5`; the four cone contacts give local relations
`[p,c p c^-1]=1` after imposing `c^2=1`, in their actual common
whiskers. No filling relation is imposed for the retained q0 lasso.

In the half-plane form put

    Q=(1+q)/(1-q), Z=(t+1)/(t-1),
    c_j=cot(pi*j/5), lambda_j=2/(1+c_j^2).

Then `Re Q>0, Re Z>0`, and the removed graphs are

    A_j=lambda_j(Q-i c_j), B_j=1/A_j,
    Z^2-2QZ+1=0.

The conic roots are interchanged by F. The projective old points
Z=0 and infinity are on the boundary of this region, not extra
interior fiber punctures.

## 2. The tangent-line and ellipse interpretation

For a continuous boundary parameter u=exp(i theta),

    A_theta=(1-cos theta) Q - i sin theta.

At fixed `Re Q>0` this is a nondegenerate ellipse centered at Q,
tangent to the imaginary boundary at zero. Writing

    A_theta=Q-(Q+1)e^(i theta)/2-(Q-1)e^(-i theta)/2

shows that its two foci are `Q ± sqrt(Q^2-1)`, exactly the retained
conic roots. The B curve is the image of this ellipse under Z to1/Z.
This geometric description does not supply a simultaneous based
straightening of the two puncture families relative to the conic.

The A_j line is tangent to the conic at

    Z=-i/c_j, Q=i(c_j-c_j^-1)/2,

on the imaginary boundary. This also follows from
`lambda_j(2-lambda_j)=sin^2(2 pi j/5)`.
In the original unordered-root coordinates

    s=v+w, q=vw,
    Z=(1+q-s)/(1-q),

the conic is the diagonal v=w and the A lines are exactly v=u or
w=u in the symmetric square. The actual half-plane restrictions
and reciprocal B family remain present. A configuration-space
description of an unrestricted conic/tangent-line complement does
not identify this restricted regional complement automatically.

## 3. The exact wall which a clustered deformation crosses

For unit parameters u=exp(2ia), r=exp(2ib), with a,b in(0,pi),
the actual mixed roots are

    alpha=u+r-ur, beta=ur/(u+r-1)=1/conjugate(alpha),

and direct expansion gives

    |alpha|^2-1 = 8 sin(a) sin(b) cos(a-b).

The inner branch changes from alpha to beta precisely when u and r
become antipodal. In the fifth-root ordering the only off-diagonal
pair whose interval avoiding the excluded point1 has length greater
than pi is (1,4). Therefore clustering all four parameters into one
such open semicircle must cross this wall. It is not an isotopy of
the inner regional divisor arrangement.

In the c parameters the wall is `c_i c_j=-1`. The two collision
values

    Q=±|1+c_i c_j|/2 + i(c_i+c_j)/2

coalesce on the base boundary. At the same point the node meets
the retained conic root `Z=-i/c_i`; its F mate meets `Z=i c_i`.
Indeed both A_i and B_j have the same tangent as the conic there.
Thus this is an actual retained-branch threading event, not an
ordinary interior motion of one node. A proposed relative deformation
must account for its based vanishing paths and the branch meridian.

There is a second boundary condition for any long parameter
deformation: a mixed node may hit the omitted vertical q=0.
The equation alpha=0 is equivalent to `u^-1+r^-1=1`, and for unit
parameters its only unordered solution is
`{u,r}={exp(i pi/3),exp(-i pi/3)}`. A chosen deformation must avoid
this event as well. It does not occur at the actual fifth roots.

## 4. What the exact presentation currently shows

The actual six-strand producer retains the distinguished cone,
the branch, all nine filled critical values, and q0 separately.
Its literal normalization gives four standard cone contacts and
six other complete words. Independent DE replay checks all ten
based actions/transports, all inverse substitutions, the triangular
basis change, and all complete relation words.

In that specified normalized marking, the candidate target

    (F(A1,...,A4) times F(B1,...,B4)) * F(P,Q)

kills seven of the ten words. The remaining three, beta13, the23
node at the shared14/23 critical value, and beta24, have nonempty
exact free-product normal forms involving retained branch letters.
This is a failure of the proposed map in that marking. It does not
prove that no alternative basis or abstract product/HNN description
exists. The exact normalized words, rather than their abelianized
incidences, are the current structural input.

No relative Oka–Sakamoto theorem, general arrangement asphericity,
or unverified conic-complement theorem has been applied.
