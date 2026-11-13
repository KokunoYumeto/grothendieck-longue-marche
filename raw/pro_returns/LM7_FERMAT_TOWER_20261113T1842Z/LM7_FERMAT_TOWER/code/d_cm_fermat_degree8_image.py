#!/usr/bin/env python3
"""Reconstruct the exact D33 words read-only and evaluate their common image."""
from pathlib import Path
from collections import deque
from functools import lru_cache
from itertools import product
import importlib.util,json,hashlib,time
import numpy as np
import d_cm_fermat_degree8_module as R

OUT=Path(__file__).resolve().parent;OLD=R.OLD;started=time.time()
Q=R.Q;qt=R.qt;qi=R.qi;qs=int(R.states[R.hs,0]);qr=int(R.states[R.hr,0])
def inverse(w):return bytes(0 if a==0 else 3-a for a in reversed(w))
def comm(a,b):return bytes(a)+bytes(b)+inverse(a)+inverse(b)
def graph(G,mul,e,s,r):
 ix={q:i for i,q in enumerate(G)};rr=mul(r,r)
 v2={q:(0,min(q,mul(q,s))) for q in G}
 v3={q:(1,min(q,mul(q,r),mul(q,rr))) for q in G}
 adj={v:[] for v in set(v2.values())|set(v3.values())}
 for i,q in enumerate(G):adj[v2[q]].append((v3[q],i));adj[v3[q]].append((v2[q],i))
 paths={v2[e]:[]};queue=deque(paths);tree=set()
 while queue:
  v=queue.popleft()
  for w,j in adj[v]:
   if w not in paths:paths[w]=paths[v]+[(j,1 if v[0]==0 else -1)];tree.add(j);queue.append(w)
 chords=[i for i in range(len(G)) if i not in tree];words=[]
 for j in chords:
  path=paths[v2[G[j]]]+[(j,1)]+[(k,-sgn) for k,sgn in reversed(paths[v3[G[j]]])]
  q=e;w=[]
  for k in range(0,len(path),2):
   a,sgn=path[k];b,sgn2=path[k+1];assert sgn==1 and sgn2==-1;a=G[a];b=G[b]
   if q!=a:assert mul(q,s)==a;w.append(0);q=a
   if b!=q:
    if mul(q,r)==b:w.append(1)
    else:assert mul(q,rr)==b;w.append(2)
   q=b
  if q!=e:assert q==s;w.append(0)
  words.append(bytes(w))
 return words,chords,ix

Nwords,chN,ixQ=graph(list(range(576)),lambda a,b:int(qt[a,b]),qi,qs,qr)
assert len(Nwords)==97
reps={qi:b''};queue=deque([qi])
while queue:
 q=queue.popleft()
 for letter,h in [(0,qs),(1,qr)]:
  z=int(qt[q,h])
  if z not in reps:reps[z]=reps[q]+bytes([letter]);queue.append(z)
O=[]
for i,q in enumerate(Q):
 if tuple(a%2 for a in q)!=R.I:continue
 sq=R.qm(q,q)
 if tuple(a%3 for a in sq) in [(1,0,0,1),(2,0,0,2)]:O.append(i)
assert len(O)==32
q0=[min(int(qt[q,o]) for o in O) for q in range(576)];Q0=sorted(set(q0))
def m0(a,b):return q0[int(qt[a,b])]
e,s,r=q0[qi],q0[qs],q0[qr];r2=m0(r,r)
Kwords,chK,ixK=graph(Q0,m0,e,s,r)
saved=json.loads((OLD/'d_cm_rank4_refine.json').read_text())
assert [list(w) for w in Kwords]==saved['K_basis_words']
chord={j:i for i,j in enumerate(chK)}
def collapse(w):
 q=e;out=[]
 def add(j,sgn):
  i=chord.get(j)
  if i is None:return
  a=sgn*(i+1)
  if out and out[-1]==-a:out.pop()
  else:out.append(a)
 for a in w:
  if a==0:q=m0(q,s)
  else:
   h=m0(q,r if a==1 else r2);add(ixK[q],1);add(ixK[h],-1);q=h
 return q,out
for i,w in enumerate(Kwords):assert collapse(w)==(e,[i+1])
def degree2(w):
 v=z=0
 for a in w:
  i=abs(a)-1
  for k in range(4):
   if (v>>k)&1:z^=1<<(4*k+i)
  if a<0:z^=1<<(5*i)
  v^=1<<i
 return v,z
relwords=[bytes(w) for w in saved['degree2_relation_words']];rel=[]
for w in relwords:
 q,cw=collapse(w);assert q==e;v,z=degree2(cw);assert v==0;rel.append(z)
def multiply(a,b,nb):
 z=0
 while a:
  bit=a&-a;i=bit.bit_length()-1;a^=bit;bb=b
  while bb:
   bit=bb&-bb;j=bit.bit_length()-1;bb^=bit;z^=1<<(i*4**nb+j)
 return z
def bracket(a,na,b,nb):return multiply(a,b,nb)^multiply(b,a,na)
Wwords=[];basis={}
for i,j,k in product(range(9),repeat=3):
 z=bracket(rel[i],2,bracket(rel[j],2,rel[k],2),4);rem=z
 for p in sorted(basis,reverse=True):
  if (rem>>p)&1:rem^=basis[p]
 if rem:basis[rem.bit_length()-1]=rem;Wwords.append(comm(relwords[i],comm(relwords[j],relwords[k])))
