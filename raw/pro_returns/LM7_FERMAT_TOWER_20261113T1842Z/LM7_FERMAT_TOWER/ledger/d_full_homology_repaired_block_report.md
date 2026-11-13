# D.58: full arithmetic homology and the repaired invariant block

## Proved result

The exact D.57 action, including one compatible pair of normalized conjugators, extends to

`Y = Bhat / (R_h intersect M_infinity intersect L_{*,2})`.

The projection to the D.57 source has kernel `L = ker(U^- -> U_*^-)`, a saturated free Z2 module of rank `w-640`. The projection to the full D.50 homology source has kernel `Z_*`, of dimension 210240. The extension keeps the complete actual small class-two action, the prescribed `W_h` action, and the literal normalized parameter. Its full arithmetic homology action is newly repaired; it does not preserve the old D.50 homology representative.

The exact source-image calculation is `image(S57 -> U) = L`. The reverse inclusion uses one actual preimage in `R_h` and a correcting preimage in `R50 -> Z_*`. This proves the image of the intersection, rather than inferring it from two unrelated images.

## Common quotients and generation

At homology level `2^k`, the maximal common quotient is `J_k/L_k`. The D.57 action descends because the image of `K_3` is invariant and its abelian exponent-`2^k` quotient is characteristic. The proof therefore retains the actual D.57 conjugators without assuming a centralizer lift into the older homology representative.

At the first level, the cusp correction is onto because `L_A=0`. The nilpotent Fitting summand of the exact regular edge chain map lies inside `L`, is projective, and admits the cyclic norm repair used in D.50. The corrected map is invertible and leaves the complete common quotient fixed. At higher levels the exact common kernel is `2^(k-1)L_k`; saturation proves that identity, and the same cusp correction gives compatible automorphisms and conjugators in the inverse limit.

## Further actual class-two extension

With `K = ker(Z -> Z_*)`, the exact quotient is `Y = X/K`, where `X` is the full D.54 source. Odd averaging splits `K = K_0 direct_sum K_1`, with `K_0=K^A`. The remaining moving module `K_1` has zero A-coinvariants. Actual central corrections therefore extend the constructed action to `X_58=X/K_0`.

The exact dimensions are:

- `dim K = w*rho - w*(w+1)/2 - 210240`;
- `dim K_0 = m^2*(q-1)/2 - 2560`;
- `dim K_1 = w*rho/2 - 207680`.

The result retains the complete original moving class-two module and all 2560 invariant coordinates already solved over the actual order-3888 arithmetic quotient. All maps use the actual huge group `G_3`; no order-1080 or other finite prototype is used to infer a lift.

## Exact remaining task

The map `X -> X_58` has kernel `K_0`, and its source preimage is exactly `R58` in (D.58.9). Its nonzero dimension supplies an actual surviving source element via the proved onto map `R50 -> Z`. The next boundary obstruction for the constructed action lies in `(K_0)_G`. That class has not been evaluated here. The full arithmetic invariant class-two problem and full profinite GT0 realization remain unresolved.

## Verification and provenance

D.58 is a proof-only extension. It introduces no claimed new numerical run. The exact arithmetic inputs and source maps are the already checked D.49-D.57 results. The control/display/environment lint passes with 17 unique equation tags. Parent and peer proof audits are pending at this freeze.

## Completed root proof audit

D.58 retains the complete D57 action and actual conjugators while restoring the full integral G3 homology through a projective Fitting repair inside L=ker(U-minus to U-star-minus). The exact source Y has kernel L over X-star and Z-star over Z_h. It further extends through the entire remaining moving class-two module to X58=X/K0, where K0=ker(Z to Z-star)^A. All2560 solved invariant coordinates remain, and the exact residual invariant dimension is m^2(q-1)/2-2560, at least366080. The actual boundary in (K0)_G and the full profinite realization remain active.

The entire frozen proof and the exact D50 repair construction were read. Every frozen file and dependency hash matches. Root audit: ledger/root_d58_audit.json.
