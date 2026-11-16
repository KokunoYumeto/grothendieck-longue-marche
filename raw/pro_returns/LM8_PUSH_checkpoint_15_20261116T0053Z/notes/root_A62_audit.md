# A.62 complete independent root audit

**Full proof audit PASS, 15 November 2026, 20:34 UTC.** The entire candidate `notes/fgh_A62_draft.tex` was read, including its actual translation comparison, algebraic charts and all cusp positions. This is a uniform argument for every prime congruent to one modulo four, not an extrapolation from finite computations.

## Source scope and the actual isogeny

The Hasse coefficient is the indicated nonzero binomial coefficient. I freshly opened Silverman's primary *Arithmetic of Elliptic Curves* PDF at Theorem V.4.1(a), printed p.148, and Theorem III.6.2(a,c,d), printed p.83: https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf . The exact current retrievals are `turn974view1` and `turn974view0`. The earlier complete III.3.7 division-polynomial check remains applicable.

The degree-p CM endomorphism must be justified using duality, not merely the existence of a Gaussian factor. The dual of [i] is [-i], and duality is additive; therefore the dual of the selected Gaussian endomorphism is its conjugate. Their composite is [p], so III.6.2(a) gives its degree p. Its unit differential makes the kernel finite etale over the good integral model, and the other factor is connected in the special fibre. This supplies actual unramified p-torsion sections. The author was asked to make this duality citation explicit.

The reduced division numerator and denominator have the asserted inseparable degree and relative primality. This gives the actual Frobenius-root polynomial g and its divisor. The degree of h and the exact pole order p−1 of H_0 at O are correct.

## The comparison modulo p squared

For a section T of the etale kernel, the characteristic-zero division divisor gives the exact ratio c_T k_T^p. The Gauss valuation has value group Z because the coefficient extension is unramified. Scaling k_T to a Gauss unit forces c_T to be an integral unit. A lift of its residue p-th root exists in that same unramified ring. Frobenius injectivity in the special function field then proves that the displayed ratio q_T is 1 modulo p, so its p-th power is 1 modulo p². The remaining discrepancy c_T/gamma_T^p is a constant. Consequently H_0 changes by a constant modulo p under every reduced torsion translation. Its differential is therefore genuinely invariant under the complete etale kernel.

This argument is carried out in the actual function field and Gauss DVR. It does not infer differential invariance just from the reduced branch divisor, and it does not replace divisibility by p with divisibility by a ramified uniformizer.

## Descent and critical multiplicities

I checked the differentiated division identity and the signs in DF=−DU. The logarithmic differential of the translated g ratio is regular because every divisor order is divisible by p. Hence DU descends to L(2O) on the actual quotient elliptic curve. Quarter-rotation removes its constant term. The leading coefficient at O gives DU=−mu² x∘alpha and hence Df=mu x for the actual descended F.

The etale descent and the exact pole at O imply that f has precisely one pole, of order p. Oddness forces a zero at (0,0). The right side mu x has order two there; because p≥5, the primitive has exact order three. Every other zero is simple. This accounts for every zero, giving p triple and p(p−3) simple centres upstairs, all away from the reduced p-torsion. The finite two-torsion points at x=±1 are among the simple centres. No lower hidden degree-p term can interfere because the chart degrees are two and four, both strictly below p.

## Actual models and marked points

The main Kummer substitution has special field k(E)^(1/p) and ordinary elliptic normalization. In the tail charts g(a) is a unit. The exact binomial identity, the numerator N_a, both kinds of elliptic local parameters, and all coefficient valuations check. The retained Artin–Schreier terms have degree two or four. The given uniformizer has valuation one and translated difference of valuation k+1, giving genus (p−1)(k−1)/2.

The positive-genus valuations persist by the already fully audited common-regular-resolution argument. Their total genus equals the characteristic-zero genus; hence every other component is rational and the graph is a tree. The actual degree-p main map exhausts the degree of q, so every off-main subtree is constant under that map. The etale/connected CM decomposition gives exactly p generic torsion points over each of the p reduced torsion points. Those p marks must be separated on a rational marked tree, away from all positive-genus tails. Thus the precise rational-path hypotheses of A.42 hold. A.59 supplies the all-prime normalizer conclusion for the actual p-group cover.

The same characteristic-zero Heisenberg group argument used in A.61 applies, since it required only that p be odd. Combining A.61 and A.62 therefore covers every odd prime, without a cofinality or universal finite-cover assertion.

## Exact certificate and presentation

I inspected the complete finite certificate. It checks the actual reduced division polynomial, the Verschiebung coordinate and elliptic identity, the descended differential, all critical multiplicities, their avoidance of reduced torsion, the valuation inequalities and genus exhaustion. A root rerun at p=5,13,17 is retained as `notes/root_A62_certificate_rerun.out`. PBC independently reran and compared every resulting prime row, and separately audited the entire proof and primary source scope.

Two exponent-comma typographical errors were identified for repair before integration. They do not affect the argument. The corrected canonical text is required to cite the dual-isogeny properties used above explicitly.
