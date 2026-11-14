--- superseded/d_e119_maps.py
+++ final_amended/d_e119_maps.py
@@ -24,7 +24,7 @@
     return hashlib.sha256(p.read_bytes()).hexdigest()
 
 PROOF_HASH = '25d9250dabab99ca3848525d608ed6968323cdc58400f75b8d074a90d79759c0'
-MANIFEST_HASH = '79d424d7f19195b64260847b54544206615d0ed4c3f1011e8f88dc4392d6831d'
+MANIFEST_HASH = '67657642ad1f77f73b23a0147b82f717eedb5e9c1165bba0fad5e39a16d082e1'
 proof = SOURCE/'sections/E_lower_fiftythree.tex'
 mp = SOURCE/'ledger/e_lower_fiftythree_manifest.json'
 assert sha(proof) == PROOF_HASH and sha(mp) == MANIFEST_HASH
@@ -33,7 +33,8 @@
     p = SOURCE/name
     assert p.stat().st_size == record['bytes'], name
     assert sha(p) == record['sha256'], name
-assert len(manifest['files']) == 191
+assert len(manifest['files']) == 415
+author_export=json.loads((SOURCE/'code/e_lower_fiftythree.json').read_text())
 
 STAGES = ('horizontal_base', 'genus_kummer', 'six_character_witness',
           'horizontal_norm_matrix', 'genus_transition', 'local_genus_maps',
@@ -50,7 +51,13 @@
 
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
@@ -230,6 +237,10 @@
     KD=matrix(r['kernel_smith_diagonal'])
     mods=[int(KD[i,i]) for i in range(n)]
     forward=KU*K.inv(); backward=K*KU.inv()
+    export_key='B2_genus' if name=='next_genus_presentation' else 'L2_genus'
+    exported=sp.Matrix([[sp.Rational(v) for v in row] for row in author_export[export_key]['forward']])
+    assert exported==forward and matrix(author_export[export_key]['inverse'])==backward
+    assert exported*backward==backward*exported==sp.eye(n)
     seen=set()
     for a in Q:
         c=forward*sp.Matrix(a); assert integral(c)
@@ -272,7 +283,9 @@
             'actual_HNF_generator_map_checks':group_checks,
             'HNF_Smith_roundtrips':len(Q),'norm_transfer_compositions':len(Q),
             'transfer_values':transfer_values,'projected_capitulation_kernel':caps,
-            'HNF':integers(H),'forward':integers(forward),'inverse':integers(backward)}
+            'HNF':integers(H),'forward':rationals(forward),'inverse':integers(backward),
+            'forward_serialization':'exact rational strings, decoded and compared entrywise',
+            'forward_denominators':sorted({int(v.q) for v in forward})}
 
 Braw=sp.zeros(2,9); Braw[:,6:]=Gclass
 Blifts=sp.zeros(9,2); Blifts[6,0]=1; Blifts[6,1]=-1; Blifts[8,1]=2
@@ -288,7 +301,8 @@
 
 result={
  'status':'PASS','statement':'E.119','audit_role':'independent peer mathematical/map audit',
- 'proof_sha256':sha(proof),'manifest_sha256':sha(mp),'frozen_files_verified':191,
+ 'proof_sha256':sha(proof),'manifest_sha256':sha(mp),'frozen_files_verified':415,
+ 'amended_author_rational_exports_decoded_and_composed':True,
  'source_read_scope':{'complete_proof_lines':len(proof.read_text().splitlines()),
                      'owned_GP_sources':8,'dependency_GP_sources':2,
                      'Python_checker_complete':True},
