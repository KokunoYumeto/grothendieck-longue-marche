# Current scope after the complete C.31 audit

C.31 is now canonical **Proved**. The full map
`(Delta, Delta D, Delta D^2): GT0 -> C2^3` is onto, already on
multiplier one, and all three characters kill the full specified Galois image.
The full proof, root/DE audits and complete successful source comparisons are
listed in `notes/pbc_C31_row.json` and `code/pbc_C31_finite_assembly.json`.

The successful G86 literal certificate was produced by a cloned quotient-only
verifier whose final `scope` string still describes the original top-kernel
question as open. That string records the scope of the standalone quotient
test and its earlier template; it is not the current project conclusion.
The exact certificate and executable source remain as executed and independently
replayed, with their original hashes. The subsequent assembly uses the separately
verified two actual central covers to settle that kernel, and then supplies
the actual full profinite lift and both normalization comparisons.

The older native-collected G86 attempt failed its original-source replay. Its
retained trace is reproducibility/history material and contributes no mathematical
identity to C.31. The fresh standard-GAP-row calculation is a distinct successful
run, with every final original source row replayed.

The following boundaries remain open: independence of every later iterate,
the restriction of Delta to the pentagon group, the prime-three arithmetic-trivial
character space, and a full presentation of the arithmetic-normal abelianization.
