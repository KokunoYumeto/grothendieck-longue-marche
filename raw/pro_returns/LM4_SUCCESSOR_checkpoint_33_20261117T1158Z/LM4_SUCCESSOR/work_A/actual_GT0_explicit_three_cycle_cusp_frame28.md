# An explicit actual three-cycle formula for the canonical cusp frame

Research, checkpoint 28. This is a new addendum. The four accepted checkpoint27 notes, A85/A86, and `actual_GT0_marked_three_cycle_gate28.md` are unchanged. All statements below concern the given actual negative-GT0 involution. Neither Main-A decision is asserted.

## 1. Actual marking and the unique positive three-cycle frame

Use the actual modular marking

    B=C2(s) amalg C3(r),  delta=sr,
    x=delta^-2,  y=s x s,  z=(xy)^-1,
    rho_cyc=Ad(r)|F,  iota=Ad(s)|F.

Thus rho_cyc sends x,y,z cyclically to y,z,x. Let alpha=(-1,f) be the actual involution, with its canonical u in F', so

    u=f alpha(u),  iota(u)=u^-1,  alpha(f)=f^-1.

The actual multiplier-one element Sigma=alpha c=(1,f) has

    Phi_Sigma(s)=s f,  Phi_Sigma(r)=f^-1 r,
    Phi_Sigma(delta)=delta.

The unique pure r-frame of this already defined actual automorphism is denoted A:

    Phi_Sigma(r)=A r A^-1=f^-1 r,  A in F.             (1)

Existence and uniqueness here are the actual pure-frame result E.65.1, using the full torsion conjugacy and centralizer facts from E.58. For clarity, the exponent is +1: the multiplier-one map preserves the r-class in B_ab, and the two nonidentity elements of the C3 factor have different abelianizations. A conjugator can be made pure by right multiplication by a power of r, since its S3 image centralizes r. Uniqueness is C_B(r) intersect F=1. No proposed map s->v, delta->delta^d is used in defining A.

Equation (1) gives the literal identity

    f=rho_cyc(A) A^-1.                                (2)

In particular A belongs to F'. Indeed the matrix of rho_cyc on the actual x,y abelianization is

    R = [[0,-1],[1,-1]],  det(R-I)=3.

Since f_ab=0, (R-I)A_ab=0. Multiplication by 3 is injective on Zhat^2, so the adjugate equation forces A_ab=0. This uses the full integral profinite module, not only its prime-to-three part.

## 2. An actual order-two frame reversing r

The given alpha extends to B by

    Phi_alpha(s)=s f,  Phi_alpha(delta)=delta^-1,
    Phi_alpha(r)=s f r^-1 s.

Put J=s f A. By (1), A r^-1 A^-1=r^-1 f, and hence

    Phi_alpha(r)=J r^-1 J^-1.                         (3)

The actual map Phi_alpha is an involution. Applying it twice to r in (3) shows that Phi_alpha(J)J centralizes r. This element is pure: both J and Phi_alpha(J) have the same transposition image s in S3. Thus

    Phi_alpha(J)J=1.                                  (4)

Write alpha also for the order-two symbol in the genuine semidirect product B semidirect <alpha>. Equation (4) says that

    w3=J^-1 alpha

is an involution, and (3) says that w3 r w3^-1=r^-1.

Retain the actual fixed involution v=u^-1s in B and the regular involution tau=v alpha. Since alpha(v)=v, this is also alpha v. Directly,

    J^-1 v=A^-1 f^-1 s u^-1 s
          =A^-1 f^-1 u=rho_cyc(A)^-1 u.

Therefore the exact expression in the actual F tau coset is

    w3=rho_cyc(A)^-1 u tau.                           (5)

The coefficient belongs to F'. The regular one-section theorem could consequently conjugate w3 to tau by a unique element of F, but no such additional conjugator is needed for the formula below.

There is also an exact useful action identity. Since Phi_alpha(J)=s alpha(A), (4) becomes

    iota(alpha(A)) f A=1.

Using iota(f)=f^-1 and (2), this gives

    alpha(A)=iota(A^-1) f,
    tau(A)=u^-1 rho_cyc(A)^-1 u.                      (6)

