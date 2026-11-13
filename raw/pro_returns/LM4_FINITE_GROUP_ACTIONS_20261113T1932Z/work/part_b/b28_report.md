# B.28: extended closed genus-two catalogue completed

**Proved and executed.** There are 92 classes: 57 full hyperelliptic lifts of the sphere6 catalogue and 35 complementary character-kernel classes. Exactly 21 preserve orientation. The proof computes the full normalizer action on characters, including fusion of complements under cone exchanges and cyclic mirror-branch permutations.

Each central presentation has an independently executed regular Todd–Coxeter permutation action of exactly twice the spherical group order. All relators, local injections, orientation characters, Euler characteristic -2, and the six fixed points of the central involution are checked. Complete cone/corner cosets and mirror graphs give the section posets; complement posets are recomputed after restriction.

The positive 21-row multiset agrees independently with work/root/higher_genus_output/oriented_higher_genus_catalogue.csv on order, full sections, partial sections, Phi, and Phi-orbits; see genus2_oriented_independent_crosscheck.json. The seven order-two rows also split into two positive and five negative classes, agreeing with the real-involution classification.

Reproduce with python work/part_b/code/catalogue_genus2_extended.py. Dependencies are Python and SymPy, plus the included catalogue_spheres.py and genus2_characters.py. The genus2_extension_cache JSON files retain the exact finite coset actions and relators; deleting this cache regenerates them from the presentations. The main CSV, section JSON, summary and stdout are attached.

New primary reading: Farb–Margalit, Section9.4.2 p257, and its proof Section9.4.3, directly opened in the complete book. The exact genus-two quotient is printed there; the extension to negative mapping classes is proved by a commuting reflection.
