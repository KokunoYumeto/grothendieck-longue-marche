# Independent review of the actual nodal-cover and Tate comparison

Reviewed complete research note:
`work_A/actual_nodal_cover_Smith_comparison_19h.md`.
The requested independent geometric review concentrates on Sections2–4;
the chain degrees, signs and exact edge map in Section5 were also checked.
Those sections pass with their stated absence of a vanishing conclusion.
This review does not independently re-prove the primary Brown–Loday
identifications in Section1.

## 1. Finite local relative model

Over a sufficiently small critical disk, only the specified disjoint
pairs collide. The exterior finite-family isotopy trivializes the other
punctures and the collision-disk collars. The exterior is therefore a
product with a punctured planar surface. Its collision-boundary loops
can be included simultaneously in a free basis.

An interior ordinary node is the complement of two transverse complex
branches. In a normal-crossing chart its homotopy model is the torus;
the common annular collar represents the product ab of the two positive
meridians. This loop injects into Z². The exterior/interior incidence
graph is a tree, and all collar maps are pi1-injective. A universal
cover is a tree of contractible vertex and edge spaces, proving local
asphericity rather than merely computing a presentation. Eliminating
the primitive exterior collar generators gives

  F_free * (free product of one Z² for each node).

The actual generic peripheral graph with one transported commutator
cell per node has the same aspherical local model. Its map to the local
complement extends the prescribed generic-fiber inclusion. The pi1
isomorphism and local asphericity make it a homotopy equivalence.
Using collars/mapping cylinders gives the relative comparison; no
generic-fiber injection after the collision is assumed. The actual
generic fiber is itself a graph up to homotopy, and the aspherical
target removes ambiguity in the required based homotopies.

## 2. The additional equivariant check is necessary and present

An ordinary equivalence of pairs would not suffice. At a fixed node,
choose one holomorphic branch coordinate and its F-image, so F exchanges
the two coordinates. The symmetric torus model has its fixed diagonal
circle, and the actual complement has a punctured diagonal disk. The
diagonal circle maps by a homotopy equivalence to that fixed subspace;
its peripheral is the actual source word ab, with the same whisker.

The selected universal old-fiber cover has one fixed point in a regular
fiber. Thus a critical disk has at most one fixed lifted node. In the
absence of a fixed node the fixed local source disk and the fixed local
model are contractible; with a fixed node both have the specified circle
type. Nonfixed node blocks and their maps are paired. The exterior
comparison retains the selected source arcs and its fixed basepoint.
Consequently the local map is an equivalence on both the underlying
and F-fixed spaces, which is exactly the extra requirement for the
equivariant CW-pair argument. The coordinate torus can be subdivided
along its diagonal; it is unnecessary and unsafe to infer its fixed
cell structure from an abstract commutator presentation alone.

The finite local relative models lift through the actual old-F5 cover:
their node commutators die under retained filling, so this covering
exists over the whole local block. This produces all deck translates
with their actual based words. The compatible regular-strip transports
and local maps can be glued over compact stages of the actual locally
finite base tree. Mapping cylinders ensure cofibrations. Compact maps
and homotopies lie in finite stages, giving the stated underlying and
fixed-space weak equivalences, and hence the equivariant CW comparison.
No global graph-product or asphericity inference is used.

## 3. The E-cover and fixed components

The comparison induces the specified quotient of the actual fundamental
group to E. The based lift therefore commutes with both deck E and F.
The covering graph of the generic free product is the one-skeleton of
T_A times T_B. Product squares are NOT attached to the actual nodal
complex: their free module P parametrizes boundaries only. Since the
product-tree boundary P->C1 is injective, the actual cellular complex
has H1=P/Lbar and H2=ker(d), with the full actions retained.

At the chosen fixed basepoint, F-fixed E labels are diagonal(r,r).
Lifting the actual source paths identifies labels by right multiplication
by I. Their components are thus the left cosets rI, giving R/I and
the left permutation module Z[R/I]. This does not require I normal
or source injection. Once a lift of a source component contains a fixed
point, uniqueness of lifts makes its entire component fixed pointwise.
All fixed points project to the selected source, so no components are
omitted. This also fixes the left-ideal convention for J_I.

