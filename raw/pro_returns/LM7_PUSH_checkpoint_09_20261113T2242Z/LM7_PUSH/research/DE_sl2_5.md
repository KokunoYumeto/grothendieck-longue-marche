# Exact SL2(F5) Ferrari comparison

## Universal free quotient — proved before the correction calculation

Let E=SL2(F5), Z={±I}, and E/Z=A5. The actual 120 matrix elements, multiplication, inversion, center, and perfectness of E are checked in `de_ferrari_sl2_5_model.py`. The quotient is identified with the previous A5 model by its conjugation action on the five Sylow-2 subgroups of PSL2(F5). Every PGL2(F5) conjugation is retained, with the precise corresponding permutation in S5. These 120 automorphisms are all of Aut(E): every automorphism descends to A5; an automorphism inducing identity there has the form g↦g·χ(g), with χ:E→Z a homomorphism, hence is identity because E is perfect. The PGL2(F5) matrices realize every automorphism of A5, so they realize all automorphisms of E uniquely.

The previous 19 epimorphism kernels F2→A5 have 4 generating-pair lifts each to E, differing by the two choices of signs of the free generators. Every such lift generates E: its image H satisfies HZ=E, and E perfect gives E=[HZ,HZ]=[H,H]⊂H. Two of the four choices cannot have equal kernels, because an automorphism identifying them would induce identity on A5 and therefore be identity on E. Conversely, any epimorphism to E reduces to one of the 19 A5 kernels. Thus there are exactly 76 epimorphism kernels.

Choose one lift (g_j,h_j) for each of the 19 A5 kernels. The combined image of F2 in E^19 is the full product: its projection to A5^19 is onto by E.29, so H Z^19=E^19, and the same perfectness argument gives H=E^19. Add the free abelianization modulo 2, F2→C2². Its joint image with E^19 is the full direct product K=E^19×C2², since a common quotient of a perfect group and an abelian group is trivial. The remaining 57 E evaluations are recovered by

    theta_(j,e1,e2)(w) = (−I)^(e1*ab_x(w)+e2*ab_y(w)) theta_j(w).

This gives a homomorphism K→E^76 that is injective: the chosen 19 evaluations recover E^19, and ratios with the sign-twisted evaluations recover both global parity coordinates. Its image is precisely the joint evaluation image of F2. This proves the exact universal comparison K≅im(F2→E^76), and not merely a surjection onto the individual factors.

## Exact Nielsen action and the finite base

An automorphism is represented by (p,c,D,M), where p permutes the 19 factors, c_j∈PGL2(F5), D is a19×2 matrix over F2, and M∈GL2(F2). Its action on K is

    (g,t) ↦ ((−I)^(D_j t) c_j g_(p(j)) c_j^−1, M t).

For the literal Nielsen substitutions a:(x,y)↦(x,yx) and b:(x,y)↦(xy^−1,y), p and c are those in the A5 model. The two generator images determine each of the 38 signs uniquely. The global matrices are [[1,1],[0,1]] and [[1,0],[1,1]] modulo2. Composition is exactly

    p_new = q∘p,
    c_new,j = c_j d_(p(j)),
    D_new = D N + F∘p,
    M_new = M N.

An element of K⋊Aut(K) is (k,t;p,c,D,M). Its new free coordinate after multiplication with (l,u;q,d,F,N) is k_j (−I)^(D_j u) c_j l_(p(j)) c_j^−1; its global coordinate is t+M u. All multiplication and inverse formulas are implemented directly using the actual SL2 and PGL2 tables. All literal Ferrari identities and braid relations hold exactly.

The projection to the old A5 Ferrari target sends k to its PSL2 image and forgets D,M,t. The other projection is the actual affine action (M,t) on C2², namely S4=AGL2(F2). The binary degree-two Ferrari model verifies this map on the actual generators and every six-pair evaluation. The joint image of B4 in T_A×S4 is exactly T_A×_(C2)S4: the maximal solvable quotient of T_A is C2 by E.29, both factors have the same braid parity, and Goursat's lemma determines the actual joint image. Thus this is the proved base of the double-cover Ferrari target.

An element above identity in this base has p=1, c_j=1, M=I, t=0, and k_j∈{±I}; D is unrestricted. Its exact multiplication adds the 19 central free signs and the38 cross-term signs. Hence the actual kernel is an F2-subspace of an explicitly identified57-dimensional elementary abelian group. The script checks every product of the57 ambient basis elements and their conjugates by the braid generators and inverses. It does not claim that all57 directions occur in the actual braid image.

