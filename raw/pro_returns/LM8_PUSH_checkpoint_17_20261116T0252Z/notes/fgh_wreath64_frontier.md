# Actual wreath-order-64 fixed-group frontier (unregistered)

This note constructs an actual next cover. It does **not** assert a fixed-subgroup theorem. A.59 already proves every normalizer assertion for this nilpotent closure, and A.78 proves potential good Jacobian reduction of special two-rank zero. Neither supplies rational companion paths by itself.

## Exact finite group and marked data

Let G=(C2)^4 semidirect C4, with the cyclic group rotating four lamp coordinates. Take a single lamp a and the rotation b. These generate G. The actual commutator [a,b] is the product of two adjacent lamps, of order two. Its normal closure is the augmentation subgroup (C2)^3, which is the derived subgroup. Thus this group is outside the cyclic-derived hypothesis of A.79. It has order64, centreC2, maximal element order8, and no cyclic subgroup of index at most two.

The natural faithful action on four pairs has degree8. The commutator has cycle lengths 2,2,1,1,1,1. Accordingly the full Galois closure has genus17 and32 cusps; the natural degree8 intermediate has genus2 and6 cusps. Its proper map factors as a double cover of a cyclic degree4 elliptic isogeny. The two branch kernel points are adjacent in that cyclic kernel. The other two kernel points each have two unramified preimages.

All of these group/action/cycle statements were checked exactly by `notes/fgh_wreath64_frontier_certificate.py`, with retained `.json/.out`. It verifies all4096 permutation-composition identities, the actual generating pair, commutator and normal closure, centre, Frattini subgroup, point stabilizer, and intermediate ramification. It does not use a numerical rank extrapolation.

## An actual algebraic realization

Work over a finite extension of Q(i) defining the points below. Put

E4: y^2=x^3-6x^2+x, R=(1,2i), T=(0,0).

The point R has order4 and 2R=T. The exact degree2 isogeny to the fixed E:v^2=u^3-u is

u=(x-1)^2/(4x),  v=y(1-x^2)/(8x^2).

Its kernel is {O,T}, and it sends R to (0,0). Composing it with [1+i] on E therefore gives an actual cyclic degree4 isogeny eta:E4→E with kernel K={O,R,T,-R}. These assertions follow directly from the displayed equation and doubling formula; the rational equation identity is independently recorded in the companion map certificate.

Choose Q with 2Q=R. Let ell_Q be the tangent line at Q. The rational function

f=(x-1)/ell_Q

has divisor R+O-2Q. Consequently the actual smooth proper normalization Y of z^2=f is a connected double cover of E4 branched exactly at O and R. It has genus2. Under eta∘q its cusp set is q^{-1}(K), consisting of the two ramified points and four ordinary points; hence six cusps.

For completeness this construction has the asserted full wreath closure, not merely the same branch data. Translate f by K and put f_j(P)=f(P+jR), j=0,1,2,3. If the four square classes had any F2-linear relation, their cyclic F2[C4]-module would have a nonzero annihilator. Every nonzero ideal of F2[C4]=F2[t]/((t+1)^4) contains (t+1)^3=1+t+t^2+t^3. Their product would therefore be a square.

But half the divisor of this product is D_K-D_{Q+K}. Its degree-zero divisor class is -4Q=-2R=T, which is a nonzero two-torsion class. Thus the product is not a square. The four classes are independent. Adjoining all four square roots gives a (C2)^4 cover of E4. Translation by R lifts by cycling those roots, literally with order4; the four root equations have no relation to obstruct this permutation. The full composite over E consequently has group (C2)^4 semidirect C4. Its only branch point is O. This proves the actual cover identification used by the finite certificate.

## What is proved and what remains

A.78 applies to the actual one-point Galois two-group closure at the potential-good supersingular place2. Its Jacobian and every intermediate Jacobian have potential good reduction of special two-rank zero. A.59 proves all normalizer assertions. The full pro2 fixed subgroup also follows from the induced pro2 topology/A.22. The remaining fixed-group question concerns odd coefficient primes and actual marked cusp paths (or a different arithmetic fixed-group argument).

The genus2 double cover has only two possible proper compact-type shapes: a smooth genus2 component, or two elliptic components. If the special degree2 map from a smooth genus2 component to the good elliptic target is separable, its one branch point over the common reduction of K has one preimage, so all six marks lie in that reduction cluster. In a two-elliptic model with component degrees1+1, the generic involution exchanges the components and both branch marks specialize to the node; the actual map again places all six marks there. These cases are promising but are not yet a complete marked-model proof.

The unresolved configuration is component degrees2+0, with the degree2 map on the main supersingular elliptic component radicial and a contracted supersingular elliptic tail over the common kernel reduction. The involution is trivial on the main component and nontrivial on the tail. Its unique special fixed point on the tail is the node, so the two ramified cusps cannot lie smoothly on the tail. The four unramified cusps could still lie smoothly there in exchanged pairs. Rank zero alone does not exclude this, and no companion path is asserted for them.

The actual cyclic kernel has two closer pairs {O,T} and {R,-R}; an exact two-adic chart or a direct Prym torsion calculation is needed to locate the four ordinary marks. Formal-distance intuition alone is insufficient. This note retains that precise missing step.
