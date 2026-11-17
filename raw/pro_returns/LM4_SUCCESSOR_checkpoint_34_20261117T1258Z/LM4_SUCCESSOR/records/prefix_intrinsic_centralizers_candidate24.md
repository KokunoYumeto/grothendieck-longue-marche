# Candidate exact intrinsic regional centralizers

Root,2026-11-17. Complete proposed discrete argument; independent review
pending. No numbered result and no profinite-centralizer conclusion yet.
The actual group R is the B112 annular bad vertex BEFORE both B114 cross
relations. The calculations use the entire regional graph, not a truncation.

## Exact graph model and its two links

Use the complete presentation isomorphism from
work_A/annular_regional_edge_centralizer23.md:

    R = N semidirect (D x Z_z),
    N = A(Omega), D=<C,k | C^2=1>, T=<k>, z=C h.

The graph vertices are (gT,U,n), with U in {a,b,d,e}, n in Z.
The actual a is (T,a,0); B=CbC is (CT,b,0). The graph contains all
D-translates of the ten listed edge types, at every integer height.
Directly applying those ten types gives the COMPLETE links

    lk(a) = {(T,b,0)} union
            {(k^m CT,U,0): m in Z, U=a,d,e},

    lk(B) = {(CT,a,0)} union
            {(C k^m CT,b,0),(C k^m CT,d,1),
             (C k^m CT,e,1): m in Z}.

The free-product normal form in D shows all the k^m CT cosets distinct,
and C k^m C lies in T exactly when m=0. Consequently

    lk(a) intersect lk(B) = {(T,b,0),(CT,a,0)}.

These two vertices are nonadjacent. The whole induced graph on lk(a)
is discrete. Indeed all its a,d,e vertices have odd C-parity, whereas
every edge of these types joins opposite C-parities; the only same-coset
edge is a--b, and the sole b vertex has coset T. The interlevel b--d/e
edges cannot occur because all these vertices have height0.

## Elementary centralizer proof for any graph

We give the needed two-letter case directly rather than use an unread
general centralizer theorem. For a graph Gamma and nonadjacent vertices
x,y, put H=A(Gamma minus x) and L=A(lk(x)). The graph presentation is
the HNN extension <H,x | [x,L]=1>. Both x and xy have translation length1
on its Bass--Serre tree. Their centralizers preserve their respective
axes and act by integral translations; the indicated length-one element
generates the image of that action. The remaining kernel fixes the axis
pointwise and commutes with the length-one element.

For x the pointwise stabilizer is L. For xy, two consecutive axis edges
force the pointwise stabilizer into L intersect y L y^-1: the second
edge stabilizer is x y L y^-1 x^-1, and x centralizes L. Split A(Gamma)
instead as the HNN extension with stable letter y. Since y is not in
lk(x), L lies in its base group. Britton's lemma says that y v y^-1
with v in L can belong to that base group only if v lies in A(lk(y));
then y commutes with v. Hence

    L intersect y L y^-1 = A(lk(x) intersect lk(y)).

Here the intersection of full graph subgroups follows even without a
word theorem: deleting generators outside a vertex set gives a
retraction, and these deletion retractions commute. Every element of
the right side commutes with x,y and fixes both initial edges, so it
fixes the entire axis. We therefore obtain, for an arbitrary possibly
infinite graph,

    C_A(x) = <x> x A(lk(x)),
    C_A(xy) = <xy> x A(lk(x) intersect lk(y)).

All HNN maps are the explicit full graph inclusions, with deletion
retractions; no completion or finiteness theorem is used.

## Return from N to the actual R

Write an element of R as n delta with n in N and delta=(g,z^m).
Conjugation by n acts trivially on the free abelian group N_ab, whose
basis consists of all vertices of Omega. If n delta centralizes a,
the coordinate vertex delta(a) must equal a. Thus m=0 and g belongs
to T. The actual k fixes a, so

    C_R(a) = C_N(a) semidirect <k>.

It fixes the vertex b and shifts m freely on each of the three remaining
families of lk(a). Eliminating their orbit generators gives the exact
presentation

    C_R(a) = Z_a x (Z^2_(b,k) * F(CaC,CdC,CeC)).

For aB, its abelianization has one a-type and one b-type coordinate.
The action cannot exchange the family types. It must therefore fix
both (T,a,0) and (CT,b,0). This requires m=0 and
g in T intersect C T C={1}, by the free-product normal form. Hence

    C_R(aB) = C_N(aB) = Z_(aB) x F(b,CaC).

The two centralizer abelianizations are Z^6 and Z^3, respectively.
They are not isomorphic. An automorphism of R sends an element's
centralizer isomorphically to the centralizer of its image. Therefore
NO discrete automorphism of R sends a to aB. In particular the actual
prefix automorphism theta of K cannot extend to any automorphism of R,
regardless of the image chosen for the base generator.

This strengthens the discrete automorphism conclusion. It does not
exclude arbitrary homomorphisms with changed orientation/winding,
does not identify completed centralizers of these infinite-order
elements, and makes no claim after the actual cross quotient.

## Literature-search boundary

We searched for Servatius's original centralizer theorem and opened
the author page and publisher metadata for Automorphisms of graph groups,
Journal of Algebra126(1),34--60(1989), DOI10.1016/0021-8693(89)90319-0.
The original full proof was not available from those retrievals. Later
paper snippets state its formula but are not substituted for that proof.
The two-letter proof above supplies the precise result needed here.
An attempted arXiv identifier1112.1047 returned an unrelated biological
network paper; it is rejected as irrelevant and supplies no fact here.
We claim no priority and no literature-based general theorem beyond
the explicitly proved special case.

Draft-count correction: the complete regional list has ten node-edge types (four diagonal, four same-height cross types and two interlevel types). The initial prose called them eight; the displayed links and the actual ten-relator input were unchanged.
