# The actual free coordinate-swap quotient

Research proof, twenty-first hour. All unadorned fundamental groups are
discrete, with the ordinary analytic topology on the displayed complex
surfaces. Completion means full profinite completion. This is a new
coordinate and finite-cover comparison for the actual surface Z, not a
decision of either main problem.

## 1. The free quotient and its literal involution

We retain exactly the Z and based involution F of B87--B105 and of
records/reflection_pencil_20h.md. In particular q=vw belongs to
B0=C minus ({0} union mu5), and v=w is removed. The ordinary coordinate
swap sigma(v,w)=(w,v) therefore acts freely. The invariant coordinates
s=v+w and q=vw identify its quotient Q with an open subset of
B0 times the affine s-line. The quotient map Z to Q is an unramified
double covering, not a branched quotient on these actual open spaces.
Indeed the two inverse points are the roots of X^2-sX+q, and its
discriminant s^2-4q is removed.

For fixed q, the maps on v are F(v)=(v-q)/(v-1) and sigma(v)=q/v.
They commute and square to the identity. The literal based map F
descends to

 F_Q(s,q)=((4q-(1+q)s)/(q+1-s),q).

The denominator vanishes precisely on the already removed divisor
s=q+1, where v=1 or w=1. Its two fixed sections are s=2 and s=2q;
they are distinct because q=1 is removed. We use the projective fiber
coordinate

 t=(s-2)/(s-2q),  s=2(qt-1)/(t-1).

This is an isomorphism of projective line bundles over B0, and F_Q
becomes t to -t. The original affine s-line omits t=1, while the
removed divisor s=q+1 becomes t=-1. Infinity in the t coordinate is
allowed where the further divisors do not remove it.

Put U=mu5 minus {1}, and, for u in U, put

 T_u(q)=(q+u^2-2u)/(u^2+(1-2u)q).

Then Q is exactly the complement, in B0 times P1_t, of

 t=1, t=-1, qt^2=1, and t=T_u(q), t=-T_u(q), u in U.

All graph equations are projective equations, including their poles.
There is no omitted pole fiber. The A-family pair v=u or w=u has
s=u+q/u and hence t=T_u(q). Its F-image has t=-T_u(q). The branch
discriminant becomes

 s^2-4q=4(q-1)(qt^2-1)/(t-1)^2.

These identities prove both containment directions and all removed
factors; no auxiliary deletion is made. At a generic q the fiber has
twelve punctures on P1, so its fundamental group is free of rank11.
Its double cover is the original twenty-two-punctured sphere with
free fundamental group of rank21.

The actual base point P=(399/200,1/200) maps to
(q,t)=(399/40000,0). In the earlier reflection chart one has t=-b/a,
and the double cover is

 a^2=(q-1)/(qt^2-1), b=-ta.

These are affine-chart equations; the covering across t=infinity is
read in the b coordinate. At t=infinity, b^2=(q-1)/q, which is nonzero
on B0. Thus this chart expression does not create a branch at infinity.

## 2. Exact collisions and the two fixed sources

Write d_u=u^2+(1-2u)q. Direct polynomial identities give

 d_u(T_u-1)=2u(q-1),
 d_u(T_u+1)=2(1-u)(q-u),
 d_u^2(qT_u^2-1)=(q-1)(q-u^2)^2,
 d_ud_r(T_u-T_r)=2(u-r)(q-1)(q-ur),
 d_ud_r(T_u+T_r)=-2(q+ur-r-u)(q(r+u-1)-ur).

For distinct u,r, all same-sign collisions, and all incidences with
the branch curve or with t=+-1, occur over already removed fifth
roots of unity. The only further graph collisions are opposite-sign
ones, at

 q=u+r-ur or q=ur/(u+r-1).

For u=r these are respectively
alpha_u=u(2-u), beta_u=u^2/(2u-1), where the opposite graphs meet at
t=0 and t=infinity. This is an exact factorization of the actual
collision equations, not a finite numerical sample.

The fixed locus of F_Q is the disjoint union

 D0={(q,0):q in B0 minus {alpha_u:u in U}},
 Dinf={(q,infinity):q in B0 minus {beta_u:u in U}}.

