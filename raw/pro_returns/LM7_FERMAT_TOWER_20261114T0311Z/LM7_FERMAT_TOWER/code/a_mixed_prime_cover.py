#!/usr/bin/env python3
"""Mixed-prime finite refinements of B=C2*C3 -> Q=PSL2(Z/12).

For every tested simple F2[Q]-quotient V of Nab/2, form H=B/L with
N/L=V. Test all lifts of the CM conjugator pairs to H and the complete
linear cusp obstruction in B/[L,L]L^3. No choice of N-homology action is
fixed. A zero obstruction is not by itself called a generating lift.
"""
from pathlib import Path
from contextlib import redirect_stdout
from collections import deque
import io,runpy,json,time,sys
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):X=runpy.run_path(str(OUT/'a_mixed_module_explore.py'))
D=X['D'];Q,ix,qs,qr,one,qm=D['Q'],D['ix'],D['qs'],D['qr'],D['one'],D['qm'];z=ix[one]
d=97;chords=X['chords'];results=[]
selected=None
if '--module' in sys.argv:
 selected=sys.argv[sys.argv.index('--module')+1]
 assert selected in X['res']
def null3(A):
 A=A.copy()%3;n,m=A.shape;row=0;piv=[]
 for col in range(m):
  hits=np.flatnonzero(A[row:,col])
  if not len(hits):continue
  k=row+int(hits[0]);A[[row,k]]=A[[k,row]]
  A[row]=A[row]*int(A[row,col])%3
  fac=A[:,col].copy();fac[row]=0
  A=(A-fac[:,None]*A[row])%3;piv.append(col);row+=1
  if row==n:break
 ans=[]
 for j in range(m):
  if j in piv:continue
  v=np.zeros(m,dtype=np.int16);v[j]=1
  for k,col in enumerate(piv):v[col]=-A[k,j]%3
  ans.append(v)
 return np.array(ans,dtype=np.int16).reshape((-1,m))