These equalities are in the full actual F and do not identify any abelian frame coordinates.

## 3. Transport the literal modular cusp reflection

The actual half rotation from A86 is

    e=(xu)v=x s=r^-1 delta r,  e^2=xy=z^-1.

The element delta alpha is an involution because alpha(delta)=delta^-1. It reverses delta. Consequently

    p_e=r^-1(delta alpha)r

is an involution reversing e and z. Retaining the semidirect multiplication order and using (3),

    p_e=r^-1 delta Phi_alpha(r) alpha
       =(r^-1 s r J r^-1) w3.                         (7)

The coefficient in parentheses can be simplified without commuting any factors. The exact free-product identity is

    r^-1 s r s r^-1=e^2=z^-1.

Since f A=rho_cyc(A), it follows that

    r^-1 s r J r^-1
      =(r^-1 s r s r^-1) rho_cyc(f A)
      =z^-1 rho_cyc^2(A).

Combining this with (5) yields

    p_e=H_e tau,
    H_e=z^-1 rho_cyc^2(A) rho_cyc(A)^-1 u.             (8)

As p_e reverses z, its actual F-head satisfies

    tau(z)=H_e^-1 z^-1 H_e.

By Section1, A and u have zero abelianization. Thus H_e has abelianization (1,1), coming solely from z^-1. This computes the normalization exponent exactly; it is not an unspecified profinite integer.

## 4. Identification with A86's uniquely normalized cusp frame

A86 defines h0 as the unique element of F' satisfying tau(z)=h0^-1 z^-1 h0. If H_e has diagonal abelian coordinate ell, that normalization is h0=z^ell H_e. Here ell=1, so (8) gives the explicit full-word formula

    h0=rho_cyc^2(A) rho_cyc(A)^-1 u.                  (9)

For completeness, multiplication of H_e on the left by z preserves the displayed cusp transport, and its abelianization becomes zero. Any two such heads differ on the left by an element of C_F(z)=closure<z>; zero abelianization forces that difference to be the identity. Hence (9) is exactly the previous canonical h0, not a new choice of frame. The actual reflection h0 tau is z p_e and is an involution because p_e inverts z.

The unique regular one-section conjugator q is therefore now specified entirely by the actual positive r-frame A and the canonical u:

    rho_cyc^2(A) rho_cyc(A)^-1 u=q tau(q)^-1,
    q_ab=(t,-t).                                     (10)

The uniqueness of q uses the actual C_F(tau)=1. In particular the relative Alexander unit remains the same full unit

    a_reg=1-4t,

as in A86. Equation (9) supplies its actual normalized cusp input; it does not solve the nonabelian equation (10) for the abelian coordinate of q.

## 5. Exact remaining comparison and boundaries

The separately proved unique pure s-frame gamma is characterized by v=gamma s gamma^-1. In the actual A45 dihedral quotient its entire image is T^rho_D, giving d_alpha=1-4rho_D. Thus the coefficient gate remains t=rho_D. Formula (9) has not equated these two coordinates. In particular A_ab=0 does not imply t=0: the norm map q->q tau(q)^-1 has nontrivial anti-diagonal abelian kernel, so abelianizing (10) loses precisely this information.

The actual full cusp gate remains Omega_alpha=1, equivalently (v delta^d_alpha)^3=1 by the separately reviewed marked-three-cycle note. Neither (9) nor (6) asserts this torsion equation for the prospective map. They instead exhibit the actual compatibility of Phi_alpha with its genuine r-frame and literal cusp inversion, without first constructing the desired positive conjugator.

All dependencies are the actual marked maps and the full torsion-frame facts used in E.58/E.65, the regular one-section and primitive-cusp centralizer facts used in A86, and the full profinite abelianization. E.65.1 and its actual map/uniqueness proof were reopened for this addendum; the complete attached E.65 proof was already read for the preceding gate note. No finite-group census, generic metabelian model, new realization theorem, unproved R2 input, or automatic coefficient comparison is used. No frozen component or prior research note was changed.
