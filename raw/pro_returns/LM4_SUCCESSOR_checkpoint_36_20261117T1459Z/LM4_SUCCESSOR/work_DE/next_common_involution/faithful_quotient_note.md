# A faithful eight-point ambient quotient

Research note, 16 November 2026, after B71. This is a fully typed next setup,
not a claim that the actual residual centralizer is trivial. No new formal
statement is requested from this note.

## 1. The group and its topology

Let r be the actual common involution of B65, and put C=C_P(r), where
P=PΓ_0,12. The twelve original marks form six free r-orbits; the two fixed
points of r were unmarked. The quotient sphere has six labelled ordinary
marks and an unordered pair of branch marks. Let Q be its mapping-class
group, fixing each ordinary label and preserving the branch pair.

The regular branched-cover normalizer comparison identifies the centralizer
of r preserving its six orbits, modulo <r>, with Q. Every element of Q lifts:
the double covering is the one whose mod-two monodromy is one at each branch
mark and zero at each ordinary mark, and this character is preserved by Q.
Its lifts differ exactly by r.

The permutation of the two sheets above the six labelled ordinary marks
gives a homomorphism

    Q -> (C2)^6 / <(1,1,1,1,1,1)>.

It is well-defined because changing the lift changes every sheet bit.
Moving a single ordinary mark once around a branch mark realizes its single
sheet flip, so this map is onto. Its kernel L has index32 in Q. An element
of L has exactly one lift fixing all twelve original labels; thus C≅L.

The prime-power centralizer comparison and full-topology argument used in
B30 apply to <r>. Consequently the actual embedded closure of C in P-hat
is its full completion. Since L has finite index in Q, its full completion
also embeds as the corresponding open subgroup in Q-hat. Thus the map

    C_(P-hat)(r) ≅ L-hat -> Q-hat

is faithful. It sends the actual two completed source groups to subgroups
in one smaller ambient group and preserves their intersection. Unlike the
rigid forgettings, this operation itself loses no element of K. A further
forgetting or representation of Q still needs its own kernel analysis.

## 2. Exact cyclic family

In B65's coordinates, r_u(z)=u/z. The invariant quotient coordinate is
t=z+u/z. The poles 0,∞ give the ordinary mark ∞. The other five ordinary
marks, indexed by the pairs X_i,Y_-i, are

    t_i(u)=ζ^i+u ζ^-i,  i=0,...,4.

The branch marks are ±2sqrt(u), unordered. This defines the Q-valued
monodromy without choosing a square root. A loop around u=0 interchanges
the branch marks, so it is not legitimate to regard the whole H5 source
as lying in the pure eight-point group.

After the double cover u=s² the branch labels are ordered. Normalize
-2s, +2s, ∞ to 0,∞,1. The five remaining coordinates become exactly

    x_i(s)=((s+ζ^i)/(s-ζ^i))².

The parameter sphere is punctured at 0,∞ and μ_10. This is the actual
index-two source, of rank11, rather than the original rank-six source.
The based marking at the icosahedral point is obtained by the quotient
of the same B61/B65 common marking. The algebraic coordinate formulas
alone do not choose new free meridian words or a new ambient conjugator.

If the branch pair is forgotten, the six ordinary marks extend across
u=0 and u=∞: at infinity divide all finite coordinates by u. Hence this
further map factors through P1\μ5. It has lost two source punctures and
cannot itself be a faithful replacement for the complete eight-point map.

The five finite ordinary marks satisfy the Dickson polynomial identity

    ∏(t-t_i(u)) = t^5-5u t^3+5u² t-(1+u^5).

This suggests a connection to the I2(5) folding into A4 and the regular
pentagon curve. No based monodromy identification, full induced profinite
topology for that folding, or resulting separability theorem has been
proved here; none is used in the faithful eight-point assertion above.

## 3. Exact tetrahedral family and a rejected shortcut

