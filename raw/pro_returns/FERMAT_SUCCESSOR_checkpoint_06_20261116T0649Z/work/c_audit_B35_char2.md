# Independent audit of B.35 and the characteristic-two translation paths

**Auditor:** Part C agent. **Date:** 2026-11-16. The B.35 source and the exact scripts were inspected. B files were not edited.

## Verdict on B.35

The nonvanishing argument is valid for **every** good rational prime (p\ne3), in precisely the unit tangent (q_0=Z/X) at (O=C_0=[1:-1:0]). It proves (m_p\ge1), and hence the unscaled input (\kappa_3(p)w) does not lift to intrinsic class three. This is a conclusion about the actual integral action class, not an upper bound obtained from its coefficient group. The field and tangent are explicitly distinguished from the (A_0) base point used for B.29--B.34.

### The tangent-rescaling identity

The automorphism (sigma[X:Y:Z]=[X:Y:\zeta_3 Z]) is defined over (K=\mathbf Q(\zeta_3)), fixes (O), and satisfies (sigma^*q_0=\zeta_3q_0). A chosen path between the two tangents supplies the actual based automorphism. Its arithmetic commutator is peripheral with abelian class (\kappa_3(\zeta_3)e_O), with the orientation fixed by the positive peripheral convention. The based lift need not have order three: its cube can be inner peripheral. This distinction is essential but does not affect the degree-three action or the cohomology identity.

On the abelian module (L=\gamma_2N/\gamma_4N), applying that commutator identity to a lift (omega) of (w) gives

\[
(sigma-1)[\eta]=\operatorname{ad}_{w*}(\kappa_3(\zeta_3)e_O).
\]

The discrepancy (sigmaomega-omega) is precisely an (A(-1))-coboundary. No division by three and no assumption of a finite-order based lift is used.

### Both primitive injections survive local cohomology

The peripheral vector (e_O) is primitive in the rank-eight boundary lattice, which itself injects into (V) with torsion-free compact quotient. Thus (\mathbf Z_3(1)e_O\to V) has torsion-free quotient. Its good-Frobenius eigenvalues have complex absolute values (sqrt q) or (q), so its invariants vanish.

The primitive decomposable vector (w=u\wedge v) has two factors extending to an integral basis, because one of its (2\times2) minors is a unit (the coefficient at (A_0\wedge A_2) is one). In a Hall ordering beginning with (u,v), the ten brackets ([e_i,w]) are ten different Hall basis vectors. Hence (\operatorname{ad}_w:V\to A(-1)) is a primitive injection with free quotient. All good-Frobenius eigenvalues in that quotient have positive weights and are not one. Both exact sequences therefore inject unramified (H^1).

For a good (K)-prime of residue size (q), the unit (\zeta_3) has exact order three in the completed three-primary residue-unit group. Its Kummer value is ((q-1)/3), up to an orientation unit, in (\mathbf Z_3/(q-1)). It can have zero reduction in the first finite Kummer quotient when the field already contains a ninth root of unity, but the completed class still has order three. Thus its image under both injections is nonzero. This proves the asserted lower bound for every good prime, not only two.

## Characteristic-two geometry is genuinely based

In the coordinate change

\[
x=Z/(X+Y),\qquad y=X/(X+Y)+\zeta,
\]

the inverse is ([X:Y:Z]=[y+\zeta:y+\zeta^2:x]). Substitution gives (y^2+y=x^3) identically. The eight finite points listed in B.35 are the nonzero three-torsion points, with origin at infinity.

The identity ([2](x,y)=(x^4,y^4+1)) is valid as a function-field identity, not merely on the nine rational points. Indeed the tangent slope is (x^2), so the addition formula gives the first coordinate (x^4), and the second is (x^3+x^6+y+1=y^4+1), using (y^2+y=x^3). Therefore Frobenius four is ([-2]).

