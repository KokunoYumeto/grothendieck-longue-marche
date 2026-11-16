# Independent D/E audit of A.52

**Verdict: PASS, including every positive integer m.** The complete updated draft `notes/fgh_A52_draft.tex` was read, together with the residue-two construction in A.50 and the exact geometric hypotheses of A.41–A.42. Two bare display closers were reported to FGH and corrected. No mathematical correction is needed.

## Actual three-adic components

The coordinate changes are invertible over the fraction field and retain the actual function field of C. The two integral equations were checked term by term: the linear term of f at each a=0,1,-1 vanishes, the quadratic and cubic coefficients are 6 delta and 12a, and division by 3 eta gives the displayed second equation. Both equations are monic after multiplying by units in their respective X and V variables, so the chart is finite free over the valuation-ring polynomial ring in U. Its reduction has unit pivots in U and V and is the smooth integral Artin–Schreier curve V^3−V=X^4.

The pole-order argument proves irreducibility over the geometric residue field. At infinity t^3 V^2 has valuation one and its nontrivial translate differs by an element of valuation five, so the lower jump is four and the different is ten. Hurwitz gives genus three. The three valuations are distinct because their restrictions to E have three distinct centers.

The main chart was independently expanded exactly. Its special function field is k(E)((x^4+x^2)^(1/3)); the differential is y^2 dx, which is nonzero, so this is the unique purely inseparable extension k(E)^(1/3) of degree three. Its normalization is an elliptic curve, and its valuation lies over the generic point of the elliptic special fibre. The generic point is smooth in the displayed chart, so normalization and regular resolution preserve its residue function field.

The comparison with the stable model is valid: take a common regular resolution of the chart compactifications and a regular resolution of the already existing stable model. Exceptional prime divisors in a birational morphism between these regular arithmetic surfaces are rational. Consequently none of the four positive-genus residue curves can disappear. Their genera already sum to ten, so the stable genus formula forces a tree and no further positive-genus component. This argument is independent of A.51's quaternion calculation. Deuring–Shafarevich gives three-rank zero for each Artin–Schreier component, and the elliptic component is supersingular.

The map q extends to the elliptic good model: resolving indeterminacy creates only rational exceptional curves, which map constantly to the elliptic special fibre and hence descend through the contractions. Its degree on the main component is already three. Constancy of the total pullback degree forces all other component maps to be constant. The main map is radicial, so each target reduction class has a unique possible attachment point on it.

## Marked clusters

For odd m, write 3m=3^h n with n odd and prime to three. Reduction of the target torsion has support E[n], and it avoids the three nonzero two-torsion points supporting the positive-genus tails. All connecting chains to those tails also map to these excluded points. The marks in each remaining class therefore lie in a connected rational tree attached to its unique main-component point. The origin class has 3^(2h+1)−18 marks and every other class has 3^(2h+1); each has at least nine. Separating coincident sections moves the whole cluster onto rational components, and marked stabilization contracts only rational components. Every cusp thus has a companion with a rational joining path including both endpoints.

For even m=2^a b, the actual normalized cubic map from A.50 extends between smooth proper models at two. Its nine branch sections stay distinct; it is tame of degree three and etale away from them. The special target torsion support is E[3b]. Above an ordinary target class, the three strict-henselian etale branches each receive exactly 4^a marks. Above a branch class there is one special source point, receiving one branch mark and three marks for each of the other 4^a−1 target sections, hence 3*4^a−2. Every source cluster has at least four marks. On the smooth proper source, its separation creates a rational marked tree. This verifies A.42 at residue two for every coefficient prime, including two. No wild quotient/reduction commutation is assumed in this step.

The all-m normalizer statement retains the actual punctured elliptic maps of A.50 on the smaller affine curve and the unchanged proper homology. Its use of A.11 and of A.50's map-detection argument is therefore legitimate. The converse for cusp inertia follows after a finite field extension making the cusp rational.

## Primary source checks

Independently opened Liu, *Algebraic Geometry and Arithmetic Curves*, actual book text at <https://rexresearch1.com/GeometryLibrary/AlgebraicGeometryArithmeticCurvesLiu.pdf>. Read Theorem9.2.2, Proposition9.2.5, Remark9.2.6 and Theorem9.2.7, printed395–397, and Theorem9.3.21, printed422. These give the exact regular-surface factorization, rational exceptional divisors, elimination of indeterminacy, and minimal-model comparison used above. Browser references: `turn787view0`, `turn788view0`–`turn788view2`, `turn789view0`–`turn789view1`. The first attempted mirror returned404; no result from that failed opening was used.

Independently opened Giulietti–Korchmaros, <https://arxiv.org/pdf/0801.3423>, formula(6), printed5, at browser reference `turn785view1`. Its cyclic-three specialization gives f−1=3(−1)+(3−1)=−1 exactly as used.

## Executed certificate

Independently executed the complete `notes/fgh_A52_certificate.py`, preserving its original JSON rather than overwriting it. Output is saved in `code/de_A52_chart_audit.out`. Every assertion passed: all three exact chart identities modulo rho^8+3, reduced equations and unit pivots, main chart modulo pi^3−3, nonzero differential, jump/genus/three-rank arithmetic, and both odd and even marking-count identities for m=1 through128. The universal count identities and geometric comparison are proved in the draft; the finite run is a check of the exact expressions and is not substituted for those proofs.
