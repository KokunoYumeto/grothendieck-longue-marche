#!/usr/bin/env python3
from pathlib import Path
import importlib.util, json, hashlib, time
import sympy as sp
root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('pbc_boundary',root/'pbc_D88_boundary_certificate.py')
b=importlib.util.module_from_spec(spec);spec.loader.exec_module(b)
start=time.monotonic(); rows=[]
for r,m,N in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]:
 M=b.actual_relative_action(r,N,multiplier=2)
 T=b.actual_relative_action(r,N,shift=5**m)
 I=sp.eye(M.rows)
 result=b.smith_report((M-I).row_join(T-I))
 expected=[m-r+min(N-m,k) for k in range(1,r+1)]
 assert result['free_rank']==m-r
 assert result['nonunit_five_valuations']==expected
 rows.append({'r':r,'m':m,'N':N,'literal_dimension':M.rows,'expected_free_rank':m-r,'expected_torsion_exponents':expected,'actual_Smith':result})
obj={'status':'PASS','scope':'Independent literal permutation/deep-translation matrices confirm the affine-stabilizer formula in all four supplied finite examples; no entire arithmetic-kernel claim.','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'support_sha256':hashlib.sha256((root/'pbc_D88_boundary_certificate.py').read_bytes()).hexdigest(),'rows':rows,'elapsed_seconds':time.monotonic()-start}
(root/'pbc_middle_boundary_literal_rerun.json').write_text(json.dumps(obj,indent=2)+'\n')
print(json.dumps({'status':'PASS','cases':len(rows),'elapsed_seconds':obj['elapsed_seconds']}))
