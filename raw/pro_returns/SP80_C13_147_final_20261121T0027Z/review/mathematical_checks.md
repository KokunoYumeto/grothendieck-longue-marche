# Local mathematical checks performed by the main reader

## MC109-01: why a chain presentation does not display a symmetric-group action

Conditional on the explicitly displayed chain with one vertex in each codimension d,d−1,…,0, every order automorphism fixes each vertex: it fixes the unique least element and then, inductively, the unique next element. Its automorphism group is therefore trivial. For the alternative poset described in the margin, with a unique least element of codimension d and d otherwise indistinguishable elements of codimension 1, permutations of those d elements give S_d (for the nondegenerate d>1 case). This verifies the combinatorial motivation for the margin's warning that the chain presentation does not itself exhibit the symmetric action. It does not verify the geometric representability assertions, nor change the printed target of any action in the transcription.

## MC110-01: local consistency of the contracted-product formula

Under the stated codimension-preserving embedding definition of H(J), for the one-element case of codimension d the image must be the full d-element subset, so there is one choice. For the two-level case with codimensions d and 1 (d>1), there are d singleton choices. For a maximal chain with every cardinality d,d−1,…,0, each chain is determined by an ordering of the d elements, giving d! choices. Thus these finite-set cases are consistent with the preceding identifications of D_d, its d-sheeted cover, and the S_d torsor. This is a targeted finite combinatorial consistency check, not a proof of (155) for arbitrary J or any global geometric claim. It supports distinguishing the d-element set I_d from the d+1-vertex chain I(d).

## MC112-01: equivariance of evaluation

For a finite-set embedding h and a permutation σ of its target, let `(σ·h)(y)=σ(h(y))`. Evaluation at x then satisfies `ev_x(σ·h)=σ(ev_x(h))`. If h preserves the assigned codimension by subset cardinality, its value at x has the required cardinality. This verifies the finite-set equivariance used by the displayed evaluation map. It does not prove the geometric identifications of the associated spaces.

## MC116-R: Boolean source fibres do not alone imply endpoint uniqueness

Take three objects a,b,c with codimensions 2,1,0. Besides their identities take distinct arrows f,g:a→b, k:b→c, and h:a→c, and define kf=kg=h. The fixed-source factorization poset at a is the Boolean diamond `{id_a,f,g,h}`, identified with `{ {1,2},{1},{2},∅ }` in reverse-inclusion order. The poset at b is `{id_b,k}`, identified with `{ {1},∅ }`; the one at c is a singleton. Target codimension agrees with subset cardinality in each case. No arrow increases codimension, and the only equal-codimension arrows are identities. Nevertheless f and g have the same source and target, so the endpoint map is not injective.

Finite discrete sets carry analytic-space structures. Thus this is also an example among internal categories in such spaces, under the reading of condition c as a ranked Boolean fixed-source factorization-poset condition. Additional geometric or categorical requirements not stated in that condition could change the implication. The claim at the end of scan 116 is retained verbatim; only the notes record the limitation.

Root and reader_c constructed this example independently before comparing their accounts. Reader_c's check was scoped to scan116 alone; root additionally checked the conditions a and b written on scan115. `scripts/check_boolean_source_counterexample.py` checks all 13 composable pairs and 21 composable triples, identities and associativity, the degree restrictions, and the three Boolean fibres. Its actual output is `review/boolean_source_counterexample.json`. This is a finite formal certificate, not an external theorem citation.

## MC120-R — literal bang and base-index discrepancies

Root inspected all17 existing first-pass crops for scan120. Formula(181) has a detached dot below a high upright, hence D_d^!, whereas witnessC gives a prime. Conditional on the torsor interpretation already written in scans110–117 and the ordinary subset-poset interpretation of P(I_x), the displayed identification has a cardinality problem: for d=2 a torsor under S_2 has2 elements, whereas the subset set of a2-element set has4 elements (empty set, two singleton sets, whole set). This finite comparison is a targeted check of the apparent mismatch, not a correction of the manuscript or a claim that every use of P must have this meaning. The bang remains.

In(182), the last base is visibly D_1 although x belongs to D_d and D_{d,1} was the d-sheeted covering of D_d. Germs at x of sections of that covering are typed over D_d. The check is a source/target consistency test, not a proof of the asserted analytic identification. D_1 remains in the text.

The pale grey horizontal trace following (D_{d,1})_x is far lighter than the nearby ink and lacks the solid edges of the separate comma to its right. It is excluded as paper/erasure trace, not transcribed as H's dash.

