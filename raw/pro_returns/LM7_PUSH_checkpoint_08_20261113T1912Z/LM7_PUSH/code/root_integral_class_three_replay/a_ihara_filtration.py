#!/usr/bin/env python3
"""Exact lower-central/Zassenhaus filtration inside F/(N^3 gamma3N).

All calculations are finite F3 linear algebra in the BCH group N/K.
Normal closure is the invariant linear span under conjugation by x,y.
For r>=4 the Zassenhaus and lower-central subgroups coincide here,
since F has exponent9 and its commutator subgroup has exponent3.
"""
from pathlib import Path
import importlib.util,json
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
gt=json.loads((HERE/'a_ihara_gt_constraints.json').read_text())
meta=json.loads((HERE/'a_ihara_metabelian.json').read_text())

def cols(A):
 A=np.asarray(A,dtype=np.int64)%3;original=A.copy();r=0;p=[]
 for j in range(A.shape[1]):
  ids=np.flatnonzero(A[r:,j])
  if not len(ids):continue
  i=r+int(ids[0]);A[[r,i]]=A[[i,r]];A[r]=A[r]*int(A[r,j])%3
  for i in range(A.shape[0]):
   if i!=r:A[i]=(A[i]-A[i,j]*A[r])%3
  p.append(j);r+=1
  if r==A.shape[0]:break
 return original[:,p]


def mat(q):
 A,J,W=f.action(q)
 return np.block([[A,np.zeros((10,45),dtype=np.int64)],[J,W]])%3
X,Y=mat((1,0)),mat((0,1));I=np.eye(55,dtype=np.int64)

def normal(B):
 B=cols(B)
 while True:
  new=cols(np.hstack((B,X@B,Y@B)))
  if new.shape[1]==B.shape[1]:return B
  B=new

c=np.concatenate(f.literal([1,2,-1,-2]))[:,None]
H=normal(c)
assert H.shape[1]==53
fil={2:H}
for degree in range(3,14):
 H=normal(np.hstack(((X-I)@H,(Y-I)@H)))
 fil[degree]=H
 if not H.shape[1]:break
print('Lower-central dimensions:',[(i,h.shape[1]) for i,h in fil.items()])
assert fil[12].shape[1]==0 if 12 in fil else not H.shape[1]
# Full normal closure of cube generators, together with gamma3, is D3.
x3=np.concatenate(f.literal([1]*3))[:,None]
y3=np.concatenate(f.literal([2]*3))[:,None]
D3=normal(np.hstack((fil[3],x3,y3)))
D={2:I,3:D3,**{i:h for i,h in fil.items() if i>=4}}
fas=[np.array(a,dtype=np.int64) for a in gt['f_homology_representatives']]
fzs=[np.array(a,dtype=np.int64) for a in gt['f_central_representatives']]
K=np.array(gt['central_kernel'],dtype=np.int64)
base=(fas[0],fzs[0]);Jbase=np.array(gt['base_Johnson_matrix'],dtype=np.int64)
variations=[];jvars=[]
for fa,fz in zip(fas,fzs):
 variations.append(np.concatenate(f.multiply((fa,fz),f.inverse(base))))
 _,j=f.generator_images(fa,fz,7);jvars.append((j-Jbase).reshape(-1)%3)
for col in K.T:
 candidate=(fas[0],(fzs[0]+col)%3)
 variations.append(np.concatenate(f.multiply(candidate,f.inverse(base))))
 _,j=f.generator_images(*candidate,7);jvars.append((j-Jbase).reshape(-1)%3)
V=np.stack(variations,axis=1);J=np.stack(jvars,axis=1)
HH=np.array(meta['metabelian_variation_columns'],dtype=np.int64)
assert f.rank(np.vstack((V,J,HH)))==f.rank(V)
print('Full f-variation span dimension:',f.rank(V))
print('Johnson and metabelian variations are linear functions on this exact span.')
rows=[]
for degree,DD in sorted(D.items()):
 top=np.hstack((V,DD));bottom=np.hstack((J,np.zeros((450,DD.shape[1]),dtype=np.int64)))
 left=f.rank(np.vstack((top,bottom)))-f.rank(top)
 metatop=np.vstack((top,np.hstack((HH,np.zeros((25,DD.shape[1]),dtype=np.int64)))))
 invisible=f.rank(np.vstack((metatop,bottom)))-f.rank(metatop)
 row=(degree,DD.shape[1],left,invisible);rows.append(row)
 print('D degree',degree,'dimension',DD.shape[1],
       'Johnson variation with f-change in D:',left,
       'of which base-metabelian invisible:',invisible)
(HERE/'a_ihara_filtration.json').write_text(json.dumps({'dimensions':[(i,h.shape[1]) for i,h in fil.items()],
 'filtered_uncertainty':rows,'D_bases':{str(i):h.tolist() for i,h in D.items()}},indent=2)+'\n')
print('PASS')
