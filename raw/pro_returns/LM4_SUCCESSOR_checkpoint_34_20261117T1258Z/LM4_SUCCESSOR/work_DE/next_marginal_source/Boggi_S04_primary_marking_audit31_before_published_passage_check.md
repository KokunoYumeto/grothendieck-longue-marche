# Four-punctured-sphere stabilizer: original proof and actual marking audit

Cycle 31. Written after the explicit checkpoint-30 release. All cycle-30 files remain unchanged. This is an independent source/dependency and application audit, not a new assertion about the original icosahedral kernel.

## 1. Verdict and exact theorem being used

**PASS for the pure four-punctured-sphere application below.** The inspected input is Boggi (2014a), Theorem 4.2 together with Proposition 3.4. The former identifies the abstract procongruence curve completion with the realization by conjugacy classes of profinite simple curves (with the two orientations identified); the latter computes stabilizers of geometric simplices for open subgroups. Their combination gives the closure of the corresponding discrete curve stabilizer. The hypothesis is negative Euler characteristic, so it includes the separating essential curve on (S_{0,4}).

The full-group formulation in Boggi and Funar (2023), Theorem 4.5, Lemma 4.8, and Corollary 4.9 was also read. It is corroborating exposition; the application below needs only the original **pure** theorem and genus-zero congruence subgroup property. No general statement about centralizers of arbitrary finite subgroups, and no faithfulness assertion for the completion of an integral matrix representation, is imported.

## 2. Complete primary readings and dependency boundary

The following are genuine complete readings of the indicated proofs, not merely search snippets or theorem statements:

* Boggi (2014a), original arXiv 0910.4305v5: Proposition 3.4; Theorem 4.2 and its entire printed proof, PDF pp. 11–16 (retrieval lines 564–922); the stabilizer deduction immediately before Theorem 4.5, PDF p. 17. The proof treats the nonseparating case in detail and explicitly assigns the separating case the same argument.
* Boggi (2014b), arXiv 1111.2372v4: Lemma 3.10 and its proof, PDF pp. 13–14; Theorem 7.7 and its entire proof, PDF pp. 31–33; Corollary 7.8 and its proof plus Remark 7.9, PDF p. 33. These provide suitable characteristic covers and the injective family of finite homology-graph encodings used by Theorem 4.2. Their construction does not invoke Theorem 4.2.
* Boggi and Funar (2023), arXiv 2004.04135v4: the full discussion and proof sketches in §§4.5–4.6, including Lemma 4.8 and Corollary 4.9. This identifies the same dependency chain explicitly.
* McReynolds (2012), arXiv 0901.4663v2: the (n=4) deduction on PDF p. 6, the marked Birman comparison in Lemma 2.2, and the complete printed proof of Proposition 3.1 in §5, including Lemmas 5.1–5.3. This is a primary independent proof of the genus-zero congruence statement attributed to Asada, rather than a reliance on Boggi's former general-genus congruence claim.

The earlier reported gap in the general congruence claim in Boggi (2006) is not an input here. The abstract-completion stabilizer calculation is a coset-completion statement; genus-zero full/congruence comparison is supplied independently. The inspected dependency graph contains no return from the homology-graph theorem to Theorem 4.2 and no appeal to the general congruence conjecture.

The scope of this audit is the complete printed proofs above and the exact application below. It does not assert a fresh proof of every background theorem on admissible covers or moduli stacks used in those papers.

**Qualification added after the complete independent/root comparison.** Reading McReynolds's entire finite proof is not an unqualified correctness endorsement of each printed step. In Lemma 5.3 the phrase allowing a fixed arbitrary prime cannot be used as written when the starting quotient is a noncyclic p-group and the chosen prime is p: the resulting nontrivial groups and quotients are p-groups and cannot be centerless. Nor is a quotient by the center generally centerless. The later product/normal-closure embedding is not imported without a proof. These issues do not change the established genus-zero CSP theorem, but the application here now uses the complete independent S0,4 proof in §5.1 below. The earlier audit bytes are preserved as Boggi_S04_primary_marking_audit31_before_CSP4_repair.md, SHA 2ec6e2df487724d3fab6b919d2a6ff9870725b589b22a5e3bb9b6a8b5a89b201. The following explicit replacement is part of the final verdict.

## 3. Separating curve and a safe cofinal-cover choice

Write the actual marked sphere group as

\[
 \Pi=\langle r,g,f,\bar r\mid rgf\bar r=1\rangle
      =F(r,\bar r,w),\qquad w=rg.
\]

