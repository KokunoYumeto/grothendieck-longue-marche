# Functoriality and reconstruction: supplemental report

| Task contribution | Outcome of the full task | Statement | Exact contribution |
|---|---|---|---|
| A.a | Partly settled | B.15 | Full typed dictionary and formal construction for C3:570–572 and 691–696; later restricted-conjugator objects remain separately indexed by B.17–B.18. |
| A.b | Partly settled | B.15 | Symbolic universal matrix identities, exact finite quotient maps, all images and kernels, and finite tests of each mathematically distinct reading used here. |
| B.c | Partly settled | B.15 | Kernel-stabilizer criterion, all induced kernel formulas, corrected coefficient-subgroup version, and finite constant group-scheme fppf exactness. |
| B.g | Partly settled | B.15 | Every effective signed universal modular automorphism preserves the congruence kernel. Its full effective image and kernel remain precise separate questions, with an explicit target parameter whose lift this argument does not supply. |

## Proven mathematics

For a surjection q:C→C′ of marked profinite groups, the maximal coefficient subgroup admitting quotient automorphisms is D_q={d:u_d(kerq)=kerq}. Descent of every effective numerical solution is exactly the assertion D_q=D. The induced target is its actual closed image H, not the full target coefficient group by assumption. The proof includes the conjugacy version of loop preservation, continuity, uniqueness with both specified embeddings, and exact kernels.

With N=kerq, A_q=ker(D_q→H), and L_N=L0∩N, the kernel on gamma is A_q/j(L_N); the kernel on G is (N⋊A_q)/anti(L_N). The starred normalizer kernel is C_KG(x). A target normalizer element lifts exactly when the corresponding two conjugates are conjugate by KG. Fibre-product kernels are the stated fibre products over K_gamma; they are not replaced by unjustified direct products. Surjectivity of q does not force normalizer or fibre-product surjectivity.

The coefficient-subgroup variant of C3:571–572 keeps the full conjugating group C. For arbitrary D0 the correct loop subgroup is L(D0)=j^{-1}(D0), with gamma0=D0/j(L(D0)) and G0=CD0=(C⋊D0)/anti(L(D0)). It is a different construction from restricting the conjugating group to C^natural in §49.VI. B.17–B.18 handle that distinction.

The congruence descent proof is stronger than a conditional kernel-stability statement. Let C be the full profinite completion of SL2(Z), with the earlier matrices rho=[[0,1],[-1,1]] and sigma=[[0,-1],[1,0]]. The matrix images R,S of an effective automorphism have traces 1,0 and satisfy SR=U(-mu). Writing S11=a gives S21=mu^{-1} and S12=-mu(1+a²). Both R,S are conjugated by g=[[mu,a mu],[0,1]], so q∘u=Ad(g)∘q on the two topological generators, hence everywhere. The loop maps injectively to U(-Zhat); consequently K_gamma=A_q and K_G=N⋊A_q. Numerical parameters remain recorded throughout.

At the end of §49, the single-factor reconstruction is (P⋊T)/{(phi(j)^{-1},j):j∈J}, under the two stated inner-action and equivariance conditions. P embeds, the quotient is T/J, and the kernel of T is kerphi. For multiple factors with common kernel and quotient, the extra datum is a compatible transitive system of isomorphisms, equivalently a closed subgroup of their fibre product whose intersection with the kernel product is the diagonal and whose quotient map is onto. Agreement of the quotient and action alone is insufficient.

The effective-conjugator dictionary at565–569 is also made explicit: Gamma=L0\P_eff and S0M≅P_eff×C as parameter spaces, with f=d U^{-1} and inverse U=f^{-1}d. The right centralizer action is conjugated by t′. The literal t interpretation of scan569(83) fails in S4 because t does not preserve C_rho. These actions and inverse formulas are checked elementwise in both finite models.

## Executed computations

`code/AB_functoriality.py` is standalone. Its `.out` and `.json` files contain all results. Every assertion passed.

The S4→S3 map is its action on the three pair partitions. The kernel is V4; the distinguished loop intersects it in {1,(14)(23)}. All automorphisms are enumerated from the two generator images by complete Cayley-graph consistency. The code constructs both linked and independent signed groups with numerical group U12, forms the actual semidirect and antidiagonal quotients, checks every multiplication pair for D, gamma, G, and enumerates every element, image and fibre in the four larger fibre products.

