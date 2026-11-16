# Independent audit of B.36: the actual local order at two

**Auditor:** Part C agent. **Date:** 2026-11-16. **Verdict:** the revised B.36 proof passes. It proves that the actual integral determinant-extension class has order \(27\), hence \(m_2=3\), in the stated \(C_0\) tangent. This is an arithmetic class conclusion, not merely a calculation of its ambient coefficient group.

The audit covers `deliverable/sections/B_local_two_exact.tex`, the framed-point program `c_char2_translation_paths.py`, the affine system `b_char2_translation_affine.py`, the independently written exhaustive verifier `c_char2_translation_verify.py`, and their saved matrices and outputs. B-owned files were not edited. Two wording repairs were sent to B and incorporated: the direction of the restriction/corestriction composite, and an explicit coherent-division proof of the compact Kummer minus sign.

## 1. Actual tangential paths and the framed Picard group

Let \(k=\mathbf F_4\), \(E:y^2+y=x^3\), and \(D=E(k)=E[3]\). The origin is \(O=C_0\), with the prescribed parameter \(s_O=Z/X\). The generalized Jacobian \(J=J_{E,D}\) is represented by degree-zero line bundles furnished with a **nonzero frame element** in each fibre over \(D\), with simultaneous scalar change identified. This frame-element convention matters: for a principal divisor \(D_f=\operatorname{div}(f)\), multiplication by \(f\) sends the local generator \(s^{-\operatorname{ord}(f)}\) of \(\mathcal O(D_f)\) to the leading coefficient of \(f\). The torus correction therefore has a positive leading-value sign.

For \(d\ne O\), define \(z_d\) by \(\mathcal O(d-O)\), with frames \(s_d^{-1}\) at \(d\), \(s_O\) at \(O\), and one elsewhere. These are genuine nonzero fibre elements: a local generator of an invertible sheaf remains a nonzero element after reducing that sheaf modulo the point, even when its expression as a meromorphic function has a pole or zero.

Here is a direct construction of the tangential comparison. Put \(R=k[[\varepsilon]]\), and choose the two formal points

\[
s_d(P(\varepsilon))=a\varepsilon,
\qquad s_O(Q(\varepsilon))=\varepsilon,
\qquad a\in k^\times.
\]

They lie off \(D\) over \(k((\varepsilon))\). The ordinary Abel divisor \(P(\varepsilon)-Q(\varepsilon)\) has canonical frame one at every point of \(D\). At \(d\), the local generator of its line bundle is \((s_d-a\varepsilon)^{-1}\), so its frame is \(-a\varepsilon\) times this generator. At \(O\), the local generator is \(s_O-\varepsilon\), so the frame is \((-\varepsilon)^{-1}\) times this generator. Divide the torus factors \(\varepsilon\) at \(d\) and \(\varepsilon^{-1}\) at \(O\). The modified framed line bundle extends across \(\varepsilon=0\), where its frames are

\[
a s_d^{-1}\quad\hbox{at }d,
\qquad s_O\quad\hbox{at }O,
\qquad 1\quad\hbox{elsewhere}.
\]

Here the minus signs disappear because the residue characteristic is two. Thus its special point is exactly \(z_d+\epsilon_d(\log_\zeta a)\).

To see that this is the **arithmetic tangential Kummer class**, rather than just a formal limit of point-group representatives, take the prime-to-two Puiseux fibre with coefficientwise Frobenius and compatible roots \(\varepsilon^{1/3^n}\) fixed by Frobenius. The divided torus factors have compatible Frobenius-fixed divisions, so contribute zero arithmetic Kummer cocycle. The formal principal units and the kernel of reduction \(J(R)\to J(k)\) are uniquely three-divisible: multiplication by three is étale on the smooth semiabelian model, and a prescribed lift in the formal neighbourhood is unique by Hensel lifting. Consequently the Kummer torsors of the remaining framed point identify with those of its special point. This proves, with its sign,

