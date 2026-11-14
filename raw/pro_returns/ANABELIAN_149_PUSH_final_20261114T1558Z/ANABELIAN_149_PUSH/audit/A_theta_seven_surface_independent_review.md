# Independent review of the theta-seven surface (proposed A.C2.15)

Reviewer: Part-A finite-field agent. Date: 14 November 2026.

**Verdict: approved in the stated scope.** I read the complete candidate
audit/A_theta_seven_surface_candidate.md and its verifier. I independently
rederived the parameter map, principal parts, norm/divisor, character
argument, finite-fibre dimension argument, converse chart, and the
one-parameter boundary family. The only wording correction was to say
“finite extension of the field of definition” for a finitely generated
base; the author has made it. No universal theta-existence conclusion is
supported or asserted.

The separate exact implementation
code/A_theta_seven_surface_independent.py/.json passes. It imports none
of the candidate code. Its universal identities are calculated in
F2(x,t), and its finite calculations use
F16=F4[w]/(w²+w+α), α²+α+1=0, instead of the candidate’s binary
polynomial implementation. For each finite norm identity it evaluates
the cleared numerator, of degree at most seven, at all sixteen field
elements; thus the verification is a polynomial identity, not a
comparison at too few rational points. It reproduces all twelve
unordered good pairs, all twelve outside the cubic locus, and fourteen
parameters of the separate one-dimensional family.

## 1. The parameter space has the claimed exact degree

Write u=x(x+1). The zeros of H_t=u³/[(x+t)^5(x²+t)²] are
0,1,∞ with multiplicity three, while its poles are t of order five
and sqrt(t) of order four. All five points are distinct for t≠0,1.
Thus the map has degree nine. Direct differentiation gives