The four alpha values are distinct and have absolute value greater
than1: |alpha_u|=|2-u|>1; equality alpha_u=alpha_r implies
(u-r)(2-u-r)=0 and forces u=r. The beta values are their reciprocal
complex conjugates, so are distinct, nonzero, and have absolute value
less than1. Hence each displayed source is an affine line with ten
punctures and has fundamental group F10.

The inverse image of D0 in Z is precisely the actual fixed source
S={v+w=2}. It is connected: the cover is obtained by adjoining
sqrt(1-q), whose monodromy around the omitted q=1 is nontrivial.
It is an unramified double cover of D0 and has fundamental group F19,
in agreement with the earlier explicit source computation. The
inverse image of Dinf is the fixed locus of F sigma, not of F.

## 3. Equivalence of the selected fixed-source comparison

Let Gamma=pi1(Q,Pbar), H=pi1(Z,P), and identify H with its index-two
image in Gamma. Let epsilon:Gamma to C2 be the monodromy of the
cover. Since F commutes with sigma and fixes P, it induces literal
compatible based involutions on H and Gamma. Let J be the image of
pi1(D0,Pbar) in Gamma, and let I_S be the image of pi1(S,P) in H.
No source injection is assumed. The covering pullback proves

 J intersect H=I_S,  epsilon(J)=C2.

The first identity follows even if the source map has a kernel:
an element represented by a source loop lies in H exactly when that
loop has trivial double-cover monodromy, precisely the condition for
lifting to a closed loop in S. The second follows from q=1 monodromy.
Both J and I_S are pointwise fixed by their respective involutions.

Consequently

 H^F=I_S if and only if Gamma^F=J.

One implication is intersection with H. For the converse, take any
F-fixed gamma in Gamma. If epsilon(gamma)=0, use the assumed equality
in H. If epsilon(gamma) is nonzero, choose j in J with the same
epsilon; then j^-1 gamma is fixed and belongs to H, so again belongs
to I_S. This proves the equality with J.

The same equivalence holds in full profinite completions:

 (Hhat)^F=closure(I_S) if and only if (Gammahat)^F=closure(J).

Here Hhat embeds as the open kernel of epsilonhat in Gammahat,
because H has finite index in Gamma and therefore carries its full
profinite topology. Similarly the source cover gives an index-two
open subgroup of pi1(D0)^. Continuous images of these compact source
groups are exactly the closures of their discrete images. Thus
closure(J) intersect Hhat=closure(I_S), with surjective epsilon on
closure(J), and the identical two-coset argument applies. This does
not replace an infinite-index subgroup by its completion.

This is a genuine equivalence of the actual selected fixed-source
gate. It does not prove either side: the critical mixed fibers remain
in Q and cannot be removed by invoking the generic bundle.

## 4. Verification, motivation, and the remaining global question

code/swap_quotient21.py checks22 exact rational identities, including
both coordinate inverses, the V4 action, all displayed collision
factorizations except the last which is output factored directly,
the cover equation, and the actual base point. Genuine successful
output is records/swap_quotient21.json/.out/.err. Two initial failed
attempts are retained with their exact sources and errors in the
corresponding failed_attempt01 and failed_attempt02 directories.
The first corrected a mistyped sum in the old reflection chart; the
second corrected the scope of a symbolic substitution. Neither
failed run is counted as a verification.

The additional V4-invariant rational function is

 h(v)=(v^2-q)^2/(4v(v-1)(v-q))
     =(s^2-4q)/(4(s-q-1))=(qt^2-1)/(t^2-1).

Its invariance is verified algebraically. This resembles the x-map
of multiplication by2 on a Legendre elliptic curve, but no elliptic
comparison theorem is invoked or needed for the present proof.

An independent geometric observation under review is that each T_u
is an inverse Blaschke factor: its zero is alpha_u outside the unit
disk and its pole is beta_u=1/conjugate(alpha_u) inside it, while its
modulus on the unit circle is1. Hence all further punctures satisfy
|t|>1 over |q|<1 and |t|<1 over |q|>1, except the retained t=+-1.
This may support compatible inner and outer markings. Such a global
marking, including the retained branch curve and all based transport,
has not yet been constructed. No simultaneous normal-form or
critical-filling fixed-lifting conclusion is asserted.
