# Actual coarse bundle and the remaining fine-kernel gluing gate

Research only. This records exact comparisons available after the mirror
calculation, without treating the fine one-neck quotient as a graph group.

## 1. The actual coarse one-neck bundle

Fill the four A and four B graph families in the actual one-neck region.
The remaining ordinary fiber is the sphere punctured at
1,-1,q^(-1/2),-q^(-1/2). In the F quotient it has two order-two cones
0,infinity and the two ordinary punctures 1,1/q. Since q=1 remains
excluded from U_ann, the remaining punctures never collide. The coarse
family is therefore the actual locally trivial orbifold bundle over
U_ann, including all formerly critical fine fibers. Its fiber group is

`W=C2(c_plus)*C2(c_minus)*Z(branch)`.

The base group is F2. The selected constant fixed section t=0 gives a
based product of that base with its C2 cone in the Borel construction.
Hence the exact bundle extension splits through the actual selected
section, and the two source-normalized base operators fix c_plus
literally. Writing B=F2, the coarse group is W semidirect B. It follows
from free-product normal form that

`C_coarse(c_plus)=B times <c_plus>`.

This also holds in full completion. The finitely generated virtually
free group W has cofinal characteristic finite-index subgroups: given a
finite-index subgroup, take its normal core and then intersect the
finitely many subgroups of that index. Each characteristic finite
quotient is preserved by B, and its action factors through a finite
quotient of B. It follows that W has its full induced topology in the
semidirect product. More explicitly, every finite target of the whole
group is retained after choosing a sufficiently small characteristic
fiber kernel and a finite-index base kernel which both kills the finite
action and lies in the original target kernel. These rectangular finite
semidirect targets are cofinal. Thus completion is exactly

`What semidirect Bhat`.

The cone centralizer in What is its original C2 factor, by the full
profinite free-product centralizer theorem already checked at B87/B108
(Herfort--Ribes, Theorem B'). Since the selected Bhat fixes the cone,
the completed coarse centralizer is `Bhat times C2`. This is a coarse
filling result; it does not identify the centralizer before filling.

The selected fine source F6 maps to this actual B=F2, killing its four
contact meridians and retaining both base directions. Consequently the
remaining fine question concerns the kernel over this exact coarse
bundle, not an abstract two-commutator quotient which discards further
height translates.

## 2. Regional kernels and the pre-cross tree of groups

The exact regional projection in
`annular_regional_edge_centralizer23.md` is precisely the regional
version of this filling. It kills the four ordinary U-types and their
cone partners and has target

`B_i=(C2(C_i)*Z(k_i)) times Z(z_i)`.

Its kernel is the actual Omega graph group constructed there. On the
common K the image is infinite cyclic, generated on the inner side by
(Ck^-1,z). Its primitive z-coordinate proves that the coarse edge
embeds in B_i. The outer edge reverses the branch height through the
actual eta, with its entire based word retained.

Before the two cross relations, there is therefore a surjection of
abstract discrete amalgams

`A=R_- *_K R_+ -> A_coarse=B_- *_Z B_+`.

The kernel acts on the actual A-amalgam tree. Its quotient graph is
the Bass--Serre tree of A_coarse: vertices and edges identify with the
corresponding coarse cosets because each vertex and edge map is onto
its indicated coarse image. Thus this fine kernel is exactly a tree
of groups whose vertex groups are conjugates of the two actual regional
Omega graph kernels and whose edge groups are conjugates of K0.

At each initial regional marking K0 is the full coordinate subgroup
on the Schreier vertices listed in the regional note. Other incident
edges are conjugates of such subgroups under their actual vertex
representatives; the fine parts of those conjugators must be retained.
The preceding graph-of-groups comparison is exact. It does not assert
that the edge identifications permute coordinate generators, or that
the resulting group is itself a right-angled Artin group.

## 3. A concrete nonmonomial edge word

The actual reflection is already nonmonomial on a coordinate vertex:

`eta(a)=a B a^-1 B^-1 a^-1`, with B=bar b.

In the standard regional Omega graph, a_0 and bar(b_0) are distinct
nonadjacent vertices. Their subgroup is a free group of rank two.
This reduced word is not a single coordinate vertex or its inverse.
It is a conjugate of a^-1, but that conjugator cannot simply be
discarded. It follows that the current two coordinate presentations
do not glue by a plain graph identification. An alternative RAAG
description would require an explicit simultaneous change of whiskers
or a graph-group automorphism extending all of the actual edge maps,
with every adjacent link checked.

This observation does not refute the existence of some such change.
It identifies the exact extra input needed beyond the statement that
both edge images are full coordinate subgroups as abstract subgroups.

## 4. The coarse two-cells retain fine prefixes

Passing from A to the actual G_ann also fills the two coarse cross
relations. The fine lifts are not obtained by deleting their prefixes:
the selected cone is a C_- a^-1 on one side and
eta(a) C_+ eta(a)^-1 on the other. Thus the actual fine cross words are

`[eta(a) C_+ eta(a)^-1,k_-]` and `[a C_- a^-1,k_+]`.

Their coarse images are the two simple cross commutators, but their
fine conjugations are part of the attaching maps. The finite coarse
presentation alone does not determine the resulting fine kernel or
its cone action. Equivalently, in a height-zero description all the
actual translated fine relations remain necessary. The already
rejected coarse truncation is not restored by the regional graph model.

No asphericity or RAAG theorem is inferred from the fact that the
deleted divisors are two families of graph sections with transverse
mixed nodes. A full comparison must establish the actual based
attaching maps and their simultaneous effect on the fine kernel.
