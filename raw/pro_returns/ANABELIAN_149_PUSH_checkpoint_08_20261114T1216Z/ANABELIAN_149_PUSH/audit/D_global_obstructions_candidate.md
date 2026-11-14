# Two precise obstructions to the proposed global section routes

Status: proved constructions, submitted for independent root review on 2026-11-14.
These statements do not refute any of the unresolved global section conjectures D1--D4.

## 1. Locally ordinary, density-one integral tangent data need not be rational

Let \(q_j\) be distinct increasing rational primes with \(q_j>2^{j^2}\), and put
\[
 A=\prod_{j\geq1}q_j^{j!}\in
 \widehat{\mathbf Q^\times}
 :=\varprojlim_n\mathbf Q^\times/(\mathbf Q^\times)^n.
\]
The product is well defined: modulo nth powers every factor with \(j\geq n\)
is trivial, and these finite products are compatible as n varies. Its valuation
coordinates are \(v_{q_j}(A)=j!\in\widehat{\mathbf Z}\), and all other valuation
coordinates are zero. Consequently A is not the image of a rational number:
every rational number has finite valuation support.

For every rational prime p, its image in \(\widehat{\mathbf Q_p^\times}\)
is represented by an actual element \(a_p\in\mathbf Q_p^\times\). One direct
proof uses \(\mathbf Q_p^\times=p^{\mathbf Z}\times\mathbf Z_p^\times\).
The power completion of its unit factor is the unit factor itself, so
\[
 \widehat{\mathbf Q_p^\times}
 =p^{\widehat{\mathbf Z}}\times\mathbf Z_p^\times.
\]
The valuation of A is an ordinary integer (either zero or j!), which proves
the assertion and uniqueness. Equivalently, delete the one possible term
q_j=p from the product. The remaining product converges p-adically: for
each r the exponent j! is eventually divisible by the exponent of
\((\mathbf Z/p^r\mathbf Z)^\times\), so every sufficiently late factor is
1 modulo p^r. This also proves compatibility with the power-completion
class. Thus
\[
 v_p(a_p)=\begin{cases}j!&p=q_j,\\0&p\notin\{q_j:j\geq1\}.
 \end{cases}
\]
The exceptional primes have Dirichlet density zero, since
\(\sum_jq_j^{-s}\leq\sum_j2^{-j^2}\) for every \(s\geq1\), while the
normalizing denominator \(\log(1/(s-1))\) diverges. They form an infinite
set. Therefore the local representatives are units at a set of primes of
Dirichlet density one, but not at all but finitely many primes. The real
local class has positive sign and is also ordinary.

This example is realised by a genuine continuous birational section, not
merely by an abstract collection of local classes. Fix the rational place
t=0 of \(\mathbf Q(t)\), a prolongation to a separable closure, and its
tangential split decomposition group
\[
 D_0\simeq\widehat{\mathbf Z}(1)\rtimes G_{\mathbf Q}
 \subset G_{\mathbf Q(t)}.
\]
For each j choose compatible roots of q_j and the resulting continuous
Kummer cocycle \(c_j:G_{\mathbf Q}\to\widehat{\mathbf Z}(1)\).
The series
\[
 c(g)=\sum_{j\geq1}j!c_j(g)
\]
converges uniformly in g modulo every n: all terms with j>=n vanish in
\(\mu_n\). It is a continuous cocycle. If s_0 is the standard tangential
split section, then
\[
 s_A(g)=i(c(g))s_0(g)
\]
is a continuous section of \(G_{\mathbf Q(t)}\to G_{\mathbf Q}\), with
image contained in D_0. Its pullback of the Kummer class of t is A.

More precisely, for \(f=t^r u(t)\), with u regular and nonzero at zero,
the restriction of the Kummer character of u to D_0 is the inflated
Kummer character of u(0); Hensel lifting gives this because
u/u(0) has constant term 1 and compatible roots in the strict henselian
local field. Hence
\[
 s_A^*\kappa(f)=rA+\kappa(u(0))
\]
in additive Kummer notation (or \(A^r u(0)\) multiplicatively). In
particular, the values of t-c for every nonzero rational c are the
ordinary rational values -c, while the value of t is A.

