# The integral first logarithm torsor and an evaluated local theta class

This note retains the first logarithm torsor at the actual point A0,
including its augmentation.  It gives an integral coefficient isomorphism
into the actual intrinsic abelian dual, a continuous cup primitive, and a
complete local theta class.  It does not assign that class to the unknown
intrinsic handle action.  The final section specifies the remaining map.
The frozen Tor-symbol and theta-principal-distribution files are inputs
to the continuing comparison, and are unchanged.

## 1. The exact finite image and the inverse limit

Let H=T3E in the retained E37 basis, let t=A0, and write m=3^n.  The
actual finite division torsor and its measure module are

    T_n(t)={Q:[m]Q=t},  R_n(t)=(Z/m)[T_n(t)](1).

It is a torsor under E[m], contained in E[3m].  There is a literal map
of arithmetic modules

    R_n(t) -> (Z/m)(1) plus E[m](1),
    delta_Q -> (1,[3]Q).                                      (L1)

Its image is exactly

    L_n(t)={(a,h):h mod3=a*t}.                                 (L2)

To prove both inclusions, choose a coherent Tate lift h0 of t and division
points Q_n with [3]Q_n=h0 modulo m.  Every point of T_n(t) is Q_n+R
for R in E[m], and (L1) sends it to (1,h0+3R).  The differences of
these images are (0,3R); they generate exactly the vectors in (L2).
Thus h=a*h0+3z, with a modulo m and z modulo 3^(n-1), is a complete
inverse coordinate system.  In particular

    L_n(t) = C_(3^n) plus C_(3^(n-1))^2,
    |L_n(t)|=3^(3n-2).                                       (L3)

The torsor transition is Q -> [3]Q, and the coefficient transition is
reduction on the scalar and the Tate coordinates.  Hence the maps
L_(n+1)->L_n are onto.  Their inverse limit is the free rank-three
lattice

    L(t)={(a,h) in Z3(1) plus H(1):h mod3=a*t},
    (a,z) <-> (a,a*h0+3z).                                   (L4)

This is also the actual first unipotent quotient of the torsor's
completed measure module.  Translation by the chosen coherent Q_n
identifies that module with Z3[[H]](1).  In a Tate basis this is
Z3[[X1,X2]](1); its augmentation and first derivatives have kernel
the closed ideal (X1,X2)^2.  Under (L1), their coordinates are precisely
(a,z) in (L4).  Thus the identification with the first logarithm quotient
is an integral map of the actual cover modules, rather than a rational
splitting or a rank comparison.

Two finite kernels must be retained.  The image of L(t)/3^n L(t) in
L_n(t) has kernel C3^2, represented by the two vectors
(0,3^(n-1)e_i) in the z coordinates.  Conversely the map from L_(n+1)
to the full rank-three target modulo 3^n has kernel C3, represented by
(a,h)=(3^n,3^n h0).  Its transition to the preceding such kernel is
zero.  These exact maps explain the extra digit used below.

## 2. Actual arithmetic action and the cup primitive

Write A_g for the actual action on H and chi_g for the cyclotomic
character.  Since t is K-rational, the integral torsor cocycle is

    kappa_t(g)=(A_g-I)h0/3 in H,  g in G_K.

The action on the coordinates in (L4) is exactly

    g(a,z)=(chi_g*a, chi_g*A_g*z+chi_g*a*kappa_t(g)).           (L5)

For a cocycle with scalar coordinate a_g and moment coordinate e_g,
put z_g=(e_g-h0*a_g)/3.  Direct substitution in (L5) gives the full
inhomogeneous cochain identity

    d z(g,h)=-chi_g*a_h*kappa_t(g)=-kappa_t cup a(g,h).         (L6)

The sign follows from d z(g,h)=g z_h-z_gh+z_g.  Thus the primitive
is integral, and its precise arithmetic torsor is part of the formula.

