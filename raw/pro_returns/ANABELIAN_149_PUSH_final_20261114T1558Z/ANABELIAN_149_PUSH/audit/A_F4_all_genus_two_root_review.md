# Root review: every genus-two curve over F4

**Date:** 14 November 2026. **Outcome:** PASS as a mathematical candidate,
pending the deliberate checkpoint-10 integration freeze. This review approves
the precise finite-moduli assertion, not universal A1 or A2.

We read all six sections of `audit/A_F4_all_genus_two_candidate.md`, the
standalone author verifier `code/A_F4_rank_one_norm_checks.py`, and the full
independent review `audit/A_F4_rank_one_degeneration_review.md`. We reran both
the author verifier and `code/A_F4_rank_one_degeneration.py`; both passed all
seven fixed polynomial identities and the twelve-class coverage test.
The fixed witness SHA-256 is
`82dd18cfcfac963e1a4217e03a55b39a47766ee521c6601f3704e9828b417ec3`.

## Geometric classification and scope

The genus and two-rank formulas force precisely two reduced Artin--Schreier
poles, of orders three and one. Their distinct ramification jumps force every
geometric isomorphism to preserve each branch value. After placing them at
infinity and zero, normalizing the simple-pole coefficient gives

\[
 C(A,B):\qquad y^2+y=A x^3+B x+1/x,\qquad A\ne0.
\]

An allowed base automorphism is a scaling. A nonconstant Artin--Schreier
correction has an even highest pole order, so it cannot equal a nonzero
difference of the reduced odd-pole expressions. The simple-pole coefficient
therefore fixes the scaling, and the normalized pair is a complete geometric
invariant. Fourth-power Frobenius fixes the class exactly when
\(A\in\mathbf F_4^*\) and \(B\in\mathbf F_4\). The twelve classes have the
seven conjugacy representatives in the candidate. No descent of an arbitrary
field-of-moduli point is assumed: each representative equation is already
defined over F4.

We independently opened Elkin and Pries, *Ekedahl--Oort strata of hyperelliptic
curves in characteristic 2*, https://arxiv.org/pdf/1007.1226, retrieval
`turn833view0`. Notation 1.1, author page 2, and Section 3.1, author page 5,
give the reduced odd-pole presentation, the genus formula, and the formula
two-rank = number of poles minus one. The uniqueness argument and this exact
twelve-class conclusion are proved here; they are not attributed to an
unstated theorem in that paper.

## Theta origin and complete divisor identity

The different divisor is \(2W_0+4W_\infty\). Subtracting the pullback of
the base pole divisor of \(dx\) gives \(\operatorname{div}(dx)=2W_0\).
Thus the Raynaud line bundle is \(\mathcal O(W_0)\), with its locally exact
differential/Frobenius module structure, and
\(\Theta=\{[R-W_0]\}\). This origin is essential in the nonordinary
stratum; the zero class itself is on theta and is not a witness.

For odd \(n>1\), put \(d=(n-1)/2\). The displayed polynomial identity

\[
 x(a^2+ab)+b^2(Ax^4+Bx^2+1)=c(x+t)^n
\]

is exactly the norm of \(q=(a+by)/x^d\), after multiplication by the
appropriate power of x. The degree restrictions imply that q is regular at
infinity. At W0, \(v(x)=2\), \(v(y)=-1\), and \(b(0)\ne0\), so its pole
order is exactly n. The point R over the nonbranch coordinate t is a zero,
while its hyperelliptic conjugate is not a zero because \(b(t)\ne0\).
The unramified norm identity therefore gives
\(\operatorname{div}(q)=n(R-W_0)\), with no omitted zeros or poles.

Since \(R\ne W_0\), the Abel class is nonzero: a principal difference of
two distinct points would give a degree-one map to the projective line.
Its actual odd order e is a nontrivial divisor of n. The stored discovery
schema calls its field `exact_order`; the fixed-identity verifier and this
proof use that number only as an annihilator. No exact-order-39 assertion
is needed or approved by the norm check alone.

## Finite arithmetic and primitive-orbit implication

Both reruns verified every coefficient of all seven identities, rather than
point counts or a random subset. The binary quotient fields have complete
nonzero generator cycles, so every nonzero element is a unit; this certifies
that they really are fields. Both programs check the embedded F4 labels,
the original curve-point equations, both local nonvanishing conditions,
and the full unit groups for n in {5,7,11,13,19,39}.

For each n, \(\langle2,-1\rangle=(\mathbf Z/n)^*\). Reduction of units
modulo a divisor e is surjective by the prime-power decomposition and CRT,
so the same assertion holds at the actual order e. Theta is symmetric
because \(R+\iota(R)\sim2W_0\). Consequently each primitive doubling
orbit modulo e contains one of the two verified theta classes
\(\pm[R-W_0]\). A.C2.5 then kills every primitive Frobenius cycle, and
A.C2.19 (equivalently A.C2.20) supplies section injectivity. This uses the
whole actual torsion class, not a primary projection that might leave theta.

Coefficientwise squaring transports the equations and divisors to the five
other classes. The independently checked parameter coverage is precisely
\(\mathbf F_4^*\times\mathbf F_4\). Rank two is supplied by A.C2.25. At
rank zero the geometric two-primary torsion is zero, and A.1 plus the
injective Abel map excludes a collision directly. These three strata exhaust
all smooth proper geometrically connected genus-two curves over F4.

The finite-extension, finitely generated form, and open-subcurve conclusions
use the already proved comparison maps A.3/A.8: the isomorphism and cover
data descend after a finite extension of the whole base field, and a
collision persists on restriction and under the map to the compactification.
There is no inference that arbitrary genus-two moduli over Fbar2 descend to
F4. The universal problem remains explicitly unresolved.

**Approved:** A.C2.26 with the exact candidate statement and proof, once the
source freeze is released. No priority is claimed.


## Integrated-proof readback

Root subsequently read all of `sections/A_F4_all_genus_two.tex`, including the added64-class count. The complete norm/divisor and actual-order proof is retained. Root opened Cardona, Nart, and Pujolàs, the primary arXiv:math/0210105 manuscript, Proposition14 (printedp14), Theorem20 (p19), and Theorem22/Corollary23 (p21), retrievals turn844view3, turn845view3--4, and turn846view2--3. The normal form, unique scaling, geometric invariant coordinates and field-of-moduli/definition distinction match the use. The64 geometric classes are distinguished from arithmetic twists. The integrated statement and proof pass.
