# Root audit of the two actual top central covers

**PASS for the complete conditional comparison.** This audit alone does not prove C.31. A fresh original-source quotient identity and the full normalized gentle lift remain separate gates. The failed native-collected quotient identity is not used.

Root read the entire proof `notes/pbc_C31_two_cover_comparison.md`, all of `pbc_top_two_section.py`, `pbc_top_two_cover_actions.py`, `pbc_top_two_cover_values.py`, the positive-word section verifier, and the independent finite-source input checker. Root also read FGH's complete independent audit and its subsequent successful finite-source gate. All conventions below refer to the original presentation of SHA256 `95fb384593bfaf97d468bbc51f11cd797484a08cb3ec3b954961085b520ffc88`.

## The actual section

Right conjugation on the binary kernel uses column vectors, so a word with successive letters i and j acts by M_j M_i. The Hall-three power and commutation equations in the source follow by expanding the actual lifts g_i a_i with this convention. The normalizer equation follows by moving the correcting binary vector across the original conjugation word, including its original binary tail. The script retains and rechecks every scalar equation.

The resulting complement to the binary kernel above the normal three-group is an actual subgroup. Its normalizer maps onto the entire quotient: conjugating a complement gives another complement in the same normal preimage, and coprime complement conjugacy supplies a binary correcting element. The normalizer kernel is the binary fixed space under that odd subgroup, which is zero. Thus this normalizer is a genuine section of the entire quotient, not merely a list of independently selected generator lifts.

Root independently executed the retained original GAP section replay. It verified all 104 quotient powers, all 5,356 quotient conjugation relations, the 18 Hall-three powers, 153 Hall-three commutators and 1,548 normalizer equations. The full stdout is identical to the author's apart from runtime integers. Executed GAP source SHA256: `c28212ed7d6ddb3fd9f262225be5f58ee98b368a9e6120b946bf0215ca42e3a8`; root stdout SHA256: `c784e2b12d2a3265ede6bbb129270583b46ebf4e217def070395165364e7dd53`. The exact root output and comparison are retained as `notes/root_top_two_section_positive_replay.out` and `.json`.

## Genuine central extensions and their actions

The diagonal of the bilinear cocycle is the invariant quadratic refinement; its symmetrization is the invariant alternating form. The cocycle difference under an action matrix is symmetric with zero diagonal. The displayed upper-triangular quadratic function therefore has precisely that polarization and gives a genuine automorphism lift. The ranks 72 and 36 are treated correctly: only the first form is nondegenerate. The automorphisms fix the distinguished central C2 kernel, without an incorrect claim that the whole larger center of the second cover is fixed.

The order-three and commutation equations for the lift corrections follow by applying the actual composites to each basis vector. The normalizer equations use the entire original conjugation word on the odd subgroup. Two lifts of the same linear map differ by a linear functional, so their discrepancy on every basis vector determines the full discrepancy. The same complement-normalizer argument in the pullback extension constructs an action of the whole quotient. This pullback remembers the quotient coordinate; faithfulness of its action on the binary module is not assumed. Odd-subgroup averaging also gives the stated vanishing of the cohomology group H^2(Q,A*) with the dual binary coefficient.

## Evaluation and original finite equalities

Writing an element as a section element followed by a central-cover element gives exactly the evaluator's update: act on the current binary vector by M_j, add its quadratic and linear lift correction to the central coordinate, and then multiply by the selected binary correction a_j using the bilinear cocycle. This ordering is consistent with the right-action convention. The evaluator does not need the accumulated quotient coordinate when the two original words have already been proved equal in the original group.

That last premise is separately checked. The retained independent input checker matches all original presentation data, all 104 section words and all 83 target/frame word pairs to the original JSON. FGH independently ran the actual finite GAP program and checked all 83 equalities. The executed source SHA256 is `33df2599e248e95ed7936ada8a8b14f77961c502289d530304dc6c6458dadd48`. Its use of GAP's own commuting optimization is confined to the finite presentation, without formal central tails. Thus the disagreement in the old native formal-tail collector does not enter this gate.

FGH independently reran the action and value programs. All mathematical fields agree: the rank-72 form has target components `(0,0,0)` and the rank-36 form has `(1,0,1)`. Both total values are zero. Every one of the 71 s-frame corrections and nine r-frame corrections has value zero in both covers.

## Exact scope of the comparison

C.43 identifies the canonical image of the exterior-square coinvariants with the precise kernel of the natural two-primary H2 map to G86. Restriction of each constructed central extension to that image is its commutator pairing. The two independent pairings therefore detect the whole binary kernel. A quadratic refinement changes only the Ext component, and a quotient-inflated cohomology class vanishes on this kernel by naturality. Neither ambiguity affects detection.

Consequently an independently proved quotient identity for the target plus the same genuine s-frame corrections puts that exact original class in this kernel. Its two zero values then make the original two-primary class vanish. C.42 separately controls the three-primary part; s-frame commutators have exponent dividing two and therefore do not alter it. The quotient certificate must still justify the annihilator and the faithful torsion-to-relation-module comparison. Finally a full gentle lift must retain the required frames through its actual normalizations. Those later steps are not asserted by this audit.
