## A relative disk comparison, an exact quartic quotient, and removal of the two-point cocycle

This update adds the fully audited statements C.67, D.68 and F.15.
The register now has 219 numbered statements: 188 Proved, 3 Known,
25 Refuted and 3 Open. The unresolved statements remain C.12, D.12
and F.7. Their remaining equations and extension requirements are
retained below and in the original claims.

### C.67: the actual boundary quotient and the full relative group

For a bounded simply connected plane domain O with locally connected
frontier, retain a Riemann map phi from the open disk and its actual
continuous Caratheodory extension q to the closed disk. The proof gives
an exact topological group isomorphism from homeomorphisms of the closed
disk fixing its boundary pointwise to plane homeomorphisms fixing the
complement of O pointwise. The map conjugates by phi on O and pastes
the identity on its complement. It permits multiple prime ends above
one frontier point.

The reverse construction is proved on the actual prime ends. An
ambient homeomorphism sends null crosscut chains to null crosscut
chains, with their nesting and equivalence relations, because its
map and inverse are uniformly continuous on the compact closure.
The construction retains composition and the equation q hhat=h q.
For a map fixing the frontier pointwise, its positive boundary circle
map r satisfies q r=q. The proof that r is the identity retains the
noninjective quotient q: its boundary curve has no constant open arc
by Schwarz reflection and the identity theorem. Its winding around an
interior point has degree one. For a real argument lift R and the
uniquely adjusted increasing lift P of r, the relation is R P=R.
Boundedness of R(t)-t makes every P-orbit bounded. Each complementary
interval of the fixed set has fixed endpoints; iteration toward an
endpoint and q-invariance would make q constant on an open arc.
This proves boundary-pointwise rigidity in the prime-end disk.

Compact quotient descent now proves both inverse group maps. Uniform
continuity of q proves forward continuity, for the maps and their
inverses. Both groups are closed Polish groups, and their explicit
transitive action satisfies the verified open orbit-map theorem used
in C.26 and C.30. It proves continuity of the inverse. The usual
Alexander family is written out on the closed disk, with displacement
at most twice its shrinking radius and the corresponding inverse
formula, so it contracts the entire relative group.

Every original operator stabilizing or transporting O has its actual
prime-end extension. The conjugation equation identifies the two
operator centralizers as topological groups, preserving the exact
restriction kernel. Preservation of a nontrivial operator centralizer
by the Alexander contraction remains unproved. Simultaneous extension
across infinitely many transported domains also remains an obligation.
Thus this result supplies an exact relative comparison inside C.12.

The new verified bibliography entry is Binder--Rojas--Yampolsky,
Computable Caratheodory Theory, Advances in Mathematics 265 (2014),
280--312, DOI 10.1016/j.aim.2014.07.039. The full primary preprint
arXiv:1209.6096v2 was read, especially Section 1 and Section 3.1,
printed pages 9--11, including Proposition 3.1. The author's research
page independently confirms the publication metadata. The exact
boundary rigidity and topology comparison required here are proved
in C.67. The complete root and independent C reviews are attached.

### D.68: every quartic torus representative has a specified dihedral quotient

For the actual order-four representative alpha supplied by D.46,
D.55 gives square minus identity on all primary handle homologies.
Its mod-two matrix has one nonzero invariant character chi. Extending
chi by zero on the specified order-four section gives a character of
the actual semidirect product. Every original cusp-normalizer root
above alpha has nonzero value under this character.

The proof gives all three discrete changes of free basis adapting
chi to chi(x)=1, chi(y)=0, with inverse words and the unchanged
original cusp c=[x,y]. In the double-cover kernel the Schreier basis
is x squared, y, and x y x inverse. Its rank-three homology carries
the deck involution J fixing the first basis element and exchanging
the other two. The actual inclusion into the base handle homology
has matrix with rows (2,0,0) and (0,1,1). Its kernel is the original
boundary line. This map factors through filling the two cover cusps
and the index-two inclusion of the filled torus lattices.

The cusp-root action T commutes with J and satisfies T squared=-J.
At the prime two its fourth norm is exactly 2(I-J); its image on
the boundary line contains only even multiples. The original odd
primary cusp exponent from D.55 therefore forces the nonzero
character label. The action S of the actual section satisfies S=JT.
The displayed matrix of T is uniquely determined by the base handle
matrix, the cusp multiplier and the exact inclusion matrix. Its
entries involving halves are integral for the proved parity reasons.

