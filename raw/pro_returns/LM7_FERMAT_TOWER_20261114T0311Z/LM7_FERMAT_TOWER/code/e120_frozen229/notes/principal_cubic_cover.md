# A framed cubic cover and the surviving augmentation coordinates

This is the next actual source comparison after the frozen logarithm
torsor calculation.  It constructs the cubic cover, the literal
norm-seven isogeny lift, and the maps from its based free group.  The
map on affine-cover homology kills both remaining intrinsic directions.
They survive primitively in the following augmentation extension, with
the two detecting coordinates given below.  Their arithmetic values
are still to be computed.

## 1. The actual proper cover and its original tangent

Use the already fixed function

    f_A0=(y+z)/(3(x+y)), div(f_A0)=3[A0]-3[O],
    f_A0=s^-3+terms of higher order, s=z/x at O.

The normalized cubic function-field cover u^3=f_A0 is the smooth
projective curve

    C: w^3-27u^3-18uwv-9v^3=0.                              (C1)

Its actual map to the original Fermat cubic is

    q[u:w:v]=[-3u^3-uwv : 3u^3+uwv+v^3 : -uwv-v^3].         (C2)

The sum of the first two coordinates is v^3, and the sum of the last
two is 3u^3.  Hence q* f_A0=(u/v)^3 exactly.  Substituting (C2) into
x^3+y^3+z^3 gives -u^3 v^3 times the left side of (C1).  The three
coordinates have no common zero on C: for v nonzero their first two
sum to v^3, and for v=0 the curve equation forces u nonzero.  Thus
(C2) is a morphism, not only a rational map.

For completeness, on v=1 put

    g1=9u^2+2w, g2=w^2-6u, g3=2uw+3.

The exact identity

    8u g1+12u^2 g2+10g3-3g3^2=3

proves smoothness away from 3; at v=0 the partial derivatives give
the same conclusion directly.  Thus C is a genus-one curve.  Its
specified rational zero is Q0=[1:3:0].  Over characteristic zero the
cubic Kummer cover is unramified at the divisor of f_A0, because every
order is divisible by 3; it is unramified elsewhere as well.  It is
connected because the divisor A0-O is a nonzero point of E[3], so
f_A0 has no cube root in K(E).  Consequently q is a degree-three
isogeny after taking Q0 as zero, with q(Q0)=O.

Write r=v/u at Q0.  Solving (C1) gives

    w/u=3+2r+r^3/27+O(r^4),
    q* s=r-r^2/3+O(r^4).                                   (C3)

In particular q carries the unit r-tangent to the original unit
s-tangent, and (u/v)*s has leading coefficient one.  This specifies
the cover branch over the original tangent exactly.  Its other two
points over O are [1:3zeta^j:0], with (u/v)*s=zeta^j.
The deck pullback is

    sigma(u/v)=zeta(u/v), sigma(w/v)=zeta^-1(w/v).

All generator maps below use the positive unit character fixed by
this root convention.

## 2. The literal pi lift and its tangent constant

Let pi=1+3zeta and theta=theta_pi be the frozen normalized function.
For f=f_A0, the frozen principal-distribution identity gives

    theta(Q-A0)^3/theta(Q)^3
       = f(Q)^7/(c_f f([pi]Q)), c_f=1/729.                   (C4)

The value and leading coefficient used here are literal:

    theta(A0)=-lambda, theta(Q)=(-D/(9pi))s^6+...,
    D=zeta*lambda.

Consequently theta(Q)/theta(Q-A0) has leading coefficient
zeta/(9pi) times s^6.  It follows from (C4) that the field map over
[pi] has the form

    u/v -> gamma (u/v)^7 theta(Q)/theta(Q-A0), gamma^3=729.

The lift which fixes Q0 must send the normalized pole u/v to a pole
with leading coefficient pi^-1, because its differential is pi.
This forces gamma*zeta/(9pi)=pi^-1, and therefore the exact lift is

    tilde(pi)*(u/v)=9zeta^2 (u/v)^7 theta(Q)/theta(Q-A0).       (C5)

