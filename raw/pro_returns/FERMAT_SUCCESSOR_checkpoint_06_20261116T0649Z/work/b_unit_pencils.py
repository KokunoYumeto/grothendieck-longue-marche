#!/usr/bin/env python3
"""Exact degree<=3 tripod maps from Fermat flex-line pencils.

All arithmetic is in Q(zeta3).  This is a finite test of the two
homogeneous cubic action directions, not an assertion that these
are all S-unit maps on the punctured cubic.
"""
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import ast,json
import numpy as np

def k(x=0,y=0): return (F(x),F(y))
zero=k();one=k(1);zeta=k(0,1)
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def mul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def inv(a):
 d=a[0]*a[0]-a[0]*a[1]+a[1]*a[1]
 assert d
 return ((a[0]-a[1])/d,-a[1]/d)
def dot(a,b):
 s=zero
 for x,y in zip(a,b):s=add(s,mul(x,y))
 return s
def cross(a,b):
 return tuple(add(mul(a[(i+1)%3],b[(i+2)%3]),neg(mul(a[(i+2)%3],b[(i+1)%3]))) for i in range(3))
def normalized(a):
 c=inv(next(x for x in a if x!=zero))
 return tuple(mul(x,c) for x in a)
def scale_ratio(li,lj,lk):
 # lj=alpha*li+beta*lk, so f=-(alpha/beta)*li/lk has 1-f supported on lj.
 for i,j in combinations(range(3),2):
  d=add(mul(li[i],lk[j]),neg(mul(li[j],lk[i])))
  if d==zero:continue
  alpha=mul(add(mul(lj[i],lk[j]),neg(mul(lj[j],lk[i]))),inv(d))
  beta=mul(add(mul(li[i],lj[j]),neg(mul(li[j],lj[i]))),inv(d))
  assert alpha!=zero and beta!=zero
  return neg(mul(alpha,inv(beta)))
 raise AssertionError('dependent pair')
def show(a):return [str(x) for x in a]
zetas=[one,zeta,mul(zeta,zeta)]
points=[(zero,neg(t),one) for t in zetas]+[(neg(t),zero,one) for t in zetas]
points +=[(one,neg(zetas[1]),zero),(one,neg(zetas[2]),zero),(one,neg(zetas[0]),zero)]
labels=['A0','A1','A2','B0','B1','B2','C1','C2','O']
lines={}
for i,j in combinations(range(9),2):
 l=normalized(cross(points[i],points[j]));div=tuple(int(dot(l,p)==zero) for p in points)
 assert sum(div)==3
 lines[l]=div
assert len(lines)==12
for i,p in enumerate(points):
 l=normalized(tuple(mul(x,x) for x in p));div=[0]*9;div[i]=3
 assert [j for j,q in enumerate(points) if dot(l,q)==zero]==[i]
 lines[l]=tuple(div)
assert len(lines)==21
lines=list(lines.items())

MOD=3**10
hall=[(i,j,jj) for i in range(10) for j in range(i) for jj in range(j,10)]
lookup={h:i for i,h in enumerate(hall)}
src=ast.parse(Path('deliverable/code/b_char2_symmetry.py').read_text())
exec(compile(ast.Module(body=[x for x in src.body if isinstance(x,ast.FunctionDef) and x.name=='bracket'],type_ignores=[]),'Hall','exec'))
data=np.load('work/b_arbitrary_action_analysis_matrices.npz')
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
bpairs=[(i,j) for i in range(8) for j in range(i)]
deriv=[]
for gen in range(2):
 b=data['boundary_bracket_parameters'][:,gen];Db=data['derivation_boundary'][gen]
 ad=np.zeros((330,10),dtype=np.int64)
 for n,(i,j) in enumerate(bpairs):
  for l in range(10):
   for r,s in bracket(i+2,j+2,l):ad[r,l]+=int(b[n])*s
 deriv.append(np.column_stack((-Db@U,3*Db))+3*ad)

records=[];detected=[]
for triple in combinations(range(21),3):
 li,lj,lk=[lines[i][0] for i in triple]
 if dot(li,cross(lj,lk))!=zero:continue
 di,dj,dk=[np.array(lines[i][1],dtype=np.int64) for i in triple]
 PW=np.vstack((di-dk,dj-dk))[:,:8]
 assert not np.any(PW@U%3)
 PV=np.column_stack((-PW@U//3,PW))
 L=np.zeros((2,330),dtype=np.int64)
 for col,(i,j,l) in enumerate(hall):L[:,col]=(PV[1,i]*PV[0,j]-PV[0,i]*PV[1,j])*PV[:,l]
 outputs=[L@D for D in deriv]
 record={'lines':list(triple),'divisors':[di.tolist(),dj.tolist(),dk.tolist()],
         'origin_is_boundary':len({int(di[8]),int(dj[8]),int(dk[8])})>1,
         'V_map':PV.tolist(),'derivations':[x.tolist() for x in outputs]}
 scale=scale_ratio(li,lj,lk)
 record['function']={'scale':show(scale),'numerator':[show(x) for x in li],'denominator':[show(x) for x in lk]}
 if dot(lk,points[8])!=zero:record['value_at_O']=show(mul(scale,mul(dot(li,points[8]),inv(dot(lk,points[8])))))
 if any(np.any(x) for x in outputs):
  row,col=next((i,j) for i in range(2) for j in range(10) if PV[i,j])
  scalars=[F(int(x[row,col]),int(PV[row,col])) for x in outputs]
  assert all(np.array_equal(x,np.array(PV,dtype=object)*s) for x,s in zip(outputs,scalars))
  record['inner_scalar']=[str(s) for s in scalars]
 records.append(record)
 if any(np.any(x) for x in outputs):detected.append(record)
print('Exact special lines:',len(lines),flush=True)
print('Exact three-line pencils:',len(records),flush=True)
print('Pencils detecting either deformation:',len(detected),flush=True)
for r in detected[:10]:print(r,flush=True)
Path('work/b_unit_pencils.json').write_text(json.dumps({'special_line_count':len(lines),'pencil_count':len(records),'detected_count':len(detected),'lines':[[[show(x) for x in l],list(d)] for l,d in lines],'records':records,'scope':'All three-line pencils among the12 flex secants and9 flex tangents; not all rational S-unit maps.'},indent=2)+'\n')
