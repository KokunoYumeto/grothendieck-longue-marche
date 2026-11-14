#!/usr/bin/env python3
"""Generation certificate for the cyclic-module mixed2-then3 refinement."""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,time,sys
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
old=sys.argv;sys.argv=[str(OUT/'a_mixed_prime_cover.py'),'--module','cyclic_order3']
with redirect_stdout(io.StringIO()):G=runpy.run_path(str(OUT/'a_mixed_prime_cover.py'))
sys.argv=old
for key in ['D','Q','ix','z','vsize','identity','hs','hr','ht','hsize','rank','C','nc','P','Pt','mul','inv','conj','perm','act','order','parent','right_s','right_r']:
 globals()[key]=G[key]
qa=D['canon']((1,0,0,1));qb=D['canon']((9,8,4,9))
a=ix[qa]*vsize+1;b=ix[qb]*vsize
ss=conj(b,hs);rr=conj(a,hr);assert mul(ss,rr)==ht
im=[None]*hsize;im[identity]=identity
for h in order[1:]:
 q,g=parent[h];im[h]=mul(im[q],ss if g==hs else rr)
assert len(set(im))==hsize
assert all(im[right_s[h]]==mul(im[h],ss) and im[right_r[h]]==mul(im[h],rr) for h in range(hsize))
Mss=act(C,ss)[nc];Mt=act(C,ht)[nc]
L=np.concatenate([np.eye(rank,dtype=np.int16)-Mss,Mss-Mt],axis=1)%3
base=(P[b]-act(P[b],ss)+act(P[a]-act(P[a],rr)+act(P[hr],a),ss)-Pt)%3
rhs=-base[nc]%3
A=np.concatenate([L,rhs[:,None]],axis=1);piv=[];row=0
for col in range(2*rank):
 hits=np.flatnonzero(A[row:,col])
 if not len(hits):continue
 k=row+int(hits[0]);A[[row,k]]=A[[k,row]];A[row]=A[row]*int(A[row,col])%3
 fac=A[:,col].copy();fac[row]=0;A=(A-fac[:,None]*A[row])%3
 piv.append(col);row+=1
 if row==rank:break
assert row==rank
free=[i for i in range(2*rank) if i not in piv]
assert len(free)==rank
# At the edge labelled h the map sends the chosen edge path to its
# translate by alpha_H(h), so this is the complete twisted-equivariant map.
indices=np.array([[mul(inv[im[h]],e) for h in range(hsize)] for e in nc],dtype=np.int32)
csupport=[np.flatnonzero(C[:,j]) for j in range(rank)]
def matrix(edge):
 T=edge[indices]
 ans=np.zeros((rank,rank),dtype=np.int16)
 for j,sup in enumerate(csupport):ans[:,j]=np.sum(T[:,sup]*C[sup,j],axis=1)%3
 return ans

def rank3(B):
 A=B.copy()%3;n,m=A.shape;r=0
 for j in range(m):
  hits=np.flatnonzero(A[r:,j])
  if not len(hits):continue
  k=r+int(hits[0]);A[[r,k]]=A[[k,r]];A[r]=A[r]*int(A[r,j])%3
  factors=A[r+1:,j].copy();A[r+1:]=(A[r+1:]-factors[:,None]*A[r])%3
  r+=1
  if r==n:break
 return r
rng=np.random.default_rng(20261114);answer=None;hist={}
for trial in range(129):
 w=np.zeros(2*rank,dtype=np.int16)
 if trial:w[free]=rng.integers(0,3,rank,dtype=np.int16)
 w[piv]=(A[:,-1]-A[:,free]@w[free])%3
 assert np.array_equal(L@w%3,rhs)
 bv=C@w[:rank]%3;av=C@w[rank:]%3
 pb=(P[b]+bv)%3;pa=(P[a]+av)%3
 defect=(pb-act(pb,ss)+act(pa-act(pa,rr)+act(P[hr],a),ss)-Pt)%3
 assert not np.any(defect)
 edge=(pa-pb)%3;edge[a]=(edge[a]+1)%3
 T=matrix(edge);r=rank3(T);hist[str(r)]=hist.get(str(r),0)+1
 print('trial',trial,'kernel rank',r,'target',rank,flush=True)
 if r==rank:
  answer={'A':[1,0,0,1],'beta':[9,8,4,9],'A_H_coordinate':1,'beta_H_coordinate':0,
          'beta_L_cycle_coefficients':w[:rank].tolist(),'A_L_cycle_coefficients':w[rank:].tolist(),
          'base_automorphism':im,'kernel_rank':r,'cusp_equation_all_edges_checked':True,
          'lambda':1,'trial':trial,'H_order':hsize,'kernel_order':'3^'+str(rank),
          'quotient':'B/[L,L]L^3, with N/L the simple cyclic-order3 F2[Q] module of dimension2'}
  break
