# E95 actual cusp path cochains: derivation for the E96 comparison

This is the working proof of the path part. The executed exact certificate is `research_e95/code/a_cusp_kummer_explore.py/.out/.json`. The JSON entry `global_cusp_coefficients[d]` contains the three rational columns named `rational_coboundary`, `Kummer3`, `Kummer_zeta`. In the original ten-coordinate order they give

\[
k_d(g)=(A_g-I)b_d+r_d\kappa_3(g)+s_d\kappa_\zeta(g),\qquad g\in G_K,
\quad \kappa_\zeta(g)=(\chi(g)-1)/3.
\]

The representatives are c-equivariant: `b_cd=J b_d`, `r_cd=-J r_d`, `s_cd=J s_d`. Their actual tau values are in `c_equivariant_cusp_tau_Kummer`. Every column is a rational vector in the actual V basis. Both r and s have zero compact coordinates. The displayed sum is integral on actual arithmetic elements; the rational summands are retained separately.

## Actual arithmetic conventions

Use the unchanged E49/E77 source: tau and tauprime=c tau c generate the actual free pro-three unramified quotient P. Their cyclotomic values are7; kappa3(tau)=1 and kappa3(tauprime)=-1. Kappa3 is the ordinary Kummer cocycle of3 with coherent positive real roots, so kappa3(cgc)=-kappa3(g). Choose coherent roots of zeta3 from the fixed cyclotomic system. Then kappa_zeta=(chi-1)/3, with values2,2. The literal identity lambda²=-3zeta, with coherent odd roots of -1 all equal to -1, permits the representative

\[
\kappa_\lambda=(\kappa_3+\kappa_\zeta)/2.
\]

Changing an exponent of zeta by3 changes this representative by the explicit Tate coboundary chi-1. The code retains chosen integer exponents; it does not erase those carries.

## The sole finite phase and its actual basis morphism

Let P=A0, Q=A2, and retain E37's actual framed point z_P. Its proper elliptic Kummer class is the class represented by f2 on tau: if t lifts P in the c-fixed O3 Tate basis, the compatible division points of P give (g-1)t/3, whose tau value is t2.

E24/E37 give the actual toric tuple

\[
3z_P=(3^{-2},-3^{-1},\lambda^{-1},\lambda^{-2},\zeta^2\lambda^{-3}).
\]

Divide this cohomology class by E92's exact elliptic carry c_T. The free toric part of kappa(z_P)-[f2] is forced to be

\[
(3^{-1},3^{-1},\lambda^{-1},\lambda^{-1},\lambda^{-2}).
\]

The sign in the second rational coordinate has its unique coherent odd roots and hence zero pro-three Kummer class. The only remaining possibilities are the three global mu3 factors. Write their exponents epsilon1,epsilon2,epsilon3 in F3. The exact tau vector before those torsion additions is

\[
(0,1,-1,-3/2,1/2,-1,-3/2,1/2,-3,1).
\]

The torsion columns are2(A1-A2),2(B1-B2),2(C1-C2). These are the actual Shapiro maps, with no unnamed toric change of basis.

Use the actual line functions

\[
f_{10}=(x+\zeta^2y+z)/(x+y),\qquad
f_{01}=(\zeta^2x+y+z)/(x+y).
\]

Their divisor rows are respectively A1+B0+C1-3O and A0+B1+C2-3O. Their compact character columns are forced by killing the actual j image, namely `-divisor_row*U/3`. The completed framed evaluations at z_P are1/3 and1/(3lambda), respectively. The literal vector-frame sign is (-1)^(ord_P f+ord_O f); its coherent odd roots give zero Kummer class. Thus no full multiplicative equality is asserted after deleting that sign.

The two Shapiro identities on BOTH tau and tauprime have the same possible boundary6a. They force

\[
(\epsilon_1,\epsilon_2,\epsilon_3)=(1-t,t,1+t),\quad t\in\mathbb F_3.
\]

The remaining vector(-1,1,1) is exactly j(P) in the three toric mu3 factors, by the E37 inverse divisor Weil pairing. This is also checked through the same global cohomology matrices.

For u=1+3t define the actual Tate-basis change t_E to u t_E. It preserves c, the reduction P, and the O3 basis. Its induced V matrix is

\[
P_u=I+t j_*\pi_E.
\]

