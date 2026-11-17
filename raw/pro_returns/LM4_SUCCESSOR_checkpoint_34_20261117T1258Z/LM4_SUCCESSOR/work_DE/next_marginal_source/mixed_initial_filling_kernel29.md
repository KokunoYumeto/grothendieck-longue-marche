# Exact mixed-kernel form of both initial fillings

Checkpoint29 research. This uses the actual B134 words, the unchanged checkpoint27 free-pair proof, and the new regional retraction-kernel presentation. It does not assert that a regional image of a mixed relator is killed in the actual filled group.

## 1. Simultaneous conjugation of the complete first family

Use

\[
V=R_L*_K R_R,\quad R_R=p(R^0),\quad p|_K=\eta,
\quad a_1=CaC,\quad v_0=p(aa_1^{-1}),
\]

\[
\sigma(CuC)=p(C\eta(u)C),\qquad s=v_0^{-1}kv_0.
\]

For every \(u\in K\), define the exact right-vertex word

\[
d(u)=v_0\sigma(CuC)v_0^{-1}
    =p\bigl(aC(a^{-1}\eta(u)a)Ca^{-1}\bigr).
\tag{1}
\]

The second equality uses \((aa_1^{-1})C=aCa^{-1}\); it is a literal free-word identity with \(C^2=1\), not a quotient calculation. The map d is a homomorphism and its image is the actual conjugate free subgroup \(p(aK_1a^{-1})\), with the invertible K-marking \(u\mapsto a^{-1}\eta(u)a\) retained.

Put

\[
(V_1,V_2,V_3,V_4)=(a,d,e,f^{-1}Bf),\qquad
\gamma=d(f),\qquad x_i=d(V_i).
\]

Conjugating all five B134 target words by the same v0 gives precisely

\[
P_0=[(\gamma k)^2,k],\qquad P_i=[k,x_i]\quad(1\leq i\leq4).
\tag{2}
\]

Thus the entire actual initial quotient is

\[
V_*=V/\langle\!\langle P_0,\ldots,P_4,
                       \theta(P_0),\ldots,\theta(P_4)\rangle\!\rangle_V.
\tag{3}
\]

Conjugating a whole relator family does not change its ambient normal closure. Equation (3) retains both mirror sheets and the square relation on each sheet.

## 2. Exact retained heads and kernel locations

Let r be the actual regional retraction to K and let the common-neck retraction on the right vertex be

\[
r_R(p(g))=\eta(r(g)).
\]

Recall \(r(CuC)=\zeta(u)\), where \(\zeta\) kills a,B,d,e and fixes f. Write \(\chi_f\) for the f-exponent. The exact reflection preserves branch height with opposite sign, so \(\zeta\eta(u)=f^{-\chi_f(u)}\). Equation (1) gives

\[
r_R(d(u))=\eta(a)\eta(f)^{-\chi_f(u)}\eta(a)^{-1}
          =q^{\chi_f(u)},
\quad q=\eta(af^{-1}a^{-1}).
\tag{4}
\]

Consequently every \(x_i\) lies in the actual right kernel \(N_R\), while \(r_R(\gamma)=q\). Also k lies in the left kernel \(N_L\). Thus every relator in (2) belongs to \(N=N_L*N_R\), as does its theta mate.

Define

\[
c=\gamma q^{-1}\in N_R,
\qquad\alpha=\operatorname{Ad}(q)|_N,
\qquad \kappa_j=\alpha^j(k),\quad c_j=\alpha^j(c).
\]

The symbol c here is a right-kernel correction, not either cone generator. It is a specified whole word \(d(f)q^{-1}\).

## 3. The retained-square relation is a mixed two-step recurrence

Use the normal form n times K in \(N\rtimes K\). Since \(\gamma=cq\), one has

\[
\gamma k=c\alpha(k)q,
\qquad(\gamma k)^2=c \kappa_1 c_1 \kappa_2 q^2.
\]

Straight multiplication and cancellation therefore give the exact kernel word

