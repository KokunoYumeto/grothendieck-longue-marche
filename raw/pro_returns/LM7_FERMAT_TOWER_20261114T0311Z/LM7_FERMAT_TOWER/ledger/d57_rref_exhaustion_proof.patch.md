--- pre_rref_exhaustion.tex
+++ D_arithmetic_class2_repair.tex
@@ -404,7 +404,16 @@
 part lies in the quaternion derived group. Exact
 integral equations pair state 26 with \(T_1\), and
 state 33 with \(T_3\). The other two pairings have
-no integral solution. The normalized \(r\)-conjugator
+no integral solution. The recorded row reductions have
+only denominators \(1,3,6\), whose two-primary parts
+divide two; the program explicitly asserts that they
+divide four before enumerating the five free variables
+modulo four. Changing any free variable by an element
+of \(4\mathbb Z_2\) therefore changes every solved
+coordinate by an integral element. The final scaling
+by seven is a unit. Thus the 1024 tested free residue
+choices exhaust all integral possibilities in each
+rejected pairing. The normalized \(r\)-conjugator
 has quotient coordinate one, by D.49's coprime
 centralizer correction. Above each of the two
 \(s\)-coordinates there are nine elements of
