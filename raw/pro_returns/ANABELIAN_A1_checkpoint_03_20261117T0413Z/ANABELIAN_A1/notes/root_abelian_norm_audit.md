# Independent root audit of B.AB1--2

The source proof was read in full. Over an unramified splitting extension of Z_p, every nontrivial prime-to-p character value minus one is a unit, so any nonzero exact-kernel packet has exactly that kernel. Norms correspond to the group-average idempotents because pullback is injective on p-primary torsion. The finite abelian subgroup-lattice argument uses prime-primary characters to detect every g outside any subgroup, hence cyclic prime-power quotients are exactly the necessary tests.

For nonconstant deck groups, F cycles exact-kernel packets. An F^m-fixed nonzero vector in one packet gives a nonzero F-invariant orbit sum in the direct sum of distinct packets; no averaging scalar is used. This is valid when p divides m. The connected relative Prym has the required p-primary packet because the isogeny degrees are prime to p, and its finite-field point count is the class-number ratio. The pointed descent field is precisely the subgroup orbit length. No finite-field extension is silently assumed to preserve nonzero invariant vectors in the reverse direction.

An independently written verifier uses a different subgroup-generation algorithm (all pairs) and weighted support enumeration via character sums, without importing the producer. It verifies all finite counts:81 versus0 in the original C9 x C3 module;20,253,807 after adding the three primitive order-nine packets;32 semilinear fixed vectors and9 satisfying all quotient conditions in the nonconstant C3 x C3 example. These are module controls, not asserted curve realizations.

Verdict: proofs and finite computations pass. Universal B2 remains Open.
