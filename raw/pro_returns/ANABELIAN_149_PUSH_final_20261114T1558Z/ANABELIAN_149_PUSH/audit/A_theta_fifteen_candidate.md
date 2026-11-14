# An exact theta-fifteen point and the remaining split-branch F4 example

Status: accepted after independent root review and integrated as A.C2.18
in sections/A_char2_deck.tex. Its primitive-Prym criterion is A.C2.17
in sections/A_primitive_prym.tex. Both complete proofs and the exact
fifteen certificate were independently reviewed before integration.
Written 14 November 2026.

## 1. Statement and curve

Let α²+α+1=0 and

C/F4: y²+y=x+α/x+α/(x+1).

The curve is ordinary of genus two. Its Raynaud theta has no points
killed by3 or5, but contains an explicit point of exact order15.
The associated cyclic étale degree15 cover D has genus16 and
two-rank8. Its deck action on two-primary torsion is faithful.
Nevertheless its entire primitive conductor15 part has two-rank
zero, and the degree-four primitive Abel–Prym criterion proves A1
for C. Thus absence of a nontrivial full deck kernel does not prevent
this stronger construction.

The conclusion applies over every finite extension and to all
finitely generated forms and hyperbolic open subcurves.
Together with the earlier results, it treats every ordinary
genus-two curve over F4 whose three hyperelliptic ramification
points are rational. No assertion is made for all ordinary F4
curves with a nontrivial Frobenius permutation of those points.

## 2. Theta characteristic and the small-order exclusions

Let Bθ=W0+W1−W∞, u=x(x+1).
The same direct differential calculation as A.C2.13 gives
div(dx)=2Bθ and the locally exact differential bundle O(Bθ).
The two logarithmic differentials dx/x and dx/(x+1) prove
ordinariness. Thus

Θ={O(R−Bθ):R∈C(kbar)}

is symmetric and does not contain the origin.

The cubic obstruction in A.C2.2 is

(1+α+α)^3+α²=1+α²=α≠0,

so theta has no nonzero3-torsion, and none including zero.

For theta-five, the complete high-jet criterion is proved in
audit/A_theta_Hankel_scan.md. Its application here is short enough
to reproduce. Let ξ be a proposed nonbranch x-coordinate and
Dξ=ξ(ξ+1). After clearing denominators, the first four local
coefficients of y+β at ξ are

P1=ξ⁴+ξ²+α,
P2=ξ⁸+α²ξ⁴+αξ+α²,
P3=α(ξ⁴+ξ²),
P4=ξ¹⁶+αξ¹⁰+αξ⁹+αξ³+α²ξ²+α.

A function with divisor5R−W0−W1−3W∞ is A+B(y+β) with
A,B linear. Cancellation of its jets through degree4
requires the matrix

[[P2,P1],[P3,P2],[P4,P3]]

to have rank at most one. The first minor is

P2²+P1P3=(ξ⁴+ξ+α)^4.

Modulo f=ξ⁴+ξ+α, the four coefficients reduce, for
D=ξ²+ξ, to

(D,D+1,αD+α²,αD+1).

The other minor P2P3+P1P4 then equals α².
This contradiction proves Θ∩J[5]=empty.
A ramification point cannot supply missing odd theta torsion,
since its difference from Bθ is killed by2.
The exclusions are therefore geometric and complete.

## 3. The exact order-fifteen function

Choose t with

t²+αt+1=0,

so t lies in F16, t⁴+t=α and t is different from0,1.
Set β²+β=αt and R=(t,β).
The curve equation at t has value αt.
Its absolute trace from F16 to F2 is one, so β may be
taken in F256.

Define polynomials A,B by their coefficients in ascending powers
of x:

A=[
 α²+t,
 αt,
 t,
 1+t,
 α²+αt,
 1+α²t,
 1+t
],

B=[
 α,
 α+t,
 α+t,
 1+t,
 α²t,
 αt,
 1
].

With F=x³+x²+α=u φ(x), the exact polynomial identity is

u(A²+AB)+B²(F+αt u)=(x+t)^15.                  (F15.1)

It is checked over F2[α,t]/(α²+α+1,t²+αt+1)
by the author certificate and independently by root.
The required local values are

A(t)=0,  B(t)=t,  B(0)=B(1)=α.

Put h=A+B(y+β). Its Artin–Schreier conjugate is h+B,
and (F15.1) gives

Nm(h)=(x+t)^15/u.

At R the function h vanishes and its conjugate has value t≠0.
The x-map is étale there, so h has its sole zero at R,
of exact order15. At W0,W1 the coefficient α of the
pole of y is nonzero, giving a simple pole at each.
At infinity the monic term x^6y has unique largest
pole order13; A and βB have pole order at most12.
Hence

div(h)=15R−W0−W1−13W∞,
div(h/u^7)=15(R−Bθ).                           (F15.2)

Thus η=O(R−Bθ) is theta torsion killed by15.
It cannot have order1,3,or5 by the preceding exclusions.
Its exact order is15.

