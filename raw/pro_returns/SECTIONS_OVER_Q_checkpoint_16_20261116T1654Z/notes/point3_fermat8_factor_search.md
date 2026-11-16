# Point-three Fermat-eight factor search

The curve under examination is the actual pointed Fermat twist

\[
3u^8-2v^8=1,\qquad (u,v)=(1,1).
\]

The completed result is A.182 in
`sections/point3_fermat8_decomposition.tex`: its actual product of
divisor-pushforward maps is an isogeny onto three elliptic curves,
six genus-two Jacobians and three two-dimensional Pryms. Every factor
is Q-simple and has an explicitly proved point of infinite order.
Thus the certified total rank is at least twelve. No upper bound for
the total rank has yet been established.

## Computation provenance

An exploratory input was submitted using the already-retained
harmonic_prym_magma_submit.py route before the parent reminded this
agent of an earlier automatic approval rejection for external uploads.
That historical rejection was absent from the agent's compacted state.
The request had completed before interruption. Its request, response
and output remain as point3_fermat8_prym_magma files. No further external
submissions are being made. Its runtime-error output is not used as
proof input for any result below.

The proof uses only local exact computation, with consolidated entry
point `code/point3_fermat8_decomposition_certificate.py`. That program
re-executes both surface certificates and checks every map, all 21
differential pullbacks including their nonzero rational scalars,
the finite group orders and irreducibility tests. All output/data are
retained. The old three-factor discussion below is an intermediate
part of this now-complete decomposition.

## Three literal genus-two quotients

There are the following actual intermediate hyperelliptic maps:

| Hyperelliptic equation | Map from the Fermat curve | Image of (1,1) |
|---|---|---|
| \(y^2=3x^8-2\) | \(x=u/v,\ y=1/v^4\) | \((1,1)\) |
| \(y^2=6x^8+3\) | \(x=v,\ y=3u^4\) | \((1,3)\) |
| \(y^2=6x^8-2\) | \(x=u,\ y=2v^4\) | \((1,2)\) |

Each smooth proper intermediate curve has genus three. Its two
degree-two quotients are

\[
(x,y)\longmapsto(x^2,y),\qquad
(x,y)\longmapsto(X,Y)=(x^2,xy).
\]

The first quotient has equation \(y^2=AX^4+B\) and genus one;
the second is \(G_{A,B}:Y^2=AX^5+BX\), of genus two.
The two involutions are \((x,y)\mapsto(-x,y)\) and
\((x,y)\mapsto(-x,-y)\). Their product is the hyperelliptic
involution. Pullback of their invariant differential spaces spans
all three holomorphic differentials, so the actual pull/push maps
give the corresponding elliptic/genus-two Jacobian isogeny.

## Exact positive-rank and simplicity certificates over Q

For the three pairs \((A,B)=(3,-2),(6,3),(6,-2)\), let
\(P=[(1,y_0)-\infty]\), with \(y_0=1,3,2\), respectively.
The polynomial \(AX^5+BX\) has discriminant supported only at two
and three. Its smooth odd-degree model therefore has good reduction
at every prime used in the certificate.

For the first Jacobian, the orders at seven and thirteen are 64 and
170. For the other two, the orders at five and seven are 26 and 64.
Prime-to-residue-characteristic torsion injection, using the other
prime to exclude torsion at each residue characteristic itself,
bounds rational torsion by order two. The class
\([(0,0)-\infty]\) has exact order two, since the divisor of \(X\)
is twice that divisor and a positive-genus curve has no degree-one
function. Thus rational torsion is exactly \(C_2\).

The double of \(P\) is not zero. In literal Mumford coordinates,

\[
\begin{array}{c|c|c}
(A,B)&u_{2P}&v_{2P}\\ \hline
(3,-2)&(X-1)^2&(13X-11)/2\\
(6,3)&(X-1)^2&(11X-5)/2\\
(6,-2)&(X-1)^2&7X-5.
\end{array}
\]

One can also see nonvanishing directly:
\(L(2\infty)=\langle1,X\rangle\), and no nonzero such function
has divisor \(2(1,y_0)-2\infty\), because \(y_0\ne0\).
Consequently each \(P\) has infinite order.