For theta=theta_pi, with the actual normalized function and norm identities
proved previously, take the Kummer class on each finite division torsor
and transfer it to the measure module.  Equivalently it is the sum over
orbits of kappa_m(theta(Q)) delta_Q with the actual corestriction maps.
Its augmentation is kappa_m(theta(t)); its first moment is the previously
defined e_n(t).  The identity Norm_[3](theta)=theta gives compatible
classes in H1(K,L_n(t)).  Finite coefficient H0 groups are finite, so
the inverse-limit H1 comparison is exact and produces a continuous
class in H1(K,L(t)).  Equation (L6) is its actual integral primitive
for kappa_t cup kappa(theta(t)).

The initial construction has ramification only above 3 and 7.  The scalar
theta(A0)=-lambda is a 3-unit.  At any good prime away 3, its scalar
inertia is zero.  A remaining inertia value is therefore in H(1), and
is killed by F-q=q(F_E-I); that endomorphism is injective on the lattice
because the elliptic Frobenius has no eigenvalue one.  The wild inertia
has residue characteristic different from 3 and also maps trivially.
Thus the continuous class is unramified away 3 and factors through the
actual P of E34.  This is an action on the actual cochain module (L5).

A change of the chosen scalar Kummer roots by a cochain boundary d s
must be lifted by the actual element (s,s*h0) of (L4).  Its raw pair
boundary is ((chi-1)s,(chi*A-I)s*h0).  This records the correction to
the moment as well as to the scalar; changing only the scalar would
not be a map of these modules.

## 3. A unimodular map into the actual intrinsic coefficient

Use V=(f1,f2,e_A0,e_A1,e_A2,e_B0,e_B1,e_B2,e_C1,e_C2), with proper
projection p:V->H.  The literal normalized unit and peripheral rows are

    l=(0,1,3,0,0,0,0,0,0,0), t0=e_A0*, u=(0,1)^T,
    l=3*t0+p* u.

The last equality is the same one used in the frozen Tor calculation.
Let the actual Weil matrix in this Tate basis be omega*S, where

    S=[[0,-1],[1,0]], omega in 1+3 Z3.

Choose h0=omega^-1 e1, so omega*S*h0=u.  This is an integral lift of
the specified A0.  Define

    Phi:L(t)->M_A0=Z3*t0 plus p*H*(2),
    Phi(a,z)=a*t0-p*(omega*S*z).                              (L7)

It has determinant omega^2 and is an integral isomorphism.  In raw
pair coordinates its value is

    Phi(a,h)=(a*l-p*(omega*S*h))/3.                            (L8)

The numerator is divisible by 3 in V*(2), by (L2); the formula does
not divide a cohomology class by 3.

Here is the complete arithmetic square.  The actual E37 action is

    A_V=[[A,0],[U(A-chi I)/3,chi I8]],  U_A0=-u^T.

On M_A0, write a vector as (a,x), where x is the proper column.  Its
action is

    g(a,x)=(chi*a, chi^2 A^-T x
                         +(chi*a/3)(I-chi A^-T)u).            (L9)

The identity det(A)=chi implies S A=chi A^-T S; substituting h0
in (L5) proves (L7) intertwines (L5) and (L9), with exactly the cross
term shown.  The certificate checks this polynomially for
A=(1+3a)I+3bR, where R=[[0,-1],[1,-1]].  For the original complex
conjugation C_E=[[1,-1],[0,-1]], h0 is fixed; the action on the log
coordinates is (-a,-C_E z), and (L7) intertwines it with
(-a,C_E^-T x).  This is an equality of coefficient maps.  Conjugation
also sends the function theta_pi to theta_bar(pi); it does not assert
that their arithmetic classes are equal.

At finite level the compatible target is

    M_A0/(3^n Z3*t0 + 3^(n-1) p*H*(2)).                       (L10)

