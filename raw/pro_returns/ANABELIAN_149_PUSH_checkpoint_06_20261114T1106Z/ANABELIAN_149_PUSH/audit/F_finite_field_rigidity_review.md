# Closing the nonconstant solvable-field test

**Prepared by:** finite-field agent; independent review of the last F2 step.  
**Date:** 14 November 2026.  
**Scope:** the corrected, closed-point-preserving meaning of “pinned.” The relative-only statement already refuted in F.17 is unaffected.

## Result and dependencies

Put \(k=\mathbb Q^{\mathrm{solv}}\), inside a fixed algebraic closure of \(\mathbb Q\). Combining the point-function theorem F.19 with the arguments below proves:

> Every closed-point-preserving geometric endomorphism of \((\mathbb G_{m,k})_{\mathrm{et}}\) over \(BG_k\) is isomorphic, over \(BG_k\), to the étale-topos morphism of exactly one algebraic map \(t\mapsto ct^m\), where \(c\in k^\times\) and \(m\in\mathbb Z\). It is nonconstant exactly when \(m\ne0\).

The case \(m=0\) is already completely proved in F.19. For \(m\ne0\), F.19 gives equality on **geometric closed points** with the finite étale map \(f(t)=ct^m\). Three further statements finish the proof:

1. Every finite quotient of the fundamental group of an open rational curve over \(k\) is the full image of a closed-point decomposition group.
2. Applying that statement to the **joint image** of two finite representations upgrades equality of geometric closed-point maps to a single relative isomorphism on generic finite étale objects.
3. On normal curves in characteristic zero, a geometric morphism which agrees generically with a finite étale algebraic map agrees with it on the entire small étale topos.

The third statement treats arbitrary separated étale charts, including charts with arbitrary genus and partly ramified completions. No vanishing assertion about their Picard Tate modules is used. No Hilbertianity assertion about \(k\) is used: Hilbert irreducibility is applied only over a number field.

## 1. Closed points detecting any finite quotient

### 1.1 Statement

Let \(U\subset\mathbb A^1_k\) be a nonempty open subscheme, and let
\[
 \rho:\pi_1(U)\twoheadrightarrow G
\]
be a continuous surjection to a finite group. For every integer \(n\ge5\), there is a closed point \(x\in U\), of degree \(n\) over \(k\), for which the composite
\[
 G_{k(x)}\longrightarrow\pi_1(U)\longrightarrow G
\]
is surjective. As usual, this statement is independent of choices of geometric paths because surjectivity is invariant under conjugation.

### 1.2 Descent and the arithmetic constant quotient

Let \(Y\to U\) be the connected finite étale \(G\)-torsor corresponding to \(\rho\). Descend its equations, its \(G\)-action, and the torsor isomorphism to a finite Galois solvable number field \(F/\mathbb Q\) contained in \(k\). Denote the descended cover again by \(Y\to U\). It is connected, because its base change to \(k\) is connected. Let \(M\) be the algebraic closure of \(F\) in \(F(Y)\). Then \(M/F\) is finite Galois, and
\[
 1\longrightarrow N\longrightarrow G\longrightarrow
 P:=\operatorname{Gal}(M/F)\longrightarrow1
\]
is the arithmetic/geometric constant exact sequence of this descended cover.

Because \(Y_k\) remains connected, \(M\) and \(k\) are linearly disjoint over \(F\), equivalently \(M\cap k=F\). Here both \(M/F\) and \(k/F\) are Galois.

We have \(F^{\mathrm{solv}}=k\). Indeed, a finite solvable Galois extension of \(F\) has solvable normal closure over \(\mathbb Q\): its conjugates over \(\mathbb Q\) have a compositum whose Galois group over \(F\) embeds into a finite product of solvable groups, and the quotient over \(\mathbb Q\) is the solvable group \(\operatorname{Gal}(F/\mathbb Q)\). The reverse inclusion follows from the definition of \(k\). Thus every finite solvable Galois extension of \(F\) lies in \(k\).

Consequently \(P\) has no nontrivial solvable quotient. Its abelianization is therefore trivial, so \(P\) is perfect. This includes the case \(P=1\).

### 1.3 The common-constant wreath cover

Form the ordered fibre product
\[
 Y\times_M\cdots\times_M Y
\]
with \(n\) factors, and restrict to the open subset \(T\) on which the \(n\) images in \(U\) are pairwise distinct. Each factor is geometrically integral over \(M\), so this product and its nonempty open \(T\) are geometrically integral over \(M\), and hence connected over \(F\).

