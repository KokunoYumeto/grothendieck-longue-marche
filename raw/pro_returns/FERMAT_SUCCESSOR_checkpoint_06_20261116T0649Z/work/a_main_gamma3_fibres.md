# Exact actual Gamma3 Selmer fibres over the surviving integer compact classes

Proposed companion to A.71. No manuscript integration requested yet.

Let E_d,R,O,U_d,Gamma3 be as in A.71, and let n∈Z. There is exactly one Gamma3 Selmer section class over compact classκ(nR): the actual point-section image for n≠0 and the common image of the O-cusp packet for n=0. Thus the section classes in the entire finite-alteration family are naturally in bijection withZ, not merely their compact exponents.

## Geometric kernel and alignment

A.67 identifies the geometric image as TE×V4; hence ker(Gamma3→π1(E_d)) is V=F2², with arithmetic action through H⊂GL2(F2)=S3. This action is independent of the reference compact section because the geometric product is abelian.

Fix the actual section s_n from the rational point nR if n≠0, or a rational tangent atO if n=0. Given any section s whose compact conjugacy class isκ(nR), conjugate by an element of the geometric group lifting the required TE element, so its compact section agrees with s_n literally. Their difference is then a1-cocycle inV. It is enough to show this class inH1(Q,V) iszero, since that makes the two sections conjugate byV.

At each finite placev, full local compact Tate Kummer injectivity identifies a Selmer centre withnR. If n≠0 it is interior, so the local section is conjugate to the local point section. If n=0 it has cusp centreO. The modular X3 inertia over the infinity block is trivial after the cubic Fermat pullback (A.67's inertia tuple(1,2,1)), and compactification also kills cusp inertia. Hence Gamma3 killsI_O, and every local tangent parameter has the same section image as the chosen cusp section.

In either case a local geometric conjugator projects to an element of(TE)^{G_v}. This invariant group iszero: local elliptic torsion is finite, so its full Tate module vanishes. The conjugator therefore lies inV. Thus the global difference cocycle has zero image inH1(Q_v,V) for every finitev. Real places are unnecessary for this argument.

## A small finite-module local-global lemma

For every continuous2-dimensional F2-moduleV ofG_Q, the map H1(Q,V)→product_{finitev}H1(Q_v,V) isinjective. LetL be the finite splitting field of the action. A locallyzero class restricts to a homomorphismG_L→V that iszero locally at every finite place ofL. Chebotarev applied to its finite quotient makes this homomorphismzero. By inflation-restriction the class comes fromH1(H,V), whereH⊂GL2(F2)=S3 is the action image.

ForH=1 the latter group iszero. ForH=C3 it iszero because3 is invertible inF2. ForH=C2 the nontrivial matrix is a transvection; the norm operatorN=1+σ=σ−1 has rank1 and squarezero, so kerN=im(σ−1), andH1(C2,V)=0. Finally forH=S3, its normalC3 has zero invariants onV and zeroH1, so inflation-restriction again givesH1(S3,V)=0. These exhaust the subgroup possibilities. Hence the global difference class vanishes and the fibre is a singleton.

The result concerns Gamma3, whose infinity cusp inertia is killed. It does not assert that the full punctured abelian or metabelian cusp packet collapses; A.64 keeps the full completed-Kummer packet there. Nor does it classify fibres over arbitrary nonrational compact exponents, whose existence is still undecided for infinitely changed exponents.
