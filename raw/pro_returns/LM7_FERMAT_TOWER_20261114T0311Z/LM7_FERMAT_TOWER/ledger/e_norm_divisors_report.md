# E.72: complete divisor coordinates and norm compatibility

## Proved outcome

The complex inverse norm system has exactly one surviving divisor chain over each eligible prime. Its eligibility condition is explicit: the rational prime p has v3(ord_p17)=1, and the chosen prime of Q(zeta3) is the one where17*zeta3 has residue of order prime to3. The corresponding prime at every higher level is obtained by its unique prime-to3 root in F_p. At3 and17 the existing unique totally ramified chains persist. All other compatible completed divisor coefficients vanish, because their residue-degree norm factors contain arbitrarily large powers of3.

The full complex divisor limit is therefore Z3² plus the restricted sequence module on this specified prime set. Rational norm is injective on it. This is an actual coefficient map, including the factor2 at17.

A prescribed divisor system has a coherent multiplicative lift exactly when its displayed prime-class sum vanishes in the3-primary class group of every specified number field. The proof first handles power completion at one field, then handles the inverse norm limit using compact principal-divisor fibers. Every finite collection of norm equations has a solution from its highest layer, so compactness gives a compatible solution at all levels. The global multiplicative completion itself is never treated as compact.

The entire nonempty fiber is the ordinary-unit norm limit. This is precisely the kernel of E69's base projection, hence has the already evaluated recursive product coordinates product_d Z3^(2*3^d). The remaining base root factor is tested by E57's literal first norm, because ordinary units there have norm1 in the3-primary completion.

## What is evaluated and what remains

The surviving prime chains, every ideal in the class equations, the transition coefficients, the exact root phase, the sufficiency of all-level compatibility, and the complete nonempty fibers are proved. The higher class matrices themselves are not numerically evaluated. In particular h remains the exact finite exponent from E69.

The prime-class identity is sharper than a name for a cohomology group:

ord([q_3,d])=3^(a_d), and c1 O_Ld=q_3,d^(3^(d-1)).

Thus q_3,2 has exact order3, and h is the eventual exponent of these particular prime classes. This does not turn a finite plateau into a stabilization theorem.

## Full positional comparison

The pure branch has eligible rational primes v3(ord_p17)=0, disjoint from the complex branch's v3=1. At3 there are two persistent pure branches and one complex branch, all residue degree1; at17 the residue degrees are1 and2. The rational norm map is therefore the identity away3,17 and has rows(1,1,1) and(1,2) at those two primes. Its kernel is exactly Z3³, with the displayed saturated basis.

It follows that every actual H toric fiber whose second coordinate has support only at3,17 consists of{3,17}-unit norm systems in both towers. Auxiliary prime valuations cannot silently cancel at infinitely many levels. This is proved by the actual divisor maps and does not identify these H sections with lifts through the intrinsic geometric kernels.

For complex component only, the entire support{3,17} system is beta^b times E69's unit system. Its base is(17*zeta)^b*lambda^(3^h*z). With pure component1 the J condition is b=3r, giving the displayed scaled toric map2r*kappa17+3^(h-1)z*kappa3.

## Executed certificate

The program e_norm_divisors.gp uses the official built PARI2.19.0 to factor both actual defining polynomials at all23 primes at most97 other than3 and17, at three levels. The discrete logarithms are checked by exponentiation. The seed is fixed explicitly. The program e_norm_divisors.py independently constructs the affine Frobenius cycles and actual weighted norm transitions. It verifies138 polynomial factorizations,171 transition systems and366 cofinal divisibility assertions. The branch norm matrix has the stated saturated rank-three kernel with unimodular completion determinant1.

The program also retains a finite example: E57's norm-root correction has divisor coefficients4,-2,-2 at the beta residues3,6,5 over7. Only the residue6 is the persistent branch. The other two primes become inert cubic at the next layer, so their coefficients fail the required divisibility by3. This concrete first-level correction cannot be prolonged even once.

## Separate attempts at h

Two original degree18 BNF computations continue without a class-group/unit result. No duplicate BNF calculation was launched. An explicit integral basis was proved locally and used for inexpensive degree6,18,54 ideal calculations. Weighted reduction recovers principal generators in degrees6 and18, but120 directions at degree54 produce no positive witness for the principal cube. This is not used as a nonprincipality result. A targeted search of degree18 units found only residues in mu3 and does not determine the full unit residue image.

The code and outputs of these exploratory attempts remain in research_norm_index/code/; the exact session status is recorded separately. They are not evidence for a numerical value of h.

## Audit

Root full-proof and fresh-execution audit PASS: all69 GP structured records are exact and the entire Python JSON is identical with no exclusions. The requested explicit E57 witness is now included as(E72.16). The files remain in research_e72 during the checkpoint149 deliverable freeze.