## 4. Exact Tate edge map; no vanishing theorem

Use cochain degrees minus cellular dimensions. The two-term complex
P_node[-2] -> P[-1] is quasi-isomorphic to the reduced cellular complex:
the quotient is the isomorphism C1/P -> ker(C0->Z). The cellular width
is finite, so complete two-periodic C2 cochains totalize without an
uncontrolled infinite-support limit. The odd Tate groups of P_node and
P carry the B91–B92 diagonal modules and their even groups vanish.
Therefore Hyper^0 is exactly coker(H1(P_node)->H1(P))=I_F2[R]/J_I.

The homology truncation has Z2 in degree-2 and M_ab in degree-1. Its
long exact sequence has the stated segment

  H²(C2,Z2) -> Hyper^0 -> H¹(C2,M_ab) -> H³(C2,Z2).

For an invariant cycle z, write z=(1+F)p in P_node. Then d(p) is
anti-invariant, and its diagonal modulo J_I is the first edge map.
This is the actual B92 representative formula, with the same sign.

Subdividing fixed torus cells along the reflection diagonal leaves
relative free C2-cells. Their bounded relative Tate hypercohomology
vanishes. The fixed graph, whose H0 and H1 are free abelian, contributes
in total degree0 precisely reduced H0 modulo2, namely the augmentation
kernel of F2[R/I]. This confirms the Smith interpretation of the same
edge sequence. It does not prove its first map zero: the actual H2
module may have nontrivial involution cohomology even though there are
no pointwise fixed open2-cells.

## Scope

This comparison is compatible with B100's actual nonzero pi2 and
non-mod-two-acyclic universal cover. It supplies a geometric meaning
for the chosen equivariant presentation and edge map, not a value of
kappa, a nonlinear fixed lift, a compact fixed lift, or I=R. A specific
geometric sphere still needs its actual cellular comparison before it
can be assigned a particular class in this kernel.

## Added Sections7–8: actual half-turn spheres and the Hopf quotient

The later half-turn sphere test also passes. The order-two rotation of
S² is orientation preserving, with precisely two fixed poles. Its
degree-zero reduced Tate hypercohomology identifies the invariant
fundamental class with the difference of those poles. Naturality of
the already reviewed edge map therefore sends an actual equivariant
sphere in C_E to the difference of its fixed source components.

The nonlinear equivalence is exact. Paths from the two poles to their
chosen based source lifts are fixed pointwise. A meridian arc between
the poles and its half-turn image are homotopic relative endpoints;
their images give an actual F-fixed element of K_s whose E image is
the corresponding diagonal element. Conversely, an equality F(g)=g
provides a homotopy gamma~F(gamma) in the actual E-cover with fixed
endpoints. Glue that disk to its F-image as the two exchanged lunes.
This produces the required genuine equivariant sphere. Thus an
equivariant sphere with poles in different components would already
give a counterexample to the projected nonlinear fixed-source gate.
No such sphere has been constructed here. Invariant ordinary H2
classes cannot be substituted for actual equivariant maps.

One coordinate convention was explicitly flagged to A and corrected:
fixed endpoints1 and diagonal(r,r) give the literal component
difference rI-I, the left-defect coordinate. The established right
defect uses r^-1I-I after translating by diagonal(r^-1,r^-1).
This affects the literal label, not the nonzero/existence equivalence.

The Hopf quotient in added Section8 agrees with the independently
saved `spherical_vs_full_kappa_cycles_19h.md`: the spherical image S
fits into0->S->Z2->H2(M;Z)->0. Vanishing of kappa on H²(C2,S),
together with H²(C2,H2(M;Z))=0, is a sufficient conditional route.
Neither premise is proved, and a nonzero universal-cover sphere
does not automatically have nonzero Hurewicz image in C_E.

## Formal B102 source review

The complete `work_A/B102_proposed.tex` was read. The requested
relative equivariant local gluing, actual E-cover, fixed component
labels, endpoint/right-defect rebase, half-turn equivalence and Hopf
scope all pass in the formal version. A cosmetic superscript typo
in the Tate hypercohomology notation was flagged and corrected.
No mathematical correction to those sections is requested.
