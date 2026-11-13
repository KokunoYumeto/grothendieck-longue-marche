#!/usr/bin/env python3
"""The exact congruence/Fermat12 fibre-product quotient of C2*C3."""
from pathlib import Path
from collections import deque
import json,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
I=(1,0,0,1);S=(0,1,11,0);R=(0,11,1,11)
def qm(a,b):
 v=((a[0]*b[0]+a[1]*b[2])%12,(a[0]*b[1]+a[1]*b[3])%12,
    (a[2]*b[0]+a[3]*b[2])%12,(a[2]*b[1]+a[3]*b[3])%12)
 return min(v,tuple(-x%12 for x in v))
def canon(a):return min(a,tuple(-x%12 for x in a))
S=canon(S);R=canon(R)
def lm(a,b):
 return (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
         a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3])
LS=(0,1,1,0);LR=(0,-1,1,-1)
Qset={I};todo=[I];linear={I:I}
for q in todo:
 for g,L in [(S,LS),(R,LR)]:
  h=qm(q,g);M=lm(linear[q],L)
  if h in Qset:assert linear[h]==M
  else:Qset.add(h);todo.append(h);linear[h]=M
Q=sorted(Qset);assert len(Q)==576
ix={q:i for i,q in enumerate(Q)};qi=ix[I];qs=ix[S];qr=ix[R]
qt=np.array([[ix[qm(a,b)] for b in Q] for a in Q],dtype=np.int16)
LM=np.array([linear[q] for q in Q],dtype=np.int16).reshape((576,2,2))
assert len({tuple(m.ravel()) for m in LM})==6
n=12
states=[(qi,0,0)];lookup={(qi,0,0):0};parent=[None]
for h,(q,a,b) in enumerate(states):
 for letter,qq,aa,bb in [(0,int(qt[q,qs]),a,b),
                         (1,int(qt[q,qr]),(a+int(LM[q,0,0]))%n,(b+int(LM[q,1,0]))%n)]:
  key=(qq,aa,bb)
  if key not in lookup:lookup[key]=len(states);states.append(key);parent.append((h,letter))
assert len(states)==6912
hs=lookup[(qs,0,0)];hr=lookup[(qr,1,0)];ident=0
def mul(a,b):
 q,u,v=states[a];qq,x,y=states[b];M=LM[q]
 return lookup[(int(qt[q,qq]),(u+int(M[0,0])*x+int(M[0,1])*y)%n,
                (v+int(M[1,0])*x+int(M[1,1])*y)%n)]
assert mul(hs,hs)==ident and mul(mul(hr,hr),hr)==ident
right_s=np.array([mul(h,hs) for h in range(len(states))],dtype=np.int32)
right_r=np.array([mul(h,hr) for h in range(len(states))],dtype=np.int32)
right_r2=right_r[right_r]
ht=mul(hs,hr)
q=ht;order=1
while q:order+=1;q=mul(q,ht)
assert order==24
kernel=[(a,b) for q,a,b in states if q==qi]
assert sorted(kernel)==[(a,b) for a in range(0,12,2) for b in range(0,12,2) if (a+b)%3==0]
assert len(kernel)==12
assert len({(q,a%4,b%4) for q,a,b in states})==2304
assert len({(q,a%3,b%3) for q,a,b in states})==1728
# Source-to-affine formulas for x=t^-2 and y=sxs are checked exactly.
def inv(a):
 q,u,v=states[a]
 qinv=ix[canon((Q[q][3],-Q[q][1]%12,-Q[q][2]%12,Q[q][0]))]
 M=LM[qinv]
 return lookup[(qinv,(-int(M[0,0])*u-int(M[0,1])*v)%n,
                (-int(M[1,0])*u-int(M[1,1])*v)%n)]
x=inv(mul(ht,ht));y=mul(mul(hs,x),hs)
assert states[x][1:]==(1,0) and states[y][1:]==(0,1)
# The Bass--Serre graph and its exact integral free homology basis.
v2=[(0,min(h,int(right_s[h]))) for h in range(len(states))]
v3=[(1,min(h,int(right_r[h]),int(right_r2[h]))) for h in range(len(states))]
vertices=sorted(set(v2)|set(v3));vi={v:i for i,v in enumerate(vertices)}
adj=[[] for v in vertices]
for h in range(len(states)):
 a=vi[v2[h]];b=vi[v3[h]];adj[a].append((b,h,1));adj[b].append((a,h,-1))
