# Independent review of the order-seven theta construction

Reviewer: degeneration agent. Date: 14 November 2026.

Reviewed files: `audit/A_theta_seven_candidate.md`,
`code/A_theta_seven_certificate.py`, and its JSON output. The relevant
previous proofs A.C2.2, A.C2.5, A.C2.7–8, and A.C2.12 were also read in
full. Integrated source files were not changed during the checkpoint08
freeze.

**Verdict: the mathematical argument passes.** It proves A1 for the
specified geometric curve and proves an obstruction for every
geometrically connected **abelian** three-group cover of that curve.
It does not assert that all nonabelian three-group covers are ordinary,
or that every ordinary genus-two curve has a useful theta point of
prime-power order.

Two wording/source refinements were sent to the author: specify
geometrically connected covers, or work explicitly over the algebraic
closure, in the abelian-cover assertion; cite Milne, III, Theorem 11.1
for the curve-count/Frobenius trace formula, in addition to II,
Theorem 1.1. Neither changes the proof.

## 1. Curve, differentials, and theta normalization

Write alpha squared plus alpha plus one equal to zero, and set

\[
 C:\quad y^2+y=x+\frac{\alpha}{x}
                  +\frac{\alpha^2}{x+1},\qquad
 B=W_0+W_1-W_\infty.
\]

The three poles on the line are simple. The Artin–Schreier extension
is therefore a separable double cover, totally ramified at exactly
these poles, with different exponent two at each. Consequently

\[
 2g(C)-2=2(-2)+3\cdot2=2,
 \qquad \operatorname{div}(dx)=2W_0+2W_1-2W_\infty=2B.
\]

In particular, both logarithmic forms are regular and have divisors

\[
 \operatorname{div}(dx/x)=2W_1,\qquad
 \operatorname{div}(dx/(x+1))=2W_0.
\]

They are linearly independent and Cartier-fixed, so they form a
Cartier-bijective basis of the two-dimensional space of differentials.
Thus the curve is ordinary, with two-rank two.

The Frobenius-module line bundle of locally exact differentials is
indeed O(B): the exact rational differential dx trivializes it
rationally, and its local orders in this Frobenius module are half
the ordinary differential orders. This verifies the stated theta
convention

\[
 \Theta=\{\mathcal O(R-B):R\in C(\overline{\mathbf F}_2)\}.
\]

There is no sign discrepancy with the criterion
H0(B_C tensor L) nonzero. The equality B_C squared equals the canonical
bundle gives symmetry of theta by degree-one Riemann–Roch. Its
geometric irreducibility follows because it is a translate of the
genus-two Abel image. Its definition field is F4 because all three
branch points and B are F4-rational.

For the ordinary cubic criterion, the parameters are exactly
(a,b,c)=(1,alpha,alpha squared). The obstruction is

\[
 (a+b+c)^3+abc=0+1=1.
\]

Thus A.C2.2 makes every nontrivial geometric cyclic cubic cover
ordinary. By the complete character formula A.C2.5, a nonzero
three-torsion theta point would kill at least one arrow in the
two-character cubic cycle, contradicting this ordinariness.
The origin is absent as well: the locally-exact-differential exact
sequence identifies H0(B_C) with the kernel of Frobenius on H1(O_C),
and the latter is zero for this ordinary curve. Therefore

\[
                 \Theta\cap J_C[3](\overline{\mathbf F}_2)
                    =\varnothing.
\]

## 2. Frobenius calculation and exclusion of the whole three-primary packet

I ran the supplied verifier and also wrote
`code/A_theta_seven_independent.py`. The latter imports no candidate
code. It constructs F4 using pairs over F2 and constructs F16 as the
quadratic tower with beta squared plus beta equal to alpha. It counts
every affine pair (x,y), rather than using the trace criterion, and
adds the three branch points. The results are respectively 3 and 15.

Hence the first two Frobenius power sums on the Jacobian are

\[
       s_1=4+1-3=2,\qquad s_2=4^2+1-15=2.
\]

Newton's identity gives the second elementary symmetric function
(s1 squared minus s2)/2 equal to one. The genus-two functional
equation gives

\[
                  P(X)=X^4-2X^3+X^2-8X+16.
\]

The independent verifier uses the integer companion matrix for P,
so its check is different from the supplied polynomial long
division. It verifies both

\[
 M^5-I=3M^3+6M^2-33I
\]

and

\[
 (M^5-I)(-207M^3-57M^2+248M+856I)=40344I.
\]