There is no unused cube-root choice in (C5).  The other two choices
differ by the displayed deck translation and do not fix Q0.  The
field equation proves the map; its extension to the smooth proper
curves is a degree-seven isogeny.  It satisfies the literal square
q tilde(pi)=[pi] q.  Complex conjugation fixes (C1), (C2), Q0 and
the unit parameter.  It carries (C5) to the bar(pi) lift with constant
9zeta; the conjugate leading-coefficient identity is checked as well.

On the proper Tate modules, the cover kernel described in Section 3
below gives the actual image lattice

    q_* T3C = {(a,b) in T3E : b in 3Z3}.

Choose its source basis mapping to (f1,3f2).  The exact three matrices
are

    q_*=[[1,0],[0,3]],
    tilde(pi)_*=[[1,-9],[1,-2]],
    c_C=[[1,-3],[0,-1]].                                   (C6)

They satisfy q_* tilde(pi)_*=A_E q_* and q_* c_C=C_E q_*.
The factor 3 in q_* is retained.  In these bases the actual Weil
units agree: the functorial pairing identity says
3 omega_C=det(q_*) omega_E=3 omega_E, and multiplication by 3 is
injective on the coefficient lattice Z3.  For a change B of the
original Tate marking, the source change is q_*^-1 B q_*; it is
integral because B=I modulo 3.  Together with C_B and its actual
free-group lift in the frozen logarithm note, this specifies the
full marking transport without assigning a numerical B.

At the pi-place, zeta reduces to 2 in F7 and 9zeta^2 reduces to 1.
The ratio theta(Q)/theta(Q-A0) reduces generically to 1.  Thus the
proper lift reduces to the seventh-power Frobenius: this follows
either from (C5), or because it and Frobenius are lifts of [pi] on E
and both fix Q0.  The certificate lists all nine F7 points on each
curve and the three rational fibres of (C2).  At the conjugate place
the corresponding calculation uses zeta=4 and 9zeta=1.

For the affine map, the source must be retained.  Put

    X=C minus q^-1(E[3]),
    X_pi=C minus tilde(pi)^-1(q^-1(E[3])).

Then q:X->U is the actual unramified degree-three cover, and the
degree-seven map is tilde(pi):X_pi->X.  The simultaneous square with
E minus E[3pi] -> U commutes.  The other map X_pi->X is the open
filling map.  These two maps have not been identified or inverted.

Moreover tilde(pi) sends the unit tangent to pi times that tangent.
If h_pi is the formal-disc path from the pi-scaled tangent to the
unit tangent sending the specified roots pi^(1/3^n) to one, then
h_pi^-1 g(h_pi) is negative kappa_pi(g) inertia at the scaled tangent.
Thus the based map h_pi tilde(pi)_* has arithmetic commutator given
by conjugation by negative kappa_pi at the target cusp.  This is the
actual tangent correction; it is not zero on the global arithmetic
source.  The proper Frobenius equality above therefore does not by
itself evaluate the based affine Frobenius after specialization of
the extra puncture clusters.

## 3. Exact cover kernel, homology map and next augmentation layer

Write a=f1, b=f2 and d_1,...,d_8 for the original positive peripheral
generators.  The actual unit row is

    l_A0=(0,1,3,0,...,0).

Hence the closed subgroup corresponding to (C2), with the chosen
branch (C3), is exactly

    K=ker(l_A0:N->Z/3)=ker((0,1)p mod3).                    (C7)

It has the rank-28 Schreier basis

    B=b^3,
    g_j=b^j g b^-j, j=0,1,2, g in {a,d_1,...,d_8}.          (C8)

The basis and its based paths are specified by lifting the original
generators along the three powers of b, with return along the inverse
power.  For g=b, the wrap-around lift is b^3.  The Kummer character
fixes the sheet convention; the field equation (C2) proves that it
is the actual cover kernel.

