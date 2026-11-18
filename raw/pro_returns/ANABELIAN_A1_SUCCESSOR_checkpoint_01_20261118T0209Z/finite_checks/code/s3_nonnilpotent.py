"""Nonnilpotent finite relative-cuspidal test for P_2(Sigma_2).

The total quotient is specified by eight matrices in Aut(P), where P is
the free class-two exponent-five group on the rank-ten C3-cover fibre.
It is not enumerated: its 5-group-by-C3^2 structure is verified via 72
Schreier generators and their shear matrices. Twenty-two pure braid
relators are obtained from Bellingeri Theorem 1.2 by index-two rewriting.
"""
from pathlib import Path
from collections import deque
import json,itertools,time
import numpy as np

out=Path(__file__).resolve().parent;p=5;t0=time.time()
def red(w):
 a=[]
 for x in w:
  if a and a[-1]==-x:a.pop()
  else:a.append(x)
 return tuple(a)
def iv(w):return tuple(-x for x in reversed(w))
def cat(*ws):return red(x for w in ws for x in w)
def comm(a,b):return cat(a,b,iv(a),iv(b))
def sub(w,imgs):return cat(*(imgs[x-1] if x>0 else iv(imgs[-x-1]) for x in w))

# K=ker(<a,b,c,d> -> C3), with a ->1. Positive a-edges form a tree.
reps=[(),(1,),(1,1)];edges=[(s,j) for s in range(3) for j in range(1,5) if (s,j) not in [(0,1),(1,1)]]
idx={e:i for i,e in enumerate(edges)};n=len(edges);assert n==10
basis=[cat(reps[s],(j,),iv(reps[(s+(j==1))%3])) for s,j in edges]
def schreier(w):
 s=0;ans=[]
 for x in w:
  e=(s,x) if x>0 else ((s-(-x==1))%3,-x)
  if e in idx:ans.append((idx[e]+1)*(1 if x>0 else -1))
  s=(s+(1 if x==1 else -1 if x==-1 else 0))%3
 assert s==0
 return red(ans)
assert [schreier(w) for w in basis]==[(i+1,) for i in range(n)]
pair=list(itertools.combinations(range(n),2));zdim=len(pair);I=np.eye(n,dtype=np.int64)
def wedge(v,w):return np.array([(v[i]*w[j]-v[j]*w[i])%p for i,j in pair],dtype=np.int64)
def class2(w):
 v=np.zeros(n,dtype=np.int64);z=np.zeros(zdim,dtype=np.int64)
 for x in w:
  u=np.zeros(n,dtype=np.int64);u[abs(x)-1]=1 if x>0 else -1
  z=(z+3*wedge(v,u))%p;v=(v+u)%p
 return v,z
def ext(A):
 return np.array([[(A[i,k]*A[j,l]-A[i,l]*A[j,k])%p for k,l in pair] for i,j in pair],dtype=np.int64)
def mi(A):
 B=np.concatenate([A.copy()%p,np.eye(len(A),dtype=np.int64)],axis=1);d=len(A)
 for j in range(d):
  ii=next(i for i in range(j,d) if B[i,j]);B[[j,ii]]=B[[ii,j]]
  B[j]=(B[j]*pow(int(B[j,j]),-1,p))%p
  for i in range(d):
   if i!=j:B[i]=(B[i]-B[i,j]*B[j])%p
 return B[:,d:]
def rank(A):
 A=A.copy()%p;h=0
 for j in range(A.shape[1]):
  ii=next((i for i in range(h,A.shape[0]) if A[i,j]),None)
  if ii is None:continue
  A[[h,ii]]=A[[ii,h]];A[h]=(A[h]*pow(int(A[h,j]),-1,p))%p
  for i in range(A.shape[0]):
   if i!=h:A[i]=(A[i]-A[i,j]*A[h])%p
  h+=1
  if h==A.shape[0]:break
 return h

