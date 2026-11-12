#!/usr/bin/env python3
"""Further exact Lie checks: kernel generators, explicit witness, elliptic dimensions."""
import json,time
import sympy as sp
from ab_lie import *

@lru_cache(None)
def kernel(n):
 ds=special(3,n)
 if n==1:return ds
 M=column_matrix([fill(D) for D in ds],2,n)
 out=[]
 for v in M.nullspace():
  out.append(tuple(lincomb(v,[D[i] for D in ds]) for i in range(3)))
 return tuple(out)

def ideal_generators(N=6):
 rows=[]
 for n in range(1,N+1):
  ds=[]
  for j in range(1,n):
   ds += [dbracket(D,K) for D in special(3,j) for K in kernel(n-j)]
  r=column_matrix(ds,3,n).rank() if ds else 0
  rows.append(dict(weight=n,kernel=len(kernel(n)),bracket_image=r,minimal_ideal_generators=len(kernel(n))-r))
  print(rows[-1],flush=True)
 return rows

def witness():
 x,y,z=map(gen,range(3));c=bracket(x,y)
 E=(bracket(bracket(y,c),x),{w:-v for w,v in bracket(bracket(x,c),y).items()},{})
 assert not add(add(E[0],E[1]),E[2])
 assert not any(fill(E))
 assert any(E)
 u,v=pointpush(1)
 assert not any(dbracket(E,u))
 ev=dbracket(E,v)
 assert ev[2]==bracket(E[0],z) and any(ev)
 pp=pointpush(3);rank=column_matrix(list(pp)+[E],3,3).rank();assert rank==3
 j=column_matrix(list(pointpush(4))+[ev],3,4).rank();assert j==4
 return dict(description='E_x=[[y,[x,y]],x], E_y=-[[x,[x,y]],y], E_z=0',
    pp3_rank=2,pp3_with_E=rank,pp4_rank=3,pp4_with_bracket_E_v=j,
    E_associative=[{''.join('xyz'[i] for i in w):str(v) for w,v in d.items()} for d in E])

def elliptic(N=12):
 rows=[]
 for n in range(1,N+1):
  l1=len(lyndon(2,n+1));l2=len(lyndon(2,n+2))
  rows.append(dict(degree=n,symplectic=2*l1-l2,outer=2*l1-l2-(n==2)))
 return rows

if __name__=='__main__':
 result={'witness':witness(),'kernel_ideal_generators':ideal_generators(),'elliptic':elliptic()}
 with open(Path(__file__).with_name('ab_kernel_results.json'),'w') as f:json.dump(result,f,indent=2)
 print(json.dumps(result,indent=2),flush=True)