The map from \(T\) to the unordered configuration space
\[
 B=\operatorname{Sym}^n(U)_{\mathrm{dist}}
\]
is a connected finite étale Galois cover with group
\[
 H=\bigl(G\times_PG\times_P\cdots\times_PG\bigr)\rtimes S_n. \tag{1}
\]
The fibre product condition means that the \(n\) coordinate automorphisms induce the same automorphism of \(M\). Permuting the ordered factors gives the literal subgroup \(S_n\). These automorphisms act freely and transitively on every geometric fibre over an unordered configuration, establishing (1).

**The source is not quotiented by \(S_n\).** Quotienting the source first would usually produce a non-Galois cover of smaller degree. The unquotiented ordered source has the stated Galois group.

Since \(U\) is an open of the affine line, \(B\) is a nonempty open of \(\mathbb A^n_F\), using the coefficients of the monic polynomial whose roots are the configuration. Hilbert irreducibility over the number field \(F\) gives a point of \(B(F)\) with a connected \(H\)-torsor fibre. Thus its residue algebra is a Galois extension \(\Omega/F\) with Galois group \(H\). The needed source statements are Serre (2007), Proposition 3.3.1 and Theorem 3.4.1, printed pp. 23 and 25. Proposition 3.3.1 only requires an irreducible cover; geometric irreducibility of the total space over \(F\) is not an additional hypothesis. The constants \(M\) therefore cause no problem.

### 1.4 What remains after passing to \(k\)

For a finite group \(H\), let \(H^\infty\) be the stable term of its derived series. The fixed field \(\Omega^{H^\infty}\) is the maximal solvable Galois subextension of \(\Omega/F\). Since \(k=F^{\mathrm{solv}}\),
\[
 \Omega\cap k=\Omega^{H^\infty},\qquad
 \operatorname{Gal}(\Omega k/k)=H^\infty. \tag{2}
\]

We claim that the stabilizer of any coordinate in \(H^\infty\) maps onto the entire coordinate group \(G\). In fact the kernel of the permutation map already does so.

First, \(A_n\) is a perfect literal subgroup of \(H\), so
\[
 A_n\subset H^\infty.
\]
Second, \(H^\infty\to P\) is surjective: the image of every derived term of \(H\) is the corresponding derived term of the perfect group \(P\). For any \(h\in H^\infty\), its permutation lies in \(A_n\). Multiplication by the inverse literal permutation removes that permutation without altering its image in \(P\). Therefore
\[
 B_0:=H^\infty\cap\ker(H\to S_n)
\]
still surjects onto \(P\).

Third, \([N^n,A_n]\subset B_0\). The projection of this commutator subgroup onto any chosen coordinate contains every element of \(N\): put a given \(a\in N\) in that coordinate and take its commutator with an even permutation moving that coordinate elsewhere. In the chosen coordinate the commutator is \(a\) or \(a^{-1}\), according to the commutator convention. Thus the projection \(B_0\to G\) contains \(N\) and surjects onto \(G/N=P\), and is therefore surjective.

The projection of \(H^\infty\) onto \(S_n\) is \(A_n\), which is transitive. Accordingly, the specialized unordered configuration gives, after base change to \(k\), one closed point \(x\) of degree \(n\). The stabilizer of a selected coordinate is the Galois group over \(k(x)\) inside \(\Omega k\). Its projection to that coordinate's \(G\)-torsor is onto \(G\), by the preceding paragraph. This is precisely the asserted surjectivity of \(G_{k(x)}\to G\).

This proves the detection statement, including arithmetic finite quotients.

## 2. From point values to one relative generic isomorphism

Let \(X=Y=\mathbb G_{m,k}\), let \(f(t)=ct^m\) with \(m\ne0\), and let \(\phi:X_{\mathrm{et}}\to Y_{\mathrm{et}}\) be relative over \(BG_k\) and agree with \(f\) on every geometric closed point.

The generic point also maps to the generic point: otherwise its image is closed, and continuity makes the whole point map constant. Thus the underlying topological maps agree. In particular, for every nonempty open \(V\subset Y\),
\[
 \phi^{-1}(V)=f^{-1}(V)=:U.
\]
The domain \(U\) is again an open rational curve.

### 2.1 The generic functor exists without an unproved factorization principle

A finite separable algebra over \(k(Y)\) spreads to a finite étale cover over some nonempty open \(V\). Pull it back along the restriction of \(\phi\) to \(U\), and take its generic fibre. Shrinking \(V\) further does not change that generic fibre. This defines a functor on finite étale generic algebras, naturally compatible with generic restriction of every étale chart. It preserves finite limits, finite coproducts, and covers, and hence gives a continuous generic Galois homomorphism. This construction does not assume that every generic-valued topos morphism has an unexplained universal factorization through a field topos.

