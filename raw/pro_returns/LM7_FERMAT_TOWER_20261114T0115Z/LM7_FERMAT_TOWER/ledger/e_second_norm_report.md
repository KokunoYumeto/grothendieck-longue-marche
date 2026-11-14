# E.62 — A second positional norm obstruction and the complete local tower

Status: Proved; independent full-proof and fresh copied-source execution audit PASS by a_structure (identical JSON). Root also read the complete proof and reran the program: PASS, no correction. The independent audit is recorded in ledger/a_independent_audits.md.

## Global finite positional obstruction

Fix the actual first cocycle A=3 kappa_3(17) in the genuine quotient H from E.38/E.46. At the first positional level the algebra is Q times K, K=Q(zeta3). The class(1,zeta3) has total norm one and therefore satisfies the actual J-cohomology condition.

E.57 supplies a literal lift at the next level: (1,w), with w=(g1/pi)^2 in L1, beta1^3=17zeta3, and N_(L1/K)w=zeta3. At the following level the complex component is L2=K(beta2), beta2^9=17zeta3. Its completion at17 is totally ramified of degree nine overK17 and has residue fieldF289. The norm of a unit reduces to a ninth power. That image has order32, so it excludes the residue ofzeta3, of order three. This finite residue quotient also detects the failure in the completions for multiplication by3^m. Thus no choice of the first lift extends further.

The actual maps are H toH3 toH2 toH1, with Hn the quotient by0 times(T^(3^n)-1)Lambda. The obstruction is to the indicated positional class. Its toric pair is(kappa17,0), which also occurs for the literal full global section g->(A(g),0,g). The comparison therefore explicitly exhibits two positional classes with the same toric pair and different lifting behavior.

## Complete local section fibers at seventeen

The pure local tower Fd=Q17(17^(1/3^d)) is totally ramified with residue fieldF17. The complex tower Ld=Q17(zeta3,(17zeta3)^(1/3^d)) is totally ramified overK17, with residue fieldF289. Their completed multiplicative groups are respectively Z3 and Z3 plusC9. The compatible uniformizers have exact norm equal to the preceding uniformizer; the common ninth roots have norm equal to their cubes.

Consequently each local finite positional fiber is the explicit group

    {(e,f) inZ3^2:e+2f belongs to3Z3} plus C9,

with transition(e,f,t)->(e,f,3t). The full local fiber is the displayed lattice, since the inverse limit of C9 under cubing is zero. It maps to the first positional coordinates as(17^e,(17zeta3)^f).

The toric quotient divides both raw coordinates by three. Its value is

    (kappa17, ((e+2f)/3)kappa17).

The inverse parametrization(e,f)=(3b-2f,f) proves that every second toric coordinate occurs and each toric fiber is exactlyZ3. The local classification includes the full geometric-conjugacy quotient: there is no remaining first-coordinate stabilizer because the cyclotomic Tate module has no fixed vectors.

## Exact certificate and scope

The standard-library Python program constructs F289 directly, enumerates its288 nonzero elements, and checks the cube/ninth-power norm images of sizes96 and32. It verifies that the literal E57 element reduces to2+8zeta3, whose cube iszeta3 and whose cubic residue iszeta3 squared. It verifies the C9 norm transition, the failure of all three first preimages at the next step, six residue norm degrees, and the lattice maps modulo3,9,27,81.

The initial one-token Python parse error is retained with its output. The corrected program passes every check.

This result does not use the still-unfinished class-group computation for the second complex global field. The obstruction and the entire local inverse limit follow from the exact local fields and their norm maps. The remaining global H fiber overkappa17 still requires compatible conditions at the other primes and the actual arithmetic comparisons retained in E.39.
