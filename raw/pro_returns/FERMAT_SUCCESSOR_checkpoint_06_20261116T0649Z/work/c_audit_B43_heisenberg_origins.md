# Independent audit of the actual Heisenberg cusp-origin projections

Date:2026-11-16. Inspected draft: `work/b_dilog_bridge_proof.tex`, together with the exact scripts. Verdict: the cover, arithmetic descent, endpoint comparison and integral shift rows pass, **with the explicit deck-versus-fibre marking correction communicated to B and root**. Raw deck values and intrinsic Hall coordinates have opposite signs in degree two.

## Maps, divisors and actual tangent scalars

For `f1=(1+ζ)X/(Y+Z)`, the denominator is the flex tangent at A0. The numerator of1−f1 is the secant `Y+Z+ζ²X` through A0,B1,C2. Consequently

\[
\operatorname{div}(f_1)=A_1+A_2-2A_0,\qquad
\operatorname{div}(1-f_1)=B_1+C_2-2A_0.
\]

At O=C0 the value is ζ². With `s=X/Z` at A0, write `Y/Z=−(1+s³)^{1/3}`. This gives `1/f1=(ζ/3)s²+O(s^5)`.

For `f2=X/(X+ζ²Y)`, the denominator is the flex tangent at C1; its numerator and the numerator of1−f2 cut the three A and three B cusps. Thus

\[
\operatorname{div}(f_2)=A_0+A_1+A_2-3C_1,\qquad
\operatorname{div}(1-f_2)=B_0+B_1+B_2-3C_1.
\]

Its value at O is `1/(1−ζ²)=(1−ζ)/3`. At C1, the parameter `s=Z/X` and `Y/X=−ζ(1+s³)^{1/3}` give `1/f2=−s³/3+O(s^6)`. These independently derived orders and leading constants agree with the draft. They are essential to the marked cusp comparison.

## The explicit cover and its arithmetic descent

The radical cover `u^m=t`, `v^m=1−t`, `w^m=∏(1−ξ^i u)^i` has no branch away from0,1,∞. The displayed coordinate transformations a,b preserve its equations and generate a free transitive action on the m³ geometric fibre points. Their positive continuation at the marked zero tangent produces the generators of the class-two exponent-m quotient. Since m is odd, this group is exactly the characteristic free quotient of rank two with class two and exponent m. Its markings yield the compatible tower; an identification of unrelated finite root choices is not being inferred from numerical coincidence.

Choose ξ compatibly with `ξ_m^{m/3}=ζ`. Reindexing j=ci modulo m gives the exact exponent identity

\[
E_{m,\xi^c}(u)=E_{m,\xi}(u)^{r_c}
 \Big/\prod_j(1-\xi^ju)^{m\lfloor r_cj/m\rfloor}.
\]

It proves the proposed semilinear lift of w. The constant-one Puiseux normalization removes the residual root-of-unity ambiguity and gives its composition law. Thus this is actual arithmetic descent, not only a geometric cover over the cyclotomic field.

## Endpoint Frobenius and the corrected sign

The leading constant at infinity is

\[
c_\infty=(-1)^{(m-1)/2}\xi^{\sum i^2}
 =(-1)^{(m-1)/2}\zeta^2.
\]

At the stated primes, ζ,1−ζ² and hence `3=−ζ(1−ζ²)^2` have mth roots. Both source tangent constants and c∞ therefore have mth roots in the residue field. The three radical coordinates have Frobenius-fixed Puiseux leading coefficients at the source cusp; the higher units lift uniquely. The actual marked cusp fibre is fixed by Frobenius.

At the ordinary O fibre, the exact finite calculation gives the central **deck** element h^k, with h acting by `w->ξw`. The relative cusp section is therefore the deck element h^(−k). This ratio is independent of a connecting path because both relevant deck images are central.

However h is not the intrinsic fibre-functor Hall generator `[y,x]`. Label a geometric fibre by `g·p0` using left deck maps. Positive continuation commutes with deck maps and acts by right multiplication `R_a:g->ga`, respectively R_b. Functional composition gives

\[
c=[R_b,R_a]=R_{a^{-1}b^{-1}ab}=R_{h^{-1}}=h^{-1}.
\]

Thus the ordinary point Frobenius h^k has intrinsic coefficient−k, and the relative cusp deck element h^(−k) has intrinsic coefficient **+k**. This is the same reversal of the degree-two sign as the chronological-to-fibre calibration in B.40. The finite numerical calculations of k do not change. The table must label both conventions or use the corrected intrinsic sign.

## Independent integral reconstruction

`work/c_B43_origin_audit.py` reconstructs both boundary parameters from the literal six-term and eighteen-term formulas, obtains each translation from the actual nine-point permutation matrices, and reconstructs both degree-one maps from the written divisors and the integral gluing matrix U. It does not import either author's projected derivation as an input.

The unreduced integer calculation verifies the two projected derivation rows `(-9,0)` and `(0,-54)`, with the target Lie generator interpreted intrinsically as c. Applying the exterior map directly to the forced cusp-origin displacement gives intrinsic rows `(9,0)` and `(0,54)`. In deck-h coordinates these latter rows are `(-9,0)` and `(0,-54)`. Output and complete matrices are in `work/c_B43_origin_audit.out` and `.json`.

The author's finite radical-fibre program was also replayed successfully to `work/c_B43_finite_replay.out`. It checks all root choices, all stated arithmetic reindexing identities, endpoint constants and lower-level reductions for m=3,9,27,81.

## Exact scope

These are genuine projected origins in actual compatible finite covers, including the source tangent frames. They are not values of either isolated linear homogeneous cocycle. A nonabelian origin has a prescribed nonzero abelian part and satisfies a cup-product equation; its central coordinate becomes a linear difference only after a reference origin and the complete quadratic pullback are fixed. The nonzero value at a Frattini-trivial prime73 concretely demonstrates this distinction. The draft's refusal to identify raw k with a homogeneous arithmetic parameter is necessary and correct.
