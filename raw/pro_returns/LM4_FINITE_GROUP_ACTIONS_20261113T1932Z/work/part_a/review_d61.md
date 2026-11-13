# Independent audit of D.61

**Verdict: PASS.** I read the full proof, metadata, and producer and reran `work/part_c/code/torus_negative_parameters_d61.py`. All 12,787 exact checks passed; captured stdout is in `work/part_a/d61_audit_stdout.txt`.

The full generation lemma is sound. A proper closed subgroup is contained in a proper open subgroup; the actual discrete punctured-torus cover associated to that open subgroup contains the original cusp as a degree-one boundary lift. Its degree exceeds one, so another boundary exists. The chosen boundary has nonzero homology over every prime field, contradicting membership in the closed commutator subgroup. For an endomorphism taking the commutator to a conjugate of a full unit power, the conjugated image contains the original commutator in its closed commutator subgroup after taking the inverse unit power. Surjectivity and profinite Hopficity then give invertibility.

Both standard extension identifications have genuine inverse generator maps. In the two-class case `w0=Y^-1 v0` has order two and commutes with X, and `Y=v0 w0`. In the one-class case `z0=X v0`, with `X=z0 v0` and `Y=v0 z0`, gives exactly the stated free profinite product. Their quotient labels agree with the chosen free kernels.

The outer-conjugator normalization is exact. The peripheral normalizer makes the unit multiplier unique. The centre-free extension map is uniquely determined by its restriction and quotient label. Its reflected image is uniquely `c^z v`; conjugation by `c^((i-z)/2)` reduces the exponent to its parity `i=0,1`, using divisibility at two and invertibility of two at the odd primes. Two normalized representatives of the same outer class differ by a c-power, and the reflection equation forces that power and the parity difference to vanish. There is no hidden conjugacy quotient in the stated parameter spaces.

The tuple maps satisfy the displayed commutator and intertwining equations. The generation lemma proves that their generator maps are full profinite isomorphisms. Conversely the normalized extension maps recover the exact tuples, including the actual other section class in the two-class case. The alternative formula `[z^2,v_i]=[f,alpha_i(f)]` and both basis images are correct.

Finally the parameter spaces are compact closed subsets: each full section class is a compact conjugation orbit, and all equations are continuous. The target is Hausdorff in the profinite outer group. Therefore the continuous bijections are homeomorphisms. The text retains the unresolved nonemptiness problem and makes no unsupported free-basis or geometric-conjugacy existence assertion.

No correction is required.
