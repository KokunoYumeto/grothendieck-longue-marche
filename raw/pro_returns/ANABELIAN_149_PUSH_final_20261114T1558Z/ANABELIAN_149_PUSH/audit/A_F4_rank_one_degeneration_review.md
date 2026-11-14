# Independent review: the twelve rank-one genus-two classes over F4

**Reviewer:** degeneration. **Outcome:** PASS for the complete twelve-class
positive assertion and its stated forms/open-curve consequences.

I also read the complete written candidate
`audit/A_F4_all_genus_two_candidate.md`, Sections 1--6, after checking
the fixed witnesses. Its classification, norm formula for the final
function, annihilator-to-actual-order passage, forms, and combination
with the ordinary and two-rank-zero cases all pass without correction.

The fixed witness file is
`code/A_F4_rank_one_witnesses.json`, SHA256
`82dd18cfcfac963e1a4217e03a55b39a47766ee521c6601f3704e9828b417ec3`.
My independent verifier is
`code/A_F4_rank_one_degeneration.py`, with its JSON output.
It passes all seven norm identities and all twelve parameter classes.

The verifier imports no search, accelerated arithmetic, Jacobian,
jet-matrix, or earlier finite-field implementation. It builds each
binary field directly, checks its complete nonzero multiplicative
cycle, and performs coefficient convolution using shift/XOR field
multiplication. It makes positive annihilator assertions only;
in particular the theorem does not require a separately tested
exact order of 39.

## 1. Exact geometric classification

Let \(C\) be a smooth proper genus-two curve over an algebraically
closed field of characteristic two, with two-rank one. The
hyperelliptic map is a separable double cover, hence has a reduced
Artin--Schreier equation
\[
                          y^2+y=\phi(x)
\]
whose poles all have odd order. The genus and two-rank formulas are
\[
                   2g+2=\sum_P(d_P+1),\qquad
                   f_2(C)=\#\{P\}-1.
\]
Thus there are exactly two poles, with orders three and one.
Move the triple pole to infinity and the simple pole to zero.
Remove the even terms by an Artin--Schreier change of \(y\), and
remove the constant over the algebraic closure. The equation is
\[
                  y^2+y=a x^3+b x+c/x,\qquad ac\ne0.
\]
Scaling \(x\) by \(c\) yields
\[
                  C_{A,B}:\quad y^2+y=A x^3+B x+1/x,
                  \qquad A\ne0.                         \tag{R1}
\]

This normalized pair is **unique geometrically**. An isomorphism
preserves the unique hyperelliptic involution and descends to the
base line. It cannot exchange the two branch points, since their
ramification jumps differ. It therefore induces a scaling
\(x\mapsto u x\). A lift differs on \(y\) by a rational
Artin--Schreier correction. A nonconstant rational correction
\(r^2+r\) has an even highest pole order at every pole of \(r\);
it cannot equal a nonzero difference of reduced expressions with
only odd pole orders. Comparison of the simple-pole coefficient
forces \(u=1\), and then comparison at infinity forces equality
of \(A,B\). Constants do not alter either coefficient.

Consequently fourth-power Frobenius fixes the geometric class
if and only if \(A^4=A\) and \(B^4=B\). There are precisely
\[
                   3\cdot4=12
\]
such classes, represented by \(A\in\mathbf F_4^\times\),
\(B\in\mathbf F_4\). Each has an actual model (R1) over
\(\mathbf F_4\). Twists do not create new geometric classes.

