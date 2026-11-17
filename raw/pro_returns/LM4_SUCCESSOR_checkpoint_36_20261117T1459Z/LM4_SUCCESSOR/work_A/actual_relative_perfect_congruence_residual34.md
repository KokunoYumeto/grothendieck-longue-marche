# The actual relative-perfect residual and its full quotient action

Checkpoint34 research, separate from all frozen formal sources and from the
previous central-tower proof. All groups, maps, and closures below are actual
profinite groups and continuous maps. No finite census or new computation is
used.

## 1. Definitions and exact prior inputs

Let B=C2(s) coproduct C3(r), let F be its actual pure index-six free profinite
subgroup, and retain the original marked negative full-GT involution alpha,
canonical u, actual even k, d=1+2k, and the same ordered word H_d as in
A89/A103/A107. Let q:F onto C be the full signed congruence map, N=ker(q),
N1=closure([N,F]), P=F^(2), pi:F onto P, and O=ker(pi). Set

    C=C_(2) × C_o,     C_o=product_(p odd) SL2(Z_p),
    M2=ker(P onto C_(2)),     M21=closure([M2,P]),
    Bbar=B/O,     B1=B/N1,
    D_o=(F_ab)_odd ×_((C_o)_ab) C_o.

All fiber-product maps are the actual abelianization maps. The odd
abelianization of C_o is C3, supported at p=3; the map from the original
abelian coordinates is their sum modulo three.

The exact inputs, with their proofs and source bindings retained, are:

* A106: N1=N intersect F' intersect pi^(-1)(M21).
* A107: B-stability of N and N1, with the full signed mod-four parity
  correction retained. The original alpha and complex conjugation c also
  preserve these groups.
* The complete first-step proof
  `actual_next_modular_central_refinement34.md`, SHA256
  9ccc6406ec9558d4715ed7837feffb844af40606b2743d6574eb6ef399eba0b5:
  pi(N1)=M21; H2(B1,Q_l/Z_l)=0 for every odd l;
  H1(D_o,Q2/Z2)=H2(D_o,Q2/Z2)=0; and H2(Bbar,Q2/Z2)=0.
  Its odd-prime inputs are precisely Beyl Proposition5.7 and its explicitly
  proved product/lattice arguments, not a vanishing assertion for C_(2).
* A89.3 and A103: the SAME full H_d has pi(H_d)=1 and H_d in N intersect F'.
  A106 therefore puts H_d in N1. The full pro-two word vanishing, not merely
  an exponent equality or a first-layer coefficient, is used here.
* A104: the actual canonical endomorphism psi=psi_d has abelianization dI,
  with d a unit, and q psi=Ad(H) q for the actual matrix H. Its identities
  with alpha and c, and the modular cubic identity, are those of A107.

Define the new closed normal subgroup

    R=N1 intersect O = N intersect F' intersect O.                 (1)

The equality is immediate from A106. In particular R is B-normal and
alpha-, c-, and psi-stable; O is fully characteristic and the other
stabilities have just been specified. No assertion that N is characteristic
under arbitrary automorphisms of F is made.

## 2. The exact full-pro-two coordinate quotient

The actual combined map

    F --> P × D_o,
    g |--> (pi(g), (g_ab,odd, q_o(g)))                             (2)

has kernel R. Indeed pi(g)=1 already forces q_(2)(g)=1 and the two-primary
abelian coordinates to vanish. The remaining two coordinates in (2) then
vanish exactly when g belongs to N and F'. This proves injectivity of the
resulting compact quotient map F/R into P × D_o.

Its projection onto D_o is onto. Given an allowed pair (a,c), choose a lift
in F with the specified odd abelian coordinates. The remaining C_o
discrepancy has zero abelianization, so it lies in C_o'. Since a continuous
surjection maps the closed derived subgroup onto the closed derived
subgroup, an F' lift corrects precisely that discrepancy without changing a.
The P projection is onto by definition.

D_o has no nontrivial pro-two quotient. Its kernel over C_o is pro-odd
abelian and has no such quotient. A pro-two quotient of C_o would, if
nontrivial, have a nontrivial C2 character, whereas (C_o)_ab=C3. Thus any
common quotient of P and D_o is trivial. Profinite Goursat, applied to the
closed subdirect image of (2), proves the exact coordinate isomorphism

    F/R = P × D_o.                                               (3)

This uses the FULL free pro-two P, not the earlier P/M21. The actual image
of O is the entire second factor D_o. Hence D_o is normal in B/R and

    (B/R)/D_o = Bbar.                                            (4)

The other natural map B/R onto B1 has kernel

    N1/R = M21,                                                  (5)

by pi(N1)=M21 and (1). This is a pro-two group, not asserted central.

## 3. Vanishing of the whole degree-two cohomology

For an odd prime l, the positive-degree continuous cohomology of the
pro-two kernel (5) with the trivial l-primary divisible coefficient
A_l=Q_l/Z_l vanishes, by finite-quotient averaging. The extension spectral
sequence therefore gives

    H2(B/R,A_l) = H2(B1,A_l) = 0.                                (6)