**Exact scope.** This refutes the unrestricted inference
``continuous birational section + locally ordinary tangent classes +
density-one integrality implies a rational tangent class/cofinite
integrality.'' It does not refute the existence or rationality of the
underlying place: that place is exactly zero. It does not yield a
noncuspidal counterexample on the thrice-punctured line. It also does not
survive as an obstruction in the proper unramified quotient, which kills
the place's inertia. This is why point reconstruction and rational tangent
reconstruction must be distinguished, and why an evaluation lemma must
exclude zeros and poles at the reconstructed place.

Independent check: /root/finite_field checked convergence, ordinary local
representability, continuous cocycle construction, and the regular-unit
evaluation formula on 2026-11-14.

## 2. A relevant Fermat quartic with no rank-zero standard elliptic quotient

Let
\[
 C:\quad x^4+2y^4=3z^4.
\]
This is a smooth projective genus-three curve over Q. Its partial
derivatives cannot vanish simultaneously at a projective point. The
affine open xyz!=0 maps to the thrice-punctured line by
\[
 t=\frac{x^4}{3z^4},\qquad 1-t=\frac{2y^4}{3z^4}.
\]
It is a fourth-power Fermat twist. The rational point P=(1:1:1) maps to
t=1/3, so the twist occurs for an actual geometric section of the base.

The three sign involutions yield genus-one quotient curves. For example
the x-sign quotient, in coordinates u=y/z and v=(x/z)^2, is
v^2=3-2u^4; its four distinct branch points show that its smooth completion
has genus one, and the image of P supplies a rational origin. The other
two quotients are obtained by permuting the role of x,y,z.

There are explicit maps to elliptic curves
\[
\begin{array}{c|c|c|c}
&E&X&Y\\\hline
x&Y^2=X^3-6X&-2y^2/z^2&-2x^2y/z^3\\
y&Y^2=X^3-12X&-2x^2/z^2&-4xy^2/z^3\\
z&Y^2=X^3+18X&3x^2/y^2&9xz^2/y^3.
\end{array}
\]
Each map factors through its indicated sign quotient. The factor from
that genus-one curve to E is nonconstant of degree two: in the general
quartic model v^2=A u^4+B, the formulas X=A u^2, Y=Auv give
Y^2=X^3+ABX, and a generic X has exactly two choices of u. Since source
and target are smooth projective genus-one curves with rational points,
translation of the target makes the map an isogeny. Thus E is in the
isogeny class of the indicated quotient Jacobian.

The rational images of P are
\[
 P_x=(-2,-2)\in E_x(\mathbf Q),\quad
 P_y=(-2,-4)\in E_y(\mathbf Q),\quad
 P_z=(3,9)\in E_z(\mathbf Q).
\]
All three points have infinite order. Here are sufficient complete
finite-field counts:
\[
\begin{array}{c|cc|c}
E& p&\#E(\mathbf F_p)&\text{second count}\\\hline
E_x&5&8&\#E_x(\mathbf F_{13})=18\\
E_y&5&10&\#E_y(\mathbf F_7)=8\\
E_z&5&10&\#E_z(\mathbf F_7)=8.
\end{array}
\]
All primes displayed are of good reduction, since the discriminant of
Y^2=X^3+AX is -64A^3. Prime-to-p torsion injects under good reduction.
For E_x, the 5-primary torsion is excluded using the count at 13, and
the 13-primary torsion using the count at 5; all other primary torsion
orders divide gcd(8,18)=2. The same argument for 5 and 7 applies to
E_y,E_z, with gcd(10,8)=2. Thus every rational torsion point has order
dividing two. Each listed point has nonzero Y, so is neither the identity
nor a point of order two. Each quotient Jacobian therefore has positive
Mordell--Weil rank.

