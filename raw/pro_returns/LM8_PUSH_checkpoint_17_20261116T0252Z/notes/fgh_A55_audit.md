# A.55 registration and audit

**Status: registered, Proved.** Parent approved integration after full independent root and DE proof/source/code audits, both PASS, on 2026-11-15.

Canonical proof: `sections/A_quartic_cm_normalizers.tex`, included after A.54 in `sections/A.tex`.
Canonical exact certificate: `code/a_quartic_cm_normalizers.py`, with `.json`, `.out` and `_root_rerun.out` retained.
Original candidate and certificate remain in `notes/fgh_A55_*` as historical staging files.

The proof has four substantive checks. First, the actual cyclic prime-power cover is built from an étale Picard torsion point whose special order remains exactly p^n; its finite-flat torsor is normal by R1/S2, with integral radicial special function field and unique Frobenius-twisted main component. Second, original Raynaud Theorem1, printed179, gives the full p^n scope and interior slopes on every exceptional component; the norm removes precisely the main component Jacobian, identifying the Prym with the exceptional product up to isogeny. Third, the full integral Schreier invariant lattice is computed rather than replaced by its rational span, so arbitrary p-divisibility of the normalized generator is handled. Fourth, the arithmetic subgroup is the actual index-p^n covering subgroup, and its normalizer intersection retains open arithmetic image. The final transfer uses the actual punctured quotient maps from A.54.

Both auditors requested or independently confirmed the explicit dualization from a Tate-homology line to an H1 crystalline quotient so that Newton slopes and Hodge jumps use the same 0/1 convention. The integrated proof contains that clarification.

Independent DE ledger: `notes/de_A55_audit.md`. Root reopened the publisher preview and independently executed all degree2,3,5,11,25,121 lattice checks,73 split-prime Cartier checks below2000,30 divisibility cases and the target coordinate identity. The canonical author execution also returned PASS. The finite checks support exact formulas; all unbounded assertions have proofs.

A.54 and A.45 now identify all-prime normalizers for the actual Heisenberg-five cover as proved. Its full fixed subgroups away from coefficient5 remain Open. No universal-cover, cofinality, quotient-fixed-lift or coprime-degree pro-prime embedding claim was added.