| Object | B source | B target | Kernel | Z source | Z target | Kernel |
|---|---:|---:|---:|---:|---:|---:|
| D | 16 | 8 | 2 | 64 | 32 | 2 |
| gamma | 4 | 4 | 1 | 16 | 16 | 1 |
| G | 96 | 24 | 4 | 384 | 96 | 4 |
| N_rho* | 12 | 12 | 1 | 48 | 48 | 1 |
| N_sigma* | 16 | 8 | 2 | 64 | 32 | 2 |
| Gamma | 48 | 24 | 2 | 192 | 96 | 2 |
| M | 1152 | 144 | 8 | 4608 | 576 | 8 |
| S0Gamma | 192 | 48 | 4 | 768 | 192 | 4 |
| S0M | 4608 | 288 | 16 | 18432 | 1152 | 16 |

Every image is the complete target in this table. Taking D0=<t> gives order 2, L(D0)=1 and G0 of order 48. Its action is nontrivial. The code verifies that t′=sigma^{-1}t does not belong to D and does not normalize L0, so the literal t′ interpretation of the margin in scan571 is false in this example.

For the quotient SL2(F3)→A4, the code verifies the projective action identification and computes D→H as an isomorphism of order-24 groups with independent U12 numerics. The G kernel is the central pair ±I. The element j=[[1,1],[1,2]] anticommutes with sigma, while its image commutes with sigma′. Both possible lifts fail the starred-normalizer condition. The starred sigma groups both have order 32, but the image has order 16. This is a substantive finite example of the conjugator-lifting obstruction.

SymPy verifies the matrix conjugation identities over Z[a,mu,mu^{-1}]. Exhaustive finite trace-pair enumeration at n=2,3,4,5,8,9 gives 2,6,8,20,32,54 solutions, exactly n per unit multiplier. These are expressly trace-pair counts, not an assertion that all separate sign-conjugacy conditions hold in every ring.

For the final reconstruction, C4 and V4 both have kernel C2, quotient C2 and trivial action. The program reconstructs each and enumerates all candidate subgroups of order four in the order-eight fibre products. Two copies of C4 have two diagonal gluing subgroups; C4 and V4 have none. This verifies the corrected extra-data requirement of scans695–696.

## Exact remaining congruence assertion

The full effective image H_q⊂D(SL2(Zhat)) and A_q=ker(D(C)→D(SL2(Zhat))) are not determined by the theorem. We fix one explicit target parameter: mu_5=2 and mu_p=1 for every p≠5, with automorphism Ad diag(mu,1) and both signs +1. It satisfies the target loop and conjugacy conditions. At 5, choosing i²=-1, i≡2 mod5, the rho centralizer element (i−1)I+2rho and sigma centralizer element I+sigma both have determinant 2. Dividing diag(2,1) by them produces determinant-one conjugators. Their reductions [[3,3],[1,3]] and [[1,1],[2,3]] are verified by the code.

The exact remaining question for this parameter is whether an automorphism u of the full profinite modular group, with the prescribed loop exponent and generator conjugacy classes, satisfies q u=Ad diag(mu,1) q. This is (B.15.16). The individual norm and matrix conditions do not construct compatible lifts through every finite quotient. We do not assert that this question is open in the literature or that the chosen unit is least in any ordering. The finite quotient maps above give a nontrivial proved and executed case of the same descent/lifting mechanism. Other remaining assertions are source-indexed separately: universal numerical realization B.8.5; named geometric image B.16; restricted-conjugator comparisons B.18; and the three arithmetic comparisons D.7.

## Sources and final §49 audit

The supplied checked transcriptions of C3:565–572 and 691–696 were read in full. Their photographs are not among the attached scan files, so this supplement makes no paleographic claim. The readings register identifies every mathematically used alternative and distinguishes the abandoned block at572 from standing assertions. No external theorem or priority claim is used.

The audit also read the later source blocks, without identifying them with the new functoriality theorem. C3:573–576 and647 contain the named geometric-extension comparison, now assigned to B.16. C3:651–653 introduces a chosen open normal conjugating subgroup and an additional quotient-action condition, unlike merely restricting D0. C3:658–660 then has a separate quotient-domain defect, treated in B.17. C3:663–665 contains the revised automorphism kernel and normalizer groups. C3:682–686 contains the proposed G^natural≅M^natural identification;689–690 leaves the image of the smaller M^{natural,?}→M^natural unresolved and expressly says verifications were avoided. These exact residual families are assigned to B.18. No statement that all remaining manuscript questions reduce to B.8.5 survives this audit.
