#!/usr/bin/env python3
"""Complete finite gentle equations through class ten, weight-nine stratum.

In the exponent-101 class-ten quotient of F2, write log(f)=f9+f10.
The simplified finite hexagons are exactly linear in these two terms.
We solve every coefficient and project the solutions to f9, independently
checking equality with the special invariant space used in de_pentagon9.
"""
from contextlib import redirect_stdout
from functools import cache
from itertools import product
from pathlib import Path
import io,json,runpy,time
import numpy as np

here=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_pentagon9.py'))
p=d['p'];add,br,scale=d['add'],d['br'],d['scale'];x,y=d['x'],d['y'];split=d['split']
z=add(d['z'],scale(br(x,y),-pow(2,-1,p)))
def trunc(q):return {w:c for w,c in q.items() if len(w)<=10}
@cache
def evaluate(w,mode):
    if len(w)==1:return ((x,y),(y,x),(z,x),(y,z))[mode][w[0]]
    k=split(w);return trunc(br(evaluate(w[:k],mode),evaluate(w[k:],mode)))
W9=d['W'];W10=[w for w in product((0,1),repeat=10) if d['lyndon'](w)]
assert len(W10)==99;rows=list(product((0,1),repeat=9))+list(product((0,1),repeat=10))
columns=[];start=time.time()
for w in W9+W10:
    f=evaluate(w,0);anti=add(f,evaluate(w,1));cycle=add(add(f,evaluate(w,2)),evaluate(w,3))
    columns.append([anti.get(v,0) for v in rows]+[cycle.get(v,0) for v in rows])
A=np.array(columns,dtype=np.int64).T;K=d['null'](A);first=K[:56];rr,pp=d['rref'](first)
rank=len(pp);image=first[:,pp]
assert rank==4 and len(d['rref'](np.column_stack((image,d['basis'])))[1])==4
# For each of the four special vectors retain an explicit degree-ten correction.
corrections=[]
for j in range(4):
    rhs=-(A[:,:56]@d['basis'][:,j])%p;RR,piv=d['rref'](np.column_stack((A[:,56:],rhs)))
    assert 99 not in piv;sol=np.zeros(99,dtype=np.int64);sol[piv]=RR[:len(piv),-1]
    assert not np.any((A[:,:56]@d['basis'][:,j]+A[:,56:]@sol)%p);corrections.append(sol)
corrections=np.stack(corrections,axis=1)
phi9=d['basis']@d['kernel'][:,0]%p;phi10=corrections@d['kernel'][:,0]%p
assert not np.any(A@np.concatenate((phi9,phi10))%p)
np.savez_compressed(here/'de_gentle_weight9_certificate.npz',hexagon_matrix=A,all_solutions=K,degree9_basis=d['basis'],degree10_corrections=corrections)
out={'prime':p,'pure_nilpotency_class':10,'f_minimum_weight':9,'weight9_variables':56,'weight10_variables':99,
     'hexagon_matrix_shape':list(A.shape),'hexagon_solution_dimension':K.shape[1],
     'weight9_leading_image_dimension':rank,'weight9_metabelian_image_dimension':2,
     'pentagon_test_pure_class':9,'pentagon_leading_subspace_dimension':1,'pentagon_metabelian_image_dimension':1,
     'all_four_weight10_corrections_verified':True,'elapsed_seconds':round(time.time()-start,3),
     'degree10_corrections_lyndon':[{''.join('xy'[a] for a in w):int(corrections[i,j]) for i,w in enumerate(W10) if corrections[i,j]} for j in range(4)],
     'gamma_shadow_log_f9':{''.join('xy'[a] for a in w):int(phi9[i]) for i,w in enumerate(W9) if phi9[i]},
     'gamma_shadow_log_f10':{''.join('xy'[a] for a in w):int(phi10[i]) for i,w in enumerate(W10) if phi10[i]},
     'scope':'Complete finite gentle weight-nine stratum at pure class10, compared with the well-defined pentagon equation in pure class9 on four strands. This does not enumerate all multipliers or lower-weight strata, and makes no cofinality assertion.'}
(here/'de_gentle_weight9.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if not isinstance(v,(dict,)) and k!='degree10_corrections_lyndon'},indent=2),flush=True)
