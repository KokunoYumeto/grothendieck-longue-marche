--- initial
+++ final
@@ -119,7 +119,10 @@
 action. There are integral equivariant maps
 \(A_a:M_a\to\mathcal L\), for \(a=1,4\), and continuous
 projective coefficient derivations \(\eta_a:Y\to M_a\),
-with \(\eta_a|_U=m_a\) and \(\eta_a(t)=0\), such that
+inflated from the actual full homology source
+\(\mathcal J_\infty\). Their restrictions to
+\(U=\ker(\mathcal J_\infty\to G)\) are \(m_a\),
+and \(\eta_a(t)=0\). They satisfy
 \[
  \begin{aligned}
  T_{64}&=T_{63}+A_1m_1+A_4m_4,\\
@@ -186,7 +189,7 @@
  \mathcal L\twoheadrightarrow\ker\theta_P.
  \tag{D.64.11}
 \]
-The first integral homology map is onto by D.58.2;
+The integral map \(\theta_U\) is onto by D.58.2;
 the second assertion is the resulting kernel map
 in the exact-sequence diagram. All these kernels
 are saturated. Their reductions are therefore the
@@ -335,7 +338,7 @@
 induced form has rank 16. Its restriction to
 \(\ker\phi_a\) has rank eight and radical rank
 four. The adjoint
-\(\bar{(H_a^{\rm int})^{-1}\phi_a^tH_{*,a}^{\rm int}}\)
+\(\overline{(H_a^{\rm int})^{-1}\phi_a^tH_{*,a}^{\rm int}}\)
 has rank four and is killed by \(\phi_a\).
 All semilinear stabilizer maps preserve the
 actual form, with coefficient conjugation on
@@ -357,12 +360,12 @@
 matrix and \(\epsilon_g\) records character
 exchange, its exact equations are
 \[
- A_g\overline X^{\,\epsilon_g}=XA_g,
+ A_gX^{[\epsilon_g]}=XA_g,
  \qquad \phi_aX=T_{*,a}\phi_a,
  \tag{D.64.17}
 \]
-where \(\overline X^{\,0}=X\) and
-\(\overline X^{\,1}=\bar X\).
+where \(X^{[0]}=X\) and
+\(X^{[1]}=\bar X\).
 The linear ranks are 504 and 506. The certificate
 retains a particular solution \(X_0\) and every
 homogeneous basis matrix \(D_i\), so all solutions
