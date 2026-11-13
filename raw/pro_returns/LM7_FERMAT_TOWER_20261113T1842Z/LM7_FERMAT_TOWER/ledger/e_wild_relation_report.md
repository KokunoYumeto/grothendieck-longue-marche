# E.75 — the actual relative module and uniform wild coordinates

## Result

The actual relative kernel R3 in the split local source has the compact left-module presentation

    R3-ab = Lambda^2 / Lambda(tau-7, -(tau'-7)),

with the involution exchanging the two coordinate generators and acting on Lambda by conjugation. The proof constructs this isomorphism from the actual local Fox row and records its inverse. A single actual source element r* is chosen once, and its conjugate supplies the second generator. Thus the extra factor in E.74 is evaluated uniformly as

    ker((1-J)(T-7): A -> A-minus).

The actual cocycle inverse is theta_a(r) + u(g) on r*j(g), with theta_a obtained from the displayed module map. The resulting finite local cochain model is A-plus -> A direct-sum A -> A-minus. The second differential is (u,a) -> (1-J)(T-7)a.

## Proof points

The first local Kummer calculation fixes an actual relative Frattini basis before any source change. The characters of u2 and u3 form the relative dual basis; their values on an element and its conjugate have the exact matrix written in the proof.

The minimal completed resolution is proved from the actual four generators and local H2 dimension one, H3 vanishing. Compact Nakayama and the Hom-to-F3 sequences force free ranks 1,4,1 and kill the next kernel. The completed Fox/bar comparison identifies its top row with an actual relation.

The top involution is normalized by the explicit unit (1-w)/2. Projection to the free quotient kills the first two Fox coefficients by the left-freeness of the ordinary augmentation ideal. The remaining two coefficients generate a right ideal. Finite regular coefficients, with commuting right multiplication, identify that ideal exactly with the kernel of the cyclotomic evaluation tau,tau' -> 7. All inverse limits use finite cohomology and retain the right character.

Twisted first-letter division gives the unique right-module basis matrix. Its inverse gives the source change, and applying the involution proves the exact equivariance. The source element r* is an actual lift of the resulting class in R3-ab; its pro-three word is not claimed numerically evaluated. This single source choice replaces the coefficient-dependent unspecified saturated lattice basis in E.74.

The top-cell scalar is fixed using the k-local Brauer invariant. The comparison over Q3 consequently sends the anti-invariant cochain class y to [y/2]; the inverse sends [x] to [(1-J)x]. The factor two is the actual restriction/corestriction degree and is checked in the coefficient matrices.

## Computation

The program a_wild_kernel.py uses the actual E.41 matrices. Exact rational elimination over Q intersect Z3 retains domain and codomain transformations, domain inverses, diagonal identities, saturated kernel bases and their coordinate inverses. It also evaluates the degree-zero map independently.

The kernel ranks are 9,22,164. The second-differential Smith valuations are respectively 0^1; 0^8,1^11,2^4; and 0^73,1^63,2^23,3^7. They give exactly the E.74 obstruction groups through the proved scalar comparison.

The program verifies finite coefficient orders for all three degrees and m=1 through6, plus every finite-kernel transition generator from m=2 through7. These checks use reduction of exact three-integral matrices, with the full transition multiplier lists retained.

## Scope

Every map is for the actual relative local arithmetic source and the geometric lattices in E.41. The additive source map is now uniform and the extra kernel coordinates have explicit numerical bases. Formula E75.25 retains the exact nonlinear restriction/equivariance problem for R3 -> W. Its higher relation values are not inferred from R3-ab, and E.23 remains open.

## Files

- sections/E_wild_relation_module.tex
- code/a_wild_kernel.py, a_wild_kernel.out and a_wild_kernel.json
- ledger/e_wild_relation_results.json
- ledger/e_wild_relation_source_evidence.json
- ledger/e_wild_relation_refs.bib


## Independent root verification

The root read the complete proof, checked all exact left/right module maps and the index-two invariant normalization, and executed the frozen program in a fresh directory. The complete JSON certificate agrees in every field, with no exclusions. All18 finite-cohomology identities and1818 finite transition generators passed. The exact hashes and reviewed proof points are retained in root_e75_audit.json.
