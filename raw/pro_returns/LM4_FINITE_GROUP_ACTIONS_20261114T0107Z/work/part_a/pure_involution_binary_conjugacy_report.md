# D.47: exact conjugator coordinates at the binary refinement

The combined executable `code/pure_involution_binary_conjugacy.py` repeats the D.45 finite construction, then solves the exact D.35 first equation by all four SL2(F5) conjugating matrices per component. It checks the third-cusp conjugacy in the complete finite conjugacy-class table, verifies actual finite invertibility through the named A5 generating-pair orbits, and imposes both Harbater–Schneps symmetries of the conjugating pair. The unit is retained modulo 120, which determines both its power residue modulo 60 and its half-exponent modulo 60.

All 324,000,000 refined involution coordinate pairs pass D.44's first-symmetry condition. Exactly 10,125,000 pass the full finite conjugator test, split equally between the square and nonsquare residue patterns modulo five. Therefore 313,875,000 are outside the finite image of the standard full conjugacy class. The six independent factor-orbit tables and a per-base histogram are recorded in the JSON output. Exactly four refined f-coordinates pass above each conjugator-compatible A5 base tuple; the other A5 base tuples have none.

The 64 f-coordinates over a fixed base t define the same actual finite automorphism. The new obstruction concerns the exact normalized coordinate f, which a full conjugator must satisfy, rather than only conjugacy of finite automorphisms. It does not establish a full lift of any finite survivor and does not settle full GT_0 involution conjugacy.

No new external reference is used. D.45 supplies the characteristic quotient, and D.35 supplies the exact full conjugator map whose finite equations are tested here.
