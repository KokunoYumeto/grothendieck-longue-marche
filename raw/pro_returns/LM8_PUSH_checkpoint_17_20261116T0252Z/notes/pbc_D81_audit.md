# Independent full audit of D81

**PASS**, reviewed by pbc_groups on 2026-11-15. The whole written proof and exact certificate have been checked, including the nonprimitive and zero local vectors. No mathematical correction is required.

## Actual images and coinduction

Global residual independence supplies two actual inertia vectors of unit determinant, and hence the full translation group H=Z5^2 in the actual operator image. The convergence and local gauge are the already audited D80 constructions.

The local complement remains exact even for a nonsaturated line: every translation lies in H5=Z5(alpha,beta), and the actual I0-kernel realizes every element of this subgroup. Correcting a lift of an I0 element by such a kernel element removes its translation. If H5=0, no correction is needed and the local image is precisely I0.

A nonzero closed line is carried by an integral change of coordinates to 5^e Z5 times0. The displayed finite-residue-times-Z5 transversal is continuous, so H is an actual product of H5 and that transversal as a translation space. Continuous function-valued cochains are coinduced with the transversal as coefficient variable. Compactness ensures that currying gives a locally constant map into the discrete function module: a continuous function on the compact product has a finite rectangular clopen refinement. Thus the acyclicity argument does not assume a saturated complement or exchange an infinite direct sum with a product. Positive cohomology of the zero group vanishes directly.

The actual Hochschild--Serre comparison, constant Cartier coefficient module lambda, and finite affine-image Chebotarev injection are therefore valid for every local vector in the statement.

## Connecting module and every annihilator case

Let f=t1^alpha t2^beta-1, R=Lambda/(f), J=(u,v)R and P=u v w. The augmentation ideal, f-ideal and P-ideal are stable under the actual semilinear action: exponentiation by a cyclotomic unit multiplies their defining elements by units. All ideals appearing in the compact exact sequence are closed, being images of finite products of the compact power-series ring.

The actual primitive delta has beta_delta-1=P times a unit; every cyclotomic-kernel multiplier differs from one by P. Hence the two invariant modules are exactly the Cartier duals of R/PR and J/PJ with their Gamma invariants. This remains valid when those compact quotients have infinite Z5 rank.

The compact four-term sequence follows from the map J/PJ to R/PR: its kernel is PR/PJ and its cokernel is R/J=Z5(2). Multiplication by P identifies the kernel with R/(J+Ann_R(P)).

For a boundary prime L, reduction of Lr=fh modulo L in the domain Lambda/(L) proves that L is a nonzero divisor in R whenever f modulo L is nonzero. If the nonzero slope is on no exact boundary, this applies to all three factors, so P is regular. On one exact boundary, f=L S_eta(L), eta nonzero. The other factors are regular; cancellation in Lambda proves Ann_R(P)=Ann_R(L)=(S_eta(L)), whose augmentation is eta. The same argument covers unit eta, when this annihilator is the whole quotient. If alpha=beta=0, R=Lambda is a domain and P is again regular. No unique-factorization assertion or division by eta is used.

On the generator P modulo PJ, the actual multiplier contributes chi^2 and the substitution contributes chi^3. Thus the connecting compact character is chi^5, and its Cartier dual has character chi^-4. This is valid in the finite Z5/(eta) case as well. The order-four subgroup kills H0 and H1 of lambda. Splitting the dual four-term sequence into two short exact sequences therefore injects the entire restriction kernel into the Gamma invariants of the connecting dual. Those invariants have order at most5, since2 generates Z5 units and v5(2^4-1)=1. This bounds the complete kernel, not merely its five-torsion.

## Common primitive at all locally five-divisible vectors

When both local coefficients lie in5Z5, every local translation is the identity on the fixed degree-three mod-five module M. The exact local gauge therefore gives the entire untwisted I0 action there.

The explicit functional has coordinates (0,2,4,0,2,1,0,0,2,0) in the stated ten-monomial order. The retained Fox multiplier, beta coefficients and binomial substitutions all have five-adic-unit denominators at this degree. The symbolic relation is chi*m-rho^t*m=c*chi^2*epsilon00. This is exactly the Cartier coboundary equation: rho^t sends epsilon00 to chi^2 epsilon00, while the Cartier operator is chi*rho^(-t). The sign and the chi^2 factor are both correct. The residual identity holds for the full two-parameter operator family, so one functional works for the whole local decomposition group, not a different functional for each element.

The global class remains nonzero. Primitive raw kappa3 detects its restriction to the cyclotomic kernel, and lambda invariants vanish, making the map from H1(lambda[5]) to H1(lambda) injective. Actual coinduction and inflation preserve this nonzero class globally.

At all other primes, the already audited D80 finite-exception argument applies. M is unramified outside the finite residual inertia set even if the full coefficient module has infinite ramification. Existing Frobenius primitives persist after coefficient inclusion. At the finitely many exceptional primes, D43 plus finite Tate duality and the finite Mittag--Leffler comparison kills the local class at some finite stage. One maximum therefore gives a common finite coefficient module. There is no interchange of a direct limit with an infinite product. This proves the full finite-localization lower bound, which matches the at-most-five upper bound.

## Classification and explicit families

D80 handles every primitive local vector; the new argument handles the zero residual vector. The residual partition is correct: three boundary lines have twelve nonzero vectors, their complement has twelve vectors, and the origin is the thirteenth order-five case.

Global independence makes all of a,b,a-b primitive. D77's continuous decomposition therefore gives exactly the sum of their three local depths, with the countable compact product when one depth is infinite, and T_s=0. The finite factor in the zero local-vector case is retained rather than absorbed into that free compact product.

The coefficient lambda31 is a unit because31^4=21 modulo25 and4log6=20 modulo25. The support {7,31,43} realizes any prescribed local logarithm vector while the inertia vectors at7 and43 stay the standard basis. For A=5 and B=5(1+5^(n-3)), the depths are exactly (1,1,n-2), including n=3. Taking A=B=0 gives the asserted mixed finite/countably free compact group. These are actual finitely ramified coefficient modules, but the proof correctly makes no section-existence claim for arbitrary such completed Kummer pairs.

## Independent execution

The certificate was executed under a separate runpy module name without modifying owner outputs. Its entire serialized result matched the owner's JSON: ten symbolic monomial identities in F5[q,c]/(q^4-1), all twenty actual residual operator pairs, the complete25-vector partition, and thirty explicit mixed finite/free examples. Runtime1.492 seconds. Outputs are notes/pbc_D81_independent_rerun.json and notes/pbc_D81_independent_rerun.out.

No new external theorem is needed beyond the already opened and audited D78--D80 sources; the new connecting-module calculation is proved directly above and in the draft.


SHA256 notes/de_sha_all_unit_pairs_draft.tex: 189952de88af4900e47af4fcb2b38f3f91ef695e2001e415f8d6e4b5ab715962

SHA256 notes/de_sha_all_unit_pairs_certificate.py: 8b7367760f37e07a447a287049997427d8880c438bb1c701cf19ef7e9dfd6ce6

SHA256 notes/pbc_D81_independent_rerun.json: 702697eddbf7ac6e8f683a6f15f5a093fae643b79787386bf0e11d6bc36c534f
