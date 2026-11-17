# Whole actual compact edge intersection via retraction kernels

Status: complete proof submitted for independent review. This is separate research, not an alteration of frozen B137. It uses the newly proved full-topology/compact embedding of the actual edge groups. No finite-geodesic argument on a profinite tree is used.

## 1. Exact conclusion

In the actual unfilled full completion of
\[
V=R_L*_{K}R_R,
\quad H_i=E_1*_{\langle f\rangle}B_i,
\quad H_j=B_j*_{\langle\eta(f)\rangle}p(E_1),
\]
we have
\[
\boxed{\overline{H_i}\cap\overline{H_j}=1.}
\tag{1}
\]
The bars are actual closures in \(\widehat V\), already proved to be the full completions of the displayed ordinary groups. The conclusion is before both initial fillings. It does not give any local quotient survival or kappa-invariance of its actual kernel.

## 2. Common-retract profinite amalgams have an exact kernel decomposition

We first prove the needed general statement. Let \(A=N_A\rtimes K\) and \(B=N_B\rtimes K\) be profinite groups with the same continuous common retract \(K\). Their proper full profinite amalgam satisfies
\[
A\amalg_KB\cong(N_A\amalg N_B)\rtimes K,
\tag{2}
\]
where the action of K extends its actual actions on the two compact factors.

Here is the continuity point explicitly. Put \(N=N_A\amalg N_B\). For each \(k\in K\), the factor automorphisms extend uniquely to an automorphism of N. Fix any finite continuous map \(\varphi:N\to F\). On either compact factor, joint continuity of the original K-action implies that an open neighborhood of1 inK fixes the whole finite map \(\varphi|_{N_A}\), respectively \(\varphi|_{N_B}\), pointwise: for each factor point use continuity into the finite discrete F and then take a finite subcover of the compact factor. Intersect these neighborhoods and choose an open subgroup K0 inside. By the coproduct universal property, K0 fixes \(\varphi\) on all of N. The K-orbit of \(\varphi\) is therefore finite. Intersect the finitely many kernels in this orbit. The result is an open normal K-invariant subgroup of N contained in ker(phi). The action on the resulting finite quotient is continuous; the same uniform factor argument gives an open action kernel. These invariant open subgroups are cofinal, proving a jointly continuous K-action on N.

Now form the profinite semidirect product on the right of (2). Its two vertex maps agree on K, so the amalgam universal property gives one map. The two kernel factors and K in the amalgam give the inverse map, because their conjugation actions agree. Both composites fix the generating kernel factors and K. This proves (2), including that its kernel is precisely the displayed free profinite coproduct.

## 3. A factorwise intersection lemma for free profinite coproducts

Let \(G=A\amalg B\), with arbitrary profinite factors, and let \(A_1,A_2\le A\), \(B_1,B_2\le B\) be closed subgroups. Write
\[
H=\overline{\langle A_1,B_1\rangle},\qquad
J=\overline{\langle A_2,B_2\rangle}.
\]
Then
\[
H\cap J=
\overline{\langle A_1\cap A_2,\ B_1\cap B_2\rangle}.
\tag{3}
\]
No finite-generation assumption is imposed on these original compact factors or subgroups.

Fix an arbitrary finite continuous target \(q:G\to D\). Compactness supplies a finite quotient \(q_A:A\to A_0\), refining \(q|_A\), such that
\[
q_A(A_1)\cap q_A(A_2)
\quad\text{maps into}\quad q(A_1\cap A_2)\text{ in }D.
\tag{4}
\]
Indeed, otherwise for every sufficiently small open normal M below ker(q|A), there are \(a_1\in A_1,a_2\in A_2\) with \(a_1M=a_2M\) but \(q(a_1)\notin q(A_1\cap A_2)\). These conditions define nonempty closed subsets of the compact product \(A_1\times A_2\), with the finite-intersection property as M is refined. A common pair has \(a_1=a_2\), contradicting the last condition. The same proof gives a finite \(B_0\) and the B version of (4).

Set \(G_0=A_0*B_0\) as an ordinary free product of finite groups. Its full completion is the corresponding free profinite coproduct. Thus the factor quotient maps give a continuous map
\(G\to\widehat G_0\), followed by a map \(\widehat G_0\to D\) whose composite is q. Put \(A_{i0}=q_A(A_i)\) and \(B_{i0}=q_B(B_i)\). The image of H in \(\widehat G_0\) is exactly the closure of
\[
H_0=A_{10}*B_{10},
\]
and similarly for \(J_0=A_{20}*B_{20}\). Both are finitely generated subgroups of the virtually free \(G_0\).

