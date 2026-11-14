--- superseded/d_e119_maps.py
+++ corrected/d_e119_maps.py
@@ -50,7 +50,13 @@
 
 def matrix(a): return sp.Matrix(a)
 def integral(a): return all(v.q == 1 for v in a)
-def integers(a): return [[int(v) for v in a.row(i)] for i in range(a.rows)]
+def integers(a):
+    assert integral(a), 'integer serialization requires integral entries'
+    return [[int(v) for v in a.row(i)] for i in range(a.rows)]
+def rationals(a):
+    data = [[str(v) for v in a.row(i)] for i in range(a.rows)]
+    assert sp.Matrix([[sp.Rational(v) for v in row] for row in data]) == a
+    return data
 def mod3(a): return a.applyfunc(lambda v: int(v) % 3)
 
 # Independently reconstruct the cyclic Kummer algebra and its real marking.
@@ -272,7 +278,9 @@
             'actual_HNF_generator_map_checks':group_checks,
             'HNF_Smith_roundtrips':len(Q),'norm_transfer_compositions':len(Q),
             'transfer_values':transfer_values,'projected_capitulation_kernel':caps,
-            'HNF':integers(H),'forward':integers(forward),'inverse':integers(backward)}
+            'HNF':integers(H),'forward':rationals(forward),'inverse':integers(backward),
+            'forward_serialization':'exact rational strings, decoded and compared entrywise',
+            'forward_denominators':sorted({int(v.q) for v in forward})}
 
 Braw=sp.zeros(2,9); Braw[:,6:]=Gclass
 Blifts=sp.zeros(9,2); Blifts[6,0]=1; Blifts[6,1]=-1; Blifts[8,1]=2
