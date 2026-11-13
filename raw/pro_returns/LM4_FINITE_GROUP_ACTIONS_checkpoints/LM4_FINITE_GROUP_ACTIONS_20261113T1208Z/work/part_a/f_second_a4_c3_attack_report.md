# Exact common-C3 comparison for the remaining A5 centralizer

The auxiliary TeX note records the exact map and the remaining intersection. It is not a new proof that the full residual centralizer is trivial.

The specified `C3=<r>` is common to the A4 stabilizers of the fourth and fifth letters. The involution `beta=(12)(45)` normalizes it by inversion and generates A5 together with the first A4. Descent by this actual C3 gives an injective map from its pure centralizer to a finite-index subgroup of `PΓ_(0,6)`. The established prime-power comparison and induced topology give the same injective map on full completions. Restricting to the actual A4 centralizer produces the displayed embedding `Fhat13 → PΓhat_(0,6)`.

This embedding is the actual six-point quotient configuration, with its two branch points and four C3 orbits. It has not been substituted by one of the six- or seven-point forgetting maps. The note displays every coordinate and label, derives the normalized involution `(s1,s2,s3) → (s1,s1/s3,s1/s2)`, and supplies the exact based transport from the icosahedral configuration to F.9's basepoint.

The residual A5 centralizer is exactly the fixed subgroup of this based involution inside the displayed embedded `Fhat13`. The proof uses injectivity of the actual C3 quotient homomorphism and the equality `<A4,beta>=A5`; it uses no closure-of-intersection assertion.

The exact certificate `code/second_a4_c3_attack.py` passed all 180 matrix product checks and 720 vertex-label checks, together with the quotient, normalization, and fixed-locus identities. JSON and stdout are adjacent. The pullback of the geometric fixed locus is finite, but that fact has not been used to infer an intersection identity on completed fundamental groups.

The numerical C3 Johnson probe remains a separate exploratory artifact. Its first nonzero outer class gives no exclusion; it does not certify the full based monodromy or a finite quotient separating the F.9 word. F.10 supplies an unconditional procyclic exclusion through a different explicit family of finite representations.
