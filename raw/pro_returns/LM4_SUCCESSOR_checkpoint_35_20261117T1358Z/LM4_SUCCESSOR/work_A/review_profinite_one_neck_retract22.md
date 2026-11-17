# Independent review: the actual one-neck profinite amalgam and selected-cone centralizer

**Status: PASS, with the finite virtual cohomological TYPE hypothesis made explicit below.**

Reviewed in full after checkpoint21 release:

- `records/profinite_one_neck_retract_proposal21.md`;
- `work_CE/shared_five_generator_neck_21h.txt`;
- `work_CE/paired_regional_retractions_22h.txt`.

This review concerns the actual simply connected slit regions joined by the first regular neck. It does not add the other four necks, identify the remaining vertex centralizer, or decide either main problem. No canonical paper, register, or bibliography is changed.

## 1. Actual ordinary retractions

Write the actual one-neck orbifold group as

\[
G=R_1*_{K}R_2,\qquad K\cong F_5.
\]

Each vertex has its retained orientation character, with ordinary index-two subgroup \(H_i\). The actual filling of the four B components is a map on the ordinary group, not on the entire orbifold group. Restricted to \(H_i\), it maps into the one-family bundle over the simply connected slit region. That bundle has fiber group \(F_7\), and the inclusion of the chosen based fiber induces an isomorphism on fundamental groups: both the first and second homotopy groups of the slit base vanish.

The common neck disk contains the same four A punctures and one branch puncture in both vertices. Its already chosen based geometric meridians extend to a geometric free basis of \(F_7\): take also the other branch meridian and one retained meridian, and omit the remaining retained puncture in the sphere relation. Thus the literal disk subgroup is a free factor. The composite of ordinary filling, the based fiber identification, and the free-factor retraction is a homomorphism

\[
r_i:H_i\longrightarrow K,\qquad r_i|_K=1_K.
\]

No injectivity of \(H_i\) into the detector is required. The embedding of the ordinary subgroup and of the actual vertex into the regional orbifold group is the already proved B107 comparison. The actual neck marking, rather than an independently chosen abstract free factor, is essential here.

## 2. The general common finite-kernel construction

For a finitely generated group \(K\), let \(L_n\) be the intersection of the kernels of all homomorphisms from \(K\) to finite groups of order at most \(n\). One may choose one representative of each isomorphism class of target. There are finitely many targets and finitely many maps to each target, so \(L_n\) is normal and finite index. Precomposition with any endomorphism of \(K\) preserves the defining family, hence \(L_n\) is fully invariant. These subgroups are cofinal among finite-index normal subgroups of \(K\).

Fix a common such \(L\). In each vertex set

\[
P_i=\ker(H_i\xrightarrow{r_i}K\longrightarrow K/L),
\qquad N_i=P_i\cap t_iP_it_i^{-1},
\]

where \(t_i\in R_i\setminus H_i\). Since \(P_i\triangleleft H_i\), \(H_i\triangleleft R_i\), and \(t_i^2\in H_i\), conjugation by \(t_i\) interchanges the two factors while \(H_i\) normalizes them. Thus \(N_i\triangleleft R_i\), with finite index, and \(N_i\subset H_i\).

Its edge intersection is exactly \(L\). Indeed \(P_i\cap K=L\), while for \(k\in L\) the second membership condition follows from the actual endomorphism

\[
K\longrightarrow K,\qquad k\longmapsto r_i(t_i^{-1}kt_i).
\]

The map is well typed because conjugation preserves \(H_i\); full invariance supplies the required image in \(L\). It need not be an automorphism.

Given prescribed finite-index normal subgroups \(M_i\triangleleft R_i\), choose \(L\subset (M_1\cap K)\cap(M_2\cap K)\), and replace \(N_i\) by \(N_i\cap M_i\). The edge intersection remains exactly \(L\). Consequently arbitrary finite vertex quotients admit simultaneous refinements with the same embedded finite edge \(K/L\). Orientation is retained since each new kernel still lies in \(H_i\).

## 3. CE's stronger paired retraction is also valid

The stronger actual argument is independent of the fully invariant construction. Choose the actual odd order-two cone \(\tau_i\in R_i\), so \(R_i=H_i\rtimes\langle\tau_i\rangle\), and let \(\alpha_i=\operatorname{Inn}(\tau_i)|_{H_i}\).

