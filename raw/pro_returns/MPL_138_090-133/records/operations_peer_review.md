# Peer review of operations_proofs.md

Reviewer: GPT-6 Astra Pro; inherited effort unspecified; run MPL_138_090-133/maps_moduli_research. Date: 2026-11-17. Reviewed the root's after-freeze proof record, frozen TeX scans 129–131, and the relevant definitions and exact normalization in arithmetic_certificate.py. No source image was read, no root proof file was edited, and no further literature theorem is claimed as checked by this review.

## Findings

**P1 — passed under its stated category.** A connected finite cover of a disc with no branch value is a disc; with one branch value, the cyclic punctured-disc cover completes to a disc. The two-branch-point double cover is an annulus, so the converse is correct when the reference cover and those double covers are allowed. The proof correctly distinguishes the folded-edge category q∈{1,2} from a category requiring index 2 everywhere above 1. A=[0,1] is a valid counterexample to a condition imposed on A itself instead of its complementary faces.

**P4 — passed.** The rational function F_n has degree 2n, the displayed derivatives and fibre multiplicities are correct, and F_n^(-1)([0,1]) is exactly the n-ray orange with vertices 0,∞. Positive real scalings give an isotopy through graph-preserving holomorphic automorphisms and change the function unless the scaling is 1. Frozen scan129 defines C=(K,S) using the graph and vertices; it does not include the distinguished edge midpoints or face centres, so these examples satisfy the strict definition and the midpoint/centre discussion is a genuinely additional condition.

**P5, finite sufficient condition — passed with an essential scope distinction.** Isotopy through map automorphisms fixes each incidence, so finite analytic boundary corners determine fixed, distinct prime ends, including repeated occurrences of one underlying vertex. Three such fixed prime ends force the face automorphism, and then the connected-surface automorphism, to be the identity. This proves rigidity in the identity component used by P5, not rigidity of every automorphism fixing the three cell sets S,A,F.

**P5, bouquet — passed.** The displayed R has passport (4)|(2,2)|(2,1,1); both points above 1 have index 2. Its one vertex and two loop edges give three faces of orders 2,1,1, so it is a counterexample to the asserted classification of maps with no face of order at least 3. It is correctly not presented as an extra continuous-automorphism family.

**P7 — passed conditional on the independently certified sextic normalization.** Cleaning by 4f(1−f) preserves the required special-value conditions. The factorization reduces an isomorphism of the cleaned maps to f_d∘h=f_c or f_d∘h=1−f_c; the distinct zero and one passports exclude the second possibility, and the unique pole plus unique zero orders 3 and 2 force h=id in the first. Evaluation on the rational identity cover then proves failure of full Galois equivariance for a non-rational member in the folded-edge reference category. Definition over Q is used as a sufficient condition; no converse necessity for every presentation of an operation is asserted.

## Scope warning sent to root

Frozen scan129, lines 26–28, says “isotope à id, i.e. fixant sommets, arêtes, faces.” The latter condition alone is weaker. The torus map checked in MM02, with r=(1234), σ=(13)(24), has a face of order 4 and a nonidentity holomorphic half-turn fixing every cell; it is not isotopic to the identity through map automorphisms. Thus P5's repair must retain the identity-component or incidence-fixing hypothesis rather than invoke that manuscript “i.e.” as an equivalence. The current proof record already uses the stronger hypothesis, so this is a warning for the integration and wording of the final notes, not a request to change its valid proof.

One minor normalization detail in P4: “fixing a single edge midpoint kills b but leaves a” is literally b=0 after normalizing that midpoint to 0; for a midpoint x0 it says b=(1−a)x0. The claimed remaining dimension is unchanged.

## Limits

This review did not verify the infinite-map extension, the existence or contractibility of every invariant rigidification, the disc-homeomorphism literature proof, or a full classification of spherical operations. It supplies no result on RESULTS_STATE LM4 C.12. The corresponding actual check events are in operations_peer_check_events.tsv.

