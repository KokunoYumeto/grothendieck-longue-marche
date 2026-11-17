# Actual nodal cover, Brown–Loday comparison, and the Smith edge map

Research proof, 2026-11-16. No vanishing of kappa is asserted. The new
nonasphericity result B100 is compatible with every construction below.
This note keeps the actual E-coefficients; an ordinary node-sphere
calculation is explicitly distinguished from them.

## 1. The actual spaces and the ordinary homotopy comparison

Use the spaces and based involution of B89–B92. Pull back to the universal
cover of the filled space X, and write

    C=Z~, A=Y~, B=V~, W=A union B=X~ minus the lifted nodes.

The letters A,B in this section denote the two open spaces. Put
K_s=pi1(C), N_A=ker(K_s→pi1(A)), N_B=ker(K_s→pi1(B)). The one-sided
groups are the two free groups R_A,R_B. B89 gives

    K_s=N_A N_B,  M=N_A intersect N_B=[N_A,N_B],
    E=K_s/M=R_A times R_B.

A and B are K(free,1)'s. The contractible four-manifold X~ with its
locally finite node set removed is2-connected: compact maps and homotopies
of dimensions at most3 can be made transverse to that discrete set and
then avoid it. Excision and the relative fundamental classes give

    H3(W,Z)=Z[lifted nodes],  pi3(W)=H3(W,Z).

In particular there is no need to assume C aspherical. The open cover is
a homotopy pushout after the usual mapping-cylinder replacement.

The exact primary dependency was reopened in Brown and Loday (1987),
Theorem3.1 and Corollary3.2, printed318–319, and Lemma4.1, printed320.
The homotopy-fiber square identifies its fundamental group with the
nonabelian tensor product N_A tensor N_B. The fibration sequences, using
pi2(A)=pi3(A)=pi2(B)=pi3(B)=0, give the exact comparison

    pi2(C) → pi3(W) → N_A tensor N_B → M →1.                 (1)

The last map is the commutator map. This formula is a homotopy-fiber
calculation, not an extension of the E-cover across the fillings.

There is a useful precise description of what (1) remembers. Replace C
by K(K_s,1) and form the classifying-space homotopy pushout W_cl. By
Brown–Loday Corollary3.4 and B89,

    pi1(W_cl)=1,  pi2(W_cl)=M/[N_A,N_B]=0,
    pi3(W_cl)=ker(N_A tensor N_B→M).

Mayer–Vietoris for W_cl, since both other vertices are graphs up to
homotopy, identifies H3(W_cl) with H2(K_s). Hurewicz is an isomorphism
in degree3. Hence the tensor kernel in (1) is exactly H2(K_s), and the
node-sphere map is, after the Mayer–Vietoris connecting isomorphism,
the ordinary Hopf map

    pi2(C) → H2(C)=Z[lifted nodes] → H2(K_s) →0.             (2)

This also checks the action limitation. Brown–Loday Proposition2.3(e),
printed314–315, says each of N_A,N_B acts trivially on the relevant
tensor kernel; they generate K_s. Thus that kernel has trivial K_s
action. It cannot retain the full E-coefficients of B92's Z2.

### Signs

At a fixed node the holomorphic branch interchange preserves the real
orientation of the local4-ball and hence the positive orientation of
its linking3-sphere. Its action on H3(W) is the positive permutation of
nodes. Mayer–Vietoris exchanges its two open-set terms, so its connecting
map into H2(C) changes sign. Equivalently, the local torus has its two
circle factors exchanged and its2-orientation reversed. Thus H2(C) has
the negative permutation action on the node basis.

The tensor action compatible with the commutator map is

    F_T(m tensor n)=(F(n) tensor F(m)) inverse.

The defining tensor relations verify this directly; the commutator of
the right side is F([m,n]). On a local node tensor it is negative
interchange. Accordingly the map from the positively oriented linking
spheres to this tensor kernel is anti-equivariant under the branch
interchange, or equivariant after the sign twist. This is precisely the
same sign as the Mayer–Vietoris map. No positive-permutation action is
silently transferred to a commutator2-cell.

