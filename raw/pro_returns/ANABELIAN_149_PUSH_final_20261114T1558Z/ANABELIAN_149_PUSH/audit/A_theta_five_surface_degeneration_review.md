# Independent review of the complete ordinary theta-five locus

Reviewer: degeneration agent. Date: 14 November 2026.

Reviewed the complete `audit/A_theta_five_surface_candidate.md` and
`code/A_theta_five_surface_checks.py`/`.json`. The script was executed
and returned PASS. No candidate or integrated A source was edited.

**Verdict: approved in the stated scope.** The norm, divisor, full
converse, two-dimensional moduli image, automorphism calculation,
and A1 implication all pass. The proof does not need an additional
genericity or separability exception. It does not claim that every
ordinary genus-two curve lies on this locus.

## 1. Exact parameter and norm calculation

For the five-power function q=(x+t)^5/[x(x+1)], characteristic-two
differentiation gives

\[
                  q'(x)=\frac{(x+t)^4(x^2+t)}{x^2(x+1)^2}.
\]

At the allowed parameter r, q(r) and q'(r) are nonzero. Put
rho=q(r)/q'(r), kappa=q(r)/q'(r)^2 and

\[
           v(x)=\frac{\rho}{x+r}+\frac{\rho}{t+r}.
\]

Multiplying by B=x+r gives

\[
       Bv=\frac{\rho(x+t)}{t+r}
          =\frac{r(r+1)}{r^2+t}(x+t)=A.
\]

At r the two principal coefficients of kappa q/B squared are
rho squared and rho. They cancel exactly with the corresponding
coefficients of v squared plus v. No higher poles are present.
At 0 and 1, v is regular, and the residues of the remaining
term are the stated b and c. At infinity v is regular and
kappa q/B squared has leading term kappa x, giving a=kappa.
Its value after cancellation at t is zero, so the constant
normalization is exactly phi(t). This proves the universal norm
identity independently of numerical specialization.

The supplied SymPy computation verifies the same identity in
the exact rational function field GF(2)(x,t,r). It is an identity
on the entire specified parameter open, since its denominators
are precisely among the nonvanishing factors imposed there.

## 2. Divisor, exact torsion order, and cover

The three nonzero simple Artin–Schreier poles give genus two
and different exponent two at each ramification point. The
logarithmic differential basis proves ordinariness, and the
locally exact differential convention gives
B_theta=W0+W1-W_infinity and the stated symmetric theta translate.

At R=(t,beta), h=A+B(y+beta) is zero and its conjugate is the
nonzero value t+r. The x-map is étale there, so the norm zero
of order five gives a zero of h of exact order five only at R.
At W0,W1, the nonzero values r,r+1 of B produce simple poles.
At infinity xy is the unique term with pole order three.
Therefore

\[
 \operatorname{div}(h)=5R-W_0-W_1-3W_\infty,
 \qquad
 \operatorname{div}(h/u^2)=5(R-B_\theta).
\]

The theta class is nonzero: a zero class would imply 2R is
canonical and hence that R is a branch point of the unique
genus-two hyperelliptic pencil. The parameter t excludes all
three branch values. Its order is therefore exactly five.
The Kummer cover has degree five and is geometrically connected;
otherwise its defining function would be a fifth power and
R-B_theta principal. Every local valuation is divisible by five,
so the normalization is étale. Its genus is six.

## 3. Full converse, with every exclusion forced

Let eta=O(R-B_theta) be a theta point of exact order five on
any normalized ordinary curve with a,b,c nonzero. If R were
a ramification point W, then 2W and 2B_theta would both be
canonical, so eta would have order dividing two. Thus R is
unramified with a finite coordinate t not equal to zero or one.

A function g with divisor 5(R-B_theta), multiplied by u squared,
has exactly the divisor of h above. Riemann–Roch gives

\[
 L(W_0+W_1+3W_\infty)=\langle1,x,y,xy\rangle.
\]

The divisor has degree five, so the space has dimension four;
the four listed functions are independent and obey its pole
bounds. The unique pole of order three at infinity forces the
coefficient B of y+beta to be linear and nonconstant. Scaling
uniquely makes B=x+r. Vanishing at R gives A=d(x+t).

The simple poles at W0 and W1 force r to be different from
zero and one. If r=t, both A and B vanish at t, and h vanishes
at both unramified points above t. This contradicts its sole
zero at R, so r is also different from t.

