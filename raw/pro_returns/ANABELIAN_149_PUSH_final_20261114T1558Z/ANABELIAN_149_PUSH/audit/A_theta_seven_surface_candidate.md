# A two-dimensional ordinary genus-two family with a nilpotent seven-character part

Status: accepted after independent root, finite-field, and topos reviews;
integrated as Claim A.C2.15 in `sections/A_char2_deck.tex`.
Written by the degeneration agent on 14 November 2026. This file retains
the complete derivation and is supplementary to the integrated proof.

This is a positive construction for a two-dimensional locus of
ordinary genus-two curves in characteristic two. It contains a
two-dimensional component not contained in the cubic positive locus
A.C2.1. It does not assert universal existence of a useful theta
torsion point.

## 1. Statement and explicit parameters

Let Omega be an algebraically closed field of characteristic two.
For t different from 0 and 1 define

\[
 u(x)=x(x+1),\qquad q_t(x)=\frac{(x+t)^7}{u(x)},\qquad
 H_t(x)=\frac{u(x)^3}{(x+t)^5(x^2+t)^2}.
\]

Choose r,s in Omega satisfying

\[
 r\ne s,\quad r,s\notin\{0,1,t,\sqrt t\},\qquad
                    H_t(r)=H_t(s).
\tag{S7.1}
\]

Set

\[
\begin{aligned}
 e&=r+s,& \kappa&=e^2H_t(r),\\
 a&=\kappa,&
 b&=\frac{\kappa t^7}{r^2s^2},&
 c&=\frac{\kappa(t+1)^7}{(r+1)^2(s+1)^2}.
\end{aligned}
\tag{S7.2}
\]

All three coefficients are nonzero. The smooth proper curve

\[
 C_{t,r,s}:\qquad y^2+y=\phi(x),\qquad
             \phi(x)=ax+\frac b x+\frac c{x+1}
\tag{S7.3}
\]

is ordinary of genus two. Its Raynaud theta divisor contains a
point of exact order seven. The associated connected étale cyclic
degree-seven cover D has genus eight and two-rank two; its entire
deck group acts trivially on geometric two-primary torsion.
Consequently A1 holds for every finitely generated form of this
geometric curve over F2, after every finite extension, and for its
hyperbolic open subcurves.

The ordered triples (t,r,s) satisfying (S7.1) form a nonempty smooth
surface, finite étale of degree 72 over

\[
             (\mathbf A^1\setminus\{0,1\})\times\mathbf G_m,
             \qquad (t,r,s)\longmapsto(t,H_t(r)).
\]

The map from this surface to normalized curve coefficients (a,b,c)
has finite geometric fibres, and its image in ordinary genus-two
moduli has dimension two. At least one such component has a
nonempty open part outside the cubic locus

\[
                         (a+b+c)^3+abc=0.
\tag{S7.4}
\]

## 2. The degree-nine parameter map and the surface

The divisors of the numerator and denominator show that H_t has
degree nine: its zeros are 0,1,infinity, each of order three; its
poles are t of order five and sqrt(t) of order four. These five
points are distinct because t is neither zero nor one. Direct
differentiation gives