Choose generic fibre functors and paths respecting the specified identification on constants. We get continuous maps over \(G_k\)
\[
 h_\phi,h_f:G_{k(X)}\longrightarrow G_{k(Y)}.
\]
For any finite quotient \(q:G_{k(Y)}\twoheadrightarrow Q\), choose an open \(V\) over which the corresponding cover is finite étale. Both \(q h_\phi\) and \(q h_f\) factor through \(\pi_1(U)\).

### 2.2 Closed-point restrictions are conjugate as whole homomorphisms

For a geometric closed point \(\bar x\) with residue field \(L=k(x)\), the two composites from \(\operatorname{Spec}L_{\mathrm{et}}\) to \(Y_{\mathrm{et}}\) are isomorphic **over \(BG_k\)**. To see this, each factors through its closed image point. The residue field of that image is finite separable over \(k\); its étale topos is the slice of \(BG_k\) classified by that finite étale field. Relative morphisms from \(\operatorname{Spec}L_{\mathrm{et}}\) to this slice are exactly the associated \(k\)-embeddings into \(L\). Equality of geometric point values says that these embeddings are the same. This is also the elementary field-source reconstruction used in F.16.

Thus the restrictions of the two fundamental-group homomorphisms to \(G_L\) are conjugate by **one** element, not merely element by element. With the paths chosen over the same geometric point of \(\operatorname{Spec}k\), this conjugator lies in the geometric target group. The relative condition supplies the identification on constants; no assertion about the centre of \(G_k\) is required.

### 2.3 The joint-image argument

Form the finite joint image
\[
 J=\operatorname{im}\bigl(qh_\phi,qh_f:\pi_1(U)\to Q\times Q\bigr).
\]
Section 1 supplies a closed point \(x\in U\) whose decomposition group surjects onto \(J\). Section 2.2 supplies an element \(a_Q\) in the image of the geometric target group in \(Q\) which conjugates the two restrictions on that entire decomposition group. Surjectivity onto \(J\) then gives
\[
 qh_\phi=\operatorname{Int}(a_Q)\,qh_f
\]
on the entire generic source group. The joint-image quotient is essential: testing covers separately without it would not justify a simultaneous conjugator.

Let \(\Gamma^{\mathrm{geom}}=G_{\overline k(Y)}\), a compact profinite group, and let
\[
 C_Q=\{a\in\Gamma^{\mathrm{geom}}:
 qh_\phi=\operatorname{Int}(q(a))\,qh_f\}.
\]
Every \(C_Q\) is closed and nonempty. The quotient by the intersection of finitely many kernels refines the corresponding finite quotients, so the family \(\{C_Q\}\) has the finite-intersection property. Compactness gives a single
\[
 a\in\bigcap_Q C_Q.
\]
It conjugates the two generic homomorphisms on all finite quotients. Because \(a\) is geometric, the resulting natural isomorphism of generic finite étale pullback functors respects \(BG_k\).

## 3. Generic agreement with a finite étale map determines the full topos

### 3.1 General rigidity statement

Let \(X,Y\) be smooth connected finite-type curves over a characteristic-zero field, let \(f:X\to Y\) be finite étale, and let \(\psi:X_{\mathrm{et}}\to Y_{\mathrm{et}}\) be a geometric morphism taking the generic point to the generic point. Suppose its generic finite étale pullback functor is equipped with a natural isomorphism to that of \(f\). Then \(\psi\) is isomorphic to \(f_{\mathrm{et}}\). If the generic isomorphism respects an identified base-field topos, the full isomorphism does too.

It is enough for the application to assume additionally that the underlying point maps agree, which has already been proved in Section 2. The proof below also explains why generic agreement itself forces that equality.

### 3.2 Representability and normalization

By Carlson, Haine, and Wolf (2024), Corollary A.9, every geometric morphism between these topoi sends quasicompact separated étale charts to quasicompact separated étale schemes. The source is topologically noetherian and the target is qcqs, exactly as required there. No separate coherence hypothesis is imposed.

By SGA 1, Exposé I, Proposition 10.1, a separated étale chart over a normal curve is an open subscheme of the normalization in its generic finite separable algebra. The normalization is finite here because a finite-type curve over a field is excellent. Quasicompactness leaves only finitely many components. A prescribed generic identification determines this open embedding uniquely.

