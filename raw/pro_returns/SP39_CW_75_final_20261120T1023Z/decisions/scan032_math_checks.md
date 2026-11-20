# Scan 032: concrete maps and actual check scope

Source claims: the two displayed chains on scan 032. Note identifiers N032.3 and N032.4. Root, GPT-6 Astra Pro; effort not exposed. Computation UTC is stored in `scan032_projective_check.json`. No external source was consulted.

## N032.3: explicit finite permutation maps

The implementation is `scripts/check_projective_links.py`. F₄ is the quotient F₂[a]/(a²+a+1), encoded as 0,1,a,a+1 ↔ 0,1,2,3. Addition is bitwise polynomial addition and multiplication reduces by a²+a+1. F₅ uses residues 0 through 4. Matrices are row-major tuples (a,b,c,d). Projective representatives have their first nonzero entry scaled to 1.

The action P(M) is the action of M on one-dimensional column-vector subspaces: the affine point t is represented by (t,1), and infinity by (1,0). Thus the finite affine output has value (at+b)/(ct+d), with a zero second coordinate recorded as infinity. This definition determines every value, including the point at infinity. Composition follows the column-vector multiplication order P(MN)=P(M)P(N).

For F₄ the projective-point order is (∞,0,1,a,a+1). Enumeration gives 60 determinant-one matrices, 60 normalized projective matrices and exactly 60 distinct actions. The set of actions equals the full set of even permutations on the five ordered points. All 3,600 pairs of determinant-one matrices were multiplied and their actions compared entrywise to permutation composition. The exact map SL₂(F₄) → A₅ is M ↦ P(M). The JSON contains every matrix and its image, both in image-list and cycle notation. Equality of these two finite sets and injectivity establish bijectivity; the product checks establish the homomorphism directly.

For F₅ the projective-point order is (∞,0,1,2,3,4). Enumeration gives 120 normalized projective matrices and 120 distinct actions. All 14,400 projective matrix products were checked against the action composition. To map this concrete group to S₅, the program lists the six cyclic order-five subgroups H₀,…,H₅ of S₅ in lexicographic order of their sorted permutation tuples. The exact subgroup entries are in `six_subgroups` in the JSON. The permutation ρ(g) sends Hᵢ to gHᵢg⁻¹. Its 120 images are distinct, and all 14,400 products in this conjugation action were checked.

The explicit relabelling from subgroup indices to projective-point indices is u=(0,1,2,5,3,4), with zero-based image-list entries. Exhaustive set equality gives uρ(S₅)u⁻¹=P(PGL₂(F₅)). Consequently the concrete map used in the check is

φ([M]) = ρ⁻¹(u⁻¹P(M)u).

Every one of its 120 matrix-to-S₅ values is in the JSON. The program checks that these values exhaust S₅ and that φ([MN])=φ([M])φ([N]) for all 14,400 pairs. The faithful action, exact relabelling and inverse lookup give a fully specified bijective morphism, rather than an inference from equal group orders.

These are finite Python computations with reproducible tables. No proof-assistant certificate was produced.

## N032.4: exact map between the two F₄ matrix groups

The three nonzero field elements have cubes 1: a²=a+1 and a³=1; (a+1)²=a and (a+1)³=1. Define θ([M])=det(M)M. Scalar replacement M↦sM gives det(sM)sM=s³det(M)M=det(M)M. Thus θ is explicitly invariant on every projective class. Its determinant is det(M)³=1. Multiplication gives θ([M])θ([N])=det(M)det(N)MN=θ([MN]). Projectivization M↦[M] reverses this map in both orders: determinant-one representatives are fixed by θ, and θ([M]) belongs to the original scalar class. This verifies the inverse and the group morphism, using the stated field arithmetic.

## Scope retained in the notes

The transcription continues to print Sl and GP in the source's own case, dimensions and spacing. The concrete SL₂/PGL₂ models above are the objects checked in the notes. The SO(3,F₄) and SO(3,F₅) links and the icosahedral geometric/combinatorial dictionaries were not checked. The mathematics does not select between frak A and cal A in the handwritten capital. No mathematical repair was inserted into the page.