The identities certifying the three rational maps can be checked without
symbolic algebra. Put F=x^4+2y^4-3z^4. After clearing denominators, the
residual Y^2-X^3-AX is respectively
\[
 4y^2F,\qquad 8x^2F,\qquad -27x^2F.
\]
The finite counts are exhaustive in the certificate
`code/D_Fermat_quartic_certificate.py`, whose output is retained as
`audit/D_Fermat_quartic_certificate.json`.

In fact **every elliptic target of C over Q has positive rank**, not only
the three displayed quotient isogeny classes. Let V be the Klein four
group of projective sign changes, with nonidentity elements
tau_x,tau_y,tau_z. The invariant function field is
Q(x^2/z^2,y^2/z^2), whose relation X^2+2Y^2=3 is a rational conic (it has
(X,Y)=(1,1)); hence C/V has genus zero. For each quotient map, pushforward
and pullback on Jacobians show that the full norm
1+tau_x+tau_y+tau_z acts as zero on J=Jac(C). Therefore in End(J) tensor Q
the operators e_i=(1+tau_i)/2 are orthogonal idempotents whose sum is 1.
Their images are the three genus-one quotient Jacobians up to isogeny.
It follows that J is Q-isogenous to their product. If C maps
nonconstantly to an elliptic curve E/Q, translate the image of P to the
origin. The induced map J->E is nonzero. Its composition with one factor
of this isogeny decomposition is nonzero; a nonzero homomorphism between
elliptic curves is an isogeny. Thus E is isogenous to one of E_x,E_y,E_z,
and has positive Mordell--Weil rank.

**Exact scope.** There is no universal argument that takes every
fourth-power Fermat twist arising from a section and chooses a rank-zero
elliptic target of that curve over Q.
Already a twist arising from a rational point defeats that assertion.
This does not rule out other covers, other twists, higher-genus descent,
or a different argument on this curve. It does not prove an exact rank,
make a Tate--Shafarevich assertion, or refute a section conjecture.

Primary torsion reference opened on 2026-11-14: J. S. Milne,
*Elliptic Curves*, second edition, Chapter II, Proposition 5.4 and
Corollary 5.7, printed p.66, https://www.jmilne.org/math/Books/EC2.pdf.
Our argument only uses the weaker prime-to-residue-characteristic
injectivity statement; every prime used in the certificate is odd.

## 3. The exact remaining local-to-global gap

Betts--Stix, *Galois sections and p-adic period mappings*, Annals of
Mathematics 201 (2025), 79--166, Theorem A, proves that for a number field
with no CM subfield and a smooth projective genus>=2 curve, the image
of the Selmer section set in X(k_v) is finite for each fixed finite v.
The primary author preprint, Definition 1.1 and Theorem A, pp.1--2, was
opened together with the publisher record on 2026-11-14:

* https://annals.math.princeton.edu/2025/201-1/p02
* https://www.math.uni-frankfurt.de/~stix/research/preprints/BETTS_STIX-GaloisSectionsPadicPeriods20220429.pdf

The checked proper local theorem makes proper global sections locally
geometric, so this finiteness result applies (with the usual real local
statement at real places). It does **not** assert that the finite sets at
different v lie in the base changes of one finite k-subscheme Z of X.
That common arithmetic finite support is the hypothesis needed by Stix's
finite-support corollary, using Stoll's Theorem 8.2. A singleton of X(k_v)
can already have generic scheme-theoretic image over k if its coordinates
are transcendental over k, so cardinal finiteness at one v cannot replace
that hypothesis.

Exact local primary text opened:
`background/literature/stix_birational_local_conditions/src_arXiv_1203.3236/STIX-birSCoverQthmAB-arXivv3.tex`,
section `Finite support`, the theorem labelled `thm:stoll`, corollary
`cor:stollforsections`, and `cor:nonconstantunit`. The density-one
integrality conclusion is Theorem 2 / `thmB`; the actual adelic condition
requires all but finitely many integral places (source section 4.1).

No additional published arithmetic statement checked in this pass fills
this common-support or cofinite-integrality gap. The two constructions
above isolate concrete invalid shortcuts without claiming the stronger
global statements false.
