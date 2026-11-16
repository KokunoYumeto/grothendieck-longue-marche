# Root audit: the three-primary component of C.31

**Verdict: PASS for the three-primary component only. C.31 remains Open.**

This audit combines the separately retained full homology-comparison audit (`root_C31_three_layer_bound_audit.md`) with a complete read and independent execution of both original-row verifiers. It approves a separately numbered partial theorem; it does not approve a full iterated-parity witness.

## Actual quotient and homology

The original 176-generator pc source and its normal cuts were checked on every power and conjugacy relation. The two-primary kernels do not change integral three-primary homology. For the elementary three-kernels of ranks 9 and 18, the indicated normal two-subgroup has zero coinvariants on the kernel, so averaging gives vanishing of all quotient homology with that coefficient module. The alternating-square coinvariant dimensions are respectively 1 and 0. The Lyndon–Hochschild–Serre argument therefore gives an isomorphism for the **actual** quotient H_2(G_176,Z_3) -> H_2(G_26,Z_3), not an abstract comparison of group orders. The remaining rank-nine layer and the order-54 base give annihilator 9. The root independently derived the base bound from its C_3^2-by-C_6 presentation and the invertibility of minus-U minus 1.

The quotient source is obtained from the actual normal quotient. Target and frame words were recollected with the original collector; the failed raw-tail truncation approach remains documented and is not used.

## Exact trace expansion

The root read `pbc_verify_quotient26_primary.py` in full. Its source hashes, quotient checks, strict DAG order, allowed operations, source header, coordinate bounds and final coefficient checks were reviewed. The 16,278-node trace expands to a target coefficient of exactly 1. Every used source identity and target/frame word is recomputed by the retained original GAP collector; no searched Hermite basis supplies authority. The root also read the complete original GAP replay body and the coordinate-bound derivation. The associativity, commutator and power-overlap identities are evaluated as original free-source relator differences. The three defining target differences cancel in the free-source abelianization, putting the target in the Schur multiplier.

The first verifier replays 443 original leaves. Coordinate reductions are justified by explicit Bezout combinations of original power rows and the modulus, rather than by an assumed presentation of the searched lattice.

## Literal original-row identity

The stronger `pbc_expand_quotient26_original_identity.py` was read in full and independently rerun. It removes every coordinate and modulus leaf before summation, then eliminates the residual using explicit integer multiples of original power-consistency rows. Its final exported witness consists solely of the target with coefficient 1, genuine frame-commutator rows, and original identity rows. The complete 351-coordinate residual is exactly 9 times the exported integer vector. A second independent summation uses only the exported ledger, and GAP replays all 442 final original leaves afresh.

All remaining r-frame coefficients are divisible by 3. Their genuine commutators have order dividing 3, so they vanish integrally. There are no power-word corrections and no s-frame corrections. Thus the torsion target is zero modulo 9. Since 9 annihilates the actual three-primary multiplier, its three-primary component is zero; the actual quotient isomorphism carries this conclusion back to G_176.

## Independent execution and retained evidence

Root copies change only output names so that the original programs and outputs remain intact:

- `code/root_C31_verify_quotient26_primary.py`
- `code/root_C31_expand_quotient26_original_identity.py`
- their separate generated GAP files, GAP logs, JSON results and root console outputs.

Both executions passed. Every mathematical JSON field and both generated GAP source hashes match the author execution. The only differing fields are executable/output provenance and runtime. The two GAP logs match exactly after normalizing only their reported runtime integers. The initial comparison that detected the differing log hashes is recorded in `root_C31_initial_comparison_diagnostic.md`; it was not silently discarded. Exact hashes and comparison scope are in `root_C31_original_row_rerun_verification.json`.

The separate two-primary target, including the two top-layer binary coordinates, is not settled by this audit.