The curve \(\gamma\) separating the puncture pair \((g,f)\) from \((r,\bar r)\) is represented, up to conjugacy and inversion, by \(r\bar r\). Indeed \(\bar r r=(gf)^{-1}\), and \(r\bar r\) is conjugate to \(\bar r r\). It is nonperipheral. Both cut components are three-punctured spheres. Thus the separating version of the original proof uses two component-group orbits, rather than the two conjugate copies of one component group appearing in its detailed nonseparating exposition. In the pure group the puncture labels preserve the two sides. The node inertia, its two adjacent component groups, and the marked finite-cover homology graph are precisely the separating counterparts of the objects in the printed proof. The proof does not require a nonseparating curve on the original surface.

There is a useful low-genus precaution when instantiating Lemma 3.10. Its printed intermediate genus assertion should not be used for an arbitrary ramified four-punctured-sphere cover: small ramified covers can compactify to genus one. For the cofinal system needed here one can instead begin inside

\[
 K_3=[\Pi,\Pi]\Pi^3.
\]

This is characteristic of index \(3^3=27\). Each of the four peripheral elements has order three in the quotient; the cover has \(4\cdot27/3=36\) punctures. Its Euler characteristic is \(27(-2)=-54\), so

\[
 2-2g-36=-54,\qquad g=10.
\]

Every further finite cover inside \(K_3\), after compactification, maps to this genus-ten surface, possibly with branching. Riemann–Hurwitz gives compact genus at least two. Intersecting any prescribed characteristic finite-index subgroup with \(K_3\), and then applying the characteristic homology-cover refinement of Lemma 3.10, preserves cofinality. This supplies exactly the covers used by the original proof without using the overbroad small-cover genus assertion.

For this curve the needed inertia self-normalizer is also transparent independently: \(r\bar r\) is primitive in the free group \(F(r,\bar r,w)\), by a Nielsen change of basis. Its procyclic factor in the free profinite product is self-normalizing. This observation does not replace the finite homology-graph part of Theorem 4.2; it only checks the elementary inertia input in this particular case.

## 4. Actual operator and finite-index marking audit

I read the complete saved CE file `work_CE/compact_one_family_stabilizer_geometric31.txt` in its initial version, as well as the frozen complete normalization30 file. The relevant operators are literally

\[
\begin{aligned}
 m(r)&=r,&m(\bar r)&=\bar r,&m(w)&=rw^{-1}\bar r^{-1},\\
 u(r)&=w^{-1}rw,&u(\bar r)&=w\bar r w^{-1},&u(w)&=w.
\end{aligned}
\]

Consequently \(m\) interchanges the positive peripheral classes of \(g\) and \(f\), fixing those of \(r,\bar r\); \(u\) is pure. In the actual tuple,

\[
 m(g)=f,\quad m(f)=f^{-1}gf,
\]

and \(u\) conjugates the first pair \((r,g)\) by \(w^{-1}\) and the second pair \((f,\bar r)\) by \(w\). These are geometric orientation-preserving sphere mapping classes with the printed based corrections retained.

For \(S=F(m,u)\), let \(S_p=\ker(\operatorname{exp}_m\bmod2)\). Its actual mapping-class image is pure. The pillowcase matrices are

\[
 M=\begin{pmatrix}1&-1\\0&1\end{pmatrix},\qquad
 U=\begin{pmatrix}1&0\\4&1\end{pmatrix}.
\]

Conjugation by \(\operatorname{diag}(2,1)\) gives the upper \(-2\) and lower \(2\) generators. The frozen all-word ping-pong proof supplies projective faithfulness. The Euclidean column reduction in CE's file gives \(\langle M,U,-I\rangle=\Gamma_0(4)\). Reduction modulo two shows that its pure subgroup is \(\Gamma_0(4)\cap\Gamma(2)\), of index two in \(\Gamma(2)\). Thus the actual outer image of \(S_p\) has index two in the pure four-punctured-sphere mapping-class group. The Klein-four kernel of the full pillowcase map meets the pure group trivially. Root independently read the complete primary pillowcase proof in Farb–Margalit §2.2.5; this audit does not substitute an unproved matrix identification for that topological input.

The slope of \(\gamma\) is \(\pm e_1\). Within the actual projectively faithful source image, an element preserving this slope is a power of \(m\); intersecting with \(S_p\) gives exactly \(\langle m^2\rangle\). This is a discrete matrix calculation. It is **not** an assertion that matrix congruence quotients induce the full topology on \(S\).

## 5. Full completion and the actual compact stabilizer

### 5.1. A complete direct compact proof of exactly CSP4

