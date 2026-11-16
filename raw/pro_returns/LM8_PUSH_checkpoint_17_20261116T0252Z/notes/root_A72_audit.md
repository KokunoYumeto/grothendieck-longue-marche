# Root full proof audit of A.72

**PASS.** Root read the complete 332-line draft, every line of its supporting
certificate, and the exact internal comparisons used in the proof. The draft
SHA-256 is `9cc005920ae12725c780277742fa25c9000e03004e8c1930dc7a3dfc1d9d0226`.
The independent execution ran the entire mathematical body, removing only the
author-owned output writes. Its whole JSON is byte-identical to the author's:
`c07aed6569b4050c180fafeb1f40d8faed49944080386fdae32727ebdeff35a4`.
The source hash and actual duration are in
`root_A72_certificate_verification.json`. The eight finite checks range from
n=2 to n=256. They support the formulas; the written proof establishes the
unbounded statement.

## Actual inertia, central quotient and Jacobian factor

The group is the generalized quaternion group of order 4n, n a power of two
at least two, with rotation r of order 2n and s squared equal to r^n. Every
generating pair has commutator r to twice an odd exponent. The actual
punctured-elliptic peripheral word therefore has inertia I=<r^2>, of order n,
with four actual cusps and proper genus 2n-1. This is not an identification
made only after passage to a convenient quotient. Squares and commutators
give exactly I as the Frattini subgroup.

The central involution sigma=r^n has actual dihedral quotient of order 2n.
For n=2 the quotient is the unramified V4 elliptic isogeny; its Jacobian has
the same supersingular reduction as the original base. For n at least four,
A.70 supplies the exhaustive classification of actual dihedral covers and
A.44/A.69 supply their good, special-rank-zero Jacobians. Actual pullback and
norm isolate the anti-invariant factor A of dimension n.

The nilpotent ramified-cover theorem, Lehr--Matignon Theorem 6.13, applies to
the actual quaternion cover: good base, one étale branch section, and tame
generic characteristic zero. Root had freshly opened the readable author
version at https://arxiv.org/pdf/math/0411059, exact printed page 21, and
checked that the hypothesis is nilpotent, not merely a p-group. Only its
good-Jacobian/tree conclusion is used here. No stronger marked-fibre or
special-rank conclusion is taken from that source.

On A, r^n=-1, so the irreducible polynomial x^n+1 gives a unital field
injection Q(zeta_(2n)) into End^0(A). This is an actual deck endomorphism.
The endomorphism extends on the good abelian scheme. On a nonzero special
étale 2-divisible Tate space its local field action is unital and hence
faithful; that local field has degree n. The dimension of the Tate space is
therefore either zero or n. Thus the only alternatives are rank zero and
ordinary, without inferring a slope from a characteristic-zero dimension
alone.

## Componentwise ordinary alternative

The good special Jacobian is the product of the positive-genus component
Jacobians of the compact-type model. A pair exchanged by sigma has invariant
and anti-invariant factors isogenous to the same positive-dimensional
Jacobian. The former must have rank zero and the latter be ordinary, so
such a pair is impossible. Sigma-trivial components remain in the old
factor and supply no anti-invariant dimension.

For a sigma-stable component with nontrivial involution, its quotient has
rank zero. Smooth-curve Deuring--Shafarevich gives f(B)=r_B-1 and forces at
least one fixed point. Riemann--Hurwitz gives Prym dimension
g(B')-1+sum(d_P)/2, with d_P at least two. A zero Prym forces both genera
zero. A positive ordinary Prym forces g(B')=0 and all d_P=2; the whole
component Jacobian is then ordinary and anti-invariant. Their genera sum
to n. Root checked the componentwise use against Crew Corollary 1.8 and
Yang Proposition 1.4 already opened in the A.69 audit, without importing
an unrestricted marked-fibre claim.

For an ordinary curve under a finite 2-group, subtracting twice
Deuring--Shafarevich from Riemann--Hurwitz forces all the nonnegative
different excesses to vanish. The classical lower different formula then
gives G_2=1; the first lower quotient is an additive subgroup of the residue
field. Consequently an inertia group cannot contain an element of order
four. Root checked the cited Bouw--Wewers Section 2.2, equation (3), and
Exercise 2.12(c) in the previous full source audit.

If an order-four automorphism a had square sigma, its action on the
genus-zero quotient would be a nontrivial involution. It has one fixed
point in characteristic two. The fibre above that point cannot be
unramified: a permutation on two points has trivial square, whereas sigma
exchanges them. Thus a fixes the unique ramified point, contradicting the
ordinary inertia calculation. This checks the precise fourth-root
obstruction, including the action on the quotient.

## Quaternion stabilizer contradiction

The stabilizer of a positive anti-invariant component contains sigma.
Every nontrivial subgroup of a generalized quaternion group contains its
unique involution sigma. Hence the kernel of its action on this component
is trivial. If the stabilizer were larger than <sigma>, it would contain
an element of order four whose square is sigma, which has just been
excluded. Thus the component has an orbit of 2n positive anti-invariant
components. Their genera would exceed the available anti-dimension n.
This contradiction excludes the ordinary alternative for every n. The
argument does not require a blanket assertion that every group action on
the entire special fibre is faithful.

## Actual cusp functions and arithmetic transfer

The actual quotient C/I is an unramified V4 elliptic isogeny E' to E.
After choosing an origin above O its kernel is E'[2]. The map C to E' has
degree n and is totally ramified at each of its four cusp points, so
h^*Q_i=nP_i. Actual rational functions with divisor 2(Q_i-Q_j) pull back
to functions with divisor 2n(P_i-P_j).

Every proper intermediate has at least two cusps because I is Frattini,
and has positive genus because it maps nonconstantly to E. The actual
Jacobian norm is surjective up to isogeny, preserving potential good
reduction and special rank zero. Norms of the actual cusp functions kill
every intermediate cusp difference by 2n. The pushforward of a geometric
point has coefficient one, irrespective of the ramification index; this
is the needed direction of the divisor comparison.

The rank-zero special abelian variety has no nonzero geometric 2-power
torsion. A.41 therefore gives the exact rational companion paths; A.42
includes the coefficient prime two; A.59 gives the normalizer assertion
for the actual nilpotent closure. All finite definition extensions concern
curves, maps, automorphisms, endomorphisms, subgroups and marks. Arbitrary
profinite base-point paths are compared only up to geometric inner
conjugacy, and the previously proved restriction comparison transfers the
stated packets and permitted open derived groups. No fixed-subgroup
surjectivity from a quotient is asserted.

Root approved canonical integration after the independent execution
passed. The universal A.45 remains open; this is an exhaustive theorem
for the stated family of actual geometric Galois closures.