Conjugate the common involution within the fixed tetrahedral coordinates
to z↦-z. Its quotient coordinate is z², and its branch marks are0,∞.
Six representatives of its pairs in the tetrahedral orbit are

    u, 1/u, (u+i)/(u-i), (u-i)/(u+i),
    (u+1)/(-iu+i), (u-1)/(iu+i).

Divide the squares of these functions by u², making the first ordinary
point1 while the branch points remain0,∞. The remaining five rational
functions are the usual coordinates on M0,8. Taking exact divisor orders
at B58's thirteen finite exceptional points gives a20-by13 integral H1
matrix. The source meridians are exactly those of the earlier H1
certificate; no numerical continuation is used.

Fresh code and actual standard output are

* check_tetrahedral_branch_h1.py
* check_tetrahedral_branch_h1.out
* tetrahedral_branch_h1.json

The eight-point matrix has rational rank9, compared with rank6 before
marking these branch points. It has rank3 on the old seven-dimensional
source homology kernel. This initially looks stronger, but the whole
cyclic source has unordered branch marks. Swapping0 and∞ sends each
normalized coordinate x to1/x. On ordinary differences its winding
covector is the original difference minus the two individual windings.

The code implements that involution exactly. The invariant/coinvariant
projection has source rank6 and is zero on the entire old source kernel;
the three new directions are all anti-invariant. Therefore one cannot
deduce that those three coordinates vanish on K just because K has zero
abelianization in the original rank-six cyclic source. Commutators in
that source may have nonzero homology after passage to its index-two
subgroup. This computation is preserved as a failed shortcut, not a new
refinement theorem.

## 4. Full ambient question retained

We still need a finite-cover or subgroup-intersection argument in the
faithful eight-point ambient group, or an independent equivalent full
ambient argument. The known source embeddings, the elementary index32
calculation, and the computed branch homology do not prove that its two
completed source subgroups have trivial intersection. B71 already shows
that the joint full rigid and full3-adic image can remain nontrivial.

## 5. A decorated seven-point target that is faithful on the cyclic source

There is a useful further reduction, different from forgetting the branch
marks. First forget the two D-fixed poles in the original twelve-point
sphere. The centralizer comparison is unchanged discretely: an
orientation-preserving representative commuting with the order-five
rotation preserves its two fixed points individually, distinguished by
their local rotation residues +1 and -1 modulo5. Marking those fixed
points recovers the inverse comparison. The quotient-cover description
still has the same four distinguished orbifold points and the same
u↦u^5 parameter cover. Thus the pure C5 centralizers on twelve and ten
marked points are isomorphic through this forgetting map.

For the topological comparison, use the valid prime-power full induced
topology and density on both mapping-class groups. Their completed
centralizers are the completions of that same free rank-six group.
The restricted forgetting homomorphism is therefore injective on the
actual completed H5, not only on its discrete dense subgroup.

Now take the common-involution quotient on the ten remaining marks.
It has five labelled ordinary marks and two unordered branch marks.
The same sheet argument gives an index16 subgroup of this colored
seven-point mapping-class group. The valid C2 topology theorem again
makes this a faithful completed comparison. Consequently the composite
decorated seven-point map is faithful on H5 and H5-hat.

This does not conflict with B69: the target retains the two r-ramification
marks, which are not among the original twelve punctures and were absent
from every original rigid forgetting. In the explicit family it is the
eight-point target above with its ordinary mark∞ removed, while retaining
both ±2sqrt(u). On the index-two cover u=s² its four variable coordinates,
after normalizing the two branch marks and the i=0 ordinary mark, are

    ((s+ζ^i)(s-1)/((s-ζ^i)(s+1)))²,  i=1,...,4.

The tetrahedral source also maps to this target, because it centralizes r
and the two forgotten poles are an r-orbit. No faithful comparison on
that tetrahedral restriction has been established. A common image of
the two source groups in this seven-point group need not have equal
preimages upstairs. Thus the construction gives an injective test on K
through its cyclic embedding, but no equality between K and an
unqualified intersection of the two seven-point images.