It fixes every peripheral vector and commutes with both retained T1 and J1. It satisfies P_u P_v=P_(uv), and its inverse is integral. On global H1 the changed coordinates are P_u^{-1}. The certificate computes the unique fixed coboundary h with

\[
P_u^{-1}k_P^{old}(\tau)-k_P^{new}(\tau)=(T_1-I)h,\qquad J_1h=h.
\]

The new finite exponents are(1,0,1). The resulting vector is

\[
k_P(\tau)=(0,1,-1,1/2,-3/2,-1,-3/2,1/2,-1,-1).
\]

This is a proved coordinate morphism. The old actual t is retained, not assigned a numerical value. On the full free pro-three group one literal lift sends each handle generator x_i to x_i^u times the ordered product of peripheral powers t U_di, and fixes all eight peripheral generators. Its Frattini matrix is invertible, so it is an actual automorphism. Transport the FULL action by Psi^{-1}rho(g)Psi and every quotient/unit map by F Psi. No equality of the higher actions before and after this transport is asserted. The first-degree matrices remain unchanged; higher maps remain their actual transported maps.

## Full cochain formula for P

Let h_+ and q be the exact fixed columns E92.22 and E92.26, embedded in V, and put h*=h_+-q. Let c_T(g) be the normalized toric Kummer cocycle of the literal E92 tuple. On G_K it is the explicitly linear combination of kappa3 and kappa_zeta obtained from the Shapiro formula; its two coefficient columns are retained in the program. The exact identity on the free source is

\[
3u_{f2}(g)=c_T(g)+(A_g-I)h_*.
\]

Both sides are cocycles, agree on tau,tauprime, and vanish at c. Therefore they agree on the actual entire source. Adding the phase-zero toric tuple above gives k_P. This proves its full formula, not merely values on selected Frobenii.

## Actual CM and line-addition transport

Use the actual algebraic automorphism sigma:[x:y:z] to[x:y:zeta z]. It sends P to Q and fixes O. On V its matrix is

\[
\Sigma=\begin{pmatrix}R&0\\(UR-SU)/3&S\end{pmatrix},
\]

where S is its actual cusp permutation. This follows from its proper CM map R, its literal torus permutation, and equivariance of the uniquely specified j map. It commutes with every actual G_K coefficient matrix.

Push the vector frames of z_P through sigma. At Q and O their factors are both zeta^{-1}; at all other cusps their factor is1. Dividing by the O factor shows

\[
\sigma_*z_P=z_Q+\delta,
\]

where delta has value1 at Q and zeta at every other non-O cusp. Hence `k_Q=Sigma*k_P-kappa(delta)` as actual cohomology classes, with explicit representatives retained.

For a+b=d in E[3], the ratio of the chord (or tangent for a=b) through a,b to the line through d,-d,O has divisor a+b-d-O. For d=O use the tangent at O as denominator. Multiplying the framed line bundles by this rational function gives

\[
z_a+z_b-z_d=(lead_r(F)/lead_O(F))_{r\ne O}.
\]

This is the actual vector-frame identity. Its leading terms are computed in the exact tangent parameters: at A_i use x/z, at B_i use y/z, and at C_i use z/x. Every value is an actual sign*zeta^e*lambda^n S-unit. These identities generate all eight z_d from P,Q.

The certificate verifies all64 additions on the two free generators. For every addition, the SAME integral boundary coefficient gives the difference at tau and tauprime. It also checks all8 third multiples, every compact Kummer projection, conjugation, and all actual field arithmetic. Thus the point identities and their cohomology transfers do not rely solely on comparison at a single cyclic subgroup.

Finally average a point cocycle with the c-transform of the conjugate point cocycle. This uses division by2 and preserves its actual Kummer class. It gives the coefficient columns exported in `global_cusp_coefficients` and the displayed exact c-equivariance. Changing a tau representative by (T1-I)b changes its cusp contribution to the wild obstruction by a literal image of T2-7, so the resulting15 obstruction coordinates retain this representative independence.

## Scope for E96

All these path formulas are now explicit on G_K in terms of A_g, chi, and the ordinary kappa3 cocycle with its actual source marking. They replace the framed-division input in E37.10. On the global slice with zero free proper-elliptic coordinate b, the abelian input itself is likewise u_f2 times its finite elliptic residue plus ordinary toric Kummer classes. The free proper-elliptic generator u_f1 remains a separate genuine arithmetic cocycle; this derivation does not evaluate its arbitrary Frobenius values.
