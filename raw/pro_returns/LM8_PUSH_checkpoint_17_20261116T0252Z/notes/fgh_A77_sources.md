# A77 sources and proof gates

Registered as A.77 after full root and DE proof/source/exact-certificate audits PASS. Canonical proof `sections/A_commutator_order_two.tex` and exact rerun `code/a_commutator_order_two.py/.json/.out`. The original audited draft and certificate remain preserved. Editorial changes are recorded in `notes/fgh_A77_registration_editorial.diff`.

The faithful-quotient classification is proved directly by Schur, Q/Z=C2² and the exact central-word identity Z=<u²,v²,sigma>. Irreps are taken over the same auxiliary-adic splitting field used for Tate homology. The actual quotient-Jacobian maps satisfy the norm identities directly on divisors, and their SUM IS SURJECTIVE; the whole product need not be isogenous to J_C.

verified: Serre–Tate Theorem1/Corollary2, printed493, https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf. Existing exact primary checks are retained in fgh_refs.bib and A65/root ledgers. Fresh opening turn1202view0 returned no OCR; turn1203view0 screenshot returned text-only, and an optional local download returnedHTTP403. No new visual-source verification is claimed.

verified: Dupuy–Rabinoff Theorem1.1/Proposition3.2, https://arxiv.org/pdf/1705.03034, turn1196view0; actual node extension.

verified: Lehr–Matignon Theorem6.13, https://arxiv.org/pdf/math/0411059, printed21/PDF20, turn1192view0; separate nilpotent tree conclusion, no marked-fibre rank inference.

Exact code constructs the order32 group, all four actual D8/D8/D8/Q8 quotients and their kernel/character checks, all sixteen linear characters, full degree-square accounting, and cyclic-centre arithmetic through order1024. It does not infer Jacobian decomposition from finite computation.

Draft SHA256: 7752d6addfa2162f0008ee82049a7a062420e4791b865ac6df809614a662e6e0

Certificate SHA256: c2b05f26e7b19bc767ad3903921e7ff63efa289fb51d2ded3b36e15fee704dda

Result SHA256: 4909041203e23a0c9f82ffa7f9698a422ac84d1e97fdd691ddcf9f2f9f9fcdbb


verified: root freshly read the exact primary Serre–Tate Theorem1/Corollary2 printed493 through the indexed original source, refs turn1208search4/turn1208view0. Root full ledger is notes/root_A77_audit.md/.json; the prior direct-PDF readability limitation is retained above as historical provenance.


## Exact Gram assertion strengthened after integration

The candidate and canonical certificates now assert the undivided nonlinear character dot products are exactly 32 times the identity before forming the Gram matrix. Both reruns passed; all prior output fields are unchanged. Original sources/outputs and exact diffs are preserved under notes/fgh_A77_certificate_before_exact_gram and notes/fgh_A77_canonical_before_exact_gram. Current hashes and the exact numerator matrix are in notes/fgh_A77_orthogonality_precision.json. No theorem or proof change was needed.
