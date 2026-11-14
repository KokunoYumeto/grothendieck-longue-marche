# A finite-field bound for prime-power torsion on a genus-two theta

Status: independently approved by root and integrated as A.C2.12.
This is a limitation and finite search reduction, not an existence theorem.

## 1. Exact statement

Let J/F_q be the Jacobian of a genus-two curve, and let Θ be a geometrically
irreducible theta divisor defined over F_q. Let ℓ be an odd prime different
from the characteristic. Choose r such that every point of J[ℓ] is
F_{q^r}-rational. Then

\[
\Theta(\overline{\mathbf F}_q)\cap J[\ell^\infty]
       \subset J(\mathbf F_{q^r})[\ell^\infty].              \tag{1}
\]

In particular the left side is finite. The statement applies to the
Raynaud theta of a genus-two curve in characteristic two, because that
theta is a translate of the Abel image of the curve and is defined over
the same finite field.

## 2. Proof, including the last nontrivial orbit

Write π for the q-power Frobenius endomorphism and σ=πʳ. Its action on
T_ℓJ is a matrix congruent to the identity modulo ℓ. Suppose that η on
Θ is ℓ-primary and σ(η)≠η. The principal congruence subgroup of
GL(T_ℓJ/ℓᵃ) is an ℓ-group, where ℓᵃ kills η. Hence there is a least
b≥1 with σ^{ℓᵇ}η=η. Put τ=σ^{ℓ^{b−1}}. Then τ(η)≠η but τ^ℓ(η)=η,
and still τ=1+ℓM on T_ℓJ for an integral matrix M.

The operator

\[
U=\frac{1+\tau+\cdots+\tau^{\ell-1}}\ell
 =1+\sum_{j=1}^{\ell-1}{\ell\choose j+1}\ell^{j-1}M^j
\]

is integral and congruent to the identity modulo ℓ. This includes ℓ=3:
the last term then has coefficient 3. Therefore U is an automorphism
of the geometric ℓ-primary torsion group and commutes with τ. Set
T=τ(η)−η. The equation τ^ℓ(η)=η gives ℓUT=0, hence ℓT=0. Moreover
T≠0 and τ(T)=T, because τ is the identity on J[ℓ]. Thus the ℓ points

\[
\eta,\ \eta+T,\ldots,\eta+(\ell-1)T
\]

are exactly the τ-orbit of η. They all lie on Θ, since τ is a power
of Frobenius. Each also belongs to Θ−T. But Θ²=2, and Θ and Θ−T are
distinct irreducible divisors: a translation preserving a principal
theta divisor belongs to the kernel of its principal polarization,
which is trivial. Their intersection cannot contain ℓ≥3 distinct
geometric points. This contradiction proves σ(η)=η and (1).

Root independently reviewed the proof and both integer remainders in audit/A_theta_prime_power_root_review.md. The exact certificate is code/A_theta_frobenius_certificate.py/.json.

No scalar or semisimple Frobenius action was assumed. The argument
works with arbitrary integral matrices congruent to the identity,
including nontrivial Jordan reduction before passing to σ.

## 3. Relation to opened primary literature

Boxall and Grant (2006), *Some remarks on almost rational torsion points*,
Journal de Théorie des Nombres de Bordeaux 18(1), 13–28, Proposition 2,
printed p.16, gives the corresponding bounded-prime-support torsion
bound for almost rational points. It uses the field splitting first
prime levels (ℓ for odd ℓ and 4 for ℓ=2), and explicitly covers finite
fields. The primary PDF was opened at
https://www.numdam.org/item/10.5802/jtnb.531.pdf, web references
turn531view0 and turn532view0. The proof above specializes directly
to a genus-two theta and proves the precise fixed-field assertion.

Pop and Saïdi (2003), *On the specialization homomorphism of fundamental
groups of curves in positive characteristic*, Proposition 2.1 and its
proof, printed pp.112–113, quote the Anderson–Indik surjectivity of the
projection of a curve to selected primary components. That projection
theorem does not require the other primary components to vanish. The
ensuing "pairwise prime" orders are pairwise coprime orders, as the
displayed proof verifies. These statements do not force a pure
prime-power theta point. Opened primary PDF:
https://library.slmath.org/books/Book41/files/pop.pdf,
references turn521view1, turn522view2 and turn524view0.

## 4. Exact bound for the curve of A.C2.11

For C:y²+y=x+1/x+α/(x+1), α²+α+1=0, direct counts give
#C(F₄)=5 and #C(F₁₆)=15. The genus-two Frobenius polynomial is therefore

\[
P(X)=X^4-X^2+16.
\]

The exact polynomial congruence

\[
X^{12}-1\equiv705X^2-3345=3(235X^2-1115)\pmod{P(X)}
\]

shows that π¹² acts as the identity on J[3]. It is not necessary to
diagonalize π or assert an exact order modulo three. Applying (1), every
three-primary theta point is fixed by π¹². A second exact identity is

\[
\begin{aligned}
 &(X^{12}-1)(176+47X^2)+27\cdot41440\\
 &\quad=P(X)\bigl(47X^{10}+223X^8-529X^6-4097X^4
                         +4367X^2+69919\bigr).
\end{aligned}                                                   \tag{2}
\]

Since 41440 is prime to three, (2) implies that every such theta point
is killed by 27. The absence of theta three-torsion leaves only possible
exact orders nine and 27. The exact order-nine point is proved in
A.C2.11. Neither the Frobenius bound nor divisibility supplies any
point of exact order 27.

The separate exploratory rank calculation in
`code/A_theta_three_power_experiment.py/.json` suggests that all
27-torsion theta points already have order nine, but this stronger
classification is not used in (1), (2), or A.C2.11 and is not promoted
without its own geometric and independent algorithmic review.

## 5. Consequence for the remaining route

Repeated ℓ-division does not force theta points of arbitrarily high
ℓ-power order. For each fixed ℓ, (1) reduces the primitive-character
criterion A.C2.8 to finitely many torsion candidates. The existence of
a suitable prime or prime power for every genus-two curve remains an
additional arithmetic-geometric statement. Prime-to-two torsion density
and primary-projection surjectivity do not establish it.