For (a_{r,b}(x,y)=(x+r,y+r^2x+b)), substitution gives the curve equation whenever (b^2+b=r^3), because (r^4=r) in (mathbf F_4). In (t=x/y), this map is (t+O(t^2)). The original parameter (q_0=x/(y+\zeta)) satisfies (t/q_0=1+\zeta/y=1+O(q_0^3)). Thus these are the same unit tangent. If a parameter is changed by (t\mapsto t u(t)) with (u(0)=1), every (u(t)) has a unique compatible (3^n)-th root with constant term one. The induced maps of the tame Puiseux fibre compose literally. Hence the quaternion group acts genuinely, and its action commutes with the based arithmetic Frobenius over (mathbf F_4). SGA1 specialization transfers this to the genuine local pro-three action.

## The arbitrary quaternion lift is legitimate only up to a controlled conjugacy

The script's compact quaternion matrices need not coincide with the original chosen CM basis. Any two integral lifts of the same residual (Q_8)-representation are strictly conjugate: solve the successive congruence conjugacy problems using (H^1(Q_8,-)=0), since eight is a unit in (mathbf Z_3). The determinant of the conjugator can be made one by multiplying it by the unique scalar square root of its inverse determinant in (1+3\mathbf Z_3). This keeps (w) literally fixed.

If this compact conjugator is (B\equiv1\pmod3), its full mixed-lattice conjugator is

\[
\begin{pmatrix}B&0\\U(B-1)/3&I\end{pmatrix}.
\]

It is integral and commutes with Frobenius four, because that Frobenius is scalar (-2) on the rational compact subspace and scalar four on the toric subspace. Thus the invariant cokernel and its Smith invariants are unaffected.

It would be incorrect to use the old CM matrix (R_3) with the script's new quaternion lifts without conjugating it as well. I independently checked that (R_3) fails to normalize six of those eight matrices modulo (3^{10}). B corrected this by using the unique compatible binary-tetrahedral order-three matrix with residual action (R_3). The actual matrix must agree with it: after the quaternion conjugacy, any two such intertwiners differ by a scalar, and (mathbf Q_3) has no nontrivial scalar cube root of unity.

## Actual Frobenius-two descent

Because the coordinate change involves (zeta), the arithmetic Frobenius of the original (mathbf F_2) curve becomes

\[
(x,y)\longmapsto(x^2,y^2+1).
\]

The extra one is required. Its square is Frobenius four, and it conjugates the quaternion automorphisms by ((r,b)\mapsto(r^2,b^2)). The script's compact matrix (J-K) has that intertwining action, determinant two, and the correct residual action. After matching (Q_8), any alternative differs by a scalar. The determinant makes that scalar (\pm1), and the residual action selects the stated sign. The full degree-one matrix follows from commuting with Frobenius four and the exact integral cusp gluing.

Quaternion averaging commutes with Frobenius two because that Frobenius normalizes (Q_8). On the quaternion-invariant coefficient lattice the restriction from the unramified (mathbf Q_2) group to its unramified quadratic extension is (1+R_2). On (C_4=\operatorname{coker}(R_2^2-1)), its image is exactly the (R_2)-fixed subgroup: (R_2) is an involution there and two is a three-adic unit. Restriction is injective and preserves orders. The finite symmetry conditions in B.35 therefore have the correct arithmetic descent, not merely a geometric (mathbf F_4) specialization.

## Why the class cannot be an inner path term at two

The quotient map (A(-1)\to A(-1)/\operatorname{ad}_wV) has free target with no Frobenius invariants, so the induced map on local (H^1) has kernel exactly the injected image of (H^1(V)). If the local (eta) were (operatorname{ad}_w(x)), quaternion invariance and injectivity would force (x) to be quaternion-invariant. But

\[
V^{Q_8}=\mathbf Z_3e_O,
\qquad H^1_{\rm ur}(V)^{Q_8}=(\mathbf Z/3)e_O.
\]

The first equality follows because the compact representation has no invariants and the eight remaining cusps are a regular (Q_8)-set. The second uses exact averaging. The order-three automorphism (sigma) fixes this entire group. Hence ((sigma-1)x=0), contradicting the nonzero class (\kappa_3(\zeta)e_O). The projection of (eta) to the quotient by inner path terms is necessarily nonzero. Any purported zero result from an affine-automorphism invariant calculation would therefore expose a lost path term or a wrong comparison, not prove vanishing of the actual class.

## Exact translation-path calculation, without a canonical-comparison claim