For l=2, use (4), retaining the actual D_o kernel. Its H1 and H2 with
A_2=Q2/Z2 vanish by the exact prior calculation. The low-degree extension
spectral sequence consequently gives the inflation isomorphism

    H2(Bbar,A_2) --> H2(B/R,A_2),

and both groups are zero. These arguments do not require higher
two-primary cohomology of D_o to vanish. Every continuous cochain with
values in the discrete torsion group Q/Z has finite image, so passage to
the direct sum of its primary components is legitimate. Thus

    H2(B/R,Q/Z)=0.                                               (7)

Now apply the five-term sequence for R --> B --> B/R. Restriction of every
character of B to R is zero, since R is contained in F' and hence in B'.
Equation (7) therefore forces H1(R,Q/Z)^B=0. Continuous characters separate
points of the compact abelian quotient R/closure([R,B]); precisely its
characters are these invariant characters. We obtain

    R = closure([R,B]).                                          (8)

This is relative perfectness in B. It does not assert R=R'.

The canonical word satisfies, using the actual inputs in section1,

    H_d in N1 intersect O = R.                                  (9)

No inverse-limit inference from finitely many heads is involved in (9).

## 4. The actual automorphism on F/R and B/R

In the exact coordinates (3), the map induced by psi is the product of:

* its actual endomorphism on P, whose action on the Frattini quotient is
  dI and is invertible; the pro-two Frattini criterion and Hopficity of the
  finitely generated P make this an automorphism;
* the map (a,c) |--> (d a, Ad(H)c) on D_o.

Both factors in the second map are automorphisms, and its C3 compatibility
is the actual compatibility of psi with abelianization. The induced map
on the common C3 quotient is multiplication by the unit d mod3. The
inverse maps therefore preserve the fiber-product equality as well. Thus
this is an automorphism of D_o. There are no unaccounted cross terms:
the P coordinate is pi psi and the other coordinates are literally the
original abelianization and q_o identities. Consequently

    psi induces an automorphism of F/R.                          (10)

By the exact original identity H_d=u((v delta^d)^3)^(-1)u^(-1), (9) makes
the two assignments

    s |--> v=u^(-1)s,       r |--> v delta^d                      (11)

an actual continuous homomorphism B --> B/R. Its restriction to F is psi
modulo R, so it kills R and descends. It is an automorphism on the pure
kernel by (10), and induces the identity on S3: u is pure and d is odd.
It is therefore an automorphism Psi_R of B/R. The actual generator-wise
identity alpha Psi_R=Psi_R c_B holds, as in A107, without using a formal
prospective homomorphism before the cubic was proved.

## 5. Full peripheral lift of this specified quotient action

The s image in (11) has the required full factor conjugacy already in B.
The r transporter in A108 lifts from B1 to B/R: the kernel (5) is pro-two,
and the two order-three lifts are conjugate by it by the complete compact
coprime conjugacy argument. Thus Psi_R preserves the actual factor
conjugacy classes, with r exponent e=d mod3 and the same S3 normalization.
The cusp image is literally delta^d.

Choose an actual Galois peripheral automorphism gamma of multiplier d.
The original LM7_PUSH E.65.8 and E.65.15 covariance, in precisely the
based marking explained in the first-step proof, show that gamma
preserves N. It also preserves F', O, and hence R. Left-compose Psi_R
with gamma^(-1). The result is a positive peripheral automorphism of
B/R, with no powers hidden inside a conjugacy-only hypothesis.

The closed-normal modular lifting criterion in the complete A3/A34
source asks for a positive peripheral lift to B/closure([R,B]). By (8)
this is exactly the quotient B/R on which that automorphism is already
defined. The criterion gives a full positive peripheral lift. Compose
back with gamma; if the cusp is initially only conjugate to delta, its
central-refinement transporter belongs to R and the usual inner
correction makes the cusp equality literal without changing B/R.
There is therefore a full peripheral automorphism Gamma_R of B inducing
the specified Psi_R and satisfying Gamma_R(delta)=delta^d.

This conclusion concerns a lift of this quotient automorphism. It does
not identify Gamma_R's pure restriction with the original canonical
psi, and does not establish alpha Gamma_R=Gamma_R c_B in the full B.

## 6. Nontrivial residual and the exact limit of the tower

A110 proves that the actual N1 is not pro-two. Since N1/R=M21 is pro-two,
R cannot be pro-two: an extension of two pro-two groups is pro-two.
In particular R is nontrivial. This independently follows from the
actual torsion in the D_o factor of (3), together with torsion-freeness
of the full free profinite F, but that alternative is not needed.

For the already saved B-central tower L0=N1,
L_(j+1)=closure([L_j,B]), equation (8) gives R contained in every L_j.
Hence

    1 != R <= L_infinity.                                       (12)

The B-central tower is therefore NOT cofinal. No equality R=L_infinity
is inferred; that would require a separate calculation of the actual
intersection of the corresponding A_j in Bbar. The new quotient B/R
can be finer than the limit of that tower.

Both main problems and the actual CM value remain open. Equations
(8)–(11) isolate a genuine residual subgroup and a fully controlled
quotient action; they do not show that the canonical H_d is the
identity in that nontrivial residual.