# Independent actual-word verification of the solution and its kernel matrix.
if answer is not None:
 from collections import deque
 ep={G['root']:[]};queue=deque([G['root']])
 while queue:
  vertex=queue.popleft()
  for target,e in G['adj'][vertex]:
   if target not in ep:
    ep[target]=ep[vertex]+[(e,1 if vertex[0]==0 else -1)];queue.append(target)
 def inverse_word(word):return [0 if x==0 else 3-x for x in word[::-1]]
 def inverse_path(path):return [(e,-sign) for e,sign in path[::-1]]
 def path_word(path):
  h=identity;word=[]
  assert len(path)%2==0
  for j in range(0,len(path),2):
   e,sign=path[j];f,sgn=path[j+1];assert sign==1 and sgn==-1
   if h!=e:assert right_s[h]==e;word.append(0);h=e
   if f==h:continue
   if right_r[h]==f:word.append(1)
   else:assert G['right_r2'][h]==f;word.append(2)
   h=f
  if h!=identity:assert h==hs;word.append(0)
  return word
 Lwords=[path_word(ep[G['vertex2'][e]]+[(e,1)]+inverse_path(ep[G['vertex3'][e]])) for e in nc]
 def eval_word(word):
  h=identity;v=np.zeros(hsize,dtype=np.int32)
  for letter in word:
   if letter==0:h=right_s[h]
   else:
    hh=right_r[h] if letter==1 else G['right_r2'][h]
    v[h]+=1;v[hh]-=1;h=hh
  return h,v%3
 for j,word in enumerate(Lwords):
  h,v=eval_word(word);assert h==identity and np.array_equal(v,C[:,j])
 reps={identity:[]}
 for h in order[1:]:
  q,g=parent[h];reps[h]=reps[q]+[0 if g==hs else 1]
 wa=[];wb=[]
 for j,word in enumerate(Lwords):
  wa+=word*int(w[rank+j]);wb+=word*int(w[j])
 wa+=reps[a];wb+=reps[b]
 h,v=eval_word(wa);assert h==a and np.array_equal(v,pa)
 h,v=eval_word(wb);assert h==b and np.array_equal(v,pb)
 sw=wb+[0]+inverse_word(wb);rw=wa+[1]+inverse_word(wa)
 cusp=sw+rw+[2,0]
 h,v=eval_word(cusp);assert h==identity and not np.any(v)
 hsimage,psimage=eval_word(sw);hrimage,primage=eval_word(rw)
 assert hsimage==ss and hrimage==rr
 riimage=inv[rr];priimage=-act(primage,riimage)%3
 images={0:(ss,psimage),1:(rr,primage),2:(riimage,priimage)}
 iminv=[None]*hsize
 for h,ih in enumerate(im):iminv[ih]=h
 direct=np.zeros_like(T)
 for j,word in enumerate(Lwords):
  h=identity;v=np.zeros(rank,dtype=np.int32)
  for letter in word:
   hh,pp=images[letter];v+=pp[indices[:,iminv[h]]];h=mul(h,hh)
  assert h==identity;direct[:,j]=v%3
 assert np.array_equal(direct,T)
 answer.update({'L_basis_words_checked':rank,'all_L_basis_images_checked':rank,
                'direct_cusp_word_length':len(cusp),'direct_cusp_word_identity':True,
                'module_phi_masks':['0x1860e0d6cb6b6efc923133e5a','0x1231c145bdbd87ed2d1f1a136']})
 print('Direct cusp word',len(cusp),'letters; all',rank,'basis images agree',flush=True)
summary={'found':answer is not None,'rank_histogram':hist,'tested':trial+1,
         'elapsed_seconds':round(time.time()-started,3)}
(OUT/'a_mixed_prime_generate.json').write_text(json.dumps({'summary':summary,'witness':answer},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
