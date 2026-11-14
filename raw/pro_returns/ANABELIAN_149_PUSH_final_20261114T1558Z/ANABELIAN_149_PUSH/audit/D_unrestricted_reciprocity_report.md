# D.29 integration report

**Status: Proved, in its precise arithmetic scope.** The full candidate was independently read and accepted by root; `D_unrestricted_reciprocity_root_review.md` records that review and the primary-source checks. The new section is `sections/D_unrestricted_reciprocity_extension.tex`, input immediately after D.28 in `sections/D.tex` with root authorization. The result ledger is separate for root's assembler.

The construction chooses an increasing sequence of primes that eventually split every prescribed finite Galois extension of Q and tend rapidly to1 in every fixed p-adic unit group. Their finite products converge to actual nonzero local elements. An additional nested congruence fixes the valuations of their translates by1 and2, proving that x_v=2+A_v is an actual ordinary local point away from both old and new punctures.

Each selected prime contributes valuation exactly1, so the tuple is outside the Kummer restricted product at every modulus n>1. This persists after any finite number-field base change. The primes have Dirichlet density zero, and at them the two original tripod coordinates are units.

For each fixed character over each finite number field, all sufficiently late selected primes split the character field. Its cup products therefore have finite support depending on the character. One sufficiently late finite principal product agrees in Kummer classes at every place in that support; its global Brauer invariant sum is zero. All the proposed characterwise tests pass, although the restricted-product input required by Poitou-Tate is absent. This proves a separation of conditions, not a failure of Poitou-Tate.

The statement explicitly does not provide a section, global completed classes for t and1-t, or the conditions on all accessible finite étale neighbourhoods. It makes no claim that those genuinely stronger hypotheses cannot imply admissibility. The norm statement is exactly the ordinary norm-of-restriction identity. The archimedean values are separately1, matching the Kummer classes of positive finite products; no divergent real product is used.

## Reproducibility

Canonical files are `code/D_unrestricted_reciprocity_checks.py` and `code/D_unrestricted_reciprocity_checks.json`. The script uses exact integer trial division and verifies the five stated primes, their least-prime progression checks, cusp-avoidance congruences, and45 quadratic Hilbert reciprocity products. All checks passed. The old audit script is a labelled forwarding wrapper, and the old audit JSON records its supersession. The candidate points to the canonical paths. These finite certificates verify the numerical prefix and finite identities; the full proof establishes the infinite/all-character claims.

## Source scope

The existing key `D_MilneCFT2020` is used and its opened-source note is updated. Exact independently opened locations are ChapterIII Proposition3.6 and Lemma3.7, pp.109–110; ChapterV Theorem3.23, p.164; and ChapterVIII Theorem4.2, p.241. They supply unramified-unit vanishing, complete-splitting existence, and global Brauer reciprocity. The new construction and its logical separation are proved in the section. No assembler or combined build was modified or run by this agent.