For \(G_{3,-2}\), the actual good Frobenius polynomial at thirteen
is \(T^4+169\). For \(G_{6,3}\) and \(G_{6,-2}\), the polynomial
at five is \(T^4+25\). The code counts the curves over the prime
field and its quadratic extension and derives these polynomials.
The polynomial \(T^4+p^2\), for either odd prime \(p\), is
irreducible over Q: a quadratic factorization with opposite
linear coefficients would require a rational square root of
\(2p\) or of \(-2p\); a factorization with zero linear
coefficients would require a square root of \(-p^2\).
There is no rational linear root.

Any proper positive-dimensional Q-isogeny factor would induce an
integral quadratic factor of every good Euler polynomial, by the
actual exact Tate-module sequence of the factor and quotient.
The displayed irreducible polynomial therefore proves that all
three Jacobians are Q-simple. Since each has positive rank,
none of these three genus-two quotients admits a nonzero
rank-zero abelian quotient over Q.

## Completion of the character decomposition

The six genus-two coefficient pairs are

`(3,-2), (6,3), (6,-2), (24,1), (3,1), (-8,9)`.

Their literal intermediate `(x,y)` maps appear in A.182.7.
All six rational torsion groups have order two by the retained
good-reduction counts. The class `(1,y0)-infinity` has nonzero
double, using `L(2 infinity)=<1,X>`, so has infinite order.
The selected good Euler polynomial is `T^4+169` at thirteen for
the first/fourth curves, and `T^4+25` at five for the others.
The elementary quadratic-factor test in A.182.20 proves each
irreducible, hence each Jacobian Q-simple.

The other three primitive factors are the actual images of
`1-iota` on the Jacobians of `w^4=A z^3+Bz`, with pairs
`(-12,1), (18,1), (3,-2)` and `iota(z,w)=(z,-w)`.
The Fermat maps are respectively

`z=-u^4/2,w=u v^2`; `z=v^4/3,w=u^2 v`;
`z=u^4/v^4,w=u/v^3`.

Each two-dimensional image has rational torsion order at most two.
Its rational class `[P-iota P]` is not killed by two: a function
with divisor `2P-2iota P` would contradict the explicit canonical
plane-quartic embedding. The independent full-rank jet certificate
also proves this nonvanishing. Selected irreducible Euler polynomials
are `T^4+8T^2+25` at five for the first two and
`T^4-24T^2+169` at thirteen for the third.

The old elliptic factors are `Y^2=X^3+cX` for
`c=-6,18,-12`, with actual rational points `(3,3),(6,18),(6,12)`.
All have torsion group of order two by the executed local counts,
so those three points have infinite order.

The exact differential table in A.182.13 uses every pair
`a,b>=1, a+b<=7` once in the plane-octic basis
`u^(a-1)v^(b-8)du`. It proves that the actual product map is
an isogeny, with dimensions `3+12+6=21`; no unproved character
decomposition or geometric-factor classification is imported.

Every nonzero Q-abelian quotient therefore contains the finite-kernel
image of a positive-rank simple factor. For a morphism over a number
field L into A/L, the explicit adjunction map from C8 into Res A,
followed by the pointed Jacobian universal map, has a nonzero
Q-abelian image B whenever the original map is nonconstant.
Since B(Q) is infinite and injects into A(L), this rules out a
nonconstant map to any abelian A with finite A(L), including after
finite extension. It does not classify Selmer sections and makes
no assertion about the new factors at N24.

## Exact primary source checks

The author PDF `https://jmilne.org/math/CourseNotes/AV.pdf`,
version 2.00, 16 March 2008, was opened at the following precise
statements:

- I, Proposition 10.1, printed p.42: the actual complement-isogeny
  construction. The final quotient argument in A.182 in fact uses
  the explicitly constructed product isogeny directly.
- I, Theorem 16.7, p.69: finite generation over a number field.
- II, Theorem 1.1, pp.75–76: the abelian variety finite-point formula.
- III, Proposition 6.1, p.104: the pointed Jacobian universal map.
- III, Theorem 11.1, p.118: the curve/Frobenius trace formula.
- IV, Theorem 3.5 and Corollary 3.6, pp.141–142: the exact
  good-reduction/Tate-module comparison used for the simplicity test.

Bibliography fragment: `notes/point3_fermat8_references.bib`.
