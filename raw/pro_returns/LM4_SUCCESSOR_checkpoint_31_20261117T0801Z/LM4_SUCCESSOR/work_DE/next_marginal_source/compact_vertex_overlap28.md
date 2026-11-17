# Actual compact vertex overlaps from a cofinal family of virtually free targets

Status: complete independent audit/proof, submitted for review. Research only; the frozen B136 and B137 sources are unchanged. The original root proposal is retained separately as `compact_vertex_overlap_proposal28.md`.

## 1. Conclusion and actual scope

In the actual B136/B137 marking put
\[
L=\langle K,k\rangle=H*_{\langle k\rangle}P,
\quad H=\langle h,k\mid[h^2,k]\rangle,
\quad P=\langle k\rangle\times F(a,d,e,V_4),
\]
\[
f=hk^{-1},\quad V_4=f^{-1}Bf,\quad
E_1=CLC,\quad \zeta=\eta(a),\quad
B_j=\langle\eta(f),\zeta^{-1}k\zeta\rangle.
\]
All closures below are **actual subgroup closures** in the indicated full completion of the actual regional group. The argument establishes full topology of the additional subgroup \(B_j\), so its closure can also be identified with its own full completion. It proves
\[
\overline{B_j}\cap\overline H=1,
\qquad
\overline{E_1}\cap\overline{B_j}=1,
\tag{1}
\]
and the exact compact product comparison
\[
\overline{B_j}\cap(\overline{E_1}\,\overline K)
 =\overline{B_j}\cap\overline K
 =\overline{\langle\eta(f)\rangle}.
\tag{2}
\]
The actual mirror gives the corresponding other-vertex statements. No compact embedding theorem for the cyclic-edge subamalgams defining \(H_i,H_j\), nor the whole compact intersection of those groups, is claimed here.

## 2. The finite-factor quotients retain the whole marked fork

For every integer \(n\ge2\) define
\[
P_n=C_n(k)\times(C_2(a)\times C_2(d)\times C_2(e)\times C_2(V_4)),
\quad G_n=C_2(C)*P_n.
\]
The homomorphism \(\phi_n:L\to G_n\) is given by \(h\mapsto C\), the indicated finite images of \(k,a,d,e,V_4\), and therefore
\[
f\mapsto f_n=Ck^{-1}.
\]
The relation \([h^2,k]\) holds, as do all relations of \(P\), so this is a genuine quotient of the entire regional \(L\), not a map defined only on the test subgroup. Put
\[
H_n=\langle C,k\rangle=C_2*C_n.
\]
Then
\[
G_n=H_n*_{C_n}P_n
\]
is a proper ordinary amalgam, directly equivalent to the displayed free product of finite groups.

Retain every letter in the exact B137 words:
\[
\ell=afa^{-1},\quad q=\eta(\ell),\quad U=\langle k,q\rangle,
\]
\[
\gamma=afV_4f^{-1}a^{-1}f,\quad D=ded^{-1},\quad
w=\gamma Df^{-1}d^{-1},
\]
\[
q=wf^{-1}w^{-1},\qquad
\zeta=\gamma V_4^{-1}f^{-1}a^{-1},\qquad
\zeta B_j\zeta^{-1}=U.
\tag{3}
\]
Use subscripts \(n\) for the images under \(\phi_n\).

The path from \(aH_n\) to \(w_nH_n\) has alternating leaf blocks
\[
a,\ V_4,\ a^{-1},\ D,\ d^{-1}
\]
and intervening \(f_n^{\pm1}\) blocks. In \(P_n/C_n\) these leaf blocks are respectively
\[
a,\ V_4,\ a,\ e,\ d,
\]
all nonidentity. Repeated involutive labels do not cancel, because every intervening \(f_n^{\pm1}\) remains outside \(C_n\). More generally every nonzero power of \(f_n=Ck^{-1}\) is outside \(C_n\): it is a nonempty alternating word in \(C_2*C_n\), since \(n\ge2\).