Formula (L7) and the inverse a followed by z=-(omega*S)^-1 x identify
L_n with (L10).  This agrees with both kernels following (L4).  The
script exhaustively checks all 61,320 elements of these lattices for
n=1,2,3,4, including the inverse and the actual Frobenius action.

## 4. The actual finite division basis and Weil unit

All finite calculations use the previously retained curve over F4,

    Y^2+Y=Z^3, theta=1/(1+zeta3^2 Z^3).

The retained F_(2^18) is F2[r]/(r^18+r^3+1).  Its integer polynomial
encoding is unchanged.  The retained CM-compatible E[27] basis is

    P=(213680,20300), Q=(29715,20300)=[zeta3]P,
    [9]P=A0, [9]Q=A2.

The roots of unity are zeta3=37385, zeta9=72 and the explicitly chosen
zeta27=128; cubing each gives the preceding root.  The separate Miller
certificate uses the actual normalized line divided by the vertical
line at each addition step.  Its pole-leading coefficients cancel in
the quotient.  It gives

    e3(9P,9Q)=zeta3,
    e9(3P,3Q)=zeta9^4,
    e27(P,Q)=zeta27^13.                                      (L11)

It retains every line factor and twelve independent bilinearity
identities.  Therefore the Weil unit in this finite division chart is
omega=13 modulo 27.  No unassigned E37 division lift has been identified
with P or Q.

The precise transport to any other retained CM-compatible full Tate
basis is as follows.  Let B be the actual change on H, defined by its
action on division points, with B=I modulo 3.  Its intrinsic abelian
lift and row map are

    C_B=[[B,0],[U(B-I)/3,I8]],
    r_old=C_B^-T r_new.                                     (L12)

This satisfies C_B*j=j*B, preserves each peripheral basis vector, and
l*C_B=l.  The Weil unit changes by omega_new=det(B)*omega_old, so
B^-T*omega_new*S*B^-1=omega_old*S.  Substitution in the raw formula
(L8) proves that C_B^-T carries its new-coordinate value to its
old-coordinate value exactly.  In (a,z) coordinates the corresponding
map is z_new=B^-1 z_old+a(B^-1 h0_old-h0_new)/3; its carry is integral.
The certificate verifies this entire square for a generic CM-compatible
B=I modulo 3.  It can be lifted to an actual free-pro-3 basis map by sending
f_i, in the stated generator order, to f1^B_(1i) f2^B_(2i) followed
by the eight peripheral powers in the i-th lower column of C_B, and
fixing the peripheral generators.  Its Frattini matrix is invertible,
so it is an automorphism.  The complete arithmetic action is transported
by conjugation with this specified free-group map.  At the present
place A=-2I, (L9) is unchanged by (L12).  Its complex-conjugation chart
is transported as C_B^-1 J C_B; no uncomputed B or conjugation value
has been substituted.  In particular the numerical coordinates below
belong to the literal finite division chart (L11).

## 5. Complete local theta value at the K-prime above two

Arithmetic Frobenius at this place is [-2] on H and has chi=4.  In
the target coordinates (a,x1,x2) of (L7),

    F=[[4,0,0],[0,-8,0],[4,0,-8]],
    F-I=[[3,0,0],[0,-9,0],[4,0,-9]].                          (L13)

The full local cohomology, its coordinate map and inverse are

    M_A0/(F-I)M_A0 = C9 plus C27,
    (a,x1,x2) -> (x1 mod9, a+6x2 mod27),
    (r,s) -> (s,r,0) modulo (F-I)M_A0.                       (L14)

The certificate retains integral boundary preimages for both inverse
identities and both periods.  The kernel of reduction to (L10) at
n=3 is contained in (F-I)M_A0: the two proper 9-multiples are immediate,
and 27*t0=(F-I)(9,0,4).  Consequently this finite level already gives
the entire local group in (L14).