The primary PDF is https://groupoids.org.uk/pdffiles/RB-Loday1.pdf.
Theorem3.1/Corollary3.4 and Proposition2.3, including their proofs, were
read at retrievals turn862view0/1 and turn864view0/1. The comparison (2)
is derived here. No use of the stronger hypothesis pi2(C)=0 in
Brown–Loday Proposition4.3 is made.

## 2. Relative homotopy model over a single critical disk

This supplies the geometric upgrade that is not part of a bare van
Kampen presentation. Work first in the finite original puncture family
over a sufficiently small disk about one of its actual nodal critical
values. No retained punctures collide there. Choose disjoint moving
fiber disks containing the colliding pairs, away from every other
trajectory. The exterior punctures and the disk boundaries trivialize
over the whole base disk by the actual finite-family isotopy.

The exterior is therefore a product of the base disk with a punctured
planar surface having one additional boundary circle for each collision
disk. Those boundary circles are part of a free basis of its group.
An interior node block is the complement of the two transverse branch
disks. Holomorphic coordinates x,y identify the branches with x=0,y=0;
shrinking the block, or changing between concentric convex neighborhoods,
gives the usual normal-crossing bidisk complement, a K(Z2,1). Its
intersection with the exterior is a product annular collar. The positive
boundary meridian is the product ab of the two positive interior
meridians, and it injects in the interior Z2.

One can check the interior homotopy type without a fibration assertion
at the node. A sufficiently small round ball is radial; removing the
two complex axes leaves the Hopf-link complement on its sphere. The
two angular coordinates and the radial ratio give its homotopy
equivalence to the torus. Annular collars and slightly enlarged node
boxes give the same pair by radial isotopy. The boundary collar loop
is ab in that torus, with the actual nearby fiber basepoint retained.

The resulting graph of spaces has a tree as its incidence graph. Its
vertex spaces are aspherical and all edge maps inject on fundamental
groups. Its universal cover is a tree of contractible vertex and edge
spaces, hence contractible. Eliminating each primitive exterior boundary
generator gives

    pi1(local block)=F_free * (free product of one Z2 per node). (3)

Here Z2 in (3) means the rank-two free abelian group, not the syzygy
module. The generic fiber is a punctured planar surface. Replace it by
its actual peripheral graph and attach one2-cell along each transported
commutator [a,b]. In a local adapted basis the resulting complex is a
wedge of the same graph and one torus per collision. It is aspherical
and has exactly the group in (3).

Map the graph to the actual nearby fiber and fill each commutator by the
local torus map. This is a map of pairs with the prescribed generic
fiber inclusion. Its fundamental-group map is the identity in the
adapted marking, so it is a homotopy equivalence. The generic fiber is a
graph up to homotopy, which also makes the specified pair comparison
unique up to the required based homotopy. This verifies the relative
attaching map, rather than inferring a homotopy type from van Kampen alone.

Pull this finite relative model back to the old-F5 covering. Covering
homotopy lifting gives the corresponding relative equivalence. The
generic graph is the actual generic-cover kernel graph, and the2-cells
are all old-F5 translates of the original local node cells. This keeps
every sheet and every based transport, including repeated component
pairs. No free graph-product replacement of their words is made.

## 3. Equivariance and global gluing

Use B92's normalization of the actual fiber involution to z↦-z and its
actual equivariant regular-path transports. At a fixed node choose an
equivariant holomorphic chart. The two transverse branches are exchanged;
one branch coordinate x and its F-image y give a coordinate pair with
F exchanging x,y. The local torus model can therefore be chosen symmetric.
With the nearby fixed-source basepoint and paired meridian arcs, its fixed
diagonal circle is exactly the actual source peripheral ab. The fixed
subspace of the node complement is the punctured diagonal disk, and this
circle map is a homotopy equivalence of that fixed subspace.

