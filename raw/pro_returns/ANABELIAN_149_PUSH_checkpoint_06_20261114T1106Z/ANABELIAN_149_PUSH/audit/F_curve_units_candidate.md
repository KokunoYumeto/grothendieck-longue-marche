# Candidate: point-theoretic Kummer classes and point functions on arbitrary curves over Qsolv

Status: independently reviewed and approved by root; integrated as F.26–F.28 with proved result-ledger rows. The historical filename records the review stage. The source Jossen (2009), Chapter 6, was actually opened at Theorem 6.0.1, Proposition 6.3.1 and Lemma 6.3.2, including the latter's proof.

Put k=Qsolv. All finite extensions below are inside Qbar. By F.16, D(E*)=k* for every finite E/k, and every such field contains all roots of unity. F.24 supplies finite-quotient detection on every geometrically connected curve over every finite E/k.

## 1. Point-Kummer images span the maximal trivial quotient

Let L/k be finite, let U/L be a smooth geometrically connected curve, and choose x0 in U(L). Write C for its smooth proper completion and D=C\U. First extend L finitely so that D is split. Let A=J_D be the reduced-modulus generalized Jacobian, pointed by x0; for D empty this is J_C. Its Abel–Jacobi map j:U→A sends x0 to 0 and identifies T_l A with the pro-l abelianization of pi1(U_Qbar). A regular unit u with u(x0)=1 corresponds, by the generalized Jacobian universal property, to a unique character A→Gm.

Descend U,C,D,x0,A,j to a number field F⊂L with L=Fk. For a fixed prime l, set H=G_L and

    V=V_l A,  W=V_H=V / span_Q_l{(h−1)v : h∈H,v∈V}.

This is a finite-dimensional quotient of the G_F-representation V, because H is normal in G_F. H acts trivially on W. Let W0 be the image of T_l A in W; it is a G_F-stable full Z_l-lattice.

For every geometric point x of U, choose a finite E/L over which x is defined and project its Abel–Jacobi Kummer cocycle to W. Restricted to G_E, this is an actual homomorphism

    c_x:G_E→W0,

independent of the chosen division points: G_E⊂H acts trivially on W, so projected coboundaries vanish. Its Q_l-span does not change when E is further extended finitely, since the image of a finite-index subgroup has finite index in the image of a homomorphism into a Z_l-module.

The spans of all these images generate W. Otherwise a nonzero Q_l-linear functional on W annihilating all of them, after scalar multiplication, is integral on W0. Using the rational point x0 to split the arithmetic fundamental group, it defines a nonzero continuous homomorphism pi1(U)→Z_l which is zero on the base-point G_L and on all closed-point decomposition groups. A nontrivial finite quotient of its image contradicts F.24. This is exactly where detection is used; no conclusion is drawn from mere elementwise conjugacy.

Consequently finitely many points x1,...,xr already suffice to span W by their projected Kummer images.

## 2. Actual values force arithmetic equivariance over one number field

Suppose xi in inverse_limit_n H1(U,mu_n) has an actual multiplicative Kummer value b_x∈E* at every x∈U(E), for every finite E/L. Choose the actual value b0 at x0 and subtract kappa(b0). The resulting class xi0 is zero at x0. Since mu_infinity⊂L, its l-primary geometric part is a G_L-equivariant integral functional

    lambda:T_l A→Z_l(1).

It factors through W after tensoring Q_l. With the normalized actual value a_x=b_x/b0, evaluation gives

    lambda(c_x(h)) = kappa_l(a_x)(h),  h∈G_E.

Choose the finite spanning collection from §1, then a single number field M containing F, the coordinates of all xi, all their actual normalized values ai, and b0. Put L'=Mk. All the chosen points and values are M-rational. Restriction of each c_xi to G_L' preserves its Q_l-span, so those restricted images still span W.

Both W and Q_l(1) have trivial G_L'-action. For g∈G_M and h∈G_L', the cocycle identities and normality of G_L' in G_M give

    c_xi(ghg^{-1}) = g c_xi(h),
    kappa_l(ai)(ghg^{-1}) = chi_l(g) kappa_l(ai)(h).

Here the points xi and ai themselves are fixed by G_M. Combining the two identities with evaluation shows

    lambda(g c_xi(h)) = chi_l(g) lambda(c_xi(h)).

