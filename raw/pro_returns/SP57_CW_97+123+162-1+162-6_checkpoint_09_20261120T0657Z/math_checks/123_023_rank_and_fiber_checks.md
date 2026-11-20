# Checks prompted by 123/023

These are internal proofs and exact matrix calculations, without external research. No result below alters a glyph or formula in the transcription. A mathematical discrepancy is reported as such even when the letter labels its statement as an expectation.

## Continuation: outer automorphisms

If the inner-automorphism stabilizer of the quadruple is trivial, restricting Aut(G)→Out(G) to the automorphisms preserving that quadruple has trivial kernel, and is injective. This checks the continued parenthesis conditionally on the preceding page's stabilizer assertion; it does not identify the actual subgroup or prove the general apposition assertion.

## Type-A subregular rank

For SL_m, use the invariant power sums tr(X^k), 2≤k≤m, on its Lie algebra. On a diagonal matrix their values generate the symmetric eigenvalue invariants with trace zero, by Newton identities over characteristic zero. The differential at X in direction Y is k tr(X^(k−1)Y). The trace pairing on sl_m is nondegenerate. For a nilpotent X with blocks (m−1,1), the nonzero powers X,…,X^(m−2) are linearly independent, whereas X^(m−1)=0. Thus the quotient differential has rank m−2=r−1. For m=2 this says rank zero at the zero matrix.

The commuting endomorphism algebra has dimension Σ_i,j min(λ_i,λ_j)=m+2: this follows directly by identifying each Jordan block with k[t]/t^λ and counting k[t]-linear maps. Passing to trace-zero endomorphisms subtracts one dimension. Therefore the orbit dimension is (m²−1)−(m+1)=m²−m−2=n−r−2. This proves the dimension and rank statement for this type-A subregular element, not for types D or E.

For U=I+X in SL_m, take tr(U^k), 1≤k≤m−1, as quotient coordinates. Their differentials on tangent directions UY are k tr(U^kY). Since tr(Y)=0, the resulting linear forms are combinations of tr(XY),…,tr(X^(m−2)Y). The binomial-coefficient matrix has full rank m−2: the polynomials binom(t,j), 1≤j≤m−2, vanish at t=0, have distinct degrees and are determined by their values at 1,…,m−1. Hence the group quotient rank is also m−2. The exact certificate independently computes the ranks and orbit dimensions for m=2,…,6.

## Explicit non-simply-laced rank counterexample

Let J have 2×2 blocks [[0,I],[-I,0]], and let N=[[0,I],[0,0]] in sp₄. Then N²=0 and U=I+N is symplectic. A basis of sp₄ consists of matrices [[A,B],[C,−Aᵀ]], with A arbitrary and B,C symmetric. The exact commutator matrix has rank six and kernel dimension four. Since dim Sp₄=10 and its rank is two, this orbit has dimension 10−2−2=6, the dimension specified in the letter. Relative to diag(a,b,−a,−b), the off-diagonal basis weights are ±2e₁, ±2e₂ and ±e₁±e₂, directly exhibiting two root lengths.

The Lie-algebra invariant coordinates tr(X²), tr(X⁴) have differentials 2 tr(NY) and 4 tr(N³Y)=0. The first is nonzero: choosing C=I gives tr(NY)=2. Their differential rank is therefore one. These invariant coordinates generate the quotient: on a Cartan with eigenvalues ±a,±b, the Weyl invariants are the symmetric polynomials in a²,b², and the displayed power sums generate them in characteristic zero. Restriction detects invariant polynomials here because regular semisimple matrices form a dense open set and are symplectically diagonalizable; the explicit power sums provide every indicated Weyl invariant.

For the group, write a=tr(U) and b=((tr U)²−tr(U²))/2, the first two characteristic coefficients. On the torus with eigenvalues t₁,t₁⁻¹,t₂,t₂⁻¹, put s_j=t_j+t_j⁻¹. Independent inversions give the polynomial ring in s₁,s₂, and permutation gives k[s₁+s₂,s₁s₂]; a=s₁+s₂ and b=2+s₁s₂. Thus a,b are quotient coordinates. At this U, a=4 and the differentials on UY are da=tr(NY), db=2 tr(NY), again of rank one. For the adjoint group PSp₄ the central involution sends a to −a and fixes b, so a²,b are coordinates; their differentials at U still have rank one. This also addresses the adjoint-group setting of the preceding letter page.

Consequently the literal strict inequality rank < r−1 on all other root-length types fails for this example: one is not less than one. The positive refined statement is that this particular C₂/B₂ subregular orbit has rank r−1. No classification-wide replacement formula is asserted. The source introduces its claim with “There are some reasons to believe”; that qualification remains, and the inequality is never changed to fit this computation. The orbit-uniqueness expectation is not established or refuted by merely displaying one orbit.

## A Springer-fiber dimension example

For a rank-one nilpotent X in sl₃ with X²=0, set L=im X and K=ker X. Then dim L=1 and dim K=2. An X-stable complete flag (ℓ,H) has ℓ⊂K. If H=K, ℓ is any line of K, giving one P¹. If H≠K, stability forces L⊂H; then H∩K=L, so ℓ=L, and H can be any plane containing L, giving another P¹. These components meet at (L,K). The stable-flag variety has dimension one. The exact commutator computation gives orbit dimension four in sl₃, so 2N=6 and (2N−dim orbit)/2=1, as expected on the page. Stability under U=I+X is equivalent to stability under X, so the same example applies to the unipotent group element.

This proves a concrete case of the dimension formula, not the formula for all groups/elements. The general bound and its claimed depth-theoretic implication are carried as background without a proof in this run.

## A rational-singularity base case

The nilpotent cone of sl₂ is the surface a²+bc=0. Up to a linear change of coordinates its ring is k[s²,st,t²], the even-degree subring of k[s,t]. It is normal: the invariant subring of an integrally closed domain under the sign involution is integrally closed, because an invariant fraction integral over that subring is integral over k[s,t], hence belongs to k[s,t] and is still invariant.

The usual incidence resolution is the total space of O_{P¹}(−2), with the zero section contracted to the vertex. One can realize the map as a closed incidence subset of the cone times P¹, so it is proper; it is an isomorphism off the vertex and its total space is smooth. For the affine bundle projection q to P¹, q_*O is the direct sum of O_{P¹}(2m), m≥0. Each has zero positive-degree cohomology (the elementary two-affine-chart computation on P¹), and the same two-chart computation commutes with the direct sum. Thus H^i of the resolution's structure sheaf is zero for i>0. Since the cone is affine, this gives R^i f_*O=0 for i>0. Also Γ(O) is the graded algebra ⊕ H⁰(P¹,O(2m)), exactly the even-degree polynomial ring of the cone; since the cone is affine this identifies f_*O with O directly.

This is an actual proof of the page's stated vanishing in one low-rank fiber. It does not prove the claimed general implication from the Borel-variety inequality or the general rationality of every fiber. The written superscript/cancellation above O and the handed inequality signs are settled only from the image.