In the chosen universal old-fiber cover there is just one fixed point
in each regular fiber. Thus above a given critical value there is at
most one fixed lifted node; the others occur in pairs. If there is no
fixed node, the local fixed subspace is the unpunctured source disk and
the fixed part of the local model is contractible. If there is one,
both fixed subspaces have the circle homotopy type just described.
For nonfixed node pairs choose one local filling and its actual F-image.

The exterior isotopies are chosen equivariantly and retain the actual
source whisker. The graph model of the generic fiber comes from the
paired quotient-orbifold arcs of B91; its fixed subspace is the selected
basepoint. Thus the local maps are equivalences both on underlying
spaces and on F-fixed subspaces, compatibly with their common generic
fiber. After mapping-cylinder replacement they are equivalences of
equivariant CW pairs. This last implication can be proved cell by cell:
the only stabilizers are1 and C2; extending a homotopy inverse over a
cell uses the vanishing relative homotopy groups on the corresponding
fixed subspace. It is not an inference from the underlying pi1 alone.

Choose the common locally finite base tree of B92, with its fixed-source
peripheral paths. Over regular strips use its equivariant fiber
trivializations. Over critical disks use the preceding relative models.
Each compact stage is obtained by gluing those maps of pairs, with
mapping cylinders used for cofibrations. The gluing preserves the
underlying and fixed-subspace homotopy equivalences. Exhaust the
universal old base by such compact stages. Every compact loop, sphere,
or homotopy meets finitely many stages; the compatible union is a weak
equivalence on underlying and fixed subspaces and hence an equivariant
CW homotopy equivalence.

This yields a based F-equivariant nodal2-complex V_nod mapping to the
actual C=Z~, with its paired generic graph and its actual transported
commutator cells. Its fixed graph is the chosen punctured source graph.
The comparison uses no assertion that the global complement is
aspherical; its2-complex can and, by B100, does have nonzero pi2.

## 4. The actual E-cover and its fixed components

The based comparison induces the actual group K_s and the quotient
K_s→E. Lift it through that quotient. Uniqueness of based lifting makes
the lift commute with both the deck E-action and F. In particular the
actual cover C_E associated with M has the equivariant cellular model

    C2=P_node  --partial*d--> C1(T_A times T_B)
                    --partial1--> C0(T_A times T_B),       (4)

where the original product squares are not attached: their module P
only parametrizes the boundaries of the actual node cells. The map d
is precisely B92's actual column map, and the product-tree boundary
partial:P→C1 is injective. Consequently

    H1(C_E,Z)=M_ab=P/Lbar,  H2(C_E,Z)=ker d=Z2.             (5)

These are isomorphisms with the full E-action and the actual F-action.
They are not obtained by extending this cover over W. Such an extension
would require its nontrivial E-monodromy to die and is not used.

The fixed locus of the selected F on C is exactly the punctured selected
source S~, by B87/B92. At a fixed basepoint the fixed fiber labels in
the E-cover are the diagonal E-elements (r,r). Lifting source paths
identifies labels by the diagonal image of its fundamental group, which
is exactly I. A component containing one fixed point is fixed pointwise
by uniqueness of lifts of the identity on S~. All fixed points project
to S~. It follows that

    pi0(C_E^F)=R/I,    H0(C_E^F,Z)=Z[R/I].                 (6)

Each fixed component is a covering of a punctured disk, so its H1 is
free abelian and it has no higher homology. No injectivity of the
source fundamental group into K_s is needed. The same argument applies
to the fixed graph of the nodal model, and the source peripheral graph
comparison lifts on each fixed component.

## 5. The exact integral Tate edge map