The supplied coefficient-by-coefficient identity was separately read
and agrees. Since P(pi)=0 in the endomorphism ring, these are valid
identities on the entire geometric three-primary torsion group;
they do not merely describe characteristic polynomials modulo three.
The first makes pi to the fifth power act identically on J[3].

I rechecked A.C2.12 at the potentially delicate prime three. If a
theta point eta of three-power order is not fixed by sigma=pi to
the fifth power, choose the last nontrivial stage in its
three-power orbit. The resulting tau satisfies tau=1+3M on T3J,
tau cubed eta equals eta, and tau eta differs from eta by a
nonzero point T. Here

\[
              (1+\tau+\tau^2)/3=1+3M+3M^2
\]

is integral and invertible. It follows that 3T=0; tau fixes T.
The three points eta, eta+T, eta+2T all lie in theta and in
theta minus T. Those irreducible divisors are distinct because
the polarization is principal, and their intersection number is
two. The three distinct common points are impossible. Thus sigma
fixes eta. This is a complete proof in the present case; no
semisimplicity, scalar Frobenius, or lattice splitting is assumed.

The second identity now gives 40344 eta equal to zero. As
40344=3 times 13448 and the latter factor is prime to three,
eta is killed by three. The theta-three exclusion above then proves

\[
             \Theta\cap J_C[3^\infty](\overline{\mathbf F}_2)
                         =\varnothing.
\]

## 3. What the full abelian three-primary assertion proves

Let D to C be a geometrically connected finite étale Galois cover
with abelian three-group G, and work over the algebraic closure.
Its character line bundles L_chi are nontrivial for nontrivial
characters, and have three-power order. The preceding theorem
therefore excludes every one of them from theta. Each nontrivial
H1(C,L_chi) has dimension one, since C has genus two.

The exact Frobenius sequence consequently makes every arrow from
the chi line to the 2chi line an isomorphism. Multiplication by
two permutes the whole character group. The invariant
two-dimensional summand is Frobenius-bijective because C is
ordinary. Thus Frobenius on H1(D,O_D) is bijective, proving D
ordinary for every such G, not merely cyclic G or exponent-three G.

The Artin–Schreier stable-part description of geometric H1 with
F2 coefficients is equivariant for G. After extending scalars to
the algebraic closure, every nontrivial character occurs; duality
to geometric two-torsion only inverts the characters. Since
characters separate an abelian group of odd order, the deck action
is faithful. The same conclusion holds on all geometric
two-primary torsion, since faithfulness is already visible on
two-torsion.

Finally, a nonzero homomorphism from an ordinary abelian variety
has an ordinary positive-dimensional image, by Poincare
reducibility and isogeny invariance of the p-rank. A subvariety of
a two-rank-zero abelian variety has two-rank zero. These statements
exclude a nonzero homomorphism from J_D to such a target, hence a
nonconstant map from D by the Albanese property.

This covers the abelian three-primary tower over the original C.
An iterated tower of covers whose total group over C is nonabelian
is outside the statement; no inference about it is used.

## 4. Exact norm, divisor, and order seven

Put t=alpha squared, choose beta squared plus beta equal to alpha,
and let R=(t,beta). Direct substitution gives the right side of
the curve equation equal to alpha at x=t, so R lies on C. Also

\[
 u=x(x+1),\quad a=x+t,\quad b=x^2+t,\quad
 F=x^3+x^2+x+\alpha.
\]

For h=a+b(y+beta), its conjugate under y maps to y+1 is h+b.
The quadratic norm is therefore

\[
 h(h+b)=a^2+ab+b^2\bigl(F/u+\alpha\bigr).
\]

The independent polynomial calculation in F4[x] verifies

\[
          u(a^2+ab)+b^2(F+\alpha u)=(x+t)^7.
\]

At R, a(t)=0 and b(t)=1, so h vanishes and its conjugate is a
unit of value one. The x-map is étale there. The norm therefore
has order seven at x=t precisely because h has order seven at R;
the other point above t contributes no zero.

At W0 and W1, b has the nonzero values alpha squared and alpha,
while y has a simple pole. Thus h has a simple pole at each.
At infinity, x has order minus two and y has order minus one;
the term x squared times y is the unique term of pole order five.
All other terms have strictly smaller pole order. Outside these
three points h is regular, and its norm has no other zeros. Hence

\[
 \operatorname{div}(h)=7R-W_0-W_1-5W_\infty.
\]

Subtracting three times
div(u)=2W0+2W1 minus 4W_infinity gives exactly

