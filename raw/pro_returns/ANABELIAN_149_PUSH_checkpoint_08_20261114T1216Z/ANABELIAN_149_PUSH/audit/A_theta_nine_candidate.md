# Exact nine-torsion beyond the ordinary cubic tower

Status: independently approved by root and integrated as A.C2.11.
The general A1 assertion remains unresolved.

## Statement

The genus-two curve

\[
C/\mathbf F_4:\quad y^2+y=x+1/x+\alpha/(x+1),
\qquad \alpha^2+\alpha+1=0,
\]

has an injective geometrically prime-to-two point-section map over every
finite extension of F₄. The same holds for its finite-extension forms over
fields finitely generated over F₂ and for its hyperbolic open subcurves.

This is the same curve for which A.C2.2 and the new cubic-compositum
obstruction show that all cyclic cubic covers, their full degree-81
compositum, and their Jacobians are ordinary. The successful cover here
has degree nine, genus ten and two-rank four. Its whole Prym is not of
two-rank zero; the order-three kernel on its two-primary torsion is the
decisive feature.

## 1. Curve, theta characteristic and fields

Write W₀,W₁,W∞ for the unique points above x=0,1,∞. The three simple
Artin–Schreier poles have different exponent two. Thus

\[
\operatorname{div}(dx)=2W_0+2W_1-2W_\infty,
\qquad B=W_0+W_1-W_\infty.
\]

The line bundle of locally exact differentials is O(B): locally an
ordinary differential is the square of a local section of this
Frobenius line bundle, so the divisor of an exact differential is twice
its divisor in that line bundle. Consequently the Raynaud theta is

\[
\Theta=\{\mathcal O(R-B):R\in C(\overline{\mathbf F}_2)\}.
\]

Choose t with t⁴+t³+t²+t+1=0 and set
α=t+t⁻¹=t³+t²+1. Then α²+α+1=0. Choose β satisfying
β²+β=t+1. These choices lie in F₁₆ and F₂₅₆, respectively:
the absolute F₁₆ trace of t+1 is one. At x=t one has

\[
t+t^{-1}+\frac\alpha{t+1}=t+1,
\]

so R=(t,β) is a point of C.

## 2. A complete norm and divisor certificate

Put

\[
\begin{aligned}
b(x)&=x^3+(t^2+t+1)x^2+(t^2+t+1)x+t^2,\\
a(x)&=x^3+t x^2+t x+t^2,\\
h&=a(x)+b(x)(y+\beta),\qquad u=x(x+1).
\end{aligned}
\]

The exact identity over F₁₆(x) is

\[
u\bigl(a^2+ab\bigr)+b^2\bigl(x^3+x^2+(1+\alpha)x+1+(t+1)u\bigr)
                  =(x+t)^9.                              \tag{1}
\]

Since the nontrivial automorphism of C/P¹ sends y to y+1,
(1) says

\[
\operatorname{Nm}_{C/\mathbf P^1}(h)=(x+t)^9/u.
\]

Here a(t)=0 and b(t)=1. Hence h vanishes at R, and its conjugate
value there is one; all nine zeros of the norm occur at R on C.
The poles of h are exactly simple at W₀ and W₁ and of order seven
at W∞. Indeed b(0)=t² and b(1)=1+t² are nonzero; y has a simple
pole at each of the three points; and the term x³y has pole order
seven at infinity, larger than any other term. Therefore

\[
\operatorname{div}(h)=9R-W_0-W_1-7W_\infty.
\]

As div(u)=2W₀+2W₁−4W∞, division by u⁴ gives

\[
\operatorname{div}(h/u^4)=9(R-W_0-W_1+W_\infty)=9(R-B).       \tag{2}
\]

Thus η=O(R−B) lies on Θ and is killed by nine. It is not killed
by three. A.C2.2, together with the exact theta-orbit formula
A.C2.5 at n=3, proves Θ∩J_C[3]=∅ for this ordinary curve: every
cubic Prym is ordinary and zero is absent because C is ordinary.
Equivalently its explicit cubic supersingularity expression is
(1+1+α)³+α=1+α≠0. Hence η has exact order nine.

## 3. The deck subgroup which disappears

Let D→C be the cyclic étale degree-nine cover associated with η;
it can be written by taking a ninth root of h/u⁴. Equation (2)
gives étaleness, and exact order nine gives connectedness. Its
genus is ten. The six primitive characters form the single
doubling orbit

\[
1,2,4,8,7,5\pmod9.
\]

Since η∈Θ, the Frobenius cycle on these six one-dimensional
coherent-cohomology spaces is nilpotent. The two nonprimitive
characters 3,6 survive because Θ contains no nonzero three-torsion.
Together with f(C)=2, A.C2.5 therefore gives f(D)=4.

The surviving nontrivial geometric two-torsion characters of the
cyclic deck group are exactly 3 and 6. Their common kernel is its
order-three subgroup. By A.C2.8 this subgroup acts trivially on all
geometric two-primary torsion. A hypothetical section collision on C
lifts to a two-primary difference [Q′−P′] on D by A.3. A nonidentity
element σ of that order-three kernel would fix this difference.
Then

\[
Q'+\sigma P'\sim P'+\sigma Q'.
\]

The two effective degree-two divisors are distinct, because P′ and Q′
lie over distinct base points and σ acts freely. Such a relation
would make D hyperelliptic, whereas a nontrivial odd étale Galois cover
of a curve of genus at least two is not hyperelliptic, as proved in
A.C2.7. This contradiction proves the statement.

Equivalently, the top connected Prym of D→D/⟨σ⟩ has two-rank zero;
the map R′↦(1−σ)[R′−R′₀] into it is geometrically point-injective.
The surviving lower two-rank does not affect this argument. All
equations and maps are defined after a finite extension, so A.3 and
the finitely generated Kummer input give the asserted variants.

## Certificate

`code/A_theta_nine_certificate.py` performs (1) in the exact field
F₂[t]/(t⁴+t³+t²+t+1), checks every nonzero local value used above,
checks the Artin–Schreier point and trace, enumerates the two
doubling orbits, and checks the order-three common kernel. It also
counts C(F₄) and C(F₁₆) for the separate Frobenius-bound note.
Root independently checked the identity in code/A_theta_nine_independent.py/.json and the full proof in audit/A_theta_nine_root_review.md. No floating arithmetic or unverified numerical point order is used.
