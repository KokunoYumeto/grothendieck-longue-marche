# The prefix change necessarily changes the regional base-loop image

Research after the formal freeze; no numbered statement added. We give a
specific obstruction to one extension convention, not to every possible
regional graph presentation.

Let K have its actual physical comb O=(O1,...,O5) and adapted basis
(a,B,d,e,f) as in B114. Define the free-group automorphism theta of K
by theta(O_i)=P_i=O1...Oi. Its inverse sends O1 to O1 and O_i to
O_(i-1)^(-1)O_i for i>1. Since O1=a B a^(-1) and O2=a,

    theta(a)=P2=O1 O2=a B.

In the actual regional group R, [k,a]=1. However [k,a B] is nontrivial.
Indeed k commutes with a, so it is an a-conjugate of [k,B]. In B112's
complete graph model the two vertices k0 and B=bar(b0) are nonadjacent;
their full graph subgroup is the free group on those vertices. This
already proves discrete nontriviality.

We additionally supply a prescribed finite detector, to prove nontriviality
in the actual full completion without inferring it from the infinite
graph kernel's topology. Pass to B112's exact even-period head m=4.
Its graph has34 vertices. Send k0 to(12),bar(b0) to(123),and every other
graph vertex to1 in S3. These two noncommuting images are assigned only
to nonadjacent vertices, so this is a graph-group homomorphism. Take
the eight translates of that map under C4(h) times C2(C). Their product
is equivariant for the regular action on the eight coordinates and
extends to a homomorphism

    R -> S3^8 semidirect (C4 times C2).

The identity coordinate detects [k,B]. The producer explicitly checks
every finite graph commutator, every acting graph automorphism, and all
seventeen actual regional defining relators (sixteen plus the cone square).
It also checks both directions of the full prefix free-basis substitution.
The complete finite image of [k,theta(a)] is nonidentity.

Consequently no homomorphism R->R restricting to theta on K and fixing
the actual k exists. The same holds for continuous maps of the full
completions with those restrictions: the finite image survives there.
This conclusion does not depend on what image is proposed for the cone.

The implication for the current gluing route is narrow but concrete:
the edge-only prefix change cannot be promoted while retaining the old
regional base-loop image. A valid simultaneous construction must change
that image or use another regional presentation comparison. Merely
renaming an edge free basis is still legitimate; it produces transformed
regional relations rather than automatically preserving a graph form.
No arbitrary basis extension, corrected section, post-cross vertex
injection or centralizer formula is refuted.

Producer and genuine output:
code/check_prefix_fixed_base_obstruction23.py;
records/check_prefix_fixed_base_obstruction23.out/.err;
records/prefix_fixed_base_obstruction23.json.
Root supplied the proof and executed the exact finite detector. Independent
review is pending after checkpoint release; this is not a new formal row.