Since the images span W, lambda is G_M-equivariant on all W, and therefore its integral composite T_l A→Z_l(1) is G_M-equivariant. The field M may depend on l; this will not cause a problem because the geometric unit lattice below is fixed.

For proper U this immediately gives lambda=0: at a good prime of M different from l, the Frobenius eigenvalues of T_l J have complex absolute value sqrt(q), while that on Q_l(1) is q. This is precisely Jossen Proposition 6.3.1. Thus every point-theoretic class on a proper pointed curve is the class of its actual constant value b0.

## 3. Integral unit lattice and the Picard Tate component

For affine U, apply Jossen Lemma 6.3.2 over the number field M:

    Hom_M(A,Gm) tensor Z_l = Hom_{G_M}(T_l A,Z_l(1)).

This is the integral statement, not merely a rational Tate-Hom theorem. Pulling characters back along j identifies the right-hand functional with an l-adic combination of normalized regular units.

There is one fixed finitely generated free unit lattice P, independent of M and l. Indeed, after D is split over the original F and x0 is F-rational, every geometric unit modulo constants is defined over F when normalized to take value 1 at x0: its divisor is supported on the F-rational boundary, and every Galois conjugate has the same divisor and the same normalized value, hence is equal. Thus

    P={u∈O(U_F)* : u(x0)=1}
      = Hom_M(A,Gm)

for every further number field M. The equality is via the generalized Jacobian universal property, not an assertion that the boundary-divisor lattice is primitive.

For every l, xi0 is therefore in P tensor Z_l. Equality of the normalized arithmetic cohomology classes follows from equality of their geometric functionals and their zero values at x0. Choosing one Z-basis u1,...,us of P gives

    xi = kappa(b0) + sum_j lambda_j kappa(uj),  lambda_j∈Zhat.

In particular the Picard Tate component of this particular point-theoretic class is zero. This does not assert T Pic(U)=0 as a group. If only the rational Tate-Hom statement were used, the same integral conclusion would require the Kummer exact sequence: the quotient of integral H1 by the completed unit group is T_l Pic(U), which is torsion free. That saturation argument also avoids any primitive-boundary-lattice assumption. The cited Jossen lemma already supplies the integral assertion directly.

The special Tate-Hom case can also be checked through the extension class. For 1→T→A→J→1, its character pushouts are the boundary-divisor points in J∨(M). On Tate modules the obstruction to extending a character is the corresponding Kummer class, using the Weil pairing. Mordell–Weil plus Kummer injectivity identifies the rational kernel with the rational character lattice of A; Frobenius weights rule out a remaining map from V_l J to Q_l(1). The integral saturation is then the preceding Kummer argument. This explains the precise content of the external input.

## 4. General integrality uses the existing norm-to-line argument

For each split boundary point d, choose by Riemann–Roch a finite map pi:C→P1_L with a simple zero at d and nonzero values at every other boundary point. Delete its branch values, 0, infinity and all boundary images. The resulting finite etale map W→V has W⊂U and V a punctured rational line.

The norm of xi|W has actual Kummer values at all finite-extension points of V: a fibre value is the product of field norms of the supplied actual values at its residual points. Apply F.18 to conclude that this norm class is an actual regular-unit class. Its residue at 0 is exactly the residue lambda_d of xi at d. All other points over 0 lie in U and have residue zero; the residue degree at d is one. The norm formula has residue degrees, not ramification multipliers. Hence every lambda_d is an ordinary integer.

The divisor matrix of the normalized basis units uj is an injective integer matrix. Its product with the vector of profinite exponents lambda_j is the integral boundary-residue vector. An invertible square minor and its adjugate force each lambda_j to be rational. Since Q intersect Zhat=Z, they are all ordinary integers. Therefore

    xi=kappa(h),  h=b0 product_j uj^{lambda_j} ∈O(U)*.

At every finite-extension point x, the actual value satisfies b_x/h(x)∈D(E*)=k* by F.16. This proves actual-unit reconstruction after the harmless finite extension used to split the boundary and choose x0. It does not use a global vanishing assertion for divisible Picard points.

## 5. Point functions of pinned curve-to-Gm morphisms

Let phi:U_et→Gm_et be pinned and relative over a finite L/k. After a finite Galois constant extension, choose x0 and split the boundary. Pull back the target coordinate class and apply §§1–4 to obtain h∈O(U)* with

    phi(x)=c_x h(x), c_x∈k*,

