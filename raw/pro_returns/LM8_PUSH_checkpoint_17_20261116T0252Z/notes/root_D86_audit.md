# Root full proof and exact certificate audit of the dependent cusp family

**Verdict: PASS for the stated D86 candidate.** The candidate remains notes-only during the checkpoint14 source freeze. This audit does not authorize a change to the frozen paper before the scheduled save. It asserts no general dependent-pair classification and no equality between every operator-image restriction-kernel class and finite-level Sha.

Root read all479 lines of notes/de_sha_cusp_infinite_torsion_draft.tex, SHA-256 `dd6f314fe25fa126a3635099dcca302277050fb2398107d912a03f0b813882de`, and the complete certificate source. The independent run reproduced the entire author JSON byte for byte. The source hash is `d0e082fc0e749e6fafef592e5d1a645c001a30378012a36b180be71f61da0fe9`; the identical result hash is `3aeb3b16c72728a5116c8881e05435bcdf7bf7f048f98c14961ba99b066cd6c1`. The independent result and execution ledger are notes/root_D86_certificate_rerun.json/.out and notes/root_D86_certificate_verification.json.

## 1. Scope, topology and actual images

The pair is exactly(a,0), with primitive away-five valuation image, zero five-valuation, arbitrary c0 support, and local logarithmic coefficient of valuation one. The actual untwisted operator image and its local surjectivity are the previously proved D77–D78 inputs. Translation inertia gives H=Z5 globally; the saturated local coefficient gives5H locally. The common local gauge preserves the global H, so the comparison is between the actual subgroups H semidirect I0 and5H semidirect I0. This is not a freely assigned formal action.

The coinduction comparison of D81/D84 has the correct direction: global H invariants in the discrete dual correspond to B=Lambda/(u), and local5H invariants to R=Lambda/((1+u)^5-1). Restriction is induced by B-dual into R-dual. Its whole kernel is the connecting quotient of J-dual invariants, J=uR, by the image of R-dual invariants. The previously audited finite affine Chebotarev descent gives an injection of the finite-level localization kernel into this quotient. That injection supplies an upper bound only; the later explicit global cocycles are needed for the lower bound.

## 2. The actual ideal and its infinite torsion layer

Cancellation in Lambda identifies J, through multiplication by its actual generatoru, with A=Lambda/(S5(u))=Z5[zeta5][[v]]. The polynomial S5 is Eisenstein, so A is a domain and u is a uniformizer in its coefficient ring. The primitive actual local cubic multiplier kills precisely PJ after coinvariants by the cyclotomic kernel. Thus the connecting compact module is T=J/PJ, with exactly one Cartier untwist.

In scalar coordinates T=A/(uvw), but retaining the actualu factor is essential. The submodule E=vwA/(uvwA) is F5[[v]] by cancellation of vw, and its actual generator is P=uvw. The quotient is Q=A/(vw). Modulo v, w becomes the nonzero divisoru, so(v) intersect(w)=(vw). This gives the exact two-boundary sequence with cokernelF5. Q is torsion-free of Z5-rank eight.

The actual Alexander multiplier, substitution on P, and one Cartier untwist give the scalar factor gamma-bar times S_gamma(1+v)^3 on E. Multiplication byv^3 embeds this as the idealv^3 of the chi-bar weighted completed group ring. The three omitted jets have the nontrivial tame weights1,2,3. Averaging over the order-four subgroup therefore removes them exactly. Continuous invariant dual functions are independently prescribed on each nonzero five-adic valuation shell, with only finitely many nonzero shells by continuity at zero. This proves E-coinvariants are the compact product of countably manyF5; it is not a sample-based inference.

## 3. Integral boundaries, the snake map and the full restriction-kernel exponent

On the two boundary modules, the actual multipliers after untwisting are S_gamma squared and S_gamma squared times t^((1-gamma)/2). Multiplication byu^2, together with the integral half gauge on the second boundary, embeds each into the augmentation-square module ofZ5[C5] with its genuine permutation action. The finite cokernel has tame weight two, so its invariants and coinvariants vanish. The quotient Q therefore has coinvariantsZ5 squared and action through the order-four group.

Two topologically generates Z5-units: its reduction has order four and2^4-1 has five-valuation one. The snake lemma for its operator minus one retains a possible kernel from Q invariants into E coinvariants. That image is finite because its source is finitely generated overZ5 and its target has exponent five. Dividing a countably infinite productF5 by a finite subgroup leaves the same compact product type. Lifting twoZ5 basis vectors continuously splits the free quotient. This proves T-coinvariants are productF5 timesZ5 squared without falsely asserting injection of E-coinvariants.

