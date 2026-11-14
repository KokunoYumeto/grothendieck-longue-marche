# E.94: the actual mu27 comparison

The next cyclotomic base change E=B3(mu27), of degree486 over Q,
has an explicitly evaluated maximal ordinary genus quotient
C9^3 plus C3 and S-genus quotient C9 plus C3. These are actual
quotients of the corresponding upper class groups; no full upper
class group is assigned from the calculation.

The proof gives every field inclusion and restriction. E/B3 is
totally ramified at each prime over3 and unramified inert at each
prime over17. The actual norm and extension coefficients are therefore
(1,1,1,3,3,3) and (3,3,3,1,1,1), respectively.
The ordinary and S-class norms are onto, proved by the Hilbert
class field intersection and actual Frobenius maps.

The actual automorphisms G,H have orders27,9 and satisfy
HGH^-1=G^4. G does not preserve B3: its exact conjugate of the
cubic deck generator is G^-9 H^3. The original g2,h2 are the
restrictions of G^3,H. Their actions on the new genus quotients,
including every coordinate inverse, are retained.

The two local norm characters at each wild prime have joint
quotient C9 plus C3. A literal eleven-column norm family proves the
entire new cyclotomic unit-norm kernel. Its index is justified by
local class field theory. The original insufficient norm family
and its actual failure output are retained. The arithmetic sign of
the cyclotomic character is fixed by the inverse-unit Artin action,
including the exact values on beta1 and 1+beta1.

The ordinary genus norm onto E91's A9 has kernel C3^2. The actual
ideal extension kills E91's residual transvection, so it factors
through A9. Both compositions are multiplication by3. The six
prime columns independently verify all residue and ramification
coefficients. This explicit map explains why the new genus
calculation does not decide that old transvection or the exponent h.

On the new relative S-genus group, G is identity and H has matrix
[[1,3],[2,1]], with row moduli9,3. The actual norm to the original
coherent prime73 C3 is -x modulo3. The upper deck coinvariants thus
surject onto C9 plus C3. A cyclic module over the cubic deck group
ring would have cyclic coinvariants, so this actual quotient proves
that the former cyclic-module premise fails for this base change.

## Exact reconstruction

    python research_e94/code/e_mu27_comparison.py --gp research_e52/vendor/pari-2.19.0/gp

The portable driver also works in the final flat code directory.
It uses the three already retained E76 dependencies
e_basechange_field.gp, e_basechange_ninth_norms.gp and
e_basechange_ninth_genus.gp, then the three owned local/genus/export
stages. It starts only the certified degree18 B1 calculation.
The six-stage author reconstruction77324 exited0.

All91 structured records, ten full Smith systems with integral
inverse maps, 2187 relative ordinary coordinates,27 relative S
coordinates,243 normalizer elements and the actual prime maps pass.
The actual local/genus BIN objects and certified B1 BNF are retained.
Five failed attempts and their literal stdout are included; no
missing successful output has been invented.

## Remaining arithmetic

The full upper ordinary/S-class groups, the old residual
transvection, and the limiting exponent h remain unevaluated.
E94 supplies an exact field and class-map comparison and an evaluated
noncyclic quotient. It does not infer principality or nonprincipality
from an unsuccessful element search, nor a stabilization assertion
from a finite level.

The two original expensive L2 BNF jobs were actually polled at
14:40 UTC and remained running without new output. No duplicate
BNF computation was started.

## Independent root verification

The complete proof and all final GP/Python programs were read. The fresh six-stage copied-source reconstruction passed. Complete JSON and every stdout file agree byte for byte, with no exclusions. The three raw BIN byte strings differ, and their complete PARI objects compare equal without any field or precision exclusion. Root freshly opened Milne V5.2 with its full proof, V5.3 and the explicit inverse cyclotomic sign in V5.9--5.10 (turn800view0--1 and turn801view0). The previous exact local norm, Hilbert-class-field and Chebotarev proof scopes remain explicit.

A separate full proof/source audit passed, including actual ideal-extension factorization, local maximality and the inverse cyclotomic sign. Its fresh91-record finite verification is exact, and explicitly excludes the six GP stages already rebuilt by root. See a_e94_audit.md.