root=vi[v2[0]];paths={root:[]};queue=deque([root]);tree=set()
while queue:
 a=queue.popleft()
 for b,h,sign in adj[a]:
  if b not in paths:paths[b]=paths[a]+[(h,sign)];tree.add(h);queue.append(b)
assert len(vertices)==5760 and len(paths)==len(vertices)
chords=[h for h in range(len(states)) if h not in tree]
assert len(chords)==1153
cycle=[]
for h in chords:
 d={}
 for e,sign in paths[vi[v2[h]]]+[(h,1)]+[(e,-sign) for e,sign in paths[vi[v3[h]]]]:
  d[e]=d.get(e,0)+sign
 cycle.append([(e,a) for e,a in sorted(d.items()) if a])
assert all(dict(c).get(chords[j])==1 and all(dict(c).get(e,0)==0 for e in chords if e!=chords[j]) for j,c in enumerate(cycle))
# Every candidate starts with the exact recorded Q conjugator pairs.
Fq=[q for q in Q if tuple(x%2 for x in q)==I]
CA=[q for q in Fq if qm(q,R)==qm(R,q)]
CB=[q for q in Fq if qm(q,S)==qm(S,q)]
assert len(CA)==6 and len(CB)==8
fibres={q:[] for q in range(576)}
for h,(q,a,b) in enumerate(states):fibres[q].append(h)
def conjugate(a,b):return mul(mul(a,b),inv(a))
candidates=[]
for a0 in CA:
 for b0 in CB:
  good=[]
  for a in fibres[ix[a0]]:
   rr=conjugate(a,hr)
   for b in fibres[ix[b0]]:
    ss=conjugate(b,hs)
    if mul(ss,rr)!=ht:continue
    # Images differ only by a crossed homomorphism of the six-element S3.
    ds=np.array(states[ss][1:])-np.array(states[hs][1:])
    dr=np.array(states[rr][1:])-np.array(states[hr][1:])
    ds%=n;dr%=n
    coc={I:np.zeros(2,dtype=np.int16)};linq=[I]
    for l in linq:
     M=np.array(l,dtype=np.int16).reshape(2,2)
     for g,v in [(LS,ds),(LR,dr)]:
      ll=lm(l,g);vv=(coc[l]+M@v)%n
      if ll in coc:assert np.array_equal(coc[ll],vv)
      else:coc[ll]=vv;linq.append(ll)
    assert len(coc)==6
    images=[lookup[(q,(u+int(coc[linear[Q[q]]][0]))%n,(v+int(coc[linear[Q[q]]][1]))%n)] for q,u,v in states]
    assert len(set(images))==len(states)
    assert all(images[right_s[h]]==mul(images[h],ss) and images[right_r[h]]==mul(images[h],rr) for h in range(len(states)))
    good.append({'A':a,'beta':b,'s_image':ss,'r_image':rr,
                 'linear_S3_cocycle':{','.join(map(str,k)):v.tolist() for k,v in coc.items()}})
  candidates.append({'A_Q':list(a0),'beta_Q':list(b0),'lifts':good})
summary={'Q_order':576,'joint_Fermat12_order':len(states),'kernel_over_Q_order':len(kernel),
 'kernel_over_Q_description':'{(a,b) mod12: a,b even and a+b=0 mod3} = C2^2 x C3',
 'joint_Fermat4_order':2304,'joint_Fermat3_order':1728,
 'free_kernel_rank':1153,'cusp_order':24,'matrix_pairs':48,
 'pairs_with_base_automorphism':sum(bool(r['lifts']) for r in candidates),
 'all_base_automorphism_candidates':sum(len(r['lifts']) for r in candidates),
 'all_generator_relations_and_generation_checked':True,
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_fermat_joint_base.json').write_text(json.dumps({'summary':summary,'Q':Q,
 'Q_linear_matrices':LM.tolist(),'states':states,'identity':0,'s':hs,'r':hr,'t':ht,
 'right_s':right_s.tolist(),'right_r':right_r.tolist(),'parent':parent,
 'cycle_chords':chords,'integral_cycle_columns':cycle,'candidate_conjugators':candidates},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