\[
\alpha_{d,a}=\kappa(z_d)+\kappa(a)e_d.
\]

This construction applies equally to any higher-order choice of the approaching arcs, since changing those terms lies in the same uniquely three-divisible formal kernel. For an automorphism fixing \(O\), the two local generators combine to a tangent ratio at \(O\), and give \(\kappa(a)e_O\). In particular the CM tangent multiplier \(\zeta\) gives \(+\kappa(\zeta)e_O\), agreeing with B.35.

For translation by \(d\), the invariant differential (dx) is preserved. The original unit tangent has (dx)-coordinate one, so its image has \(s_d\)-coordinate \(k_d=(ds_d/dx)(d)\). Thus the path used by the translation identity is exactly

\[
\kappa\bigl(z_d+\epsilon_d(\log_\zeta k_d)\bigr).
\]

No translation path has been set to zero, and no function has been evaluated at its pole.

## 2. The Abel map and the precise comparison with homology

For an ordinary geometric base point \(b\in E\setminus D\), the Abel map \(j_b(P)=\mathcal O(P-b)\), with its canonical modulus frames, induces the map from geometric abelianized pro-three fundamental groups to \(T_3J\). Its compact map is the ordinary genus-one Abel map and acts as the identity on \(T_3E\). The same local frame computation as above shows that a positive peripheral generator goes to the positive torus cocharacter. Compare the exact sequences

\[
0\longrightarrow \mathbf Z_3(1)[D]/\mathbf Z_3(1)\sum_{d\in D}e_d
\longrightarrow V\longrightarrow T_3E\longrightarrow0
\]

and

\[
0\longrightarrow T_3\bigl((\mathbf G_m)^D/\mathbf G_m\bigr)
\longrightarrow T_3J\longrightarrow T_3E\longrightarrow0.
\]

The two outer maps are the stated integral identities, so the middle map is an integral isomorphism. The first sequence is the punctured-curve homology sequence already used in B.24; the second follows from the semiabelian extension and divisibility over the algebraic closure. The ordinary Abel–Kummer comparison is also stated explicitly in the primary literature: Saïdi (2021), Section 1, immediately after the sequences marked (*) and (**), identifies the full Tate module of the generalized Jacobian with the geometric abelianization and matches its toric subgroup. That source is in characteristic zero; the good prime-to-two specialization used here is the separately verified SGA1, Exposé XIII, §§2.9–2.12. The displayed local construction proves the additional tangential normalization, rather than attributing it to an unspecified general comparison theorem.

## 3. The path-commutator sign

Fix the convention that a path \(p:b\to gb\) produces the based automorphism \(T(n)=p^{-1}g(n)p\). Because \(g\) is defined over \(k\), direct groupoid composition gives

\[
T\rho(h)T^{-1}=\operatorname{Int}(p^{-1}h(p))\rho(h).
\]

The abelian class of \(p^{-1}h(p)\) is the positive Kummer class just constructed; on multiplication torsors it is the familiar difference \(h(Q_n)-Q_n\). If \(T\omega=\omega+t\) and \(\rho(h)\omega=\chi(h)(\omega+\eta(h))\), then in \(\gamma_2N/\gamma_4N\)

\[
(T-1)\eta(h)=[p^{-1}h(p),w]+(\chi(h)^{-1}\rho_A(h)-1)t.
\]

Thus

\[
(g-1)[\eta]=\operatorname{ad}_{w*}(\alpha_g).
\]

The correction \(t\) is a coboundary in (A(-1)). This checks the sign in B.36.2 independently of its geometric point-group calculation. It also shows why the chosen based lift need not have the same finite order as the unbased curve automorphism.

## 4. Finite framed group, automorphisms, and the three comparisons

