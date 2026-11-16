# D75 source and dependency ledger

The candidate is notes/de_compact_axis_draft.tex. It uses only the actual Alexander formula and compact duality already established in D35/D39/D63, together with elementary Kummer theory and the explicit affine-function calculation proved in full.

- verified: D35 and D39's actual multiplier restricts at v=0 to chi S_chi(t), since the normalized integral beta series is one on the axis. Multiplication by t−1 identifies M_a(−1) exactly with the augmentation ideal of the completed group ring. The scalar chi is explicitly retained before the Tate twist.
- verified: D63's local duality and inverse limits identify its compact quotient with the dual of D_s^(G_Q5)/D_s^(G_Q), and its compact kernel maps onto that quotient. The proof uses Milne, Arithmetic Duality Theorems, primary https://www.jmilne.org/math/Books/ADTnot.pdf , Chapter I local duality and the global sequence. These exact primary statements were opened in the earlier D63 audits; FGH has additionally reopened I.2.1/I.2.3 during the D75 audit. No finite-level survival assumption is made.
- verified: Kummer identification and the global completed prime-coordinate group are the explicit ones proved and used throughout D1/D35. The local coordinate formula is derived in this proof from Q5×=5^Z times mu4 times (1+5Z5), with the elementary convergent logarithm.
- proved directly: every primitive Kummer class restricts primitively to the cyclotomic kernel, because H1(Z5×,F5(1))=0 by the tame scalar. This determines the entire closed affine image, including all translations, not merely its finite reductions.
- proved directly: all invariant continuous functions modulo constants are the valuation-ball functions. An additive translation defect is forced to zero by the tame multiplier two. Compatible local/global gauges fix the first r balls.
- proved directly: the exact local/global axis invariant quotient injects into the full Cartier-dual quotient. Duality therefore gives a continuous compact quotient; divisibility of its discrete dual supplies a continuous splitting.

## Executed exact certificate

code/de_compact_axis.py, code/de_compact_axis.json and code/de_compact_axis.out are retained. PASS at depths0–5. The program enumerates actual affine orbits modulo5^(N+1), verifies the triangular determinant-one matrix of translation defects, and checks that all those defects vanish at1 so no constant defect is hidden. It computes log16/log81 modulo5^20 as46173538124618 modulo95367431640625 using44 terms in each logarithm; the proved tail valuation leaves more than20 digits after division. Its residue is3. Example primes101,251,11251,37501,62501 have exact local depths1,2,3,4,5 respectively.

No diagnostic PDF was created. This is a genuine computation of a split free factor of the retained compact term. Its compact complement, all arbitrary-pair section existence, and explicit first finite-derived obstructions remain open.
