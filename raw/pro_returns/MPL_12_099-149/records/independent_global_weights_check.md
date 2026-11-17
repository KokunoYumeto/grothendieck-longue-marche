# Independent check of the proposed R04 global weight counterexample

Research-only verification after the transcription freeze; no frozen file changed. Proposed by the root researcher as a global consequence of W13–W14 and independently checked by the weights researcher. **Verdict: valid, with high confidence.** No novelty claim is made and no RS status is changed.

## Witness and scope

Frozen cote 12, scan 108, section B.1, the two marginal questions: “peut-on remplacer 2n+2j par 2n+j ?” and “peut-on remplacer 2i+2j par 2i+j ?”. The second appears in the discussion with i≤n; the example has i=n=j=1 and satisfies that restriction. The coefficient is itself a smooth projective higher direct image, so no conjectural dévissage or semisimplicity reduction is needed.

## Exact-sequence check

Let k=F_q have odd characteristic with −1 a square, let U=P¹_k−{0,1,∞}, and let a:U→P¹_k. For the Legendre elliptic scheme π:E→U, y²=x(x−1)(x−λ), take F=R¹π_*Q_l, with l≠char(k). In the following all cohomology is over k̄; the maps and groups retain their natural geometric-Frobenius action.

1. Katz states that F has geometric monodromy SL₂, so the dual representation has no invariant vector and H⁰(U_k̄,F∨)=0. Poincaré duality for the smooth curve gives H²_c(U_k̄,F)=H⁰(U_k̄,F∨)∨(−1)=0.
2. Set B=coker(a_!F→a_*F). This is a sheaf supported on the three boundary points, with stalk F^{I_x} at each one. Over k̄ these points have no higher étale cohomology, so H¹(P¹_k̄,B)=H²(P¹_k̄,B)=0. The long exact sequence therefore gives H²(P¹_k̄,a_*F)≅H²(P¹_k̄,a_!F)=H²_c(U_k̄,F)=0.
3. The Leray five-term sequence contains H¹(U_k̄,F)→H⁰(P¹_k̄,R¹a_*F)→H²(P¹_k̄,a_*F). Its first displayed arrow is consequently surjective.
4. The stalks of R¹a_*F at 0 and 1 are each Q_l(−2), by the split multiplicative calculation in W13 and the independent check V1. These points are k-rational, so projection onto their direct sum is Frobenius-equivariant and yields H¹(U_k̄,F)↠Q_l(−2)². This quotient has weight 4, whereas either proposed bound gives 3.

No computation at infinity is required for this argument: projection onto the 0 and 1 summands is enough. Katz also states that its inertia has a nontrivial quadratic character times a unipotent block, so its invariants and first inertia cohomology vanish; that observation is optional and not used to establish the quotient. The finite-field arithmetic cohomology of a boundary point can have positive-degree terms, which is why the displayed cohomology groups must remain explicitly geometric.

## Suggested main note: four sentences

Over an odd finite field k=F_q in which −1 is a square, let a:U=P¹_k−{0,1,∞}→P¹_k and let F=R¹π_*Q_l for the Legendre family y²=x(x−1)(x−λ). Its geometric monodromy is SL₂ (Katz, 2012, Chapter 15, p. 77), so duality gives H²_c(U_k̄,F)=0, and the zero higher cohomology of the boundary quotient a_*F/a_!F gives H²(P¹_k̄,a_*F)=0. The Leray edge map therefore surjects from H¹(U_k̄,F) onto H⁰(P¹_k̄,R¹a_*F), whose rational boundary summands at 0 and 1 are Q_l(−2)² by the split multiplicative calculation. Hence H¹(U_k̄,F) has a weight-4 quotient, contradicting both proposed upper bounds 2n+j and 2i+j when i=n=j=1.

**Kind:** own idea / explicit counterexample, proposed by the root researcher and independently verified. **Confidence:** high, because every map is supplied by a sheaf long exact sequence, curve duality or Leray, and the Frobenius weights of the boundary stalks are explicit. **Context relation:** answers the two open weight-improvement questions in Hua, “Poids de la cohomologie ℓ-adique d'une variété singulière ou non propre (pages 104 à 108)”; complements W13's local obstruction to the coefficient variant, not a refutation of the constant-coefficient immersion bound. **Related records:** `records/research_weights.md`, W13–W14; `records/independent_weight_examples_check.md`, V1 and “Compact-support counterpart”.

## Primary reference

Katz, N. M. (2012). *Convolution and equidistribution: Sato–Tate theorems for finite-field Mellin transforms* (Annals of Mathematics Studies, Vol. 180). Princeton University Press. Author-hosted manuscript: https://web.math.princeton.edu/~nmk/mellin357.pdf . Chapter 15, p. 77, supplies the family, weight-one purity, SL₂ geometric monodromy and the local inertia blocks. Reopened for this independent check: `turn164871981view0`; earlier inspected refs: `turn233036191view0`, `turn650332182view0`, `turn650332182view1`.
