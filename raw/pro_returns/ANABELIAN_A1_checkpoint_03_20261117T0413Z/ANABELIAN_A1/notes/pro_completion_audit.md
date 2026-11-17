# Ordinary pro-reconstruction: proof development and adversarial checks

AI-produced by the configuration auditor, 17 November 2026. The complete proof is `sections/B_pro_completion.tex`, claims B.PRO1–5. These claims address B9 in the ordinary category of topoi and isomorphism classes of geometric morphisms, over the ordinary pro-base. The input is not changed to the earlier coherent relative category.

## The distinction which must remain visible

The natural field-transition map need not preserve closed points: the point T=u over F(u) maps to the generic point over F. Consequently the finite-transcendence proof B.CF1, which makes all transitions finite, does not immediately generalize. The new proof does not claim finite-stage pinning. Instead, an E-closed point is shown to have output coordinates in its residue field; that field may still be transcendental over the target field F. Projection A1_E to A1_F is a useful positive check on this distinction.

## Coherence and effectivity

At a finitely generated source stage, CHW Appendix A.8–A.9 makes the inverse-image functor representable on the qcs separated étale site. Over the reduced noetherian limit source, an isomorphism between two such étale schemes is determined on finitely many generic finite fibres, so its set is finite. Natural-isomorphism spaces are therefore compact closed subsets of products of finite sets.

One initially tempting formulation used the whole natural-isomorphism space over k. Self-review found that this was not enough to recover ordinary-pro slice comparisons: an isomorphism of an entire inverse-image functor over k need not descend to a finitely generated source field merely because one component does. The repaired statement takes the **closed closure of isomorphisms which already descend as whole functor isomorphisms**. The selected coherence is then approximable on any finite list of objects by one whole finite-stage comparison. This supplies actual ordinary-pro slice comparisons. Every finite collection of cocycle equations is solved by comparing through a common upper target representative and a common finitely generated source refinement. Compactness supplies all equations at once.

The fixed diagram of field base-change sites has its ordinary canonical associative identifications; strictifying that pre-existing diagram is harmless. It is not the same as assuming coherent data for the unknown pro-morphism.

## Why algebraically closed k does not erase the argument

It would be invalid to compare evaluated Kummer classes only after restriction to G_k: when k is algebraically closed this loses all arithmetic information. B.PRO2 instead compares **whole geometric morphisms** at a target level containing the actual output b. Its image is then a closed rational point, so the representative factors through that point's closed topos. Pro-compatibility gives equality of whole geometric morphisms after a **single** finitely generated source extension M. Pullback gives equality of all Kummer levels in the same completed multiplicative group of M. Fields M_n depending on n would not suffice.

For an arbitrary geometric point with a finitely generated field of definition L/E that is not finite, first extend k by the point's finite field of definition over k, refine the source model to L, and apply the point argument to the L-rational point. The finite extension in the point lemma is then the identity extension of the new source field.

## The completion-intersection lemma

For finitely generated characteristic-zero fields A subset B, if the image of xi in the completion of B× equals the Kummer class of an actual b in B×, then xi and b already come from A×.

Divisorial valuations on a normal projective model over the relative algebraic closure A' of A in B force b into A'. Root-closedness of A' in B gives injectivity on multiplicative completions. Norm gives d xi actual in A×. No false assertion that A× itself is finitely generated is used. Instead, d-torsion in its completion is represented by mu_d(A): inspect the component at nd and use the finite set mu_d(A). Reduction mod d and this torsion calculation show that the actual multiplicative group is saturated in its completion. The usual Kummer injectivity over finitely generated fields finishes the argument.

## Fixed source field, not objectwise unrelated fields

CHW's unit proof (Proposition 6.22, with its explicitly stated normal-source extension in Remark 4.20 and Picard finite generation in Proposition 5.22) applies to the pulled-back completed unit on the normal E-scheme. It is not applied to the original cross-field topoi map as though its source were finite type over F.

Every qcs étale slice V of the target has the fixed source model U_E=a*V. The same unit-and-coordinate construction reconstructs its point-function map over E itself. The resulting map U_E to f*V is a bijection on all geometric closed fibres after base change to k, hence an isomorphism after that base change and then already over E by faithful flatness. Natural slice point functions and reducedness make these isomorphisms natural on the whole site. Thus there is no residual phantom arising from different source extensions for different cover objects.

Finite normalization and CHW h-descent handle seminormal sources. Actual scheme maps at these stages have no topos automorphisms: all residue fields are finitely generated over Q, their induced residue-Galois images are open, and the target residue-Galois groups are slim. Thus the h-descent isomorphisms are uniquely coherent.

## Verified source inputs

- Carlson–Haine–Wolf, author PDF dated 28 July 2024, `sources/CarlsonHaineWolf2024.pdf/.txt`: Theorem 4.1, Proposition 4.8, Remark 4.20, Proposition 5.22, Proposition 5.24, Corollary 6.18, Proposition 6.22, Theorem A.8, Corollary A.9. Primary URL: https://peterjhaine.github.io/files/reconstruction_of_schemes_from_etale_topoi.pdf
- Hoshi–Tsujimura, revised author PDF, Definition 4.3 and Corollary 4.5: https://www.kurims.kyoto-u.ac.jp/~yuichiro/rims1962revised.pdf
- Stacks Lemma 59.51.2, Tag 0EYL, opened in full: https://stacks.math.columbia.edu/tag/0EYL
- Stacks Lemma 32.10.1, Tag 01ZM, opened in full: https://stacks.math.columbia.edu/tag/01ZM
- Stacks Lemma 32.4.2, Tag 0CUF, already checked for the underlying inverse-limit spaces: https://stacks.math.columbia.edu/tag/0CUF

## Review status at 03:12 UTC

Root read B.PRO1–5 independently and reported a favorable audit. The literature auditor independently reported favorably on B.PRO1–2. The criterion auditor is checking B.PRO3–5. The configuration auditor made the closure-of-descending-comparisons repair before that review and has explicitly checked the single-field Kummer comparison, completion saturation, normal-source reduction, fixed-E site naturality, and finite normalization descent.

The old B.CF3 open statement and its metadata have been updated to reference the completed B.PRO5 proof. The earlier finite-transcendence proof remains a simpler special case.

### Post-checkpoint clarification (03:15 UTC)
B.PRO4 now explicitly invokes h-separatedness (CHW Theorem 4.1) to descend equality from the normalization of the reduced normalization relation to its absolute weak normalization before applying the h-sheaf equalizer. This is an exposition clarification, independently requested by the criterion reviewer.
