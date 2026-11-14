# Independent root review of the two-prime primitive-Prym criterion

Date:14November2026, approximately12:51UTC.

Reviewed every step of audit/A_two_prime_prym_candidate.md, including
the nonordinary genus-two scope, the separate elementary proof of the
two-rank bound, and the prime-power comparison with integrated A.C2.8.
Verdict: approved for integration as A.C2.17. This is a sufficient
criterion and does not prove that every genus-two curve has the required
theta torsion.

## 1. The degree-four exclusion is valid in characteristic two

Let D have genus n+1, n odd and at least15, with a free cyclic group
of order n. A group-invariant pencil of degree less than n is
impossible: the induced cyclic action on P1 has a fixed point (or is
trivial), and the corresponding fibre is an invariant effective
divisor whose degree is a multiple of n. This uses multiplicities,
so a ramified fibre causes no exception. Hyperellipticity gives just
such an invariant pencil. Two distinct degree-three rational
subfields have compositum equal to k(D), so Castelnuovo–Severi gives
genus at most4; hence a trigonal pencil would also be invariant.

An inseparable function over the algebraically closed field is a
square. At degree at most4 its square root has degree at most2,
already excluded. Thus a hypothetical tetragonal pencil is separable.
For two distinct G-conjugates, the index of their compositum divides4.
Index1 gives genus at most9, index4 makes the pencils equal, and
index2 gives a separable double cover of a curve of genus at most1.
The genus-zero case is hyperelliptic; the remaining quotient is
elliptic. Two distinct elliptic double quotients would give genus at
most5, so this involution is unique and is centralized by G.

The ramification set is nonempty, has size a positive multiple of n,
and has at most n points: its total different degree is2n, and a
wild quadratic ramification point has different exponent at least2.
Consequently it has exactly n points. The ramified Deuring–Shafarevich
formula gives f(D)=2f(E)+n−1, in particular f(D)≥n−1. This contradicts
the asserted strict inequality f(D)<n−1.

The independent divisor proof gives the same required lower bound.
The induced odd cyclic action on the elliptic quotient is free,
because a nontrivial odd stabilizer of a point there would fix a point
in its at-most-two-point fibre. Hence it is a translation action by
an order-n subgroup. The n−1 classes n[P_i−P_0] at its ramification
orbit are two-torsion. A principal F2-linear relation has invariant
divisor; the involution acts on its function by a scalar whose square
is1, hence by1 in characteristic two. The function descends and has
even valuation at every ramification point, contradicting the odd
coefficient n at any selected P_i. Thus the classes are independent.
This proof does not need an ordinary elliptic quotient.

## 2. Primitive characters and integral torsion

For a connected cyclic étale degree-n cover of a genus-two curve,
all nontrivial character H1 spaces have dimension1, regardless of
ordinariness of the base. Vanishing of one arrow makes its whole
doubling cycle nilpotent. Killing every primitive cycle therefore
gives f(D)≤n+1−phi(n)<n−1, since n has two distinct odd prime factors
and phi(n)≥8.

The group-ring endomorphism

    (1−sigma^(n/ell))(1−sigma^(n/m))

has nonzero scalar exactly on the primitive characters. The integral
odd-order character idempotents exist after an unramified extension
of Z2 containing the n-th roots of unity. Primitive Tate summands
have rank zero; on all remaining summands one of the two factors
vanishes identically. The endomorphism is consequently zero on the
entire étale Tate module and on all geometric two-primary torsion.
This is an integral representation argument, not a lifting from a
mere congruence modulo two. Inversion of characters under duality
preserves primitive support and causes no change.

## 3. The section comparison has no cancellation gap

All cover, line-bundle and deck data descend after a finite extension
of the finitely generated ground field. A section collision restricts
there, and A.3 supplies a lift with two-primary point difference.
Applying the displayed endomorphism gives two effective degree-four
divisors. The four group elements1,a,b,ab are distinct, the deck
action is free, and the two lifted points have different base images.
All eight support points are therefore distinct. The resulting
function has degree exactly4 and simple poles, so it is separable.
This contradicts the geometric lemma. No degeneration or
specialization of the theta hypothesis is needed.

## 4. Arithmetic corollaries and their scope

Symmetry of theta means that a point and its negative kill the two
possible primitive doubling cycles when <2,−1> is the full unit
group. For3^a5^b the two elementary valuation calculations give
orders2*3^(a−1) and4*5^(b−1); their gcd is2. The parity conflict
between the exponents giving minus one modulo3 and modulo5 puts
minus one outside the doubling subgroup. Thus the stated corollary
holds for every a,b≥1, not merely the finitely checked examples.

The all-odd-n wording is also sound. The quotient of the unit group
by squares has rank equal to the number of distinct prime divisors
of n. Generation by two elements forces at most two prime divisors.
The one-prime case is exactly A.C2.8, while the two-prime case is
proved here. No primitive conclusion is imported for unrestricted
composite conductors.

## 5. Sources and certificate

Root independently opened Poonen (2007), Gonality of modular curves
in characteristic p, Section2 Proposition2.1, authorp.3, at
https://math.mit.edu/~poonen/papers/gonality.pdf . The perfect-field
hypothesis includes the algebraically closed characteristic-two
field here. Web records turn679view0 and turn680view0.

Root also opened Crew (1984), Étale p-covers in characteristic p,
Corollary1.8 and its proof, printedpp.35–36, at
https://www.numdam.org/item/CM_1984__52_1_31_0.pdf . The formula is
for a ramified finite p-group action, exactly the needed quadratic
action. Web records turn679view1, turn680view1 and screenshots
turn681view0–1. The separate elementary divisor argument above
independently verifies the only lower bound needed in the proof.

The existing code/BC_two_prime_prym_checks.py was rerun and passed.
Its finite arithmetic checks illustrate the universal proof; they
do not assert existence of a suitable theta point. The degree15
example has its own author and root-independent exact norm
certificates. No correction to the mathematical candidate is needed.