Choose a positive peripheral free generator \(\lambda\) of \(\Pi=F_3\), and put \(\Pi_0=\Pi/\langle\!\langle\lambda\rangle\!\rangle=F_2\). Let \(\operatorname{Out}_c(\widehat\Pi)\) be the closed subgroup preserving the conjugacy class of each positive peripheral element. Every element has a representative fixing \(\lambda\). Two such representatives differ by \(\operatorname{Inn}(c)\) with \(c\in C_{\widehat\Pi}(\lambda)=\overline{\langle\lambda\rangle}\), because \(\lambda\) is a primitive free factor. After killing \(\lambda\), this ambiguity is trivial. Therefore descent defines a homomorphism

\[
 \widehat\delta:\operatorname{Out}_c(\widehat\Pi)
                 \longrightarrow\operatorname{Aut}(\widehat\Pi_0).
\]

It is continuous without choosing a continuous representative section: the closed compact subgroup of peripheral-preserving automorphisms fixing \(\lambda\) maps continuously onto \(\operatorname{Out}_c\), and its continuous descent to \(\widehat\Pi_0\) kills exactly the relevant inner ambiguity. The resulting quotient map is continuous.

The actual marked Birman point-push isomorphism identifies \(\operatorname{PMod}(S_{0,4})\) with \(\Pi_0\), and its normalized action satisfies \(\delta\circ\operatorname{Push}=\operatorname{Inn}\). This is precisely McReynolds's Lemma 2.2 and the n=4 point-push identification; these marked statements have been read independently. Completing and using density gives

\[
 \widehat\delta\circ\widehat{\operatorname{Push}}
       =\operatorname{Inn}:\widehat F_2\longrightarrow
                                      \operatorname{Aut}(\widehat F_2).
\]

The center of \(\widehat F_2\) is trivial, by the free-profinite-product factor-centralizer argument already used in this project. Hence the completed point-push is injective. Its compact image is precisely the procongruence closure of the pure mapping-class group. This proves the exact full/procongruence comparison required here, independently of the questionable finite steps just identified.

### 5.2. Actual source application

Since \(S_p\) is an actual finite-index subgroup, its full completion identifies with an open subgroup of that procongruence group. Apply Boggi's Proposition 3.4 and Theorem 4.2 directly to this open subgroup:

\[
 \operatorname{Stab}_{\widehat S_p}(\gamma)
       =\overline{\langle m^2\rangle}.
\]

This is an open-subgroup application of the cited theorem, not an exchange of arbitrary completion and subgroup intersection.

Now use the actual semidirect group \(E_0=T_0\rtimes S\), with \(T_0=F(r,\bar r,w)\). Finite characteristic fiber quotients show \(\widehat E_0=\widehat T_0\rtimes\widehat S\). The actual section \(H=\langle m,fv\rangle\) is the graph of the ordered peripheral cocycle \(h_s\); its completion is likewise an embedded graph section. Define \(L_c=\widehat H\cap\widehat S\) inside this group, without calling it \(\widehat{H\cap S}\).

The identities \(\alpha_s(r)=h_srh_s^{-1}\) and \(\chi_x(h_s)=0\), with \(\chi_x(r)=1\), continue by continuity. The centralizer of the primitive free generator \(r\) is \(\widehat{\mathbb Z}(r)\); therefore

\[
 L_c=\{s\in\widehat S:\alpha_s(r)=r\}.
\]

Every source commutes with the actual involution exchanging \(r,\bar r\). Hence an element of \(L_c\) fixes both words and the geometric curve \(\gamma\). If it has even \(m\)-parity, the preceding theorem places it in \(\overline{\langle m^2\rangle}\). If it has odd parity, multiply by \(m^{-1}\), which itself fixes \(r\), and apply the even case. Conversely every profinite power of \(m\) fixes \(r\). Thus

\[
 \boxed{\widehat H\cap\widehat S=\overline{\langle m\rangle}
                =\widehat{\mathbb Z}(m).}
\]

This closes the stated compact stabilizer input for the actual one-family coarse group. It gives neither the ambient full topology of the larger one-family fixed-source image nor its completed marked section by itself. Those require CE's separate finite-permutation extension, retaining \(T_0\). It does not establish the original B75 characteristic-neighborhood criterion or the remaining fixed-kernel generation.

### 5.3. Independent one-target finite proof of CSP4

There is also a direct finite detector, useful for comparing the original B75 kind of uniform-neighborhood problem. Given any finite quotient of the point-push \(F_2\), refine it to a centerless finite quotient \(P\). Here is a complete safe refinement: start with a nontrivial finite image \(Q=F_r/N\), \(r\ge2\), choose a prime \(\ell\nmid|Q|\), and put \(E=F_r/(N^\ell[N,N])\). Its kernel V over Q has the finite Cayley-graph exact sequence

