# E.65: every adjacent pure-seventeen norm

## Proved result

The exact cyclic-complexification map is followed by explicit quadratic descent: from N(b)=z in the real base, z/(b*c(b)) is an actual pure preimage of z. Keeping the cubic generator fixed makes conjugation act by negative permutation on the relative Brauer local coordinates. The global quotient is therefore one F3 per nontrivial conjugate pair, with no additional sum relation.

This identifies every pure norm condition. At primes away from3 and17, an unramified inert cubic contributes its valuation modulo3. A residue field of cardinality2 modulo3 gives a linear-quadratic algebra with surjective norm. The unique prime17 has surjective pure local norm. At3 the pure field has two completions of degrees3^(d-1) and2*3^(d-1); precisely the second contributes a single wild coordinate, for d>=1.

The wild coordinate is evaluated by a finite matrix over F3. The actual local integer ring is reduced modulo pi^(2e+1), already a quotient of Z/27. Cubes of the ordered unit generators and determinant norms of every source unit generator provide the rows. Local reciprocity proves its nullspace has dimension one in every degree. Thus this is an all-degree finite algorithm, with exact executions at d=1,2,3.

The ordinary norm-one group is torsion-free free abelian of countably infinite rank. Its multiplication completion is the explicitly restricted sequence group, so every nonempty fiber has computed coordinates and topology. Both completion exact sequences are proved rather than inferred from compactness.

## Concrete first witness

The certified fundamental unit epsilon=7*cuberoot(17)-18 has wild symbol2. The certified first unit norm matrix is (0,3,0,0), with signs (0,0,1,0); the four actual source units and three kernel generators are printed in the theorem. Both pure fields have certified class number1. The exact determinant verification agrees with PARI.

## Executed files

- `code/e_pure_norm_fields.gp` and `_gp.out`: official PARI2.19.0, certified fields and unit bases, actual relative unit norms, complexification embeddings, prime ideals and39 contractions.
- `code/e_pure_norm_local.py`, `.out`, `.json`: finite wild rings, all ideal indices, unit relations, determinant norms and1456 additivity checks.
- `code/e_pure_norm_verify.py`, `.out`, `.json`: independent characteristic-zero and finite-field checks,1014 finite norm determinants,4 unit norms,6 Eisenstein layers,9 witness powers.
- The initial polynomial-domain comparison failure, compositum-shape failure and accessor/prototype evidence are retained; the successful exact values are unchanged.

## Scope and comparisons

The theorem evaluates the pure factor of the same actual positional arrow as E.64. Norm transitivity proves preservation of the E.46 total-norm J condition. It does not replace compatible inverse-limit choices by unrelated finite-level choices. The entire H section set on the17 line still requires that all-level calculation.

## Independent audit

Root read the complete final proof and all three programs, reran fresh copies and compared all49 GP structured records and both complete JSON certificates. Every value agrees, with no elapsed-time or other field omitted. The audit corrected a product-notation typo and spelled out the normal closure Q(mu_{3^{d+1}},17^{1/3^{d+1}}) in the infinite-rank proof. Neither correction changed any arithmetic value. Root also reopened and read Milne's complete Hasse norm proof, relative Brauer exact sequence and cyclic comparison, local norm-index argument, crossed-product theorem and complete Chebotarev proof. The audit output and all fresh execution outputs are retained in code/.
