# Independent FGH audit of D.81

Status: complete written proof, existing-source scope and independent exact-certificate PASS. I read all370 lines of the candidate and its complete certificate, after full independent audits of D78–D80. No canonical change or registration is made by this ledger.

## Nonprimitive and zero local translations

The global residual independence still supplies two actual inertia columns with unit determinant away from five. The local equality I5=H5 semidirect I0 uses the same proven κ(6) saturation and allows H5 to be a nonsaturated rank-one lattice or zero. When H5=5^e Z5×0 after an integral coordinate change, the finite-coset transversal times Z5 is compact and continuous. H is homeomorphic as an H5-space to H5 times that transversal. Function-valued cochains are genuinely coinduced: compactness makes the finite local partitions uniform. Thus the positive-degree contraction works without a saturated direct summand. The zero group case is immediate. Hochschild–Serre and finite affine Chebotarev give precisely the asserted upper bound for the actual inverse finite-localization kernel.

## Exact annihilators, including all boundary degeneracies

For L=u,v,w, reducing Lr=fh modulo L in the domain Λ/(L) proves that L is a nonzero divisor in R whenever f mod L is nonzero. This argument uses only cancellation in Λ and does not require R itself to be a domain. For a nonzero slope, at most one of the three boundary reductions can vanish. In that case f=L S_eta(L), and the two other factors remain nonzero divisors. Cancellation gives Ann_R(P)=Ann_R(L)=(S_eta(L)). Its augmentation is eta, so C=PR/PJ is Z5/(eta), with the correct zero case when eta is a unit. If no boundary equality holds, or if the slope vector is zero and R=Λ, P is a nonzero divisor and C is Z5. These cases exhaust the possibilities; no lost cyclotomic component or rational saturation occurs.

The primal four-term exact sequence is C→J/PJ→R/PR→R/J. Cartier duality is exact on these compact modules. On the generator P modulo PJ, the multiplier contributes χ² and substitution χ³, so the character is χ^5, including the finite eta-torsion case. Its Cartier dual has character χ^(−4). Since H0(Γ,λ)=H1(Γ,λ)=0, the WHOLE restriction kernel embeds into (C^D)^Γ, of order at most5. This bound is not merely an order-five torsion calculation. It remains valid for zero local vector and infinite-rank intermediate quotients.

## The single local primitive and finite coefficient uniformity

When both local coefficients are divisible by five, an integral local gauge makes every local translation exponent divisible by five. All such translations act trivially on the order-five cubic module. The asserted fixed functional therefore only has to be checked against the actual untwisted operator. I checked the conversion between the compact and Cartier actions: the identity χm−ρ^t m=cχ² ε00 is equivalent to (χρ^(−t)−1)m=c ε00 because ρ^t ε00=χ² ε00. The displayed beta coefficients are the exact D31/D39 two- and three-jets, and all relevant denominators are units at five. No higher arithmetic coefficient can enter this quotient.

The same primitive works for the entire local decomposition group at five, not just a selected element. Global nonvanishing is retained by full-translation coinduction and the primitive raw Soulé restriction. D80's finite residual-inertia exceptional set then supplies one common finite coefficient level for every place: the fixed cubic module handles all other primes, while local compact H1=0 and finite Tate duality supply a finite larger level at each exceptional prime. This proves the nonzero lower bound in the actual finite-localization direct limit. It does not interchange that limit with an infinite product.

The primitive local cases are exactly D80. Together these give the thirteen versus twelve residual-vector partition. Global residual independence makes all three global boundary classes primitive, hence T=0. D77 supplies the continuous compact product and the sum of the three actual local depths, with the zero-vector countable product interpreted correctly.

## Explicit examples and computation

The parameter construction at7,31,43 has actual standard inertia vectors at7 and43. The logarithm denominator λ31 is a unit because31^4≡21 modulo25 and4log6 has leading residue20. The chosen local vector (5,5(1+5^(n−3))) has depths (1,1,n−2), including n=3, so every finite free rank n≥3 occurs together with the finite order-five factor. Setting both target logarithms to zero gives the stated countable product. No section existence is inferred for these completed pairs.

I copied and independently ran the complete certificate as notes/fgh_D81_certificate.py/.json/.out. Exit0/PASS, and the entire JSON equals the author result. It checks the ten exact symbolic remainders, all20 residual actual operators, all25 slope vectors, and30 explicit finite-rank parameter checks. Independent JSON SHA-256: 702697eddbf7ac6e8f683a6f15f5a093fae643b79787386bf0e11d6bc36c534f. The coinduction and annihilator proof is not inferred from these finite computations.

## Source scope

The new argument is elementary integral algebra applied to the actual D35/D39 operator and the D77 primitive local element. The previous full D80 audit freshly opened Milne, Arithmetic Duality Theorems, I Corollary2.3, printed28, primary https://math.stanford.edu/~conrad/BSDseminar/refs/MilneADT.pdf (turn1048view1/turn1049view0). D81 uses precisely that finite local result through D80's explicit ML/dual-limit argument. D31/D39 and D77's raw normalization remain their already verified primary inputs. No new unverified arithmetic nonvanishing theorem is introduced. No correction needed.