\[
 q_t'(x)=\frac{(x+t)^6(x^2+t)}{u(x)^2},\qquad
 H_t(x)=\frac{q_t(x)}{q_t'(x)^2},\qquad
 H_t'(x)=\frac{u(x)^2}{(x+t)^6(x^2+t)}.
\tag{S7.5}
\]

In particular the degree-nine map is separable and is étale away
from its zeros and poles. A scheme-theoretic verification of the
parameter degree avoids any assumption about a generic fibre.
Over

\[
 R=\mathbf F_2[t,t^{-1},(t+1)^{-1},\lambda,\lambda^{-1}],
\]

the equation H_t(x)=lambda is

\[
       \lambda(x+t)^5(x^2+t)^2+x^3(x+1)^3=0.
\tag{S7.6}
\]

Its leading coefficient is the unit lambda, and it has degree
nine. None of x,x+1,x+t,x squared plus t can vanish in any
geometric fibre of (S7.6), by direct substitution. They are
therefore units in its finite R-algebra. On this algebra the
x-derivative of the left side is

\[
                         \frac{u(x)^2(x^2+t)}{x+t},
\]

using (S7.6); it is a unit. Thus (S7.6) defines a finite étale
cover of degree nine over Spec(R). The off-diagonal part of its
fibre square is finite étale of degree 9 times 8, and is exactly
the parameter space in (S7.1). It is nonempty, smooth, and pure
of dimension two. Every geometric fibre has 72 ordered pairs.

## 3. Removing the two apparent poles by an Artin–Schreier term

Define

\[
 \rho_r=\frac{(r+t)r(r+1)}{r^2+t},\qquad
 \rho_s=\frac{(s+t)s(s+1)}{s^2+t},\qquad
 B(x)=(x+r)(x+s).
\]

Put

\[
\begin{aligned}
 v(x)&=\frac{\rho_r}{x+r}+\frac{\rho_s}{x+s}
       +\frac{\rho_r}{t+r}+\frac{\rho_s}{t+s},\\
 A(x)&=B(x)v(x).
\end{aligned}
\tag{S7.7}
\]

Then A is a polynomial of degree at most two, B is monic of
degree two, and A(t)=0. Consider

\[
                 \Phi(x)=\frac{\kappa q_t(x)}{B(x)^2}
                              +v(x)^2+v(x).
\tag{S7.8}
\]

We check that its apparent poles at r and s cancel completely.
At r, with z=x+r, one has B=z(e+z), so

\[
 \frac1{B^2}=\frac1{e^2z^2}+\text{a regular power series}.
\]

The double- and simple-pole coefficients of the first term of
(S7.8) at r are respectively

\[
          \frac{\kappa q_t(r)}{e^2},\qquad
          \frac{\kappa q_t'(r)}{e^2}.
\]

Since kappa divided by e squared is H_t(r), equations (S7.5)
give these two coefficients as rho_r squared and rho_r.
They are precisely the principal part of
(rho_r/z) squared plus rho_r/z. Characteristic two makes their
sum vanish. The same calculation at s is valid because
H_t(s)=H_t(r). All cross terms in the square vanish, so the
other summands of v create no additional principal part.

Thus the only poles of Phi are at 0,1,infinity, and each is
simple. The coefficients of 1/x and 1/(x+1), obtained by
evaluating the remaining units at 0 and 1, are respectively
b and c in (S7.2). At infinity q_t/B squared has leading term
x, while v is regular, so the coefficient of x is a=kappa.
Therefore Phi minus phi is constant. Since q_t(t)=v(t)=0,
one has Phi(t)=0, and the constant is phi(t). We have proved
the exact rational identity

\[
 \frac{\kappa q_t}{B^2}+v^2+v=\phi(x)+\phi(t).
\tag{S7.9}
\]

This principal-part proof establishes the identity for every
parameter satisfying (S7.1), not only for the finite examples
in the accompanying certificate.

## 4. The norm and the exact divisor

Choose beta in Omega with beta squared plus beta equal to
phi(t), and let R_t=(t,beta) on C. The choice is possible
over a finite extension of any field defining the parameters.
Define

\[
                         h=A(x)+B(x)(y+\beta).
\]

The involution y maps to y+1 sends h to h+B. Using (S7.9),

\[
\begin{aligned}
 \operatorname{Nm}_{C/\mathbf P^1}(h)
  &=A^2+AB+B^2\bigl(\phi(x)+\phi(t)\bigr)\\
  &=\kappa q_t(x)
    =\frac{\kappa(x+t)^7}{x(x+1)}.
\end{aligned}
\tag{S7.10}
\]

Let W0,W1,W_infinity denote the unique points above the three
Artin–Schreier poles. As in A.C2.13, they have different
exponents two, giving genus two and

\[
 \operatorname{div}(dx)=2W_0+2W_1-2W_\infty,
 \qquad \mathcal B_C\simeq\mathcal O(B_C),
 \qquad B_C=W_0+W_1-W_\infty.
\]

Both logarithmic differentials dx/x and dx/(x+1) are regular,
independent, and Cartier-fixed. Hence C is ordinary and its
Raynaud theta divisor is the symmetric translate

\[
           \Theta_C=\{\mathcal O(P-B_C):P\in C(\Omega)\}.
\]

At R_t, A(t)=0 and B(t) is nonzero. Thus h vanishes and its
conjugate has the nonzero value B(t). The x-map is étale at
R_t. Equation (S7.10) therefore makes the zero of h at R_t
have exact order seven; there are no other zeros.

At W0 and W1 the nonzero values of B give simple poles of h.
At infinity the monic term x squared times y has pole order
five and is the unique term of that order: A has degree at
most two, and B times beta has pole order at most four.
Consequently

\[
 \operatorname{div}(h)=7R_t-W_0-W_1-5W_\infty,
 \qquad
 \operatorname{div}(h/u^3)=7(R_t-B_C).
\tag{S7.11}
\]

The class eta=O(R_t-B_C) belongs to theta and is killed by
seven. It is nonzero. Indeed, the exact differential sequence
and ordinariness give H0(B_C)=0; equivalently the origin is
not on theta. Alternatively, a zero class would make 2R_t
canonical, forcing R_t to be a hyperelliptic branch point,
whereas t is neither 0 nor 1 nor infinity. Thus eta has exact
order seven.

Adjoining a seventh root of h/u cubed gives a geometrically
connected degree-seven cover: otherwise this function would
be a seventh power and R_t-B_C would be principal. It is
étale because all valuations are divisible by seven and
seven is invertible. After adjoining seventh roots of unity
it is cyclic Galois. Riemann–Hurwitz gives genus eight.

## 5. Both character cycles vanish, and A1 follows

The nonzero characters of the cyclic group of order seven
have the doubling cycles

\[
                         \{1,2,4\},\qquad\{3,6,5\}.
\]

The first meets theta at eta; the second meets it at minus
eta by symmetry. All nontrivial H1(C,eta to the i) spaces
are one-dimensional. The exact Frobenius-kernel argument
of A.C2.5 therefore kills the stable part of both cycles.
The invariant summand retains the two-rank two of C.
Thus f(D)=2=f(C), and the full cyclic deck group acts
trivially on geometric two-torsion. Its action on all
geometric two-primary torsion is also trivial by the
odd-order congruence induction in A.C2.7.

For a direct account of the final implication, a collision
of two distinct point sections on C lifts by A.3 to P',Q'
on D whose difference is two-primary. A nonidentity deck
transformation delta fixes that difference and produces

\[
                         \delta Q'+P'\sim Q'+\delta P'.
\]

The effective degree-two divisors are distinct because P'
and Q' lie over distinct base points and the deck action is
free. Their equivalence would make D hyperelliptic. But
an order-seven free action cannot occur on a hyperelliptic
curve: it descends faithfully to the line, fixes a point
there, and consequently fixes a point in the fibre of at
most two points above it. This is a contradiction.

All covering data descend to a finite extension of the field
of definition when the curve and parameters are defined over
a finitely generated field. Restriction of a collision to that extension
is permitted. The same argument applies to any form, and
the proper compactification quotient transfers injectivity
to hyperbolic open subcurves. This is precisely the scope
already proved in A.C2.7; no finite-field counting hypothesis
is used in this positive construction.

## 6. The image has dimension two

Fix a normalized coefficient triple (a,b,c) with abc nonzero.
Every parameter triple mapping to it gives a point
R_t with O(R_t-B_C) in J_C[7] minus the origin. The Abel
map R maps to O(R-B_C) is injective, and J_C[7] has only
7 to the fourth power geometric points. There are therefore
at most 7^4 minus one possibilities for R_t.

For each fixed R_t the divisor of h in (S7.11) is fixed, so
h is unique up to a nonzero scalar. Its representation
h=A+B(y+beta), with deg(A),deg(B) at most two, is unique
once beta=y(R_t) is fixed. Indeed,

\[
                   1,x,x^2,y,xy,x^2y
\]

is a basis of L(W0+W1+5W_infinity): these six independent
functions have the allowed poles, and Riemann–Roch gives
dimension 7+1 minus 2 equal to six. The coefficient of
x squared times y in h is nonzero, since h has pole order
five at infinity. Requiring B to be monic fixes the scalar.
Its two ordered roots then leave at most two choices for
(r,s). Thus the coefficient map has at most
2(7^4 minus one) geometric points in each fibre.

The parameter space is pure two-dimensional and the map is
of finite type with finite fibres. Every irreducible
component therefore has two-dimensional image in the
three-dimensional coefficient space.

Passing to geometric isomorphism classes does not lower
this dimension. An isomorphism of these genus-two curves
descends through the unique hyperelliptic pencil and sends
the branch set {0,1,infinity} to itself. There are only six
such Möbius transformations. For each of them, two
Artin–Schreier functions with only these simple poles can
differ by z squared plus z only when z is constant: any
pole of z would create a highest pole of even order at
least two. A constant changes none of a,b,c. Consequently
only finitely many normalized triples represent a fixed
geometric isomorphism class. The image in moduli has
dimension two as asserted.

One can also identify the scope of this chart. Conversely,
any nonzero theta-seven point on an ordinary normalized
curve determines h as above. If its monic B has two distinct
roots, the absence of poles in (S7.9) forces the two
principal-part equalities in Section 3, hence (S7.1) and
exactly this construction. A root with r squared equal to t
would make q_t'(r)=0 while q_t(r) remains nonzero, so its
double pole could not be removed by an Artin–Schreier term;
this case is impossible. Thus the surface describes the
separable-B chart of the ordinary theta-seven incidence.
No exhaustion of the double-root boundary is asserted.

## 7. A checked point outside the cubic locus

Let omega satisfy omega to the fourth power plus omega plus
one equal to zero in F16, and take

\[
 t=\omega,\qquad r=\omega^3+\omega,\qquad
 s=\omega^3+\omega^2+1.
\]

Then H_t(r)=H_t(s)=1, all excluded values are avoided, and

\[
 (a,b,c)=(\omega^2+\omega,\ \omega^3+\omega^2+1,
                                  \omega^3+\omega+1).
\]

The explicit polynomials are

\[
\begin{aligned}
 A(x)&=(\omega^2+\omega)x^2+x+(\omega^3+1),\\
 B(x)&=x^2+(\omega^2+\omega+1)x+(\omega^3+\omega+1).
\end{aligned}
\]

Here phi(t)=omega cubed plus omega plus one; beta may be
chosen in F256. The cubic obstruction is

\[
                   (a+b+c)^3+abc=\omega^2+\omega+1\ne0.
\]

These identities are checked exactly in the certificate.
Therefore the component of the parameter surface containing
this point has a nonempty open subset outside (S7.4).
Its image still has dimension two by the finite-fibre proof.
This establishes a broader positive locus than the cubic
condition, not merely a renamed point on that locus.

## 8. A simpler one-parameter family, including A.C2.13

There is also a useful formula with an inseparable quadratic
B. For arbitrary t different from zero and one, put U=t(t+1)
and

\[
 a=\frac1{U^2},\qquad b=\frac{t^3}{(t+1)^2},\qquad
 c=\frac{(t+1)^3}{t^2},\qquad
 \beta^2+\beta=a(t+1).
\tag{S7.12}
\]

For the curve (S7.3), R=(t,beta), and

\[
                         h=(x+t)+(x^2+t)(y+\beta),
\]

one has exactly

\[
          \operatorname{Nm}(h)=\frac{a(x+t)^7}{x(x+1)}.
\tag{S7.13}
\]

Here is a direct identity valid for the whole family. Write
z=x+t, so u=z squared plus z plus U, and note

\[
 u\bigl(\phi(x)+\phi(t)\bigr)=z+az^3,
 \quad \phi(t)=a(t+1),\quad A=z,\quad B=z^2+U.
\]

Expanding in characteristic two gives

\[
\begin{aligned}
 u(A^2+AB)&=z^5+z^3+U^2z,\\
 B^2(z+az^3)&=z^5+az^7+U^2z+z^3,
\end{aligned}
\]

because aU squared equals one. Their sum is a z to the
seventh power, proving (S7.13). The same divisor and
character arguments prove A1. This family is nonisotrivial:
a=1/U squared varies, while each geometric isomorphism
class has only finitely many normalized coefficient triples.

Its cubic obstruction is

\[
              (a+b+c)^3+abc=\frac{U^3+U+1}{U^3}.
\]

It is therefore outside the cubic locus except at finitely
many parameters. Taking t=alpha squared with alpha squared
plus alpha plus one equal to zero gives U=1 and the curve
(a,b,c)=(1,alpha,alpha squared) of A.C2.13.

## 9. Verification and exact remaining universal issue

The standard-library script
`code/BC_theta_seven_surface_checks.py` and its adjacent JSON
verify all twelve good unordered parameter pairs over F16,
the norm for each, every excluded denominator and local
value used, the explicit example above, and all fourteen
parameters of the simpler family over F16. All checks pass.
The general norm identity, étaleness, dimension, and A1
implication are proved above and do not rely on sampling.

This construction uses the already proved exact
theta/Frobenius and deck criteria A.C2.5–8. The elementary
new inputs are (S7.5)–(S7.11) and the finite-fibre dimension
argument. No new external existence theorem is invoked.

For an arbitrary ordinary genus-two curve, the remaining
cyclic-cover existence statement is still to find an odd n
and L of exact order n for which the common kernel of all
characters in doubling orbits disjoint from theta is
nontrivial. Prime-to-two theta torsion density and existence
of a nonordinary cover do not imply that condition. This
candidate establishes it on an explicit two-dimensional
locus, and makes no universal claim.
