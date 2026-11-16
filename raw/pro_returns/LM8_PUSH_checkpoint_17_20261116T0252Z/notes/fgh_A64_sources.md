# A64 primary-source and proof-gate ledger

Registered after full root and PBC proof/source/certificate audits PASS; the original candidate is retained as provenance. It proves a general torsion enlargement criterion when the enlargement has a residue prime outside the actual geometric Galois closure order. The Heisenberg consequence includes every odd prime and every positive enlargement integer. The universal Task A.5 remains Open.

## Primary sources actually opened

- **verified:** SGA1, Expose XIII, Corollary2.9 and Section2.10 (recomposed pages288–289, PDF303–304; original pages389–391), and the proof of Corollary2.12 (recomposed pages291–292, PDF306; original page394). Primary reprint: https://arxiv.org/pdf/math/0206203 . Exact prior openings `turn1001view1`, `turn1001view2`, reopened as `turn1002view1`, `turn1002view2`, with precise-find refs `turn1003view2`, `turn1003view3`. The prime-to-residue specialization comparison preserves the actual finite cover and inertia; it is not a statement about arbitrary wild covers or merely Jacobians. The same comparison was independently audited in A56 and A59. A finite arithmetic twist is killed after finite extension.
- **verified:** Silverman, The Arithmetic of Elliptic Curves, second edition, PropositionVII.5.5 printed197 (PDF zero-based212), proof's characteristic-two/three cross-reference to AppendixA.1.4(b) on printed199 (PDF zero-based214). Primary PDF: https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf . Exact earlier `turn997view1`, reopened `turn1002view3`; precise-find `turn1003view1`. This gives potential good reduction from integral j, including residue2, before applying tame specialization.
- **verified:** Same primary book, TheoremV.3.1 printed145 (the theorem statement), exact earlier `turn1001view0`, reopened `turn1002view0`, precise-find `turn1003view0`. In characteristic r the geometric r^a torsion has r^{af} points with f=0 or1. Finite-flat idempotent decomposition and translation give equal generic specialization fibres of size r^{a(2-f)}; this equal-fibre assertion is proved explicitly in the draft.

## New gates and dependencies

1. An actual prime-to-r geometric Galois closure extends to the good pointed elliptic model after finite extension; its normalization and every subgroup quotient are smooth curves, with local map t=u^e and r not dividing e. Residue2 is explicitly included.
2. Every target m-torsion specialization fibre has at least two points. The exact source clusters have size c off the origin and 1+e(c-1) at an original cusp. No ordinary-reduction clusters away from the origin are omitted.
3. Good proper-source reduction plus these clusters gives a rational marked joining path for every selected cusp. A41/A42 therefore give all coefficient primes and all packets directly on the new affine curve.
4. For inert Heisenberg p and a pure p-power enlargement, A61's actual main map is radicial and every other positive-genus component maps to a finite critical centre different from O. All new marks map to O, so they lie in the single rational marked fibre at the unique main point above O. This separate argument treats the only case not covered by the prime-outside-closure criterion or A63.
5. A11/A53 transfer normalizer recognition through the actual open immersion, using unchanged proper homology. No fixed-element lifting or finite refinement over the original map is asserted.

## Certificate

`notes/fgh_A64_certificate.py/.json/.out` checks the symbolic cluster and Euler identities, finite tame branch-index count examples, actual Heisenberg degree/ramification count examples including residue2, inert pure-power counts, and the exhaustive elementary case partition in 600 sample pairs. Abstract branch-index lists are expressly not claimed to be realized covers. Stable models and arithmetic fixed groups are proved in the text, not inferred from these finite checks.

Root primary page checks and exact rerun are in `notes/root_A64_audit.md`; the full PBC independent audit is in `notes/pbc_A64_audit.md`. Canonical proof and certificate are `sections/A_torsion_enlargement_closure.tex` and `code/a_torsion_enlargement_closure.py`.