Norm_[3](theta)=theta provides a useful exact finite computation.
After grouping the first-moment terms by R=[3]Q, the level-n pair is
computed on the smaller actual torsor

    R in E[3^n], [3^(n-1)]R=t,
    sum_R Cor(kappa_(3^n)(theta(R)) tensor (1,R)).              (L15)

Thus the complete n=3 value needs only the retained E[27] table.
For an orbit of length f, its Kummer exponent k is specified by

    theta(R)^((4^f-1)/3^n)=zeta_(3^n)^k.

Transfer evaluated at F is the single wrap-around term (k,kR), with
no additional factor f.  Changing the orbit representative by F^r
changes this pair by (F-1)(1+...+F^(r-1))(k,kR), an actual boundary
in L_n.  The script checks every such change.  It also reproduces both
earlier immutable moment levels for all eight nonzero t and computes
their entire level27 augmentation/moment pairs.

For t=A0 the pairs at levels 3,9,27 are respectively

    (2;2,0), (8;8,3), (8;8,3).                              (L16)

The simultaneous pair at the last level is not obtained by dividing
the previous moment alone.  Under (L8), with omega=13, it gives
(a,x1,x2)=(8,4,4) in (L10).  The direct local roots of
theta(A0)=-lambda have scalar Kummer value 2: its Teichmuller residue
is zeta3^2 and its principal unit has a unique 3^n-th root in the local
pro-two principal-unit group.  The scalar root change is
s=(2-8)/3=-2.  Its simultaneous lift is (s,s*omega^-1 e1), so its
boundary changes the pair by (3s,-9s*omega^-1 e1).  It gives

    normalized pair (2;26,3),
    normalized target (2,4,5),
    full local class (4 mod9,5 mod27).                       (L17)

This is an actual class of order 27.  Its augmentation in local
H1(Z3(1))=C3 is 2.  Both finite transition maps have been checked as
literal cochain boundaries.  The observed raw representatives in
(L16) happen to agree under reduction; that observation is not used
to assume arbitrary choices agree.

## 6. Scope of the remaining intrinsic comparison

Equations (L1)--(L12) give an actual integral logarithm-torsor coefficient
map, and (L6) is its explicit continuous cup primitive.  Equations
(L13)--(L17) evaluate one complete local theta class in that module.
These maps preserve the augmentation and the previously lost ternary
digit.  The first-moment construction is compatible with the integral
finite-cover logarithm construction in Kings,
https://arxiv.org/pdf/0711.2443, Section 1.1.  The exact first quotient
used here was proved directly by the completed augmentation ideal
above.

For the next step, Kings https://arxiv.org/pdf/math/0003113,
Theorem 4.1.3 (printed 41--42) identifies the finite geometric
polylogarithm with the displayed one-motive via relative Picard sheaves;
its complete proof and its explicit derived-tensor extension have been
opened.  Proposition 4.1.5 (printed 44--45) retains a sign in the
auxiliary-isogeny comparison.  The subsequent projection at a torsion
point is an isomorphism under the prime-to-3 assumption in Lemma 3.5.1;
the rational moment map in Section 3.5 cannot remove that assumption
in this integral problem.  Formula (L2) supplies the exact lattice at
the present 3-torsion point.

The required next morphism is from the intrinsic class-two arithmetic
extension, including its peripheral-commutator part surviving the
ambient metabelian quotient, to this logarithm-torsor class.  The actual
coefficient map (L7) alone is not that extension comparison.  The
theta-principal-distribution identity D4 and its operator with Smith
factors 3,9 remain available, with all constant symbols.  The frozen
Tor symbol gives the surviving C3 regulator and its actual Bockstein.
Neither its coefficient in the intrinsic action nor the missing
integral extension comparison has been assigned by the present result.

Executed files: a_log_torsor_pairing_probe.py and
a_elliptic_log_torsor.py, their complete actual stdout/stderr/JSON,
with immutable input hashes in the latter certificate.
