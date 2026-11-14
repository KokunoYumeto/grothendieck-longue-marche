#!/usr/bin/env python3
r"""Actual Heisenberg quotient from the rational Belyi function u=-z/x.

The map u:U->P1\{0,1,infinity} has O tangent -1, whose pro3 Kummer
cocycle is zero. Thus its exact class-two map intertwines Galois actions.
The target Ihara action is scalar chi on abelianization and chi² on center,
since f_sigma is central in the target class-two quotient.
"""
from pathlib import Path
import importlib.util,json
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
gt=json.loads((HERE/'a_ihara_gt_constraints.json').read_text())
K=np.array(gt['central_kernel'],dtype=np.int64)

def cyclic_rewrite(word):
 q=0;out=[]
 for l in word:
  if abs(l)==1:
   if l>0:
    if q==2:out.append(1)
    q=(q+1)%3
   else:
    if q==0:out.append(-1)
    q=(q-1)%3
  elif q==0:out.append(2 if l>0 else -2)
 assert q==0
 return out

def collect2(word):
 a=np.zeros(2,dtype=np.int64);z=0
 for l in word:
  b=np.zeros(2,dtype=np.int64);b[abs(l)-1]=1 if l>0 else -1
  z=(z+2*(a[0]*b[1]-a[1]*b[0]))%3;a=(a+b)%3
 return a,z
vals=[collect2(cyclic_rewrite(w)) for w in f.NWORDS]
P=np.stack([a for a,z in vals],axis=1);Q=np.array([z for a,z in vals],dtype=np.int64)
omega=np.array([P[0,i]*P[1,j]-P[0,j]*P[1,i] for i,j in zip(*f.UP)],dtype=np.int64)%3
assert f.rank(P)==2 and np.any(omega)
print('Actual u-map abelian matrix:',P.tolist())
print('Actual u-map central cochain:',Q.tolist())

def solve(A,b):
 A=np.asarray(A,dtype=np.int64)%3;aug=np.column_stack((A,b%3));r=0;pv=[]
 for col in range(A.shape[1]):
  ids=np.flatnonzero(aug[r:,col])
  if not len(ids):continue
  ii=r+int(ids[0]);aug[[r,ii]]=aug[[ii,r]];aug[r]=aug[r]*int(aug[r,col])%3
  coeff=aug[:,col].copy();coeff[r]=0;aug=(aug-coeff[:,None]*aug[r])%3
  pv.append(col);r+=1
  if r==A.shape[0]:break
 if np.any(aug[r:,-1]):return None
 part=np.zeros(A.shape[1],dtype=np.int64)
 for rr,col in enumerate(pv):part[col]=aug[rr,-1]
 fr=[j for j in range(A.shape[1]) if j not in pv];kk=np.zeros((A.shape[1],len(fr)),dtype=np.int64)
 for ii,j in enumerate(fr):
  kk[j,ii]=1
  for rr,col in enumerate(pv):kk[col,ii]=-aug[rr,j]%3
 return part,kk,r

def autom(im):
 vals=[]
 for w in f.NWORDS:
  ww=[]
  for l in w:ww+=im[l] if l>0 else f.inverse_word(im[-l])
  vals.append(f.literal(ww))
 A=np.stack([a for a,z in vals],axis=1);J=np.stack([z for a,z in vals],axis=1)
 return A,J,f.exterior(A)
