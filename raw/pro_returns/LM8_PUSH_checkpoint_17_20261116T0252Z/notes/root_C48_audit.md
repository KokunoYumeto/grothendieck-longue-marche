# Root complete audit of the sharp outer-action depth candidate C.48

**Verdict: PASS.** Root read the entire final 217-line proof, independently
opened the precise primary relation-module construction, and checked every
comparison below. The audited draft is
`notes/pbc_solvable_outer_depth_draft.tex`, SHA-256
`64052b4435aa83d96f5616f0c77c2d928053fc21dadcc2a3fba1f8a02212617e`.
This is a structural argument. It requires no new numerical certificate.
It remains notes-only during the checkpoint16 canonical freeze.

## The exact imported compact-module statement

Root freshly opened Grunewald--Jaikin-Zapirain--Pinto--Zalesski,
*Normal Subgroups of Profinite Groups of Non-negative Deficiency*,
https://arxiv.org/pdf/0810.2027, Section2.2, printed page13, display(2.1)
and its preceding derivation. Retrievals are `turn1256view0`,
`turn1257view1` and, for the complete exact paragraph, `turn1258view0`.
The last retrieval also includes the free augmentation-ideal calculation.
The initial broad find for the equation number was not used as proof.

The source takes an arbitrary finitely generated profinite quotient and
its closed presentation kernel. Compact Shapiro and the free augmentation
resolution give the equivariant injection of the pro-p abelian relation
module into the corresponding finite free completed group-ring module.
No openness or finite generation of the kernel is assumed. In our actual
derived quotients the unchanged free abelianization forces minimal
generator number two. The candidate also supplies the resolution argument
for the stated rank-two presentation, so it does not silently require
minimality for every possible auxiliary quotient.

## Integral invariants, with the actual transition maps

The crucial measure argument is valid for a nonabelian profinite H.
For an arbitrary finite quotient D, let n be the order of y. The actual
quotient by the intersection with the p-adic abelian-coordinate kernel
embeds in D times Z/p^(k+v_p(n)). The order of y in this image is exactly
the least common multiple, namely n p^k. A left y-orbit is free on the
finite group, so each fibre over a point of its projected orbit has
exactly p^k points. An invariant integral coefficient is constant on the
upper orbit. The actual group-ring pushforward sums coefficients, hence
its value at each lower point is divisible by p^k. For the same inverse
limit element this holds for every k. Separation of Z_p forces each
coefficient to vanish, and then every finite quotient vanishes.

This proves injectivity of multiplication by y-1 in both copies of the
completed group ring. It does not assert the existence of a normalized
integral Haar measure or pass to a rational coefficient ring. Equivariance
of the relation-module injection is exactly the property needed to apply
it to conjugation invariants.

## Closed derived induction and full peripheral centralizers

The induction starts with f in F'. If its commutator with y lies in the
d-th closed derived subgroup, the preceding stage places f in
N=F^(d-1). Its class in N/N' is y-fixed. Here N' is exactly F^(d),
with the closures retained. Every pro-p factor is zero by the preceding
injection, and the product decomposition of a compact profinite abelian
group kills the entire class. The quotient F/N still has the genuine
second free abelian coordinate needed by the measure argument. This
proves rigidity for every d, and the same reasoning applies to x.

For a general centralizer element c, each integral Heisenberg pro-p
quotient is metabelian and therefore kills F'' and F^(d), for d at least
two. Its upper-right commutator coordinate detects the unwanted
abelian coordinate of c. This vanishes at every prime, hence in the
full profinite integer ring. Removing the remaining actual power x^a
puts c in F'; derived rigidity now applies. The converse is immediate.
The procyclic subgroups inject into the free abelianization, so their
exponents really lie uniquely in the full profinite integers. The proof
establishes the whole centralizer, not merely its commutator intersection.

## Literal action, outer action and multiplier

The normalized automorphism fixes x and conjugates y by f in F'.
Literal identity on the d-th derived quotient is equivalent to f
centralizing y there, hence to f lying in F^(d). If its outer class is
identity, an actual inner conjugator must centralize x and is therefore
x^a. The displayed conjugacy identity implies that f x^a centralizes y,
so it equals y^b. Abelianization reads (a,0)=(0,b), forcing both exponents
to vanish. This proves the claimed outer kernel without replacing an
outer action by a retained conjugator by assumption.

For arbitrary multiplier, the induced action on the unchanged free
abelianization is scalar multiplication by lambda. An inner action has
identity abelianization, so lambda must be exactly one. Thus the same
kernel comparison applies to the full gentle group, not only its
multiplier-one subgroup.

Root rechecked the exact C.47 conclusions in the frozen canonical text:
f in F^(4) forces Delta zero, while the actual full C.46 element has
f in F^(3) and Delta one. These are statements about actual normalized
pairs, with their full lifting proofs already audited. They supply the
upper and lower bounds after the newly proved outer-kernel comparison.
The lower witness also kills every smaller derived quotient. No finite
compatible pair is being substituted for that actual full element.

## Continuity and an actual finite characteristic detector

For a finitely generated profinite group, characteristic open subgroups
are cofinal, and the automorphism group is profinite in the resulting
topology. The inner subgroup is a compact image of the group and is
closed. Therefore the compact actual outer image receives the same
quotient topology as the full gentle group modulo its closed action
kernel. The descended parity character is continuous.

The finite-detector argument uses the product of the finite outer groups.
It does not postulate transition maps between arbitrary outer
automorphisms of nested finite quotients. If a fixed automorphism is
inner on every characteristic finite quotient, the sets of genuine
conjugators are nonempty closed subsets of the original compact group.
Intersecting finitely many quotient kernels proves their finite
intersection property and supplies one conjugator on the whole group.

Likewise, if every finite characteristic quotient admitted an actual
gentle element of parity one with trivial outer residue, the corresponding
closed subsets of the compact gentle group would have the finite
intersection property. Their intersection would be a parity-one element
in the whole outer kernel, contradicting the factorization. Thus one
finite characteristic quotient suffices. Its pullback to F is
characteristic because both the closed fourth derived subgroup and the
chosen subgroup of its quotient are characteristic.

The statement proves sharp outer derived depth four and existence of an
actual finite characteristic outer detector for the full character.
It does not give a size bound, identify the full outer image, prove that
C.47's explicit finite pair quotient already works for outer actions,
or provide an explicit all-multiplier evaluation algorithm. The final
draft preserves all these limits. The complete independent DE audit,
`notes/de_C48_audit.md`, was also read and agrees on each of these gates.

Canonical integration is approved only after the checkpoint16 freeze is
released. No canonical file or frozen claim was changed by this audit.