at all geometric points. Here field-source reconstruction gives the actual values. We first work over this enlarged L.

### Constant h

If h=h0 is constant, every value lies in h0 k*. Choose a nonzero algebraic beta with beta/h0 not in k, and make one finite constant extension containing beta. The inverse image of beta has no closed point, hence is empty; a nonempty closed subset of the curve has a closed point. Pull back t−beta on all of U and apply the unit theorem to get g∈O(U)* with

    phi(x)−beta=d_x g(x), d_x∈k*.

The left side belongs to the current constant field L for every geometric point x. If g were nonconstant, a closed point of degree over L larger than deg(g:C→P1), supplied by F.24, would have g(x) not in L, a contradiction. Thus g is constant. Ratios with x0 give

    (h0 c_x−beta)/(h0 c_x0−beta) ∈ k.

Since beta/h0 is not in k, this forces c_x=c_x0. The point map is constant. Its closed-subtopos factorization and relativity identify the entire morphism with the corresponding algebraic constant map.

### Nonconstant h

The point map is nonconstant, since a constant value would put h(x) in a fixed one-dimensional k-vector subspace of L for every x, contradicting the same high-degree argument. For b∈k*, put U_b=U\phi^{-1}(b), a nonempty open, and pull back t−b. If necessary make a further finite constant extension to give U_b a point and split its boundary. The unit theorem gives a regular unit h_b on that base-changed open with

    phi(x)−b=d_{x,b}h_b(x), d_{x,b}∈k*.

For b=1, the rational function c_x h−d_{x,1}h_1−1 has a pole divisor of degree bounded independently of x. Choose a closed point x outside the finitely many exceptions with degree over the current finite constant extension of L larger than that bound, using F.24. Vanishing at x forces the rational identity

    c h−d h_1−1=0,

so h_1=A h+B with A,B∈k*.

For every x with h(x) not in k, the pointwise identity gives

    (c_x−d_{x,1}A)h(x)=1+d_{x,1}B.

Thus c_x=−A/B=:c. Such x cannot lie in the removed fibre phi(x)=1. Consequently phi(x)=c h(x) whenever h(x) not in k.

For any b∈k*, work over the finite constant extension on which h_b was obtained and choose a sufficiently high-degree point outside all exceptions and with degree greater than deg(h), so h(x) is outside that field and hence outside k. The bounded-pole-degree argument again gives

    h_b=e_b(c h−b), e_b∈k*.

Since h_b is a unit on U_b, every zero of c h−b in U belongs to phi^{-1}(b). For any remaining geometric point x with h(x)∈k*, choose b=c h(x)∈k*. This forces phi(x)=b. Thus phi's full geometric point function is the regular unit c h.

Finally descend from the finite Galois constant extension. The constructed unit is unique because it agrees with the given point function on all geometric points. That point function is G_L-equivariant, so the unit is Galois invariant and descends. This proves the algebraicity of point functions for all smooth geometrically connected curve sources over every finite L/Qsolv.

This last statement is about point functions. It does not by itself identify full topos morphisms for an arbitrary non-etale curve map; that additional conclusion is only needed through CHW's precise reconstruction criterion or F.22 where applicable.

## Primary source record

- Jossen, Peter (2009), On the arithmetic of 1-motives, doctoral dissertation, Central European University, Budapest. Author PDF https://www.jossenpeter.ch/PdfDvi/Dissertation.pdf. Actually opened through the search-service cached primary PDF: Theorem 6.0.1 p.75; Proposition 6.3.1 pp.80–81; Lemma 6.3.2 and proof pp.81–82. The latter states integral Tate-Hom full faithfulness for semiabelian varieties over a number field. It is applied only after constructing the finite number field M, not directly over Qsolv.
- Bresciani, On the section conjecture over fields of finite type, arXiv:1911.03234v3, Proposition 4.6 proof p.9, opened primary arXiv PDF, explicitly identifies the generalized Jacobian Tate module with the geometric abelian fundamental group and the evaluation with point Kummer classes. The final version's corresponding proposition cites its original generalized-Albanese source; root is checking the higher-dimensional version separately.
- F.24 and the exact already-opened sources supporting it supply the detection theorem. F.18 supplies the norm target unit theorem. The norm-residue computation is the already-reviewed one in F.5.