# An automorphism is (A,B,Lambda^2 A), where image of generator e_i is
# (A e_i,B e_i).  This gives an actual 55 by 55 invertible block matrix.
ident=(I,np.zeros((zdim,n),dtype=np.int64),np.eye(zdim,dtype=np.int64))
def amul(a,b):
 A,B,E=a;C,D,F=b
 return (A@C%p,(E@D+B@C)%p,E@F%p)
def ainv(a):
 A,B,E=a;C=mi(A);F=ext(C)
 return C,(-F@B@C)%p,F
def aequal(a,b):return all(np.array_equal(x,y) for x,y in zip(a,b))
def auto(imgs):
 cols=[class2(schreier(sub(w,imgs))) for w in basis]
 A=np.column_stack([a for a,b in cols]);B=np.column_stack([b for a,b in cols])
 assert rank(A)==n
 return A,B,ext(A)

letters=tuple((i,) for i in range(1,5));t=cat(comm((1,),(-2,)),comm((3,),(-4,)))
first=[tuple(cat((i,),w,(-i,)) for w in letters) for i in range(1,5)]
second=[]
for i in range(1,5):
 u=cat(t,(-i,),t,(i,),iv(t));w=cat(iv(u),t)
 imgs=list(letters);imgs[i-1]=cat(t,(i,),iv(t))
 if i%2:imgs[i]=cat(t,(i+1,),iv(t),u)
 else:imgs[i-2]=cat((i-1,),iv(t))
 for j in range(i+2 if i%2 else i+1,5):imgs[j-1]=cat(w,(j,),iv(w))
 assert sub(t,imgs)==u
 second.append(tuple(imgs))
gens=[auto(a) for a in first+second]
allg={i+1:a for i,a in enumerate(gens)};allg.update({-i:ainv(a) for i,a in list(allg.items())})
def aval(w):
 a=ident
 for j in w:a=amul(a,allg[j])
 return a

# Bellingeri g=n=2 source relators, with sigma the fifth original letter.
rel=[];sigma=(5,);si=(-5,)
for i in range(1,5):rel.append(('R2_'+str(i),cat(si,(i,),si,(i,),iv(cat((i,),si,(i,),si)))))
for i in (1,2):
 for j in (3,4):rel.append((f'R3_{i}_{j}',comm(cat(si,(i,),sigma),(j,))))
for i,j in [(1,2),(3,4)]:rel.append((f'R4_{i}',cat(si,(i,),si,(j,),iv(cat((j,),si,(i,),sigma)))))
rel.append(('TR',cat(t,(-5,-5))))
def pure(w):
 state=0;a=[]
 for j in w:
  if abs(j)!=5:a.append((abs(j)+4*state)*(1 if j>0 else -1))
  else:
   if (j>0 and state==1):a.extend(t)
   elif (j<0 and state==0):a.extend(iv(t))
   state=1-state
 assert state==0
 return red(a)
pure_rel=[]
for name,w in rel:
 for b in (False,True):
  rr=pure(cat(sigma,w,si) if b else w)
  assert aequal(aval(rr),ident),(name,b)
  pure_rel.append({'name':name+('_sigma' if b else '_1'),'word':rr,'verified':True})

# Quotient by C3 x C3 records first a and second A independently.
def deck(w):return (sum((1 if j==1 else -1 if j==-1 else 0) for j in w)%3,
                   sum((1 if j==5 else -1 if j==-5 else 0) for j in w)%3)
cosets=list(itertools.product(range(3),repeat=2));repc={s:(1,)*s[0]+(5,)*s[1] for s in cosets}
cusp=[class2(schreier(cat(reps[i],t,iv(reps[i]))))[0] for i in range(3)]
W=np.column_stack(cusp[:2]);assert rank(W)==2
assert rank(np.column_stack(cusp))==2
Hs=[];Ns=[]
for s in cosets:
 for j in range(1,9):
  dg=deck((j,));ss=((s[0]+dg[0])%3,(s[1]+dg[1])%3)
  w=cat(repc[s],(j,),iv(repc[ss]));assert deck(w)==(0,0)
  A,B,E=aval(w);N=(A-I)%p
  assert rank(np.concatenate([W,N],axis=1))==2
  assert not np.any(N@W%p)
  Ns.append(N)
  Hs.append({'coset':s,'generator':j,'word':w,'linear':A.tolist(),'central':B.tolist()})
