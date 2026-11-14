# D.37: an actual mixed Fermat12 shadow and its two compact cover actions

The new result is a fully generating finite GT0 shadow on a quotient that contains the congruence data and the common Fermat12 homology. Its actual normalized cubic-cover Tate4 matrix is -I, and its actual quartic-cover Tate3 matrix is I. Both are obtained from the same cyclic12 compact action through the exact maps of D36. The resulting pair violates D36's arithmetic degree-six graph. The retained LM2 fixed-fibre coordinates are T4=I and W3=[i], with the exact conjugator and gauge maps kept throughout.

## Exact quotient and source maps

Let B=C2*C3, F=ker(B→S3), Q=SL2(Z/12)/{±I}, N=ker(B→Q), and F12=ker(F→(Z/12)^2), with the positive loops x,y mapping to the ordered basis. Set L=N∩F12. The explicit affine representation sends s to the swap matrix with zero translation and r to the order-three matrix (0,-1;1,-1) with translation e1. Direct multiplication gives x=t^-2 the translation e1 and y=sxs the translation e2, so its kernel is exactly F'. Joining its mod12 reduction with Q gives H=B/L of order6912.

The kernel of H→Q is the twelve-element subgroup {(a,b):a,b even,a+b=0 mod3}, isomorphic to C2²×C3. The corresponding graph has6912 edges,5760 vertices and1153 fundamental cycles. Thus L is free of rank1153. Its affine mod4 and mod3 reductions have orders2304 and1728, and H is their full fibre product overQ. The subgroup F12 has rank145 and L has index8 in it.

There is an actual comparison chain J12→G6→H→Q, where Jm=B/[L,L]L^m and G6=B/[N,N]N^6. The first inclusion of kernels uses L⊂N and12 divisible by6; the second uses the exponent-six abelian kernel of H→Q. The geometric plus Fermat12 model maps to v^12=z(z−1) over Q(ζ24) by z=−x0^12/x∞^12 and v=ζ24 x0x1/x∞². The specified positive-interval roots reproduce the exact tangent of D36; the twist is not suppressed.

## Complete finite equations and actual generation

All48 matrix conjugator pairs have been tested, with144 possible joint-base lifts each. Exactly576 choices satisfy the base cusp relation, and every one induces a base automorphism checked on all6912 states and both generators. The complete homology correction matrix has rank1152 at both2 and3. At2,288 choices survive over24 matrix pairs, including12 extra pairs. At3,192 survive over all48 pairs, including24 extra pairs. Exactly96 base choices satisfy both tests, over24 matrix pairs,12 of them extra. These counts concern linear cusp solvability; the final generating witness is separately checked.

The selected witness retains D33's exact G6 conjugators before the common Ihara gauge. Its mod2 target includes D27's recorded right-s-centralizer correction, retained by all later corrections in Φ(N^(2)); its mod3 target is the separately retained centralizer representative, with twice cycle39. It does not silently reduce D33's long pro2 word at3. Appending these exact constraints gives ranks1247 and1248, with affine dimensions1059 and1058. The selected base coordinates are A=(I,(6,0)) and beta=((3,4;8,3),(6,0)).

The mod2 kernel map has rank1153 on trial1. At3 the successive ranks are1099,1045,1135,1063,1081,1135,1153, so trial7 gives the generating map. Every fundamental cycle is converted to a literal B word and checked integrally; direct substitution independently reproduces every induced kernel column. The resulting J6 action is an actual automorphism.

The exponent4 upper equation then passes on its first attempt and retains that exact J6 action. Its correction rank is1152 and affine dimension1154. CRT with the recorded mod3 solution gives an actual J12 automorphism, of quotient order6912·12^1153. The cusp has order288, and the GT-shadow N_ord is144. A673392-letter corrected cusp word vanishes in all6912 graph coordinates modulo12. All1153 kernel images are checked again. The integral beta abelianization is(882,180), so the common gauge k=−702 gives an actual commutator f; both m=0 hexagons are multiplied in the faithful model and pass. The gauge leaves T=A^-1V and W=beta^-1V unchanged. D25's retained G6 rigidity makes the extra CM pair an invariant of this finite shadow.

## The actual two-cover evaluation

The six-edge S3 graph gives the exact free-basis conversion x=b1,y=b2^-1. The normalized f becomes a99308-letter word in x,y. For each n=3,4,12, its Schreier coordinates give the action through y↦f^-1 y f and x↦x. Every Schreier-generator image is also checked by direct word substitution. The compact filling matrices are exactly those of D36.

The outputs are cubic Tate4=-I and quartic Tate3=I. Both are checked against the single compact C12 matrix through the integral projection matrices. The cubic Teichmueller factor is1, hence its normalized sign is−1; the quartic projective i-exponent is0. These violate the arithmetic graph, giving a second direct nonarithmeticality certificate. This calculation evaluates the actual cover and fixed-fibre maps separately on one finite source; it does not infer GT0 naturality from a theorem proved only for Galois elements.

## Exact relative quotients and the mixed kernel

Put L4=ker(B→H4) and L3=ker(B→H3), of ranks385 and289. The sequences L→L4→C3 and L→L3→C2² give exact coinvariant isomorphisms (L_ab/4)_C3≅L4_ab/4 and (L_ab/3)_C2²≅L3_ab/3. The complementary group orders are units, so averaging proves these statements and splits the coefficient kernels.

Therefore J12's universal relative pro2 quotient overQ is B/[L4,L4]L4^4, while its universal relative pro3 quotient is B/[L3,L3]L3³. Both are actual quotients of the corresponding full relative sources. Their maximal common quotient isQ. The map from J12 onto their fibre product has exact kernel (Z/4)^768⊕(Z/3)^864. These maps show exactly what the separate prime-relative tests forget in this finite quotient.

## Reproducibility and scope

All six installed programs were run under their final names, with actual nonempty stdout and JSON certificates: d_cm_fermat_joint_base.py, d_cm_fermat_mixed_linear.py, d_cm_fermat_mixed_generate.py, d_cm_fermat_mixed_compatible.py, d_cm_fermat_exponent4.py and d_cm_fermat_cover_matrices.py. Dependencies are NumPy, the earlier exact D25/D27/D36 JSON certificates, and the preceding programs' output. Their import chain regenerates the required intermediate calculations. The full integrated runs passed, with times approximately11.5,16.6,21.2,54.3,56.6 and1.0seconds.

Agent A independently checked the base quotient, reran its complete certificate, and audited both maximal-relative-quotient proofs. The final cover and witness audit passed: root independently read the complete proof, reopened the finite-shadow definitions and freshly reran all six computations. Every exact certificate agrees; only execution-time metadata differs. The complete audit outputs are retained in code/root_d37_audit.out, code/root_d37_exponent4_fresh.out and code/root_d37_cover_fresh.out. No full profinite lift of this shadow has been proved. The exact comparison with D33 stops at G6; matching its larger degree-eight action remains a separate finite compatibility calculation. The whole missing CM pair and the full profinite metabelian realization tasks remain unresolved.
