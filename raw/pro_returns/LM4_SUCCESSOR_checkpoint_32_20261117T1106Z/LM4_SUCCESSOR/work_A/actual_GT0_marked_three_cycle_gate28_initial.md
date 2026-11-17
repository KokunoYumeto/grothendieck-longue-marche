# The actual marked three-cycle and the remaining full cusp gate

Research, checkpoint28. This note leaves the four reviewed checkpoint27 notes and the frozen A85/A86 proposed components unchanged. Both main decisions remain Open. It uses the actual attached modular marking, not a newly chosen S3 action or a finite shadow.

## 1. The actual modular extension of the given involution

Let B=C2(s) amalg C3(r), let delta=sr, and identify its actual pure subgroup F with the free profinite group on

    x=delta^-2,    y=s x s,    z=(xy)^-1.

The exact conjugation table in the attached D.44.8 is

    r x r^-1=y,    r y r^-1=z,    r z r^-1=x,
    s x s=y,      s y s=x.

Write rho=Ad(r)|F and iota=Ad(s)|F. Distinguish this modular cusp delta from the regular involution tau below.

Retain the actual negative-GT0 involution alpha=(-1,f), its canonical u in F', and

    u=f alpha(u),    iota(u)=u^-1,
    v=u^-1 s in B,   tau=Ad(v) Phi_alpha.

Here Phi_alpha is the actual modular extension. Its literal formulas are

    Phi_alpha(s)=s f,    Phi_alpha(delta)=delta^-1,
    Phi_alpha(r)=s f r^-1 s.

To verify the source and signs, alpha c=(1,f) is an actual multiplier-one gentle pair. D.50.23 and E.65.8 give its modular map s->sf, r->f^-1r, delta->delta. The standard c fixes s and sends delta to its inverse. Their composition gives precisely the three displayed formulas. Thus the order-three relation is already valid for Phi_alpha; it is not being supplied by a prospective conjugator.

Moreover alpha(f)=f^-1, either from alpha²=1 and the normalized group law or by applying alpha twice to u=f alpha(u). Hence Phi_alpha² fixes s and delta, and is the identity on B. The two-cycle relation gives f s f=s. Therefore

    Phi_alpha(v)=alpha(u)^-1 s f=u^-1 f s f=u^-1s=v.

Also v²=1. Consequently tau is an actual involution of B and restricts to the regular negative-pants involution called tau in A85/A86. All uses of the regular one-section theorem below are on this actual F restriction.

The canonical half rotation has a particularly simple modular marking:

    e=(xu)v=x s=r^-1 delta r,    e²=xy.

The identity follows by free-product reduction: x s=(r^-1s)^2s=r²s r²=r^-1(sr)r. This is an exact based equality and retains the third-cusp conjugator r.

## 2. The full positive hexagon is one actual torsion equation

Let d=d_alpha be the actual A45 full unit and put m=(d-1)/2. Define

    T_d=v delta^d in B,        Xi_d=T_d³.

Since d is odd, T_d has the three-cycle r as its S3 image. In particular Xi_d belongs to F. Using delta^d=delta x^-m, put u0=u(x,y), u1=u(y,z), u2=u(z,x). Then

    T_d=u0^-1 r x^-m=u0^-1 y^-m r,
    Xi_d=u0^-1 y^-m u1^-1 z^-m u2^-1 x^-m,
    Xi_d^-1=x^m u2 z^m u1 y^m u0.                       (1)

These formulas hold for profinite m by continuity of power maps. No candidate automorphism is assumed.

The positive hexagon for the marked pair (d,u), in the exact C30.1 order, is

    u0 x^m u2 z^m u1 y^m=1.                             (2)

Its left side is u0 Xi_d^-1 u0^-1. Thus (2) is equivalent to Xi_d=1. The other required equation is already the actual swap duality u(x,y)u(y,x)=1.

The equivalence with the canonical full cusp word is exact:

    Xi_d=1  <=>  Omega_alpha=1.                          (3)

For the forward implication, C30 turns the two full equations for (d,u) into a full automorphism theta of F, with theta(x)=x^d and theta(y)=u^-1y^d u. Its explicit third-cusp equation is C30.4, so A86 yields Omega_alpha=1.

For the reverse implication, A86 gives the full third-cusp equation for these same d,u. C29 makes this particular normalized theta a peripheral automorphism. The canonical u relation gives alpha theta=theta c on both generators. Since both alpha and c centralize the geometric S3, A6 forces this very peripheral conjugator theta into GT0. Its hexagon is (2), and (1) gives Xi_d=1. No different conjugator is substituted in this direction.

Thus the modular assignment s->v, delta->delta^d is a homomorphism from the actual B precisely when Xi_d=1. At that point C30 supplies its full pure automorphism and the modular map is an automorphism as well: it is the actual GT0 extension. Defining that map before proving the order-three relation would assume the remaining gate.

## 3. What the actual three-cycle already implies without vanishing

Equation (1) shows unconditionally that Xi_d lies in F'. Indeed u0,u1,u2 have zero abelianization and x+y+z=0, so the sum of the remaining exponents is -m(y+z+x)=0.