assert all(not np.any(N@M%p) for N in Ns for M in Ns)
shear_rank=rank(np.column_stack([N.reshape(-1) for N in Ns]))

# Actual fibre quotient of order 75, nontrivial deck action on cusp part.
S=np.array([[0,4],[1,4]],dtype=np.int64);Sps=[np.eye(2,dtype=np.int64),S,S@S%p]
assert np.array_equal(Sps[-1]@S%p,np.eye(2,dtype=np.int64))
def qm(a,b):
 v,i=a;w,j=b;u=(np.array(v)+Sps[i]@np.array(w))%p
 return tuple(map(int,u)),(i+j)%3
def qi(a):
 v,i=a;j=(-i)%3;return tuple(map(int,-Sps[j]@np.array(v)%p)),j
qone=((0,0),0);qgens={1:((0,0),1),2:((1,0),0),3:qone,4:qone}
qgens.update({-i:qi(a) for i,a in list(qgens.items())})
def qval(w):
 a=qone
 for j in w:a=qm(a,qgens[j])
 return a
seen={qone};todo=deque(seen)
while todo:
 a=todo.popleft()
 for g in qgens.values():
  b=qm(a,g)
  if b not in seen:seen.add(b);todo.append(b)
assert len(seen)==75
qt=qval(t);assert qt[1]==0 and qt[0]!=(0,0)
assert rank(np.column_stack([qt[0],S@np.array(qt[0])%p]))==2
Qbasis=[qval(w) for w in basis];assert all(a[1]==0 for a in Qbasis)
lam=np.column_stack([a[0] for a in Qbasis]);assert rank(lam)==2

# Check kernel-of-inner-action criterion directly in the whole vector space:
# v -> (w |-> v wedge w) is an injective linear map (rank 10).
ad=np.column_stack([np.concatenate([wedge(I[:,i],I[:,j]) for j in range(n)]) for i in range(n)])
assert rank(ad)==10
ans={'verified':True,'p':2,'r':5,'A':'C3','source':'Bellingeri (2004), Theorem 1.2, closed oriented surface g=2,n=2',
 'fibre_quotient_order':75,'fibre_quotient':'F5^2 semidirect C3','deck_action_S':S.tolist(),
 'cusp_image_in_Q':qt,'non_nilpotent':True,'K_rank':10,'class2_group_order':'5^55',
 'ambient_total_group':'Aut(free class-two exponent-5 group on 10 generators) x C3^2',
 'total_quotient':'subgroup generated by the eight displayed automorphisms and their displayed deck coordinates',
 'total_order_form':'9*5^m for a nonnegative integer m; no group enumeration or exact m asserted',
 'basis_F4_words':basis,'K_edges':edges,'second_strand_F4_automorphisms':second,
 'automorphism_generators':[{'linear':A.tolist(),'central':B.tolist(),'deck':deck((i+1,))} for i,(A,B,E) in enumerate(gens)],
 'original_relators':rel,'pure_relators':pure_rel,'H_Schreier_generators':Hs,
 'cusp_space_W':W.tolist(),'shear_span_dimension':shear_rank,'Q_factor_map_lambda':lam.tolist(),
 'inner_action_linear_rank':10,'relations_checked':len(pure_rel),'shear_generators_checked':len(Hs),
 'shear_pair_products_checked':len(Hs)**2,'seconds':time.time()-t0}
(out/'s3_nonnilpotent.json').write_text(json.dumps(ans,indent=2)+'\n')
print('PASS: Q order75 = F5^2 semidirect C3, noncentral cusp subgroup; 22 pure braid relations.')
print('PASS:',len(Hs),'Schreier generators have shears in dimension',shear_rank,'with all pair products zero.')
print('PASS: T has order9*5^m and fibre quotient dominates Q; rank(ad)=10, rank(lambda)=2.')
print('seconds',time.time()-t0)
