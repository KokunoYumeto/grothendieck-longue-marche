# Independent review of the intermediate boundary amalgam

**Status: PASS**, at the precise intermediate scope. Full source read: `work_A/intermediate_boundary_amalgam25.md`.

## Exact marked presentation

The marked inclusions of H=C2(c)*Z²(k,T) into R and the isolated corner are the actual inclusions proved in B118. Eliminating D=j c j and u=T D recovers exactly the fifth-prefix relation jPj=P^-1 and the one cross relation; its j-conjugate supplies the other cross relation. The four remaining prefix relations are still absent. No final quotient injection follows.

## Compatible finite kernels

The j-even corner retraction is literal: D,k' go to 1, u to T, and c,k are fixed. Its conjugate companion on H sends c,k to 1 and T to T^-1 c=P^-1. Thus it sends P to P^-1 and satisfies nu³=nu. The actual regional branch character has lambda(c)=lambda(k)=0 and lambda(T)=lambda(P)=1, so v(g)=P^(-lambda(g)) is an actual regional homomorphism extending nu, with v³=v.

Given prescribed vertex kernels, full topology of H in R permits the initial regional refinement. The exact H-kernel of (psi,psi v,psi v²) is L=N intersect nu^-1 N intersect nu^-2 N, and nu(L) is contained in L because nu³=nu. The paired corner map into (H/L)^2 semidirect C2 restricts to h -> (h,nu(h)); its kernel on H is exactly L. Intersecting with the prescribed corner kernel retains L because L was chosen inside that restriction. Hence both finite vertex images have precisely the same embedded edge H/L.

The finite permutation representation used next is sufficient: take free regular-multiple actions of the two finite vertices on a common finite set, and conjugate one action to align the restrictions to H/L. This is injective on both finite vertices. Consequently each vertex receives its full topology in the ordinary amalgam, and the completion is the proper profinite pushout of the explicitly embedded full completions. The proof does not require a general efficient-amalgam assertion.

## Discrete cone centralizer

All involutions of H are H-conjugate and C_H(c)=<c>. Every c-fixed incident edge at either vertex in the ordinary Bass--Serre tree can therefore be represented by an element of that vertex's c-centralizer: adjust the edge representative using the unique involution class in H. Connectedness of the fixed subtree gives a single-edge quotient under C_M(c), and normal form identifies C_M(c)=C_R(c)*_<c>C_B(c). The regional factor is the actual F5_source times C2, and the corner factor is <k'> times C2, so this is F6 times C2. The opposite cone statement is its j-conjugate.

The source comparison retains the full selected-gap conjugation and the actual outer mirror; it is a statement about the six exact preimages before the remaining prefix relations. It does not claim that their final images remain free. No completed centralizer formula is inferred from the discrete tree calculation or from properness of the profinite pushout.

## Limits retained

The final four prefix relations can change both the source image and its centralizer. This review establishes no survival theorem after imposing them, no full completed centralizer formula for the intermediate amalgam, and no conclusion about either main question.

Source SHA256: `ffc1b4395092ba62b8956ffa58fe9c0aa8871a98b76b9b30cfa7cf11004e0eb8`.