The actual tau reverses T_d:

    tau(v)=v,    tau(delta)=v delta^-1 v,
    tau(T_d)=delta^-d v=T_d^-1.

Hence tau(Xi_d)=Xi_d^-1. The regular one-section theorem C43 supplies a unique a_d in F with

    Xi_d=a_d tau(a_d)^-1.                                (4)

Uniqueness uses C_F(tau)=1. Since Xi_d has zero abelianization and tau acts by negative interchange, (a_d)_ab has the form (ell_d,-ell_d). Also Xi_d=1 exactly when a_d=1.

This is a full-group norm equation, not a vanishing result. In particular merely abelianizing the actual hexagon gives zero before any equality a_reg=d is established. The canonical cusp word Omega has a potentially nonzero first coefficient, while its equivalent torsion relation Xi already lies in F'. Equivalence of the two vanishing tests does not identify their abelian images. There is no contradiction and no inference that the coefficient has vanished.

## 4. A second exact frame description of the dihedral coefficient

There is a unique gamma in F such that

    v=gamma s gamma^-1.

For existence, the full free-product torsion theorem conjugates the involution v to s. Its conjugator has S3 image centralizing s, hence in <s>; multiplying on the right by s if necessary makes it pure. Uniqueness follows from C_B(s) intersect F=1. This is precisely the full torsion-centralizer scope already used in E58, not a realization theorem for a new virtually free group.

The equality is equivalent to

    u=iota(gamma) gamma^-1.

Since u belongs to F', gamma_ab=(b,b) for some b in Zhat. In the actual A45 dihedral quotient pi(x)=a, pi(y)=aT, gamma therefore has even reflection parity and a unique image T^rho. The actual swap sends T to T^-1, so

    pi(u)=T^(-2rho),    k=-2rho,    d=1-4rho.            (5)

This rho is the rotation coordinate of the entire actual gamma, not either coordinate of gamma_ab. In contrast, A86 defines q uniquely by the normalized regular cusp reflection and has q_ab=(t,-t), a_reg=1-4t. Consequently the remaining coefficient equality is precisely

    a_reg=d  <=>  t=rho.                                (6)

This compares two explicitly different actual frame coordinates. Equation (5) does not equate them. It provides a canonical interpretation of -k/2 without ever identifying k with q's abelianization.

For completeness the unique pure s-frame beta of Phi_alpha(s)=beta s beta^-1 satisfies

    beta=alpha(gamma)^-1 gamma,    beta_ab=(2b,2b).

Apply Phi_alpha to v=gamma s gamma^-1, use Phi_alpha(v)=v, and use C_B(s) intersect F=1. This is the exact frame law; it does not supply (6).

## 5. The actual LM7/R2 input that remains missing

The authoritative attached D50 theorem lifts an already existing positive peripheral automorphism of the whole pronilpotent source, with all three specified conjugator coordinates. Its proof counts homomorphisms from the genuine source, not from a presentation with an unsatisfied product or torsion relation. E58 extends this to every actual open normal U and its relative pronilpotent quotient, retaining a common finite base and all three coordinates.

In the modular version, the three peripherals are s,r,(sr)^-1. Before applying the count, the new source map on the auxiliary central quotient must already be a homomorphism; its r-image satisfies order dividing three. For the present proposed marked map that is exactly the image of Xi_d=1. Applying the lift theorem to s->v and delta->delta^d without that check is therefore circular.

Equivalently, in the pants version the desired candidate has x-image x^d and y-image u^-1y^d u. The specified third coordinate must conjugate their inverse product to z^d. That is the actual full cusp compatibility, or its genuinely established image at a chosen relative level. The C44 automorphism supplied by the regular Alexander equation is on its own actual relative quotient, and is not claimed to preserve the three original peripheral markings. It therefore does not by itself furnish this R2 input. Nor does its full unit a_reg identify the missing conjugator coordinate with d.

If compatible marked conjugators were proved on every cofinal open-normal relative level, the actual inverse-limit comparison A2 would give the full conjugator. Nothing here establishes those marked relative inputs, their compatibility, or an order-preserving new lift. This is the exact remaining use of R2, rather than a failure of its already proved lifting theorem.

## 6. Dependency and proof audit

For this note I reopened the complete C29 and C30 proofs, the complete A6 proof, the actual D44.8 conjugation table, the complete attached D50 source, E58's entire relative lifting/product proof, and the complete E65 source, including its actual B3/B action and frame multiplication conventions. The attached referee companion was read for comparison only, not substituted for these maps. Their authoritative locations are the original recovered_background/LM7_PUSH_checkpoint_09/sections files; no full attached source was copied into the authored output.

The A45 and A86 coefficient constructions retain their previously full-reviewed scope. The root's separate checkpoint28_root_dihedral_boundary.md proves that pi(Omega)=1 identically and independently of (6). Neither that quotient nor the unconditional properties in Section3 decide (6) or (3). No new finite target, metabelian family, torsion census, or generic profinite recognition theorem is used.