\[
0\longrightarrow V\longrightarrow\mathbb F_\ell[Q]^r
 \longrightarrow I_Q\longrightarrow0.
\]

Semisimplicity gives \(V\cong\mathbb F_\ell\oplus\mathbb F_\ell[Q]^{r-1}\); averaging splits the group extension. Quotient by the central invariant subspace \(V^Q\). The resulting split kernel is \(I_Q^{r-1}\), has no invariants, and carries a faithful Q-action, since the regular module is the sum of its invariant line and augmentation module. Thus the resulting quotient is centerless and still maps onto Q. A trivial prescribed target needs no refinement.

Now map \(\Pi=\Pi_0*\langle\lambda\rangle\) to
\(\mathbb F_\ell[P]\rtimes P\) by \(\lambda\mapsto(1,1)\) and \(\Pi_0\mapsto(0,P(\Pi_0))\). Every element centralizing the displayed lamp has trivial P-head. Choose a characteristic finite-index subgroup K of \(\Pi\) inside the kernel of this one homomorphism; such a refinement exists because \(\Pi\) is finitely generated. If the normalized point-push of s is inner on \(\Pi/K\), its conjugator c centralizes \(\lambda\) there. The lamp quotient gives trivial P-head for c. The exact normalized Birman identity, after killing \(\lambda\), then says that \(\operatorname{Inn}(P(s))\) is trivial. Since P is centerless, \(P(s)=1\).

Therefore the principal characteristic congruence kernel lies in the arbitrary prescribed point-push kernel. This is one actual finite target followed by characteristic refinement; it uses neither a product quotient/normal-closure embedding nor an arbitrary finite-subgroup centralizer theorem.

## 6. Retrieval and bibliographic record

Primary PDFs successfully read:

* https://arxiv.org/pdf/0910.4305 — original theorem; refs `turn1090view0`, `turn1092view0`, `turn1093view0`, `turn1105view1`, `turn1107view2`, `turn1119view4`, `turn1120view4`.
* https://arxiv.org/pdf/1111.2372 — cover/graph dependencies; refs `turn1097view0`, `turn1099view0`, `turn1099view1`, `turn1105view2`, `turn1107view3`, `turn1119view3`, `turn1120view2`, `turn1120view3`.
* https://arxiv.org/pdf/2004.04135 — later exposition; refs `turn1107view0`, `turn1112view0`, `turn1112view1`, `turn1112view2`.
* https://arxiv.org/pdf/0901.4663 — primary genus-zero CSP proof; refs `turn1112view3`, `turn1114view1`, `turn1117view0`–`turn1117view3`, `turn1119view0`–`turn1119view2`, `turn1120view0`, `turn1120view1`.

The version-suffixed Boggi PDF fetches and the Funar author-PDF fetch initially failed; no successful fetch or reading is attributed to those failures. Unversioned arXiv URLs returned the specified versions successfully. Asada's original publisher abstract/metadata was retrieved; its entire original proof was **not** newly retrieved in this audit. The complete independent genus-zero proof just listed supplies the proof reading for that input.

References:

Asada, M. (2001). The faithfulness of the monodromy representations associated with certain families of algebraic curves. *Journal of Pure and Applied Algebra, 159*, 123–147. https://doi.org/10.1016/S0022-4049(00)00056-6

Boggi, M. (2014a). On the procongruence completion of the Teichmüller modular group. *Transactions of the American Mathematical Society, 366*, 5185–5221. https://doi.org/10.1090/S0002-9947-2014-05971-0

Boggi, M. (2014b). Galois coverings of moduli spaces of curves and loci of curves with symmetry. *Geometriae Dedicata, 168*, 113–142. https://doi.org/10.1007/s10711-012-9821-2

Boggi, M., & Funar, L. (2023). Automorphisms of procongruence curve and pants complexes. *Journal of Topology, 16*, 936–989. https://doi.org/10.1112/topo.12306

McReynolds, D. B. (2012). The congruence subgroup problem for pure braid groups: Thurston's proof. *New York Journal of Mathematics, 18*, 925–942. https://nyjm.albany.edu/j/2012/18-47p.pdf . Publisher metadata and final-PDF first page independently opened as turn1127view0 and turn1127view1. The detailed earlier proof-read log concerns the stated arXiv version; the direct replacement above does not depend on the finite proof's disputed steps.
