#!/usr/bin/env python3
"""Evaluate the two marked elliptic cover actions of the actual J12 shadow."""
from pathlib import Path
from collections import deque
import json,time
import numpy as np

OUT=Path(__file__).resolve().parent;started=time.time()
J=json.loads((OUT/'d_cm_fermat_exponent4.json').read_text())
OLD=OUT if (OUT/'d_cm_elliptic_pair.json').exists() else OUT.parent.parent/'LM7_FERMAT_TOWER'/'code'
G=json.loads((OLD/'d_cm_elliptic_pair.json').read_text())
LS=(0,1,1,0);LR=(0,-1,1,-1);I=(1,0,0,1)
def mm(a,b):return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
Q=[I];ix={I:0}
for q in Q:
 for h in [LS,LR]:
  t=mm(q,h)
  if t not in ix:ix[t]=len(Q);Q.append(t)
assert len(Q)==6
rs=[ix[mm(q,LS)] for q in Q];rr=[ix[mm(q,LR)] for q in Q];rr2=[rr[rr[i]] for i in range(6)]
v2=[(0,min(q,rs[q])) for q in range(6)]
v3=[(1,min(q,rr[q],rr2[q])) for q in range(6)]
vertices=sorted(set(v2)|set(v3));vi={v:i for i,v in enumerate(vertices)};adj=[[] for v in vertices]
for e in range(6):
 a,b=vi[v2[e]],vi[v3[e]];adj[a].append((b,e));adj[b].append((a,e))
root=vi[v2[0]];seen={root};queue=deque([root]);tree=set()
while queue:
 a=queue.popleft()
 for b,e in adj[a]:
  if b not in seen:seen.add(b);queue.append(b);tree.add(e)
chords=[e for e in range(6) if e not in tree];ci={e:i+1 for i,e in enumerate(chords)}
assert len(chords)==2
def red(w):
 out=[]
 for a in w:
  if out and out[-1]==-a:out.pop()
  else:out.append(a)
 return out
def inv(w):return [-a for a in reversed(w)]
def collapse(word):
 q=0;out=[]
 for a in word:
  if a==0:q=rs[q]
  else:
   h=rr[q] if a==1 else rr2[q]
   if q in ci:out.append(ci[q])
   if h in ci:out.append(-ci[h])
   q=h
 return q,red(out)
x=[2,0,2,0];y=[0]+x+[0]
qx,fx=collapse(x);qy,fy=collapse(y);assert qx==qy==0
images={1:fx,2:fy,-1:inv(fx),-2:inv(fy)}
queue=deque([([],[])]);known={():[]};inverses={}
while queue and len(inverses)<2:
 w,im=queue.popleft()
 if im in [[1],[2]]:inverses[im[0]]=w
 assert len(w)<=12
 for a in [1,2,-1,-2]:
  if w and w[-1]==-a:continue
  v=red(im+images[a]);key=tuple(v)
  if key not in known:known[key]=w+[a];queue.append((w+[a],v))
assert len(inverses)==2
for a in [1,2]:
 im=[]
 for b in inverses[a]:im=red(im+images[b])
 assert im==[a]
def to_F(word):
 q,ww=collapse(word);assert q==0;out=[]
 for a in ww:out.extend(inverses[a] if a>0 else inv(inverses[-a]))
 return red(out)
Bw=J['beta_word'];bF=to_F(Bw)
bab=[sum(1 if a==i else -1 if a==-i else 0 for a in bF) for i in [1,2]]
assert bab==J['summary']['beta_integral_F_abelianization']
k=J['summary']['Ihara_gauge_exponent']
fF=red(([2]*k if k>=0 else [-2]*(-k))+[2 if a==1 else 1 if a==2 else -2 if a==-1 else -1 for a in bF]
        +inv(bF)+([-1]*k if k>=0 else [1]*(-k)))
# This is s(x^k beta)s (x^k beta)^-1 in the exact x,y basis.
assert [sum(1 if a==i else -1 if a==-i else 0 for a in fF) for i in [1,2]]==[0,0]

