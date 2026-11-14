# E.74 wild local layer certificate

Status: PASS for degrees 1, 2 and 3. The full, geometrically metabelian and marked quotients have identical integral layer matrices in these degrees; the program verifies this equality for both arithmetic generators.

| Degree | Layer rank | Smith valuations, including units | Free rank of H2 | Finite part of H2 | Free rank of H1 |
|---|---:|---|---:|---|---:|
| 1 | 10 | 0:5 | 5 | 0 | 15 |
| 2 | 45 | 0:29, 1:11, 2:4 | 1 | C3^11 + C9^4 | 46 |
| 3 | 330 | 0:237, 1:63, 2:23, 3:7 | 0 | C3^63 + C9^23 + C27^7 | 330 |

The presentation is the actual integral matrix [T_r-7I | J_r+I], with T and J imported from E.41. The arithmetic input now resolves beside the program in an installed code directory, with the research-directory fallback retained.

## Actual coordinate maps

Degree 1 retains exact integer Smith transformations and their exact integer inverses in the JSON. Both products of each inverse pair and the Smith identity are verified. The last five coordinates of Lx give the five free coordinates; the inverse is L^-1 applied to those coordinates with zero pivot coordinates.

For degrees 2 and 3 the NPZ files retain A, L, R, L^-1 and R^-1 modulo 81 and 729, respectively. Every elementary row/column operation is also retained in the JSON. The program verifies LAR=D and both orders of each inverse product. Every positive Smith pivot is separately checked through the forward/inverse torsion-coordinate maps and its full annihilating modulus.

In degree 2 the exact first Hall row, corresponding to [x1,x0], is zero in A. It is the primitive free quotient. The unused Smith row is exactly this row, and every torsion inverse column has zero first coordinate. Thus first remove x[0]e0, apply L to obtain the torsion digits, and retain x[0] as the free coordinate. The inverse uses the saved L^-1 and then restores x[0]e0.

## Precision proofs

The integral split-lattice matrices satisfy B_r C_r = 3^r I and F_r B_r = B_r D_r, with F the actual Frobenius at the K-prime above 2. In the cokernel all arithmetic elements act by their cyclotomic scalar: this follows from the relations for tau and complex conjugation, their conjugates, and closedness of the finitely generated relation module. Consequently (F_r-4I)L_r lies in the relation module.

In degree 2, let K be the first-coordinate-zero lattice. The saved exact matrices verify that its determinant-elliptic eigencoordinate vanishes after C_2, and
(F_2-4I) B_2 diag(0,-1,+1) C_2 K = 108 K,
where the diagonal signs are selected by the actual split eigenvalues 4,-8,16. Therefore 27 annihilates the torsion. Reduction modulo 81 determines every torsion invariant, while the primitive free coordinate is retained integrally.

In degree 3 the split eigenvalues are -32,-8,16,64. Each 9/(e-4) is in Z_3. Together with B_3 C_3=27I this proves that 3^5 annihilates the cokernel. Reduction modulo 729 therefore determines every invariant. The actual Smith computation is stronger: the largest invariant is only 27.

## Attempt history

The original exact-integer Smith program completed degree 1 and was interrupted while computing degree 2; its actual source and output remain unchanged. The separate inline diagonal-only SymPy computation reached its explicit 20-second alarm and produced no result. Their precise session/exit statuses are retained in e_wild_layers_attempt_status.json. Neither attempt is reported as a successful degree-two calculation. The completed program uses the proved finite-precision method above.

Degree 4 was not run: the requested useful degrees 1-3 are complete, and the degree-four rectangular transformations are substantially larger. No degree-four value is claimed.
