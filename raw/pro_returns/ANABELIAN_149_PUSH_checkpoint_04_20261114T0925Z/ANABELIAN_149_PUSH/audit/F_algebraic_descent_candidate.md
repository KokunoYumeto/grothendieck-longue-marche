# Algebraic descent of étale reconstruction

Status: complete candidate proof, awaiting independent root review. The integrated files through F.31 remain frozen for checkpoint04.

## Statement

Let K/k be an algebraic extension of characteristic-zero fields. If K satisfies étale reconstruction in the actual Carlson–Haine–Wolf closed-point-preserving sense, then k satisfies it as well. Neither finiteness nor normality of K/k is required.

Consequently F.31 extends to every characteristic-zero field that embeds in a finite extension of Qsolv. In particular it extends to every subfield of Qsolv. This still gives a sufficient field class, not an intrinsic classification of all reconstruction fields.

## 1. Base change of a pinned geometric morphism along algebraic constants

Let X and Y be finite-type k-schemes and let phi:X_et -> Y_et be a geometric morphism relative to BG_k. For every finite subextension E/k of K/k, the finite étale scheme Spec(E) represents an object of BG_k. The relative structure identifies phi*(Y_E) with X_E. Slicing phi at this object gives a geometric morphism

    phi_E:(X_E)_et -> (Y_E)_et

over BG_E. This uses the canonical equivalence of an étale scheme's small topos with the corresponding slice. The slice construction is compatible, with its canonical associativity isomorphisms, with every inclusion E subset E' inside K.

Write C(Z) for the category of quasicompact separated étale Z-schemes, with the étale topology. For finite-type schemes over a field, CHW Lemma A.4 makes this a basis, and Theorem A.8/Corollary A.9 show that every inverse-image functor phi_E* carries C(Y_E) into C(X_E). This is stronger than preservation of constructible sheaves. The precise proof of Theorem A.8 takes the complementary clopen to the diagonal V -> V x V. Inverse image preserves the resulting coproduct decomposition V disjoint_union Vprime = V x V. The representing étale algebraic space U therefore has a closed diagonal, so U is separated; the locally quasi-finite separated algebraic-space criterion (Stacks 03XX) then makes U a scheme. Coherence supplies quasicompactness. Thus nonseparated constructible objects do not invalidate the stated basis. The resulting functors preserve terminal objects, fibre products and finite covering families. Finite-stage compatibility is not an unsupported base-change theorem for arbitrary geometric morphisms: it follows directly from taking successive slices of the original relative morphism. In particular, for V in C(Y_E),

    phi_E'*(V x_E E') = phi_E*(V) x_E E'.

All schemes X_E and Y_E are quasicompact and quasiseparated. The categories C(X_K) and C(Y_K) are the filtered 2-colimits of their corresponding finite-stage categories. Indeed, schemes of finite presentation, their morphisms, and finite collections of equations among those morphisms descend to a finite stage; the étale and separated predicates descend after increasing the stage. Covering families may be chosen finite and their surjectivity descends. The precise affine-site statement is Stacks Lemma 59.51.2, Tag 0EYL; its proof invokes Lemma 32.10.1 for categories of finitely presented schemes and the étale/surjectivity limit lemmas. Passing from the affine basis to C(Z) is legitimate by the same finite-presentation descent, or by a finite affine covering and its overlap data.

Thus the compatible phi_E* define a functor

    u:C(Y_K) -> C(X_K).

Every finite-limit diagram and every finite cover can be represented at one finite stage. Therefore u preserves finite limits and covers. Stacks Proposition 7.14.7, Tag 00X6, gives the induced geometric morphism

    phi_K:(X_K)_et -> (Y_K)_et.

Its relative structure over BG_K is inherited on finite étale K-schemes, each of which descends to a finite stage. The construction is compatible with the projection to phi, with further algebraic scalar extension, and with geometric points. It supplies precisely the scalar extension needed here; no unsourced assertion that arbitrary small étale topoi preserve every scheme fibre product is required.

If phi is pinned, so is phi_K. Let x_K be a closed point of X_K and x its image in X. The extension kappa(x_K)/K is finite, and K/k is algebraic. Hence kappa(x)/k is algebraic; since X is finite type, x is closed. The commuting diagram of topoi implies that the image y_K=|phi_K|(x_K) lies over the closed point y=|phi|(x). The fibre of Y_K -> Y over y is Spec(kappa(y) tensor_k K), a finite K-scheme. Consequently y_K is closed. This argument also proves pinning at every finite stage.

