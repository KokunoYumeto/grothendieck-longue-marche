#!/usr/bin/env python3
"""Exact arithmetic-conjugacy action on the final two Johnson parameters.

u remains a Frobenius at7 after conjugation in G_K,{3}; v=cuc is then
redefined by the same fixed involution.  This is a source basis change,
with the actual matrix morphism retained, not a geometric gauge assertion.
"""
from pathlib import Path
from itertools import product
import importlib.util,json,contextlib,io
import numpy as np
HERE=Path(__file__).resolve().parent
def load(name):
 spec=importlib.util.spec_from_file_location(name,HERE/(name+'.py'))
 obj=importlib.util.module_from_spec(spec)
 with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(obj)
 return obj
f=load('de_fermat_schreier');g=load('a_ihara_gauge')
raw=json.loads((HERE/'a_ihara_final_parameters.json').read_text())
U0,J0=f.generator_images(np.array(raw['base_fa']),np.array(raw['base_fz']),7)
J0=np.array(raw['base_Johnson_matrix'],dtype=np.int64)
L=[np.array(A,dtype=np.int64) for A in raw['correction_matrices']]
C0,CJ=f.generator_images(*f.zero(),chi=8)
def autom(A,J):
 return np.block([[A,np.zeros((10,45),dtype=np.int64)],[J,f.exterior(A)]])%3
def inv(A):
 RR,piv=g.rref(np.hstack((A,np.eye(A.shape[0],dtype=np.int64))))
 assert piv==list(range(A.shape[0]))
 B=RR[:,A.shape[0]:]%3
 assert np.array_equal(A@B%3,np.eye(A.shape[0],dtype=np.int64))
 return B
C=autom(C0,CJ)
assert np.array_equal(C@C%3,np.eye(55,dtype=np.int64))
family={p:autom(U0,(J0+p[0]*L[0]+p[1]*L[1])%3) for p in product(range(3),repeat=2)}
def locate(A):
 found=[p for p,V in family.items() if np.array_equal(A,V)]
 assert len(found)==1
 return found[0]
actions={};outside=[]
for p,U in family.items():
 V=C@U@C%3
 generators={'v':V,'comm_uv':U@V@inv(U)@inv(V)%3,
             'v_uinv':V@inv(U)%3}
 row={}
 for name,G in generators.items():
  UU=G@U@inv(G)%3
  try:row[name]=locate(UU)
  except AssertionError:outside.append((p,name))
 actions[p]=row
 print('Parameters',p,'conjugation actions',row)
print('Actions outside the saved affine family:',outside)
assert not outside
seen={(0,0)};todo=[(0,0)];paths={(0,0):[]}
while todo:
 p=todo.pop(0)
 for name,q in actions[p].items():
  if q not in seen:seen.add(q);todo.append(q);paths[q]=paths[p]+[name]
print('Orbit of base parameter:',sorted(seen))
print('Orbit size:',len(seen))
out={'actions':[{ 'parameters':list(p),**{k:list(v) for k,v in row.items()}} for p,row in actions.items()],
     'base_orbit':[list(p) for p in sorted(seen)],
     'paths_from_base':[{'parameters':list(p),'successive_current_basis_conjugators':w} for p,w in paths.items()],
     'source_morphism':'u_new=g(u,v)*u*g(u,v)^-1; v_new=c*u_new*c; c fixed',
     'parameter_convention':'(h03−2,h05) overF3'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: all arithmetic matrix conjugations computed exactly.')