The Miller functions in `c_char2_translation_paths.py` have divisor (P+Q-(P+Q)-O), where the third term denotes the point obtained by elliptic addition. Multiplication by each function gives the frame-element correction with the positive leading-value sign from §1. The derivative factors \(k_d\) are computed from the specified original plane parameters, including the \(C_1,C_2\) factors. All 729 cocycle identities, 81 commutativity identities, 891 generator/point-pair automorphism identities, and 81 Frobenius-two identities pass. The finite group has order \(3^{10}\), type \(C_9^2\oplus C_3^6\), with \(3z_P=2U\operatorname{coord}(P)\).

The full point-group action of an automorphism must transform the frames as well as the cusp labels. The factors in B.36.8 follow from the pushed parameter \(s_P\circ g^{-1}\), whose derivative relative to \(s_{gP}\) is \(k_P/(c_gk_{gP})\). In particular the numerator at (gP) is \(c_gk_{gP}/k_P\), while the frame at (gO) contributes its inverse \(1/(c_gk_{gO})\). These are exactly the factors used by the code.

For the compact Kummer sign, a coherent Tate sequence \(t_{i,r}\) with first term \(P_i\) gives the division \(Q_r=t_{i,r+1}\). Actual Frobenius four is ([-2]), so

\[
F_4Q_r-Q_r=-3Q_r=-t_{i,r}.
\]

Therefore \(\kappa(P_i)\) has compact representative \(-f_i\). The torus sign is positive: coherent roots of \(\zeta\) have Frobenius difference exponent \((4-1)/3=1\). The strict quaternion conjugacy is identity modulo three, so it does not alter this residual compact basis.

Matching the compact and toric maps leaves precisely sixteen three-element shear coordinates. The actual automorphism and Frobenius-two equations have rank fifteen and are consistent; all three resulting comparisons are retained. The kernel vector equals the concatenated columns of \(-U\bmod3\). This provides a useful independent conceptual check: the possible difference maps lie in

\[
\operatorname{Hom}_{E[3]\rtimes\mathrm{SL}_2(\mathbf F_3)}
      (E[3],W[3]).
\]

For the regular translation module modulo constants, its translation invariants are precisely affine-linear functions modulo constants, a copy of \(E[3]^\vee\). The Weil pairing identifies this with the standard \(\mathrm{SL}_2\)-module, whose equivariant endomorphisms are the scalars \(\mathbf F_3\). Thus a one-dimensional ambiguity is expected; the exact equations verify it, including Frobenius two. No one of the three is chosen without proof.

## 5. Integral translation matrices and actual descent

On compact homology translation is the identity. On the boundary it is the literal nine-cusp permutation after quotienting the diagonal. Consequently a column mapping a finite cusp to \(O\) has all entries (-1). Commutation with the actual Frobenius-four matrix forces the cross block to be ((U-PU)/3). These are integral matrices, and they fix both columns of \(\binom{3I}{U}\), hence fix the actual primitive vector \(w\) exactly.

The local calculation includes actual Frobenius-two descent. On the rank-41 quaternion-invariant lattice, its map to the Frobenius-four cokernel is \(E(1+R_2)Q_2^{-1,+}\). The quaternion projector commutes with Frobenius two because that Frobenius normalizes the quaternion group. Restriction is injective and preserves orders because **corestriction composed with restriction** is multiplication by two on the base-field cohomology. In general the reverse composite is \(1+F_2\), not scalar two on every extension-field class; B's proof now states the correct direction.

The translation equations are imposed in the full rank-330 Frobenius-four cokernel. A translation need not preserve the rank-41 invariant lattice; using the full target is essential and is done correctly.

## 6. A second, independent exhaustive solver

`c_char2_translation_verify.py` does not reuse B's sequential affine-lattice solver. It reads the certified 594-by-13 scalar congruence matrix, the three target vectors, the row moduli, and the domain moduli. It first verifies that every domain relation annihilates every row. Then it divides each sigma congruence by its exact common power of three and constructs every solution digit by digit over \(\mathbf F_3\).

