# Root full proof and certificate audit of A.73

**PASS.** Root read the entire 324-line final draft, SHA-256
`24e5ba673c1a3d9a2bbe8fcd64a83e2781a418fc0ef39f584c371198ab87ac4a`,
and every line of its supporting code. The independent execution ran
the entire mathematical body while removing only the owner's final file
write and print. Its whole JSON is byte-identical, SHA-256
`a02ae27a1a780c077950511d8e453a93a809190837e6100e180f6b8df5df1370`.
The exact source, duration and seven levels n=4 through 256 are recorded
in `root_A73_certificate_verification.json`. The universal geometry is
proved in the text, not inferred from those samples.

## Exact group and old factor

The semidihedral presentation has r of order 2n, s of order two, and
conjugation exponent n-1, for n a power of two at least four. The pair
generation criteria and explicit commutator formulas imply that the
actual peripheral inertia is <r^2>, order n. It is normal and Frattini,
so there are four cusps and genus 2n-1. The actual central quotient by
sigma=r^n has the dihedral group of order 2n and genus n-1. A.70,
A.44 and A.69 therefore apply to this actual quotient, not merely to an
isogenous substitute. The nilpotent ramified-cover theorem supplies
potential good Jacobian reduction and a compact-type tree for C.

The anti-invariant factor has dimension n and the actual rotation gives
the same unital Q(zeta_(2n)) action as in A.72. The local field degree n
forces special 2-rank either zero or n. Under the ordinary alternative,
the componentwise pullback/norm, Deuring--Shafarevich and Riemann--Hurwitz
calculation has exactly the scope checked in A.72: exchanged positive
components are impossible, sigma-trivial components remain old, and
each positive anti-component is ordinary with genus-zero sigma quotient.
The total of their genera is n. The ordinary fourth-root obstruction
is repeated explicitly, with the correct lower-ramification argument.

## Stabilizers do not assume faithful specialization

For a positive anti-component B, sigma acts nontrivially. A rotation
outside {1,sigma} has a power whose square is sigma and whose order is
four. If it stabilized B, its action on B would have order four,
regardless of any other kernel of the stabilizer action. The same holds
for every outside element r^a s with a odd, whose square is sigma.
Thus the rotation intersection of the stabilizer is exactly <sigma>,
and the whole stabilizer has order at most four. This is valid without
claiming that the full semidihedral stabilizer is faithful.

Every orbit of positive anti-components consequently has at least n
members. Since their total genus is n, there is one full G-orbit of
exactly n ordinary elliptic components, each with stabilizer order four.
The inertia element mu=r^2 has orbit size n/2 on every such component;
this is nontrivial even at n=4. It fixes each of the four generic cusps
individually because it belongs to the normal inertia subgroup.

## Local lifting and the full-group centre

Each of the ordinary elliptic components has exactly two sigma-fixed
points. Neither can be smooth on the whole special fibre. At a smooth
fixed point the local action on R[[t]] is nontrivial modulo the
uniformizer and fixes R. Thus sigma(t)-t has positive finite order
modulo the uniformizer and no vertical factor. Weierstrass preparation
gives a nonempty finite flat horizontal fixed locus. Its generic point
belongs to the actual generic fixed scheme, which is contained in the
cusps because the actual cover is étale elsewhere. Properness then
specializes an individually mu-fixed cusp to the alleged smooth point
on a component moved by mu, a contradiction. The argument does not
apply this assertion to nodes or to components with trivial sigma.

The root must be fixed by the whole G. Root identified this essential
point during draft development: a root fixed merely by mu would not
put its two elliptic orbits at the same depth. The final proof uses the
canonical centre of the entire finite tree. If it is an edge, its
midpoint is an abstract barycentric root; no model is altered. Thus all
n elliptic vertices in the one G-orbit are equidistant at positive
depth. The sigma-fixed root-to-vertex path supplies one fixed parent
node, and the other fixed node leads to a child subtree.

These child subtrees have no elliptic vertex from that orbit because
their depth is larger. They contain no marked cusp: mu fixes the root
and every cusp vertex, hence fixes each root-to-cusp path pointwise,
whereas it moves the elliptic attachment vertex. Each child subtree
is nonempty, unmarked and attached at one point. If all its v vertices
were rational, their total full-graph valence would be 2v-1, contradicting
the stable lower bound 3v. Each therefore contains positive genus.
The n subtrees are pairwise disjoint because their attachment vertices
have the same depth. The n elliptic genera and n additional positive
genera give at least 2n, contradicting genus 2n-1. The abstract centre
cannot introduce an unstable geometric vertex in any child subtree,
since it is the root outside them.

## Cusps, intermediates and arithmetic comparison

The actual quotient C/<r^2> is an unramified elliptic V4 isogeny.
Its kernel is E'[2], and C to E' has total ramification degree n at
each of the four kernel points. Pulling back the actual functions with
divisor 2(Q_i-Q_j) kills cusp differences by 2n. The Frattini argument
gives at least two cusps on every proper intermediate, whose genus is
positive because it maps to E. Actual norm maps preserve potential
good reduction and rank zero and push those principal divisors with
coefficient one on geometric points.

A.41 then supplies the rational companion paths, A.42 includes all
coefficient primes including two, and A.59 supplies normalizers for
the actual two-group closure. Finite extensions define only algebraic
data and reduction; arbitrary profinite paths are handled up to inner
conjugacy. The existing restriction comparisons transfer the original
packets and permitted open derived groups. The proof therefore closes
the stated semidihedral family while leaving the universal A.45 open.

All primary inputs were already opened and checked in root's A.69,
A.70--A.72 audits: Lehr--Matignon Theorem 6.13, Crew Corollary 1.8,
Yang Proposition 1.4, Bouw--Wewers Section 2.2 and Vonk Corollary 2.16.
No extra theorem is inferred from their titles. The last is used with
its explicit uniformizer-power factor, which the nonzero reduction
sets to zero. Canonical integration was approved after this full proof
review and the independent certificate execution passed.
