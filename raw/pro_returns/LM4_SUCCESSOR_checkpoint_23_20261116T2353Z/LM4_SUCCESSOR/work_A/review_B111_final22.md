# Complete independent formal review of B.111

**PASS.** I read `work_CE/B111_q0_diagonal_proposed.tex` completely, after independently reconstructing the beta33 witness without importing the HNN normal-form evaluator.

The chronological braid in the actual input is literally `W0 (3,3) W0^-1`, with the seven-entry `W0` printed in the proof. Its positive push and inverse convention match B.110. The raw involution `U`, contact relation and two inverse-image identities are correctly typed before filling.

The marked substitutions give `V=g e w S g^-1`. The existing relation `[a,bar a]=1` makes `S` commute with the cone, and the resulting image of `U` has exactly the displayed conjugator. Every line of the four-line calculation is valid: first conjugate the commutator by `e`, then use the HNN identity, and finally use `e w=w p`. The final conjugator is precisely `a b^-1 w p`.

The coordinate retraction onto the nonadjacent vertices `p,bar p` proves that their commutator is nontrivial in the base. Actual HNN base injection proves discrete nontriviality. The base is residually finite and has its full induced topology in the HNN group, so the same element is nontrivial in the full completion. This step does not require a separate claim that the whole slit group is residually finite.

In the annular group, the retained far generator implements the raw zero monodromy. Hence the inverse image of the filled contact relation is trivial by actual conjugation. The proof uses the raw free-group automorphism and its defining annular relations; it does not suppose that this automorphism descends to the slit quotient. The killed conjugate therefore gives the claimed nontrivial element of the kernel, both discretely and after completion.

The only notation correction sent to CE is to write `Gamma`, matching B.110's RAAG group, instead of the otherwise undefined `A_Gamma` in Section 3. All scope limits are correct: no full annular kernel, centralizer, or source equality is asserted.

Independent evidence is recorded in `work_A/review_q0_and_one_neck22.md`, `work_A/code/review_q0_beta33_witness22.py`, its genuine stdout/stderr, and `work_A/review_q0_beta33_witness22.json`.
