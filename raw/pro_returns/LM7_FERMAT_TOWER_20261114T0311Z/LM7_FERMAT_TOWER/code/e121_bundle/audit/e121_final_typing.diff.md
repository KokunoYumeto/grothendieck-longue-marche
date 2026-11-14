--- original_128_file_freeze
+++ actual_lift_rule_and_completed_kernel_map
@@ -438,9 +438,14 @@
 Applying the actual projected norm of E.119 to
 $p_L(a)=(1,1)$ gives $N_L(a)=(2,0)$.
 It is onto; alternatively, onto-ness follows directly from
-E.119's onto quotient norm. The trace identity then forces
-$j_L=3N_L^{-1}$ in the displayed bases, yielding (E121.4).
-Its kernel is zero. All norm/extension squares and both
+E.119's onto quotient norm. Its kernel is $3A_{L_2}$:
+the target has exponent three, while both $\ker N_L$ and
+$3A_{L_2}$ have order nine.
+The actual trace identity gives the precise rule
+$j_L(b)=3a$ for any lift $a$ with $N_L(a)=b$.
+Changing that lift by $3A_{L_2}$ changes $3a$ by zero,
+since $9A_{L_2}=0$. This rule yields (E121.4), and its
+kernel is zero. All norm/extension squares and both
 compositions are verified on the full finite groups.
 The ambiguity $a\mapsto a+3ku$ gives the literal coordinate
 shear $(r,s)\mapsto(r+3ks,s)$; it leaves every displayed
@@ -540,6 +545,19 @@
 $N_h(\xi)=\xi^{1+4+7}=\zeta$.
 Thus every completed kernel has exactly the displayed
 literal $\mu_3$ torsion and the rank difference in (E121.9).
+For each of these actual kernels $K$, choose a $\mathbb Z_3$-basis
+of the free quotient $K/\mu_3$ and lifts $k_1,\ldots,k_r\in K$.
+The displayed direct-sum isomorphism is the continuous map
+$(z,(a_i))\mapsto z\prod_i k_i^{a_i}$.
+Its inverse reads the quotient-basis coordinates $(a_i)$ and
+then divides the input by $\prod_i k_i^{a_i}$ to obtain
+$z\in\mu_3$. These two constructions compose to the identity.
+A different quotient basis is an actual $\mathrm{GL}_r(\mathbb Z_3)$
+coordinate change; a different lift multiplies $k_i$ by
+a specified element of $\mu_3$ and changes the torsion coordinate
+by the inverse product of those elements to the powers $a_i$.
+Thus the choice ambiguity is explicit without assigning an
+uncomputed numerical upper unit basis.
 Finite-rank unit groups complete exactly, and all norm
 images have the proved finite index, so the same finite
 quotients and actual images persist under completion.
