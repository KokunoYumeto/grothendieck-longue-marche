# A193 exact maps and certificate

Source: `sections/point3_genus2_finite_selmer_loci.tex`.
Executed certificate: `code/point3_genus2_finite_selmer_certificate.py`,
with retained output and exact data. The first complete execution passed.

The local basis proof is elementary and does not depend on a software local
square oracle. In L=Q2(theta), theta^4=54, the literal Kummer values are
3-theta, -theta, and -86-theta. Their independence follows from odd theta
valuation, the two exact norms, and the impossible valuation three of a
unit square minus one. The finite-index rank-two formal subgroup, the
actual rational two-torsion, and complete Nakayama give the surjective
completion map. The independently proved logarithms make that map injective.

The new finite Selmer equivalence uses A186's exact global finite Kummer
sequences and A192's actual all-disc abelian logarithm. It is not a claim
that every Jacobian Selmer class lifts to a locally curve-matching section.
The explicit quotient-section exclusion is the necessary direction of
the actual arithmetic map through the selected cyclic-eight sheet.

The group certificate starts from literal Schreier words. Killing proper
boundary inertia gives the primitive quotient Z2[v]/(v^4+1). The resulting
semidirect product is metabelian, with exact order2^(4n+3) and class4n.
The certificate independently verifies Delta^4=2U with U unimodular, the
first vanishing augmentation depth for24 exponents, and the stated point
with x=11. Finite tests supplement the all-n DVR/lower-central proof.

Primary inputs are already opened and verified in A186, A189 and A192:
the actual odd-degree Kummer map, finite Selmer sequence, and formal Neron
logarithm. No new unverified arithmetic theorem is used. The exact local
Kummer values were additionally checked with the installed local PARI
runtime as an exploratory independent check; the proof does not require it.