Let \(A\) be a finite separable \(k(Y)\)-algebra, let \(S\to Y\) be its finite normalization, and let
\[
 Z=S^{\mathrm{et}}
\]
be its maximal étale locus. Since \(f\) is étale, \(f^*S\) is normal and is the normalization of \(X\) in the generic algebra \(k(X)\otimes_{k(Y)}A\). Moreover, étaleness is local for the étale topology on the base, so
\[
 (f^*S)^{\mathrm{et}}=f^*Z. \tag{3}
\]
The generic comparison and the preceding normalization fact identify \(\psi^*Z\) with an open subscheme of \(f^*S\). Since \(\psi^*Z\to X\) is étale, (3) gives a canonical open inclusion
\[
 \psi^*Z\hookrightarrow f^*Z. \tag{4}
\]

### 3.3 Ramification detects any discrepancy of point maps

Suppose a closed point \(x\in X\) has \(\psi(x)=y'\ne y:=f(x)\). If \(y'\) is closed, choose \(h\in k(Y)^\times\) with
\[
 v_y(h)=1,\qquad v_{y'}(h)=0.
\]
If \(y'\) is generic, only the first condition is needed. Such an \(h\) exists by approximation for the two discrete valuations; equivalently use Riemann–Roch on a smooth proper completion to prescribe the first jet at \(y\) and a nonzero value at \(y'\), with a sufficiently large pole divisor elsewhere.

The quadratic extension \(k(Y)(\sqrt h)\) is totally ramified at \(y\). It is unramified at \(y'\) when \(y'\) is closed, since \(h\) is a unit there and 2 is invertible. Let \(Z\) be the maximal étale locus of its normalization. Then its geometric fibre at \(y\) is empty, while its geometric fibre at \(y'\) is nonempty. By (4), the geometric fibre of \(\psi^*Z\) at \(x\) must be empty, because that of \(f^*Z\) is empty. The stalk formula for inverse image says instead that it is the nonempty geometric fibre of \(Z\) at \(\psi(x)=y'\). This contradiction proves \(\psi(x)=f(x)\).

The generic point is fixed as prescribed by the generic comparison. Hence the underlying point maps agree. This also rules out a closed point being sent to the generic point; a closed-point-preservation assumption is not needed in this rigidity statement.

### 3.4 Maximal étale loci are fixed canonically

For a general \(Z=S^{\mathrm{et}}\), inclusion (4) is an equality. Indeed, at every geometric closed point \(\bar x\) the point-map equality and the stalk formula give
\[
 |(\psi^*Z)_{\bar x}|=|Z_{\psi(\bar x)}|
 =|Z_{f(\bar x)}|=|(f^*Z)_{\bar x}|.
\]
Only equality of the underlying image point is required for the middle equality of cardinalities. The geometric fibres are finite. An inclusion between them of equal cardinality is onto. The generic fibres also agree by construction, so the open subschemes in (4) are equal. This produces a canonical isomorphism
\[
 \psi^*Z\simeq f^*Z
\]
extending the specified generic isomorphism.

### 3.5 Slicing recovers all open subobjects, including partly ramified charts

Use this isomorphism to form the sliced morphism
\[
 \psi_Z:(f^*Z)_{\mathrm{et}}\longrightarrow Z_{\mathrm{et}}.
\]
It has the same generic functor as the finite étale algebraic map
\[
 f_Z:f^*Z\longrightarrow Z.
\]
Apply the argument of Section 3.3 to these curves. It gives equality of the underlying point maps of \(\psi_Z\) and \(f_Z\). If the curves are disconnected, their finitely many clopen components are preserved according to their generic supports. One applies the argument on each relevant connected component; a clopen subset is determined by which generic points it contains.

Every open subobject \(V\subset Z\) consequently has the same inverse-image open subobject under \(\psi_Z\) and \(f_Z\). Every quasicompact separated étale chart \(V\to Y\) is such an open in the maximal étale locus of its finite normalization. Therefore
\[
 \psi^*V\simeq f^*V
\]
for every chart in the quasicompact separated étale site. These isomorphisms extend the fixed generic comparison.

This is the step that cannot be replaced by claiming that finite étale covers of Zariski opens alone generate the small étale site. Partly ramified completions can have both ramified and unramified points over one base point; taking the maximal étale locus and then all its open subobjects handles exactly that issue.

### 3.6 Naturality and the relative identification

For a morphism \(V\to V'\) of such charts, the two maps obtained from the canonical identifications agree on generic fibres. The source is reduced with dense generic points, and the target is separated over \(X\). Thus the maps agree everywhere: their equalizer is closed and contains all generic points, so its defining ideal is zero on the reduced source. Hence the chart identifications form a natural isomorphism.

The quasicompact separated étale site is a basis for the small étale topology (Carlson et al., 2024, Lemma A.4). Inverse-image functors preserve colimits, so a natural isomorphism on this generating site extends to a natural isomorphism on all sheaves. Equivalently use their Corollary A.11, which identifies the groupoids of these site morphisms and topos morphisms.

Finally, if the generic comparison respects \(BG_k\), so does the full comparison. This is true on finite constant étale objects by the generic construction and uniqueness; arbitrary discrete continuous \(G_k\)-sets are coproducts of finite transitive ones. Thus the resulting isomorphism is an isomorphism of relative geometric morphisms, with the given pinning.

## 4. Application to F2 and exact limitations

By F.19, a nonconstant closed-point-preserving relative endomorphism of \((\mathbb G_{m,k})_{\mathrm{et}}\) agrees on geometric closed points with \(f(t)=ct^m\), \(m\ne0\). Section 2 gives a relative generic isomorphism, and Section 3 extends it to the entire étale topos. The constant case is already handled by F.19. Uniqueness follows at once from the point functions, or from the known injectivity statement for algebraic morphisms.

Accordingly, the **corrected F2 endomorphism test is proved**. The relative-only statement of F.17 remains refuted. This argument does not assert the full étale reconstruction property of \(\mathbb Q^{\mathrm{solv}}\) for all finite-type schemes. The rational source is used in the Hilbert configuration argument and in F.18–F.19; a general source has not been substituted without proof.

The proof uses full finite groups and all finite-extension closed points. It supplies no statement that \(k\)-rational points, pro-\(\ell\) quotients, or Kummer classes alone detect arbitrary covers.

## 5. Source audit and exact locations

All following primary sources were opened, not inferred from secondary summaries. No source is quoted verbatim here.

- Carlson, M., Haine, P. J., & Wolf, S. (2024). *Reconstruction of schemes from their étale topoi*. arXiv:2407.19920. https://arxiv.org/abs/2407.19920. Appendix A: Lemma A.4 (qc separated étale basis), Theorem A.8 (representable pullbacks), Corollary A.9 (automatic coherence and site realization for noetherian source), and Corollary A.11 (equivalence of morphism groupoids). Corollary A.9 is on printed pp. 36–37, PDF pages 36–37 counting the first page as 1. Supplied source: `tmp/CHW/reconstruction_of_schemes_from_etale_topoi.tex`, approximately lines 2835–2965. Opened PDF: https://arxiv.org/pdf/2407.19920; root-readable web references from this review are `turn203view0`, `turn204view2`, and `turn204view3`.
- Grothendieck, A. (1971). *Revêtements étales et groupe fondamental (SGA 1)* (Lecture Notes in Mathematics, Vol. 224). Springer. Exposé I, Proposition 10.1, printed p. 21, identifies separated étale charts over a normal connected base with opens of the normalization in their generic algebra. The complete supplied source is `background/literature/SGA1/src_arXiv_math_0206203/smf_doc-math_3_01.tex`, lines 2028–2050. Its isolated occurrence of “normalisé de X” in the component sentence is a typographic slip: the immediately following parenthesis correctly states normalization of Y. The proof here uses normalization of the base Y.
- Serre, J.-P. (2007). *Topics in Galois theory* (2nd ed.; notes by H. Darmon). A K Peters. Proposition 3.3.1, printed p. 23 / zero-based PDF page 39, gives full-group specialization outside a thin set for an irreducible Galois cover. Theorem 3.4.1, printed p. 25 / zero-based PDF page 41, gives the Hilbert property for affine space over a number field. The geometric-irreducibility assumption appearing later in Proposition 3.3.3 is not needed in Proposition 3.3.1. Opened primary PDF: https://indico.math.cnrs.fr/event/11410/attachments/4760/7351/SerreTopicsGaloisTheory.pdf; web references `turn203view1`, `turn204view0`, and `turn204view1`.

## 6. Independent-review record

- Root independently checked the perfect-residual group argument, the arithmetic constant quotient, and the joint-image step.
- Topos independently checked the ordered common-constant cover, the distinction between its Galois cover and its quotient by \(S_n\), the geometric relative conjugators, and the compactness argument.
- Root and topos independently checked the normalization, ramification, fibre-cardinality, and slice argument. The direct finite-étale version above follows root's suggested formulation, avoiding any choice of an \(m\)-th-root lift through \(f\).
- This note does not modify `sections/F.tex`, its ledger, or the settled Part-A files; the root/topos owner will integrate the final statement and update the former unresolved status of F.9.