This part is an algebraic identity even before the geometric comparison
of Sections2–4. Use cochain degrees equal to minus cellular dimension.
The reduced complex in (4) has terms in degrees-2,-1,0. The augmented
product-tree complex is exact. Its degree2 boundary therefore gives a
quasi-isomorphism from the two-term complex

    D:  P_node in degree-2  --d-->  P in degree-1           (7)

to the reduced cellular complex. The quotient has its only two terms
identified by an isomorphism, since C1/P maps isomorphically to the
augmentation kernel of C0. Thus the comparison is E- and F-equivariant.

Apply the complete two-periodic C2 cochain resolution, with alternating
maps1-F and1+F, and totalize. Because the cellular direction is bounded,
all the elementary row and column spectral sequences converge without
infinite-product or support assumptions. A quasi-isomorphism of these
bounded complexes induces an isomorphism on this Tate hypercohomology.

Both P and P_node have vanishing even Tate cohomology and their odd
cohomology is the negative-fixed-index binary module. B91–B92 identify
the map between their odd groups as having image J_I. The two-term
calculation gives, canonically,

    TateHyper^0(D)=I_F2[R]/J_I.                            (8)

Its homology truncation has H^-2(D)=Z2 and H^-1(D)=M_ab.
The exact triangle of these two homology objects gives

    H2(C2,Z2) --kappa--> I_F2[R]/J_I
       → H1(C2,M_ab) → H3(C2,Z2) → TateHyper^1(D).          (9)

Here H2,H1,H3 denote group COHOMOLOGY. To check the first map exactly,
represent a degree2 class by z in Z2 with Fz=z. Since H2(C2,P_node)=0,
write z=(1+F)p with p in P_node. Then d(p) is anti-invariant, and its
diagonal class modulo J_I is the edge image in (9). This is literally
B92's representative formula for kappa, including its sign convention.
Thus kappa is the edge/transgression map in (9), not an unexplained
new map or a conclusion that a spectral-sequence differential vanishes.

There is an elementary fixed-space interpretation of (8). Subdivide each
fixed commutator disk along its reflection diagonal; its two open halves
are exchanged and its diagonal is pointwise fixed. Subdivide paired
cells compatibly. The cellular chains relative to the fixed graph are
then sums of free Z[C2]-modules. Their Tate hypercohomology is zero,
because the complex is bounded and every such summand has zero Tate
cohomology. Hence inclusion of the fixed graph induces an isomorphism
on reduced Tate hypercohomology. For a graph with trivial action, the
integral H0 and H1 are free, so its degree0 reduced Tate hypercohomology
is its reduced H0 with F2 coefficients. By (6), this is

    ker(F2[R/I]→F2)=I_F2[R]/J_I,

exactly (8). This is the precise Smith-chain comparison in the present
model, with no appeal to vanishing of an unknown homology group.

The map from the coset augmentation module to H1(C2,M_ab) in (9) sends
the difference r-inverse I minus I to the actual right-defect class of
the diagonal target(r,F(r)). This follows either from the elementary
product rectangle or from B91's actual defect formula. Its kernel is
im(kappa). This is the sought exact comparison, not an injectivity proof.
To retain the vertex convention precisely, a path from vertex1 to
vertex(r,r) gives the LEFT defect F(x)x-inverse and the coordinate r-1.
The RIGHT defect x-inverse F(x) is its diagonal r-inverse translate;
its coordinate is r-inverse-1 in characteristic2. Thus the preceding
evaluation at r-inverse I-I does not identify the endpoint label r
with r-inverse or alter the left R-action.

## 6. What this does and does not decide

The full E-cover retains the obstruction; the ordinary Brown–Loday
node-sphere quotient does not. The fixed graph has dimension one, but
this does not kill the first map in (9). An invariant2-cycle can still
contribute through H2(C2,H2(C_E)); a submodule of a free C2-module need
not have zero cohomology. There is therefore no inference from the
absence of pointwise fixed2-cells to kappa=0.