For an A meridian in the literal disk basis, \(\alpha_i\) gives a based conjugate of a B peripheral. Ordinary B filling kills that entire conjugated peripheral, with its connector retained. For the disk's branch meridian, \(\alpha_i\) gives a based conjugate of the other branch peripheral. The free-factor projection kills the normal closure of that other branch generator. A common change from the global involution to the vertex cone only introduces further based conjugations and does not change either normal-killing statement. Therefore

\[
r_i|_K=1_K,\qquad r_i(\alpha_i(K))=1.
\]

It follows that

\[
h\longmapsto(r_i(h),r_i(\alpha_i(h)))
\]

extends to \(R_i\to(K\times K)\rtimes C_2\), with the cone swapping the factors and with \(k\mapsto(k,1)\). This construction does not assert an involution on the one-family filling target. Equivariance arises only in the paired target.

For every finite-index normal \(L\triangleleft K\), the resulting finite paired quotient has edge kernel exactly \(L\). Intersecting its kernel with a prescribed \(M_i\) retains that exact edge kernel when \(L\subset M_i\cap K\). Thus the actual geometric situation permits arbitrary common finite edge kernels; the more general fully invariant argument remains sufficient on its own.

## 4. Finite heads, residual finiteness, and completion

Let \(A_i=R_i/N_i\), \(D=K/L\), and form the discrete finite-group amalgam

\[
V=A_1*_{D}A_2.
\]

Take a finite set whose cardinality is a common multiple of \(|A_1|\) and \(|A_2|\). Realize each \(A_i\) by copies of its regular action. Restricted to \(D\), these are free \(D\)-sets of the same cardinality, so they can be identified. The resulting homomorphism \(V\to\operatorname{Sym}(X)\) is injective on both finite vertices. Its finite-index kernel acts freely on the ordinary amalgam tree and is therefore free. It has finite rank because \(V\) is finitely generated and the kernel has finite index.

This also proves residual finiteness of \(V\). An element outside the free kernel is already detected by the finite permutation quotient. For an element inside, use residual finiteness of the free subgroup and then take the finite-index core in \(V\). No residual finiteness of the original \(R_i\) is assumed or needed.

Every finite quotient of \(G\) factors through some \(V\): refine the two kernels of its vertex restrictions as in Section 2. Conversely, for any prescribed finite vertex quotient, construct a compatible finite head and then a finite permutation quotient of that head that embeds both finite vertices. Hence \(R_i\) has its full induced profinite topology in \(G\), and the maps \(\widehat R_i\to\widehat G\) are injective. The edge likewise has full topology, either by the common-kernel construction or by the actual ordinary retractions and an index-two core.

The universal property on finite targets now identifies

\[
\widehat G\;\cong\;\widehat R_1\amalg_{\widehat K}\widehat R_2.
\]

The amalgam is proper because both vertex maps have just been proved injective. This conclusion uses compatible finite edge kernels and finite-head extensions, not merely the separate assertion that \(K\) has full topology in each vertex.

## 5. All hypotheses of the prime-order centralizer theorem

The draft's reference to finite virtual cohomological dimension must be supplemented by the finiteness condition in **finite virtual p-cohomological type**. Here is a direct verification for every finite head \(V\), in particular for \(p=2\).

Choose a normal free finite-index subgroup \(F_r\triangleleft V\), with finite quotient \(D_0\). Its full profinite topology is induced from \(V\), by the ordinary finite-index core argument. Thus completion gives the exact extension with open kernel \(\widehat F_r\) and quotient \(D_0\).

For every discrete continuous \(\mathbb F_p[[\widehat F_r]]\)-module \(A\), comparison is an isomorphism in every degree. In degree zero this follows from density. In degree one, a cocycle of either free group is determined by arbitrary values on the finite free basis. Any finite tuple in \(A\) lies in a finite-dimensional finite invariant submodule: its compact-group orbits are finite. The corresponding finite semidirect product gives the continuous free-profinite extension of those cocycle values. Coboundaries are identical. In higher degrees both groups have cohomological dimension at most one, equivalently their standard free resolutions have length one.

Apply the Lyndon--Hochschild--Serre comparison to

\[
1\to F_r\to V\to D_0\to1,
\qquad
1\to\widehat F_r\to\widehat V\to D_0\to1.
\]