## MC124-R: conditional coordinate-projection check

On scan124, the surjectivity claim can be checked within the indicated coordinate model without deciding any uncertain ink. Let I be a d-element set and J a d′-element subset. Restriction r_J: Z^I -> Z^J is surjective because extension by zero e_J satisfies r_J e_J=id. Its kernel is Z^{I\J}. For a permutation sigma of I, evaluation at j in J gives r_{sigma J}(sigma v)(sigma j)=v(j), which equals (sigma|_J r_J v)(sigma j); hence the restriction maps are equivariant as the selected subset varies. This verifies the finite-coordinate model of the stated surjective map, conditionally on the manuscript’s local identifications. It does not prove a global descent assertion or alter the visible high clusters in(193), the tiny connector caps, or the final D_{d′} factor in the written fibre product. The last factor remains a source-notation issue, since the displayed data do not provide a map D_{d′}->D_d for that literal product.

## MC125-R — conditional associativity of extension of structure group

For homomorphisms φ:G→H and ψ:H→K, take a right G-torsor P and the quotient relation (pg,h)∼(p,φ(g)h). The map [[p,h],k]↦[p,ψ(h)k] is invariant under the first relation because [pg,ψ(h)k]=[p,ψφ(g)ψ(h)k], and under the second because ψ(hh₀)k=ψ(h)ψ(h₀)k. The inverse is [p,k]↦[[p,1],k]: the G relation is respected by moving φ(g) across the second contracted product. The two composites are identities, using [[p,h],k]=[[p,1],ψ(h)k]. This proves only the stated formal associativity conditional on the group actions and quotients. It does not certify the manuscript index pairings, base spaces or the crowded product sign in198. Root independently checked these relations; linked to S125-03/N125-10.

## MC129-R — conditional pullback test for the unstarred lower bases

This is a formal test to be attached to the review of(209), not an ink decision. Let q:B′→B be a covering of locally path-connected spaces and let p:E→B be any map. The pullback E′=E×_B B′ has Π₁(E′) equivalent to the 2-fibre product Π₁(E)×_{Π₁(B)}Π₁(B′). To see essential surjectivity, a triple(e,b′,α), with α a path in B from p(e) to q(b′), can be moved by the unique lifted path to an object over an exact equality p(e)=q(b′₀). Morphisms between such objects are precisely pairs of paths with compatible projection homotopies: uniqueness of lifting identifies these with paths and homotopies in E′. In the manuscript notation, if D_mult→D_d0 is such a covering and P_mult^*=P_d0^*×_{D_d0}D_mult, then a groupoid square with unstarred lower D bases can still be2-cartesian. Missing lower stars alone would therefore not refute it. This conditional check does not establish all covering hypotheses of the manuscript or settle any overwritten glyph.

## MC130-R — conditional kernel check

For a locally trivial bundle with connected fibre F=(C*)^d, the homotopy exact sequence gives π₂(B)→π₁(F)→π₁(E)→π₁(B)→π₀(F)=0. The elementary coordinate retraction of(C*)^d onto(S¹)^d identifies π₁(F) with Z^d. If π₂(B)=0, the connecting-map image is zero, so the fibre map is injective and its image is exactly the kernel of π₁(E)→π₁(B). Thus the written π₂-vanishing qualification is sufficient under these bundle hypotheses. Without it, the kernel is the quotient of Z^d by the connecting-map image and need not be the whole lattice. This uses the standard homotopy exact sequence as background and checks its consequence; it is not a fresh proof of that theorem, nor proof that every manuscript object satisfies the bundle hypotheses.

## MC131-R — normal-crossing coordinate test of the last-vertex restriction

For the coordinate divisor D={xy=0} in X=C², D₁ is the disjoint union of the two coordinate lines and D₂ is their intersection point. The induced boundary on D₁ consists of the two origins, so D₁^*=C* disjoint union C*. There is no deeper boundary on D₂, so D₂^*=D₂. The incidence space D_{2,1} consists of the two choices of a branch at the crossing, and its source-restricted open D_{2,1}^*=D_{2,1}×_{D₂}D₂^* is still those two points. The target map sends them to the two origins of D₁; neither image lies in D₁^*. Consequently this geometric target map does not restrict to a map D_{2,1}^*→D₁^*. This verifies a concrete obstruction to inheriting the last-vertex map after restricting by the first vertex. It does not prove that no abstract groupoid functor, auxiliary-choice construction or tangential construction could exist, and it does not complete the manuscript's unfinished parenthetical argument.
