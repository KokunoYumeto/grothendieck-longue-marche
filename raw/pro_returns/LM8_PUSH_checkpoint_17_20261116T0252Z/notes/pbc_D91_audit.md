# Independent full audit of D91

**Status: PASS for the full mathematics and executed certificate.** One literal TeX typo (`+in` after the whole-kernel sentence) was reported to the author; it does not affect the proof. Reviewed draft: `notes/de_sha_all_cusp_parameters_draft.tex`, SHA-256 `639d726ded3ce6519ce4788ebf6a071497823197f4771913f39de84f3ce5f8ec`, all 529 lines.

## Actual actions and natural maps

1. The pure-valuation and zero-class cases use equality of the actual global/local graph images, so no subtraction of infinite depths occurs. The range N≤m has the graph multiplier literally trivial on both R and its actual submodule J; it is the same D88 map. The m≤r range reduces to the previously audited D90 argument.
2. In the strict middle range, the operator-difference ideal is exactly (P,q_m), and the actual compact kernel is retained as the kernel of the map induced by J→R. The target is the ordinary dual of the actual local Cartier-invariant group and is torsion-free by D77. This target property is used explicitly later; no map is discarded from a rank comparison.
3. The scalar coefficient is exactly R_m/(5^b F_(r,m)), with the retained q_r factor. Its Cartier-untwisted action is χ^-1 Sχ(t^(5^r))ρ0, and the natural map is multiplication by q_r. These formulas match the independent actual scalar matrices.

## Infinite product layer and axes

4. Both v and w are regular in the coefficient ring: w is the image of v under the continuous invertible change of variables in the complete (5,u,v)-adic ring. Thus the product layer is the actual quotient B/uB, with coefficient C=Z/5^e or Z5. Its retained generator gives χSχ(1+v)^3; multiplication by v³ identifies the relevant weighted augmentation module, with omitted tame weights χ,χ²,χ³. The product type follows from the already audited shell argument.
5. Modulo u, the two quotient jets have weights χ²,χ³. Every invariant quotient element therefore lies in uQ. The identity (u)∩(vw)=(uvw) follows because v² is regular modulo u, so uT→uQ is an actual equivariant isomorphism. This proves the zero snake map and injects E_Γ before any boundary calculation. The same argument works under each coefficient reduction.
6. The annihilator of u is exactly (Z/5^b)[[v]]Norm_m in the finite case. Cancellation in the original torsion-free ring and evaluation at u=0 prove both generation and its exact coefficient modulus. At infinity the norm line has coefficient Z5. The two-axis kernel has weight χ³ and the cokernel weight χ², so they disappear under exact tame averaging.
7. The source first-axis action is transported by uq_r to ordinary permutation on uJ/q_m uJ. The comparison with J/q_mJ has kernel q_mJ/u q_mJ of weight χ² and cokernel J/uJ of weight χ; these vanish in all Γ-homology. The target is transported by u to uR_m. Its coinvariants inject into R_m coinvariants because the fixed zero basis vector gives the required H1 surjection. Both half-gauges commute with q_r. Therefore the actual boundary map is the literal map, with its full torsion kernel retained.

## Exact middle boundary

8. I independently derived this part before the owner draft in `pbc_middle_boundary_derivation.md`. For the actual affine group C_(5^b)⋊Γ, a nonzero lower shell has stabilizer abelianization C_(5^min(b,k))⊕Z5. The sole upper stabilizer maps by (unit,5^h). Its cokernel is one cyclic group of exponent h+min(b,k), rather than a split sum of two layers. The zero-orbit stabilizer gives no extra cokernel. The free orbit-kernel quotient has rank h.
9. The continuous Shapiro passage is correctly justified by dualizing finite permutation modules to discrete Q5/Z5-valued functions. The functorial map is restriction on characters and thus stabilizer inclusion after dualizing, not transfer. Freshly opened primary support: J. S. Milne, *Class Field Theory*, version4.03, ChapterII Proposition1.11 (printed62), Example1.27(a) (printed68–69), Proposition1.30 (printed70), https://www.jmilne.org/math/CourseNotes/CFT.pdf; opened refs turn1205view0–2. The finite-coset cochain proof applies continuously to the open stabilizers used here.

## Entire finite and infinite kernels

10. At finite depth, the preimage of finite boundary torsion is exactly M_tor: its product layer is bounded and its remaining quotient is finite. The actual target is torsion-free, so this entire preimage lies in the kernel, and injectivity of the free boundary part gives the converse. Restriction/corestriction for the actual finite-index operator subgroup kills the entire kernel by5^e. Exact bounded cyclic lifts then split the extension; the exponent-e factors are absorbed into the countable product, while the smaller factors remain. This is not a split-graded inference.
11. In (D91.24), compactness and closedness of the image of the actual operator2−1 justify passage to the inverse limit. The ideals5^bF tend uniformly to zero. For b≥r, the actual maps are onto, identity on the free orbit quotient, and have the same finite torsion order; hence they are isomorphisms. This gives the infinite boundary and its actual natural map.
12. In (D91.27), the finite coefficient zero-snake injection is compatible with reduction and gives E_Γ∩5^H M=5^H E_Γ. After removing the finite free orbit quotient, H≥m kills the finite remaining quotient, so5^H M0=5^H E_Γ. The finite order lifts modulo this subgroup can be corrected integrally to actual finite order. This proves the continuous split extension at infinity without equal-corank reasoning.
13. The actual generator maps as q_rvw=P(q_r/u)=0. Thus the whole product layer is killed, and target torsion-freeness kills the split finite torsion. The actual boundary map embeds the free orbit quotient, proving that there is no larger kernel.
14. D77 gives precisely the additional free boundary rank2H or2h. The three actual tripod automorphisms carry their tangential frames and all global/local maps; κ(-1)=0 only in the stated pro-five setting. The rational tangent examples have primitive away-five valuation at2 and the claimed local logarithmic depth. The explicit (1,2,4,3) example and all degeneracies agree with the stated formula. No assertion about arbitrary pairs or all infinitely ramified H1 ranks is made.

## Executed independent evidence

The independent rerun of `de_sha_cusp_complete_certificate.py` reproduced the entire mathematical JSON after excluding only elapsed time and source metadata: twelve middle source/diagonal rows, two target rows, exact norm and natural-map equations, and the stated rational tangent. Retained outputs: `pbc_D91_certificate_rerun.json/.out`.

Additional independent supporting artifacts are `pbc_middle_boundary_certificate.py/.json/.out` (180 exact stabilizer Smith/valuation checks) and `pbc_middle_boundary_literal_rerun.py/.json/.out` (all four literal integral permutation/deep-translation examples). None is used in place of the all-depth or actual-map proof.
