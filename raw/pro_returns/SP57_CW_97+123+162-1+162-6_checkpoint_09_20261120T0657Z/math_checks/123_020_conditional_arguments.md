# Targeted checks prompted by 123/020

These checks use the supplied pages and explicit algebra only. They do not supply ink missing from the typescript.

## The U-orbit statement, under the graded SL2 setup

Work in characteristic zero with a finite Z-graded Lie algebra arising from an sl2 triple, with a in degree 2, and positive-degree nilpotent Lie algebra u. Suppose the indicated exponential identifies u with the unipotent group U in the setup under consideration. The elementary sl2 weight formulas show that ad(a):g(r)→g(r+2) is onto for r≥1: in each finite-dimensional irreducible sl2 module, the raising operator maps onto every positive target weight above 2. This is a representation-theoretic hypothesis check, not an ink reading.

Conjugation by exp(x), with x of positive degree r, changes a first in degree r+2 by [x,a]. Higher terms have strictly larger degree. Given a+v with v in Fil³(g), remove its degree-3 component using x in g(1), then its degree-4 component using g(2), and continue. Previously corrected degrees are unchanged. The grading is finite, so this terminates. Thus U acts transitively on a+Fil³(g). Conversely, positive-degree conjugation cannot change the degree-2 component. Distinct a therefore give distinct U-orbits in this set.

The exponential is equivariant for conjugation wherever this finite nilpotent construction applies, so the same statement holds for the displayed exp-set. To obtain the page's single P-orbit on the union over g(2)*, one additionally needs the Levi's transitivity on g(2)*. That orbit assertion is carried as background here, not proved by the filtration argument. General group-scheme or base-ring extensions are not asserted.

## What a possible g(1)=0 interpretation would imply

The typescript leaves a blank before (1)=0. It remains blank. For a conditional check only, interpret the missing object as the graded Lie algebra g and “principal” as the regular single-block SL2 representation in type A.

The explicit dimension-four representation with blocks (2,2) has diagonal weights (1,1,−1,−1). No matrix unit has weight 1, so g(1)=0, but E has nilpotency index 2 rather than the regular block's index 4. The block pattern (3,1), with weights (2,0,0,−2), gives a second example: g(1)=0 and nilpotency index 3. The matrices in the certificate satisfy all three sl2 relations exactly and come from direct sums of polynomial symmetric-power representations. Thus this interpretation of the stated equivalence is false in that setup. It is not a license to identify or fill the blank or to redefine the author's word.

## The marginal A2 and A4 examples

The block pattern (2,1) in dimension 3 has weights (1,0,−1), and (4,1) in dimension 5 has weights (3,1,0,−1,−3). Every weight is distinct, so the associated descending weight flag is complete and its stabilizer is a Borel. These E matrices are not regular single blocks: their nilpotency index is n−1, and exact commutator-kernel computations give conjugacy orbits of dimension two less than the regular block's orbit. These are the explicit (n−1,1) examples underlying the source's “sous-réguliers” terminology; no classification of all subregular orbits is used.

For comparison, (3,1) in dimension 4 has the repeated weight 0 and a partial flag of dimensions 1 and 3, not a full flag. This agrees with the contrast suggested by the A2/A4 ranks in the marginal example. It does not resolve the antecedent of the differently worded marginal note on 123/019, and the earlier conditional noninjectivity computation remains valid.

## Unit stabilizer and the group center

The setup stated on 123/016 allows a semisimple group in characteristic zero; the supplied text inspected here does not impose an adjoint-group hypothesis. For G=SL2 and the identity principal homomorphism, −I is a nonidentity determinant-one matrix commuting with the entire image. The stabilizer is therefore not the unit group, and conjugation on that orbit cannot be free under SL2. This is a direct counterexample to the unqualified unit-stabilizer/G-torsor assertion under those assumptions.

More generally, in a single irreducible type-A block the diagonal weights are distinct. A commuting matrix is therefore diagonal; commuting with the nonzero adjacent entries of E forces all its diagonal entries to coincide. The commutant in GL_n is scalar, leaving μ_n in SL_n and trivial stabilizer after passing to the projective quotient. This supplies a concrete refinement in the checked examples, not a general assertion for every reductive form.

The author's final “la réciproque n'étant pas vraie sans doute” is retained as a hesitation; no counterexample to that general converse is claimed here. The cancelled earlier “sans doute” belongs to the separate Borel parenthesis and is not revived.
