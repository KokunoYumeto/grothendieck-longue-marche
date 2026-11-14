--- root_original_replayed_source
+++ corrected_frozen_author_source
@@ -67,7 +67,17 @@
     r=[x for x in records[name] if x['type']==typ];assert len(r)==1,(name,typ)
     return r[0]
 def mat(x):return S.Matrix(x)
-def ints(m):return [[int(v) for v in m.row(i)] for i in range(m.rows)]
+def ints(m):
+    assert all(S.denom(v)==1 for v in m), 'nonintegral matrix passed to integer serializer'
+    encoded=[[int(v) for v in m.row(i)] for i in range(m.rows)]
+    assert S.Matrix(encoded)==m
+    return encoded
+
+def rationals(m):
+    encoded=[[str(S.Rational(v)) for v in m.row(i)] for i in range(m.rows)]
+    decoded=S.Matrix([[S.Rational(v) for v in row] for row in encoded])
+    assert decoded==m, 'rational matrix export failed exact round trip'
+    return encoded
 def imod(m,n):return m.applyfunc(lambda x:int(x)%n)
 def integral(m):return all(S.denom(x)==1 for x in m)
 def r3(m):
@@ -284,7 +294,7 @@
     return {'Gamma':gd,'coinvariants':kd,'norm_matrix':ints(N[:,:len(kd)]),
             'norm_fibres':{str(k):v for k,v in sorted(images.items())},
             'exact_Smith_roundtrips':roundtrips,'Gamma_restriction_fibres':dict(fibres),
-            'kernel_lattice':ints(K),'forward':ints(KU*K.inv()),
+            'kernel_lattice':ints(K),'forward':rationals(KU*K.inv()),
             'inverse':ints(K*KU.inv()),'relation_HNF':ints(H)}
 
 gb=row('e53_genus_transition','next_genus_presentation')
