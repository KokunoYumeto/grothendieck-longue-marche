# Literal norm-seven theta function and its local first moments

This is an actual arithmetic computation in the E120 curve and point
marking.  The comparison from these first moments to the intrinsic
handle cocycle has not been asserted.  The two exact coefficient maps
and the unresolved integral comparison are kept separate below.

## The curve, isogeny and scalar

Write zeta for the specified primitive cube root, D=1+2 zeta,
lambda=1-zeta and pi=1+3 zeta.  Thus D^2=-3 and pi=(-1+3D)/2.
The actual Weierstrass map from the Fermat cubic is

    X=-3z/(x+y),  y_W=9(x-y)/(2(x+y)),
    y_W^2=X^3-27/4.

Its zero is O=[1:-1:0].  The kernel polynomial of [pi] is

    h_pi(X)=X^3-27/pi=X^3+(27+81D)/14.

The certificate verifies the normalized Velu quotient explicitly:

    X_v=X-18cX/(X^3+c)
                   +12(B-c)X(X^3-2c)/(X^3+c)^2,
    y_v=(dX_v/dX)y_W,
    c=(27+81D)/14, B=-27/4,
    y_v^2=X_v^3+B*pi^6.

The map (X_v/pi^2,y_v/pi^3) has invariant-differential multiplier pi.
It is therefore the endomorphism [pi] in the retained CM embedding;
the equality also distinguishes pi from its conjugate.  Its six
nonzero kernel points have X-coordinates the roots of h_pi, each
with the two possible y_W-coordinates.

For a finite isogeny f, Norm_f means the function-field norm.  Thus
div(Norm_f u)=f_*div(u), and a constant c has norm c^deg(f).
For the multiplication maps, the exact X-preimage polynomials are

    F2(T)=T^4-4XT^3-8BT-4BX,
    P3(T)=3T(T^3-27),
    phi3(T)=T^9+648T^6+2187T^3-19683,
    F3(T)=phi3(T)-X P3(T)^2.

They are monic in T, and generically each root corresponds to exactly
one preimage of the specified target point (its y-coordinate is fixed
by the multiplication map).  Hence the two literal resultants compute
the norms without an additional leading coefficient.  They give

    Norm2(h_pi)=K2 h_pi,
    K2=1594323(10D-27)/343,
    Norm3(h_pi)=K3 h_pi,
    K3=-150094635296999121(2769D-239)/11529602.

The exact constant

    C=K2^3/K3=81(D-9)/14=81(zeta-4)/7

satisfies C^3=K2 and C^8=K3.  Consequently

    theta_pi=C/h_pi
       =3D(x+y)^3/((x+y)^3+pi*z^3)

has divisor 7[O]-sum_(T in E[pi])[T] and is fixed by Norm2 and Norm3.
The O term in the kernel sum is included: the order of theta_pi at O
is6.  The six poles are the nonzero pi-kernel points.

These two checked norms give every coprime norm directly.  If b is a
nonzero endomorphism prime to pi, it permutes E[pi].  Its pushforward
fixes the displayed divisor, so Norm_b(theta_pi)/theta_pi=u_b is a
constant in K.  The norms for commuting isogenies commute.  Applying
Norm2 to this equality and using Norm2(theta_pi)=theta_pi gives
u_b^4=u_b; Norm3 gives u_b^9=u_b.  Thus u_b^3=u_b^8=1 and u_b=1.
Similarly any other function with the same divisor and both norm
normalizations differs by a constant with cube and eighth power1,
and is equal to theta_pi.

This is the normalization of the CM Kato--Siegel function in Kings
math/0003113, Theorem4.2.2.  No Tamagawa theorem or prime restriction
from that paper's later regulator-index theorem is used.  For an
independent original construction of the scalar convention, Scholl's
author-hosted “An introduction to Kato's Euler systems”, Theorem1.2.1
and Remark(v), printed384--387, gives the divisor/norm convention and
its extension to odd finite subgroups of order prime to6.  The whole
proof through its norm/sign calculation has been read.  The resultants
and commuting-norm argument above also prove existence and uniqueness
for this particular function without importing the general construction.

At the retained E[3] points the actual values are

    theta_pi(A_i)=theta_pi(B_i)=-lambda,
    theta_pi(C1)=theta_pi(C2)=3D.

All points in these formulas are outside E[pi].

## The integral class and its transition

For m=3^r and t in E[3] minus O, let Z_r(t) be the finite etale
scheme of points Q satisfying [m]Q=t.  Each Q lies in E[3m].  Define
the finite class by the actual Kummer and corestriction maps:

    e_r(t)=sum_(Galois orbits Q in Z_r(t))
             Cor_(K(Q)/K)( kappa_m(theta_pi(Q)) tensor [3]Q )
          in H1(K,E[m](1)).

Here [3]Q belongs to E[m] and is fixed over K(Q); the tensor is with
the Kummer coefficient mu_m.  This formula is the integral first
moment map of the torsor's measure module.  It is the finite map
itself, not a rational splitting of a logarithm sheaf.

The transition Z_(r+1)(t) -> Z_r(t) is Q -> [3]Q.  The coefficient
transition E[3m](1) -> E[m](1) is multiplication by3 on the elliptic
factor and cubing on the root-of-unity factor.  On a fibre of this
scheme map the resulting moment is [9]Q=[3]Q_old, which is constant.
The projection formula and the proved Norm3(theta_pi)=theta_pi then
give exactly e_(r+1)(t) -> e_r(t).  Finite coefficient H0 groups are
finite; their inverse system is Mittag--Leffler.  Thus these classes
define an actual continuous class in H1(K,T3E(1)).

