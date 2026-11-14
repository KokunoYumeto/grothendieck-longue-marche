# E.32: every completed inherited cubic class-two toric pair

The classification now covers the entire completed pro-3 Kummer domain. Its central corrections are explicit convergent sums of finite-field Kummer logarithms. A fibre is nonempty exactly when each correction is integral and the family of corrections tends to zero 3-adically across the primes. Each nonempty fibre has the three explicit twists already computed in E.29.

The proof computes the actual continuous cohomology group as

`H2_cts(G_Q,Z3(2)) = R / diag(q-1)R`,

where R is the group of restricted Z3 sequences indexed by primes q other than3. The denominator is the actual image, with no closure. The localization morphism is constructed by first taking the direct limit over finite sets of removed primes at each coefficient level, and only then taking the derived inverse limit over3-powers. The residue-field complexes have surjective transition maps on both terms. Vanishing of H2 and H3 over Spec Z[1/3] is proved from the unique cyclic cubic extension unramified away from3, Milne's global Euler characteristic, and his odd-coefficient real-place result. Thus the calculation accounts for the full derived inverse limit.

The obstruction representative is verified at the cochain level. The alternating cup cocycle is zero on two inertia arguments, so its central-zero inertia splitting is defined. Frobenius conjugation has defect `q((q-1)c+9(A b-B a))`; dividing by q gives the residue complex's cochain. Its central coboundary has the exact sign and coefficient q-1. Restrictedness follows because each term contains one of the completed valuation coordinates, which tend to zero.

The theorem constructs an actual completed toric pair for which every local obstruction and every finite-coefficient global obstruction vanishes, while the continuous obstruction remains nonzero. Choose primes q_j congruent1 mod3^j with3 a noncube modulo q_j; the completed exponent at q_j is `(q_j-1)/(9 r_j)`, where r_j is the unit Kummer logarithm of3. These exponents tend to zero, but every required central inertia correction equals−1. Every finite-support partial pair has a lift, and the full completed pair has none. This provides a concrete obstruction to discarding lim1.

The independent finite program passed:

- 7,200 tame semidirect relations;
- 7,200 coboundary and Frobenius changes;
- 6,000 two-cocycle identities and cup-product signs;
- 6,000 coefficient transitions;
- 40,000 comparisons with independently computed rational tame symbols:39,378 admissible and622 obstructed;
- the first ten prime/exponent choices for j=3 through12, and finite support primitive transitions through3^12.

The first witness primes are109,163,487,1459,39367,131221,196831,1299079,5314411,8503057. Their central corrections are all−1. The finite code is evidence for the explicit formulas; the infinite existence and nonconvergence are proved in the text.

The result classifies the inherited quotient H, with the exact intrinsic-to-inherited map(E.29e). The intrinsic obstruction E.31 remains necessary for the cubic's own rank-ten class-two quotient. No intrinsic classification is inferred from the inherited calculation.

The Part B/C author independently audited the complete mathematical proof, including the support complex, the chain-level representative, and the completed-pair example; no gap was found. Root owns the shared bibliography entry E_MilneADT; the new bibliography supplies E_JannsenContinuous and E_MilneCFT.
