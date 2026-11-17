# Exact corner face and axes of the four actual final roots

Research, checkpoint25. The group M is the actual intermediate amalgam
of B120. The four relations (j P_i)^2, i=1,...,4, are NOT imposed.
This note proves ordinary-tree overlap statements only. It invokes no
small-cancellation, developability or final-centralizer theorem.

## 1. The additional corner face is an immediate actual retraction consequence

In W_boundary put H=<c,k,T>, P=cT=P5. The mirror-even subgroup has
the path graph-product presentation on D,k,u,k',c from B120.2.
Its actual retraction rho to H sends D,k' to1 and u toT, and fixes c,k.
The companion on H is

    nu(c)=nu(k)=1,   nu(T)=P^-1,   nu(P)=P^-1.

Therefore rho(j H j)=<P>. Since rho fixes H, every element of
H intersect j H j belongs to <P>. Conversely jPj=P^-1 gives the
reverse inclusion. Hence

    H intersect j H j=<P> inside W_boundary.

The same proof is continuous, using the already embedded full
completions. The extension of rho fixes Hhat and maps j Hhat j onto
the actual full procyclic closure of <P>. Thus

    Hhat intersect j Hhat j=closure<P> inside W_boundaryhat.

This is an actual completed intersection, not the completion of an
intersection inferred by exchange of operations.

## 2. The common two-edge turn in the ordinary amalgam tree

Let T_M be the ordinary Bass–Serre tree of M=R *_H W_boundary.
Write e for the base edge H, joining the vertices R and W_boundary.
For i=1,...,4 put

    w_i=j P_i.

Each is cyclically reduced of amalgam syllable length2, because
j is outside H and P_i is outside H. Its ordinary translation
length is2 edges. Its axis A_i contains the four consecutive edges

    P_i^-1 e,  e,  j e,  j P_i e.

Their successive vertices are P_i^-1 W, R, W, jR, jP_i W.
The element w_i moves the first two edges to the last two. Repeating
this path in both directions gives the entire geodesic axis by
ordinary amalgam normal form. Its W-type vertices, with their two
incident axis edges, are exactly the w_i^n translates of the common
turn e union j e.

The pointwise stabilizer of that two-edge turn is

    H intersect j H j=<P>.

Its setwise stabilizer is precisely Q0=<P,j>: an element preserving
the unordered turn fixes its middle W vertex, hence belongs to W.
If it fixes both edges it lies in <P>. If it exchanges them, multiply
by j to reduce to that case. Thus it lies in j<P>. This proves the
assertion, including both alternatives.

## 3. A complete three-edge overlap calculation

Suppose g A_i and A_l share at least three edges. Their overlap
contains a two-edge turn centered at a W-type vertex. Multiply g
on the left and right by suitable powers of w_l and w_i to align
this common turn with e union j e. These multiplications preserve
the corresponding axes. The resulting element a has one of the
two forms

    a=P^n or a=jP^n,  n in Z.

The common three-edge path includes at least one of the two
extensions of this turn. Equality of edges is equality of their
left H cosets. There are exactly four cases:

| a | shared extension | necessary and sufficient edge equality |
|---|---|---|
| P^n | at the R endpoint | P_l P^n P_i^-1 belongs to H |
| P^n | at the jR endpoint | P_l^-1 P^-n P_i belongs to H |
| jP^n | at the R endpoint | P_l P^-n P_i belongs to H |
| jP^n | at the jR endpoint | P_l^-1 P^n P_i^-1 belongs to H |

For example, in the third row the image of the right-hand outside
edge is jP^n jP_i e=P^-n P_i e, which must equal P_l^-1 e.
The second and fourth rows are obtained after cancelling the common
initial j. These use the actual relation jPj=P^-1 and no other
corner relation.

Every displayed word lies in the actual K. The exact regional face
K intersect H=<P> of B118 therefore replaces H by <P> in each row.
Now P1,...,P5 are the literal free K basis and i,l are in1,...,4.
Free reduced-word normal form proves uniformly for EVERY integer n:

* The first two rows are possible exactly when i=l and n=0.
* The last two rows are never possible: the two non-P letters have
  the same sign, and when n=0 and i=l they give P_i^2 or P_i^-2,
  still outside <P>.

Thus a=1 and i=l. Undoing the two powers used for normalization
shows g A_i=A_l. We conclude:

    Two DISTINCT translates of the four axes share at most two edges.

The bound is sharp: A_i and A_l for i different from l share exactly
the turn e union j e and neither outside edge. The proof is uniform
over all translates and all integer powers; it is not a bounded
normal-form test or finite orbit calculation.

## 4. Exact ordinary axis stabilizers

Apply the same normalization to an element g preserving A_i.
There is certainly a three-edge overlap, so the previous calculation
gives a=1. Undoing normalization shows

    Stab_M(A_i)=<w_i>.

In particular no element reverses this axis, and its pointwise
stabilizer is trivial. The centralizer and normalizer of the
nontrivial cyclic subgroup therefore satisfy

    C_M(w_i)=N_M(<w_i>)=<w_i>.

More generally, if <w_i> intersects g<w_l>g^-1 nontrivially,
the corresponding nonzero hyperbolic powers have the same axis.
The calculation gives i=l and g in<w_i>. Thus these four cyclic
subgroups form an actual malnormal family in the discrete M.

## 5. What these exact statements do not prove

The final relation w_i^2 has translation length4, while the sharp
overlap bound is2. The result is therefore not a strict one-sixth
metric small-cancellation estimate. No stronger relative
small-cancellation or link condition has been established here.
In particular the simple word length cannot be used to infer a
CAT(0) development, regional injection, a centralizer formula after
filling, or a profinite axis argument.

Only the corner-face equality in Section1 is asserted in the full
completion. Sections2–4 use the ordinary Bass–Serre tree and finite
geodesic paths. Their analogues for arbitrary closed procyclic
subgroups in the completed group are not claimed. The actual final
neck embedding remains the independently proved B121 retraction,
not an inference from this overlap calculation.
