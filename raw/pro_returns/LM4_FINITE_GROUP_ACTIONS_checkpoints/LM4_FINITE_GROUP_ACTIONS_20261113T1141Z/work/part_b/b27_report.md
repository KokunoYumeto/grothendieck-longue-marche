# B.27: punctured-torus catalogue completed

**Proved and executed.** The four complete catalogues contain 13, 40, 38, and 115 finite-subgroup conjugacy classes for types (1,1), (1,2), (1,3), and (1,4). Each concrete group is its exact finite collection of rational affine matrices, recorded in `torus_affine_normal_forms.json`. The CSV and section JSON files retain every class and every requested invariant.

The proof establishes the bound on the translation kernel, enumerates all cocycles for the thirteen integral point groups, proves the exact affine-conjugacy tests, derives complete normalizer stratum permutations, and enumerates every puncture decoration modulo these permutations. It proves that topological normalizers induce the same stratum permutations as their averaged affine replacements. The final rational mesh has denominator144, with a Smith-normal-form denominator proof and separate inverse-matrix certificates.

Reproduce by running `python work/part_b/code/catalogue_tori.py`; it imports the attached `catalogue_low_complexity.py` and reads the independent B.25 type(1,1) CSV for a final comparison. The executed stdout is `catalogue_tori_stdout.txt`; the summary and independent-check result are `catalogue_tori_output.json`. The earlier denominator72 output is retained as `catalogue_tori_grid72_crosscheck.json`. Both counts agree; mathematical completeness is claimed for144.

Every local section satisfies its exact order and power formula; every section containing a rotation has exactly one maximal extension, while mirror sections with multiple maximal extensions remain visible. The (1,1) group-order/orientation/full-section/partial-section multiset agrees with the independently proved GL2Z amalgam catalogue.
