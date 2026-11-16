# D.81 source, dependency, and computation ledger

**UNREGISTERED candidate.** Full proof: `notes/de_sha_all_unit_pairs_draft.tex`. Exact certificate: `notes/de_sha_all_unit_pairs_certificate.py/.json/.out`. No diagnostic PDF.

## Checked inputs and exact use

- **verified:** D78/D80 actual global image H semidirect I0 and local saturation kappa(6)(ker local-to-I0)=Z5. The proof now checks continuous coinduction for a nonprimitive line explicitly using a finite-coset transversal, and handles the zero subgroup separately. No primitive direct complement is assumed.
- **verified:** D31/D39 actual beta coefficients and all three exact boundary restrictions; D77's actual local primitive Soulé element makes beta-1 equal to P times a unit. The existing raw primary is Nakamura--Sakugawa--Wojtkowiak (1.1)--(1.2), https://arxiv.org/pdf/1410.1045 , freshly opened in the D78 ledger as turn1022view1. The current proof uses exactly the degree-two and degree-three coefficients already checked there.
- **verified:** D63 is the exact finite-global-localization definition of S_s and the compact extension. D77 computes the complete local/global invariant map and its continuous product splitting. D80 proves the finite Tate-duality/ML passage and the single common coefficient level after finitely many residual inertia exceptions. Its primary Milne ADT I.Corollary2.3, printed28, was freshly opened as turn1039view0, https://www.jmilne.org/math/Books/ADTnot.pdf .
- **verified:** D74 applies only to the explicit finite-support modules when their unrestricted first cohomology is mentioned. No general section existence follows.

## New algebra and exact finite computation

The upper bound is an elementary ideal calculation. Reduction modulo each of u,v,t1*t2-1 proves regularity unless it is the one exact boundary factor; cancellation computes the annihilator in that case. The resulting connecting module is Z5(5) or Z5/(eta)(5), so its Cartier Gamma-invariant group has order at most5. This remains valid for the zero local vector. No general UFD, Weierstrass, or finite-rank citation is needed.

The lower bound at a locally5-divisible vector uses one explicit functional in the actual ten-dimensional mod5 cubic Cartier module. The certificate derives its ten symbolic residuals from the true Fox multiplier and beta coefficients; modulo5 they are q(q^4-1) times the displayed fixed vector. It separately verifies all20 residual (chi,c) possibilities. It also counts the13/12 residual partition and checks the thirty mixed finite/free examples and the unit logarithm denominator at31. These computations do not replace the coinduction, annihilator, or finite-level uniformity proofs.

The exact comparison with D80 makes the classification valid for arbitrary infinite ramification. General pairs with a nonzero five-valuation, globally dependent reductions, arbitrary infinite H1 ranks, and section existence remain outside the theorem.

## Integration and complete audits

D81 is integrated as Proved in `sections/D_alexander_all_unit_pairs.tex` after root, FGH, and PBC complete independent proof/source/exact-certificate audits. Ledgers: `notes/root_D81_audit.md`, `notes/fgh_D81_audit.md`, and `notes/pbc_D81_audit.md`. Canonical executable/output: `code/de_sha_all_unit_pairs.py/.json/.out`. The original candidate and each separate rerun remain retained. No diagnostic PDF was created.
