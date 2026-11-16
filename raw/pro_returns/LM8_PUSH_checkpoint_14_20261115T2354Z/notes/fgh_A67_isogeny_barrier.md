# The tetrahedral star does not obey A66's unique-main base-change argument

This is an explicit limitation of the proof, not a counterexample to either cusp assertion.

Let X→E be an A67 tetrahedral cover. Its actual compact-type three-adic model has four elliptic tails, each mapping to the good E model by the same degree3 supersingular isogeny, and a rational centre mapping constantly to O. Thus each tail map is radicial of degree3.

Pull back along a degree-h elliptic isogeny E''→E with (h,3)=1. It is finite étale on good models after finite extension. Each elliptic tail pulls back to one connected elliptic curve: the original degree3 radicial map and the étale degree-h isogeny are linearly disjoint. The rational centre pulls back to h disjoint copies. Every connected tail has one node above each of the h centre copies. The dual graph is therefore the complete bipartite graph K_{4,h}, with

    vertices = 4+h, edges = 4h, first Betti number = 3(h−1).

The proper genus is 1+h(4−1)=3h+1, agreeing with four elliptic components plus graph genus3h−3. For h>1 the Jacobian is not potentially good at this place and this model is not of compact type. The selected cusps still have companions on their rational centre copy, but A42 requires compact type in addition.

In particular a prime-to-six abelian factor cannot be appended to A67 by copying A66's proof. A66 has a unique radicial main component and constant off-main trees; A67 has four nonconstant elliptic components. No fixed-group or normalizer failure is asserted.
