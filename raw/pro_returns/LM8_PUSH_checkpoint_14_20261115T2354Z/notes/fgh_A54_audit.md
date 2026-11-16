# A54 audit record

Registered canonical source: sections/A_heisenberg_five.tex. Original notes draft retained.

Root full mathematical audit: **PASS**, with independent reruns of both the exploratory character-sum script and the complete A54 certificate. Output retained as notes/fgh_H5_frobenius_root_rerun.out and notes/fgh_A54_certificate_root_rerun.out. Root checked the actual quotient, sigma parity on the H-fixed line, the same primitive20 factor, Hodge signature, persistent global fields and the rational special-fibre centralizer argument. Minor TeX corrections and shorter discriminant displays requested and being applied.

PBC independent structural check: **PASS** for maximal-CM-part invariance, rank-one quotient implication, balanced-embedding centralizer dimension, and faithful global specialization. Completed full focused proof/code audit also **PASS**; ledger notes/pbc_A54_audit.md and exact rerun notes/pbc_A54_certificate_rerun.out.

DE independent full audit: **PASS**, including a separate elliptic addition-law derivation of the actual alpha=2−i quotient and its kernel label. Ledger notes/de_A54_audit.md; output code/de_A54_independent_audit.out.

Exact certificate: notes/fgh_A54_certificate.py/.json/.out, executed successfully. Its computations are quotient identity, normalized five-point Fourier matrix, multiplicity equations from actual quotient genera, primitive20 Hodge signature, primitive quartic CM-type stabilizer, complete F_q/F_q² character sums at41 and61, and all four finite square-class/persistence witnesses.

Scope restrictions are explicit: normalizer recognition only for ell not congruent1 mod5; full fixed group only at ell5. No pro-ell injection is inferred from the degree5 map to the tripod at ell other than5. The remaining split-prime A2 lines are actual residual possibilities, not constructed normalized subgroups.

Canonical certificate code/a_heisenberg_five.py/.json/.out, with root, PBC and DE rerun outputs. All requested TeX corrections and split displays applied. Source input, a_results row and the A45 frontier/register were updated while preserving A46.
