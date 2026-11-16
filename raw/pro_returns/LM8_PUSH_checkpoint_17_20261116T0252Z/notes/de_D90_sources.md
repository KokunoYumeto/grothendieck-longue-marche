# D90 exact-dependency and computation ledger

Status: unregistered notes-only candidate. No canonical integration before checkpoint15 save. The full candidate is `de_sha_dominant_valuation_cusp_draft.tex`; exact current hashes and independent replay are recorded in `de_D90_candidate_hashes.json`.

## Actual arithmetic inputs

D89's proof before its unit step gives the exact actual cyclotomic-kernel difference ideal(P,q_m). It uses the actual D82 kappa(5) saturation and D77/D82 primitive cubic element in its kernel, with D39 divisibility. D87 supplies the exact finite-global-localization comparison and the actual coinduced inclusion. For m<=r that inclusion lands in q_mR, so its invariant map is literally zero. The relative norm becomes exactly5^e moduloq_m; the retained q_r generator makes the remaining action rho0 after the Cartier untwist. These are all proved explicitly in the draft, with no new external theorem.

## New integral module proof

The ring C[C_(5^m)][[v]] has a nontrivial annihilator ofu. Its additional axis-intersection kernel C*v*Norm_m is retained, assigned its exact chi³ action, then killed by tame averaging; the cokernel has chi². The actual boundary is transported by augmentation and the integral diagonal half gauge to a weighted permutation module. Every cyclic factor C/(5^j) remains visible. The zero snake map is proved over every coefficient ringC, not inferred from dimensions.

For finiteC, the proof adjusts lifts using the explicit annihilator identity in productC to split each cyclic quotient. For C=Z5 it uses the natural reduction maps, the finite zero-snake injection, and5^hM=5^hE for h>=m. It thereby constructs integral finite-order lifts rather than assuming a split extension or inferring one from abstract end groups. The remaining finite lower-exponent factors are not absorbed into the infinite product. The free local boundary factor is zero because the five-valuation depthm is no larger than the away depthr.

## Exact executed boundary support

`pbc_D90_boundary_certificate.py/.json/.out` constructs literal integral matrices for the actual chi=2 axis action2(I+T)Perm, diagonal half gauge and weighted permutation action. It verifies the exact augmentation/gauge intertwiners and full integer Smith forms for m0,1,2,3, with dimensions1,5,25,125. It then records every reduced coefficient exponent e1 through5, covering e<m,e=m,e>m and m0. The DE independent execution is retained at `de_D90_boundary_independent_rerun.json/.out` and matches the entire author JSON. The action on the norm line is checked exactly. The shared shell and logarithm computations remain the already executed D88 certificate. No finite computation is claimed to replace the new all-depth splitting proof, and no diagnostic PDF is created.

The scope m<=r is explicit. The middle range r<m<N, arbitrary other dependent pairs and higher-derived obstructions remain separate.