- q_t'=(x+t)^6(x²+t)/u²;
- H_t=q_t/(q_t')²;
- H_t'=u²/[(x+t)^6(x²+t)].

In particular there are no additional ramification points over
G_m. Over the proposed two-dimensional base, the polynomial
F=λ(x+t)^5(x²+t)²+u³ has degree nine and unit leading coefficient.
Substitution at 0,1,t,sqrt(t) shows that all excluded factors
are units in the finite algebra. Its derivative, reduced using F=0,
is u²(x²+t)/(x+t), also a unit. Hence the degree-nine cover is
finite étale over the entire stated base, not merely generically.
The complement of the diagonal in its fibre square is open and
closed in a finite étale cover, and has rank 9·8=72.
This proves nonemptiness, smoothness and pure dimension two without
requiring the parameter cover to be geometrically connected.
Each of its components is legitimate for the later dimension claim.

## 2. Principal-part cancellation is exact

At r let z=x+r and e=r+s. Then B=z(e+z), and
1/B²=e^−2 z^−2 plus a regular series; notably there is no
z^−1 term. Therefore κq_t/B² has principal coefficients
κq_t(r)/e² and κq_t'(r)/e². Since κ/e²=H_t(r),
these equal ρ_r² and ρ_r, respectively, because

H_t q_t' = q_t/q_t' = (x+t)u/(x²+t),
H_t q_t = (q_t/q_t')².

The same holds at s by the defining equality H_t(r)=H_t(s).
Squaring v introduces no cross terms in characteristic two.
Thus v²+v cancels both apparent poles completely.

Only 0,1,∞ remain. Their principal coefficients are exactly
b,c,a, respectively. Hence Φ−φ is constant. Since v(t)=0
and q_t(t)=0, that constant is φ(t). This proves S7.9
uniformly, including every parameter in the finite étale chart.
There is no loss at a pole, a zero of B, or infinity.

## 3. The norm produces exact theta seven-torsion

Set β²+β=φ(t), h=A+B(y+β). The Artin–Schreier conjugate
is h+B and the proved rational identity gives
Nm(h)=κ(x+t)^7/u. At R_t=(t,β), A(t)=0 while B(t)≠0.
Thus exactly one point of the unramified fibre is a zero,
and its order is seven.

At W0 and W1 the y-term has pole order one because B is
nonzero at both branch coordinates. At infinity, x²y has pole
order five and is the only term of that order: A and βB have
degree at most two, hence pole order at most four.
Thus div(h)=7R_t−W0−W1−5W∞ exactly, and
div(h/u³)=7(R_t−B_C).

The differential divisor, theta translate and ordinariness are
the same directly checked data as in A.C2.13. The class
O(R_t−B_C) cannot vanish: it would put the origin on ordinary
Raynaud theta, or make 2R_t canonical despite R_t being
non-Weierstrass. Hence it has exact order seven.
All Kummer valuations are divisible by seven and the class has
exact order seven, so the cover is geometrically connected and
étale, of genus eight. The ordinary base has two-rank two.

## 4. Character and point-section implications

The two nontrivial doubling orbits modulo seven are negatives.
Theta symmetry puts one point in each orbit, so each cycle of
one-dimensional H1 character spaces has a zero Frobenius arrow.
Both new cycles are nilpotent; only the invariant stable rank
two remains. The deck group acts trivially on geometric
two-torsion and, since its order is odd, on all two-primary
torsion by the pro-two congruence-kernel argument.

A.C2.7 then applies exactly as stated. The nontrivial deck
transformation is free; it cannot fix the difference of lifts
of two distinct base points, since that would produce distinct
linearly equivalent effective divisors of degree two on the
upstairs nonhyperelliptic curve. Nonhyperellipticity follows
from the free order-seven action: on a hyperelliptic curve,
it would descend faithfully to a line automorphism, have a
fixed base coordinate, and hence fix a point in a fibre of
size at most two. This is impossible for a free action.
No estimate on finite rational point counts is used.

All maps, the point and the Kummer line descend after a finite
extension of a finitely generated field of definition. Thus
the argument covers the stated forms and all finite
extensions, and the already proved proper-to-open reduction
gives the open variants.

## 5. Finite fibres and the moduli dimension

For fixed coefficients, each parameter gives a point R_t
in the finite set Θ∩J[7]. The Abel map is injective, so
there are at most 7^4−1 choices of R_t.
Its required h divisor is fixed; h is unique up to scalar.
The six functions

1, x, x², y, xy, x²y

are independent and have the allowed poles in
L(W0+W1+5W∞), whose dimension is six by Riemann–Roch.
The order-five infinity pole makes the x²y coefficient
nonzero. Normalizing B to be monic therefore fixes the
scalar. Its two ordered roots give at most two parameter
choices. This proves a genuine finite-fibre bound, rather
than an inference from the number of formal parameters.

A geometric isomorphism of the genus-two curves preserves
the unique hyperelliptic pencil and permutes its three branch
coordinates. There are only six relevant Möbius maps.
After one of them, an Artin–Schreier change between two
simple-pole normal forms must add a constant: a pole of
the changing function would give an uncancellable pole
of even order at least two in its square plus itself.
Thus there are only finitely many normalized coefficient
triples per geometric moduli point. Each surface component
has a two-dimensional moduli image.

The explicit F16 point has nonzero cubic obstruction, as
independently verified. A component through it therefore
has a nonempty open part outside the earlier cubic locus;
its image still has dimension two by the finite-fibre result.

## 6. Converse chart and the inseparable-B family

For an arbitrary theta-seven point on an ordinary normalized
curve, multiply its seventh-power divisor function by u³.
The resulting h has exactly the required poles, lies in
the six-dimensional space above, and has B monic quadratic.
The point cannot be Weierstrass, so t avoids 0,1,∞, and
the sole-zero condition gives B(t)≠0; the simple poles
give B(0)B(1)≠0.

If B has distinct roots r,s, the same local equations
force κ/e²=q_t(r)/q_t'(r)²=H_t(r), and likewise at s.
A root with r²=t would have q_t'(r)=0 but q_t(r)≠0:
the required Artin–Schreier residue would be zero while
its square would have to be nonzero. This excludes that
case. The normalization v(t)=0 then fixes the constant
term and recovers exactly the displayed chart.
No double-root boundary is implicitly claimed.

For the independent one-parameter family put U=t(t+1).
The coefficients satisfy b=a t^5,c=a(t+1)^5 and aU²=1.
It follows directly that φ(t)=a(t+1) and, with z=x+t,

u(φ(x)+φ(t))=z+a z³.

Taking A=z and B=z²+U gives the two displayed norm
expansions, whose sum is a z^7.
Also a+b+c=(U+1)/U and abc=1/U, so the cubic obstruction
is exactly (U³+U+1)/U³. The family is nonisotrivial and
contains the A.C2.13 point at U=1 as claimed.

## Scope retained

This gives an explicit two-dimensional positive locus and
a separate nonisotrivial boundary family. It does not prove
that every ordinary genus-two curve has theta seven-torsion,
or that nonordinary covers necessarily have a useful deck
kernel. The finite-prime obstruction A.C2.14 remains
consistent with the construction.