Let V_K=K^ab and V=N^ab.  In the displayed bases, define L and eta by

    L(B)=3b, L(g_j)=g,
    eta(B)=0, eta(g_j)=j b wedge g.

Then the literal class-two group map in BCH coordinates is

    (v,z) -> (L v, (wedge2 L)z+eta(v)).                    (C9)

It follows directly by collecting b^j g b^-j; class two and p=3
make the coefficient 1/2 integral.  The central map has rank 45,
image wedge2(LV_K), and exact cokernel C3^9.  Its kernel is a
primitive free rank-333 module.  The certificate retains the image
basis, its diagonal entries 1^36 and 3^9, and all 333 sparse kernel
vectors with their inverse coordinates.  This is the central map
in (C9); the linear correction eta is separately retained.

The action of conjugation by b is also based, not a cyclic action
with its last term dropped:

    B -> B, g_0 -> g_1, g_1 -> g_2, g_2 -> B g_0 B^-1.       (C10)

Its abelian matrix P is the three-cycle on each triple.  The central
correction on g_2 is B wedge g_0.  The complete cube is exactly
conjugation by B.  The program checks (C10), its cube and its square
with (C9), including the wrap-around term.

All eight original peripheral generators belong to K.  Both remaining
intrinsic handle differences D1,D2 have image in wedge2 W, with W the
original peripheral lattice.  Thus every such image is represented
by a commutator of two elements of K and has zero image in K^ab.
This proves the exact zero comparison on affine-cover homology.  It
does not use a rational dimension argument.

The following layer retains those commutators.  Write da=D(a) and
db=D(b), and embed their peripheral commutators into the j=0 sheet
of wedge2 V_K.  An actual free-group lift sends

    a -> da*a, b -> db*b, d_i -> d_i,

where da,db mean the ordered products of the corresponding peripheral
commutator powers.  This map is a pro-three automorphism because its
Frattini map is the identity, and it preserves (C7).  In class two of
K the corrections are central, so its exact induced linear correction is

    D_K(B)=(1+wedge2 P+(wedge2 P)^2)db,
    D_K(a_j)=(wedge2 P)^j da,
    D_K((d_i)_j)=0.                                       (C11)

In particular

    (wedge2 L)D_K=D L,
    D_K P=(wedge2 P)D_K.

The program verifies both equations for both retained residual basis
vectors.  This is a comparison of the actual coordinate changes;
no arithmetic value is selected by applying it.

The two coefficient rows detecting the residual parameters are
especially small.  Use the central coordinate d_1,0 wedge d_2,0,
where d_1=A0 and d_2=A1.  Its values on source a_0 and B, respectively,
are

    [[0,-1],[1,0]]                                        (C12)

on the retained pair (D1,D2).  Its determinant is one, and its inverse
is retained.  Thus the next augmentation extension detects both
directions integrally, while (C7) proves their vanishing on homology.
The extension meant here can equivalently be read inside
I_K/I_K^3: the antisymmetric degree-two tensors are the displayed
peripheral commutators.  It is not just the induced action on
I_K/I_K^2=V_K.

## 4. Remaining actual evaluation

The literal isogeny lift (C5), its tangent correction and the source
square in Section 2 now specify the input for an evaluation in the
extension (C11).  What remains is the arithmetic action on that
extension, with the cluster specialization and the fixed based paths
retained.  Its two coefficients are not determined by (C6), the
homology zero map, or the unit minor (C12).  In particular neither
the action on the whole affine-cover homology nor a genuine
class-two Frobenius lift has been substituted from graded data.

The executed record is a_principal_cubic_cover.py and its actual
stdout, stderr and full JSON.  Two preliminary interface failures
are retained under history: the first used a nonexistent conjugation
method on the immutable QZ helper; the second expected the retained
45-by-2 handle columns to have their eight zero peripheral columns
already adjoined.  Both were corrected by explicit maps in this
program, without changing any frozen input.
