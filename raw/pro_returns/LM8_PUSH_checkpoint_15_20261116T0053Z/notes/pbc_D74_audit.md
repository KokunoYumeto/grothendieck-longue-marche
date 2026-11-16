# Independent audit of D.74

**Result: PASS.** Audited by the P/B/C agent on 2026-11-15 after checkpoint 10. Read the complete candidate `notes/de_finite_ramification_ore_draft.tex`, and reread the actual action/torsion argument of D.35 and the uniform ramification/compactness proof of D.47.

## Arithmetic and actual coefficient scope

The finite-module Euler characteristic over Q(zeta5) gives d-h=3. The injection from the maximal pro-five quotient's H2 is justified independently: a nonzero invariant character of its kernel would produce a pro-five extension quotient in which that kernel survived. Finite relation rank and the minimal-presentation argument therefore give deficiency at least three without assuming cd(P)=2. Actual finite coefficient and affine-cocycle actions over Q(zeta5) are five-groups, so their factorization through P and the coprime C4 extension is valid.

The primitive Soulé element from D.35 survives in the finite-ramification operator image. Its nonzero multiplier cannot be canceled by the Kummer monomial: modulo five the latter either has a degree-one term, or has no nonconstant term below degree five while the Soulé factor retains its nonzero degree-three term. Thus the special multiplication operator h is nonzero for every twist in the stated scope.

## Ring and actual cocycles

The completed semidirect-product ring has the asserted ordered expansion and continuous action. The weighted filtration is essential: wt(5)=2 and wt(u)=wt(v)=wt(z)=1 make the commutator error have strictly higher degree, giving a commutative polynomial associated graded ring. The direct finite-generation argument sums finitely many coefficient series in the complete ring and does not assume an arbitrary ideal is closed. The Noetherian-domain argument supplies both Ore conditions, and right localization applies to the Fox cycle/boundary right modules, not to the actual Alexander module.

Arbitrary values on free pro-five generators yield compatible finite affine five-group homomorphisms. The completed Fox equations therefore describe continuous actual cocycles. The localized deficiency calculation supplies a nonzero class represented by an integral cycle; no formal fraction is treated as an actual Alexander cocycle.

## Tame descent and denominators

Conjugation by the actual order-four operator gives the stated automorphism of the operator ring. Its nonidentity powers are outer on the division ring because inner automorphisms fix leading symbols in the commutative graded fraction ring, whereas the tame action scales u by a nontrivial fourth root. The division-ring automorphism independence argument is valid on the generating subring. It produces a nonzero exact invariant cycle, and then a nonzero invariant element of the intersection of the four denominator ideals. Multiplying on the right preserves the invariant cycle and its nonzero localized class. The equation w_i=h*u and the nonzero detecting operator r_j*u-w_j have the correct multiplication order.

## Infinite rank and final topology

The eigenprojector unit e and the integral coordinates U,V put every e*U^n with n=2 mod4 in the actual C4-fixed module. For any nonzero operator, its least augmentation-degree coefficient is detected by a nonzero power series evaluated at 6^n-1. The Strassmann argument applies to f(5z), whose coefficients tend to zero. The distinct nonzero leading augmentation orders yield actual Q5-linearly independent outputs. This proves the needed infinite rank, as well as faithfulness, rather than assuming a formal operator representation is faithful.

Evaluating the invariant operator cocycle on these actual fixed inputs gives integral continuous cocycles on P, extending by zero to the chosen C4 complement. If such a cocycle is principal, the special h component determines its primitive uniquely and forces the detecting operator to vanish. Thus the class map has infinite rank. D.47 identifies the finite-ramification and unrestricted first cohomology and gives a compact countably based product of Z5's; D.35 gives torsion-freeness. Infinite rank excludes every finite product and proves the countably infinite product conclusion. Fixed abelian coordinates leave at most one class in each cusp packet; rational points are countable. The uncountability conclusion is restricted correctly to already nonempty fibres, including cusp fibres.

## Primary sources independently opened

- Venjakob, *A noncommutative Weierstrass preparation theorem and applications to Iwasawa theory*, https://arxiv.org/pdf/math/0204358, Example 2.3 and its preceding construction, printed pages 5–6. Opened references `turn950view0`, `turn951view1`. The uniform semidirect product meets the displayed hypotheses.
- Venjakob, *On the structure theory of the Iwasawa algebra of a p-adic Lie group*, https://arxiv.org/pdf/math/0106269, Theorem 3.26, printed page 18. Opened references `turn950view1`, `turn951view2`. This supports the general ring assertion; the draft also gives a direct proof in its particular ring.
- Milne, *Arithmetic Duality Theorems*, second edition, https://www.jmilne.org/math/Books/ADTnot.pdf, Chapter I, Theorem 5.1, printed page 67. Opened references `turn952view0`, `turn953view0`. The complex-place factors give 5^(-2), hence 1-d+h=-2, for the trivial F5 module over Q(zeta5).

No proof gap or required correction found. This audit does not promote the remaining compact H2 calculation, existence for arbitrary abelian pairs, or any explicit first higher-derived obstruction.
