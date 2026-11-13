#!/usr/bin/env python3
"""Gauge test for the remaining intrinsic Johnson uncertainty.

Only exact mod3 coordinate changes fixing complex conjugation and the
actual O cusp generator are allowed. A positive result identifies the
precise morphism; a negative result is reported as a remaining obstruction.
"""
from pathlib import Path
import importlib.util,json
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
meta=json.loads((HERE/'a_ihara_metabelian.json').read_text())
gt=json.loads((HERE/'a_ihara_gt_constraints.json').read_text())
fas=[np.array(a,dtype=np.int64) for a in gt['f_homology_representatives']]
fzs=[np.array(a,dtype=np.int64) for a in gt['f_central_representatives']]
U,_=f.generator_images(fas[0],fzs[0],7)
C,_=f.generator_images(np.zeros(10,dtype=np.int64),np.zeros(45,dtype=np.int64),8)
WU,WC=f.exterior(U),f.exterior(C)
I10=np.eye(10,dtype=np.int64);I45=np.eye(45,dtype=np.int64)
dU=(np.kron(WU,I10)-np.kron(I45,U.T))%3
dC=(np.kron(WC,I10)-np.kron(I45,C.T))%3
eO=f.CUSP_VECTORS[:,0]%3
fixO=np.kron(I45,eO[None,:])%3

def rref(A):
 A=np.asarray(A,dtype=np.int64).copy()%3;r=0;p=[]
 for j in range(A.shape[1]):
  ids=np.flatnonzero(A[r:,j])
  if not len(ids):continue
  ii=r+int(ids[0]);A[[r,ii]]=A[[ii,r]];A[r]=A[r]*int(A[r,j])%3
  coeff=A[:,j].copy();coeff[r]=0
  A=(A-coeff[:,None]*A[r][None,:])%3
  p.append(j);r+=1
  if r==A.shape[0]:break
 return A,p

def kernel(A):
 RR,p=rref(A);free=[j for j in range(A.shape[1]) if j not in p]
 K=np.zeros((A.shape[1],len(free)),dtype=np.int64)
 for kk,j in enumerate(free):
  K[j,kk]=1
  for rr,col in enumerate(p):K[col,kk]=-RR[rr,j]%3
 assert not np.any(A@K%3)
 return K

K=kernel(np.vstack((dC,fixO)))
D=dU@K%3
J=np.array(meta['Johnson_variation_columns'],dtype=np.int64)
H=np.array(meta['metabelian_variation_columns'],dtype=np.int64)
blind=J@kernel(H)%3
print('Allowed coordinate-change dimension:',K.shape[1])
print('Allowed gauge image rank:',f.rank(D))
print('Total Johnson variation rank:',f.rank(J))
print('Total variation modulo allowed gauge:',f.rank(np.hstack((D,J)))-f.rank(D))
print('Metabelian-invisible Johnson variation rank:',f.rank(blind))
print('Metabelian-invisible variation modulo allowed gauge:',f.rank(np.hstack((D,blind)))-f.rank(D))
fil=json.loads((HERE/'a_ihara_filtration.json').read_text())
base=(fas[0],fzs[0]);vcols=[]
for fa,fz in zip(fas,fzs):vcols.append(np.concatenate(f.multiply((fa,fz),f.inverse(base))))
cent=np.array(gt['central_kernel'],dtype=np.int64)
for col in cent.T:vcols.append(np.concatenate(f.multiply((fas[0],(fzs[0]+col)%3),f.inverse(base))))
VV=np.stack(vcols,axis=1)
for degree in (5,6,7,8,9):
 DD=np.array(fil['D_bases'][str(degree)],dtype=np.int64)
 top=np.vstack((np.hstack((VV,DD)),np.hstack((H,np.zeros((25,DD.shape[1]),dtype=np.int64)))))
 kk=kernel(top)
 blindfiltered=J@kk[:J.shape[1],:]%3
 print('Invisible variations in D',degree,'rank',f.rank(blindfiltered),
       'modulo allowed gauge',f.rank(np.hstack((D,blindfiltered)))-f.rank(D))
print('PASS (finite coordinate-change comparison only)')
