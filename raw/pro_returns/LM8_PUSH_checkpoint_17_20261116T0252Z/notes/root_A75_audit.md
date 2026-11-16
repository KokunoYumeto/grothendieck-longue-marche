# Root full audit of the modular two-group candidate A.75

**PASS for the complete written proof and the independently executed finite
certificate.** The candidate remains outside the frozen checkpoint15 paper;
canonical integration is deferred until after its scheduled save. Root read
the entire draft and certificate source, not only the statement or an audit
summary. The exact draft hash is
`e287d5c6b92735b189199a6579b3c4b80ae86e585ec750162fe65dad48e0927f`.

## Actual cover and algebraic comparisons

The generating-pair computation uses the actual modular presentation with
cyclic subgroup of order2n, n a power of two at least4. Both types of
generating pair have commutator r^n. Thus the actual cover has central
inertia I of order2, exactly2n cusps, and proper genus n+1. Quotienting the
actual curve by I gives an unramified elliptic isogeny with kernel
C_n times C_2. This identifies the quotient and its supersingular reduction;
no cover is substituted merely because it has the same abstract group.
The Frattini calculation gives I contained in Phi(G), not equality. It
therefore supplies at least two cusps in every proper intermediate.

Pullback and norm identify the invariant factor with that elliptic quotient
and the anti-invariant factor with an n-dimensional abelian variety. The
relation r^n=-1 and irreducibility of X^n+1 give a unital cyclotomic field
action. At two the field degree is n, so the special etale Tate dimension
is either zero or n. Potential good reduction is supplied by the actual
nilpotent ramified-cover theorem; the generic characteristic-zero inertia
is tame and the sole branch section does not coalesce.

## Ordinary alternative and stabilizers

The component argument accounts for all three possibilities under the
central involution. Exchanged positive-genus components would contribute
isogenous invariant and anti-invariant factors, which cannot be both
supersingular and ordinary. A component with nontrivial involution has
quotient of special rank zero. Subtracting the smooth-curve
Deuring--Shafarevich and Riemann--Hurwitz equations forces its quotient
genus to be zero and its entire positive-genus Jacobian to be ordinary
and anti-invariant. Pointwise fixed components supply the remaining
invariant genus one.

The fourth-root obstruction is applied to the faithful image of the
cyclic order-four subgroup. It does not assume that the entire component
stabilizer acts faithfully. Ordinary weak ramification makes every wild
point stabilizer elementary abelian; an order-four automorphism whose
square is sigma would have a fixed point above the unique fixed point
of its induced involution on the rational quotient. An unramified
two-point fibre cannot realize that square action. This is the required
contradiction.

Every rotation except1 and sigma, and every outside element except the
two outside involutions, has a power of order four with square sigma.
Consequently the component stabilizer is contained in the actual V4
subgroup H0. The orbit/genus bound forces one orbit of n ordinary
elliptic components. There is then precisely one invariant supersingular
elliptic component B0, fixed by the whole group. Rooting the actual tree
at B0 puts all ordinary elliptic vertices at the same positive depth and
gives each stabilizer a fixed parent node.

## The outside-inertia fixed-locus step

This is the decisive correction to the earlier marked-tail obstruction.
A faithful V4 action on an ordinary elliptic curve cannot have a common
fixed point: the p-rank formula would require total ramification
contribution4, whereas the fixed point contributes3 and further orbits
contribute2 or3. Thus the H0 action has a kernel of order2 outside I.
The other outside involution acts as sigma on the component but has no
generic fixed point anywhere on the actual proper curve, since every
generic stabilizer is trivial or I.

At a smooth special fixed point, the local difference series of this
outside involution has nonzero reduction and positive finite vanishing
order. In the complete smooth chart it therefore has uniformizer exponent
zero in Weierstrass preparation and a distinguished factor of positive
degree. Its roots give a nonempty horizontal fixed locus and, after a
finite extension, a genuine generic fixed point. The coefficient ring is
fixed because the deck action was defined over the chosen finite base.
The formal-disc point belongs to the actual proper curve by the smooth
formal chart and properness. This contradicts generic fixed-point-freeness.

The argument must be made on the proper **unmarked** stable model. It
cannot be replaced by a statement about cusp marks on exceptional tails.
Both sigma-fixed points of each ordinary elliptic component are therefore
nodes on that proper model. One is the parent node; the other starts a
nonempty descendant subtree. It contains neither B0 nor another ordinary
elliptic component, because all the latter have the same depth. A finite
rational-only subtree with one attachment has total valence2v-1, whereas
unmarked stability requires at least3v. This contradiction excludes the
ordinary alternative for every n.

## Intermediates and final scope

The actual elliptic kernel has exponent n. Pulling its principal
n-torsion point-difference divisors back through the actual degree-two
map kills all cusp differences by2n. At each intermediate the actual
norm is an isogeny quotient on Jacobians and pushes an algebraically
closed point with coefficient one. Hence good reduction, special rank
zero and the required cusp torsion transfer in the stated direction.
The Frattini inclusion supplies the distinct companion needed by A.41.
A.41, A.42 and A.59 then apply at their already checked scopes, including
coefficient prime two, every induced packet and permitted open derived
subgroup. The original elliptic base is handled separately. No claim of
cofinality among all finite covers or of a solution to A.45 is made.

## Source and execution record

Root freshly reopened the primary sources at the exact uses:

- Lehr--Matignon, Theorem6.13, printed21/PDF20, in
  <https://arxiv.org/pdf/math/0411059>, retrieval references
  `turn1197view0`, `turn1198view0`: nilpotent cover, smooth base,
  noncoalescing branch locus and generic tameness give tree-like reduction.
- Crew, Corollary1.8, printed35--36, in
  <https://www.numdam.org/item/CM_1984__52_1_31_0.pdf>, references
  `turn1197view1`, `turn1198view1`, `turn1199view0`: smooth proper
  component curves and finite p-group ramification. The exact formula was
  already read in the preceding A.69--A.73 audits and is rederived here
  in both involution and V4 uses.
- Vonk, Corollary2.16 and its proof, printed23/PDF22, in
  <https://pub.math.leidenuniv.nl/~vonkjb/teaching/2021_topics/Topics.pdf>,
  references `turn1197view2`, `turn1198view2`: the uniformizer factor is
  explicitly checked to be absent before obtaining generic roots.

The earlier primary different/first-ramification checks are retained in
the A.73 source record; the needed fourth-root consequence is proved
again in the candidate. No priority or exhaustive novelty claim is made.

Root executed the entire read source using
`code/root_A75_certificate_rerun.py`. All seven levels n=4 through256,
their subgroup and cusp-permutation calculations,100 V4 constraints and
100 tree constraints passed. The whole JSON is byte-identical to the
author's output, SHA-256
`53f9818b2b2df0e62bf8ae7136ed4799abc56b9f336957506c814e0456341dda`.
The source hash is
`39f234545f081f9ed234393c65adad6eaf71b60fc5d05252abd4622c407bf61f`.
These finite checks support the written uniform proof; they are not its
replacement. DE independently read the complete proof, reopened sources
and reran the whole certificate with the same result.
