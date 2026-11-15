# A53 integration and audit

Registered after independent full root and DE proof/source/code audits: PASS.

Root read the complete proof and exact counting certificate, independently reran it successfully, and reopened Liu Proposition10.1.21(a), pp462–463 (turn808view0). Silverman's supersingularity criterion was already independently checked. Root checked tame coordinate and unit-root extraction, exact per-cusp counts, all marked-tree endpoints, arithmetic finite-field/open-derived passage, and conditional normalizer inheritance through unchanged proper homology.

DE's independent full audit is notes/de_A53_audit.md; it also independently reran the certificate and reopened Liu and Silverman. Both audits specifically confirm that no finite-refinement or fixed-lift assertion is hidden.

Canonical source: sections/A_universal_enlargement.tex.
Canonical executed certificate: code/a_universal_enlargement.py/.json/.out.
Independent reruns: code/a_universal_enlargement_root_rerun.out and code/a_universal_enlargement_de_rerun.out.
Original notes drafts and staging outputs remain retained.

Scope: every compactification already occurring in a finite cover of U admits infinitely many new torsion-punctured covers with full all-prime fixed inertia; normalizers transfer conditionally from the original affine curve. Universal TaskA5 remains Open. A45 source/register updated while preserving A46.
