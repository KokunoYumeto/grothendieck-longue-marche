# D.32: exhaustive degree-eight obstruction for the recorded D.31 action

D.32 proves that the specific T2 action recorded in D.31 has no torsion-conjugate peripheral lift to T3 and no cusp-power-preserving automorphism lift to the full relative pro2 group. This result concerns the recorded action. It does not exclude the entire CM pair or D.30's explicitly different earlier central representative.

## Exact computation

The direct reconstruction retains all 4,903,248 letters of the recorded cusp word. Its Magnus coefficients vanish through degree seven; its degree-eight error has 32,296 monomials. The restricted Hall layer D8(K)/D9(K) has dimension 8230. The group T3 has order 576 times 2^11563 and maps to T2 with kernel C2^8230.

The fixed-conjugator correction map has rank 7753. The cusp order changes from 48 to 96. The t48 column has 6561 monomials; the compatible multiplier change by144 gives the same column and raises the rank to7754.

The full lower centralizer is constructed through successive central extensions, using complete polycyclic sequences. The counts for N/D3 through N/D8 are 6,16,50,152,494,1666 in logarithmic base-two order. The connecting ranks are 1,6,3,13,7. At the final stage all generators have degree at least four, so the centralizer is elementary abelian; its degree-four through degree-seven dimensions are 37,102,348,1179. Including every generator's defect raises the rank to7777. The saved functional annihilates this entire image and pairs to1 with the target.

The exact G2 homology calculation has ordinary lower-central ranks 87,67,43,19,4,0 in degrees three through eight. The other restricted-power terms vanish as well, proving D8(K) is contained in Phi(N). Thus T2 retains G2. Normalizing a possible s-conjugator into F and projecting its lower centralizing difference to G2 puts that difference in the computed N-centralizer by D.25. The r-centralizer contributes no additional obstruction classes because order-three complements lift and are conjugate across a two-kernel. All multiplier changes retaining the lower action are included.

## Structural promotion to the full relative source

The preimage of the order-two subgroup of Q0 has index nine. Its Bass-Serre graph has nine edges, three order-two vertex stabilizers, and one free loop. The full induced pro2 topology gives the exact free pro2 product C2 coproduct C2 coproduct C2 coproduct Z2. Herfort-Ribes1985 section2 explicitly allows the class of finite two-groups; Theorems A-prime and B-prime apply. Every involution of the full relative group is conjugate to s. The graph normalizer quotient C3 permutes the three Sylow involution classes cyclically and yields C_P2(s)=<s>.

An r-image agreeing with the recorded lower action is conjugate with its prescribed lower conjugator by the coprime complement theorem. Hence every full relative automorphism lifting the recorded action and mapping the cusp to a power would supply one of the finite conjugator solutions already excluded. This proves the actual relative-source obstruction. It leaves all previously proved quotient automorphisms intact.

## Runnable certificate

Run code/d_cm_degree8_seed.py, then code/d_cm_degree8_centralizer.py; the latter invokes the complete central-layer calculation. The shared exact polynomial arithmetic is code/d_cm_degree8_magnus.py. The independent graph check is code/d_cm_degree8_sylow.py. All mathematical outputs and saved exact vectors are JSON/stdout files beside the programs. The seed and linear programs consume only those saved JSON certificates, not binary caches.

The first functional-extraction assertion caught a free-coordinate selection error in a partially reduced remainder. The corrected routine selects the highest unreduced pivot, and the complete rerun verifies annihilation and target pairing. All rank and centralizer counts were reproduced. The independent root audit reran the seed, the full corrected centralizer calculation, and the Sylow graph program; all certificate fields agree except elapsed times. The proof and original Herfort--Ribes source pages were also checked. The detailed audit is in root_degree8_audit_report.md.
