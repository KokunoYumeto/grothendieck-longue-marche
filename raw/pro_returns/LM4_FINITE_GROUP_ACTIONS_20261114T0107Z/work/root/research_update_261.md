## Continuation: the actual skeleton section, cocompact operators, and all-field marginal cocycles

This continuation adds C.89, C.90 and F.24. The registers now contain 261 claims: 230 Proved, 3 Known, 25 Refuted and 3 Open. The return remains **INCOMPLETE**, governed by the same 39-obligation table. The three new results retain the original maps and their topologies. They do not change the unresolved status of the general C.12, D.12 or F.7 assertions.

### C.89: a global section on the actual compact lifted skeleton

Retain C.81's original closed disk, its original discrete free proper operator group, and its transitive boundary-fixed commuting subgroup. C.82 supplies an actual quotient triangulation whose lifted closed stars, and hence lifted triangles, form a null family in the original disk. The closure of its full one-skeleton is exactly that skeleton together with the original circle. It is a compact connected space \(X\).

The new result characterizes the exact image \(\mathscr B\) of restriction of the original centralizer to \(X\). Its intrinsic data are an embedding fixing the original circle, commuting with every actual operator on the skeleton, carrying each triangle boundary with its positive orientation, and leaving the interior of the bounded target Jordan disk disjoint from the entire embedded skeleton. These conditions force distinct target face interiors to be disjoint. An intersection would put one boundary in the other Jordan curve; injectivity of the embedding then identifies the original triangles.

For each chosen representative triangle, three labelled vertices normalize its source and target Riemann maps. The boundary comparison
\[
\eta_b=f_b^{-1}\,\iota b\iota^{-1}\,f
\]
is an exact circle homeomorphism fixing the three standard vertices. Its radial extension gives the full face map
\[
F_b=\iota^{-1} f_b\widehat\eta_b f^{-1}\iota,
\]
with its displayed inverse. It agrees with the prescribed embedding on the entire boundary. Every other triangle receives the literal transported map \(qF_bq^{-1}\). Triviality of triangle stabilizers, proved from the original covering, makes this prescription unique. Commutation on common edges pastes the maps, and both occurrences of \(q\) retain orientation even for orientation-reversing operators.

The bounded Jordan disk is contained in the convex hull of its boundary and has exactly the same Euclidean diameter. Nullity of the source triangles and uniform continuity of the embedding therefore prove continuity of the pasted map at every point of the original circle. Disjoint face interiors give injectivity; invariance of domain and compactness give surjectivity. Conversely every original centralizer map satisfies the intrinsic face conditions. This proves equality with the actual restriction image.

The section is continuous for the full original map-and-inverse topology. The verified Radó theorem gives closed-disk convergence of normalized Jordan maps on each fixed face. The additional three-boundary-point normalization is proved using convergent boundary preimages and the unique Möbius map of the three cyclic points. For all remaining faces at once, equicontinuity of a convergent family of skeleton embeddings and C.82 nullity bound both image diameters. The exact comparison through a common source boundary point is
\[
d_E(\mathfrak s(b_n)x,\mathfrak s(b)x)
\leq\operatorname{diam}b_n(\partial\Delta)
+\sup_Xd_E(b_n,b)+\operatorname{diam}b(\partial\Delta).
\]
Uniform convergence of inverse maps follows from the fixed inverse modulus on the compact disk. The chosen disk coordinate and its inverse have explicit metric moduli, so this is continuity in the original topology.

Restriction and the section give the inverse maps
\[
(b,k)\longmapsto\mathfrak s(b)k,
\qquad
h\longmapsto\bigl(h|X,\mathfrak s(h|X)^{-1}h\bigr)
\]
between \(\mathscr B\times\mathscr S_{Q,\Lambda}\) and the original centralizer. C.82's identity-fixed contraction of the second factor gives an actual strong deformation retraction onto the section image. The complete deformation of \(\mathscr B\) remains to be constructed. Root and an independent reviewer read the full proof and checked the original topology, all operator labels, both product maps, and the infinite-face estimate.

### C.90: every positive sphere fills for a compact actual quotient