for name,data in X['res'].items():
 if selected is not None and name!=selected:continue
 k=data['dimension'];vsize=2**k
 phi=np.array(data['basis'][0],dtype=np.int16)
 S=np.array(data['S'],dtype=np.int16);R=np.array(data['R'],dtype=np.int16)
 Vq={one:np.eye(k,dtype=np.int16)};todo=deque([one])
 while todo:
  q=todo.popleft()
  for g,Vg in ((qs,S),(qr,R)):
   qq=qm(q,g);A=Vq[q]@Vg%2
   if qq in Vq:assert np.array_equal(Vq[qq],A)
   else:Vq[qq]=A;todo.append(qq)
 edge_phi=[0]*len(Q)
 for j,e in enumerate(chords):edge_phi[e]=sum(int(phi[a,j])<<a for a in range(k))
 def fedge(bits,perm=None):
  value=0
  while bits:
   b=bits&-bits;e=b.bit_length()-1
   value^=edge_phi[e if perm is None else perm[e]];bits^=b
  return value
 fp={q:fedge(D['P'][q]) for q in Q}
 va={q:[sum(int((Vq[q]@np.array([(a>>i)&1 for i in range(k)],dtype=np.int16)%2)[j])<<j for j in range(k)) for a in range(vsize)] for q in Q}
 dc={}
 def delta(q,r):
  key=(q,r)
  if key not in dc:dc[key]=fp[q]^fedge(D['P'][r],D['all_left'][ix[q]])^fp[qm(q,r)]
  return dc[key]
 def mul(a,b):
  q,u=Q[a//vsize],a%vsize;r,v=Q[b//vsize],b%vsize
  return ix[qm(q,r)]*vsize+(u^va[q][v]^delta(q,r))
 hsize=len(Q)*vsize;identity=z*vsize;hs=ix[qs]*vsize;hr=ix[qr]*vsize;hr2=mul(hr,hr)
 assert mul(hs,hs)==identity and mul(hr2,hr)==identity
 inv=[]
 for h in range(hsize):
  qi=D['canon'](D['inv'](Q[h//vsize]));cands=[ix[qi]*vsize+v for v in range(vsize)]
  inv.append(next(x for x in cands if mul(h,x)==identity))
 def conj(a,b):return mul(mul(a,b),inv[a])
 right_s=[mul(h,hs) for h in range(hsize)];right_r=[mul(h,hr) for h in range(hsize)];right_r2=[mul(h,hr2) for h in range(hsize)]
 parent={identity:None};order=[identity];P=np.zeros((hsize,hsize),dtype=np.int16)
 for h in order:
  for g,trans in ((hs,right_s),(hr,right_r)):
   hh=trans[h]
   if hh not in parent:
    parent[hh]=(h,g);order.append(hh);P[hh]=P[h]
    if g==hr:P[hh,h]+=1;P[hh,hh]-=1
 assert len(order)==hsize
 vertex2=[(0,min(h,right_s[h])) for h in range(hsize)]
 vertex3=[(1,min(h,right_r[h],right_r2[h])) for h in range(hsize)]
 vertices=set(vertex2)|set(vertex3);adj={v:[] for v in vertices}
 for h in range(hsize):adj[vertex2[h]].append((vertex3[h],h));adj[vertex3[h]].append((vertex2[h],h))
 root=vertex2[identity];paths={root:np.zeros(hsize,dtype=np.int16)};queue=deque([root]);tree=set()
 while queue:
  v=queue.popleft()
  for w,e in adj[v]:
   if w not in paths:
    paths[w]=paths[v].copy();paths[w][e]+=1 if v[0]==0 else -1
    tree.add(e);queue.append(w)
 nc=[h for h in range(hsize) if h not in tree];rank=len(nc);assert rank==hsize//6+1
 C=np.zeros((hsize,rank),dtype=np.int16)
 for i,h in enumerate(nc):C[:,i]=paths[vertex2[h]]-paths[vertex3[h]];C[h,i]+=1
 assert np.array_equal(C[nc],np.eye(rank,dtype=np.int16))
 C%=3;leftcache={}
 def perm(h):
  if h not in leftcache:leftcache[h]=np.array([mul(h,x) for x in range(hsize)],dtype=np.int32)
  return leftcache[h]
 def act(vec,h):
  ans=np.zeros_like(vec);ans[perm(h)]=vec;return ans
 Ms=act(C,hs)[nc];Mr=act(C,hr)[nc]
 dual=null3(np.concatenate([(Ms-np.eye(rank,dtype=np.int16)).T,(Mr-np.eye(rank,dtype=np.int16)).T],axis=0))
 assert not np.any(dual@(Ms-np.eye(rank,dtype=np.int16))%3)
 assert not np.any(dual@(Mr-np.eye(rank,dtype=np.int16))%3)
 ht=mul(hs,hr);Pt=act(P[hr],hs);pair_records=[]
 def finite_auto(ss,rr):
  image=[None]*hsize;image[identity]=identity
  for h in order[1:]:
   a,g=parent[h];image[h]=mul(image[a],ss if g==hs else rr)
  for h in range(hsize):
   if image[right_s[h]]!=mul(image[h],ss) or image[right_r[h]]!=mul(image[h],rr):return False
  return len(set(image))==hsize
 for rec in D['records']:
  qa=D['canon'](tuple(rec['A']));qb=D['canon'](tuple(rec['beta']));lifts=[]
  for av in range(vsize):
   a=ix[qa]*vsize+av;rr=conj(a,hr)
   for bv in range(vsize):
    b=ix[qb]*vsize+bv;ss=conj(b,hs)
    if mul(ss,rr)!=ht:continue
    is_auto=finite_auto(ss,rr)
    if not is_auto:continue
    dr=(P[a]-act(P[a],rr)+act(P[hr],a))%3
    ds=(P[b]-act(P[b],ss))%3
    defect=(ds+act(dr,ss)-Pt)%3
    # Exact integral graph cycle, not an arbitrary edge chain.
    assert np.array_equal(C@defect[nc]%3,defect)
    ob=(dual@defect[nc])%3
    lifts.append({'A_kernel_coordinate':av,'beta_kernel_coordinate':bv,
                  'automorphism_H':True,'linear_lift_exists':not np.any(ob),
                  'obstruction':ob.tolist()})
  pair_records.append({'A':rec['A'],'beta':rec['beta'],'missing_CM_coset':rec['missing_coset'],'lifts':lifts})
 summary={'module':name,'V_dimension':k,'H_order':hsize,'L_rank':rank,
          'central_cover_obstruction_dimension':int(dual.shape[0]),
          'CM_pairs_tested':len(pair_records),
          'CM_pairs_with_H_automorphism':sum(bool(r['lifts']) for r in pair_records),
          'CM_pairs_with_linear_J_lift':sum(any(x['linear_lift_exists'] for x in r['lifts']) for r in pair_records),
          'extra_CM_pairs_with_linear_J_lift':sum(r['missing_CM_coset'] and any(x['linear_lift_exists'] for x in r['lifts']) for r in pair_records),
          'scope':'All H-lifts of matrix conjugators; a zero linear obstruction does not assert generation on the L/3 kernel.'}
 print(json.dumps(summary,indent=2),flush=True)
 results.append({'summary':summary,'pairs':pair_records})
(OUT/('a_mixed_prime_cover'+('_'+selected if selected else '')+'.json')).write_text(json.dumps({'results':results,'elapsed_seconds':round(time.time()-started,3)},indent=2)+'\n')
print('elapsed',round(time.time()-started,3),flush=True)
