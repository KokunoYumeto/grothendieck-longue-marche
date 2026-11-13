# E.39: the exact arithmetic free-inertia comparison

The arithmetic Riemann-existence route was checked against Wingberg's original author PDF, Proposition 2.1 and Theorem 2.4. For K=Q(zeta3), S the prime above3, the theorem gives the continuous free pro3 product of the actual inertia groups over primes of K_S(3) outsideS as the exact kernel L of G_K(3) -> G_K,S(3). Every factor is Z3. The topology is retained: maps out of this product are continuous bundle maps, with finite support at each finite level.

The free rank2 quotient admits a split chosen by the two conjugate actual Frobenius lifts above7. The theorem then records the exact reconstruction of a section cocycle from a homomorphism lambda:L->W and a cocycle on the free quotient, including the required operator compatibility. It also records the actual descent to Q and the residual geometric conjugation action.

The key new finding is that this splitting does not erase local Frobenius correction words. Define h_q=F_q s(sigma_q)^-1. The local section equation contains lambda(h_q), multiplied with the unramified cocycle value. For every possible splitting, the claim that all h_q lie in their local inertia groups contradicts the cyclic cubic Kummer character of2 and abelian Chebotarev: its restriction along the splitting is unramified outside3 but cannot have the same Frobenius values as the character ramified at2.

For the chosen split, the difference is visible at a specific prime. At the two primes over7, the characters of2,zeta,lambda have values (2,2,0) and (1,2,2). Hence kappa2 composed with the splitting equals kappa(zeta*lambda) on the rank2 quotient. At the prime (-2+3*zeta) above19, their Frobenius values are1 and2. The correction h19 has kappa2 value2, while kappa2 is zero on local inertia at19. The supplied program verifies these finite residue computations exactly.

This is a proved comparison and a proved failure of a proposed simplification. It leaves a concrete further step: evaluate the correction words and their conjugation action in the images needed for each intrinsic metabelian or marked-depth section. The source theorem supplies the exact free kernel, and the section formula displays where those additional words occur. Neither the kernel theorem nor the two unramified action matrices alone evaluate them.

## Sources opened

- Kay Wingberg, *Riemann's existence theorem and the K(pi,1)-property of rings of integers*, author's December 2007 PDF, Proposition2.1 and its following remark, Theorem2.4 including its infinite-set clause.
- J.S. Milne, *Class Field Theory*, version4.03, V Theorem3.23, the exact abelian Chebotarev statement used in the character argument.
- Wingberg, *Free Product Decomposition of Galois Groups of Number Fields*, Publ. RIMS41(2005), introduction pp295–296, independently confirms the wild-set inertia theorem and its continuous-product interpretation.
- The author's NSW2.3.pdf link was attempted but redirected to the book landing page; it was not treated as an opened theorem. The redirected page is recorded as sources/nsw23_landing.html. The proof instead cites the directly opened Wingberg theorem.

## Deliverables

sections/E_riemann_coordinates.tex; ledger/e_riemann_results.json; ledger/e_riemann_refs.bib; code/e_riemann_correction.py/.out/.json. The program completed with PASS.
