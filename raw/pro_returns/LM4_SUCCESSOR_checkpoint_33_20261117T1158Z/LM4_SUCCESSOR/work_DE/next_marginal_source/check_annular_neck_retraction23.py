#!/usr/bin/env python3
"""Literal first-neck basis and its actual annular retraction."""
from pathlib import Path
import hashlib,json
import sympy as S
ROOT=Path(__file__).resolve().parents[2]
path=ROOT/'work_CE/next_symmetric_nodes/inner_q0_adapted_basis22.json'
D=json.loads(path.read_text())
def red(w,c=0):
 a=[]
 for x in w:
  x=c if c and abs(x)==c else int(x)
  if a and (a[-1]==-x or c and a[-1]==x==c):a.pop()
  else:a.append(x)
 return tuple(a)
def inv(w,c=0):return red((-x for x in reversed(w)),c)
def sub(w,A,c=0):return red((y for x in w for y in (A[abs(x)] if x>0 else inv(A[-x],c))),c)

# Old neck basis O=(x1,x3,x4,x5,x6), new basis Z=(a,bar b,d,e,f).
O_in_Z={1:(1,2,-1),2:(1,),3:(5,3,4,-3,-5),4:(3,),5:(-3,5,3)}
Z_in_O={1:(2,),2:(-2,1,2),3:(4,),4:(-5,-4,3,4,5),5:(4,5,-4)}
for j in range(1,6):
 assert sub(O_in_Z[j],Z_in_O)==(j,)
 assert sub(Z_in_O[j],O_in_Z)==(j,)
Z_in_Y={1:(1,),2:(3,2,3),3:(5,),4:(6,),5:(4,)}
actual_old=(1,3,4,5,6)
for j,old in enumerate(actual_old,1):
 assert sub(O_in_Z[j],Z_in_Y,3)==red(D['old_in_Y'][str(old)],3)
def detector(w):
 parity=0;out=[];positions={1:1,2:2,5:3,6:4};keep={1:0,2:1,5:0,6:0}
 for x in red(w,3):
  if x==3:parity^=1
  elif abs(x)==4:out.append(5*(1 if x>0 else -1))
  elif parity==keep[abs(x)]:out.append(positions[abs(x)]*(1 if x>0 else -1))
 assert parity==0
 return red(out)
for j in range(1,6):assert detector(Z_in_Y[j])==(j,)
opposite={j:detector((3,)+Z_in_Y[j]+(3,)) for j in range(1,6)}
assert opposite=={1:(),2:(),3:(),4:(),5:(5,)}

# Actual original comb cone and its connector to the q0-adapted cone.
old_cone_Y=red(D['old_in_Y']['2'],3)
P=(1,3,-2,3) # a*(bar b)^-1
assert old_cone_Y==red(P+(3,)+inv(P,3),3)
K0=inv(P,3)
assert K0==sub((-2,1),{1:tuple(D['old_in_Y']['1']),2:tuple(D['old_in_Y']['3'])},3)

# The mirror identity is rational, with z later specialized to bar(q).
q,u=S.symbols('q u')
T=lambda v,x:(x+v*v-2*v)/(v*v+(1-2*v)*x)
assert S.cancel(T(u,1/q)-1/T(1/u,q))==0

out={'status':'PASS','input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'old_neck_basis_labels':['x1','x3','x4','x5','x6'],
 'new_neck_basis_labels':['a','bar_b','d','e','f'],
 'old_basis_in_new':O_in_Z,'new_basis_in_old':Z_in_O,
 'ten_literal_free_inverse_compositions':10,
 'new_basis_in_actual_Y':Z_in_Y,'all_five_actual_table_comparisons':True,
 'detector_on_new_basis':[[j] for j in range(1,6)],
 'retracted_opposite_cone_images':opposite,
 'original_comb_cone_in_Y':old_cone_Y,
 'P_for_c_old_equals_P_C_P_inverse':P,'K0_for_C_equals_K0_c_old_K0_inverse':K0,
 'rational_mirror_identity':'T_u(1/bar(q))=1/overline(T_u(q))',
 'scope':'Actual ordinary annular K retraction. No generator-wise mirror inversion or identification of a boundary-gap cone with a comb cone is assumed; actual cross-commutator maps remain separately typed.'}
Path(__file__).with_name('annular_neck_retraction23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS ten free Nielsen inverses and all5 actual old-to-Y neck expressions.')
print('PASS actual detector is identity on K=(a,bar b,d,e,f).')
print('PASS opposite-cone retraction kills first4 and fixes f; exact old-cone connector retained.')
print('PASS rational mirror identity; no individual mirrored meridian word assumed.')
