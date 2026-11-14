# An actual Tor symbol for the residual three-torsion

This note constructs a literal integral arithmetic symbol and evaluates
its proper regulator in the retained E37/E95 marking.  Its class is the
nonzero C3 summand of the residual handle module.  The coefficient of
this class in the actual intrinsic arithmetic action remains unassigned.
All maps below precede any rational Bloch or logarithm-sheaf comparison.

## 1. The function, tangent values and tame boundaries

On E: x^3+y^3+z^3=0, with O=[1:-1:0] and s=z/x at O, put

    f_A0=(y+z)/(3(x+y)),   Xi_Tor={zeta3,f_A0}.

The two lines are the actual tangents at A0=[0:-1:1] and O.  Thus
div(f_A0)=3[A0]-3[O].  The nine literal tangent frames, in the same
parameters used in E95, are as follows.  A frame is the coefficient of
the indicated order; it is an ordinary value when the order is zero.

| cusp | order | leading coefficient |
|---|---:|---|
| O | -3 | 1 |
| A0 | 3 | 1/9 |
| A1 | 0 | (2+zeta3)/3 |
| A2 | 0 | (1-zeta3)/3 |
| B0 | 0 | -1/3 |
| B1 | 0 | (1+zeta3)/3 |
| B2 | 0 | -zeta3/3 |
| C1 | 0 | (1-zeta3)/9 |
| C2 | 0 | (2+zeta3)/9 |

The new certificate recomputes every entry from the two line equations
and the actual cubic expansions.  Each line has total cusp intersection
multiplicity three, so this also proves that there is no further zero
or pole.  The tame symbol of Xi_Tor at a cusp d is
zeta3^ord_d(f_A0), which is exactly one at all nine cusps.  At every
other point both entries are units.  On the smooth model with three
inverted they are also units away from the displayed horizontal
divisors, so no vertical boundary away from three is introduced.

Consequently Xi_Tor lies in the actual function-field tame kernel,
and 3 Xi_Tor={zeta3^3,f_A0}=0 exactly.  The constant-symbol construction
in Goncharov--Levin, Theorems 3.7--3.8 and the proof of equation (21),
identifies the relation 3(A0-O)=div(f_A0) and the cube root zeta3 with
the corresponding Tor representative.  The source is
https://arxiv.org/pdf/alg-geom/9508008, printed pages 14--15.
Its arbitrary-field statement modulo torsion is not used to discard
anything here.  Nonvanishing of this particular arithmetic symbol is
proved by its integral regulator below.

## 2. Exact arithmetic cup, peripheral boundary and proper factorization

Write V in the E37 order (f1,f2,e_A0,e_A1,e_A2,e_B0,e_B1,e_B2,e_C1,e_C2).
The actual unit character and an integral peripheral row are

    l=(0,1,3,0,0,0,0,0,0,0),
    t=(0,0,1,0,0,0,0,0,0,0).

The original tangent normalization at O is one.  Its coherent root is
therefore one at every level, and the function's Kummer cocycle on the
actual semidirect product N semidirect P is a(n,g)=l(v_n), with zero
value on the original arithmetic section.  Here P is the actual free
unramified source of E34, with the original marked tau and tau-prime.
For the compatible roots zeta_(3^(n+1)) of zeta3,

    kappa_zeta(g)=(chi(g)-1)/3  for g in P.

The coefficient action on rows V^*(2) is g·r=chi(g)^2 r A_g^-1.
Since l A_g=chi(g)l, the actual cup kappa_zeta cup a has cross cocycle

    beta_g=kappa_zeta(g) l.

