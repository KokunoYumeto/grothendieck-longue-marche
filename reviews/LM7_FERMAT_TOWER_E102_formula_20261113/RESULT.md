# E.102 of LM7_FERMAT_TOWER: independent recomputation and the structure behind the numbers (13 Nov 2026)

By the main Claude session (Claude Opus 5.5 at effort max), with its own code (`e102_formula.py`). Only the degree-one
data were taken from the return (the definitions in `arithmetic_inputs()` of
`answers/LM7_FERMAT_TOWER_20261113T2044Z_unzipped/LM7_FERMAT_TOWER/code/e100_root_rebuild/inputs/e_unramified_sections.py`,
read, not run). E.102 is a claim of GPT-6 Astra (ChatGPT Pro mode).

**Identification used.** N is free pro-3 of rank 10 (its rank tables are those of the free Lie algebra on 10
generators: 10, 45, 330, 2475, 19998). For a free group, gr N = Lie(V) with V = N^ab = Z_3^10, and every
automorphism acts on gr through its action on V. The degree-four kernel is
K_4 = ker(L_4(N) -> L_4(N/N'')) = [L_2, L_2] = Lambda^2(Lambda^2 V), of rank C(45,2) = 990.

**Recomputation.** With T_1 = the action of tau on V (cusp loops x7, genus part [[1,-3],[3,-2]], eigenvalues
1+3 zeta_3 and its conjugate) and J_1 = the action of c, the cokernel of (T_4 - I)(I + J_4) on Lambda^2 Lambda^2 V is
  Z_3^504 + C_3^144 + C_9^56 + C_27^30 + C_81^9   (247 unit pivots; torsion 3^382),
exactly E.102. **E.102 is confirmed.**

**Split model.** With the extension block of V (cusp loops by the genus part) set to zero, the same computation
gives Z_3^504 + C_3^443 + C_9^43 (torsion 3^529). This agrees with a closed formula computed by hand: K_4 splits into
the Schur pieces Lambda^2W(x)W(x)C (16), Lambda^2W(x)Lambda^2C (28), Lambda^2W(x)S^2C (36), S^2W(x)Lambda^2C (84),
W(x)C(x)Lambda^2C (448), Lambda^2(Lambda^2C) (378); on each, T = (small matrix on the W part)(x)(scalar 7^k on the C
part), so the cokernel is Q+ (x) N+ + Q- (x) N- with Q+- = M/(sT_M - 1)M+- computed from 1-, 2- or 3-dimensional
matrices and N+- the J-eigenspaces of the Schur functors of C (C+ = 3, C- = 5). Pieces: Z^8+C3^8; Z^13+C9^15;
Z^21+C9^15; Z^43+C3^28+C9^13; Z^224+C3^224; Z^195+C3^183.

**What moves the actual numbers.** Only the integral extension 0 -> C -> V -> W -> 0. N is the fundamental group of
the Fermat cubic minus its 9 cusps; the cusps are its 9 flexes, i.e. E[3] for the j = 0 elliptic curve, and N is the
Frattini subgroup of the free pro-3 group on two generators (pi_1 of P^1 minus 3 points), free of rank 1 + 9 = 10 by
Schreier. The extension class is the cuspidal 3-torsion (the "/3" in the off-diagonal block). It lowers the total
torsion from 3^529 to 3^382 and moves it into exponents 27 and 81.

**Open (the formula for 144, 56, 30, 9).** Decompose Lambda^2 Lambda^2 V as a module over Z_3[E[3]] (E[3] = (Z/3)^2
acts by deck transformations; Z_3[(Z/3)^2] is not semisimple, which is where higher 3-power torsion comes from),
with tau and c acting compatibly, and compute the cokernel piece by piece.