Choose one algebraic closure kbar containing K. For x in X(kbar), field-source reconstruction (CHW Proposition 3.6) identifies the composite of phi with x_et with the actual point phi(kbar)(x). Forgetting from BG_K to BG_k shows

    phi_K(kbar)(x) = phi(kbar)(x).

Here we identify (X_K)(kbar) with X(kbar) using the fixed embedding K subset kbar. The relative structure is essential for this equality and has been retained at every slice.

## 2. Descent of the reconstructed unit

We verify CHW Theorem 4.18(5) over k. Let X=Spec(A) be regular, connected, affine and of finite type over k, with a k-rational point, and let phi:X_et -> Gm_k,et be pinned and relative. In characteristic zero X is smooth; its rational point and connectedness imply geometric connectedness. Therefore X_K is regular connected affine with a K-rational point.

By the preceding construction phi_K is a pinned relative morphism. Reconstruction over K provides a unit h_K in (A tensor_k K)* whose geometric-point function equals phi_K(kbar), hence equals q=phi(kbar).

The relative morphism phi defines a G_k-equivariant point function q. Let h_bar be the image of h_K in A tensor_k kbar. For every sigma in G_k, the functions sigma(h_bar) and h_bar have the same values on X(kbar), because q is equivariant. A reduced affine finite-type scheme over an algebraically closed field has its regular functions determined by its closed-point values. Thus sigma(h_bar)=h_bar for all sigma.

The invariant ring (A tensor_k kbar)^{G_k} is A. This is also immediate without a general descent theorem: write h_bar as a finite linear combination of k-linearly independent elements of A with coefficients in kbar. Invariance makes all coefficients fixed by G_k, hence elements of k. The inverse h_bar^{-1} is invariant as well. Consequently h_bar comes from a unit h in A*, and h has point function q.

This is precisely CHW Theorem 4.18(5); Theorem 4.18 proves the full all-scheme reconstruction property over k. This proof does not descend an arbitrary natural isomorphism of topoi or assume that point equality alone forces full-topos equality. It descends the regular unit required by the exact CHW criterion, and then uses that theorem for the all-scheme conclusion.

No Galois hypothesis on K/k was used. Even when sigma(K) is not K, sigma(h_bar) is well defined in A tensor_k kbar, and its equality with h_bar follows from the original G_k-equivariant point function.

## 3. Application to F.31 and scope

If k embeds in a finite extension L of Qsolv, then L/k is algebraic and F.31 proves reconstruction over L. The preceding theorem proves reconstruction over k. Every subfield of Qsolv is an immediate special case. More generally, every algebraic k/Q for which k Qsolv is finite over Qsolv belongs to this class, and this formulation is equivalent after choosing the embedding in Qbar.

This says nothing about all subfields of a transcendental extension of Qsolv. Extending to that class would require further work on arithmetic equivariance and integrality over finitely generated fields. It also does not turn the sufficient field class into the intrinsic necessary-and-sufficient classification requested in F.9.

## Opened primary sources

- Carlson–Haine–Wolf, supplied arXiv:2407.19920 source: Proposition 3.6 (field-source reconstruction); Theorem 4.18 and its entire proof; Appendix A, Lemma A.4, Theorem A.8 and Corollary A.9. Already opened and used in F.21–F.31.
- The Stacks Project, Lemma 59.51.2, Tag 0EYL, https://stacks.math.columbia.edu/tag/0EYL, opened 2026-11-14: the affine small étale site of an affine-transition inverse limit is the filtered colimit of the finite-stage sites, including descent of coverings. Its proof expressly references finite-presentation descent and descent of the étale/surjective properties.
- The Stacks Project, Proposition 7.14.7, Tag 00X6, https://stacks.math.columbia.edu/tag/00X6, opened 2026-11-14: a continuous finite-limit-preserving functor induces a geometric morphism.
- The Stacks Project, Lemma 32.10.1, Tag 01ZM, https://stacks.math.columbia.edu/tag/01ZM, opened 2026-11-14: filtered descent of categories of schemes of finite presentation.
- The Stacks Project, Lemma 7.28.2, Tag 03EF, https://stacks.math.columbia.edu/tag/03EF, opened 2026-11-14: localization of site morphisms, compatible with geometric-morphism slices.
