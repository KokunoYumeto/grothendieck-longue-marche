#!/usr/bin/env python3
"""First new rank4 Zassenhaus refinement beyond the N-class-two tower.

K=ker(B->Q/O2(Q)) is free rank4; N is its index32 subgroup.
N lies in D2(K), hence gamma3N lies in D6(K). The quotient
B/D7(K) has a690-dimensional degree6 restricted Lie layer.
First test corrections represented by actual gamma3N words,
which preserve the complete D29 class-two quotient.
"""
from pathlib import Path
from collections import deque
from contextlib import redirect_stdout
from functools import lru_cache
from itertools import product
import io,runpy,json,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):D=runpy.run_path(str(OUT/'d_cm_shadow.py'))
Q,qm,one,qs,qr=D['Q'],D['qm'],D['one'],D['qs'],D['qr'];qr2=qm(qr,qr)
def inverse(w):return [0 if a==0 else 3-a for a in w[::-1]]
def comm(a,b):return a+b+inverse(a)+inverse(b)

def graph_basis(G,mul,e,s,r):
 ix={q:i for i,q in enumerate(G)};rr=mul(r,r)
 v2={q:('s',min(q,mul(q,s))) for q in G}
 v3={q:('r',min(q,mul(q,r),mul(q,rr))) for q in G}
 adj={v:[] for v in set(v2.values())|set(v3.values())}
 for i,q in enumerate(G):adj[v2[q]].append((v3[q],i));adj[v3[q]].append((v2[q],i))
 root=v2[e];paths={root:[]};queue=deque([root]);tree=set()
 while queue:
  v=queue.popleft()
  for w,j in adj[v]:
   if w not in paths:
    paths[w]=paths[v]+[(j,1 if v[0]=='s' else -1)];tree.add(j);queue.append(w)
 chords=[i for i in range(len(G)) if i not in tree]
 cycles=[paths[v2[G[i]]]+[(i,1)]+[(j,-sgn) for j,sgn in paths[v3[G[i]]][::-1]] for i in chords]
 words=[];C=np.zeros((len(G),len(chords)),dtype=np.int16)
 for col,path in enumerate(cycles):
  q=e;word=[]
  for j,sgn in path:C[j,col]+=sgn
  for j in range(0,len(path),2):
   aa,sgn=path[j];bb,sgn2=path[j+1];assert sgn==1 and sgn2==-1
   a,b=G[aa],G[bb]
   if q!=a:assert mul(q,s)==a;word.append(0);q=a
   if b==q:continue
   if mul(q,r)==b:word.append(1)
   else:assert mul(q,rr)==b;word.append(2)
   q=b
  if q!=e:assert q==s;word.append(0)
  words.append(word)
 assert np.array_equal(C[chords],np.eye(len(chords),dtype=np.int16))
 return words,C,chords,ix
Nwords,CN,chN,ixQ=graph_basis(Q,qm,one,qs,qr);assert len(Nwords)==97
reps={one:[]};queue=deque([one])
while queue:
 q=queue.popleft()
 for a,g in ((0,qs),(1,qr)):
  qq=qm(q,g)
  if qq not in reps:reps[qq]=reps[q]+[a];queue.append(qq)
O=[]
for q in D['H']:
 a=D['red'](D['flift'](q),3)
 sq=((a[0]*a[0]+a[1]*a[2])%3,(a[0]*a[1]+a[1]*a[3])%3,
     (a[2]*a[0]+a[3]*a[2])%3,(a[2]*a[1]+a[3]*a[3])%3)
 if sq in ((1,0,0,1),(2,0,0,2)):O.append(q)
assert len(O)==32
q0={q:min(qm(q,o) for o in O) for q in Q};Q0=sorted(set(q0.values()));assert len(Q0)==18
def m0(a,b):return q0[qm(a,b)]
e,s,r=q0[one],q0[qs],q0[qr];r2=m0(r,r)
Kwords,C,chords,ix=graph_basis(Q0,m0,e,s,r);assert len(Kwords)==4
chord={j:i for i,j in enumerate(chords)}
def collapse(word):
 q=e;ans=[]
 def append(j,sgn):
  i=chord.get(j)
  if i is None:return
  a=sgn*(i+1)
  if ans and ans[-1]==-a:ans.pop()
  else:ans.append(a)
 for a in word:
  if a==0:q=m0(q,s)
  else:
   qq=m0(q,r if a==1 else r2);append(ix[q],1);append(ix[qq],-1);q=qq
 return q,ans