For compact \(N=O/Q\), the proof now gives
\[
\pi_n(\mathscr C_Q,1)=0\qquad(n\geq1)
\]
in the original disk topology, with every original operator retained. The quotient may be nonorientable; the torus and Klein bottle are included. No boundary extension of an operator or an interior conjugacy is used.

C.81's exact evaluation bundle over the contractible original open disk identifies every positive homotopy group with that of the stabilizer of one actual point \(x\). A based sphere in this stabilizer descends continuously, for maps and inverses, to the identity component of \(\operatorname{Homeo}(N\operatorname{rel}\{p\})\), where \(p=\pi(x)\). Only the given based sphere is placed in this component; the argument does not identify the descents of arbitrary other components.

Yagasaki's original Lemma 2.1(i), printed page 2 with proof on page 3, contracts this exact pointed compact-surface group [C_Yagasaki2000]. All exceptions are checked. The quotient is closed and has contractible universal cover, so the sphere and projective plane are excluded. The torus and Klein-bottle exceptions listed by the source have empty fixed set. Here the fixed set contains the specified point. The boundary cases cannot occur. The applicable item is **(i)**; the boundary-fixed item **(ii)** used in earlier results is not substituted for it.

The normalized contraction \(J_r(b)=C_{1-r}(b)C_{1-r}(1)^{-1}\) starts at the identity, ends at \(b\), and fixes the group identity throughout. Lifting \(J_r(b_\xi)\pi\) from the identity through the original covering gives the family of interior homeomorphisms. Lifting the inverse family gives its exact inverse. Covering-homotopy uniqueness proves commutation with each individual deck operator, fixation of \(x\), the sphere basepoint condition, and literal agreement with the original sphere at the final endpoint.

C.88 supplies the missing original-boundary comparison: its compact-parameter tail condition is satisfied with the compact set \(K=N\). The identity extensions therefore give a continuous family of original disk maps and inverses. Concatenating with the based homotopy supplied by the evaluation bundle fills the original sphere. Root and a second independent reviewer checked the full proof, including the exact Yagasaki exception list and both original-source pages. The remaining noncompact quotient requires its own uniform tail control.

### F.24: exact rank-one restriction over every finite field

The actual negative marginal coordinates are
\[
V_-=\widehat F(X_1,\ldots,X_7),\qquad
R_-=\ker(V_-\to\widehat F(X_1,X_2,X_3)).
\]
For a finite field \(k\) and a continuous character \(\chi:V_-\to k^\times\) nontrivial on \(R_-\), restriction to the actual source subgroup \(\mathcal K_-\) is injective both on continuous crossed homomorphisms and on first continuous cohomology. The positive assertion follows by pullback through the explicit F.23.13 isomorphism and its inverse, which carry both \(R_-\) and \(\mathcal K_-\) to their specified positive counterparts.

The coefficient calculation takes place in
\[
\Lambda=\mathbb Z[t_1^{\pm1},\ldots,t_7^{\pm1}].
\]
On the dense discrete free group, the universal character sends \(X_i\) to \(t_i\), and the universal crossed homomorphism sends it to the row vector \(e_i\). Evaluation \(t_i\mapsto\chi(X_i)\) sends its row for a word \(w\) to the exact coefficient row computing \(d(w)\) from the seven values \(d(X_i)\).

The eight negative collision rows and eleven old-source action matrices are produced from the literal F.23 braid records by multiplication in the universal affine group
\[
(a,v)(b,w)=(a+b,v+t^a w),\qquad
(a,v)^{-1}=(-a,-t^{-a}v).
\]
The same decorated Artin words, erased eighth generator, conjugator \(u=c_8^{-1}\), and actual action \(u x_j u^{-1}\) are retained. Source normality places every collision seed and every selected source-conjugate seed in \(\mathcal K_-\). Purity of the old source braids fixes the universal character and proves the exact row chain rule.

The certificate uses 64 rows: the eight seeds and eight rows for each source index in \((2,9,8,10,1,0,7)\). It proves rank seven over each of the following rings or specialized strata:

