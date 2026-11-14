--- original_frozen
+++ post_word_moving_repair
@@ -653,7 +653,44 @@
 Use the eight actual involution words in
 (D.64.27) to cancel the two coordinates
 \(p_2[q_2z]\), \(p_3[q_3z]\). They do not
-change (D.64.29). The only remaining defect
+change (D.64.29). Before odd averaging, these
+eight words can also introduce a new component
+in \(\mathcal K_{\rm mov}=(1-e_\Delta)\mathcal K\).
+Remove that component at this point, after the
+eight words. The group \(\Delta\) is normal of
+odd order, so \((\mathcal K_{\rm mov})_\Delta=0\)
+and hence \((\mathcal K_{\rm mov})_G=0\).
+The exact two-conjugator map on this actual
+submodule is therefore onto:
+\[
+ (1-s)\mathcal K_{\rm mov}
+       +s(1-r)\mathcal K_{\rm mov}=\mathcal K_{\rm mov}.
+\]
+This is the same augmentation argument as
+D.58.17, now with the specified \(\Delta\)-moving
+summand in D.63.10. The full kernel proof in
+D.58 identifies \(\mathcal K\) with the actual
+image of \(R_{50}\cap L_{*,2}\) in \(\mathcal T_2\).
+Thus the two chosen coefficients have source
+lifts in
+\[
+ R_{50}\cap L_{*,2}
+       \ \subset\ S_{57}=\mathfrak R_h\cap M_*\cap L_{*,2}.
+\]
+They have zero images in \(Y\), in both literal
+\(X_*\) conjugators, and in \(\mathcal W_h\).
+All previously selected invariant projectors
+kill \(\mathcal K_{\rm mov}\). The maps defining
+\(\Phi_{64}\) also kill it, when extended by
+zero from the invariant summand: each begins
+with the compact self projection after \(e_\Delta\).
+Consequently this post-word correction removes
+precisely the reintroduced moving component
+and preserves all the just-cancelled compact
+coordinates. The cusp error is again in
+\(\mathcal J_{63}\).
+
+The only remaining defect
 in \(\mathcal E_{64}\) is the augmentation
 part of \(C_1\). Since the actual generators
 \(s,r\) generate \(G\), the exact map