At each digit stage, independent Gaussian elimination selects the pivot coordinates and enumerates **all** free digits; the remaining rows reject any incompatible partial solution. Thus induction proves that no solution is omitted and no false partial solution is retained. The exact stage counts are:

| Digit | Active variables | Constraint rank | Free digits | Partial solutions |
|---|---:|---:|---:|---:|
| 1 | 13 | 8 | 5 | 243 |
| 2 | 8 | 6 | 2 | 2,187 |
| 3 | 6 | 4 | 2 | 19,683 |
| 4 | 2 | 1 | 1 | 59,049 |

The verifier checks every resulting vector against all original sigma rows, then exhaustively tests every vector against both translation blocks for each of the three comparison maps. Each comparison leaves exactly nine elements. Every element has exact order 27 in

\[
C_2=(\mathbf Z/3)^5\oplus(\mathbf Z/9)^2
       \oplus(\mathbf Z/27)^4\oplus(\mathbf Z/81)^2.
\]

All 27 vectors agree exactly with B's independently computed affine-lattice output. The complete 59,049-candidate set is saved in `c_char2_translation_verified_solutions.npz`; the surviving vectors and their orders are in `c_char2_translation_verify.json`. Thus the solver cross-check is exhaustive, not a sample or a re-evaluation of only B's proposed answers.

B's concise certificate gives the same union as \(b+s h_3+t h_9\), with \(s\bmod3\), \(t\bmod9\), and comparison \(t\bmod3\). Every candidate is annihilated by 27 and has its twelfth coordinate congruent to 3 modulo 9 in \(\mathbf Z/81\). This proves its exact order is 27 without having to choose the actual class among the candidates.

## 7. Scope and dependencies of the conclusion

The actual class satisfies the affine system for one of the three exhaustive comparisons. Every such solution has order 27. Averaging and unramified quadratic restriction preserve the order of that actual class, so B.36 proves \(m_2=3\). The claimed global lift criterion \(27\mid a\) then uses the previously proved B.31 local-order/decay theorem; the current audit does not substitute a finite or purely module-level assertion for that theorem. The arbitrary unramified summand is included through B.31's zero-obstruction assertion.

The conclusion concerns the intrinsic class-three obstruction of the actual zero-abelian class-two section. It neither identifies an arithmetic Ross generator nor proves lifting through all higher nilpotent classes. No such stronger conclusion appears in the revised B.36.

## 8. Source verification

- Saïdi, M. (2021). Arithmetic of p-adic curves and sections of geometrically abelian fundamental groups. *Mathematische Zeitschrift, 297*, 1191–1203. https://doi.org/10.1007/s00209-020-02553-1. **Opened:** publisher full article, https://link.springer.com/article/10.1007/s00209-020-02553-1, Section 1 after (*) and (**). The full Tate-module/geometric-abelianization identification and boundary exact sequence were read. Its field assumption is characteristic zero; it is not misrepresented as the characteristic-two tangential calculation.
- Grothendieck, A. (Ed.). (2003). *Revêtements étales et groupe fondamental (SGA 1)*. Documents Mathématiques 3, Société Mathématique de France. **Already independently verified by B/root:** original source of Exposé XIII, §§2.9–2.12, including proof of the prime-to-residue-characteristic specialization isomorphism. Local source `work/b_sga1_source/smf_doc-math_3_01.tex` and bibliography key `BSGA1`.
- Wickelgren's author-hosted chapter, https://services.math.duke.edu/~kgw/papers/3NilP1.pdf, was also opened. Its opening paragraphs identify the generalized Abel map with geometric abelianization, and §12.2.2 discusses the tripod's tangential Abel map. It was used as corroboration only; the present modulus-frame normalization is proved directly above and is not attributed to that tripod-specific example.

All decisive new geometric constructions, path signs, finite-group operations, and affine solution calculations are proved or computed in the present work. Previous unrefereed outputs supply no authority for B.36.