| Chart | Exact coefficient condition | Recorded row operations | Final rank |
|---|---|---:|---:|
| 4 | Invert \(t_4-1\) | 389 | 7 |
| 5 | Invert \(t_5-1\) | 444 | 7 |
| 6 | Invert \(t_6-1\) | 445 | 7 |
| 7 | Set \(t_4=t_5=t_6=1\), invert \(t_7-1\) | 196 | 7 |

Every division by a character difference is checked by multiplication back, and every pivot is a signed Laurent monomial times a power of that chart's inverted difference. No integer other than \(1\) or \(-1\) is inverted. The first chart's final two one-column rows satisfy the explicit identity
\[
r_5=(1-t_6)e_2,\qquad
r_{48}=\bigl(t_1t_2t_3t_4t_5t_7(t_6-1)-1\bigr)e_2,
\]
\[
r_{48}+t_1t_2t_3t_4t_5t_7r_5=-e_2.
\]
These four charts exhaust every character nontrivial on the closed normal subgroup generated by \(X_4,\ldots,X_7\). The conclusion holds over every field, including characteristics 2 and 3; it is proved by the integer polynomial identities.

The independent verifier imports none of the three producers. It reconstructs all 19 literal word evaluations with generic affine multiplication, reconstructs all 64 rows, and replays the exact row operations, all divisibility identities, the triangular pivot orders, the displayed two-row identity, and the longer retained scalar-ideal certificate. It passes **13,982 exact assertions**. Root also executed it in an isolated directory; every mathematical output agrees with the original verification. The isolated output records its own paths, and the comparison checks their input hashes separately. All programs, inputs, outputs, manifests and stdout are retained.

A continuous crossed homomorphism vanishing on \(\mathcal K_-\) is killed by these 64 rows. Rank seven forces its generator values to zero, hence its values on the dense discrete subgroup to zero, and continuity gives zero on \(V_-\). A cohomology class whose restriction is principal is handled by subtracting the same principal crossed homomorphism on \(V_-\). This proves the stated maps on \(Z^1\) and \(H^1\), with their exact coefficient restrictions.

For every continuous scalar affine representation \(\rho:V_\pm\to\operatorname{Aff}_1(k)\), the two groups \(\rho(\mathcal K_\pm)\) and \(\rho(R_\pm)\) have exactly the same fixed-point set in \(k\). For a scalar character nontrivial on \(R_\pm\), that set also equals the fixed-point set of \(\rho(V_\pm)\). The proof applies the crossed-homomorphism assertion to \(g\mapsto\rho(g)z-z\). For a trivial scalar character on \(R_\pm\), F.21 normal generation through the actual maps \(D^+\to R_\pm\to\rho(R_\pm)\) proves equality of the translation images directly.

The marginal images themselves are equal for every representation satisfying the exact condition
\[
\rho(\mathcal K_\pm)\cap T_k=\{1\}.
\]
For \(M=\rho(\mathcal K_\pm)\), the scalar projection is then injective, so \(|M|\) divides \(|k|-1\). The explicit average \(|M|^{-1}\sum_{m\in M}m(0)\) is a fixed point. The proved fixed-point comparison places the whole image in its abelian scalar stabilizer, and the same actual normal-generation maps give the image equality. The outstanding affine class has nonzero intersection with translations. No ambient invariant quotient killing that intersection is assumed or constructed.

### Exact remaining scope and source record

C.12 still retains its full admissible-surface zero-level kernel, the noncompact discrete-operator tail, the deformation of the entire compact skeleton image, arbitrary-frontier lifting and nonfixed-frontier pasting. C.89 and C.90 remove the exact global-section and cocompact subproblems proved above. D.12 retains its literal full peripheral equations, scalar cubic decision, and D.78's actual pro-odd fixed-group kernel. F.7 retains full marginal equality, the interaction source image, and the original residual membership equation.

No new bibliography entry is introduced by this continuation. The exact Radó and Yagasaki source uses are checked against the already retained original PDFs. The F.24 calculation derives its rows from the already audited actual F.23 source and supplies the complete new polynomial certificate. The proof audits and original-code hashes are retained. The next build and actual page-review records govern the final current PDF; earlier checkpoint counts and scope sentences remain historical records.