The normalization z^15=h/u^7 is geometrically connected:
exact order of the associated torsion line bundle gives a
connected μ15-torsor. It is étale since every valuation is
divisible by15. All15-th roots of unity already lie in
F16. After the needed constant extension it is a cyclic
Galois cover; its genus is1+15(2−1)=16.

## 4. The surviving and killed character parts

The nonzero doubling orbits modulo15 are

{1,2,4,8}, {7,14,13,11}, {3,6,12,9}, {5,10}.

The first two are primitive conductor15 orbits and are
negatives of each other. They meet theta at η and−η,
respectively, so every primitive character space is
Frobenius-nilpotent. The conductor5 orbit and conductor3
orbit survive: every point in them is nonzero5- or
3-torsion, and the theta exclusions just proved apply.
Their one-dimensional arrows are bijective.
The ordinary invariant part has rank2.
Consequently

f(D)=2+4+2=8.

The surviving characters3 and5 have kernels of coprime
orders3 and5 in C15, so their common kernel is trivial.
Thus the full geometric deck action on two-torsion
(and hence on the two-primary Tate module) is faithful.
The earlier A.C2.7 nonfaithful-deck criterion does not
apply to this cover.

## 5. Why the primitive part still separates point sections

This is the special n=15 application of the companion
criterion audit/A_two_prime_prym_candidate.md.
Let σ generate the free cyclic15 deck group.
The operator

u_prim=(1−σ³)(1−σ⁵)

kills every surviving two-primary character: conductor3
is killed by one factor, conductor5 by the other,
and the invariant part by both.
Hence it kills every two-primary point of J_D.

A section collision downstairs lifts to P',Q' on D with
two-primary difference. Applying u_prim gives an equivalence
of effective divisors of degree4:

Q'+σ⁸Q'+σ³P'+σ⁵P'
  ~ σ³Q'+σ⁵Q'+P'+σ⁸P'.

The divisors are distinct because P',Q' lie in different
deck orbits, and the deck action is free.
They would therefore give a degree-at-most-four map to P1.

The companion proof excludes such a map using g(D)=16,
the free odd deck action and f(D)=8.
For clarity, its mechanism is as follows.
Castelnuovo–Severi makes a degree3 pencil unique, and
a distinct pair of degree4 pencils can only factor
through a degree2 genus-at-most-one quotient because
16>(4−1)². The hyperelliptic case is impossible for
a free odd action. A bielliptic involution, if present,
is unique since two independent double-elliptic maps
would force genus at most5. Thus the cyclic15 group
centralizes it. Its nonempty fixed set has cardinality
divisible by15; Riemann–Hurwitz bounds that cardinality
by15 because the different has total degree30 and each
wild fixed point contributes at least2. The cardinality
is therefore15. The Deuring–Shafarevich formula forces
f(D)≥14, contrary to8. An invariant pencil of degree≤4
is equally impossible: a fixed coordinate of the odd
action on P1 would have a fibre of degree≤4 partitioned
into free orbits of size15. The companion audit contains
the full factorization and source checks.

Thus the divisor equivalence cannot occur, proving A1
for the stated curve by the now accepted A.C2.17 criterion. The same finite-field-extension and finitely
generated descent arguments as A.C2.15–16 apply.

## 6. All normalized nonzero F4 coefficient triples

The six branch-coordinate transformations permute a,b,c.
There are ten unordered triples from {1,α,α²}.

- The three equal triples satisfy the cubic positive
  condition and are covered by A.C2.1.
- (1,1,α) and its conjugate (1,1,α²) are covered by
  A.C2.11 and its constant-field conjugate.
- (1,α,α²) is A.C2.13.
- (α,α,α²) and (α,α²,α²) lie in the one-parameter
  family A.C2.15. Choose t²+t=U with U=α² orα:
  then a=U^−2 and t^5=(t+1)^5=U, so b=c=U^−1.
- (1,α,α) and its conjugate are the present mixed15 case.

Thus every normalized model over F4 with a,b,c nonzero is
covered. A constant Artin–Schreier term can be removed
after a finite extension, already allowed by the scope.
Every ordinary genus-two curve over F4 with three rational
ramification points has such a normalization, since its
hyperelliptic quotient has a rational point and all three
reduced Artin–Schreier poles are simple.
Ordinary curves whose branch points are not all rational
need not have normalized coefficients in F4 and are not
included in this enumeration.

## 7. Reproducibility and retained limitations

Author: code/A_theta_fifteen_certificate.py/.json, PASS.
Independent root:
code/A_theta_fifteen_root_independent.py/.json, PASS.
The latter uses a separate SymPy quotient-polynomial
implementation with the two field relations, independent
formal jets for the theta5 obstruction, and character checks.
The fixed identity is the proof certificate; its discovery
through the broader Hankel scan is not a substituted proof.

The broader exact scans are retained in
audit/A_theta_Hankel_scan.md and code/A_theta_F4_scan.py/.json.
They suggest further prime-power absences for this curve,
but no unbounded exclusion or universal cutoff is claimed.
The present positive result needs only the proved
3- and5-torsion exclusions, the explicit exact15 divisor,
and the separately reviewed primitive-Prym criterion.