At the initial endpoint the first core edge remains \(af_nC_n\). For each nonzero residue \(j\pmod n\),
\[
f_n^{-1}k^jf_n=kCk^jCk^{-1}\notin C_n.
\tag{4}
\]
At the other endpoint all nonzero powers of \(q_n\) give distinct incident directions because they conjugate to nonzero powers of \(f_n^{-1}\). Thus the same equivariant subdivided-tree map is locally injective, now from the tree of
\[
C_n(k)*\mathbb Z(q).
\]
A locally injective map of ordinary trees is injective. Its equivariance and the faithful action prove
\[
U_n=\langle k_n,q_n\rangle\cong C_n*\mathbb Z,
\qquad \ker(U\to U_n)=\langle\!\langle k^n\rangle\!\rangle_U.
\tag{5}
\]
Here \(U\cong F(k,q)\) was already established by the unrestricted B137 endpoint proof.

At the interior vertex \(\gamma_nP_n\), the two core directions are \(1,D_n=e\), whereas the path to \(\zeta_nH_n\) begins in direction \(V_4^{-1}=V_4\). These three cosets remain distinct in \(P_n/C_n\). The entire tail \(f_n^{-1}a^{-1}\) is reduced after that departure. The endpoint therefore projects to this interior core vertex, whose \(U_n\)-stabilizer is trivial. Hence, for **every** \(n\ge2\),
\[
U_n\cap\zeta_nH_n\zeta_n^{-1}=1.
\tag{6}
\]
No finite sample of moduli replaces this all-n argument.

## 3. The precise topological facts in each target

The group \(G_n\) is a free product of two finite groups. The kernel of
\(C_2*P_n\to C_2\times P_n\) has finite index and acts freely on the ordinary free-product tree: its intersection with every conjugate of either finite vertex group is trivial. It is therefore a free group of finite rank, because its quotient graph is finite.

Every finitely generated subgroup of a finite-rank free group is closed in the profinite topology. For completeness, its finitely many generating loops lie in a finite core of its Schreier cover. To exclude any fixed word outside the subgroup, adjoin that word's finite path to the core; its endpoint is different from the basepoint. Complete this finite labeled graph to a finite cover by pairing, for each label, the missing outgoing and incoming slots. Their counts agree. No existing vertex is identified, so the word remains excluded. This produces a finite-index supergroup separating the word.

A finite-index free subgroup has the full induced profinite topology in \(G_n\): take the intersection of finitely many ambient conjugates of a finite-index normal subgroup. For a finitely generated \(A\le G_n\), its intersection with that free subgroup is finitely generated and finite index in \(A\). The finite coset decomposition then proves that \(A\) is closed in \(G_n\). The same applies to every finite-index subgroup of \(A\). Given \(A_0\triangleleft A\) of finite index, separate its finitely many nonidentity coset representatives from \(A_0\) by finite-index ambient subgroups, then take their normal core. This gives a finite-index normal \(N\triangleleft G_n\) with \(N\cap A\subset A_0\). Thus every finitely generated \(A\) has its **full** induced topology.

The additional input needed is closedness of products. Ribes and Zalesskii (2004), Theorem 3.13, proves that free products preserve the property that products of two finitely generated closed subgroups are closed, for the full profinite topology as a special case of their extension-closed pro-class statement. Both finite factors satisfy that property immediately. Thus every product of two finitely generated subgroups of \(G_n\) is closed. Their Lemma 3.1 independently verifies finite-index passage of the product property.

**Primary-source audit.** The author's complete PDF was opened at
https://mat.unb.br/~pz/arquivos/profreeprod.pdf . The full Theorem 3.13 and proof were read on PDF pages 15–19, and the complete Lemma 3.1 proof on pages 5–6. Successful retrieval references: `turn1018view1`, `turn1020view0`, `turn1020view1`, `turn1020view2`, `turn1020view3`. The original 1993 paper's publisher abstract was accessible, but its full-PDF attempts redirected to the abstract or failed; no full 1993 proof read is claimed. The later 2004 primary theorem is sufficient here, and the subgroup-topology argument above is explicit.

## 4. Why closed products give the exact completed intersection

The following proof is included to avoid an unproved completion/intersection exchange. Let \(A,B\) be finitely generated subgroups of \(G_n\), and let \(x\in\overline A\cap\overline B\). Fix any finite quotient \(\pi:G_n\to D\). Choose \(a\in A,b\in B\) with
\(\pi(a)=\pi(b)=\widehat\pi(x)\). Set
\[
A_0=A\cap\ker\pi,\qquad B_0=B\cap\ker\pi.
\]
They have finite index in the finitely generated groups \(A,B\). The finite coset decomposition yields
\[
x\in a\overline{A_0}\cap b\overline{B_0}.
\]
It follows that
\[
b^{-1}a\in\overline{B_0}\,\overline{A_0}
             =\overline{B_0A_0}.
\]
This last product is compact. Since \(B_0A_0\) is closed in \(G_n\), and \(b^{-1}a\) is an actual group element, write \(b^{-1}a=b_0a_0\) with \(b_0\in B_0,a_0\in A_0\). Then
\[
bb_0=aa_0^{-1}\in A\cap B
\]
has exactly the prescribed image of \(x\) in \(D\). As \(\pi\) was arbitrary,
\[
\overline A\cap\overline B=\overline{A\cap B}.
\tag{7}
\]
Applying (7) to (6) gives a trivial intersection in every \(\widehat G_n\).

