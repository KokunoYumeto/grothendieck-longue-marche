# Checked full-topology reduction through the common involution

Research proposition for the next review, 16 November 2026. No addition to
checkpoint09's formal theorem register is made here. The geometric part
and the source-completion comparison were independently reviewed by CE.

Let P12=PΓ0,12 and use the actual common involution r from B65. Its six
orbits on the original labels all have size two. Let C12=C_P12(r), and let
Q8 be the mapping-class group of the quotient sphere which fixes the six
ordinary orbit labels and preserves the unordered pair of branch labels.
The actual common marking fixes all identifications below.

**Proposition.** There is an index32 subgroup L8 of Q8 and an isomorphism
C12→L8 which induces an isomorphism from C_(P12-hat)(r) onto the open
subgroup L8-hat of Q8-hat. In particular the images of H_T-hat and H5-hat
have intersection exactly the image of K in this eight-point group.

There is also a homomorphism from C12 to a colored seven-point group Q7
which fixes five ordinary labels and preserves an unordered branch pair.
Its restriction to H5 is injective and induces an injection on H5-hat.
Consequently its restriction to K is injective. No equality between K
and the intersection of the two seven-point source images is asserted.

**Proof of the eight-point assertion.** The two branch marks are the
images of the two unmarked fixed points of r. A mapping class in Q8 lifts
through the degree-two branched cover because it preserves its monodromy
character: branch meridians map to1 in C2 and ordinary meridians to0.
Regular fully ramified Birman–Hilden comparison identifies the symmetric
mapping-class group modulo its deck involution with Q8. Each lift acts on
the two labels over every ordinary mark by a sheet bit. The vector of six
bits is defined modulo the diagonal vector, since changing the lift
composes with r. This gives a homomorphism

    epsilon8: Q8 → (C2)^6 / <(1,1,1,1,1,1)>.

Moving one ordinary point around one branch point realizes its coordinate
bit. Hence epsilon8 is onto. If its value is zero, exactly one of the two
lifts fixes all twelve labels. Thus its kernel L8 is identified with C12,
and its index is32. The valid prime-power full-topology and centralizer
comparison from B30 applies to <r>. It identifies C_(P12-hat)(r) with the
full completion of C12. Since L8 is finite index in Q8, its full completion
is precisely the corresponding open subgroup of Q8-hat. The resulting
map is injective on the entire common centralizer, so it preserves the
actual intersection of the two specified source closures. B65 puts both
source groups in C12, and continuity does the same for their closures.

**Proof of the seven-point assertion.** Forget the two marked fixed
points of D=C5. They form one r-orbit. This gives a homomorphism from C12
to C10=C_P10(r). The restriction to H5 identifies it with C_P10(D).
Indeed both cyclic quotient orbifolds have two ordinary orbit marks and
the same two distinguished branch points. The latter are individually
distinguished by the local rotation residues +1 and -1 modulo5. A
commuting representative in the ten-point group preserves the two fixed
points individually, and marking them gives the inverse quotient-cover
comparison. The deck rotations act nontrivially on the ten ordinary
labels, so there is no pure finite kernel. Both pure centralizers are the
same free rank-six group associated with u↦u^5 and its seven-punctured
source curve. The established prime-order-five topology/density theorem
applies on both surfaces. Thus the restriction of the completed forgetting
map to the actual completed H5 is injective. This is not an inference
from discrete injectivity alone.

The involution r is still free on the ten retained labels. Its quotient
has five ordinary labels and two branch labels. The preceding sheet-bit
argument gives

    epsilon7: Q7 → (C2)^5 / <(1,1,1,1,1)>,

with kernel L7 of index16 and C10≅L7. Applying the valid prime-order-two
comparison identifies C_(P10-hat)(r) with L7-hat. Composition gives the
claimed injection on H5-hat and hence on its subgroup K. The tetrahedral
source also has a map to Q7, but no injectivity on that source has been
used. Equal images under this further forgetting need not have equal
preimages in C12-hat; that is the exact remaining lift-matching issue.

**Geometric coordinates and the branch permutation.** In the cyclic
family r_u(z)=u/z, the six ordinary quotient marks are infinity and

    t_i(u)=zeta^i+u*zeta^(-i),  i=0,...,4.

The two branch marks are ±2sqrt(u), unordered. The seven-point target
forgets the ordinary infinity mark and keeps both branch marks. A loop
around u=0 interchanges the branches, so the full source must land in the
colored group, not the pure seven-point group. On the index-two source
u=s^2, normalize the two branch marks and t_0 to0,infinity,1. The four
remaining coordinates are

    ((s+zeta^i)(s-1)/((s-zeta^i)(s+1)))^2,  i=1,...,4.

The index-two source is P1 minus {0,infinity,mu_10}, of free rank11.
These are the branch marks absent from B69's original rigid forgettings;
retaining them explains why this faithful target does not contradict the
explicit full-rigid relation there.

**Next gate.** A solution still needs a full ambient intersection or
compatible-lift argument inside Q8-hat, or a proof that the seven-point
comparison separates the two particular images. Discrete disjointness
B72, the prime-power comparisons, and the known individual source
embeddings do not establish that intersection assertion.

**Pure target on the actual intersection.** The tetrahedral parameter
family uses a fixed actual T-action on the sphere. The two fixed points
of the chosen r are therefore fixed individually throughout that family.
Its quotient monodromy has trivial branch-pair permutation. Density gives
the same conclusion on H_T-hat, and hence on K. Thus the faithful image
of K lies in the open pure seven-point subgroup PΓ0,7-hat of Q7-hat.
On the cyclic source this is precisely the index-two subgroup obtained
from u=s²; its rank is11. This additional typing does not make the
seven-point map faithful on the tetrahedral source or identify the two
source-image intersections.


**Chosen splitting of the deck extension.** For Q8 choose the ordinary
label which is the image of the actual pair {1,3}, and require its lift
to fix original label1. Every class has exactly one of its two lifts
with that property, and the property is preserved under products. This
splits the central extension by <r>. In Q7 the pair {1,3} has been
forgotten; instead choose the ordinary label from {2,5} and require the
lift to fix original label2. This gives the analogous splitting. Both
sections agree with the unique all-label-pure lift on L8 and L7,
respectively. Their choices need not agree as sections under forgetting
on all of Q8; the quotient comparison and its restriction to the pure
source groups do commute.

**The exact finite-index refinement gate in Q8.** Put A=image(H_T) and
B=image(H5) in L8≤Q8. The original prime-power topology comparison makes
C12 carry its full topology from P12. Thus the eight-point replacement
changes no finite-index refinement problem for these two source groups.
The equality of completed intersections is equivalent, by B46, to closure
of the appropriate refined products in Q8. One may test cofinally all
normal finite-index V in Q8, and the sufficient symmetric form is
(A∩V)(B∩V) closed for every such V. Full induced topology on C12 guarantees
that the finite-index neighborhoods obtained this way are cofinal with
those induced from P12. The unrefined product is closed by B52 and the
finite-index embedding L8≤Q8. No arbitrary refinement has been proved by
this change of ambient group.

**Transferred discrete disjointness.** For every q in Q8,

    A ∩ q B q^(-1) = 1.

Indeed choose any actual lift g of q to the twelve-point symmetric
mapping-class group. Equality in Q8 between the images of a∈H_T and
b∈g H5 g^(-1) says that a*b^(-1) is a deck transformation. Both a and b
are pure, while r has six nontrivial transpositions on the original
labels. The deck difference is therefore the identity, and B72 applies.
This proof neither asserts A*B embeds nor supplies the full induced
topology on the subgroup generated by A and B.
