#!/usr/bin/env python3
"""Literal generic section failure only; no post-node assertion."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_CE/next_symmetric_nodes/m_star_relative_face27.json';d=json.loads(p.read_text())
v=d['all_four_source_operators_local7']['v'];C=v['6'];a=v['1']
def red(w):
 z=[]
 for x in w:
  if abs(x) in (6,7):x=abs(x)
  if z and (z[-1]==-x or (x in (6,7) and z[-1]==x)):z.pop()
  else:z.append(x)
 return z
assert red(C)==C and len(C)==337 and any(abs(x) in (1,2,3,4) for x in C)
assert red(a)==a and len(a)==147
P={1:[1],2:[],3:[],4:[],5:[5],6:[6],7:[7]}
def project(w):return red([y if x>0 else -y for x in w for y in (P[abs(x)] if x>0 else P[abs(x)][::-1])])
assert project(C)==[-5,6,5] and project(a)==[-5,1,5]
result={'status':'PASS_LITERAL_INPUT_ONLY','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'original_v_C_length':len(C),'original_v_a_length':len(a),'projected_v_C':project(C),'projected_v_a':project(a),'scope':'Literal generic coarse section is not v-stable. No post-node nonexistence or surviving correction is inferred.'}
(ROOT/'work_CE/next_symmetric_nodes/one_family_kernel_gate28.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
