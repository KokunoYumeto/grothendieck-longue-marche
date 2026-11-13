# E.44: exact higher central lifting images

## Proved criterion

For the full cubic pro-3 group, its metabelian quotient, and the quotient marked at the single rational cusp B0, fix any actual lower section and any degree r>=3. The error of the lifted tame relation at a prime of K=Q(zeta3) is an explicit element of the central lattice A_r. Its unique rational correction is minus (Frobenius-q)^(-1) applied to that error. A global lift exists exactly when every correction is integral and the corrections tend to zero three-adically over the primes away from3.

The criterion includes the continuous inverse-limit obstruction. The support sequence is formed at finite coefficients, with direct sums over finite sets of removed primes, before taking the derived inverse limit. The actual image, without closure, occurs in the resulting restricted-sequence cokernel.

## Exact maps and gluing

The actual lower cocycle and a continuous Hall set lift give a continuous central two-cocycle. On tame inertia, the homomorphism t^s -> n^s is an explicit local splitting. Its Frobenius defect, divided by q, is the chain-level localization representative. Changing inertia lifts gives precisely the differential q^(-1)Frobenius-1. Central changes of Frobenius lifts have no effect.

At each finite coefficient level, the local splitting cochains vanish outside finitely many base primes uniformly over prolongations. Their dependence on conjugating elements is locally constant. Global localization gives a lift, and its degree-one residue sequence adjusts the lift to the prescribed inertia. The remaining choices are finite unramified cocycles. Compactness gives compatible continuous global lifts. This establishes actual gluing and the continuous inertia-bundle equivariance, rather than assuming that arbitrary pointwise inertia lifts already glue.

Restriction to K detects the rational obstruction because restriction followed by corestriction is multiplication2. Every nonempty rational geometric-conjugacy fiber is the explicit matrix-cokernel group from E.41. The same weight argument proves that all differences between lifts are unramified outside3 and that no additional lower-section stabilizer acts.

## Executed exact local calculation

Files: `code/e_higher_images.py`, `.out`, `.json`.

At the K-prime(2), residue cardinality4, the degree-three central matrix is the actual Lie3(Frobenius)-4. Its Smith valuations are:

- 0, multiplicity132;
- 1, multiplicity70;
- 2, multiplicity24;
- 3, multiplicity76;
- 4, multiplicity28.

Therefore the local obstruction group is C3^70 plus C9^24 plus C27^76 plus C81^28, of order3^458. This module is common to the full, metabelian and single-cusp marked quotients because their actual central layers agree through degree3.

The JSON retains complete invertible transformations modulo729 and every elementary operation. The exact split-lattice identity B3 C3=27I and the split eigenvalues64,-32,16,-8 show that the cokernel is killed by3^5, so the finite certificate determines the integral answer. The multiplicities168,128,32,2 give the independent determinant valuation458. Five exact rational inverse corrections are checked as linear-lattice examples; they are not claimed to be errors of globally realized lower sections.

## Sources opened

Milne, Arithmetic Duality Theorems, second edition: II.0.1(f), II.1.7(b), II.2.9 and the previously verified finite-coefficient I.4.10(c), I.4.15. Jannsen, Continuous etale cohomology: Theorem2.2, Proposition1.6 and their exact inverse-limit comparison. Existing bibliography keys are reused, with no duplicate entries.

## Exact remaining arithmetic input

The theorem evaluates the lifting image from the actual higher Frobenius action and actual lower section values. The latter are lambda(h_q)u(sigma_q), with the correction word h_q from E.39 retained. The linear matrix Phi_q on A_r is determined by the full rank-ten action; the error additionally uses the genuine higher action on W_r. Evaluation of those higher words for every ramified input is still the remaining step in a complete full metabelian or marked section classification. E.41 completely handles the unramified family, and E.38/E.43 evaluate particular ramified families.

## Rational-prime refinement and independent audit

The actual rational-Q2 local obstruction module is also evaluated: C3^36 plus C9^12 plus C27^38 plus C81^14, of order3^230. Its Smith valuations are0^230,1^36,2^12,3^38,4^14. The program retains both transformations and verifies the square agrees with the K-Frobenius matrix. The comparison is an actual integral norm-one CM action on the entire generalized-Jacobian lattice, with elliptic block v and lower block U(v-I)/3. It conjugates rational Frobenius to elliptic sqrt(-2)C_E and toric2P. The root is computed modulo2187 so the divided block is correct modulo729. The same3^5 exponent bound follows by factorization of Frobenius squared minus4.

Agent A independently reopened the stated primary passages, audited the complete proof and both Frobenius comparisons, and reran the program. Both Smith certificates, determinant checks and precision bounds passed.
