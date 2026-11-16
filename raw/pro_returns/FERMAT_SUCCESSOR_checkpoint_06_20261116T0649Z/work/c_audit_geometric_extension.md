# Audit: the actual geometric extension separates the three B.38 phases

## Conclusion and precise scope

The proposed new condition is valid and genuinely stronger than the cohomological commutation identities imposed in B.38. After dividing out inner-path terms, the actual geometric automorphism group acts on an actual integral extension module. Fixing its extension class excludes both nonzero members of B.38's remaining cyclic homogeneous ambiguity.

This proves uniqueness of the integral arithmetic refinement **relative to the fixed actual geometric extension** and the previously fixed data. It does not, by itself, calculate that geometric extension, assign a numerical Frobenius value to the selected phase, or construct a second geometric arithmetic action. The independent finite calculation described below agrees with B's calculation using a different algorithm and exact integers throughout.

## 1. There is a genuine joint module

Let (L_w\) be the pullback of \(\gamma_2N/\gamma_4N\to\Lambda^2V\) along the determinant line \(\mathbf Z_3w\). Its kernel is (A=\operatorname{Lie}_3V). A geometric inner automorphism by an element of abelian image (t\) acts trivially on (A\), and sends a lift of (w\) to that lift plus \([t,w]\). Consequently it acts trivially on

\[
\overline L_w=L_w/\operatorname{ad}_wV.
\]

Put \(Q=A(-1)/\operatorname{ad}_wV\). Thus the actual outer actions of the global geometric automorphism group \(\mathcal A\), of order 54, and of the arithmetic group \(\Gamma\) give a genuine action on the exact sequence

\[
0\longrightarrow Q\longrightarrow\overline L_w(-1)
\longrightarrow\mathbf Z_3\longrightarrow0.
\tag{1}
\]

Over (K=\mathbf Q(\zeta_3)\), all the geometric automorphisms are defined and commute with arithmetic. Over \(\mathbf Q\), complex conjugation permutes them, giving the corresponding semidirect-product action. Base-point paths introduce precisely the geometric inner actions already killed above; there is no remaining projective-action or compatible-path assumption.

In particular (1) has an actual geometric class

\[
t_{\mathcal A}\in H^1(\mathcal A,Q).
\]

It is additional data. Knowing only the resulting invariance of the arithmetic cohomology class under \(\mathcal A\), or the path commutation identities before taking (Q\), does not determine (t_{\mathcal A}\).

## 2. Which homogeneous arithmetic differences preserve this class?

Suppose two joint extension classes have the same geometric restriction. Their difference belongs to the kernel of restriction to \(H^1(\mathcal A,Q)\). The inflation–restriction sequence for \(\mathcal A\triangleleft\mathcal A\rtimes\Gamma\) says that it comes from

\[
H^1(\Gamma,Q^{\mathcal A}).
\tag{2}
\]

The rational averaging projector \(|\mathcal A|^{-1}\sum_{a\in\mathcal A}a\) commutes with arithmetic, because arithmetic permutes \(\mathcal A\). Therefore the inclusion in (2) is rationally a direct summand of (H^1(\Gamma,Q)\). If the arithmetic difference is torsion, its antecedent in (2) is torsion as well. Good-Frobenius weights imply \((Q\otimes\mathbf Q_3)^\Gamma=0\), and similarly for the invariant submodule.

It follows from the coefficient connecting sequences that a torsion difference represented by an invariant rational coset (y\in Q\otimes\mathbf Q_3/Q\) can preserve the actual geometric class if and only if

\[
y\in Q+(Q\otimes\mathbf Q_3)^{\mathcal A}.
\tag{3}
\]

Equivalently, its geometric connecting class \(\delta_{\mathcal A}(y)\) must vanish in (H^1(\mathcal A,Q)\). This is a connecting class attached to the common rational coset, not an unsupported restriction map from arithmetic cohomology to geometric cohomology. The coset is jointly invariant, so it also defines a cocycle on the joint group; its two restrictions are the arithmetic torsion difference and this geometric connecting class.

For (y=z/3\), condition (3) is exactly

\[
z\bmod3\ \in\operatorname{im}\bigl(Q^{\mathcal A}\to Q/3Q\bigr).
\tag{4}
\]

Indeed, if (z/3=q+r\) with (q\in Q\) and (r\) rationally invariant, then (z-3q=3r\) is an integral invariant with the same reduction as (z\). The converse follows by division by three. No rational-to-integral averaging assumption is hidden in (4).