The natural invariant-factor statement of D77, freshly reread at its exact comparison-map scope, supplies two additional local divisible factors and the unchanged zero-boundary factor. Hence R-dual invariants modulo B-dual invariants inject as two copies ofQ5/Z5. Their image fills the maximal divisible subgroup of the connecting module: duality gives a surjection fromZ5 squared to itself, which is an isomorphism. The entire restriction kernel is consequently a countable direct sumF5. This establishes both its exponent and the countable-dimensional upper bound.

## 4. Infinitely many genuine global classes

The actual quotient J/uJ has, after the same Cartier untwist, action gamma-bar times S_gamma. Multiplication byv identifies it with the chi-bar weighted group-ring ideal; the omitted constant has nontrivial tame weight. The same shell calculation gives an infinite-dimensional invariant dual. Its intersection with the preceding divisible image hasF5 dimension at most two, so its connecting image remains infinite-dimensional.

The concrete extension is the coefficient-of-u functional in R/5R=F5[[u,v]]/(u^5). It restricts to the chosen functional on J, has finite v support, and has order five. Its I0 coboundary lies in B-dual. Inflating that cocycle to H semidirect I0 is legitimate because H fixes B-dual, and inflation to the actual Galois group is injective in degree one. The resulting classes are continuous global classes, not merely formal connecting symbols.

## 5. The uniform cyclic primitive is the decisive finite-level comparison

For a chosen class, take n large enough to contain the functional and all cocycle values in the dual of Lambda/(5,(u,v)^n). A single next level works for every unramified Frobenius.

If the translation h is divisible by five, multiplication by(1+u)^h has no u terms of degrees one through four modulo five; the first-u functional is fixed, and itself supplies a primitive. If chi-1 is a unit, actual integral translation conjugation removes h; the cocycle vanishes on H and its values are H-fixed, so transporting the I0 primitive gives a primitive in the same finite module.

In the remaining case, chi is one modulo five and h is a unit. On the full compact coefficient ring modulo five, the one-time Cartier-untwisted operator minus one raises augmentation degree and has leading symbol h-bar timesu. Substitution differs from the identity only at degree at least five; the Fox factors and beta contribute no linear term. Multiplication by h-bar timesu is injective on every homogeneous polynomial piece. This proves the map from truncationn to truncationn+1 is injective, including its well-definedness on the quotient. The actual dual operator differs from the transpose by an invertible inverse-action factor, so its map from M_(n+1) to M_n is surjective. The certificate explicitly checks the stated leading symbol and rank in540 exact finite tests, but the proof holds for everyn and every actual element by the universal leading-symbol argument.

## 6. One coefficient level at every place

Choose b with5^b at leastn+1. The c0 condition makes the primes whose inertia coefficient is not divisible by5^b finite. At every other prime except five, the chosen finite module and the cocycle are unramified. The preceding common cyclic bound therefore trivializes every such local restriction at once. At five, the whole5H subgroup fixes the first-u functional, so it is already a primitive on the entire actual local image.

At each exceptional prime, inertia is nonzero. Root reread D80's precise passage from compact localH1 vanishing to the discrete Cartier dual: finite local Tate duality and the Mittag–Leffler finite tower identify the direct-limit dualH1 with the dual of the zero inverse limit. This is used only for finitely many exceptions; each primitive fits a finite module, and their maximum fits one common level. Earlier primitives remain valid after inclusion, even if the larger module has extra ramification. Real-place cohomology is zero at five. Thus the classes belong to the actual finite-level localization kernel before the filtered union is taken. There is no exchange of a filtered union with an infinite product of local cohomology groups.

The infinite lower bound and countable exponent-five upper bound prove the abstract direct-sumF5 dual, hence the stated compact productF5. The proof does not need to show that the entire operator-image restriction kernel equals the finite-level localization kernel.

## 7. Remaining factors, the example and limits

D77's natural map is identity on the zero-parameter countable product and has two new local depth-one factors. Its continuous splitting gives K as the compact productF5 timesZ5 squared. This is a statement about the separated compact second-cohomology obstruction, not torsion in the first-cohomology fibre or a splitting of the unrestricted nonseparated quotient.

The cusp pair(a,0) has an actual inertia section. For a=kappa(26), the coefficients at2 and13 are primitive, five-valuation is zero, and26=1+25 gives logarithmic valuation two versus valuation one forlog6. Thus the required local depth is one. D74 applies to this finitely ramified example and gives its metabelian fibre as a torsor under the stated countable productZ5. No assertion that all classes in that fibre are cuspidal is made.

The new proof uses the exact previously audited primary-source inputs through D35/D39, D43, D63, D74, D77–D78 and D80–D84. No new external theorem is introduced under an unverified name. All infinite-dimensional conclusions are structural; the executable output supports the finite formulas and example only. The full general dependent-pair and higher-derived questions remain unresolved.