The proved finite-core/finite-index argument gives their closedness and full topology. Ribes–Zalesskii2004 Theorem3.13 gives closed products of the relevant finitely generated subgroups in this finite-factor free product. The explicit closed-product intersection argument in `compact_vertex_overlap28.md` Section4 therefore gives
\[
\overline{H_0}\cap\overline{J_0}
   =\overline{H_0\cap J_0}.
\]
Ordinary reduced-word uniqueness gives
\[
H_0\cap J_0=(A_{10}\cap A_{20})*(B_{10}\cap B_{20}).
\]
For any \(x\in H\cap J\), equations (4) and its B counterpart imply that q(x) lies in the subgroup of D generated by \(q(A_1\cap A_2)\) and \(q(B_1\cap B_2)\). This holds for every finite q. The closed subgroup on the right of (3) is determined by these finite images, proving the nontrivial inclusion; the converse is immediate.

The images of the individual free profinite coproducts of closed factor subgroups are their expected embedded coproducts. This can be seen either from the already verified zero-edge closed-subgroup theorem, or directly: refine arbitrary finite maps of the two closed subgroups by finite quotients of A,B, embed their finite-factor free product in the corresponding virtually free finite-factor overgroup, and extend the prescribed finite target using its full subgroup topology. The argument for (3) itself only needs the actual closed generated subgroups, so does not depend on an unstated embedding assertion.

## 4. The two actual cyclic retraction images intersect trivially

The two actual vertex retractions to the identified K agree, giving
\[
r_V:\widehat V\to\widehat K.
\]
For the actual edge groups,
\[
r_V(\overline{H_i})=\overline{\langle f\rangle},\qquad
r_V(\overline{H_j})=\overline{\langle\eta(f)\rangle}.
\tag{5}
\]
The complete marked dictionary gives
\[
\eta(f)=P f^{-1}P^{-1},\quad
P=aBfde d^{-1}f^{-1}d^{-1}.
\]
The cyclic closures in (5) have trivial intersection, with an elementary all-modulus proof. For each \(n\ge2\), map the actual free K to
\[
C_n(f)*C_2(a)
\]
by killing B,d,e. Then P maps to a and eta(f) maps to \(a f^{-1}a\). The finite subgroup \(C_n(f)\) and its conjugate by a intersect trivially by ordinary free-product normal form. This free product is residually finite, and these two subgroups are finite, so they remain the same disjoint finite subgroups in its full completion. A common element \(f^\lambda\), \(\lambda\in\widehat{\mathbb Z}\), must therefore have \(\lambda=0\pmod n\) for every n. Hence it is one. This does not invoke a centralizer theorem for arbitrary free-profinite elements.

## 5. Apply the kernel decomposition and factorwise lemma

Let
\[
N_L=\ker(\widehat R_L\to\widehat K),\qquad
N_R=\ker(\widehat R_R\to\widehat K).
\]
These are compact groups. The actual proper amalgam and its common retractions give, by (2),
\[
\ker r_V=N_L\amalg N_R.
\tag{6}
\]
Full topology of H_i and its actual compact cyclic-edge decomposition were proved in `compact_actual_edge_embedding28.md`. Applying (2) to that common cyclic retract shows that its retraction kernel is exactly the closed generated subgroup
\[
M_i=\overline{\langle E_i,B_i^0\rangle}
   \le N_L\amalg N_R,
\]
where
\[
E_i=\ker(r_L|_{\overline E_1})\le N_L,\qquad
B_i^0=\ker(r_R|_{\overline B_i})\le N_R.
\]
The notation \(B_i^0\) here denotes only this retraction kernel, not the earlier geometric orientation kernel. Similarly
\[
M_j=\overline{\langle B_j^0,E_j\rangle},
\]
with \(B_j^0\le N_L\) and \(E_j\le N_R\) the corresponding retraction kernels in \(\overline B_j\), \(\overline{p(E_1)}\).

The separately proved actual compact vertex intersections are
\[
\overline E_1\cap\overline B_j=1,
\qquad
\overline B_i\cap\overline{p(E_1)}=1.
\]
They imply
\[
E_i\cap B_j^0=1,\qquad B_i^0\cap E_j=1.
\]
Equation (3), applied in (6), therefore gives \(M_i\cap M_j=1\).

Finally any \(x\in\overline{H_i}\cap\overline{H_j}\) has trivial image under r_V by (5) and Section4, so it belongs to \(M_i\cap M_j\). Hence x=1, proving (1).

## 6. Scope and primary proof record

This proves the actual whole compact unfilled intersection, using arbitrary finite-target refinements rather than an ordinary-geodesic substitution. The proof also recovers the ordinary conclusion, but does not replace or edit the already frozen B137 geometric proof.

Trivial unshifted intersection does not imply free-product generation of the two overgroups, control every translated intersection, or prove survival after imposing either local relator family. Both initial fillings, their theta symmetry, and the actual kappa-kernel matching problem remain in force and unresolved. In particular no equality between the ordinary matching closure and the compact base kernel is asserted.

The sole new primary product input is the complete Ribes–Zalesskii2004 Theorem3.13/proof and its finite-index Lemma3.1, already independently read by all four agents and recorded in `RibesZalesskii2004_primary_audit28.md` and the separate verified BibTeX file. All finite-factor full-topology arguments used above are explicitly proved in the companion notes. No finite group census or orbit truncation was used.
