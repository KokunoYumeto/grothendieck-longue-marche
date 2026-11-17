#!/usr/bin/env python3
"""Impose the gentle identities and both pure frames in the source quotient.

D=F2/(J'J^6), |F2/J|=288. J is B-normal. All identities are imposed
inside D, and A belongs to D' while beta has diagonal abelianization.
This remains a necessary finite-image computation, not a lifting theorem.
"""
import test_cm_cubic_refinement as R
T=R.T
import numpy as np,json
from pathlib import Path
nv=T.nv;jci={e:k for k,e in enumerate(T.jchords)}
def chain(q,w):
 v=np.zeros(nv,dtype=np.int16)
 for j in w:
  k=abs(j)-1
  if j>0:e=(q,k);q=int(T.jtable[q,T.jgens[k]]);sg=1
  else:q=int(T.jtable[q,T.jinverse[T.jgens[k]]]);e=(q,k);sg=-1
  if e in jci:v[jci[e]]+=sg
 return q,v
X=(1,);Y=(2,);Z=(-2,-1)
pairs=[(X,Y),(Y,X),(Z,X),(Y,Z)]
loopwords=[[T.subst(w,pair) for w in T.jloops] for pair in pairs]
for ws in loopwords:
 assert all(chain(0,w)[0]==0 for w in ws)
print('PASS J is invariant under the two marked S3 substitutions',flush=True)
cache={}
def loops(i,q):
 key=(i,q)
 if key not in cache:cache[key]=np.array([chain(q,w)[1] for w in loopwords[i]],dtype=np.int16)
 return cache[key]
expressions={'two':(1,2),'three+':(3,4,1),
             'three-':(3,T.inverse(Z),4,T.inverse(Y),1,T.inverse(X))}
def equation(base,tokens,p):
 q=0;A=np.zeros((nv,nv),dtype=np.int32);b=np.zeros(nv,dtype=np.int32)
 for token in tokens:
  if isinstance(token,tuple):q,v=chain(q,token);b+=v;continue
  i=token-1;A+=loops(i,q);q,v=chain(q,T.subst(T.jpaths[base],pairs[i]));b+=v
 if q:return None
 return A.T%p,-b%p

S=loops(1,0)
rloops=[T.subst(w,(Y,Z)) for w in T.jloops]
assert all(chain(0,w)[0]==0 for w in rloops)
RR=np.array([chain(0,w)[1] for w in rloops],dtype=np.int16)
assert np.array_equal(S@S,np.eye(nv,dtype=np.int16))
assert np.array_equal(RR@RR@RR,np.eye(nv,dtype=np.int16))
exponents={q:np.array([sum(1 if j==k else -1 if j==-k else 0 for j in T.jpaths[q])
                       for k in (1,2)],dtype=np.int16) for q in range(288)}
# The joint kernel equals the intersection of the harmonic level-12
# kernel with the abelianization-mod-3 kernel: the 288 joint residues
# are distinct under those two maps.
keys=[]
for q in range(288):
 bq,_=T.b_eval(T.subst(T.jpaths[q],(T.bx,T.by)),2)
 keys.append((bq,tuple(exponents[q]%3)))
assert len(set(keys))==288

frame_cache={}
def source_frame(base,fr,p):
 key=(base,fr['qb'],fr['qa'],fr['rho'],p)
 if key in frame_cache:return frame_cache[key]
 kb=(fr['qb'],((-fr['rho'])%3,)*2);ka=(fr['qa'],(0,0))
 if kb not in keys or ka not in keys:return None
 qb=keys.index(kb);qa=keys.index(ka)
 Ad=np.array([chain(base,w)[1] for w in T.jloops],dtype=np.int16)
 As=[];bs=[]
 for q,sub,action,is_cubic in ((qb,(Y,X),S,False),(qa,(Y,Z),RR,True)):
  t=T.jpaths[q]
  w=T.subst(t,sub)+T.inverse(t)+T.inverse(T.jpaths[base])
  end,const=chain(0,w);assert end==0
  if is_cubic:
   assert not np.any(exponents[q]%6)
   ab=T.abloops.T;desired=-exponents[q]//6%p
  else:
   diff=int(exponents[q][0]-exponents[q][1]);assert diff%6==0
   ab=(T.abloops[0]-T.abloops[1])[:,None];desired=np.array([-diff//6%p])
  matrix=np.hstack(((action-Ad)%p,ab%p))
  _,P=T.row_space_projection(matrix,p)
  As.append(P[:nv].T)
  bs.append((const@P[:nv]-desired@P[nv:])%p)
 frame_cache[key]=(np.vstack(As)%p,np.concatenate(bs)%p)
 return frame_cache[key]

records=[]
for base in sorted(T.derived):
 qf=T.Q[T.JQ[base][4]];frames=[fr for fr in T.frames if fr['qf']==qf]
 if not frames:continue
 results={};valid=True
 for p in (2,3):
  As=[];bs=[]
  for name,tokens in expressions.items():
   v=equation(base,tokens,p)
   if v is None:valid=False;break
   A,b=v;As.append(A);bs.append(b)
  if not valid:break
  # The actual five-point pentagon at the refined characteristic-three
  # target and at the original characteristic-two target.
  pent=T.expressions['pentagon']
  v=T.expression_matrix(base,pent,2) if p==2 else R.expression_matrix(base,pent)
  if v is None:valid=False;break
  A,b=v;As.append(A);bs.append(b)
  As.append(T.abloops%p);bs.append(-T.abelian_base_coordinates(base)%p)
  fixedA=np.vstack(As);fixedb=np.concatenate(bs)
  arr=[]
  for fr in frames:
   frame_result=source_frame(base,fr,p)
   if frame_result is None:arr.append((None,False));continue
   A,b=frame_result
   rank,good=T.solve_many(np.vstack((fixedA,A)),np.concatenate((fixedb,b))[:,None],p)
   arr.append((rank,bool(good[0])))
  results[p]=arr
 if not valid:continue
 for i,fr in enumerate(frames):
  if all(results[p][i][1] for p in (2,3)):
   rec=dict(fr);rec['base']=base;rec['ranks']={str(p):results[p][i][0] for p in (2,3)}
   records.append(rec);print('Full source framing survivor:',rec,flush=True)
hist={str(b):sum(r['parity']==b for r in records) for b in (0,1)}
print('Full source identities and framing census:',hist,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Necessary source-framed finite equations; no full lifting assertion',
 'source_order':'288*6^289','records':records,'parity_counts':hist},indent=2)+'\n')