## 3. Independent exact invariant-lattice calculation

The independent script `work/c_geometric_extension_test.py` constructs the 54 geometric degree-one matrices from the four generators already used in the C implementation, transfers them by the exact unimodular adapted basis, and calculates the ordinary degree-three Hall action over the integers. It deletes exactly the ten Hall columns spanning \(\operatorname{ad}_wV\), obtaining the actual rank-320 quotient action.

Let

\[
S=\sum_{a\in\mathcal A}a\in\operatorname{Mat}_{320}(\mathbf Z).
\]

The exact character formula \(\operatorname{tr}(\operatorname{Lie}_3g)=((\operatorname{tr}g)^3-\operatorname{tr}(g^3))/3\), followed by subtraction of the ten-dimensional inner image, gives

\[
\operatorname{rank}_{\mathbf Q}S=4.
\]

The program checks (S^2=54S\) and (aS=S\) for all 54 exact matrices. Its largest absolute entry is 135, so all the integer products lie far below the 64-bit range. More concretely, zero-based rows

\[
(46,51,80,81)
\]

and columns

\[
(4,13,40,66)
\]

give the minor

\[
\begin{pmatrix}
-1&2&0&0\\
-6&6&0&1\\
-2&2&0&0\\
-1&-2&1&1
\end{pmatrix},
\qquad\det=2.
\tag{5}
\]

Thus four integral columns of (S\) already span a primitive rank-four \(\mathbf Z_3\)-sublattice. They span the full rational invariant space, so they are the entire invariant lattice (Q^{\mathcal A}\). No finite-precision kernel saturation or unverified high-valuation pivot is required.

There is a particularly short separating functional. On the quotient coordinates, let

\[
\ell=2e_{51}^*+2e_{80}^*+2e_{81}^*+e_{82}^*
\quad\text{over }\mathbf F_3.
\tag{6}
\]

The exact certificate is

\[
\ell S=0\pmod3,
\qquad
\ell z=1\pmod3.
\tag{7}
\]

The adapted Hall labels at these four quotient positions are respectively

\[
(4,0,5),\quad(5,0,0),\quad(5,0,1),\quad(5,0,2),
\]

where the adapted degree-one basis starts with (u,v\), and \((i,j,k)\) denotes \([[e_i,e_j],e_k]\). The orientation is the negative affine-line cube sum used for B.38's local value 54. Reversing the generator changes the last value in (7) to two and leaves the exclusion unchanged.

Equations (5)–(7) prove that the residual numerator is outside the reduction of (Q^{\mathcal A}\). Hence

\[
\delta_{\mathcal A}(z/3)\ne0\in H^1(\mathcal A,Q).
\]

It has order three, since (3(z/3)\) is integral. Its two nonzero multiples are distinct. Therefore all three B.38 phases have distinct geometric extension classes.

The independent B implementation obtains the same conclusion by transposed Smith reduction of the invariant equations, with nonzero valuations (0^{313},1^2,3^1\), followed by its mod-three membership test. The exact average and primitive minor above provide an independent algorithm and a much smaller human-readable certificate of the required exclusion.

## 4. Remaining work

**Resolved subsequently:** the actual CM/translation module calculation, with chronological words converted to fibre composition, selects exactly candidate \(b+6h_9\). See `work/c_audit_B40_actual_phase.md` for the complete independent marking, sign, comparison, and arithmetic audit. The former next step is retained below to identify the boundary of this invariant-lattice computation itself.

The actual geometric class can be computed topologically from the index-nine étale covering \([3]:E-E[3]\to E-O\). The current B calculation has matched the integral Schreier abelianization and both translation matrices. Translations alone do not distinguish the residual class: B's separate calculation finds zero geometric connecting class after restriction to (E[3]\). The order-three CM action is consequently essential to the current route. That actual CM extension calculation must still be matched with the fixed quotient and normalizations before a numerical arithmetic phase is announced.

Files:

- `work/c_geometric_extension_test.py`
- `work/c_geometric_extension_test.out`
- `work/c_geometric_extension_test.json`
- `work/c_geometric_extension_test_matrices.npz`
- complementary actual finite arithmetic detector: `work/c_residual_class_two_detector.md`

This audit uses no new unverified external theorem: the joint-action descent is checked directly, the group-cohomology exact sequence is standard and its needed criterion is also proved explicitly, and the invariant-lattice calculation is exact.
