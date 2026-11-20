# Checks prompted by 123/028

These are internal arguments prompted by the cancelled typescript. No external text or the unprovided sections cited by its references was consulted. The arguments do not settle a digit, alphabet, cancellation or edge-cut word.

## Uniqueness and preservation

Write L=u* and R=u_* with L left adjoint to R. If two right adjoints R and R' are given for the same L, their representing functors are naturally identified:

Hom(X,RY) ≅ Hom(LX,Y) ≅ Hom(X,R'Y).

Yoneda gives the unique natural isomorphism compatible with these adjunction identifications. The same argument with the variables reversed applies to two left adjoints of one R. Thus the opening uniqueness statement is checked in the usual sense that the adjunction data are respected. It does not claim that an underlying functor has no natural automorphisms when the adjunction is forgotten.

For a small diagram D in the source of R,

Hom(X,R lim D) ≅ Hom(LX,lim D) ≅ lim Hom(LX,Dj)
≅ lim Hom(X,RDj) ≅ Hom(X,lim R Dj).

The natural representing comparison is an isomorphism, so R preserves limits. Dually L preserves colimits. Adding the stated finite-limit preservation of u* proves its finite-limit-and-colimit exactness. It also preserves epimorphisms in a topos: every epimorphism is the coequalizer of its kernel pair, and u* preserves that coequalizer. These calculations prove the needed preservation statements; they do not repair the cancelled local wording.

## Transporting the stated structures

For an internal group, its multiplication, unit, inverse and defining commutative diagrams use finite products and a terminal object. Applying a finite-limit-preserving functor and the product comparison isomorphisms gives the corresponding group operations and identities. The same construction transports internal rings, and an A-module becomes an L(A)-module by applying L to the addition, zero, inverse and A×M→M action. This is a direct operation-and-equation check for the first three examples in the paragraph.

For a G-torsor P, use the intrinsic two conditions: P→1 is an epimorphism, and G×P→P×P, (g,p)↦(gp,p), is an isomorphism. The preservation just proved carries these to the same conditions for L(P) under L(G). This proves transport of torsors without assuming a chosen section or invoking points of the topos.

More generally, any explicitly given construction from finite limits and small colimits is transported by the corresponding comparison isomorphisms; a structural equation is a commutative diagram and remains one after applying a functor. This is a conditional construction principle, not a formal definition of every possible “espèce de structure” in the source. For coalgebra/comodule/bialgebra examples one must also specify the ring and coalgebra data and their tensor products. The clipped page does not supply that complete specification. The phrase “comodule sur un anneau” is left literally as read and is not silently changed to another word. No independent full tensor/coalgebra construction is claimed here.

## The footnote's adjoint criterion: an internal proof under explicit size hypotheses

The necessary directions are the preservation calculations above. Here is a proof of the converse under the standard structural hypotheses of Grothendieck topoi relative to a universe U: locally U-small, U-complete and U-cocomplete, U-wellpowered, U-cowellpowered, and having a U-small separating family. These structural properties, including effectiveness of epimorphisms, are used as topos background; their derivation from a site is not reproved in this run.

First, a separating family (G_j) in a topos gives a cogenerating object Q=∏_j Ω^(G_j). To see this, for different f,g:X→Y choose x:G_j→X with fx≠gx. The graph of fx is a subobject of Y×G_j, hence defines Y→Ω^(G_j). Its composites with f and g are different: after pulling back along (x,id), the first contains all of G_j and the second does not. Fill the other product components with the constant truth maps. This gives a map Y→Q separating f and g. This construction uses a family of generators, not the generally invalid assumption that their coproduct is a single generator.

The following general argument also works with a small family of cogenerators (Q_j). Let F:C→D preserve U-small limits, with C U-complete, locally U-small and U-wellpowered, and with that cogenerating family; D is locally U-small. Fix d∈D. We construct an initial object in (d↓F).

Form the U-small disjoint union A of the sets Hom_D(d,FQ_j), retaining j as part of each index. Given an object (c,u:d→Fc) of the comma category, consider every pair f,g:c→Q_j with F(f)u=F(g)u. Equalize all these pairs at once, obtaining i:c0→c. Limit preservation factors u uniquely as F(i)u0. For each index a=(j,v) actually obtained as v=F(f)u for some f:c→Q_j, all the restrictions fi agree. Choose one such f for each a. Their product gives

c0 → P_B = ∏_(a=(j,v)∈B) Q_j,

where B⊂A is the subset of obtained indices. This map is monic: its components include the restrictions of every map c→Q_j, and the cogenerating family separates maps into c; i is itself monic. In the comma category it lies over the canonical map d→F(P_B) determined by the v components. There is a U-set of subsets B, and for each product P_B a U-set of subobjects up to isomorphism. For any underlying subobject, at most one compatible comma-category arrow from d exists, because F preserves monomorphisms. Consequently these compatible subobjects form a U-small family S. Every (c,u) receives a map from one member of S, namely the represented (c0,u0). Thus S is weakly initial.

The comma category has U-small limits since F preserves them. It is nonempty, using the terminal object of C and its terminal image. Take the product W of the weakly initial family S; W is weakly initial. Let e:I→W equalize all endomorphisms of W with its identity. There is r:W→I by weak initiality. Since er is an endomorphism, (er)e=e, and hence re=id_I. For any f,g:I→X take their equalizer h:J→I and a map s:W→J. The endomorphism ehs of W satisfies (ehs)e=e, whence hse=id_I; therefore f=g. A map I→X exists by I→W and weak initiality. Thus I is initial, as required. The universal arrows for all d assemble into a left adjoint of F.

For a colimit-preserving functor, apply the same argument to the opposite categories: U-cowellpoweredness and a U-small generating family become the hypotheses just used. It follows that the functor has a right adjoint. For the topoi in the excerpt, this proves the footnote's two sufficiency directions under the stated universe and structural hypotheses. It does not verify that the printed references (1.5 et 1.8), (I 2.11), or the cancelled final subdivision point to those proofs in the unseen text.

## Limits of this check

The original excerpt expressly declines the full formalization: “Plutôt que d'entrer dans la tâche peu engageante de donner un sens précis à cet énoncé et de le justifier de façon formelle”. The definite insertion advising the reader to make examples explicit is distinct from any crossed-out “vérifier que” in the footnote. The mathematical checks above are this run's work; they do not turn either a cancelled instruction or a source hesitation into live text.