SA,SJ,SW=autom({1:[2],2:[1]})
Pv=P@SA%3;Qv=(Q@SA+omega@SJ)%3;ov=omega@SW%3
TA,TJ,TW=autom({1:[1],2:[1]*4+[-2]+[1]*4})
Pw=P@TA%3;Qw=(Q@TA+omega@TJ)%3;ow=omega@TW%3
print('v-map abelian matrix:',Pv.tolist())
print('v-map central cochain:',Qv.tolist())
print('w-map abelian matrix:',Pw.tolist())
print('w-map central cochain:',Qw.tolist())
# The actual rational function a=(1-u)/(1-zeta*u) fills u=zeta and infinity.
# In the cyclic cover basis A=x³,B_i=x^i y x^-i, the infinity relation is
# B1 B2 A B0.  Take A=target_y, B0=target_x, B1=1, B2=(A B0)^-1.
def cross_rewrite(word):
 q=0;out=[];bb={0:[1],1:[],2:[-1,-2]}
 for l in word:
  if abs(l)==1:
   if l>0:
    if q==2:out.append(2)
    q=(q+1)%3
   else:
    if q==0:out.append(-2)
    q=(q-1)%3
  else:out+=bb[q] if l>0 else f.inverse_word(bb[q])
 assert q==0
 return out
cv=[collect2(cross_rewrite(w)) for w in f.NWORDS]
Pc=np.stack([a for a,z in cv],axis=1);Qc=np.array([z for a,z in cv],dtype=np.int64)
oc=np.array([Pc[0,i]*Pc[1,j]-Pc[0,j]*Pc[1,i] for i,j in zip(*f.UP)],dtype=np.int64)%3
assert collect2(cross_rewrite([-2,-1]*3))[1]==0
print('Cross-ratio map abelian matrix:',Pc.tolist())
print('Cross-ratio map central cochain:',Qc.tolist())
solutions=[]
for branch,(aa,zz) in enumerate(zip(gt['f_homology_representatives'],gt['f_central_representatives'])):
 fa=np.array(aa,dtype=np.int64);fz=np.array(zz,dtype=np.int64)
 U,J=f.generator_images(fa,fz,7)
 assert np.array_equal(P@U%3,P)
 print('v raw compatibility row:',((ov@J+Qv@U-Qv)%3).tolist(),'Pvx:',Pv[0].tolist())
 print('w raw compatibility row:',((ow@J+Qw@U-Qw)%3).tolist())
 assert np.array_equal(Pc@U%3,Pc)
 base=np.concatenate(((omega@J+Q@U-Q)%3,(oc@J+Qc@U-Qc)%3))
 columns=[]
 for col in K.T:
  _,JJ=f.generator_images(fa,(fz+col)%3,7)
  columns.append(np.concatenate((omega@(JJ-J)%3,oc@(JJ-J)%3)))
 mat=np.stack(columns,axis=1)
 sol=solve(mat,-base)
 print('GT branch',branch,'new equation rank',f.rank(mat),'compatible',sol is not None)
 if sol is None:continue
 pp,kk,rr=sol
 zz=(fz+K@pp)%3;_,jj=f.generator_images(fa,zz,7)
 assert not np.any((omega@jj+Q@U-Q)%3)
 js=[]
 for col in kk.T:
  _,jnew=f.generator_images(fa,(zz+K@col)%3,7)
  js.append((jnew-jj).reshape(-1)%3)
 js=np.stack(js,axis=1) if js else np.zeros((450,0),dtype=np.int64)
 print('Johnson variation surviving this actual cover:',f.rank(js))
 solutions.append({'fa':fa.tolist(),'fz':zz.tolist(),'J':jj.tolist(),'parameter_kernel':kk.tolist(),
                   'Johnson_variations':js.tolist()})
assert solutions
base=np.array(solutions[0]['J'],dtype=np.int64)
var=[np.array(r['Johnson_variations'],dtype=np.int64) for r in solutions]
var += [(np.array(r['J'],dtype=np.int64)-base).reshape(-1,1)%3 for r in solutions]
print('Total Johnson uncertainty after actual u-cover:',f.rank(np.hstack(var)))
(HERE/'a_ihara_heisenberg.json').write_text(json.dumps({'P':P.tolist(),'Q':Q.tolist(),'omega':omega.tolist(),
 'solutions':solutions},indent=2)+'\n')
print('PASS: the additional condition comes from the specified rational map, not an unspecified GT lift.')
