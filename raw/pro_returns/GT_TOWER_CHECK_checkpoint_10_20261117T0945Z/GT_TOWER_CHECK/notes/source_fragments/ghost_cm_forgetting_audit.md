# Independent audit of the finite CM descent/forgetting discrepancy

The root's matrix program was copied with only its input-root path made explicit and freshly executed as `work/ghost_code/review_finite_cm_forgetting_discrepancy.py`. Its actual `.out`, `.json`, and `.npz` are saved separately. All assertions passed. The source program and each original input hash are retained in that record.

## Matrix and exact quotient map

The input reflection \(R\) is the actual \(H\)-linear Hermitian reflection from A.4.20 on \(M_{18}\). The program verifies \(R^2=I\), \(R^tFR=F\), and commutation with both named generators of \(H=C_3^2\). Thus
\[
P=(I-R)/2=2(I-R)
\]
is an \(F\)-self-adjoint, \(H\)-linear idempotent. The checked rank is nine. Its image and kernel are perpendicular nondegenerate subspaces, and \(H\) preserves both.

The actual element
\[
k=h_1P+h_1^{-1}(I-P)
\]
acts as \(h_1\) on the first summand and \(h_1^{-1}\) on the second. Hence it preserves \(F\), commutes with every element of \(H\), and has order dividing three. The explicit matrix is not the identity, so its order is exactly three. Both determinant and spinor are homomorphisms to groups of order two, and therefore both have value one on \(k\). The exact map to the orthogonal group consequently places \(k\) in \(\Omega^-_{18}(3)\).

The program does not infer the quotient from dimensions. It uses the retained surjective matrix
\[
\phi:M_{18}\longrightarrow M_{18}/\mathfrak m_H^2M_{18}
\]
of A.4.18/A.4.21, constructs a right inverse, and checks
\(k_6\phi=\phi k\). The same check is made for both deck generators. It then enumerates all nine actual deck matrices and both scalar signs. The induced \(k_6\) differs from every one of these eighteen matrices.

In the retained free \(\mathbf F_3[X,Y]/(X,Y)^2\)-basis its first-order coefficients are exactly
\[
D=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad E=0.
\]
The full eighteen-element inner ambiguity on the compact faithful module is precisely the one already proved in A.4.22. Thus this calculation proves a nontrivial outer class in \(\operatorname{Out}(\mathcal P_c)\); it does not merely prove that a chosen matrix representative is nonidentity.

## Actual source word with all solvable comparison coordinates killed

Use the actual pure quaternion-kernel domain of A.4.23, and join its finite representation on \(M_{18}\) to the actual lower \(Q_L\), signed-period, and nine ordinary forgetting maps. The joint lower target is solvable: this follows from the actual finite lower image and the computed solvability of \(J_c\), and is preserved by finite direct products and subgroups.

The orthogonal projection of this actual domain contains the perfect group \(\Omega^-_{18}(3)\) and lies in \(\mathrm{SO}^-_{18}(3)\). Its first and every further derived image is therefore \(\Omega^-_{18}(3)\). Explicitly, a surjective homomorphism \(\pi:D\to\pi(D)\) satisfies
\(\pi(D^{(r)})=\pi(D)^{(r)}\), since each commutator in the target is the image of a commutator of chosen preimages. At a derived depth at least the derived length of the lower joint image, the lower coordinates are all one while the orthogonal image is still the whole \(\Omega\). There is consequently an actual pure source word at that depth whose matrix is the displayed \(k\).

The exact split-extension reconstruction of A.4.19/A.4.25 turns its fixed base and commuting module maps into centralization of the named finite deck subgroup. The product outer-automorphism comparison retains the \(Q_L\) coordinate. The six-dimensional quotient class is non-inner by the preceding enumeration, so its intrinsic finite descent \(d\) is nonidentity. Every retained ordinary forgetting coordinate, including \(j_0\), is the identity by construction.

This proves the stated discrepancy at the named output and its joint solvable forgetting extension. It does not claim that the source word centralizes the deck subgroup in the full discrete mapping-class group, nor that it centralizes that subgroup at every stronger finite input. Those assertions are not needed for the counterexample to equality of these two specified finite maps.

Audit conclusion: the exact matrix certificate, inner-kernel comparison, and perfect-image source argument check. The final numbered A.4.42 source was not yet present when this independent note was written; its stated mathematical construction has been reviewed in full.