The model verifies both projection maps on1000 successive literal braid words and every one of the76 free evaluations on100 literal free words. The proof above establishes the all-word statements; those executed checks are additional independent controls. The source correction calculation below retains the complete elementary kernel; no central lifting conclusion is drawn merely from the corresponding A5 result.

## Completed exact image stages

The complete lifted Schreier–Sims algorithm in `de_lifted_schreier_kernel.py` retains all stabilizer-chain Schreier relations and closes their actual elementary-kernel values under the original generators. Its source-word DAG is independently replayed. `de_ferrari_sl2_5_nielsen.py` evaluated11989 relators and obtained a36-dimensional cross-term kernel. Together with the19 central free signs, the actual four-strand kernel over T_A×_(C2)S4 has dimension55. The four-strand order is5690374860680314949416693111761942757307842560000000000000000000000000000000. Runtime7.910s.

`de_ferrari_sl2_5_source.py` computes the complete36-coordinate induced source. Its affine component has order6, entirely the existing outer B/F permutation; all pure evaluation pairs have trivial affine S4 image. The faithful base is therefore exactly the old A5 source. All25965 lifted Schreier relations give a44-dimensional elementary kernel. Source order287196033979968407657248500744192000000000000000000000; total runtime165.948s.

`de_ferrari_sl2_5_N.py` retains all97 literal N generators: the six old base generators and the91 differences from their complete lifted base presentation. All24623 relations give a41-dimensional kernel over the old N image. Its actual order is498604225659667374404945313792000000000000000000000; total runtime168.510s. Its index in the new source is576. Since the original discrete N also has index576 and is contained in the preimage of this image, the preimage is exactly N. This proves the actual modular quotient G_new/im(N)≅SL2(Z/12)/±1 through the specified B matrices.

The complete derived calculation in `de_ferrari_sl2_5_derived.py` has finished. Nprime and Nprimeprime both have41 kernel directions, so C=im(Nprime) is perfect. The Fprime image has42 directions and E/C has order8. The complete lifted relation counts are20880,21640,18600 respectively, with stage runtimes120.787s,141.927s,68.940s. The total1186.028s includes the slower search for base-derived generating sets. All word DAGs were independently replayed and all saved kernel spans compared exactly. The source/C order is43200, P/C has order75, and source/P has order576.

The maximal solvable four-strand quotient has finished in `de_ferrari_sl2_5_solvable.py`. First quotient by the explicitly perfect normal subgroup SL2(F5)^19. The remaining group C2² semidirect Nielsen is represented faithfully on251 points; its derived indices are1,2,6,96,96. The last equality proves that the terminal subgroup is perfect. Its inverse image in the Ferrari target is perfect as an extension of that perfect subgroup by SL2(F5)^19. The resulting maximal solvable quotient therefore has order96. Its entire right Cayley table and literal B4 representative words are saved. An independent exhaustive traversal of all1536 elements of the actual binary degree-two Ferrari quotient, checking all three outgoing generator edges at each element, proves the exact quotient homomorphism T_(2,2)→S96 with the specified braid-generator values. This is a factorization assertion through the actual maps, not an identification based on orders alone. Runtime43.521s.

The additional small exhaustive controls in `de_lifted_schreier_control.py` compare the lifted algorithm with all elements of A4 and of the order-eight Heisenberg group over F2. The first retains an extra lift and needs one new normal-conjugation direction; the second retains a nontrivial presentation relator. In both cases the entire kernel sets agree, and every saved relator DAG is replayed. Runtime0.008s.

## Exact modular arithmetic control

Using x=[[1,2],[0,1]] and y=[[1,0],[-2,1]] in SL2(Z/12), the subgroup they generate has order96 and its derived subgroup has order8. Every matrix in the derived subgroup reduces to I modulo4. Thus its image in SL2(Z/12)/±1 has a unique representative which is I modulo4, and reduction of that representative modulo3 identifies it with the quaternion subgroup of SL2(F3).

The24 retained E.17 literal commutator words have exactly the following three SL2(Z/12) values:

    kappa=0: [[1,0],[0,1]]
    kappa=1: [[1,4],[4,5]]
    kappa=2: [[1,8],[8,5]].

The complete index table is the same as E.29.13. These matrices are exactly [[1,−8kappa],[−8kappa,1+64kappa²]] modulo12, including the sign; they are not merely the same PSL2(F3) values. The actual source quotient Q and the upcoming complete Fprime/Nprime order comparison supply the needed map from the full source correction problem.

