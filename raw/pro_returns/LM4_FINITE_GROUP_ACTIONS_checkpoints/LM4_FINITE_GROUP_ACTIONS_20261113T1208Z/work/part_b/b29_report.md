# B.29: punctured extended genus-two catalogues completed

**Proved and executed.** The complete catalogues for(2,1) and(2,2) contain32 and121 classes. Their positive portions10 and23 agree independently with the primary-source oriented computation in B33 on five full-section invariants. The negative involutions give4 and11 classes, independently matching B16.

The classification decorates intrinsic K-fixed strata and computes the entire normalizer action through the central hyperelliptic involution. Complement sheet labels are values of the character chi:E→F2. Colored sphere-cone permutations and pure braids give independent split-cone flips. Colored boundary dihedral symmetries have explicit sheet correction q*chi(e). Interior braids and the deck map supply the remaining allowed permutations. The proof explicitly allows punctures to pass through noncritical Weierstrass points and does not require the puncture set to be hyperelliptic invariant.

The finite mirror graph is subdivided before punctures are selected. Every line and oval is recomputed after deletion, as are the section poset and all stabilizers. Outputs record local puncture multipliers and explicit free orbit models for regular punctures.

Reproduce with python work/part_b/code/catalogue_genus2_punctures.py. It imports the attached genus2 and sphere programs and uses the exact closed catalogue, finite-presentation caches, and the copied oriented_higher_genus_catalogue_input.csv for its independent final check. All checks and counts appear in catalogue_genus2_punctures_output.json and the retained stdout.
