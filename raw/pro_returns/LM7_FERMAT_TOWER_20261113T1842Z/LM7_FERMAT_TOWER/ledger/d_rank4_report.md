# D.30: a rank-four obstruction and a compatible replacement

**Proved progress; the genuine full profinite CM image remains incomplete.**

The exact map Q→S3×C3 is induced by reduction modulo2 and by SL2(F3)→SL2(F3)/Q8. Its kernel is O2(Q)=C2²×Q8 of order32. Thus K=ker(B→S3×C3) is free rank4, and N is its normal subgroup of index32. The full pro2 topology on N is induced from K, by taking normal cores of two-power-index subgroups. This identifies the same relative pro2 completion with a free rank4 kernel over the order18 quotient.

The first new test is the Zassenhaus quotient B/D7(K). The restricted Hall-power basis gives graded dimensions4,10,20,70,204,690 through degree6. Since N⊂D2(K), gamma3N starts in degree6; N^4 and[N,N]^2 start in degree8. The degree6 gamma3N subspace has dimension240. This is therefore a new nonabelian refinement of the previous N-class-two calculations, even though its graph basis has only four generators.

## Exact rejection of two selected central representatives

The initial central correction ranks are227 on the240-dimensional gamma3N layer and648 on the full690-dimensional layer. To exhaust lower-conjugator freedom, compute P=image(N in K/D6). It is class-two exponent4 of order2^303. Its central elementary Frattini subgroup has dimension225 and its Frattini quotient dimension78. The fixed spaces for s have dimensions117 and42. The additive connecting map from the fixed quotient to the coinvariant central subgroup has rank7, leaving35 liftable quotient directions. Fixed central elements and corrected lifts give152 explicit generators of the full centralizer.

Their actual degree6 defects raise the full correction rank to654. The targets for both D.27's original alternate H2 central representative and D.29's retained changed representative remain outside. Saved linear functionals annihilate all correction columns and take value1 on each target. The code also checks that t=(sr) has order48 at both stages, so no multiplier change preserving the lower action contributes a missing degree6 column.

For a genuine full lift, the original Herfort–Ribes torsion theorem supplies elliptic conjugators. The retained G6 action fixes their Q coordinates by D.25.6. This condition is used jointly with the K/D6 action: the latter alone has smaller Frattini data and cannot replace G6. The computed N-centralizer freedom is therefore exhaustive for the stated two selected representatives. Their full lift is excluded. Other homology or central actions with the same CM pair are not excluded.

## A new compatible seed

The initial central coordinates can be changed while retaining the original homology masks, right-centralizer data and G3 conjugators. Their images form an abelian module in both the rank97 Z/4 class-two quotient and the rank4 degree6 quotient. The previous4769-dimensional central relation space is subjected to fifteen Z4 constraints and thirteen gamma3N degree6 constraints. The joint matrix has full rank28, and the code solves it exactly.

The final correction uses actual gamma3N words, so it vanishes in every class-two quotient of N. One2,944,468-letter B cusp word, collapsing to562,814 rank4 letters, is checked directly in both models: all rank97 Z/4 degree-one/two coordinates vanish, and all rank4 mod2 terms through degree6 vanish. Its multiplier is1. Generation holds by the original rank97 Frattini map and by the identity on K/D2(K)=O2(Q)^ab.

The exact common quotient of the two finite groups is B/(gamma3N D7(K)), of order576*2^753. Their combined quotient has order576*2^9843. Future D.29 corrections begin in D8(K), so the same new finite action and conjugators survive the entire infinite class-two tower. The two-primary target is exactly P2/(closure(gamma3N) intersect D7(K)); its N-kernel has class3, third lower-central subgroup C2^240, and trivial fourth subgroup.

The unchanged homology and G3 data preserve the D.28 mixed-prime compatibility. All odd relative pro-p kernels are retained as before. One global cusp gauge gives the compatible nonarithmetical finite shadow family on characteristic refinements retaining G6 and CM data. The original central representatives and their rejection certificates remain separately saved.

## Sources, reproduction and limits

The opened primary source for the exact restricted Hall-power basis is Ido Efrat, *The p-Zassenhaus filtration of a free profinite group and shuffle relations*, JIMJ22(2023),961–983, Proposition4.4; Lemma2.2 fixes the Lyndon standard factorization. The original arXiv PDF page10 was visually inspected, and the official publisher full text and metadata were checked. Its verified bibliography key is dEfrat2023.

Programs and outputs are `d_cm_rank4_refine`, `d_cm_rank4_centralizer`, and `d_cm_rank4_joint` in the code directory, each with `.py`, `.out`, and `.json`. All three were independently rerun and audited by agent A, including the complete centralizer generation argument, cusp multiplier order, joint rank28, both direct word checks, exact common quotient and stability of the infinite extension. The retained G3 conjugators are separately selected odd-primary components of the fibre product; the displayed discrete two-primary correction word need not have the original G3 abelianization.

The new quotient retains only a specified part of the third lower-central layer of N. It does not settle every higher two-primary or mixed finite quotient. Genuine full GT0 realization of the new replacement and of its CM pair remains the all-finer-quotient problem in D.22.
