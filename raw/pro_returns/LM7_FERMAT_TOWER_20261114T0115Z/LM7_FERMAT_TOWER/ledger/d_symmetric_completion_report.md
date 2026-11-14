# D41: all actual symmetric quotients

## Proved result

D41 extends D40 simultaneously through every actual epimorphism from the marked source \(B=C_2*C_3\) onto a full symmetric group \(S_n\), \(n\ge5\). One coordinate is indexed by each distinct marked kernel. The exact simultaneous image is the full fibre product over the common sign:

\[
\mathcal S=\{(g_M):\operatorname{sign}(g_M)\text{ is the same in every coordinate}\}.
\]

Its even subgroup is the full product \(\prod_M A_M\), and the actual image of \(s\) gives a section of the sign map. Thus the theorem specifies both maps in the semidirect-product description and the action of the section.

The source image jointly with D40's \(\mathcal U\) is exactly

\[
\mathcal W=\mathcal U\times_{C_2}\mathcal S
=\widehat B/(R_T\cap K_{\mathcal R}\cap K_{\mathcal S}).
\]

The normalized action is \((\alpha_{39},1_{\mathcal R},1_{\mathcal S})\), with actual simultaneous conjugators, one global profinite gauge, multiplier one and both hexagons. It extends the D40 action exactly and now includes identity on the explicitly marked \(S_{10}\) quotient.

## Exact source and quotient proofs

Every symmetric epimorphism has the same sign character: \(r\) is even because its order divides three, and \(s\) must be odd for surjectivity. Restricting to \(B_{\rm even}\) gives epimorphisms onto the alternating factors with exactly the original marked kernels. These kernels are distinct.

Inductive simple-group Goursat proves surjectivity onto every finite product of alternating factors. A nontrivial common quotient would identify one new kernel with an old one. Compactness then gives the full infinite product. Multiplication by the actual \(s\) tuple supplies the odd coset.

Repeated epimorphisms with the same kernel are compared by the induced coordinate automorphism. Deletion and reinsertion through that automorphism give explicit inverse marked maps. Their even images are diagonal simple blocks, whose normalizers inside the corresponding alternating products are the blocks themselves.

A proper normal subgroup of a finite simultaneous symmetric image lies in its even subgroup. An odd element in a normal subgroup would act nontrivially on every surviving alternating factor, forcing all those factors into the subgroup. Therefore every nonabelian finite quotient of the simultaneous image has a full symmetric quotient. The iterated-coordinate-kernel argument of D40 excludes every such symmetric quotient of \(\mathcal U\), so their exact common quotient is sign \(C_2\).

The exact projection kernels are

\[
\ker(\mathcal W\to\mathcal V)=\prod_{M\ne M_7}A_M,
\qquad
\ker(\mathcal W\to\mathcal T)=\mathcal R'\times\prod_M A_M.
\]

Here \(\mathcal V\) is D40's specified \(S_7\) extension, and \(\mathcal R'\) retains its closed-commutator definition.

## New remaining-kernel test

The program evaluates the actual source map

\[
s\mapsto\left[\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\right],
\qquad
r\mapsto\left[\begin{smallmatrix}1&-1\\1&0\end{smallmatrix}\right]
\]

to \(J=\operatorname{PGL}_2(\mathbb F_7)\). It generates all 336 elements. Its determinant-square subgroup \(L=\operatorname{PSL}_2(\mathbb F_7)\) has order 168. The even-source generators \(r,srs\) generate \(L\).

The certificate exhausts all six conjugacy classes in \(L\), of sizes \(1,21,42,56,24,24\). Every nonidentity class normally generates all of \(L\). The centralizer of \(L\) in \(J\) has order one. These direct checks give the simplicity and normal-subgroup inputs used in the proof.

The action on \(\mathbb P^1(\mathbb F_7)\) is faithful of degree eight and has image order 336. It is therefore not a surjection onto \(S_8\), whose order is 40320. This specific map is not one of the full symmetric coordinates.

An iterated-coordinate-kernel argument proves that \(\mathcal W\) has no quotient \(J\): the solvable-coordinate and symmetric-coordinate kernels have images containing \(L\), while the perfect-coordinate kernels have image \(J\). Their iterated commutator cannot simultaneously be trivial in the product and contain the perfect group \(L\).

Consequently

\[
\sigma(R_T\cap K_{\mathcal R}\cap K_{\mathcal S})=L.
\]

This is the exact remaining source-kernel map. It does not assert that the entire CM pair has no full profinite lift.

## Comparison of the two mod-seven markings

The canonical good-prime map uses the previously fixed matrices

\[
\rho_7(s)=\left[\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right],
\qquad
\rho_7(r)=\left[\begin{smallmatrix}0&-1\\1&-1\end{smallmatrix}\right].
\]

The program enumerates all 56,448 paired elements under \((\rho_7,\sigma)\), proving the full joint image \(L\times J\). On the actual even source it enumerates all 28,224 pairs, proving image \(L^2\). Thus the comparison is through explicit marked maps.

The new remaining kernel kills the canonical \(\rho_7\) coordinate, which belongs to the all-perfect construction, while it surjects under the displayed second map onto \(L\). The finite pair calculation and the full-kernel proof are stated separately.

## Program and status

The standalone standard-library program d_cm_symmetric_completion.py has actual output and JSON certificates. It runs in approximately 1.2 seconds. It enumerates both projective matrix groups, every required normal closure, the centralizer, the faithful permutation action, and both complete paired images. It has no external source-file dependency.

The exact infinite-source statements are proved in sections/D_symmetric_completion.tex. No new bibliography entry is needed. Parent and A full audits are pending. The D13/D19 full profinite realization questions remain open; the new quotient family is explicitly noncofinal, as witnessed by the remaining projective-linear source quotient.

## Subsequent exact lifting test

D.45 proves that the entire recorded normalized D39 action and all D40-D44 extensions retaining it have no genuine full profinite GT0 lift. The full retained loop homology forces multiplier1; all112 central and38 complete lower-centralizer columns are annihilated by a four-term degree9 functional that takes value1 on the actual sphere target. The elliptic projection has a literal corrected finite lift. The prescribed CM pair remains open for a replacement action.
