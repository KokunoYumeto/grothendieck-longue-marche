# E.29: complete rational-pair calculation for the inherited cubic quotient

For every a,b in Q*, the inherited class-two pro-3 quotient admits a section with toric pair (kappa_a,kappa_b) exactly when every tame residue theta_q(a,b) has3-primary order at most9. Each nonempty fibre has exactly three conjugacy classes. Given one cocycle, its three representatives are obtained by adding j(chi_3²−1)/3 to its central coordinate, j=0,1,2.

The obstruction is9 kappa_a cup kappa_b. The proof constructs the integral Steinberg symbol in continuous cohomology from actual rational-point sections of P1 minus{0,1,infinity}, then uses the opened K2(Q) localization calculation. An explicit local tame residue detects the3-primary part. This proves both directions without a global inverse-limit injectivity assertion. The coefficient group H¹(Q,Z3(2)) is computed using tame inertia, Hain–Matsumoto Theorem7.2, and the explicit invariant1/3 in Q3/Z3(2).

The quotient and arithmetic normalization are explicit. The cubic inclusion multiplies toric coordinates by3 in the base group, giving commutator coefficient9. The inherited class-two group receives the intrinsic rank-ten class-two quotient by the displayed surjection. E.29 does not identify these quotients or claim a classification for the larger intrinsic quotient.

## Computations run

`code/e_rational_pairs.py` completed with all assertions passing. It checked40,000 positive integer pairs1<=a,b<=200;39,378 satisfy the criterion and622 fail. Counts by maximum3-primary residue order1,3,9,27,81 are19,036;15,198;5,144;364;258. It also checked101,124 ordered pairs of318 signed rationals of height<=16, all admissible, and317 exact Steinberg identities. All obstructed integer pairs are recorded in the JSON output. The three central cocycles and invariant counts were checked modulo3,9,27,81.

Examples: (6,109) has residue3-order27 and is obstructed; (6³,109) has order9 and three classes. (2,163) has order81 and is obstructed; (2⁹,163) has order9 and three classes.

## Scope retained for the next step

The rational-pair statement is complete. General completed Kummer pairs can have infinitely many prime coordinates tending to zero3-adically; their cup products require controlling the global continuous inverse-limit issue. That further problem is being investigated separately. No local-to-global criterion for those infinite pairs is asserted in E.29.