\[
P_0=c \kappa_1 c_1 \kappa_2 c_1^{-1}\kappa_1^{-1}c^{-1}\kappa_0^{-1}.
\tag{5}
\]

The symbols \(\kappa_j\) denote this q-orbit and are not the regional generators \(k_0,k_1=CkC\). Its equation is

\[
\kappa_0=(c \kappa_1 c_1)\,\kappa_2\,(c \kappa_1 c_1)^{-1}.
\tag{6}
\]

Here the kappa letters belong to \(N_L\), the c letters belong to \(N_R\), and the actual q action preserves the two factors. The four other equations are the mixed commutators \([k,x_i]\). Their theta mates have the factors exchanged and the full actual eta-marking retained.

Equations (5)–(6) show exactly why this is not merely a list of commutations between coordinate graph vertices. The two-step recurrence is part of the actual local E1 presentation. Dropping it is the earlier incomplete leaf-only repair, not an equivalent presentation.

The full kernel of \(V\to V_*\) is the normal closure in N of all actual K translates of these ten words. This follows from \(V=N\rtimes K\) and the fact that all ten words lie in N. The actual actions are the factorwise ordered cocycles in `regional_retraction_kernel_graph29.md`; no bound on word length, height or translation is imposed.

## 4. A concrete obstruction to erasing the opposite regional kernel

There is a genuine unfilled retraction \(\pi_L:V\to R_L\), identity on the left vertex and equal to \(r_R\) on the right. The common K maps agree. It kills \(N_R\), fixes k, and sends gamma to q. Hence

\[
\pi_L(P_i)=1\quad(1\leq i\leq4),\qquad
\pi_L(P_0)=[(qk)^2,k].
\tag{7}
\]

This last word is **nontrivial** in the actual left regional group. Put \(\ell=afa^{-1}\). Then \(q=\eta(\ell)^{-1}\). The complete all-exponent normal-form proof in checkpoint27 established that

\[
\langle k,\eta(\ell)\rangle=\langle k\rangle*\langle\eta(\ell)\rangle.
\]

Thus k,q are a free basis of the same free subgroup. The word in (7) freely reduces to the nonempty length-eight word

\[
qkqkq^{-1}k^{-1}q^{-1}k^{-1}.
\]

Therefore the existing retraction \(\pi_L\) does **not** descend to a homomorphism \(V_*\to R_L\). Its theta counterpart fails for exactly the mirrored square relation. This is a statement about compatibility of a specified retraction with the filling. It does not assert that the nontrivial regional word in (7) is itself killed by \(V\to V_*\): it is the image of a mixed relation under a map which does not descend.

Both square words remain nontrivial in the corresponding regional completions as well, since the actual free pair has full induced topology by the checkpoint28 all-n proof. Thus the same specified continuous retractions cannot descend after the closed initial filling. This conclusion uses the full topology already proved for the marked pair, not an assumption that the whole regional group is residually finite.

## 5. A sharper location of this obstruction

In the graph model of `regional_retraction_kernel_graph29.md`, delete every expanded family vertex and retain all expanded k vertices. Since no two expanded centers are adjacent, this gives a retraction

\[
N_R=A(\Sigma)\longrightarrow F(\Sigma_{\rm centers}).
\]

It is compatible with the actual K action: retained translations and the height shift preserve centers and families, and each section correction in the cocycle is a word entirely in center vertices. Consequently it extends to the established color retraction \(R^0\to L=\langle K,k\rangle\). In particular it fixes the entire free pair \(\langle k,q\rangle\), because q belongs to K.

The obstruction (7) is therefore already present in this exact free regional retraction kernel together with K. It is not caused by omitted opposite-family node relations. Resolving it requires the genuine coupled recurrence (6), or an equivalent faithful presentation of its all-translates quotient; declaring the regional kernels free or imposing only the four mixed leaf commutators does not remove it.

This note gives an exact whole-input rewrite and a specified nonextension result. It does not prove that the local quotient Dloc embeds in V_*, that its actual kernel is kappa-invariant, that the two filled edge maps have matching kernels, or that the fixed-source question is decided. Those remain the substantive next gates.
