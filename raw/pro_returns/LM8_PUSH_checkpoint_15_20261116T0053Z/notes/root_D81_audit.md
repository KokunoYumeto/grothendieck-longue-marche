# Root full audit of D.81

Status: complete written-proof PASS, with the independent exact certificate and the additional ten explicit residual factorizations recorded in `root_D81_rerun_verification.json`. The candidate remains a draft until its owner incorporates the audited text. This audit reads all 370 lines, including the nonsaturated and zero local cases, and does not infer the continuous cohomology from finite computations.

## Actual global and local images

The global residual independence away from five is exactly the hypothesis used in D.80 to produce two actual pure inertia translations with a unit determinant. Thus the global image is the full translation semidirect product. The local unit assumption permits an integral monomial gauge, after which D.78's surjectivity and saturated kappa(6) on the kernel give the stated local image even when its translation lattice is not saturated or is zero. Correcting an arbitrary lift by an element of that kernel supplies the actual zero-translation complement.

For a nonzero nonsaturated line, the integral coordinate change and the finite-residue-times-Z5 transversal identify the whole compact translation space with the subgroup times a compact transversal. Continuous functions into a discrete torsion module admit uniform finite partitions on this compact product. Consequently the usual coinduced contraction applies with the transversal as a coefficient variable. No nonexistent direct summand is used. The trivial subgroup case is immediate. These facts justify both Hochschild--Serre identifications and their actual restriction map. The finite affine Chebotarev injection is used before its direct limit, exactly as in the already audited D.78 and D.80.

## Whole connecting kernel and exact boundary algebra

For each boundary prime L, reduction of Lr=fh in the domain Lambda/(L), followed by cancellation in Lambda, proves L regular in R whenever f modulo L is nonzero. For a nonzero slope at most one boundary equality occurs. In its exceptional case f=L S_eta(L); cancellation gives Ann_R(L)=(S_eta), while the other two factors remain regular. This proves the stated Ann_R(P) without assuming R is a domain and without replacing an integral quotient by its rational saturation. The zero slope leaves R=Lambda and P regular. Augmenting S_eta gives precisely eta, including the unit case.

The four-term compact sequence is exact: the kernel of J/PJ to R/PR is PR/PJ, and the remaining quotient is R/J. Multiplication by P identifies its first term with R/(J+Ann_R(P)). The constant multiplier chi^2 and substitution factor chi^3 give the actual character chi^5 on this cyclic term, and Cartier duality gives chi^(-4). The nontrivial order-four character on lambda makes H0 and H1 of Gamma vanish. The resulting quotient of invariant modules embeds into the invariants of C dual. This bounds the entire restriction kernel, not just its order-five torsion. The invariant group has order at most five since v5(2^4-1)=1.

## Nonzero lower bound at a locally divisible vector

All local translations act trivially on the order-five cubic quotient when both local unit coefficients are divisible by five. I checked the exact monomial order and the fixed functional against the actual D.31/D.39 multiplier. Multiplying the Cartier equation by rho transpose correctly gives chi m-rho transpose m=c chi^2 epsilon00, since rho transpose epsilon00=chi^2 epsilon00. The author certificate is independently rerun in a separate root copy and its whole JSON compared, and an additional symbolic check verifies the displayed ten residuals before imposing chi^4=1.

The raw weight-three restriction proves global nonvanishing; injection from lambda[5] to lambda follows from the vanishing of lambda invariants. At five the same cubic primitive handles the whole decomposition group. Away from five the finite residual-inertia exceptional set is genuinely finite because the completed valuation coordinates tend to zero. The already verified D.43 local vanishing and finite local Tate duality give one finite killing level at each exceptional prime. Taking their finite maximum with the cubic level preserves all previous primitives and produces a single global finite module. There is no interchange of a direct limit with an infinite product of local groups.

## Classification and examples

D.80 supplies every primitive residual vector; the new lower bound supplies the zero vector. The resulting partition has thirteen vectors with an order-five factor and twelve with none. Global independence makes all three boundary classes primitive, so D.77 gives T=0 and the claimed continuous, noncanonical compact product. The local valuation sum includes every exact zero as infinity.

For the explicit family, the actual inertia columns at 7 and 43 are the standard basis, irrespective of the coefficient at 31. The computation 31^4=21 modulo 25 makes lambda31 a unit of residue one. Thus every prescribed local pair is attained by the displayed finite-support completed Kummer classes. The vector (5,5(1+5^(n-3))) has depths (1,1,n-2), including n=3; the zero vector gives the countable product. These are statements about actual Alexander modules. The text correctly does not infer the existence of sections above arbitrary chosen abelian parameters.

## Sources and scope

The new connecting-module computation and finite symbolic identities are proved in the text. Their arithmetic inputs are the already fully checked D.31/D.39 operator, D.77 local primitive, and D.78/D.80 actual-image and finite-level arguments. The root D.80 audit freshly opened Milne, *Arithmetic Duality Theorems*, I Corollary 2.3, printed page 28, at https://www.jmilne.org/math/Books/ADTnot.pdf (root retrieval turn1041view0). D.81 uses precisely this finite duality through D.80's explicit Mittag--Leffler comparison. No new external arithmetic theorem is silently introduced.

No correction to the full written argument is needed. The general valuation-at-five case, globally dependent residual pairs, nonseparated kernels, unrestricted first-cohomology ranks with infinite ramification, and section-existence questions remain separate.
