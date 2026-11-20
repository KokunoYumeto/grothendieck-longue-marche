# Internal checks prompted by 123/040

No outside source or unprovided section was consulted. The witness text identifies the claims to examine; the source glyphs will be settled independently by the three readers and root crops. These arguments do not authorize correcting the manuscript.

## Inverse image and explicit algebraic constructions

Let L:E→F preserve finite limits and small colimits, as the excerpt assumes of an inverse-image functor. The earlier check for 123/028 established preservation of finite-product operations/equations, and the limit/colimit comparison principle. Here the application to free objects and tensor products can be made more concrete.

For the free group on an object X of a topos, start from the coproduct of finite words in X plus a formal inverse copy of X. Impose, by a coequalizer equivalence relation, the elementary cancellation and unit relations. All stages use finite products, finite coproducts, the coproduct over finite word lengths, and coequalizers. A functor preserving finite limits and small colimits transports that construction and its universal operations, hence carries the free internal group on X to the free internal group on L(X). One must interpret the coproduct indices within the allowed universe; the construction does not require preservation of arbitrary products.

For an internal A-module, the free-module object on X can likewise be presented by finite formal sums of pairs from A×X, modulo the additive and scalar relations. The operations and relations are preserved, so L carries the free A-module to the free L(A)-module on L(X). For modules M,N over a commutative internal ring A, the tensor product is the quotient of the free A-module on M×N by additivity in both variables and balancing. Preservation of that presentation gives the canonical comparison

L(M⊗_A N) ≅ L(M)⊗_{L(A)}L(N).

This verifies the stated free-group/free-module/tensor examples under the explicit preservation assumptions. It does not formalize every possible “opération fonctorielle”; the complete scope remains conditional on a construction of the stated kind. The unprovided §6 is not checked.

## Direct image and structures defined by limits

If R:F→E preserves the relevant limits, internal groups, rings and modules are transported by applying R to their operations and defining commuting diagrams, with the product and terminal-object comparisons. An A-module becomes an R(A)-module. This is a direct finite-product/equation check. A reference to an arbitrary family of objects additionally requires preservation of the corresponding products; the text assumes projective limits in this passage.

## A single concrete direct-image example

Take G=C2. In the topos of left G-sets, the constant-trivial-action functor L:Set→G-Set is left adjoint to the fixed-point functor R(X)=X^G. L preserves finite limits, so this is a geometric morphism G-Set→Set. The following statements about its direct image are explicit calculations, not merely examples cited from memory.

1. **Epimorphisms need not survive.** The regular G-set P=G maps surjectively to 1. Its fixed points are empty, whereas 1 has one fixed point. Thus R(P)→R(1) is ∅→1, not surjective. In G-sets, a surjective equivariant map is the coequalizer of its kernel pair; this follows by applying the ordinary set quotient with the induced G-action. In Set, epimorphisms are surjections. Hence the example also shows that R does not preserve the relevant finite coequalizer and is not right exact. Limit preservation follows from taking coordinatewise fixed points in a compatible tuple.

2. **Torsors need not survive.** Let A be the constant group C2 with trivial external G-action. Since C2 is abelian, its multiplication action on the regular external G-set P is equivariant. P→1 is epi, and A×P→P×P, (a,p)↦(ap,p), is an isomorphism. Thus P is an internal A-torsor. Its direct image is empty under the group A^G=C2, so it is not a torsor in Set. This checks the need for more than finite-limit preservation in transporting torsors.

3. **Free modules need not commute.** Let X={x,y} with the two elements exchanged by G. Then X^G=∅. The free abelian group Z[X] has fixed part Z(x+y), while the free abelian group on X^G is 0. Therefore R does not commute with this free-module construction.

4. **Tensor products need not commute.** Let M=N=Z with the generator of G acting by −1. Each fixed module is 0. On M⊗_Z N≅Z the action is +1, so the fixed module is Z. The natural comparison M^G⊗N^G→(M⊗N)^G is therefore 0→Z and is not an isomorphism.

5. **A bialgebra may not inherit its comultiplication on fixed points.** In G-equivariant abelian groups take the bialgebra B=Z[C3], with G acting by inversion on C3. Write the C3 generator as a. The invariant submodule is Z·1⊕Z·s, s=a+a². Its multiplication is closed (invariants always form a subring), but

   Δ(s)=a⊗a+a²⊗a²

   does not lie in the image of B^G⊗B^G→(B⊗B)^G. In the nine-element tensor basis, the invariant tensor-domain image is spanned by 1⊗1, 1⊗s, s⊗1 and s⊗s. Only the last basis vector has the two required diagonal coefficients, and it also has nonzero coefficients of a⊗a² and a²⊗a. No linear combination cancels these using the other three vectors. Thus the comultiplication cannot be transported by inverting this comparison. This establishes failure of the naive inherited structure; it is not a claim that the invariant ring admits no unrelated bialgebra structure whatsoever. The coefficient and rank calculation is saved separately.

The source's broader statement about comodules is kept as a statement of the manuscript, subject to the necessary coalgebra and base-ring data. The explicit bialgebra calculation demonstrates the tensor-comparison obstruction. It does not exhaust all choices of comodule data or prove a universal nonexistence theorem for arbitrary extensions of R.

## Section 3.1.3 and the direction of a geometric morphism

For f:E→F preserving small colimits and finite limits, the adjoint-existence argument already given for 123/028 supplies a right adjoint under the stated Grothendieck-topos universe/size hypotheses. Taking u*=f therefore defines a geometric morphism u:F→E. The reversal of E/F is forced by the definition of inverse image, but the written arrow must still be read from the scan.

If f preserves arbitrary projective limits, the same earlier criterion supplies a left adjoint, under those size hypotheses. This alone does not say that this left adjoint preserves finite limits. The visible last sentence is unfinished after the cancelled g; no unseen qualification or conclusion is supplied. The statement “s'il s'avère que” earlier is a conditional hypothesis, not an explicit request to verify an unproved claim.

The source connects failure of exactness to later cohomological properties. No derived-functor construction or the unprovided following exposé was checked in this run; that connection is background only.
