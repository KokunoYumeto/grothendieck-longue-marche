# A full profinite boundary-power criterion from actual finite covers

Checkpoint35 research, separate from all frozen formal sources. This is a conditional theorem about the exact boundary equation in `actual_elliptic_original_cusp_bridge35.md` (ec8fef231a71e2329ed2cfbdedaafe90055dce8a45a2ef77aa428eb1a85eadde). It supplies no proof that the canonical candidate satisfies that equation.

## 1. Statement

Let E be the free profinite group on X,Y, and let K=[Y,X]. If a continuous endomorphism eta of E satisfies

\[
 \eta(K)=K^d,\qquad d\in\widehat{\mathbb Z}^{\times},       \tag{1}
\]

then eta is an automorphism. The proof uses actual finite covers of the discrete once-punctured torus, not an identification of arbitrary closed subgroups with discrete surface completions.

## 2. The finite-cover homology fact, with the topology retained

Identify the discrete free group F=F(X,Y) with the fundamental group of a compact orientable once-punctured torus S, choosing orientation and a boundary whisker so that its boundary word is K (reversing orientation if necessary).

Let V be a proper open subgroup of E containing K, and put V0=V intersect F. The dense map from F to the finite coset set E/V shows that V0 has the same finite index n=[E:V]>1. Its connected n-sheeted cover S0 of S is a compact orientable surface with boundary.

The boundary components of S0 correspond to the orbits of K on the n cosets. The degree of a component over the original boundary is the size of its orbit. Since K belongs to V0, the base coset is a singleton orbit. It corresponds to a degree-one boundary component whose based word is K. Since n>1, there is at least one further orbit, and therefore at least two boundary components.

For a connected compact orientable surface of genus g with b boundary components, its elementary polygon presentation is

\[
 \left\langle a_1,b_1,\ldots,a_g,b_g,c_1,\ldots,c_b
 \ \middle|\ \prod_{j=1}^g[a_j,b_j]c_1\cdots c_b=1\right\rangle,
\]

where the c_i are the boundary loops with whiskers. This presentation is obtained by cutting along arcs joining all boundary components and the usual handle arcs to one polygon. Abelianizing gives a free abelian group on the handle classes and the b boundary classes, with the single boundary relation c_1+...+c_b=0. When b>=2, each individual boundary class is nonzero and primitive. In particular the class of K is nonzero in (V0)_ab.

There is no completion-topology assumption here. Every finite-index subgroup of V0 is also finite-index in F, and its core in F is finite-index and normal. Hence the full profinite topology of V0 is precisely the topology induced from F. Its completion is the actual open subgroup V of E. Abelianization commutes with this completion, either by the universal finite-abelian quotient property or by the explicit free basis of V0. Consequently

\[
 V_{\rm ab}\simeq\widehat{(V0)_{\rm ab}}
             \simeq\widehat{\mathbb Z}^{\,2g+b-1},
\]

and the nonzero integral primitive boundary class [K] remains nonzero there.

## 3. Surjectivity and injectivity of the actual endomorphism

The image H=eta(E) is compact, hence closed. Equation (1) and the unit condition imply K belongs to H: the continuous procyclic power operation gives K=(K^d)^(d^{-1}).

If H were proper, choose t outside H. Compactness and finite separation give an open normal subgroup U of E such that t does not belong to HU. Then V=HU is a proper open subgroup containing H, and therefore containing K. The finite-cover fact in section2 applies to this actual V.

Both eta(X) and eta(Y) lie in V, so

\[
 K^d=[\eta(Y),\eta(X)]\in\overline{[V,V]}.
\]

Its image in V_ab is d[K]=0. Multiplication by the unit d is an automorphism of the free profinite abelian group V_ab. This contradicts [K] nonzero. Therefore H=E and eta is surjective.

For clarity, the usual Hopfian step is elementary here. In a finitely generated profinite group there are finitely many open normal subgroups of each given index. A surjective continuous endomorphism induces an injective map on this finite set by inverse image, preserving the index, hence a permutation. For every open normal subgroup M there is consequently an open normal subgroup M' with eta^{-1}(M')=M. Every element of ker(eta) lies in all such M, hence is one. Thus eta is injective and is an automorphism.

## 4. Exact application and limits

In the preceding elliptic bridge, eta(X)=xi and eta(Y)=omega, and the missing boundary equation is precisely

\[
 [\omega,\xi]=K^d.
\]

Since the actual canonical d is a full profinite unit, this equation, **if proved**, forces eta to be an automorphism of the entire free profinite group E. Combined with the already proved exact identity Theta eta=eta c_ell if and only if this boundary equation holds, it would then give genuine conjugacy of these elliptic involutions.

The boundary equation remains unproved. This conditional automorphy result does not establish the original H_d=1, the original CM sign, all defining elliptic relations for (d,u), or an elliptic action for the GT0 lift Gamma. It is also not a transfer from automorphy on all maximal pro-p quotients.

## 5. Source audit and proof status

The surface calculation above is supplied in full through the actual finite cover and its polygon presentation. No general test-word transfer theorem is needed. The primary source for the preceding elliptic candidate and its completion conventions remains Enriquez (2014), *Elliptic associators*, Proposition2.20, https://doi.org/10.1007/s00029-013-0137-3; its entire proof and exact scope were read and bound in the predecessor notes.

A separate search found Singh (2025), *A note on words having the same image on finite groups*, Bulletin of the London Mathematical Society,57(10),3181–3193, https://doi.org/10.1112/blms.70150, author version https://arxiv.org/pdf/2407.00789 (v2,27February2026). Its entire section3/Proposition3.4 proof, printed pp.9–10, was read. That proof's converse asserts that the intersection of a profinite retract with the discrete free group is a discrete retract, without showing that the given retraction preserves that discrete group. We do not use that unverified step or claim a counterexample to its theorem. The finite-cover argument in sections2–3 establishes exactly the boundary criterion needed here independently.

This is a complete symbolic proof. There is no finite target census, numerical producer, new rendering, or formal promotion. Independent conversation review of the finite-cover argument by CE passed before this source was saved; the saved bytes are submitted separately for full review.