assert len(Wwords)==240
def lyndon(w):return all(w<w[k:]+w[:k] for k in range(1,len(w)))
@lru_cache(None)
def lieword(w):
 if len(w)==1:return Kwords[w[0]]
 k=next(k for k in range(1,len(w)) if lyndon(w[k:]))
 return comm(lieword(w[:k]),lieword(w[k:]))
L3=[w for w in product(range(4),repeat=3) if lyndon(w)]
pairs=[(i,j) for i in range(97) for j in range(i,97)]
def nw(mask):
 return b''.join(w for i,w in enumerate(Nwords) if (mask>>i)&1)
def central(mask,power=1):
 out=[]
 while mask:
  bit=mask&-mask;i,j=pairs[bit.bit_length()-1];mask^=bit
  out.append((Nwords[i]*2 if i==j else comm(Nwords[i],Nwords[j]))*power)
 return b''.join(out)
J=json.loads((OLD/'d_cm_quadratic_search.json').read_text())['witness']
fixed=[int(v,16) for v in json.loads((OLD/'d_cm_class2_two.json').read_text())['s_centralizer_basis']]
wa=central(int(J['central_A_coefficients'],16))+nw(int(J['homology_A_cycles'],16))+reps[qi]
qb=R.ix[R.canon(J['beta'])]
wb=central(int(J['central_beta_coefficients'],16))+nw(int(J['homology_beta_cycles'],16))+reps[qb]
right=int(J['beta_right_s_centralizer_coefficients'],16)
for j,v in enumerate(fixed):
 if (right>>j)&1:wb+=nw(v)
J4=json.loads((OLD/'d_cm_exponent4.json').read_text())['witness']
wa=central(int(J4['upper_A_correction'],16),2)+central(int(J4['previous_A_central_change'],16))+wa
wb=central(int(J4['upper_beta_correction'],16),2)+central(int(J4['previous_beta_central_change'],16))+wb
namespace={'Nwords':Nwords,'Kwords':Kwords,'relwords':relwords,'Wwords':Wwords,
           'L3':L3,'lieword':lieword,'lyndon':lyndon,'wa':wa,'wb':wb}
spec=importlib.util.spec_from_file_location('read_only_d33_reconstruct',OLD/'d_cm_degree8_reconstruct.py')
reconstruct=importlib.util.module_from_spec(spec);spec.loader.exec_module(reconstruct)
words=reconstruct.joint_words(namespace)
expected=json.loads((OLD/'d_cm_degree8_reconstruct.out').read_text())
for name in ['A','beta']:
 assert hashlib.sha256(words[name]).hexdigest()==expected[name+'_sha256']
assert 2*(len(words['A'])+len(words['beta']))+4==12921196
print('D33 exact source hashes and12921196-letter cusp length verified',flush=True)
targetA=R.model(words['A']);targetB=R.model(words['beta'])
source37=json.loads((OLD/'d_cm_fermat_exponent4.json').read_text())
assert targetA[0]==R.projection[source37['summary']['A_H']]
assert targetB[0]==R.projection[source37['summary']['beta_H']]
S=(R.hs,np.zeros(R.size,dtype=np.int16));Pr=np.zeros(R.size,dtype=np.int16);Pr[0]=1;Pr[R.hr]=-1
RR=(R.hr,Pr);T=R.mm(S,RR)
ss=R.mm(R.mm(targetB,S),R.ii(targetB));rr=R.mm(R.mm(targetA,RR),R.ii(targetA))
defect=R.mm(R.mm(ss,rr),R.ii(T));assert defect[0]==0
assert R.W['contains'](defect[1][R.nc])
oldA=R.model(source37['A_word']);oldB=R.model(source37['beta_word'])
differences={}
for name,old,target in [('A',oldA,targetA),('beta',oldB,targetB)]:
 assert old[0]==target[0]
 v=(old[1]-target[1])[R.nc]%4
 differences[name]={'same_recorded_conjugator_in_common_quotient':R.W['contains'](v),
  'reduced_difference':R.W['reduce'](v).tolist()}
summary={'D33_words_reconstructed_with_matching_source_hashes':True,
 'D33_cusp_word_length':12921196,'A_H4':targetA[0],'beta_H4':targetB[0],
 'D33_cusp_defect_lies_in_exact_D9_image':True,
 'previous_J12_conjugator_comparisons':{k:v['same_recorded_conjugator_in_common_quotient'] for k,v in differences.items()},
 'scope':'Exact conjugator images in the maximal common T3 quotient. A nonzero difference does not exhaust alternative centralizer representatives.',
 'elapsed_seconds':round(time.time()-started,3)}
certificate={'summary':summary,'A_path_mod4':targetA[1].tolist(),'beta_path_mod4':targetB[1].tolist(),
 'cusp_defect_mod4':defect[1][R.nc].tolist(),'differences':differences,
 'source_A_sha256':expected['A_sha256'],'source_beta_sha256':expected['beta_sha256']}
(OUT/'d_cm_fermat_degree8_image.json').write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
