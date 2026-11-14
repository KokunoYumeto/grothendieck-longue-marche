# D.45: cyclic-prime outer chief steps

The proved draft is sections/D_cyclic_outer_agent.tex. It applies to every finite nonabelian simple S with an actual split identification Aut(S)=S semidirect C_r, r prime, and every finite chief extension S^Omega over an arbitrary finite base D. It retains the actual original source epimorphism, an arbitrary new multiplier-one peripheral epimorphism to D, and all prescribed base conjugators. The full literal epimorphism counts agree.

## Exact new mechanism

For a nonzero surface character chi to C_r, every zero-character boundary admits an actual phase-changing source automorphism. If a handle supplies the nonzero character, the displayed bounding-pair map fixes [a,b]c and has c-conjugator c^-1 a^-1. Its homology changes b by c, so it preserves chi when chi(c)=0. If another boundary supplies the character, a pure Hurwitz square has the required phase at c and zero phase at the supplier. Every nonzero phase generates C_r. A boundary with nonzero character already has an outer-phase-invariant S-conjugacy class: its own element supplies every outer exponent while centralizing itself. These are actual bijections preserving epimorphisms, with inverses; no class-sum or proper-subgroup estimate is used.

The twisted Shapiro formulas retain the non-binary signs:

* b_original(d,omega)=-s_omega+epsilon(k(omega,d))+s_(omega*d);
* the gauge is z -> t^s_omega z t^-s_(omega*d);
* j_C(z,d)(omega)=t^g_omega z(p(omega)) t^-g_(omega*d).

All extending epsilon_C characters are counted. The actual canonical lift over each h_i gives one common field phase for each enlarged boundary root-set, including all its relative degrees and intersections. Source character matching and the independent phase bijections then give equal epimorphism counts at each intermediate subgroup.

For arbitrary finite D, maps killing the source kernel K are subtracted through the exact same finite epimorphism Phi:C -> S semidirect im(epsilon_C) on both sides. Its Shapiro section D -> E_C is independent of q_j. The displayed prescribed-conjugator difference lies in S^Omega, proving the finite-base bijection. The remaining maps have phi(K)=S by simplicity. Their normalizer extension to Aut(S) is unique because C_Aut(S)(S)=1. Subgroup-poset inversion and the exact coordinate-kernel/Goursat comparison prove equality of the complete literal generating fibres.

## Actual PSL2(F32) input

The proof identifies SL2(F32)=PGL2(F32) through the bijective square map on F32*. Its sharp three-transitive projective action identifies the 33 Sylow-two subgroups. Every automorphism is a normalizing permutation of this action. After the unique inner correction fixing infinity,0,1, translation and multiplicative subgroups force the permutation to be an actual field automorphism. This proves Aut(S)=S semidirect C5 with the literal squaring map. Simplicity is proved by the primitive-action/abelian-normal-subgroup argument, with the actual commutator [h(a),u(b)]=u((a^2-1)b) proving perfectness.

Primary texts independently opened:

* Donald L. White, author manuscript Character Degrees of Extensions of PSL2(q), 25 July2011, Section3 preceding Lemma3.1 and Lemma3.2; https://www.math.kent.edu/~white/papers/autpsl2.pdf. It states the exact field automorphism and full automorphism group. Proposed bibliography key ACyclicOuterWhite2011.
* Guralnick–Zieve, Polynomials with PSL(2) monodromy, Annals172(2010),1315–1359, Appendix, author PDF pp39–42; https://websites.umich.edu/~zieve/papers/gz.pdf. Its Appendix states simplicity, Dickson TheoremA.1 and the PGL/field automorphism comparison. Its subgroup classification is not needed in D45.

The exact D37 map is q1=beta_Q rho_n, with the literal three conjugators1,f_Q,h_Q. The resulting chief extension has maximal pro-five quotient exactly P_n because its simple-product kernel has no nontrivial finite five-group image. The theorem also retains an actual coupled finite source whose kernel over D is solvable. These positive chief-step families do not settle the full D1/D2 image.

## Reproducible checks

code/a_cyclic_outer_phase.py/.out/.json and _certificate.npz:

* all free-word maps/inverses,24 nonzero F5 handle characters;
* exact F32 arithmetic and all32736 determinant-one matrices;
* actual generation by upper unipotent, diagonal and Weyl matrices;
* all15 Frobenius generator-edge comparisons, sharp3-transitivity;
* all33 S-classes, three fixed plus six field orbits of size5;
* all12 S-classes in the four nonzero field cosets, each field-fixed;
* ten actual onto surface phase examples, with inverse words proving preservation of generation.

The first execution failed only in packing the ordered projective triple: an intermediate NumPy uint8 multiplication overflowed before conversion. The exact old script/output are retained as a_cyclic_outer_phase_uint8_superseded.py/.out. The authoritative run casts the entire action array to int32 before packing; it passed in0.778s. No mathematical conclusion uses the superseded packing.

code/a_cyclic_outer_shapiro.py/.out/.json and _certificate.npz:

* actual order125 Heisenberg base and its25-factor transitive action;
* all15625 base products and both signed cocycle/gauge identities;
* all five character extensions to one order25 overgroup;
*845 actual Aut(PSL2(F32)) multiplication comparisons for j_C;
*65 specified-base-conjugator comparisons;
* exact nonextension of the central character to the whole base, witnessed by [x,y]=(0,0,1).

The authoritative run passed in7.591s. It uses a_cyclic_outer_phase.py, which imports only the established word helpers from a_relative_prop.py and a_peripheral_count.py; no frozen source file was changed.

## Previous route and current boundary

The first contemplated route was a PSL2(F32) class-algebra annihilator computation plus a proper-subgroup subtraction. The actual boundary pushes supersede that approach and prove surjectivity preservation directly. No failed finite group-count claim was made. A possible stronger proper-subgroup-inner property of the D37 P1 automorphisms was considered but is not used or asserted in D45.

The two exact uses of prime cyclic outer order are the invertibility of a nonzero boundary character and the fact that a nonzero boundary element supplies all outer phases in its coset. Composite or noncyclic outer groups are not covered by this proof. In particular the A6 V4 obstruction family D36 remains within its proved scope and is not contradicted.
