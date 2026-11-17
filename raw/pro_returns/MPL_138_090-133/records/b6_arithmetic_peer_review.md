# Bounded arithmetic peer review of B6 and operation notes

**Reviewer:** GPT-6 Astra Pro; inherited effort not exposed; run MPL_138_090-133/arithmetic_research.

**Scope:** Read records/root_research.md, BC01–BC14 and OP44–OP46, and records/operations_proofs.md, P7–P8; OP43 was read because it summarizes P7's arithmetic hypothesis. Compared these with the completed arithmetic certificates, the already consulted Hua and RESULTS_STATE context, frozen scan103 TeX, and the supplied Esquisse's retrospective Belyi passage. No scan images were opened, no frozen source was modified, and this is not a second exhaustive historical audit of all43 leaves or a fresh verification of the external theorem numbering.

## Verdict

**The mathematical use of the sextic family in OP44/P7, the invariant argument in OP45/P8, and the finite-group distinction in OP46 pass this bounded review.** BC01–BC14 consistently separate a finite example from a faithful global action and distinguish retrospective context from what is stated in this packet. Two small corrections were communicated to the root: an incorrect Hua subsection locator in BC14, and an overstrong “only” in the adjacent OP43 summary; neither requires changing P7 or P8.

## BAP01 — B6 scope and historical qualifications

**Targets:** BC01–BC14; particularly BC02, BC05–BC10, BC13–BC14. **Result:** pass for the claimed logical scope, subject to the stated limits of this review.

Frozen scan103, lines3–6, explicitly inserts the algebraic-point comparison and states the Galois action; line8 says “peut ne pas être triviale,” while line10 announces elementary calculations. The notes correctly avoid deriving representability of the raw pinned isomorphism-class functor from those lines, or treating nontriviality as faithfulness. A fixed finite passport gives a finite permutation set, whereas the absolute Galois group has arbitrarily large finite cyclotomic quotients, so BC09's obstruction to faithfulness on one fixed type is valid; the arithmetic S3 and geometric S6 in BC10 are properly distinguished.

BC06–BC08 correctly keep separate the map-to-algebraic-curve direction, the converse Belyi theorem, and the later regular-dessin faithfulness result. The supplied Esquisse, scan119/17, lines721–735, is retrospective evidence for the Helsinki announcement and the converse; it does not date the mathematical writing on reused sheets, and BC07 explicitly retains that limitation. I did not independently repeat the root's complete absence search over all43 leaves or reopen Belyi/Theorem4 and González-Diez–Jaikin-Zapirain/Theorem18; their precise numbering remains the root's checked citation, not a new peer-verification claim.

## BAP02 — Minor BC14 locator correction

**Target:** root_research.md, BC14 context line111 as reviewed. **Result:** correct the locator.

“Hua's project §4, Kummer discussion” should cite **§3, “Calculs : z ↦ zⁿ, la fonction g, Kummer sur Q,” lines551–600**, especially582–600. Section4 begins at line656 and is “La tour de Fermat”; the actual cube-root-of-two comparison used by AR13 is in §3. BC14's mathematical boundary remains correct: the cubic parameter algebra is a small Kummer-related example and does not compute LM7_PUSH E.3 or certify the unrefereed EXIT_TOWER E.49 claim.

## BAP03 — OP44/P7 cleaned-sextic counterexample

**Targets:** root_research.md OP44; operations_proofs.md P7, lines188–202. **Result:** pass, for isomorphisms over the fixed target and the explicitly stated folded-edge reference category.

For each certified sextic f_c, the outer quadratic C(t)=4t(1−t) sends0,1 to0 and infinity to infinity; C(t)−1=−(2t−1)², and f_c is unramified over1/2 because its critical values are0,1,infinity, so β_c=C∘f_c is clean. The factorization C(u)−C(v)=−4(u−v)(u+v−1) holds in the integral function field, so an isomorphism β_d∘h=β_c forces f_d∘h=f_c or f_d∘h=1−f_c globally, with no possibility of switching between the alternatives pointwise. The second alternative contradicts the distinct0/1 passports, and the first fixes the unique pole and the unique zeros of orders3 and2, forcing h to fix infinity,0,1 and hence c=d. Thus the three cleaned covers remain distinct Galois conjugates, and evaluating a fixed β_c-operation at the rational identity cover proves non-equivariance; no unproved faithfulness or moduli-representability statement is used.

## BAP04 — OP45/P8 invariant transport

**Targets:** root_research.md OP45; operations_proofs.md P8, lines204–214. **Result:** pass.

For a Galois-equivariant Ω and invariant I, the equality I(Ω(σD))=I(σΩ(D))=I(Ω(D)) proves the claim by substitution. Distinct values therefore separate orbits, but no invariant so obtained can distinguish the three certified sextics as different orbits because they form one orbit. The explicit rejection of completeness and of a solution to EXIT_TOWER E.24 is appropriate; the independent content of Wood's Proposition4 was not recomputed in this bounded review.

## BAP05 — OP46 distinguishes two kinds of operation correctly

**Target:** root_research.md OP46. **Result:** pass.

On the certified three-element orbit, mirror reversal is a transposition and the arithmetic image includes a3-cycle, so their two permutation products differ. Jones, Example7.7, which was already opened in the arithmetic research and independently opened by the root, explicitly gives the corresponding noncommutation for the associated regular covers and the wider Out(F₂) operation group. This does not conflict with rational postcomposition equivariance; OP46 states that boundary accurately and does not attribute the later comparison to the manuscript.

## BAP06 — Adjacent OP43 overstates the field-of-definition implication

**Target:** root_research.md OP43, phrase “and only for G_K when it is defined overK.” **Result:** replace “only” by a guarantee, for example “definition overK guarantees equivariance for G_K.”

Being defined overK does not imply failure of equivariance for elements outside G_K: the identity map is defined over every number field and its operation commutes with the whole absolute Galois group. More generally, a stated field of definition need not be minimal, and the operation on isomorphism classes could have additional symmetry. P7 itself already uses the correct sufficient formulation, “definition overK gives it for Gal(Qbar/K),” so its proof requires no correction.

## Review boundaries and ledger

The main arithmetic certificate was used, not rerun gratuitously; its exact remainder, admissible passport, irreducibility, field identities and three-class enumeration are the inputs to BAP03–BAP05. No novelty is claimed for the cubic family, and no regular-dessin faithfulness theorem is inferred from it. Actual proof checks from this review are logged separately in records/b6_arithmetic_peer_events.tsv; no main check ledger was edited.