**Primary source check.** I independently opened Elkin and Pries,
*Ekedahl--Oort strata of hyperelliptic curves in characteristic 2*,
https://arxiv.org/pdf/1007.1226, Notation 1.1 (author p.2) and
Section 3.1 (author p.5), retrieval `turn823view0\).
Those passages give the reduced odd-pole equation and both
ramification formulas used above. The normalization and uniqueness
argument here are supplied explicitly, rather than attributed to
a nonexistent classification theorem in that paper.

## 2. Raynaud origin and the polynomial model

Let \(W_0,W_\infty\) be the ramification points of (R1).
Their different exponents are two and four, respectively.
Since the pullback of the base divisor of \(dx\) is
\(-4W_\infty\),
\[
                          \operatorname{div}(dx)=2W_0.
\]
With the Frobenius module structure on locally exact
differentials, this gives
\[
                           \mathcal B_C\simeq\mathcal O_C(W_0).
\]
Thus the Raynaud theta curve is
\[
                   \Theta=\{[R-W_0]:R\in C\}.
\]
This is different from the ordinary three-pole origin.
Here zero belongs to theta; it must not be counted as a
nontrivial torsion witness.

Putting \(Y=xy\) gives
\[
                        Y^2+xY=A x^5+B x^3+x.
\]
The reduced Mumford pair \(T=(x,0)\) is
\([W_0-W_\infty]\), and
\(\operatorname{div}(x)=2W_0-2W_\infty\).
Therefore
\[
              [R-W_\infty]+T=[R-W_0].
\]
The exploratory arithmetic uses exactly this shift.
The final norm certificates do not need a Jacobian algorithm.

## 3. The exact norm certificates and their divisors

The seven representatives and supplied annihilators are:

| \((A,B)\) | \(n\) | Certificate field |
|---|---:|---:|
| \((1,0)\) | 13 | \(\mathbf F_{16}\) |
| \((1,1)\) | 5 | \(\mathbf F_4\) |
| \((1,\alpha)\) | 11 | \(\mathbf F_{16}\) |
| \((\alpha,0)\) | 39 | \(\mathbf F_{256}\) |
| \((\alpha,1)\) | 19 | \(\mathbf F_{16}\) |
| \((\alpha,\alpha)\) | 7 | \(\mathbf F_4\) |
| \((\alpha,\alpha^2)\) | 5 | \(\mathbf F_{16}\) |

Here \(\alpha^2+\alpha+1=0\); each actual binary embedding of
\(\alpha\) is recorded in the fixed file and checked independently.

For each row put \(d=(n-1)/2\). The supplied polynomials
\(a(x),b(x)\), scalar \(c\ne0\), and point \(R=(t,y_R)\) satisfy
\[
 x(a^2+ab)+b^2(Ax^4+Bx^2+1)=c(x+t)^n,                    \tag{R2}
\]
\[
 \deg a=d,\qquad \deg b\le d-2,\qquad b(0)b(t)\ne0,
 \qquad a(t)+b(t)y_R=0,\qquad t\ne0.                    \tag{R3}
\]
My verifier checks every coefficient of (R2), all inequalities
and evaluations in (R3), the original curve equation of \(R\),
and \(c=a_d^2\).

Let
\[
                            f=\frac{a+b y}{x^d}.
\]
The identity (R2) says
\[
                    \operatorname{Norm}(a+b y)
                         =c(x+t)^n/x.
\]
At \(R\), \(a+b y\) vanishes, while its conjugate has value
\(b(t)\ne0\). The \(x\)-map is unramified there because
\(t\ne0,\infty\). Thus \(f\) has a zero of order exactly \(n\)
at \(R\).

At \(W_0\), one has \(\operatorname{ord}(x)=2\) and
\(\operatorname{ord}(y)=-1\). Since \(b(0)\ne0\), the
numerator has pole order one; division by \(x^d\) gives pole
order \(2d+1=n\).

At \(W_\infty\), one has
\(\operatorname{ord}(x)=-2\), \(\operatorname{ord}(y)=-3\).
The term \(a\) has pole order \(2d\), while \(by\) has
pole order at most \(2d-1\). They cannot cancel.
Division by \(x^d\) therefore makes \(f\) a unit there.
At all other points it has no pole. It follows that
\[
                         \operatorname{div}(f)=n(R-W_0).
                                                               \tag{R4}
\]
This is the exact divisor statement needed for the theorem.

The class \([R-W_0]\) is nonzero: \(R\ne W_0\), and a
principal divisor \(R-W_0\) would give a degree-one map
from a genus-two curve to the projective line. Thus its
exact order \(m\) is a nontrivial odd divisor of \(n\).

## 4. Primitive orbit coverage without an unnecessary exact-order test

The independent verifier enumerates the powers of two and
their negatives modulo each supplied \(n\), and obtains
\[
                        \langle2,-1\rangle=(\mathbf Z/n)^\times.
\]
The doubling orders are respectively \(12,4,10,12,18,3,4\).
For \(n=7,39\), the sign adds the second doubling orbit;
for the other rows there is a single primitive doubling orbit.

For every divisor \(m\mid n\), the reduction map
\[
                     (\mathbf Z/n)^\times\longrightarrow
                     (\mathbf Z/m)^\times
\]
is surjective. This follows prime by prime from CRT (and is
also explicitly verified for these small integers). Hence
\(\langle2,-1\rangle=(\mathbf Z/m)^\times\) for the actual
nontrivial order \(m\) of \([R-W_0]\).

The theta curve is symmetric; here this follows directly
from \(R+\iota R\sim2W_0\).
It contains both the torsion class and its negative.
Thus every primitive doubling orbit modulo its **actual**
order has a theta hit. A.C2.5 makes every primitive
character block Frobenius-nilpotent, and A.C2.19--20 supplies
point-section injectivity.

In particular, the row with annihilator 39 is sufficient
without claiming its exact order is 39. Its possible
nontrivial orders are \(3,13,39\), and the same argument
handles each. No negative torsion test or extra Jacobian
computation is needed.

## 5. Complete coverage and final scope

Coefficientwise squaring fixes the first two representative
pairs and pairs each of the other five with a distinct
conjugate. The independent verifier checks that these
orbits are disjoint and exhaust
\[
                      \mathbf F_4^\times\times\mathbf F_4.
\]
Thus the certificates treat all twelve geometric rank-one
classes, including all their forms over finite extensions
and finitely generated fields in the existing theorem's scope.

Combining this with the already proved ordinary case
A.C2.25, and the previously proved two-rank-zero case,
gives point-section injectivity for **every genus-two curve
over \(\mathbf F_4\)**, and for finite-extension forms of
these geometric curves and their hyperbolic open subcurves.
It does not cover every genus-two curve over every finite
field merely by extending the base field: a new geometric
moduli class need not descend to \(\mathbf F_4\).
Universal A1 remains outside this result.

## 6. Coefficient cross-check and a retracted preliminary calculation

For clarity, the correct special degree-five expansion is
\[
\begin{aligned}
 x\,\operatorname{Norm}(y+u x^2+v x+w)
  ={}&u^2x^5+A x^4+(v^2+u)x^3\\
    &+(B+v)x^2+(w^2+w)x+1.
\end{aligned}
\]
An initial unintegrated message misplaced the \(v\) term;
that message was explicitly retracted before any proof
was integrated. The corrected comparison gives
\(v=B\), \(u=B^2\), and \(A^5=B^{16}\), with \(B\ne0\),
in agreement with A.C2.3. The seven-row verification above
uses the full correct identity (R2) and is independent of
that preliminary calculation.

**Final conclusion:** the exact classification, Raynaud
origin, all seven positive divisor certificates, primitive
orbit implication, and twelve-class coverage pass.

