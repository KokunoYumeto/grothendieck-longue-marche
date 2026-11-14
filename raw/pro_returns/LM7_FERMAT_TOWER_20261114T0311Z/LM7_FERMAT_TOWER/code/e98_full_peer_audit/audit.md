# Complete independent proof audit of E.98

Status: PASS. The complete 675-line theorem/proof was read. All four final program sources were inspected. The final central and normal-form programs were copied to this directory and executed afresh; both complete JSON certificates agree byte for byte with their author references. The earlier independent calculation in bc_e98_audit retains the full 73-element cusp-ray equality and all 2,190 original congruence substitutions. No mathematical correction is requested.

## Arithmetic source and actual section maps

The four actual decomposition generators in E98.15 have the displayed tame relations. The normalized Frobenii have independent Frattini characters, with determinant -4 over F_3. The actual E.56 source comparison and the continuous inertia bundle in Wingberg Theorem 2.4 give mutually inverse kernel maps, indexed by the two coset spaces of this free basis. This proves the pro-three free product with both specified local embeddings. Its actual generator inclusions into the full relative source give the reciprocal section and commute with complex conjugation. Inflation and the pro-three semidirect-product factorization consequently identify the stated global ramification locus with this source, including geometric conjugacy.

The odd-group square-root construction normalizes the value at c to one. Its remaining conjugators are exactly the fixed subgroup. The primed packet is the actual J-image with inverse inertia, so the single equation u T(a) u^{-1}=a^7 is both necessary and sufficient. There is no omitted arithmetic relation or unstated independent local extension.

## Class-two obstruction and complete fibres

The class-two tame equation is d m + sum v_d[U-k_d,e_d]=0, with d=(wedge^2 T_1)/7-I. The actual peripheral Kummer columns are sufficient here; the handle part of the higher action cancels from this equation. The compact determinant vector w is primitive, its chosen toric wedge coefficient is one, and the displayed maps Q,S,P give the actual quotient by its kernel. The 44-by-44 Smith inverse has factors 1^14,3^18,9^12 and is checked in both directions. Thus every integral central inertia is the specified solution plus a unique scalar multiple of w.

For each cusp, the projection of w after deleting that primitive cusp direction remains primitive. If h=(T_1-I)^{-1}(U-k_D), the exact identity d[h,e_D]=[(T_1-I)h,e_D] shows that the solution change is -SQ[rh,e_D]. Projecting first away from e_D forces the possible rational w-correction to be integral. The remaining wedge is integral exactly when rh belongs to V+Q_3 e_D. Applying T_1-I gives precisely r(U-k_D) in (T_1-I)V+Z_3 e_D. This checks both directions of E98.3, including the cusp O origin and the addition of any vector in 9W.

All nine actual local quotients have type C_3^5 plus C_9^2. Their displayed quotient maps are onto from P_1. The primitive cusp kernel contains no nonzero torsion element of P_1, while the triple-cusp kernel contains its full C_3^3; their indices are respectively 3^9 and 3^2. This yields all the stated fixed-inertia fibre types. The exhaustive two-digit elimination retains both the divided constant and divided-kernel carries, and tests exactly the original congruences. Its 73-element output is equal, as a set, to the nine cusp lines modulo nine. The universal horizontal kernel is exactly 9I_8.

After fixing the horizontal Smith representative, the first-degree conjugator is unique because I-T_1 is rationally injective on V^J. The residual central gauge is exactly (I-wedge^2 T_1)M^J. Its 45-by-21 matrix has factors 1^7,3^9,9^5 and free cokernel rank 24. The retained full row/column transformations, inverses and all 40 coordinate/conjugator round trips check. Adding the independent tame-kernel coordinate gives free rank 25 and the stated finite factors. The literal change E98.26 follows directly from the BCH product and retains the genuine eta_T(h) term, so it does not replace the actual action on handle lifts by its graded action.

The nonlifting inertia 9(e_A0+e_B0) has an integral displayed central solution and satisfies the full tame equation. Its abelian vector is outside every individual cusp line. Restriction along the actual arithmetic decomposition map and projection along N to N/N'' to N/gamma_3 N therefore prove its two nonlifting conclusions using the complete E.61/E.66 local classifications.

## Full and metabelian packets and their topology

E.61 and E.66 include all nonzero exponents and, for the metabelian group, exclude nonidentity inertia with zero abelianization. Their actual cusp centralizer is the full procyclic peripheral group. Hence changing g to g delta_D^k changes b to b+6k. Choosing b in {0,1,2} removes this right ambiguity uniquely; the remaining equivalence is precisely left multiplication by H^J. The actual word maps in E98.9 therefore give the claimed complete ramified packets.

The map [g] to g^{-1}J(g) is injective, has image the anti-fixed elements, and has the continuous inverse x to [x^{-1/2}]. On each nonzero valuation shell the packet map is a continuous bijection from compact to Hausdorff, and the shells are clopen in the ramified locus. This proves the asserted topology rather than only a set parametrization.

For R=N'', every fixed element of the metabelian quotient lifts to a fixed element: if k=h_0^{-1}J(h_0), then h_0 k^{1/2} is fixed. Removing this fixed lift from a representative over a target coset leaves k g_0 with k in R. Equivalence is exactly left R^J, proving the actual fibre map E98.28 and its inverse.

## Infinite Hall/Chen coordinates

The integral Fox map and its completed induced-module proof in E41.12–15 were reread. In particular the filtration equality K intersect m^(k+1)Lambda^10 = m^k K identifies the metabelian graded lattice with the homogeneous polynomial syzygy and supplies its topology. For R with its induced lower-central filtration, a zero graded image can be corrected by a lift from the next lower-central term; this proves exactness onto the kernel. The kernel is saturated because the target lattice is free. Thus the Hall-to-Chen kernel bases really supply the indicated group lifts.

For an anti element at one lower stage, any Hall/Chen lift u has d=uJ(u) central and J-fixed. The element u d^(-1/2) is an actual anti lift, and all others differ uniquely by the negative central eigenspace. The two integral idempotents (1 plus/minus J)/2 give both coordinate maps. Continuity holds at every finite stage. Every finite quotient of each pro-three group is nilpotent, and compactness gives surjectivity to the complete inverse limit; this proves the product homeomorphisms, including the induced filtration on R.

PBW/Mobius inversion gives the stated full character formula. The surjective multiplication map V tensor Sym^(m-1)V to Sym^m V gives the Chen rank and character, with no denominator issue over Z_3. Taking negative ranks and then the saturated comparison kernel gives every exponent in E98.11–14. The first fourteen rows were executed independently, including the degree-four difference 504.

## Source and execution scope

The fresh primary Wingberg reading and exact references are retained in bc_e98_audit/audit.json: Theorem 2.4 and full proof, printed pages 13–15; continuous bundle and Lemma 1.1, pages 4–5; remark after Proposition 2.1, page 11. The present audit also reread the actual integrated proofs E.41, E.61 and E.66 at the precise comparison steps above.

The two newly copied executions are e_global_split7_central.py and e_global_split7_normal_forms.py, with their actual stdout and JSON in this directory. No claim is made to have rerun the two earlier exhaustive author programs a second time; their complete sources were inspected, and the independent earlier witness/set check is retained separately. All mathematical assertions in the complete E.98 proof passed this audit.