The anti-deck character on the cover, with values (0,1,-1), has a
kernel normal in the original full free profinite group and invariant
under alpha. Two inverse presentation maps identify that kernel with
the closed normal subgroup generated by x squared and (xy) squared.
The full quotient is Zhat semidirect C2: x maps to the reflection t,
y to the rotation r, and the retained cusp maps to r to the power -2.
The induced automorphism sends r to r to the power -lambda and t
to r to the power j times t. The equations are (1-lambda)j=0 and
j_2 odd; its exact order is two. Every odd negative quartic scalar
coordinate consequently gives an actual finite dihedral quotient
fixed pointwise by alpha. These maps impose constraints on actual
actions without supplying the unresolved scalar realizations or
excluding them.

The exact producer torus_quartic_dihedral_d68.py and independent
runs passed 147860 checks in 32 integral double-cover models,
22 scalar primary models and 1112 finite dihedral models. The
arbitrary-parameter equations are proved in the text. The source,
machine-readable output, producer stdout, root stdout and independent
audit stdout are attached. The typographical quad/qquad omissions
found in the first draft were repaired before assembly; the inclusion
map and manuscript metadata were also checked in their final form.

### F.15: the full two-point fixed subgroup and every correcting coset

Retain F.12's actual six-puncture sphere M, based pair (1,c0), and
involution r(z)=c0/z. The two-point configuration involution sends
(x,y) to (r(y),r(x)). Its based group J is the actual two-point
pushing kernel in the pure eight-point mapping class group. The
proof identifies its full completion with that ambient kernel,
using the split free-by-free Fadell--Neuwirth sequence and the two
actual completed Birman sequences. The two-track quotient is the
product of the two based Fhat5 groups. Its kernel is exactly
B=K0 intersect K2 from F.14.

Removing the two unmarked fixed points of r from M gives the
fixed-configuration map z -> (z,r(z)). Its double-cover monodromy
identifies the resulting F7 with the discrete fixed subgroup of J.
Full induced topology follows through the exact point-pushing and
prime-order normalizer maps. On the two-track quotient its map is
the graph of the filling epimorphism F7 -> F5. In the completion
the fixed subgroup is this actual Fhat7, and its intersection with B
is the kernel of that filling, the closed normal closure of the two
specified branch meridians.

The section comparison retains the original labels. Punctured
Nielsen realization and the double-cover monodromy give a pure
conjugator between any discrete order-two section and the specified
one. Independently correcting each within-pair choice retains all
eight labels. The surjective map from the pure eight-point centralizer
to the pure six-point centralizer follows by paired point motion on
M minus the two branch points. Removing its exact lift from the
conjugator gives a conjugator in J. The sections therefore have one
labelled J-conjugacy class.

For E=J semidirect C2, the proof verifies residual finiteness,
goodness, finite virtual cohomological type and the comparison for
all discrete F2[[Ehat]]-modules required by Boggi--Zalesskii Theorem A.
A finite graph-of-graphs model, finite-type resolutions and filtered
unions of finite invariant submodules provide the required module
comparison. The theorem's prime-order conjugacy and centralizer
statements then give the completed section comparison and the exact
fixed subgroup. The argument uses these proved prime-order statements
with their hypotheses checked for E.

Every B-valued involution cocycle is consequently a B-coboundary.
First correct it in Jhat; the projection of that correcting element
is in the fixed graph of the two-track quotient. Surjectivity of the
fixed Fhat7 onto that graph removes the projection and places the
correction in B. Equal coboundaries correspond exactly to left cosets
of C_B(r). The coset parametrization is a homeomorphism by compactness.
The same computation gives the exact surjective fixed-quotient sequence
from C_P8(r) to (P8/B)^r, with kernel C_B(r).

For each u in the seven-point equalizer E7, the defect
phi(u) inverse times R(phi(u)) therefore has a nonempty correcting
coset in B. The paper gives the exact centralizing coset of phi(u)
and its ambiguity C_B(r). The original curve image meets B trivially
by F.14, so it contributes at most one element to that coset. That
element is its original representative precisely for u in the full
equalizer. Proving that this full equalizer is trivial remains the
explicit F.7 obligation. No correction outside the original curve
image is asserted to solve that equation.

The primary sources Boggi--Zalesskii, arXiv:2406.08639v2,
Definitions 1.1--1.2 and Theorem A(i),(iii), and Kerckhoff (1983),
Theorem 4 and Section IV, printed pages 255--256, were reopened.
Both are existing verified bibliography entries. F.15 introduces
no finite computation used to infer a full profinite conclusion;
the existing executed F.12/F.14 certificates retain the exact
basepoint, labels, involution and forgetful formulas. The full root
audit and independent B audit are attached.