for i,w in enumerate(Kwords):assert collapse(w)==(e,[i+1])
def poly(word,degree=6):
 P=[np.zeros(4**n,dtype=np.uint8) for n in range(degree+1)];P[0][0]=1
 for a in word:
  i=abs(a)-1
  for n in (range(degree,0,-1) if a>0 else range(1,degree+1)):
   P[n][i::4]^=P[n-1]
 return P
def bitpoly(a):return int.from_bytes(np.packbits(a,bitorder='little').tobytes(),'little')
def arraypoly(a,n):return np.unpackbits(np.frombuffer(a.to_bytes((4**n+7)//8,'little'),dtype=np.uint8),bitorder='little')[:4**n]
q,t6word=collapse([0,1]*6);assert q==e
t6poly=poly(t6word);assert t6poly[1].any()
q,t48word=collapse([0,1]*48);assert q==e
assert all(not p.any() for p in poly(t48word)[1:])
def mulpoly(a,b,nb):
 ans=0
 while a:
  bit=a&-a;i=bit.bit_length()-1;a^=bit;bb=b
  while bb:
   bbit=bb&-bb;j=bbit.bit_length()-1;bb^=bbit;ans^=1<<(i*4**nb+j)
 return ans
def bracket(a,na,b,nb):return mulpoly(a,b,nb)^mulpoly(b,a,na)
def echelon(columns):
 bas={}
 for j,v in enumerate(columns):
  w=1<<j
  while v:
   k=v.bit_length()-1
   if k not in bas:bas[k]=(v,w);break
   v^=bas[k][0];w^=bas[k][1]
 return bas
def solve(v,bas):
 w=0
 while v:
  k=v.bit_length()-1
  if k not in bas:return False,w,v
  v^=bas[k][0];w^=bas[k][1]
 return True,w,0
M={}
for q in Q0:
 tmp=np.zeros_like(C);tmp[[ix[m0(q,a)] for a in Q0]]=C;M[q]=tmp[chords]%2
def action(v,m):
 a=arraypoly(v,6).reshape((4,)*6).astype(np.int16)
 for axis in range(6):a=np.moveaxis(np.tensordot(m,a,axes=(1,axis)),0,axis)%2
 return bitpoly(a.reshape(-1).astype(np.uint8))
MS,MSR=M[s],M[m0(s,r)]

# Degree2 relations are read from the actual97 N basis words.
rel=[];relwords=[];rb={}
for w in Nwords:
 q,cw=collapse(w);assert q==e;P=poly(cw,2);assert not np.any(P[1])
 z=bitpoly(P[2]);rem=z
 for k in sorted(rb,reverse=True):
  if (rem>>k)&1:rem^=rb[k]
 if rem:rb[rem.bit_length()-1]=rem;rel.append(z);relwords.append(w)
assert len(rel)==9
W=[];Wwords=[];wbasis={}
for i,j,k in product(range(9),repeat=3):
 z=bracket(rel[i],2,bracket(rel[j],2,rel[k],2),4);rem=z
 for pivot in sorted(wbasis,reverse=True):
  if (rem>>pivot)&1:rem^=wbasis[pivot]
 if rem:
  wbasis[rem.bit_length()-1]=rem;W.append(z);Wwords.append(comm(relwords[i],comm(relwords[j],relwords[k])))
assert len(echelon(W))==len(W)

def lyndon(w):return all(w<w[k:]+w[:k] for k in range(1,len(w)))
@lru_cache(None)
def lie(w):
 if len(w)==1:return 1<<w[0]
 k=next(k for k in range(1,len(w)) if lyndon(w[k:]))
 return bracket(lie(w[:k]),k,lie(w[k:]),len(w)-k)
@lru_cache(None)
def lieword(w):
 if len(w)==1:return Kwords[w[0]]
 k=next(k for k in range(1,len(w)) if lyndon(w[k:]))
 return comm(lieword(w[:k]),lieword(w[k:]))
L6=[w for w in product(range(4),repeat=6) if lyndon(w)]
L3=[w for w in product(range(4),repeat=3) if lyndon(w)]
Z=[lie(w) for w in L6]+[mulpoly(lie(w),lie(w),3) for w in L3]
Zwords=[lieword(w) for w in L6]+[lieword(w)*2 for w in L3]
assert len(L6)==670 and len(L3)==20 and len(echelon(Z))==690
for w in W:assert solve(w,echelon(Z))[0]

# Reconstruct the exact D29 Z/4 certificate without rerunning its solvers.
pairs=[(i,j) for i in range(97) for j in range(i,97)];cdim=4753
def nw(mask):
 ans=[]
 for i,w in enumerate(Nwords):
  if (mask>>i)&1:ans+=w
 return ans
def central(mask,power=1):
 ans=[]
 while mask:
  b=mask&-mask;i,j=pairs[b.bit_length()-1]
  ans+=(Nwords[i]*2 if i==j else comm(Nwords[i],Nwords[j]))*power;mask^=b
 return ans
J=json.loads((OUT/'d_cm_quadratic_search.json').read_text())['witness']
fixed=[int(x,16) for x in json.loads((OUT/'d_cm_class2_two.json').read_text())['s_centralizer_basis']]
wa=central(int(J['central_A_coefficients'],16))+nw(int(J['homology_A_cycles'],16))+reps[D['canon'](tuple(J['A']))]
wb=central(int(J['central_beta_coefficients'],16))+nw(int(J['homology_beta_cycles'],16))+reps[D['canon'](tuple(J['beta']))]
right=int(J['beta_right_s_centralizer_coefficients'],16)
for j,v in enumerate(fixed):
 if (right>>j)&1:wb+=nw(v)
wa27,wb27=wa.copy(),wb.copy()
J4=json.loads((OUT/'d_cm_exponent4.json').read_text())['witness']
wa=central(int(J4['upper_A_correction'],16),2)+central(int(J4['previous_A_central_change'],16))+wa
wb=central(int(J4['upper_beta_correction'],16),2)+central(int(J4['previous_beta_central_change'],16))+wb
lam=J4['lambda_mod288'];assert lam==1
cusp=wb+[0]+inverse(wb)+wa+[1]+inverse(wa)+[2,0]*lam
q,cw=collapse(cusp);assert q==e
P=poly(cw);assert all(not np.any(P[n]) for n in range(1,6))
target=bitpoly(P[6]);assert solve(target,echelon(W))[0]
print('Rank4 quotient:',len(Q0),'degree6 layer:',len(Z),'gamma3N degree6:',len(W),flush=True)

def test(basis):
 S=[action(w,MS) for w in basis];SR=[action(w,MSR) for w in basis]
 cols=[w^v for w,v in zip(basis,S)]+[v^z for v,z in zip(S,SR)]
 bas=echelon(cols);good,sol,rem=solve(target,bas)
 return {'rank':len(bas),'dimension':len(basis),'solvable':good,'solution':sol,'remainder':rem}
small=test(W);large=test(Z)
print('gamma3N corrections:',small['solvable'],'rank',small['rank'],flush=True)
print('all degree6 corrections:',large['solvable'],'rank',large['rank'],flush=True)
witness=None
if small['solvable'] or large['solvable']:
 chosen=small if small['solvable'] else large;BW=Wwords if small['solvable'] else Zwords;n=len(BW)
 sol=chosen['solution'];bb=sol&((1<<n)-1);aa=sol>>n
 cb=[];ca=[]
 for i,w in enumerate(BW):
  if (bb>>i)&1:cb+=w
  if (aa>>i)&1:ca+=w
 waa=ca+wa;wbb=cb+wb
 final=wbb+[0]+inverse(wbb)+waa+[1]+inverse(waa)+[2,0]*lam
 q,cwf=collapse(final);assert q==e;PP=poly(cwf)
 assert all(not np.any(PP[n]) for n in range(1,7))
 witness={'compatible_with_D29_class2':small['solvable'],'beta_correction':hex(bb),'A_correction':hex(aa),
  'basis':'gamma3N triples' if small['solvable'] else 'restricted Lyndon degree6',
  'corrected_B_word_length':len(final),'collapsed_K_word_length':len(cwf),
  'direct_full_degree6_Magnus_identity_checked':True}
summary={'Q0_order':18,'K_rank':4,'N_index_in_K':32,'degree2_relation_rank':9,
 'restricted_degree6_dimension':690,'gamma3N_leading_dimension':len(W),
 'fixed_gamma3N_corrections_lift':small['solvable'],'gamma3N_correction_rank':small['rank'],
 'fixed_full_degree6_corrections_lift':large['solvable'],'full_correction_rank':large['rank'],
 'finite_quotient_order':'18 * 2^998 = 576 * 2^993',
 't6_degree1_mask':hex(bitpoly(t6poly[1])),
 'cusp_order_both_D6_and_D7':48,
 'scope':'Only the stated fixed-conjugator corrections are tested; failure does not exclude all same-action conjugators or the CM pair.',
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_rank4_refine.json').write_text(json.dumps({'summary':summary,'witness':witness,
 'K_basis_words':Kwords,'degree2_relation_words':relwords,
 'gamma3N_correction_obstruction':hex(small['remainder']),
 'full_correction_obstruction':hex(large['remainder'])},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
