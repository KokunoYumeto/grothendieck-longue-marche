# E.48: exact polynomial norm systems and infinitely many ramified directions

For the actual finite etale extension Y^3=X, the determinant norm is

N(Phi_m(Y)) = Phi_m(X), for 3 not dividing m.

The proof computes N(Y-xi)=X-xi^3 with its exact sign and uses the permutation of primitive m-th roots under cubing. It also determines both cases where 3 divides m.

For the rational first class A=3 kappa_3(a), the systems Phi_m(X_n)^(3z) are actual completed multiplicative norm systems. E.46 turns them into continuous global H-section classes, and the scaled toric coordinate is z kappa_3(Phi_m(a^3)).

For any integer a>=2 and the increasing primes ell_j>=5, the integers B_j=Phi_(ell_j)(a^3) are pairwise coprime and prime to 3a. The full product of Z_3 parameters maps by

u_n = product_j Phi_(ell_j)(X_n)^(3^(j+1) z_j).

At each coefficient level all but finitely many factors are exactly one. A prime dividing B_j detects only z_j in the toric projection, proving injectivity. Compactness of the parameter product and the Hausdorff cocycle quotient prove that the image is closed. Taking every z_j=1 gives a continuous section with nonzero toric inertia at infinitely many distinct primes.

The actual geometric maps and their kernels remain those of E.38 and E.47. No intrinsic lifting assertion is added.

## Executed checks

The saved program and output are code/e_cyclotomic_norms.py, code/e_cyclotomic_norms.out, and code/e_cyclotomic_norms.json.

- 45 exact resultant identities, including every norm sign and both 3-divisible index cases.
- 108 total norms in radical finite etale algebras.
- 84 pairwise coprimality checks, with explicit supporting prime factorizations.
- Exact coefficient tail bounds for the unrestricted compact product.

All checks pass. The all-level assertions are proved by the universal determinant identity and the displayed convergence argument.
