# The actual canonical equation in the three cyclic-cover modules

Cycle30 research. This is a direct calculation for an ACTUAL negative GT0 involution, before adding a full-GT pentagon assumption. It determines what its canonical norm and negative hexagon contribute to the selected Alexander quotients. The global canonical equation is not replaced by those quotients.

## 1. Actual notation

Let alpha=(-1,f) be an actual nonidentity GT0 involution, with canonical u in F' and

    alpha(x)=x^-1, alpha(y)=f^-1 y^-1 f,
    u=f alpha(u), iota(u)=u^-1, iota(f)=f^-1,
    iota(x)=y, iota(y)=x, z=(xy)^-1.

Use the actual three cyclic-cover coordinates from the companion note `actual_odd_head_common_word_surjectivity30.md`: x-meridian/retained y, y-meridian/retained x, and z-meridian/retained x. First work with the full characteristic-two procyclic coefficient ring Lambda; every formula then projects to every finite head. Write

    U=[u]_x=[u]_y, W=[u]_z=[u(y,z)]_x,
    F_f=[f]_x=[f]_y, G_f=[f]_z=[f(y,z)]_x.

The equalities between the first two coordinates are the actual swap dualities. Their third coordinates obey

    bar(W)=T W, bar(G_f)=T G_f.                            (1)

Here bar sends T to T^-1. All coordinate identifications retain the precise meridian/retained-generator choices.

## 2. Canonical norm and the complete negative hexagon

On the x-cover module, alpha sends the x-meridian to its inverse and inverts the retained head. In characteristic two its action on the kernel module is therefore coefficient bar. The conjugator f lies in this kernel and does not change that action. The canonical equation gives

    F_f=U+bar(U), hence bar(F_f)=F_f.                      (2)

The ACTUAL GT0 negative hexagon is the complete word

    f(x,y) x^-1 f(z,x) z^-1 f(y,z) y^-1=1.                (3)

Evaluate (3) in its stated order in the x-cover. Its six module contributions are respectively

    F_f, 1, bar(F_f), 1, T G_f, 0.

The two units are the x^-1 and z^-1 contributions; they cancel in characteristic two. Thus

    F_f+bar(F_f)+T G_f=0.

Combining with (2) and the invertibility of the group element T gives the exact additional value

    G_f=0.                                               (4)

No multiplier d_alpha is inserted into (3): this is the defining negative hexagon for f, whose multiplier is -1. Confusing it with the prospective positive hexagon for u would change the calculation.

## 3. The entire joint action at this linear level

On the y-cover alpha again acts by coefficient bar: the y-meridian is inverted up to conjugation by f in the kernel, and the retained x is inverted. On the z-cover, (4) makes the image of f trivial in that affine quotient. There x=(0,T), y=(T^-1,T^-1), so

    alpha(x)=(0,T^-1), alpha(y)=(1,T),
    alpha(z)=(T^-1,1).

Consequently alpha acts on the z-kernel module by j(P)=T^-1 bar(P). On the direct sum of the three modules its exact action is

    alpha: (P_x,P_y,P_z) -> (bar(P_x),bar(P_y),j(P_z)).    (5)

The actual v=Inn(u^-1)iota has the same action as iota on these kernel abelianizations, since u belongs to every K_x,K_y,K_z. Thus

    v: (P_x,P_y,P_z) -> (P_y,P_x,j(P_z)),
    tau=alpha v: (P_x,P_y,P_z) ->
                         (bar(P_y),bar(P_x),P_z).         (6)

These formulas satisfy the entire Klein-four multiplication exactly. They are consequences of the actual actions, not independently imposed linear operators.

Applying u=f alpha(u) to all three coordinates now gives precisely

    (U,U,W)=(F_f,F_f,0)+(bar(U),bar(U),j(W)).              (7)

The first two equations are (2), while the third is exactly (1). Thus after the actual negative hexagon is retained, the canonical equation supplies no further relation between U and W INSIDE THESE THREE MODULES. In particular (5)--(7) do not give the missing A89 relation bar(R_d)=T^d R_d. This conclusion does not say that the full nonlinear canonical equation is redundant.

## 4. The marked odd dihedral coordinate is independent at the actual common-word level

For odd n let D_n=<a,R | a^2=R^n=1, aRa=R^-1>, with the actual marked map

    pi_n(x)=a, pi_n(y)=aR, pi_n(xy)=R.

It sends c=[x,y] to R^2, so pi_n(F') is the full rotation group C_n. Combine this map with the three actual Alexander maps of the companion note. Their joint image on F' is exactly

    I_n^3 x C_n.                                        (8)

Here is a direct proof, with no classification theorem. Both projections are onto. If a source word has image (v,R^r), its n-th power has image (v,1), because n is odd and the first factor has exponent2. Squaring a source word kills the first factor, and multiplication by2 is invertible on C_n. Therefore the image contains both direct factors.

The swap iota acts on the rotation coordinate by R->R^-1. Given any U in I_n, any W in I_n with bar(W)=T W, and any k in Z/n, choose w in F' with the required three preimage coordinates from the companion norm proof and rotation k/2. Then u=w iota(w)^-1 is an ACTUAL full-source duality word with

    [u]_x=U, [u(y,z)]_x=W, pi_n(u)=R^k.                  (9)

The same finite-intersection argument as before gives (9) simultaneously at every odd head for compatible U,W,k. This does not conflate k with the separate canonical abelian-frame coordinate t. It shows that the odd part of the dihedral word coordinate cannot be recovered from common-word/duality data in these Alexander modules alone.

## 5. What is and is not exhausted

For actual GT0 canonical data, Sections2--3 prove the exact image of the canonical involution condition and its negative hexagon in the chosen modules. Section4 is an independent actual-source range theorem; its constructed words are NOT asserted to be canonical parameters of GT0 involutions. In particular it does not manufacture a counterexample to a_reg=d_alpha.

The remaining possible force must come from the GLOBAL canonical/integrability condition beyond (7), from the full marked pentagon when alpha lies in full GT, or from a further faithful relative/nonlinear comparison. A module-only replacement of those conditions would lose precisely the information not measured here. The known full-GT dyadic equality and the all-odd-head criterion remain intact, and the full coefficient and nonlinear Omega gates remain Open.

No finite-head census, additional producer, private PDF, or new external theorem is used. All identities are literal marked computations or uniform compact-source arguments.