The signed comparison is now saved and executed in `de_ferrari_sl2_5_modular.py`. It also evaluates all24 old correction words, all6 ternary basis words, and all7 binary basis words in the literal family reconstruction formula. They are all killed in Q. Checking the exact base expression with its integral cusp gauge proves that all864 parameter points have the indexed Q value. An independent group-theoretic upper bound agrees with the Fprime calculation: the equality of the P and C projection kernels gives pi^−1(C_A)∩P=C; since E_A∩P_A=C_A, one gets E∩P=C. Therefore the actual modular map identifies E/C with Q8, without relying on a predicted kernel dimension.

## Complete E.38 correction and generation conclusion

The formal result is `sections/E_ferrari_sl2_5_agent.tex`. Fix any compatible profinite unit lambda≡1 mod72 and its E.24 branch modulo144. The cyclotomic character is onto; its kernel maps onto the Kummer C3 for2 because Q(zeta3,cuberoot2) meets the full cyclotomic field in Q(zeta3). Thus an actual Galois sigma with chi=lambda can have whichever kappa2 mod3 occurs in the retained word. NS Theorem2.5 gives its exact signed Q matrix, since lambda≡1 mod12. The difference of its full36-coordinate source image from the retained word lies in the perfect group C. Its joint image with the solvable old Nprime image is a product, giving a discrete Nprime correction which preserves the entire old point and matches all new evaluations. This retains every one of the864 points; it does not select just one point in a correction fibre.

The multiplier argument includes the halved exponent m. The old cusp has order144 and x,y,z have order72, so lambda modulo144 determines all old source and half-multiplier powers. The old braid-generator orders divide8 and9. For explicit representative units, use1 and eta73 whose p-adic entries are73 for p=2,3,5,7 and1 elsewhere. Every finite group in the comparison has only those prime divisors, so eta73 and (eta73−1)/2 act by the exact integer powers73 and36, including the source permutation components. For the general compatible unit the new target uses the very same multiplier as the selected actual Galois element.

Projection induces P/C≅P_A/C_A. Hence K=im(K6) has K/C of order25 and im(K6∩Fprime)=C. The actual joint source is D23×_(G_L/K)G_L, with common quotient order1728: every common quotient is solvable, kills C, then kills the normal5-group K/C. The actual joint four-strand target is T23×_(S96)T_L by the proved maximal solvable quotient and its binary degree-two factorization. Component generation and these exact maximal-common-quotient arguments prove generation in both common refinements. No generation with additional boundary moduli is inferred here.

The all76 free-evaluation target is a concrete refinement of the A5 Ferrari target. These results remain finite; the directed family containing every finite quotient has not been established and the full profinite CM question remains undecided.

## Primary-source search and its scope

Queries included `"Grothendieck" "Teichmuller" "SL(2,5)"`, `"GT-shadows" "SL" "Ferrari"`, `Pierre Guillot SL2(5)`, and `"Grothendieck" "SL(2,q)" Guillot`. No opened result supplied the present common-source CM-fibre calculation.

Opened Pierre Guillot, *The Grothendieck–Teichmüller group of a finite group and G-dessins d'enfants*, arXiv1407.3112v3, 3 December2015, https://arxiv.org/pdf/1407.3112. Section2.1, Lemma2.1 and the ensuing generating-pair orbit construction give the universal finite quotient by all epimorphism kernels. We use that construction with the explicit comparison proved above. Section2.3 takes the directed inverse limit over all finite groups; the introduction, printed page2, explicitly identifies that limit with the group denoted GT0 and leaves the pentagon subgroup outside the paper's subject. It therefore supplies no transfer from our single finite Ferrari target to the full profinite problem.

Also opened Guillot, *The Grothendieck–Teichmüller group of PSL(2,q)*, arXiv1604.04415, https://arxiv.org/pdf/1604.04415. Theorem1.1 concerns GT1(PSL2(q)); Section4 uses SL2 trace triples. These statements do not compute the induced SL2(F5) source and its joint CM corrections used here.

Reopened Nakamura–Schneps, *On a subgroup of the Grothendieck–Teichmüller group acting on the tower of profinite Teichmüller modular groups*, author manuscript https://webusers.imj-prg.fr/~leila.schneps/newGT.pdf. Theorem2.5, manuscript printed page11, gives the exact matrix formula for an actual Galois element; its sign is positive for chi=1. Equation(1.1) gives the braid action with f(y_i,sigma_i²)^−1 sigma_i^lambda f(y_i,sigma_i²). We will use the matrix theorem only for the actual Galois elements whose Kummer coordinates are supplied in E.29, not for arbitrary full-GT elements. Remark6.2 retains the additional relation(IV) for the extended coefficient comparison.