## 5. Cofinality on the actual free pair, not a residual finite-word test

Let \(\psi:U\to D\) be an arbitrary finite target. Choose \(n\ge2\) divisible by the order of \(\psi(k)\). By (5), \(\psi\) factors through \(U_n\). Full induced topology of \(U_n\) in \(G_n\) supplies a finite quotient of \(G_n\) whose restriction kernel on \(U_n\) is contained in the kernel of that factored target. Compose with \(\phi_n:L\to G_n\).

Therefore the actual subgroup \(U\) has full induced profinite topology in \(L\), and the maps
\[
\widehat U\longrightarrow\widehat G_n\qquad(n\ge2)
\]
jointly separate **all completed elements**: their finite refinements are cofinal among arbitrary finite \(U\)-targets. This is stronger than separating the nonidentity ordinary words of \(U\).

If \(x\in\overline U\cap\zeta\overline H\zeta^{-1}\), its image in every \(\widehat G_n\) is one by (6)–(7). Cofinality forces \(x=1\). Conjugating by \(\zeta\) proves
\(\overline{B_j}\cap\overline H=1\).

All completions here are the actual embedded closures: \(L\) is a retract of \(R^0\), \(H\) is a retract of \(L\), and \(B_j\) is conjugate within \(L\) to the just-proved full-topology \(U\).

## 6. Continuous color and neck retractions give the claimed vertex results

The actual color-zero retraction \(R^0\to L\) fixes \(L\) and maps \(E_1\) onto \(H\). Extend it continuously. If \(x\in\overline{E_1}\cap\overline{B_j}\), then \(x\in\overline L\), so the retraction fixes it and also places it in \(\overline H\). The preceding trivial intersection proves (1). The same argument gives
\(\overline{E_1}\cap\overline L=\overline H\).

For (2), take \(b=e k_0\in\overline{B_j}\cap(\overline{E_1}\,\overline K)\). Compactness makes this product an actual closed product, so such factors exist. Since \(b,k_0\in\overline L\), we have \(e\in\overline H\). The continuous actual retraction \(r:\overline L\to\overline K\) satisfies
\[
r(\overline{B_j})=\overline{\langle\eta(f)\rangle}\subset\overline{B_j},
\quad r(\overline H)=\overline{\langle f\rangle}\subset\overline H.
\]
Consequently
\[
b r(b)^{-1}=e r(e)^{-1}
 \in\overline{B_j}\cap\overline H=1.
\]
Thus \(b=r(b)\in\overline K\), and retraction also identifies that intersection with \(\overline{\langle\eta(f)\rangle}\). This proves (2). All mirror statements follow from the actual continuous involution \(\theta\), retaining its \(\eta\) on the common neck.

## 7. Precise remaining compact gate

These are full compact **vertex** and incident-product comparisons. They do not by themselves prove that the abstract completed cyclic-edge subamalgams defining \(H_i,H_j\) embed in \(\widehat V\), or that their invariant compact trees are the expected embedded images. No general subamalgam theorem with nontrivial edge intersection has been invoked. The ordinary B137 whole-intersection proof is unchanged; its completed analogue remains a separate gate.

Likewise these comparisons are before the two initial fillings. They do not prove that \(D_{\rm loc}\) survives in \(V_*\), that its actual kernel is \(\kappa\)-invariant, or that the fixed-source equality holds after the entire matching normal closure.

## Reference

Ribes, L., & Zalesskii, P. (2004). Profinite topologies in free products of groups. *International Journal of Algebra and Computation, 14*, 751–772. https://doi.org/10.1142/S0218196704001992 . Primary author PDF and exact theorem/proof locations are recorded above. Publisher DOI-page retrieval returned HTTP 403; the actual primary PDF read succeeded.