The construction uses a finite ramification set: the curve, its
3-power torsion and the theta divisor are defined with3 and7 inverted.
At a prime away3 the inertia value of an integral T3E(1) cocycle is
annihilated by F-q.  On the Tate factor this is q(F_E-1).  The proper
elliptic Frobenius has no eigenvalue1, since its two complex absolute
values are sqrt(q).  The lattice is torsion-free, so this inertia value
is zero.  Wild inertia of residue characteristic different from3 has
zero homomorphism to the lattice.  Consequently the integral class
is unramified away3, including at the auxiliary pi-prime, and factors
through the actual finite-S arithmetic source of E34.  No choice of
an unevaluated Frobenius word is introduced by this factorization.

Kings2013 Definitions3.3.3--4 express precisely the same finite
Kummer/moment operation for the standard theta function.  The integral
sheaf comparison in Theorem4.5.2 is available for its unipotent
logarithm quotients.  The subsequent splitting and moment comparison
in Definition4.5.7/Proposition4.5.8 and Theorems4.6.3/4.7.1 has a
rational target; its displayed N factors have not been cancelled in
this integral computation.  The printed generality of Proposition4.5.3
is not used beyond the actual unipotent logarithm sheaves, whose finite
augmentation filtration is killed by a sufficiently high [3^s] pullback.

## The actual place above2

Set Z=z/(x+y), Y=x/(x+y)+zeta.  Over the integers at2 the equation is

    Y^2-DY=(2-Z^3)/3.

It is smooth at2.  Its reduction over F4 is Y^2+Y=Z^3 and

    theta_pi=1/(1+zeta^2 Z^3).

The original O maps to infinity.  The E37 points A0 and A2 reduce to
(1,zeta) and (zeta,zeta), respectively.  The actual CM map [zeta] is
(Z,Y)->(zeta Z,Y).  Arithmetic Frobenius at this K-prime is [−2],
as checked on every retained point and as follows from the supersingular
curve endomorphism.  It acts on T3E(1) by−8.  Therefore

    H1(F4,T3E(1))=T3E(1)/9.

This is the entire local unramified group.  Its mod9 class is already
the complete local value, including both ternary digits.

The program constructs F_(2^18) from an explicitly checked irreducible
polynomial and retains the literal embedding of the earlier F64.  It
finds P,Q in E[27], with [9]P=A0 and Q=[zeta]P.  Hence [9]Q=A2 and
the CM matrix on this actual basis is [[0,-1],[1,-1]].  All729 points,
their coordinates and all Frobenius/CM equations are saved.  The
mu9 generator is the retained literal F64 image of the chosen zeta9.
These data specify the tensor identification used in the output;
they do not identify an unstated entire E37 Tate division basis.

For a Frobenius orbit Q of length f, the actual Kummer exponent is
the integer k with

    theta_pi(Q)^((4^f-1)/m)=zeta_m^k.

Corestriction sends the orbit's value k*[3]Q to its class modulo F-1.
There is no additional factor f.  To see the precise map, use coset
representatives 1,F,...,F^(f-1) in the cyclic group: evaluating the
transfer cocycle at F leaves the single wrap-around term evaluated at
F^f.  Different representatives alter it by an (F-1) boundary.  The
program checks each representative directly.  At m=3,9 the operator
F-1=-9 is zero on the retained finite coefficients.

The eight complete moment values modulo9, in ([3]P,[3]Q) tensor zeta9,
are

| t in the E37 (A0,A2) coordinates | e_2(t) |
|---|---|
| (1,0) | (8,3) |
| (2,2) | (4,1) |
| (0,1) | (6,5) |
| (2,0) | (1,6) |
| (1,1) | (5,8) |
| (0,2) | (3,4) |
| (2,1) | (0,0) |
| (1,2) | (0,0) |

All sixteen level3/level9 values, their orbits and Kummer exponents
are retained.  Reduction gives e_1(t)=t*kappa_3(theta_pi(t)), checked
for all eight points.  Pushing the level9 formula through [3] gives a
second independent computation using only E[9] over F64: for [3]Q=t,
use kappa_9(theta_pi(Q)) tensor Q, with exponent theta_pi(Q)^7.  Its
eight outputs agree with the E[27] computation.  The A0 and A2 columns
have determinant4 modulo9, so these actual local classes generate the
entire C9^2 group.

## Exact remaining comparison

The Xi symbols and the full constant-correctable tame lattice in
elliptic_symbols.md give an intrinsic residual-regulator map with
Smith factors9,9.  At this place, F-1 on that residual coefficient is
−9.  Thus every variation through either of those regulator maps is
zero in local H1.  Extending F4 to F64 cannot restore it: restriction
carries zero to zero.  This is the exact obstruction to reconstructing
the missing handle digits from an F4-only enumeration of those
symbols.  The present theta classes do generate C9^2, but an integral
map identifying them with the intrinsic action has not yet been proved.
The rational Bloch/Eisenstein comparison and its known factors do not
authorize division by9 in this finite group.

Executable record: code/a_elliptic_theta_pi.py, its actual stdout,
stderr and full JSON.  The first successful calculation before imposing
the CM-compatible division basis is retained under history; the new
certificate includes the literal change from that division basis.
