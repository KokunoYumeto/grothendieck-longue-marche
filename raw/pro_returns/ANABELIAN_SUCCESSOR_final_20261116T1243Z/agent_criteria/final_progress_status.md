# Finite-field criteria: final stable-source status

Recorded 16 November 2026, 12:28 UTC, for the parent agent's 12:39 progress review.

## Integrated and audited

- `criteria_section.tex` contains AC.1–AC.45. AC.45 is the newest claim: the exact norm-module coinvariant description and realization of every class by a full arithmetic section, with nonzero classes non-point-theoretic after A1.
- `criteria_results.csv` includes AC.45. No aggregate outcome table was edited by this agent.
- `criteria_refs.bib` includes the verified Milne1986 Jacobian source for the characteristic-prime abelian fundamental-group comparison and the verified Oort2008 source for the L5 spectral test.
- `criteria_audit.md` records root, geometric_routes, and topos_reconstruction approval of the complete AC.45 proof, the exact F2 point-count certificate, the fixed-geometric-curve finite-prime limitation, and the final primary Iwasawa-source check.
- `norm_module_section_origin.tex` is the standalone AC.45 source. Its two unnumbered consequences give the F2 example and the finite-prime obstruction on the fixed explicit AG.38 geometric curve.
- `norm_module_small_curve.py` and `norm_module_small_curve_output.json` are the exact standard-library certificate for N1=N2=3, P(T)=1−T²+4T⁴, #J(F2)=4.
- `fixed_prime_cuspidal_independent_audit.md` is the independent complete review of the accepted AG.40–AG.42 A1 proof chain, including arithmetic descent, compactification, boundary transport, and the distinction from the refuted full configuration exactness claim.
- `A1_downstream_scope_assessment.md` gives the exact A3/A5/A10/L5/L8/L11 consequences and the final existence-gap assessment.
- `L5_consequences_insertion.tex` was supplied for the geometric agent's existing AG.1 claim, not a duplicate result.

## Remaining universal questions

A3 remains open in its intended nontrivial-cover meaning. A1 is proved by the accepted independent cuspidal chain but does not imply universal rational class-number witnesses. A10(c)'s arbitrary all-normal free-orbit assertion remains open; AC.45 realizes nonzero classes by full sections but does not supply freeness. Universal supersingular correspondences remain separate from the literal A5 consequence of A1. The degree-one-permitted version of A6 retains its stated caveat; the nontrivial primitive-cover version is refuted by the explicit certified curve.

No concrete additional finite attack on A3 or freeness is currently available. Further work on the hereditary criterion or actual Abel tower would need a new existence or torsion theorem. No further isolated witness or census computation is proposed. Source writes are held after this record so the parent can assemble a stable snapshot.