The independent standard finite-field calculation is in `deliverable/code/c_char2_translation_paths.py`, with `.out`, `.json`, and `_matrices.npz` outputs. It works in (mathbf F_4=mathbf F_2[\zeta]/(\zeta^2+\zeta+1)) and constructs the complete framed point group (J_{E,D}(mathbf F_4)), of order (3^{10}), directly.

Write (z_P) for the framed degree-zero line bundle (mathcal O(P-O)), with frames (s_P^{-1}) at (P), (s_O) at (O), and one elsewhere. For (P,Q\ne O), the Miller function given by their line divided by the vertical line at (P+Q) has divisor (P+Q-(P+Q)-O). Its regularized leading values at the cusps, divided by its leading value at (O), are exactly the toric correction in (z_P+z_Q-z_{P+Q}).

At a finite cusp (R=(x_R,y_R)), put (delta=x-x_R). The equation gives

\[
y-y_R=x_R^2\delta+\delta^3+\delta^6+\cdots.
\]

Consequently a nonvertical line has a leading coefficient read from its constant term, its slope term, or the cubic term; no numerical expansion is needed. The prescribed parameter derivatives relative to the invariant differential (dx) are

\[
k_R=\frac{ds_R}{dx}=
\begin{cases}
x_R,&R=A_i\text{ or }B_i,\\
(y_R+\zeta)^{-1},&R=C_1,C_2,\\
1,&R=O.
\end{cases}
\]

The leading value in the prescribed parameter is the leading value in (delta) multiplied by (k_R^{-\operatorname{ord}_R f}). At (O) the Miller functions used have leading coefficient one. This gives an exact abelian group law, verified on all (9^3=729) triples. Its abstract type is (C_9^2\oplus C_3^6).

For a geometric automorphism (g) with (g^*dx=c_gdx), the pushed frame at (gP) differs by (c_g k_{gP}/k_P), and the pushed frame at (gO) differs by (1/(c_g k_{gO})). These factors, together with (z_{gP}-z_{gO}), give its full action on the finite framed group. The script verifies this action on all group laws for the quaternion generators, the order-three CM automorphism, and translations by (A_0,A_2), for 891 checks. It also verifies all 81 laws for the actual arithmetic Frobenius two, whose action on the prescribed original-model frames has no omitted derivative factor.

Translation by (d\in E[3]) preserves (dx). Its image of the original unit tangent has derivative (k_d) in the prescribed parameter at (d). Thus the actual tangent-path class is the framed point

\[
                         z_d+e_d\kappa_3(k_d).
\]

This formula recovers (\kappa_3(\zeta)e_O) for a tangent rescaling fixing (O), and gives zero for the quaternion automorphisms, so it retains exactly the known normalization.

The final comparison to (V/(F_4-1)V) is kept explicit. On the compact quotient (F_4-1=-3), so (\kappa(A_0)) has top coordinate (-f_1), not (+f_1), and similarly (\kappa(A_2)) has (-f_2). Matching only compact and toric parts leaves sixteen (mathbf F_3) shear coordinates. The actual geometric automorphisms and Frobenius two impose rank-fifteen affine constraints. Therefore **exactly three** equivariant comparisons remain. The JSON file records a particular shear, its one-dimensional kernel, and all eight translation-path values under that particular comparison. Adding each of the three kernel multiples gives the other possible tables.

Every actual Kummer comparison must occur in this set of three. The code does not select one as canonical. All three must be carried into the affine equations for (eta), or one additional division/path normalization must be computed. During development an apparent inconsistency was traced to prematurely replacing an integral (-1) by its residue (2) in a boundary-permutation column mapping to (O), before dividing ((UM-PU)) by three. The corrected code retains literal integral (-1) there and all checks pass.

The numerical translation computation was then used in the next affine test. **Subsequent resolution:** B.36 and the separate audit work/c_audit_B36_exact_two.md now prove the actual order \(m_2=3\), with an independent exhaustive verifier of all 59,049 initial candidates. B.37 and work/c_global_torsion_exclusion.md then prove arithmetic Ross nonvanishing using the primitive rank-320 quotient and a five-entry modulo-nine functional. The earlier paragraphs record the state and proof of B.35 itself.
