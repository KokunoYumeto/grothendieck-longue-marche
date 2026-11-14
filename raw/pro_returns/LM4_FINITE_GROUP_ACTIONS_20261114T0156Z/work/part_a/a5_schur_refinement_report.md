# D.45: characteristic binary-icosahedral refinement

The exact quotient is SL2(F5)^19 × C2², formed from the 76 epimorphism kernels to SL2(F5). Its central reduction is D.38's A5^19. The proof supplies the named two-generator map, proves surjectivity using perfection and the exact A5 quotient, and identifies its kernel by all four sign lifts of each representative pair.

The executed program checks both Harbater–Schneps cycles and the full involution norm. Exactly 5,062,500 base tuples lift, and they coincide with the triangle survivors. Every survivor has 64 f-coordinates, producing 324,000,000 refined coordinate pairs in total. Those 64 central choices yield the same actual automorphism at this quotient; the proof distinguishes the coordinate count from the automorphism count.

This identifies a single characteristic finite refinement that detects the previously proved triangle obstruction. It supplies no new exclusion among the remaining 2,531,250 finite survivors outside the standard pure conjugacy model. No finite survivor is asserted to lift to a full GT_0 involution.

The calculation is self-contained finite matrix arithmetic and uses the previously verified D.38 A5 enumeration. No additional external theorem or bibliography entry is needed. Captured output is in code/a5_schur_refinement_output.json and code/a5_schur_refinement_stdout.txt.