def cyclic_chain(n,word):
 q=0;v=np.zeros((n,2),dtype=np.int64)
 for a in word:
  if a>0:v[q,a-1]+=1;q=(q+1)%n
  else:q=(q-1)%n;v[q,-a-1]-=1
 return q,v
def coords(n,word):
 q,v=cyclic_chain(n,word);assert q==0
 return np.concatenate([[v[n-1,0]],v[:,1]])
def power(M,k,mod):
 if k<0:k%=mod*12
 ans=np.eye(M.shape[0],dtype=np.int64)
 while k:
  if k&1:ans=ans@M%mod
  M=M@M%mod;k//=2
 return ans

records={}
for n,mod in [(3,4),(4,3),(12,12)]:
 cv=G['covers'][str(n)];D=np.array(cv['D'],dtype=np.int64)
 P=np.array(cv['P'],dtype=np.int64);S=np.array(cv['J'],dtype=np.int64)
 fv=coords(n,fF)%mod
 H=np.eye(n+1,dtype=np.int64);delta=(D-np.eye(n+1,dtype=np.int64))@fv%mod
 for j in range(n):H[:,j+1]=(H[:,j+1]+power(D,j,mod)@delta)%mod
 compact=P@H@S%mod
 # Independent direct substitution of every Schreier generator.
 yimage=inv(fF)+[2]+fF
 subst={1:[1],-1:[-1],2:yimage,-2:inv(yimage)}
 direct=[]
 for word in cv['basis']:
  w=[]
  for a in word:w.extend(subst[a])
  direct.append(coords(n,w)%mod)
 direct=np.stack(direct,axis=1)
 assert np.array_equal(H%mod,direct)
 cusp=np.array(cv['cusp'],dtype=np.int64)
 assert not np.any(P@H@cusp%mod)
 dc=np.array(cv['Dc'],dtype=np.int64)
 assert not np.any((compact@dc-dc@compact)%mod)
 records[str(n)]={'coefficient_modulus':mod,'f_Schreier_coordinates':fv.tolist(),
  'punctured_homology_action':H.tolist(),'compact_action':compact.tolist(),
  'all_Schreier_images_directly_checked':True}

E3=np.array(records['3']['compact_action']);D3=np.array(G['covers']['3']['Dc'])
units3=[]
for sign in [1,-1]:
 for a in range(3):
  if np.array_equal(E3%4,sign*power(D3,a,4)%4):units3.append((sign,a))
assert len(units3)==1;sign3,tau=units3[0]
E4=np.array(records['4']['compact_action']);D4=np.array(G['covers']['4']['Dc'])
units4=[a for a in range(4) if np.array_equal(E4%3,power(D4,a,3))]
assert len(units4)==1;ell4=units4[0]
# The cover projections are actual reductions of the single C12 action.
H12=np.array(records['12']['compact_action'])
for n,mod in [(3,4),(4,3)]:
 M=np.array(G['cover12_maps'][str(n)]['compact_homology_matrix'])
 assert not np.any((M@H12-np.array(records[str(n)]['compact_action'])@M)%mod)
summary={'B_to_F_free_basis_map':{'x':fx,'y':fy,'inverse_chord_basis':inverses},
 'beta_F_word_length':len(bF),'gauged_f_F_word_length':len(fF),
 'beta_F_abelianization':bab,'Ihara_gauge_exponent':k,
 'cubic_compact_Tate4_matrix':E3.tolist(),
 'cubic_Teichmueller_exponent':tau,'cubic_normalized_sign':sign3,
 'quartic_compact_Tate3_matrix':E4.tolist(),'quartic_i_exponent':ell4,
 'quartic_projective_i_exponent':ell4%2,
 'arithmetic_cover_graph_relation_holds':(int(sign3==-1)==ell4%2),
 'LM2_retained_CM3_sign':1,'LM2_retained_CM4_projective_i_exponent':1,
 'all_three_compact_cover_actions_and_projection_maps_checked':True,
 'scope':'Actual compact-cover evaluations of the finite shadow; no full GT0 naturality with fixed-fibre coordinates is inferred.',
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_fermat_cover_matrices.json').write_text(json.dumps({'summary':summary,'covers':records},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
