#!/usr/bin/env python3
"""Actual map of the finite Fermat Ihara uncertainty into base metabelian F2.

Let K=N^3 gamma3N, N=F2^3 F2'.  The image of K in F2/F2''
has commutator coefficient ideal (X6,X3Y3,Y6,X5Y2,X2Y5) overF3,
where X=x-1,Y=y-1.  Coefficients are obtained by exact Fox derivatives
of literal Schreier words, then reduced in that ideal.  We keep only
necessary GT symmetry/hexagon constraints, not an arithmetic assertion.
"""
from pathlib import Path
import importlib.util,json,math
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
gt=json.loads((HERE/'a_ihara_gt_constraints.json').read_text())
MON=[(a,b) for a in range(6) for b in range(6)
     if not(a>=3 and b>=3) and not(a>=5 and b>=2) and not(a>=2 and b>=5)]
assert len(MON)==25


def binom(a,n):
 if n<0:return 0
 if a>=0:return math.comb(a,n) if n<=a else 0
 return (-1)**n*math.comb(n-a-1,n)


def fox_coefficient(word):
 # D_y(word) - D_y(x^a y^b) = X*h for word=c^h*x^a*y^b.
 a=b=0;dy={(i+1,j):0 for i,j in MON}
 # The constant-X coefficient must cancel for everyY.
 extra={(0,j):0 for j in range(6)}
 dy.update(extra)
 for l in word:
  if abs(l)==2:
   bb=b if l>0 else b-1;sign=1 if l>0 else -1
   for i,j in dy:dy[i,j]+=sign*binom(a,i)*binom(bb,j)
  if abs(l)==1:a+=1 if l>0 else -1
  else:b+=1 if l>0 else -1
 for i,j in dy:dy[i,j]-=binom(a,i)*binom(b,j+1)
 assert all(dy[0,j]==0 for j in range(6))
 return np.array([dy[i+1,j]%3 for i,j in MON],dtype=np.int64),(a,b)


def comm(a,b):return a+b+f.inverse_word(a)+f.inverse_word(b)
check,ab=fox_coefficient([1,2,-1,-2])
assert ab==(0,0) and check[MON.index((0,0))]==1 and np.count_nonzero(check)==1
HC=np.stack([fox_coefficient(comm(f.NWORDS[i],f.NWORDS[j]))[0] for i,j in zip(*f.UP)],axis=1)


def image(fa,fz):
 word=[]
 for a,w in zip(fa,f.NWORDS):word+=w*int(a)
 h,ab=fox_coefficient(word)
 assert ab[0]%9==0 and ab[1]%9==0
 correction=(np.asarray(fz)-2*np.outer(fa,fa)[f.UP])%3
 return (h+HC@correction)%3

fas=[np.array(a,dtype=np.int64) for a in gt['f_homology_representatives']]
fzs=[np.array(a,dtype=np.int64) for a in gt['f_central_representatives']]
K=np.array(gt['central_kernel'],dtype=np.int64)
baseJ=np.array(gt['base_Johnson_matrix'],dtype=np.int64)
baseH=image(fas[0],fzs[0])
jcols=[];hcols=[]
for fa,fz in zip(fas,fzs):
 A,J=f.generator_images(fa,fz,7)
 jcols.append((J-baseJ).reshape(-1)%3);hcols.append((image(fa,fz)-baseH)%3)
for col in K.T:
 fa=fas[0];fz=(fzs[0]+col)%3
 A,J=f.generator_images(fa,fz,7)
 jcols.append((J-baseJ).reshape(-1)%3);hcols.append((image(fa,fz)-baseH)%3)
J=np.stack(jcols,axis=1);H=np.stack(hcols,axis=1)
rj=f.rank(J);rh=f.rank(H);rp=f.rank(np.vstack((J,H)))
print('Base metabelian coefficient monomials:',MON)
print('Intrinsic central45 to base metabelian rank:',f.rank(HC))
print('Necessary GT Johnson uncertainty rank:',rj)
print('Metabelian coefficient variation rank:',rh)
print('Joint variation rank:',rp)
print('Johnson variation invisible in base metabelian quotient:',rp-rh)
for degree in range(2,13):
 ids=[i for i,(a,b) in enumerate(MON) if a+b+2<degree]
 HH=H[ids,:]
 print('Base Zassenhaus coefficients of degrees below',degree,
       'rank',f.rank(HH),'remaining Johnson uncertainty',f.rank(np.vstack((J,HH)))-f.rank(HH))
out={'commutator_coefficient_monomials':MON,'central_to_metabelian':HC.tolist(),
     'base_f_metabelian':baseH.tolist(),'metabelian_variation_columns':H.tolist(),
     'Johnson_variation_columns':J.tolist(),
     'Johnson_rank':rj,'metabelian_rank':rh,'joint_rank':rp,'invisible_Johnson_rank':rp-rh}
(HERE/'a_ihara_metabelian.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: exact comparison of the enlarged necessary-constraint set.')
