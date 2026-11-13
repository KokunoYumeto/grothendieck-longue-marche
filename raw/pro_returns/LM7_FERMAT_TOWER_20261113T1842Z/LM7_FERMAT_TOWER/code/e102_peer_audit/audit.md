# Independent audit of E.102

**Outcome: PASS.** I read the entire theorem and proof and the complete author program. I independently rebuilt the actual 990-dimensional degree-four kernel matrices from the frozen E.100 certificate and executed a separately written verifier. No author Smith routine was imported or called.

## Mathematical proof

The exact involution identity and trace give fixed rank 486 and negative rank 504. Since 2 is a unit in Z_3, the image of I+J is the complete fixed lattice, so C=(T-I)(I+J) presents precisely K_4/(T-I)K_4^J. The rank upper bound is exact and independent of any finite-precision torsion bound. The independent computation detects 486 nonzero pivots, so no hidden higher-valuation invariant factors remain.

For the saved integer representatives, B=UCV has B_11=DS with S=I+E and E divisible by 27. The displayed Neumann inverse and both block-triangular changes of basis have the correct left/right order. Their coefficients are integral: B_12 and B_21 are divisible by 3^7 while every diagonal entry of D divides 3^4. The remaining Schur block is zero by the exact rank equality. Thus the proof supplies actual integral basis maps, not only a finite list of elementary divisors.

The quotient map U_1 U, finite-coordinate reductions, inverse map U^{-1} U_1^{-1}, and continuous choice of finite representatives have the stated kernels and topologies. The finite order is 3^382 and exponent is 81. The transfer to section fibres uses the strict induced kernel and the actual nonlinear triangular maps already proved in E.100; no substitution of a graded matrix for the higher arithmetic action is made.

I reported one missing backslash before `longrightarrow` in E102.4. Root corrected precisely this typesetting error. The hash in audit.json is the corrected section, with no mathematical change.

## Independent computation

The independent program uses successive Schur blocks modulo 3: exhaust all unit pivots, divide the remaining block by 3, and repeat. Its reverse lexicographic pivot rule differs from the author's forward minimum-valuation rule. It independently obtains ranks 247, 144, 56, 30, 9, 0, 0 in valuations 0 through 6, leaving dimension 504.

It reconstructs every input matrix from the frozen Hall-coordinate data and checks the archive against these reconstructions. It verifies both saved inverse identities for U and V, recomputes the exact integer product UCV with explicit overflow bounds, and checks every entry of the diagonal congruence and residual top matrix.

It then lifts the block transformations independently two additional digits, checking the complete integral diagonal identity modulo 3^9. The inverse of S is computed modulo 3^13 before division by powers up to 81. Both orders of the block inverse identities and both orders of the ambient quotient-coordinate round trip pass. These checks cover the actual maps as well as their invariant factors.

The full author Smith implementation was not rerun by this peer; root separately owns that fresh-copy rerun. The peer certificate is a genuinely separate calculation with complete output and source hashes retained.
