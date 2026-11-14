# E.97 — the evaluated ξc1 unit-norm coset

The result resolves the specific S-unit-norm coset left in E.84. The target ξc1 is a field norm from B2 to B1, but its actual S-unit defect is +1 in the coherent prime-73 basis of Cl_S(B2){3}=C3. Hence it has no S-unit norm preimage. On the completed power line the preimage set is empty for r outside 3Z3; for r=3z it is the literal preimage (ξc1)^z times the actual norm kernel, whose compact group type is C3 plus Z3^18.

The calculation uses the smaller complex layer L2/L1. An explicit 3-by-6 coefficient table gives u in B1 with horizontal norm β1. Matrices A^3=ζ, B^3=β1 and BA=ζAB convert that witness to w in L2 with norm ζ. Every field element and matrix is retained. The complete divisor of w has four split prime orbits, over 7, 13, 988728187 and 212464545716738508121. The exact HNF ideal equation is σ(D)/D=(w). In the actual E.86 lower genus coordinates D maps to (0,1,2), and hence to (0,1) in Cl(L2){3}=C9×C3.

The strongly ambiguous subgroup is exactly <q3> = <(3,0)>: invariant divisors are extended base divisors plus ramified primes, the seventeen-prime is principal, and ordinary norm surjectivity with jN=3 evaluates the extension image. The nonzero class of D therefore proves that ζ is not an ordinary-unit norm, despite its explicit field-norm witness. This uses the precise Hilbert90 divisor map, not a search failure.

The field square is essential. For any field preimage x of ξc1, its six S-valuations are (1,1,1,0,0,0). Thus y=N_h(x)/c1 has zero S-valuations and norm ζ. An S-unit x would make y an ordinary unit, which is impossible. For arbitrary field x the outside-S divisor is retained; its horizontal norm maps the B2 S-class defect to (0,1). The established class map z↦(0,z) fixes the sign +1 of the original defect.

The main portable rebuild has only two GP stages: the already proved degree-six lower genus and the owned literal witness/class calculation. It does not compute a BNF of L2 or B2. Python independently checks the rational norm forms, all three cyclic-algebra matrix identities, the absolute degree-eighteen norm, twelve Hensel valuation checks, all 27 inverse class coordinates, the nine ordinary quotient cosets, and the unique horizontal defect preimage.

Command from the workspace:

    python research_e97/code/e_unit_norm_coset.py --gp research_e52/vendor/pari-2.19.0/gp

In the final flat code directory, place e_stable_lower_genus.gp beside the driver and pass the GP executable path. Every GP stdout and the two complete PARI data objects are retained by the driver.

The preliminary horizontal S-unit solve, its exact cyclic switch, the separate ideal-defect calculation, and the coefficient export are also preserved with their actual stdout/BIN files. Three actual API/representation failures are retained with their sources and outputs; each was corrected before the final certificate. The two much earlier degree-eighteen BNF jobs were observed running without new output at 15:12:23 UTC; no duplicate was launched.

The eventual exponent h and the old B3 transvection remain unevaluated. The proof does not identify this single power line with all positional sections or with intrinsic section lifts. Its transfer is the exact norm map already used in E.46/E.88.

## Completed root verification

Author fresh two-stage GP/Python rebuild PASS. Only the degree-six lower BNF/genus is rebuilt; no upper BNF is used. The eventual exponent h and old B3 transvection remain unevaluated. Complete failed API/representation attempts and exploratory norm constructions are retained. Root read the complete frozen proof and every final program; the fresh copied reconstruction passed. Every complete JSON and stdout agrees byte for byte, with no exclusions. Both complete PARI objects compare equal without field or precision exclusions; raw BIN hashes and the actual object-comparison output are retained.