The norm is kappa q for a nonzero scalar, and its leading term
at infinity gives kappa=a. Evaluating at r gives
A(r)^2=kappa q(r). Differentiating the norm and evaluating at r
gives A(r)=kappa q'(r): the derivative of A squared and B
squared is zero, the derivative of AB contributes A(r), and
the remaining term has a factor B squared. The first identity
shows A(r) is nonzero, so q'(r) is nonzero; equivalently
r squared is different from t. Dividing these two identities
gives exactly kappa and d from the proposed formulas. Residues
at zero and one give exactly b,c. Thus no additional chart
condition has been silently introduced in the converse.

## 4. Finite fibres and dimension

The parameter space is an irreducible nonempty open in the
affine plane. For any fixed coefficient triple, the injective
Abel map R maps to O(R-B_theta) confines R to the finite set
J[5]. The divisor determines h up to scalar; making B monic
removes that scalar and determines r. Hence the coefficient
map has finite geometric fibres and its image has dimension
two.

Each geometric isomorphism class has only finitely many
normalized triples. Any isomorphism preserves the unique
hyperelliptic pencil and hence induces a Möbius transformation
preserving {0,1,infinity}, of which there are six. Once that
transformation is fixed, an Artin–Schreier correction with a
pole would create a pole of even order at least two. It cannot
be the difference of two functions having only the stipulated
simple poles. Thus the correction is constant and changes no
normalized coefficient. Passage to moduli preserves dimension.

For forms defined over a finitely generated field, the finite
geometric fibres also justify choosing the parameters over an
algebraic extension of the field of definition; all the finite
covering data then descend after a finite extension. This is
compatible with the field scope of A.C2.7.

## 5. The automorphism assertion is valid

The two branch permutations act by

\[
 x\mapsto x+1:\ (a,b,c)\mapsto(a,c,b),\qquad
 x\mapsto1/x:\ (a,b,c)\mapsto(b,a,c),
\]

up to a removable constant in the Artin–Schreier function.
They generate all six transformations. Their action on the
coefficient triple is faithful. If a,b,c are pairwise distinct,
no nonidentity branch permutation preserves the curve.

An automorphism inducing the identity on x is a deck
automorphism of its separable quadratic function-field
extension, and therefore is either the identity or y maps to
y+1. More generally, an isomorphism above a fixed x-map
must have this Artin–Schreier form: writing the image as
alpha(x)y+z(x), its equation forces alpha squared plus alpha
to vanish, so the nonzero alpha is one. The pole argument
above then forces z to be constant. There is no omitted
continuous rescaling of y.

For the displayed F16 example (a,b,c)=(1,omega,omega+1),
the coefficients are pairwise distinct and nonzero. Its
geometric automorphism group is exactly the order-two
hyperelliptic group. The stated absence of nontrivial odd
geometric automorphisms and of an odd-order Galois elliptic
quotient follows. This is a statement about geometric
automorphisms, not semilinear automorphisms of the constant
field, so Frobenius introduces no exception.

## 6. Character computation and A1

Multiplication by two has the single nonzero orbit 1,2,4,3
modulo five. The theta point gives one zero arrow among its
one-dimensional H1 character spaces, making the entire
nontrivial Frobenius part nilpotent. The invariant part has
stable dimension two, so the cover has two-rank two and
trivial deck action on geometric two-torsion. A.C2.7's
odd-order congruence induction promotes this to all geometric
two-primary torsion.

The same claim then excludes a section collision: its lifted
two-primary point difference would be fixed by a nontrivial
free deck element, giving distinct linearly equivalent
effective degree-two divisors on the nonhyperelliptic cover.
The nonhyperellipticity proof works for order five just as
for order seven. Restriction to finite extensions and the
proper-to-open comparison yield exactly the asserted scope.

## 7. Computational record

The existing script was executed successfully. Its exact
fraction-field assertions pass, its finite enumeration has
168 allowed parameter pairs over F16 with 156 outside the
cubic locus, and it verifies the displayed pair t=omega,
r=omega squared. It gives (a,b,c)=(1,omega,omega+1),
d=omega squared plus omega plus one, and cubic obstruction
omega squared plus omega, which is nonzero. Its single
doubling orbit is correct.

No mathematical correction is required. The universal A1
existence question remains explicitly outside the result.
