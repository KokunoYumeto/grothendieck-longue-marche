# D75 integration and audit ledger

Integrated as sections/D_alexander_compact_factor.tex after root and FGH independent complete proof/source/certificate audits passed. The original candidate is retained as notes/de_compact_axis_draft.tex. Root's detailed audit is notes/root_A61_D75_audit.md; FGH's is notes/fgh_D75_audit.md. The source/dependency ledger is notes/de_D75_sources.md.

The result uses the exact axis quotient of the actual Alexander action. Its Tate-twisted quotient is the measure augmentation ideal, with the full affine action determined by the Kummer cocycle. Primitive restriction to the cyclotomic kernel determines the entire translation subgroup, so the global and local affine images are exact. Every invariant function modulo constants is classified: the possible additive translation defect is killed by the tame multiplier two. The local gauge is divisible by the global depth and therefore preserves the first r ball functions.

The local/global quotient of axis Cartier-dual invariants injects into the full invariant quotient. This is an actual inclusion of discrete groups; duality gives a continuous quotient of D63's compact term. Its divisible discrete dual supplies a continuous splitting. Thus the proof does not rely on finite-level classes surviving an inverse limit, or on formal monomial actions being trivial modulo the same coefficient exponent.

The finite-depth conclusion is a free factor Z5^(N-r), not an infinite product modulo5^N. Divisibility of a translation exponent does not trivialize its action on the entire completed power-series module. It instead preserves exactly the required initial valuation balls; exact local zero makes all shells available and yields the infinite product.

The explicit examples are actual completed cusp parameters. For kappa(101), global depth0 and local depth1 give Z5. For kappa(2)-(log16/log81)kappa(3), the logarithms cancel exactly, the prime-two coefficient is a unit, and the compact factor is a countably infinite product of Z5. The latter parameter has finite support, contrasting D64's vanishing compact kernel for any pair supported at5 and one primitive prime.

Executed files code/de_compact_axis.py, .json, and .out pass. FGH independently reran the same certificate with output notes/fgh_D75_certificate_rerun.out. The calculation checks exact affine orbits and the determinant-one ball-defect matrix through depth5, gives sample prime parameters, and computes the logarithm ratio modulo5^20 with an explicit tail bound. It supports the finite identities only; the continuous and infinite claims are proved in the text.

D5 and D63 summaries and the owner register were updated. The complementary compact factor, arbitrary infinitely ramified H1 multiplicities, arbitrary-pair section existence, and the first explicit higher-derived obstruction remain Open. No diagnostic PDF was created; root's combined build and normal checkpoint QA handle the integrated section.

## Supplemental third independent audit

PBC independently completed the full proof audit and copied/reran the exact certificate without changing the original files. Its full JSON agreed with the original. Ledger notes/pbc_D75_audit.md and comparison notes/pbc_D75_certificate_rerun_comparison.json are retained. All actual affine-image, invariant-defect, gauge, duality, and continuous-splitting steps passed with no correction.
