# E.119 — independent proof, source and marked-map audit

**Verdict: PASS. No correction requested.**

Reviewer: `/root/d_galois`. The frozen proof reviewed is
`research_e119/sections/E_lower_fiftythree.tex`, SHA-256
`25d9250dabab99ca3848525d608ed6968323cdc58400f75b8d074a90d79759c0`.
Its manifest has SHA-256
`79d424d7f19195b64260847b54544206615d0ed4c3f1011e8f88dc4392d6831d`.
All 191 manifest entries were checked against both their byte counts and hashes.
No frozen author file was modified.

## Scope of this independent review

I read all 745 proof lines, all eight owned GP programs, both dependency GP
programs, the complete Python checker, and the source/computation ledgers.
The ten GP sources contain 453 lines in total. I independently opened the
primary sources listed below, including the relevant proofs and the PARI
certification contract.

I wrote and executed `code/d_e119_maps.py`. It uses the frozen literal output
tables as input, then reconstructs the horizontal finite group and transfer,
the ordinary-to-S-class map, universal integral unit basis changes, and both
idele quotients using canonical HNF representatives. Its actual execution
returned exit status zero. The complete stdout and JSON are retained beside
the source. This is an independent finite-map verification, not a second
execution of the ten GP stages. Root separately performed the source-only
ten-stage arithmetic reconstruction and full decoded-object comparisons.

## The lower class group and its actual field maps

The proof of the complete group `A(B1)` does not use the uncompleted upper
BNF certification. The certified cyclotomic base has class number one.
The displayed local characters give the actual genus quotient. At a prime
over 53, total ramification in the cubic lower extension and complete
splitting in its S-Hilbert class field provide a decomposition subgroup
mapping isomorphically to that cubic Galois group. Consequently the kernel
in the abelianized extension is exactly the class-group coinvariant, with
the displayed genus-coordinate map.

For the real fixed field, `bnfcertify(...,1)` supplies only the stated
natural class-group upper quotient. The five literal prime relations kill
that upper quotient after S-localization. The resulting `A(R)=0` gives
`1+c=0` on `A(B1)` through the actual quadratic norm/extension maps.
The relation `cgc=g^{-1}`, together with scalar action by `c=-1`, gives
`g=g^{-1}`; since `g^3=1`, the cubic action is the identity. This identifies
the entire class group with the already computed coinvariant.

I checked the Kummer field and marking: the three displayed radicals have
product 53, are real, and are cycled by `xi -> xi^4`. Their prime valuation
matrix has determinant a unit. The retained Hensel element has error and
derivative valuations 13 and 6. The local cube conditions therefore give
the actual S-split extension of degree nine over `B1`, equal to its full
S-Hilbert class field by the established class number.

The independent verifier constructs all 27 elements of the marked
semidirect-product subgroup and checks all 729 products. It computes group
transfer from every one of the 81 right-coset factors, instead of using only
the value on a chosen generator. Its restriction to the Kummer phase plane
and its transfer are precisely

\[
N(e_0,e_1)=(0,e_0+2e_1),\qquad j(a,b)=(a,a).
\]

The actual residue primes calibrate the horizontal Artin coordinate as
`2a`. The chosen auxiliary abelian coordinates in the verifier put the
displayed lift `tau` at `(2,0)`; the restriction and transfer are unchanged
by the available shear in its second coordinate. No unrecorded identification
of a full field representation is inferred from that auxiliary choice.

The reciprocity directions in the proof are correct. In Tate degree minus
two, restriction is group transfer and corestriction is induced by subgroup
inclusion. In degree zero the corresponding field operations are inclusion
and norm. The compatibility with the fundamental class gives the two
commuting squares used here, and the product of local maps gives the global
ideal maps. The proof supplies this argument rather than relying on the
unfinished proof notice after Milne III, Lemma 3.2.

## Unit completeness, principal divisors and exact inverse coordinates

Every candidate is used as a literal algebraic element. In particular,
`e53_local_genus_maps.gp` checks each of all fifteen entire principal ideals
against the product of its six recorded S-prime powers. The class and
S-prime relations in both transition programs are likewise checked as
full ideal equalities. The candidate upper BNF supplies these elements and
ideals, not an assumed class number or complete unit lattice.

The explicit outside-S Hilbert 90 maps in (E119.16) are inverse: an S-unit
cocycle gives a principal extended outside-S divisor, and such a divisor
gives its unit cocycle. Absence of ramification outside S makes every
invariant outside-S divisor an extended divisor. This gives the actual
capitulation group as H1. Applied to the horizontal extension over `M`,
the vanishing lower three-class group and the S-unit Herbrand quotient
give norm index nine. The actual norm columns have the same index, so their
image is the full image.

Normalized valuations are preserved at the relevant ramified 3-primes
because their relative residue degree is one. The three valuation
coordinates are therefore congruent modulo three. The listed units realize
the entire resulting lattice; its index is nine. The independent HNF check
recovers exactly that lattice. The nine ordinary-unit residue characters
have determinant minus 17, hence give a basis modulo cubes of the full
ordinary unit group. Its rank and its torsion `mu_9` are independently
determined. This proves the completed S-unit basis.