For B_t(n,g)=t(v_n), a direct bar-cochain calculation gives

    dB_t((n,g),(n',h))=(d t)_g(A_g v_n').

Set p:V->H=T3E equal to the first two coordinate projection and put
u=(0,1) in H^*(2).  The literal coefficient equality is

    l-3t=u p.

It follows, without division in a cohomology group, that

    beta-dt=p^* d(u/3),
    cup(Xi_Tor)=Inf(cross(d(u/3)))+dB_t.                 (T1)

Although u/3 is rational, d(u/3) is integral: beta and dt are integral.
In particular it is the Bockstein of the actual invariant u/3 modulo
H^*(2).  Equation (T1) records the complete cochain correction and not
just its class.  The program checks it as a polynomial identity for
A_E=(1+3a)I+3bR, q=det A_E, using the actual integral gluing
A_V=[[A_E,0],[U(A_E-qI)/3,qI8]].

The proper factor is unique.  The quotient of the row modules in p^*
is W^*(2)=Z3(1)^8, whose P-invariants are zero since chi(tau)=7.
Thus p^*:H1(P,H^*(2))->H1(P,V^*(2)) is injective.  The localization
term preceding restriction from E to U is the direct sum of
H0(K,Z3(1)), also zero.  On the proper elliptic curve, the other two
Hochschild--Serre terms in total degree two are H2(P,Z3(2))=0 and
H0(P,Hom(wedge2 H,Z3(2)))=H0(P,Z3(1))=0.  Therefore the unique proper
regulator is exactly d(u/3).  Every cochain in (T1) restricts to zero
on the original arithmetic tangent section; after filling, this is
the ordinary O section.  Hence no arithmetic-base component has been
added.  The finite coefficient H1 groups for P are finite, so inverse
limits are Mittag--Leffler and retain (T1) integrally.

For the actual marked elements, the two proper coordinates are

| element | chi | d(u/3) |
|---|---:|---|
| tau | 7 | (-7,2) |
| tau-prime=c tau c | 7 | (7,-5) |
| Frobenius at the K-prime over 2 | 4 | (0,-3) |

The last row uses the actual proper Frobenius [-2], the corresponding
E37 gluing matrix [[-2I,0],[-2U,4I8]], and the same root normalization.

## 3. The Q/K twist and the complete Weil-pairing marking

The function f_A0 is rational and c(zeta3)=zeta3^-1, so c(Xi_Tor)
is exactly -Xi_Tor.  This is already visible on the full rows:
lJ=-l and tJ=-t.  Thus the proper cocycle is anti-invariant for the
usual c action on H^*(2).  Twisting by chi_K produces a c-invariant
class with value zero at c, extending from P to Gamma=P semidirect C2.
Its value at tau-prime is forced by c and is the one displayed above.
Restriction to K is injective because cor composed with res is
multiplication by two.  These are the actual coefficient descent maps.

In columns, let

    R=[[0,-1],[1,-1]],   S=[[0,-1],[1,0]],
    A_E=[[1,-3],[3,-2]], C_E=[[1,-1],[0,-1]].

The algebraic alternating map S sends v to the functional h->det(v,h).
E37 proves e3(A0,A2)=zeta3 and chooses its full Tate basis lifting those
points.  In that original full basis, write its actual Weil matrix as
omega S, with omega in 1+3Z3.  The full value of omega was not assigned
in E37.  The exact canonical Weil map used here is therefore

    H^*(2) tensor chi_K -> H(1) tensor chi_K,
    v -> omega^-1 S^-1 v,

followed by the retained integral residual-coordinate map R.  The
matrix R S^-1 is unimodular.  Its action squares are

    H_tau (R S^-1)=(R S^-1)(49 A_E^-T),
    H_c   (R S^-1)=(R S^-1)(-C_E^-T),

where

    H_tau=[[7,-21],[21,-14]], H_c=[[-1,0],[-1,1]].

The second square includes the chi_K twist.  Equivalently,
H_c=R C_E R^-1 because the Tate(1) sign and chi_K sign cancel at c.
All four matrices and their inverses are retained in the certificate.

Put h_plus=(0,1) and k=(-7,-5).  Then

    H_c h_plus=h_plus,  (H_tau-I)h_plus=3k,
    R S^-1 d(u/3)(tau)=k.

The actual Weil transport has value k/omega.  The precise difference
from k is the integral c-fixed coboundary

    k/omega-k=(H_tau-I)((omega^-1-1)h_plus/3).           (T2)

The coefficient (omega^-1-1)/3 is integral.  Thus retaining the full
Weil unit changes no cohomology class, and (T2) supplies the literal
coordinate transport.  The certificate also verifies this carry for
every omega in 1+3Z/3^n through n=6.  No silent Tate-basis replacement
has been made.

## 4. Exact C3 coordinate and survival under the full integral IA gauge

Normalize cocycles by their value zero at c.  Their free-source value
at tau is any vector in H_res=Z3^2, and integral normalized boundaries
are (H_tau-I)H_res^c=Z3(-21,-15).  Hence the actual coordinate map is

    (x,y) -> (5x-7y, 2x-3y mod3),
    (a,b mod3) -> (3a-7b, 2a-5b) modulo (-21,-15).       (T3)

These matrices are mutual integral inverses before taking the indicated
quotient.  They give H1(Gamma,H_res)=Z3 plus C3, and k has coordinates
(0,1).  Thus the regulator of Xi_Tor is exactly its nonzero order-three
class.  The corresponding Bockstein point is h_plus/3 modulo H_res;
under R^-1 it is the actual A0 tensor zeta3 with the chi_K twist.

This class survives the entire integral central IA coefficient module,
not only H_res.  The retained maps D1,D2:V->wedge2V embed H_res there.
A rational primitive is D2/3.  Every possible change of this primitive
by a tau-fixed rational Hom map has image in Q3 w, where w=j1 wedge j2.
The exact weight decomposition proves this statement and is retained
in a_handle_torsion_gauge.py.  At exterior row19=(e_A0,e_B0), w is zero
but (D2/3)(f1)=-2/3.  Therefore no such primitive is integral.  The new
certificate rechecks the relevant maps and this immutable entry.

At the K-prime over two, Frobenius on H_res is -8.  The local group is
H_res/9, and Xi_Tor has value -3h_plus/omega, whose class equals
-3h_plus modulo9 by omega=1 modulo3.  It is nonzero of exact order
three.  This detects the same integral term lost when the previous
Xi and full constant-correctable lattice comparisons multiply the
residual regulator by a matrix with Smith factors9,9.

Equations (T1)--(T3) give an explicit representative for the torsion
coordinate discarded by rationalization.  The rationalization kernel
of H1(Gamma,H_res) is precisely the group generated by this regulator.
The actual unknown handle cocycle still has an unevaluated coordinate
in that group.  Neither its value nor a full intrinsic lifting image
has been inferred from the existence of this symbol.

## 5. Two actual conjugate elliptic filling maps

There are actual based maps from U to

    U1=E minus {O,A0,A1},  U2=E minus {O,A0,A2},

obtained by filling the other six cusps and retaining the original
unit tangent at O.  They are K-defined, and c exchanges them.  Give
their free rank-four groups the generators which are the images of
the original f1,f2,e_A0,e_Aj.  The abelian maps Q1,Q2 are the literal
coordinate selectors (0,1,2,3) and (0,1,2,4); their central maps are
wedge2 Q1 and wedge2 Q2.  Thus no higher-coordinate basis or path has
been substituted.

The only image of either residual D is the central commutator of the
two remaining peripheral generators.  On its two handle inputs, the
maps from H_res are the unimodular matrices

    P1=[[0,-1],[1,0]],  P2=[[1,-1],[0,1]].

Both satisfy Pi H_tau=49 A_E^-T Pi.  The actual c squares are

    Q2 J=J21 Q1, Q1 J=J12 Q2, J21 J12=I,
    P2 H_c=C_E^-T P1, P1 H_c=C_E^-T P2,

with

    J21=[[1,-1,0,0],[0,-1,0,0],[0,0,-1,0],[1,-1,0,-1]],
    J12=[[1,-1,0,0],[0,-1,0,0],[0,0,-1,0],[1,0,0,-1]].

All actual quotient matrices, exterior maps and inverses are in the
new certificate.  The pair detects the full residual lattice
integrally over K and carries the displayed Q descent.  It supplies
an exact target for further evaluation; the actual arithmetic
commutator values in these targets have not been assigned by their
linear divisor maps.

## Executed record and retained first attempt

The new program is code/a_elliptic_tor_symbol.py, with its actual
stdout, stderr and full JSON.  The first execution caught an incorrect
redundant terminal square R(-C_E)R^-1: that square had included the
Tate sign but omitted the compensating chi_K sign.  The primary
R S^-1 square already checked correctly.  The failed source and full
output are retained in history/a_elliptic_tor_symbol_redundant_c_twist.*;
the final program explicitly checks R C_E R^-1=H_c.