The two \(E_2\)-pages agree naturally for every discrete continuous \(\mathbb F_p[[\widehat V]]\)-module. Only rows zero and one occur, so the comparison proves goodness in every degree for **all** those modules. In particular no passage from finite-module goodness to arbitrary modules is being left implicit. Equivalently one could use filtered finite invariant submodules and the finite-type resolutions.

For a finite coefficient module \(A\), \(H^0(F_r,A)\) and \(H^1(F_r,A)\) are finite. Every cohomology group of the finite group \(D_0\) with a finite module is finite, since the cochain groups are finite. The same two-row spectral sequence therefore makes \(H^n(V,A)\) finite for every \(n\). Finally \(\operatorname{vcd}_p(V)\leq1\). These statements establish finite virtual p-cohomological type, rather than only finite vcd.

Residual finiteness supplies the required injective dense map \(V\hookrightarrow\widehat V\). Thus every hypothesis at the prime-two element use is established explicitly.

## 6. Primary proof read and the exact centralizer use

I independently opened Boggi and Zalesskii, *Finite subgroups of the profinite completion of good groups*, arXiv:2406.08639v2, and read Definition 4.1, Theorem 4.3, the complete proof of Lemma 4.4, Section 4.2, and Lemma 2.2 with its proof. The proof at this use is the prime-order case: comparison of high-degree cohomology gives hereditary conjugacy distinction for order-p elements, and the element-centralizer criterion gives the closure equality. No later claim about arbitrary finite or nonsolvable subgroup centralizers is used.

Primary URL: https://arxiv.org/html/2406.08639v2 (PDF: https://arxiv.org/pdf/2406.08639v2). Fresh retrieval records: `turn934view0`, `turn935view0`, `turn936view0`. The theorem's hypotheses are dense injectivity, finite virtual p-cohomological type relative to that embedding, and comparison for all discrete continuous modules in sufficiently high degrees. Section 5 proves the stronger all-degree comparison in the actual finite heads.

For completeness, the element-centralizer implication used from Lemma 2.2 can also be seen directly. Suppose an element \(x\) is conjugacy distinguished in \(\langle x\rangle U\) for a cofinal family of open normal \(U\). For \(c\in C_{\widehat V}(x)\), choose \(g\in V\) in the same \(\overline U\)-coset as \(c\). Then \(g^{-1}xg\) lies in \(\langle x\rangle U\) and in the closure of the \(U\)-conjugacy class of \(x\). Conjugacy distinction gives \(g^{-1}xg=u^{-1}xu\) for some \(u\in U\); powers of \(x\) in the conjugator can be discarded. Hence \(gu^{-1}\in C_V(x)\) has the same \(\overline U\)-coset as \(c\). Varying \(U\) proves \(C_{\widehat V}(x)=\overline{C_V(x)}\). This avoids any additional finite-centralizer approximation lemma at the last step.

## 7. The selected odd cone and passage back to the actual completion

Let \(\tau\in R_1\) be the selected order-two cone. Its image survives with odd orientation in every finite head. Every conjugate of the edge is even. Consequently the fixed subtree of \(\tau\) in the ordinary amalgam tree consists of exactly its vertex: two fixed vertices would give a fixed connecting edge. Thus

\[
C_V(\tau)=C_{A_1}(\tau).
\]

The right side is finite. The verified prime-order theorem therefore gives

\[
C_{\widehat V}(\tau)=C_{A_1}(\tau).
\]

Now take \(g\in C_{\widehat G}(\tau)\). Its image in every \(\widehat V\) belongs to the corresponding \(A_1\). If \(g\) were outside the compact image of \(\widehat R_1\), a finite quotient of \(\widehat G\) would separate it from that image. Its restriction to \(G\) factors through a finite head, contradicting the asserted membership in \(A_1\). Hence

\[
\boxed{C_{\widehat G}(\tau)=C_{\widehat R_1}(\tau).}
\]

The inclusion from right to left is immediate. This separation proof needs no compatibility choice of representatives across different heads and no residual finiteness assertion for \(R_1\) or \(R_2\).

## 8. Final scope

The complete proposed profinite upgrade passes. Its conclusions are the proper full profinite amalgam for the **actual first-neck slit model** and reduction of the selected cone centralizer to the appropriate actual vertex completion. The latter centralizer is still unevaluated. The three natural mixed-neck maps are already noninjective, so this argument cannot be reused for those necks before their actual quotient-edge maps have been identified. There is no all-neck, global fixed-source, full M-freeness, or kappa-vanishing conclusion.