B100 supplies a concrete nonzero pi2 sphere, so a proof based on
contractibility of the actual universal cover is unavailable. The
sphere's existence does not supply a nonzero kappa value: its relevant
old0 node orbit belongs to paired summands in B95. The task remains to
evaluate the actual edge map (9), or to prove its image contains no
nontrivial coset difference. Even that projected conclusion would not
by itself settle the remaining nonlinear or compact fixed-lifting gates.

The present note is research for independent review. No formal source,
register, or bibliography was changed by it.

## 7. A precise equivariant-sphere test

Let C2 act on S2 by a half-turn about its vertical axis. Its action on
the fundamental class is positive and its fixed locus consists of the
two poles n,s. For this model the reduced Tate hypercohomology sequence
has H1(S2)=0, and its Smith edge is an isomorphism

    H2(C2,H2(S2,Z))=F2 → reduced H0({n,s},F2)=F2.

It takes the fundamental class to n-s. This can also be checked by
dividing the sphere into two exchanged lunes. Naturality of Section5
therefore gives, for any actual equivariant map f:S2→C_E,

    kappa([f_*[S2]]) = [component(f(n))]-[component(f(s))]
                        in ker(F2[R/I]→F2).              (10)

In particular an equivariant sphere whose poles lie in different fixed
source components would give a nonzero kappa value. An invariant ordinary
homology class is not automatically represented by such an equivariant
sphere; (10) cannot be applied without the actual map.
For poles at vertices1 and(r,r), (10) is rI-I. Translating the whole
sphere by the F-fixed deck element(r-inverse,r-inverse) gives instead
r-inverse I-I, exactly the right-defect convention of Section5 and
B91. The two literal values differ by this specified invertible left
translation; they are not asserted equal without it.

There is an exact nonlinear interpretation of this special test. Choose
fixed paths within the pole components to points over the original
source basepoint. After a diagonal deck translation, their labels are
1 and(r,r). A meridian arc of the sphere from n to s and its F-image are
homotopic relative endpoints in the sphere. Their images in C_E project
to the same based element of K_s, so this element is literally F-fixed
and has image(r,r) in E. Different pole components mean r is not in I.

Conversely, if g in K_s is literally F-fixed with image(r,r), lift a
representing loop to a path gamma in C_E from the chosen basepoint to
its(r,r)-translate. The equality F(g)=g supplies a based homotopy
between gamma and F(gamma), lifting relative endpoints. Use it as one
lune and its F-image as the other. They glue to an actual equivariant
half-turn sphere with fixed poles at those endpoints. Thus a sphere of
the kind in (10), with distinct source components, is equivalent to a
counterexample to the actual nonlinear projected fixed-source assertion
over the zero Q-head. General heads in H_b reduce to this one by an
actual fixed source lift, as in B92.

This does not construct a counterexample. It explains why finding an
actual equivariant sphere is stronger than finding an arbitrary
invariant2-cycle or a nonzero class in H2(C2,Z2).

## 8. Spherical and nonspherical2-cycles

The ordinary Hopf sequence for the actual E-cover is F-equivariant:

    pi2(C_E) → H2(C_E,Z)=Z2 → H2(M,Z) →0.                 (11)

Let S_sph be the image of the first map. The covering identifies the
pi2 term with pi2(Z), but the Hurewicz image need not be all of Z2 and
need not identify with pi2(Z) injectively. Consequently the actual
sphere families from B100, even after all deck and F translates, do not
by themselves determine the whole kappa domain.

For example a valid sufficient decomposition of the remaining problem
would be to prove both

    kappa composed with H2(C2,S_sph)→H2(C2,Z2) is zero,
    H2(C2,H2(M,Z))=0.

The cohomology exact sequence of0→S_sph→Z2→H2(M,Z)→0 would then make
the first map onto and force kappa=0. Neither premise is established.
This conditional observation was independently pointed out by DE; it
keeps the nonspherical group-homology quotient visible rather than
silently replacing all2-cycles by transported spherical identities.
