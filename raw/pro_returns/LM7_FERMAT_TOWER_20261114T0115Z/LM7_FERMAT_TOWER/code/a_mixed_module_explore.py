#!/usr/bin/env python3
"""Exact small Q-module quotients of the rank97 relation module, over F2."""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json
import numpy as np
OUT=Path(__file__).resolve().parent
with redirect_stdout(io.StringIO()):D=runpy.run_path(str(OUT/'d_cm_shadow.py'))
Q,ix,qs,qr=D['Q'],D['ix'],D['qs'],D['qr'];d=97
chords=[i for i in range(len(Q)) if i not in D['tree']]
C=np.array([[int(bool(c>>i&1)) for c in D['cycles']] for i in range(len(Q))],dtype=np.int16)
M={}
for q in (qs,qr):
 T=np.zeros_like(C);T[np.array(D['all_left'][ix[q]],dtype=int)]=C
 M[q]=T[chords]
def nullbits(rows,n):
 basis={}
 for v in rows:
  while v:
   j=v.bit_length()-1
   if j not in basis:basis[j]=v;break
   v^=basis[j]
 ans=[]
 for j in range(n):
  if j in basis:continue
  v=1<<j
  for k in sorted(basis):
   if (v&basis[k]).bit_count()%2:v^=1<<k
  assert all((v&r).bit_count()%2==0 for r in rows)
  ans.append(v)
 return ans
representations={
 'trivial':([ [1] ],[ [1] ]),
 'cyclic_order3':([[1,0],[0,1]],[[0,1],[1,1]]),
 'symmetric_order6':([[0,1],[1,0]],[[0,1],[1,1]])}
res={}
for name,(s,r) in representations.items():
 k=len(s);rows=[]
 for q,V in [(qs,s),(qr,r)]:
  for a in range(k):
   for j in range(d):
    v=sum(1<<(a*d+i) for i in range(d) if M[q][i,j])
    for b in range(k):
     if V[a][b]:v^=1<<(b*d+j)
    rows.append(v)
 basis=nullbits(rows,k*d)
 matrices=[]
 for b in basis:
  A=np.array([[(b>>(a*d+i))&1 for i in range(d)] for a in range(k)],dtype=np.int16)
  assert np.array_equal(A@M[qs]%2,np.array(s)@A%2)
  assert np.array_equal(A@M[qr]%2,np.array(r)@A%2)
  matrices.append(A.tolist())
 res[name]={'dimension':k,'Hom_Q_dimension':len(basis),'S':s,'R':r,'basis':matrices}
 print(name,'dimension',k,'Hom_Q dimension',len(basis),flush=True)
(OUT/'a_mixed_module_explore.json').write_text(json.dumps(res,indent=2)+'\n')
