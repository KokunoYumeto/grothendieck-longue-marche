# The canonical Alexander equation in the original first-cusp marking

Research, checkpoint 28. This is a separate consequence of the fully reviewed explicit three-cycle cusp-frame formula. All prior notes and formal components remain unchanged. It gives an exact equation using the original alpha, not a new positive peripheral map.

## 1. The canonical reflection has a literal modular expression

Retain B=C2(s) amalg C3(r), delta=sr, x=delta^-2, y=sxs, z=(xy)^-1 and the actual alpha, v, tau. The preceding note proved

    p_e=r^-1(delta alpha)r,  e=r^-1 delta r,
    e^2=z^-1,  h0 tau=z p_e.

Therefore, using z=r^-1 delta^-2 r and preserving factor order,

    h0 tau=r^-1(delta^-1 alpha)r.                    (1)

This is the actual uniquely normalized reflection, because the previous proof already computed the head abelianization before multiplying by z. It is not an independently selected conjugate.

Let q be A86's unique pure element with h0 tau=q tau q^-1. Multiplying (1) by r and using tau=v alpha gives

    (r q) tau (r q)^-1=delta^-1 alpha,
    Phi_alpha(r q)=delta (r q) v.                    (2)

The second equality follows by comparing the B-heads in the first: (r q)v Phi_alpha(r q)^-1=delta^-1. It is thus a full actual equation for the same q; it does not supply a formula for its abelian coordinate.

## 2. Transport C44's unique solution, with its coefficient unchanged

Write sigma=Ad(h0)tau. A86/C44 supplied the unique full element

    g=e(q v q^-1) in F,
    sigma(g)g^-1=z,
    g_ab=(1-2t,2t),  q_ab=(t,-t).

Conjugating sigma and the equation by r, define

    sigma_x=Ad(delta^-1)Phi_alpha|F,
    G=r g r^-1.

Equation (1) shows these are exactly the transported involution and solution. In particular

    sigma_x(G)G^-1=x,
    Phi_alpha(G)=delta^-1 G delta^-1.                (3)

For the second form, multiply delta^-1 Phi_alpha(G) delta G^-1=delta^-2 by the indicated factors. Every term in (3) is defined in the existing actual B; the right side of the second equality is in F because delta^-2=x and F is normal.

The solution G is unique in the full F, by C44's uniqueness transported by r. Its abelianization is obtained by the actual cyclic matrix rho_cyc:

    G_ab=(-2t,1-4t)=(-2t,a_reg).                     (4)

Consequently the original first-cusp quotient F/normal-closure(x), with y as generator, sends G to y^a_reg. This is the same full profinite unit a_reg as before. It is not a newly normalized or unspecified unit.

An alternative full expression records the commuting involution:

    J_x=(r q)v(r q)^-1,  G=delta J_x.

Here J_x is an involution and commutes with delta^-1 alpha, by (2) and the actual commutation of v and tau. This also verifies (3) directly. Neither J_x nor r q is assumed to preserve all three original peripheral subgroups.

## 3. Explicit action and the remaining scalar comparison

Put j_delta=Ad(delta^-1)|F, distinguishing it from the involution J_x. Free-product reduction gives

    j_delta(x)=x,  j_delta(y)=y^-1 x^-1.

The actual original alpha sends x to x^-1 and y to f^-1y^-1f. Therefore

    sigma_x(x)=x^-1,
    sigma_x(y)=j_delta(f)^-1 x y j_delta(f).          (5)

Thus (3) is an explicit equation determined by the original actual f and alpha. No additional cusp conjugator is part of its input. The full group equation (3), together with C44, supplies uniqueness and the full-unit conclusion; a solution is not inferred merely from its abelianization.

For an abelianization G_ab=(b,a), the second equality in (3), equivalently alpha(G)=j_delta(G)x, gives

    (-b,-a)=(b-a+1,-a),  hence a=2b+1.

The actual solution has b=-2t, by (4), so this recovers a_reg=1-4t. The actual A45 dihedral exponent is k, with d_alpha=2k+1. The coefficient gate can now be stated as

    a_reg=d_alpha  <=>  G_ab,x=k.                    (6)

The two entries in (6) are still different actual invariants: the first is a coordinate of C44's unique full solution G, while the second is the rotation exponent of the canonical u in the specified universal dihedral quotient. Equation (3) has not equated them. In particular one must not replace the full dihedral exponent by the ordinary abelianization of either u or q.

The first-cusp reformulation makes the existing relative Alexander input explicit in the original alpha-marking. It does not manufacture the missing marked three-cusp R2 datum: proving (6), and then the nonlinear Omega_alpha=1, remains necessary. No torsion equation for the prospective map s->v, delta->delta^d is assumed, and no relative automorphism is silently upgraded to a full three-peripheral automorphism.
