# E.45: complete local H section classes

## Completed classification

The actual arithmetic module quotient H=3Z3 semidirect(3,U)Z3[[U]] now has a complete local section classification over each K-prime away from3. The full geometric conjugation formula preserves the actual inertia coordinates a,c, and normalizes b,d uniquely in the multiples of3 between0 and3^(v3(q-1)+1)-3. The residual conjugation group is exactly UZ3[[U]].

For nonzero first inertia, E.42's finite two-row Smith system and its explicit representatives give all classes. For zero first inertia, the remaining operator D_b=qT^b psi_q-1 is completely evaluated on the augmentation ideal.

When r=b/(q-1) is integral, the coordinate group is the full product of Z3 indexed by j>=0 and units u modulo3^v3(q-1). The actual representative is w=d+T^(-r) sum z_j,u(T^(3^j u)-1), with v=cT^(-r). The series converges in the actual profinite completed-group-ring topology, equivalently (3,U)-adically. It is not claimed to converge U-adically with discrete coefficients.

When r is nonintegral, c must be0. Put t=v3(b). The coordinate group is the rank3^t lattice of vectors whose sum is divisible byq-1, with basis(q-1)e0 and e_i-e0. It has actual representatives w=d+z0 q(1-T^b)+sum z_i(T^i-1), v=0.

## Exact maps

The proof identifies the completed group ring with integral measures, not with a changed coefficient object. Multiplication by T^r conjugates D_b to D_0 in the integral-r case. Restriction to the clopen free q-orbits gives a topological product decomposition of the augmentation ideal; the inverse is the centered-measure series. Each orbit quotient is evaluated by the actual weighted integral integral q^(-n) dmu, whose kernel is multiplication byqS-1.

For nonintegral r, the affine action qx+b has exactly3^t free compact orbits. Weighted integrals give the full group-ring cokernel. Their sum moduloq-1 is augmentation, and a direct preimage construction proves the precise augmentation-kernel lattice, including injectivity. All quotient and representative maps are continuous between compact Hausdorff modules.

## Executed finite verification

`code/e_tame_classes.py`, `.out`, `.json` are complete. The program verifies48 finite coinvariant systems and36 actual transition maps for q=4,7,19,37,109 and several translations b. It computes the augmentation-ideal matrix in the basis delta_j-delta_0, verifies its exact Smith valuations against the orbit formula, and checks that both representative families generate the finite quotient.

For transitions, it checks group-ring reduction intertwines D_b and verifies the weighted-integral coefficients on every Dirac mass. Three full modular Smith transformation certificates are retained. The infinite centered-series convergence is also checked directly at every tested group-ring level, where all terms with j>=k vanish.

The all-degree result follows from the written integral measure and orbit proof. No finite experiment is used to infer an unproved infinite identity.

## Scope

This completes all local section classes of the actual H quotient. Intrinsic metabelian and marked groups map to H through the exact E.38 homomorphisms with their stated kernels. Their additional lifting conditions remain the actual E.37/E.44 tests. The proof does not assert that every H section lifts intrinsically.
