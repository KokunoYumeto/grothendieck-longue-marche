# Active Part A proof routes after checkpoint 03

## 1. The remaining third-derived peripheral kernel after A.67

Let M=S2, L=F''/F''', and Lambda=Zhat[[M]]. The new equality H^1(M,L)=0 means that an outer automorphism of S3 inducing the identity on M is uniquely determined by its Lambda-linear action T on L. Indeed, two such automorphisms with the same T differ by an L-valued continuous crossed homomorphism on M; A.67 makes that difference inner by L. This is an actual injective map from the outer kernel to Aut_Lambda(L), not merely an analogy with a module problem.

The exact remaining conditions can be recorded in relative extension language. The extension 1→L→S3→M→1 comes with its actual splittings on the three primitive procyclic subgroups <x>, <y>, <xy>. Their metabelian centralizers are those same procyclic groups. Thus any peripheral conjugator for an automorphism inducing identity on M can be adjusted by the corresponding primitive lift to lie in L. Its existence is therefore exactly preservation of the relative extension class by T. Arithmetic outer commutation is exactly commutation of T with the genuine semilinear Galois action: the difference then acts identically on M and L and is inner by A.67. This gives a prospective explicit module-stabilizer presentation of the remaining kernel; it does not compute that stabilizer.

A fully written relative-cohomology version still needs to specify the mapping-cone convention and the actual continuous section used to represent the extension. An elementary alternative is the already derived normalized formula: after fixing x, write alpha(y)=d y d^{-1}, d∈L. The third cusp requires (1−xy)e=x(1−y)d. Its action on L is l→l+pi_2(l)(1−y)d. Invertibility is equivalent to 1+(1−y)pi_2(d) being a unit in Lambda (rank-one matrix inverse). The genuine tangential arithmetic action supplies the additional linear equations recorded in the audit. No nonzero solution or vanishing theorem is presently proved.

## 2. Why the finite quaternion compact block has not lifted

The finite Q8 quotient has a positive-genus compact homology block on which x−1, y−1 and xy−1 are invertible. The sign Haar projector e used in A.59 does not impose those finite relations on the full completed group ring. It kills only the appropriate normal prime-to-ell part of M'; its pro-ell part survives. In particular e·c is −c_ell rather than −1, and x²,y² do not become central. Imposing their finite character values before controlling that surviving part changes the module.

A finite central idempotent need not lift centrally through a pro-ell extension: modular blocks can fuse. Noncentral idempotent lifting does not by itself give an arithmetic-equivariant endomorphism of the relative relation module satisfying all three cusp equations. The candidate proof route is to show that deeper covers and their actual arithmetic action couple the compact block to the boundary, preventing a bounded integral projector. Weight separation over Q_ell at an individual finite cover does not prove this: denominators may grow in the cover tower. No assertion of such a coupling theorem is made.

## 3. Higher class-preserving rigidity

The direct H^1(P,Zhat[[P]])=0 proof extends to a group with a normal abelian subgroup containing a closed Zhat². For higher free derived quotients this addresses the cocycle part. The missing step in iterating A.67 is a relation-module vector with a Fox coordinate having zero left annihilator modulo every coefficient prime. The pattern r=[u,xux^{-1}] repeats the factorization A(u−1)=(u−1)(u^x−1)(x−1), but also needs delta_y(u) regular in the larger completed group ring. Its regularity after projection to a smaller derived quotient does not prove that lift: prime-to-ell Haar summands obstruct augmentation-separatedness. F independently identified this exact same gap.

The primary Romanovskii1997 Theorem1 proves the pro-p analogue for every derived length at least three. Its exact theorem and proof were opened. It is not being transferred to the full profinite quotient.

## 4. The remaining arithmetic normalizer extension

A.62 gives N0=P⋊B, geometric kernel P×C, and 1→C→B→G_L→1 with C pro-prime-to-ell. The quotient N0/C really has a section. A.61 and A.65 show that a noncuspidal example would require the remaining extension to fail every virtual section. A.63 proves that this failure is possible for abstract number-field extensions with a pro-prime-to-ell kernel. Therefore a further proof must use the actual embedding B⊂E_U and its geometric centralizer relation with P. No argument using prime support or absolute-Galois cohomological dimension alone presently supplies the lift.
