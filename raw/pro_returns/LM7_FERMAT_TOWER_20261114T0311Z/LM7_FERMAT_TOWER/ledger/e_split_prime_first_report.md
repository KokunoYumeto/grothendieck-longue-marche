# E.56: complete mixed first fibers at a split prime

Status: Proved; independent full proof and fresh-execution audit PASS. The proof and certificates are installed in the deliverable after the checkpoint freeze was released.

## Exact scope

Let ell be a rational prime with v_3(ell-1)=1 and with three a noncube modulo ell. For every a != 0 and b in Z_3, E.56 evaluates every global section class of the actual inherited quotient H with first cocycle class 3a kappa_3(ell)+3b kappa_3(3).

Writing s=v_3(3a), the complete coordinates are Z_3^2 times the restricted sequence module on the explicitly eligible primes, times Z_3^(2s), times Z_3[[Z]]. The two unrestricted scalar coordinates and the restricted prime coordinates give exactly the scaled second toric Kummer coordinate. Each toric fiber is the explicitly parametrized compact group Z_3^(2s) times Z_3[[Z]]. The entire fixed-first fiber is torsion-free.

An outside prime p is eligible exactly when the three-primary component of ell^(3a) 3^(3b) modulo p is trivial. The displayed finite congruence uses a and b only modulo 3^max(v_3(p-1)-1,0), so the condition is defined for every three-adic a and b.

## Arithmetic comparison maps

The proof chooses actual Frobenius and tame inertia generators at the two primes of K=Q(zeta_3) over ell. An explicit conjugation makes the two Frobenius Kummer values of three exactly +1 and -1; both Frobenii fix the compatible roots of ell. Their Frattini determinant is a three-adic unit, so their images form a free basis of G_(K,{3})^(3).

Wingberg's opened Theorem 2.4 supplies the continuous inertia kernel. The induced inertia bundles give inverse maps identifying G_(K,{ell,3})^(3) with the free pro-three product of the two actual local tame groups. The same actual local inclusions give a complex-conjugation-equivariant section into the full relative arithmetic group. The proof states both bundle relations and maps rather than inferring a presentation from generator counts.

For the fixed first cocycle, the additive coefficient module is J=(3,T-1)Z_3[[T-1]]. Complex conjugation exchanges the two local factors. After normalizing its cocycle value to zero, the entire finite-ramification calculation reduces to one explicit tame relation and the exact residual odd-series conjugations.

The finite quotient is the actual cyclic group ring Z_3[C_(3^s)]. Multiplication by T^(3b/(ell-1)) removes the affine shift. Multiplication by ell has exactly 2s+1 finite orbits. Centered representatives have first moments +A/3 and -A/3, which compute the second augmentation and impose exactly one index-three condition. Equation E56.8 solves that condition with an explicit integral basis. The residual odd series is removed by an allowed geometric conjugation; the remaining even series is uniquely a power series in T+T^(-1)-2. Its constant is fixed by the prescribed second toric coordinate.

Outside ell and three the actual free inertia kernel acts trivially on J. Its equivariant additive maps are precisely the restricted families of the integral fixed Dirac measures. Each residue cocycle has a displayed toric correction kappa_3(p)-kappa_3(p)(sigma) kappa_3(3). Adding the specified unramified normal form produces a cocycle with exactly kappa_3(p) as its second toric image. This supplies the full global reconstruction and its inverse.

The comparison with E.46 is through its actual finite Kummer-Shapiro maps, followed by inertia extraction, finite orbit extraction, principal-ideal division and even projection. The reverse construction is the stated arithmetic cocycle and its corresponding norm system. The maps are inverse at every finite level and continuous in the established topologies. The restricted sequence module retains its noncompact inverse-limit topology.

The intrinsic Fermat group, its metabelian quotient and its marked-depth quotient still map to H through the exact kernels in E47.8. E.56 computes the target fibers; source lifting conditions remain attached to those kernels.

## Verification

The retained standalone Python program uses exact integer and rational arithmetic. Its successful execution checks:

- 36 actual affine Frobenius normalizations and nonzero Frattini determinants.
- 15 complete cyclic orbit decompositions.
- 81 exact finite-lattice, gauge, toric-coordinate and normal-form recoveries.
- 1,458 integral Frobenius power-series coefficients.
- 11,172 equivalent residue, order, discrete-log and affine-fixed-point tests.

The exact division certificates use a prime-to-three coordinate root and Laurent polynomial division, followed by a denominator with three-adic-unit augmentation. Negative exponents, nontrivial denominators, negative A, and an intentionally forbidden finite parameter are checked.

The first exploratory run failed on the ordinary dictionary lookup of the integer three in F_2; the corrected program reduces that lookup modulo p. Its original failure output is retained. The mathematical formulas were unchanged.

The proof covers all three-adic parameters and all levels. The finite checks verify the explicit formulas and signs; they do not replace the arithmetic and topological proofs.

## Source

Kay Wingberg, Riemann's existence theorem and the K(pi,1)-property of rings of integers, preliminary version 6 December 2007. Theorem 2.4 and its proof, printed pages 13-15, and Proposition 2.3, printed page 13, were opened directly. The forward implication of Theorem 2.4 explicitly includes infinite sets. The proof uses the already established K(pi,1) case containing the prime above three and the cyclotomic local unramified extensions. No new bibliography key is introduced.

## Independent audit

Agent a_structure read the entire proof and reran a fresh copied program. Its JSON is identical. The audit checked the actual local free-product transfer, integral Frobenius normalization, centered first moments, index-three finite lattice, even/odd conjugation, global residue normalization, and both Kummer-Shapiro directions. No correction remained. The completed audit is recorded in ledger/a_independent_audits.md. Root also independently checked the entire proof, with PASS recorded in ledger/root_split_prime_report.md.