\[
                   \operatorname{div}(h/u^3)=7(R-B).
\]

Thus eta=O(R-B) is a theta point killed by seven. It is nonzero
already because the origin is absent from theta. The candidate's
alternative argument also checks: if R were linearly equivalent
to B, then 2R would be canonical, forcing R to be a ramification
point of the unique hyperelliptic map; x(R)=alpha squared is not
0, 1, or infinity. Therefore eta has exact order seven.

The Kummer cover z to the seventh power equals h/u cubed is
geometrically connected because eta has exact order seven; an
actual seventh power would make R-B principal. It is étale
because every valuation is divisible by seven and seven is
invertible. All data and seventh roots of unity are available
after a finite constant extension, for example F_(4^6). The
unramified Riemann–Hurwitz formula gives genus eight.

## 5. Both character cycles and transfer to A1

The nonzero characters of C7 have exactly the two doubling cycles

\[
       \{1,2,4\},\qquad \{3,6,5\}=-\{1,2,4\}.
\]

The first meets theta at eta and the second at minus eta, because
theta is symmetric. Each cycle contains a zero Frobenius arrow
between one-dimensional cohomology spaces; hence Frobenius is
nilpotent on every nontrivial character summand. The invariant
summand has stable dimension two. The cover D consequently has
two-rank exactly two and the C7 action on geometric two-torsion
is trivial. Its action on all geometric two-primary torsion is
also trivial: an odd-order integral two-adic matrix congruent to
the identity modulo two is the identity, by the elementary
congruence induction proved in A.C2.7.

For completeness, the last geometric contradiction has no
hyperelliptic exceptional case. A free order-seven action on a
hyperelliptic curve descends faithfully to the line, because
the kernel of descent has order at most two. That order-seven
action fixes a point of the line. Its fibre has at most two
geometric points, so the order-seven action fixes each point in
that fibre, contradicting freeness. Thus D is not hyperelliptic.

A collision of distinct point sections on C lifts, after the
finite field extensions permitted by A.3, to P',Q' on D with
T=[Q'-P'] two-primary. A nonidentity deck transformation delta
fixes T. It follows that

\[
                    \delta Q'+P'\sim Q'+\delta P'.
\]

These effective degree-two divisors are distinct: their terms
over the two distinct original base points cannot be matched
unless delta fixes P' and Q', contrary to freeness. Their linear
equivalence would produce a degree-two map to the line, since
genus excludes a degree-one map after removing base points.
This contradicts the nonhyperellipticity just proved.

The collision argument remains valid after any finite extension
of the initial field. A form over a field finitely generated
over F2 becomes the stated curve after a finite extension and
inherits its geometric cover and deck action. A.C2.7 applies
directly; the proper-to-open quotient also preserves a putative
collision. These justify the claimed finite-extension,
finitely-generated-form, and open-subcurve scope.

## 6. Primary-source and certificate record

The mathematical proof is the candidate together with the
explicit previously proved claims cited above. The new independent
arithmetic certificate is `code/A_theta_seven_independent.py`, with
adjacent JSON; it returns PASS. It enumerates both finite fields,
checks the norm polynomial, verifies the companion-matrix
endomorphism identities, and checks the two character cycles.
Those finite calculations do not replace the divisor,
cohomological, or point-section arguments.

The reviewer additionally opened the exact primary texts:

- Milne, J. S. (2008). *Abelian varieties*, version 2.0, March 16.
  https://www.jmilne.org/math/CourseNotes/AV.pdf . II, Theorem 1.1,
  printed pp.75–76, gives the abelian-variety Frobenius/counting
  formulas. III, Theorem 11.1 and its proof, printed p.118, gives
  the curve-count/Jacobian trace relation; Corollary 11.4 is on
  p.119. Opened web references: turn633view0, turn635view0–1.
- Boxall, J., & Grant, D. (2006). Some remarks on almost rational
  torsion points. *Journal de Theorie des Nombres de Bordeaux*,
  18(1), 13–28. https://doi.org/10.5802/jtnb.531 . Proposition 2,
  printed p.16, states the bounded-prime-support torsion bound in
  terms of the first division field and explicitly includes
  finite fields. Exact primary PDF opened at
  https://www.numdam.org/item/10.5802/jtnb.531.pdf ; references
  turn633view1 and turn635view2–3. This is corroborating context
  for A.C2.12, whose genus-two intersection proof was checked
  directly above; it is not used as a theta existence theorem.

No unresolved mathematical step was found in the stated scope.
