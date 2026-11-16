# Exact continuation of the A208 secondary-unit diagram

Authors/reviewers: local_preprint and birational_main. Date: 2026-11-16.
This note continues `two_inert_eta_secondary_divisor_comparison.md`.

## 1. Norm-one alignment and a lower capitulation divisor

The following identity was derived by birational_main and independently verified coefficient by coefficient by local_preprint. Work in the integral group ring Z[gamma]/(gamma^9-1), with Ns=1+gamma^3+gamma^6. For j=0,1,2 let

    Lj=P4(gamma^(4^(j-1)))-1-Ns,

where the exponent of 4 is read modulo three. Then

    Lj=(gamma^(4^j)-1)Rj,

with coefficient vectors in ascending powers of gamma

    R0=(0,0,0,0,0,-1,0,-1,-1),
    R1=(0,-1,-1,0,0,-1,0,0,0),
    R2=(0,0,-1,0,-1,0,0,0,-1),
    R0+R1+R2=-(gamma+2gamma^2)Ns.

Apply these identities to h^j(w). Because h(b)=b and
(gamma^(4^j)-1)h^j(w)=b, the product of the three h-conjugates of r0 is

    Nh(r0)=b^(-(gamma+2gamma^2)Ns)*(sigma a)^3
          =a^(Nsigma-3sigma)*(sigma a)^3=1.

The last equality uses the exact certified Nsigma(a)=1. Hilbert90 in
F'/F gives an actual y in F'^times with r0=h(y)/y. The simultaneous
replacement

    w -> w/y,  x -> x/y,  f -> f/y^3

preserves b and u=w/x literally, preserves c=x^3/f literally, and makes
r0=1. Therefore f belongs to F and hJ=J. The only ramified prime in
M/E2 is the unique three-prime; its coefficient in J is
v_M(f)/3=3v_F(f). Hence J is the actual ideal extension of an E2 divisor D.
Taking divisor coefficients gives

    J=j_h D,  3D=div_E2(f),  j_h[D]=0.

The relation f*tau(f)=a0^3, initially in F', already makes f*tau(f) a
cube in F: the Kummer restriction kernel F^times/F^times3 ->
F'^times/F'^times3 is the tau-minus line of zeta, whereas the class of
f*tau(f) is tau-plus. Its cube root differs from a0 by an element of
mu3, which is itself in F. Thus D+tau(D) is principal and [D] is in
the actual group A2-minus. The class is killed by three before taking
any primary projection.

The divisor D is sigma-invariant. The base F has no three-class group,
so its primary class is represented by the seven ramified-prime
coefficients. The tau-minus relation removes the unique three-prime
and the tau-fixed q branches and makes each exchanged pair opposite.
Writing Delta_q=[R_q,1]-[R_q,2], with the chosen branch alpha=r_q*zeta,
gives the exact formula

    [D]=k11 Delta11+k59 Delta59,  psi2(v)=2(k11,k59).

The k_q are the unchanged coefficients v_Rq(J). This realizes psi2
through an actual lower capitulation class. No comparison of this class
with Theta_h(a) has yet been proved.

## 2. The complete necessary unit cube-class space

The unit c=x^3/f satisfies

    sigma(c)/c=(sigma(x)/x)^3,
    h(c)/c=(h(x)/x)^3,
    c*tau(c)=(x*tau(x)/a0)^3.

All quotients inside the cubes are actual units. Moreover
Ns(u)=sigma(a)/c. Since sigma(a) comes from E2, its next tame characters
are zero in the degree-six residue fields. Hence the class of c lies in

    C = (U_M/U_M^3)^(sigma=1,h=1,tau=-1) intersect ker Lambda_next.

The new exact program `code/two_inert_secondary_invariant_units.py`
computes the four actual automorphism matrices through A199's complete
27-dimensional residue isomorphism. It checks sigma^3=h^3=tau^2=1,
the commuting and conjugation relations, and g^3=sigma. The fixed
anti-space has dimension four. The next tame map has rank one on it;
C has dimension three.

There is an exact, small basis for C:

    C = < [epsilon], res[u11], res[u59] > over F3.

The last two classes are actual unit classes in M. Indeed
div_E2(u_q)=3(R_q,2-R_q,1), these divisor classes have order dividing
three, and their extension to M vanishes by A206. Choose an actual
principal generator of the extended divisor; dividing u_q by its cube
gives a global M-unit. The resulting unit cube-class is independent of
that generator. The residue coordinates of epsilon,u11,u59 are
independent and are in C; the dimension-three computation proves equality.
The program evaluates the literal u_q rational functions at every one
of A199's 27 exact residue maps and records the complete coordinate maps.

For reference, the three Gaussian kernel vectors printed by the program
have coordinates (2,0,0), (1,1,1), (2,0,2) in this basis. Thus the first
line is epsilon^2, and the other two retain both actual changed-prime
directions.

The restriction kernel from F to M is the Kummer plane
<zeta,d^2 alpha>. Its tau-minus part is <zeta>. Consequently the last
two coordinates of a class in C are unambiguous lower radical
coordinates. With c=x^3/f and the chosen q branch, u_q has valuation
-1, so these two coordinates are (k11,k59), and psi2 is twice them.
This identifies the exact remaining finite coordinates; it does not
assign them to the three specified input units without the remaining
actual norm/alignment comparison.