The peer verifier replaces finite sample checks of inverse coordinates by
universal integral matrix identities. For the norm to `M` it constructs a
unimodular 15-by-15 source basis carrying the norm to the displayed index-nine
target basis plus eight zero columns. For the norm to `L1` it constructs a
unimodular source basis carrying the norm to the identity target matrix plus
ten zero columns. Both basis changes preserve the first source coordinate,
whose relation is `9e_0`. Its norm has relation `3e_0`. Thus the two full
kernels have the stated free ranks and a `C3` torsion summand, with actual
forward and inverse coordinates. Taking the representative in `{0,1,2}`
has precisely the stated carry in the torsion kernel.

The ordinary three-class group is also justified without assuming the
candidate group: the principal S-divisor lattice gives an S-prime subgroup
of order nine and the S-class quotient has order nine. The actual generator
relations and S-prime expressions then generate all 81 classes. The peer
verifier enumerates this entire group and verifies that the subgroup
generated by the actual S-prime columns equals the kernel of the genus map.

## The two vertical coinvariants, norm and projected extension

The local uniformizers and embeddings in the proof retain the actual
generator `sigma(beta_2)=zeta beta_2`. At the wild primes the local extension
is the indicated cyclotomic extension; the normalization by `beta_1+1`
removes valuation and the remaining cyclotomic character has the stated
minus sign and denominator nine. At the tame primes the normalized cubic
residue character has the same chosen arithmetic reciprocity convention.
Every S-place is totally ramified in the relevant vertical extension.
The complete character matrix has rank two over the `B1` base, and the
positional lower S-units have zero local characters. The cyclic Hasse norm
theorem gives the field-norm indices nine and one respectively.

The idele presentations retain both sorts of principal relation. A class
generator power contributes its local character with the class-power
relation; an S-prime expression contributes the opposite local character
with its actual class coordinates. I checked these signs and all actual
source/target maps. The restriction row kills every relation.

An S-prime decomposition group splits the extension of the upper S-Hilbert
class field by the cubic Galois group. Its abelianization therefore has
kernel exactly `A(B2)_sigma`, respectively `A(L2)_sigma`. This proves why
the computed idele kernels are precisely the two claimed coinvariants.
The proof does not identify them with the full upper class groups.

The peer computation works in the full HNF residue boxes of orders 729
and 81. It verifies every restriction fibre, enumerates the 243- and
27-element kernels, and checks all forward/backward Smith maps against
those canonical representatives. The maps to the lower class groups are
computed from the original ideal-coordinate projections. All nine norm
fibres have the claimed sizes. It checks 6,561 and 324 generator-map
identities in the respective full idele groups.

The projected extension is three times an actual ideal lift. Changing
that lift by a local Artin generator leaves the triple unchanged, and
this is checked in the full HNF group for every lower class. The
norm/extension composites are checked for every element of both
coinvariant groups. In the published coordinates the resulting maps are

\[
\begin{aligned}
N_B(x_0,x_1,x_2,x_3)&=(2x_3,x_0+2x_3),&
\bar j_B(a,b)&=(6a+3b,0,0,0),\\
N_L(x,y)&=(-x,-x+y),&
\bar j_L(a,b)&=(6a,0).
\end{aligned}
\]

The actual capitulation subgroups are correctly retained as subgroups of
the kernels of these projected maps. The proof does not assert equality.
The outside-S H1 identification, the two Herbrand quotients and the
local-global field-norm indices then give exactly the stated unit-norm
index and defect formulas. Tensoring with `Z3` preserves the relevant
finite-group cohomology and finite indices here because the unit groups
are finitely generated and `Z3` is flat over `Z`.

## Primary-source checks

I independently opened [Milne, Class Field Theory](https://www.jmilne.org/math/CourseNotes/CFT.pdf):
III, Lemma 2.7 and Theorem 3.1 with their proofs; V, Proposition 3.3,
Proposition 5.2 and Theorems 5.3/5.5; VII, Proposition 3.1 including its
lattice proof and the reciprocity/existence proofs in sections 8–9;
VIII, Theorem 3.1 including its cohomological proof. These cover the exact
norm/transfer, S-unit quotient, reciprocity and local-global inputs used
above. The missing proof notice after III, Lemma 3.2 does not enter the
argument.

I also opened [Lemmermeyer, Ambiguous Class Numbers](https://arxiv.org/pdf/1309.1071),
Proposition 1 and its full ideal/Hilbert 90 proof. Its surjectivity paragraph
prints `Am_st` where the preceding construction gives an ambiguous class.
E119's explicit outside-S inverse maps provide the needed assertion
directly, so that printed label is not used.

The [official PARI documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html)
states the full flag-zero certification contract, the weaker class-quotient
contract with flag one, and the meaning of factored principal elements.
The proof and programs respect those contracts.

## Retained scope

The complete lower class/unit maps and the two marked vertical coinvariants
are established. The kernels `(sigma-1)A(B2)` and `(sigma-1)A(L2)`, and the
actual upper capitulation subgroups inside the displayed bounds, remain
unevaluated. The audit records no stronger result and no higher-stage
stability. The frozen E119 proof and certificates pass this independent
review unchanged.
