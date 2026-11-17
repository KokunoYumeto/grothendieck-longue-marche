#!/usr/bin/env python3
"""Add the actual order-three primitive equation to finite framed shadows.

This equation is necessary for genuine GT. Its implication from a single
finite pentagon test is not asserted; the output preserves that scope.
"""
import check_cubic_centralizer_homology as C
R=C.R;T=C.T
import numpy as np
from pathlib import Path
import json

def braid_matrix(w):
 U=(1,1,0,1);L=(1,0,2,1);gs=(U,L,U);out=R.I
 for j in w:out=R.mul(out,gs[j-1] if j>0 else R.inv(gs[-j-1]))
 return out

def homology_action(w):
 images=[C.comb(C.concat(w,g,C.inverse(w))) for g in C.generators]
 M2=np.array([[sum(1 if j==k else -1 if j==-k else 0 for j in u)%2
               for u in images] for k in range(1,6)],dtype=np.int16)
 iw=C.inverse(w)
 iimages=[C.comb(C.concat(iw,g,w)) for g in C.generators]
 Mi=np.array([[sum(1 if j==k else -1 if j==-k else 0 for j in u)%2
               for u in iimages] for k in range(1,6)],dtype=np.int16)
 assert np.array_equal(M2@Mi%2,np.eye(5,dtype=np.int16))
 d3=braid_matrix(w)
 def dq(q):return R.idx[R.mul(R.mul(d3,R.Q[q]),R.inv(d3))]
 def chiout(ch):
  v=np.array([(ch>>j)&1 for j in range(5)],dtype=np.int16)
  return sum(int(x)<<j for j,x in enumerate(v@Mi%2))
 M=np.zeros((114,114),dtype=np.int16)
 for ch in range(32):
  ch2=chiout(ch);rows=[]
  for q in range(24):
   for u in images:
    _,v=R.chain((0,dq(q)),u,ch2);rows.append(v)
  block=C.cycles[ch]@np.array(rows,dtype=np.int16)@C.proj[ch2]%3
  a,b=C.offsets[ch],C.offsets[ch2]
  M[a:a+len(C.cycles[ch]),b:b+len(C.cycles[ch2])]=block
 return M

Ma2=homology_action((1,1));Ma2b=homology_action((1,1,2))
assert np.array_equal(homology_action(C.d),C.M)
F2=np.array([C.h1(w) for w in T.mappedloops[4]],dtype=np.int16)
F3=np.array([C.h1(w) for w in T.mappedloops[1]],dtype=np.int16)
# E_d=Ad(a^2)(F2^-1) Ad(a^2 b)(F2 F3^-1) Ad(d)(F3).
Elinear=(-F2@Ma2+F2@Ma2b-F3@Ma2b+F3@C.M)%3
Econstraint=(Elinear@C.coker).T%3
frames=[fr for fr in T.frames if fr['rho']==0 and fr['T_R_power']==0]
As=[];bs=[]
for name,tokens in T.expressions.items():
 A,b=R.expression_matrix(0,tokens);As.append(A);bs.append(b)
As.append(T.abloops%3);bs.append(-T.abelian_base_coordinates(0)%3)
fixedA=np.vstack(As);fixedb=np.concatenate(bs)
records=[]
for fr in frames:
 Af,bf=T.frame_equations(0,fr,3)
 kappa=int(fr['T_sign']==-1)
 q=(26*kappa,0);w=C.bpaths[q]
 obstruction=C.h1(C.concat(C.subst(w,C.dgen),C.inverse(w)))@C.coker%3
 A=np.vstack((fixedA,Af,Econstraint));b=np.concatenate((fixedb,bf,-obstruction%3))
 rank,good=T.solve_many(A,b[:,None],3)
 rec={'rho':0,'T_sign':fr['T_sign'],'W_power':fr['W_power'],
      'parity':fr['parity'],'rank':rank,'consistent':bool(good[0])}
 records.append(rec);print('Cubic primitive constraint:',rec,flush=True)
out={'scope':'Necessary genuine-GT cubic primitive equation, not yet derived from finite pentagon alone',
     'target_order':'768*3^114','rho':0,'records':records}
np.savez_compressed(Path(__file__).with_suffix('.npz'),Elinear=Elinear,Econstraint=Econstraint)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
