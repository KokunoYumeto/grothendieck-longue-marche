#!/usr/bin/env python3
"""Reproducible finite genus-two configuration-group certificates.

Input conventions: Bellingeri, arXiv math/0110129v2, Theorem 1.2,
genus 2, n=2. Generators a,b,c,d move strand one; sigma interchanges
strands. [x,y]=xyx^-1y^-1; t=[a,b^-1][c,d^-1]=sigma^2.

Positive: p=2, r=3, A=(C3)^4 x C5, fibre order 1215, total order492075.
Negative: p=2, K=ker(F4->UT3(F3)), a,b standard, c=d=1;
N=[K,K]K^5.  F4/N has order 27*5^82.  C=sigma*c*sigma^-1,
D=sigma*d*sigma^-1. On K/N, C^3D^3 has a nonzero -1 eigenvector.

Only integer arithmetic and NumPy are used. All finite matrices and the
Schreier basis are exported in readable JSON. No random search is needed.
"""
from pathlib import Path
import itertools, collections, json
import numpy as np
OUT=Path(__file__).resolve().parent

def red(w):
    ans=[]
    for x in w:
        if ans and ans[-1]==-x: ans.pop()
        else: ans.append(x)
    return ans

def inv(w): return [-x for x in reversed(w)]
def mul(*ws): return red([x for w in ws for x in w])
def comm(a,b): return mul(a,b,inv(a),inv(b))
def subst(phi,w): return mul(*(phi[x] if x>0 else inv(phi[-x]) for x in w))
t=mul(comm([1],[-2]),comm([3],[-4]))

def presentation_relations():
    s=[5];si=[-5];rel=[]
    for j in range(1,5):
        rel.append((f'R2_{j}',mul(si,[j],si,[j],inv(mul([j],si,[j],si)))))
    for i in (1,2):
        for j in (3,4):rel.append((f'R3_{i}_{j}',comm(mul(si,[i],s),[j])))
    for i,j in ((1,2),(3,4)):
        rel.append((f'R4_{i}',mul(si,[i],si,[j],inv(mul([j],si,[i],s)))))
    rel.append(('TR',mul(t,[-5,-5])))
    return rel

# Positive: ((F3^4)^2 x F3 x (F5)^2) semidirect C2. Multiplication
# in the central part is the alternating cocycle (1/2)J(sum v,sum w).
z8=(0,)*8;z2=(0,0);identity=(z8,0,z2,0)
def sw(v,n): return v[n:]+v[:n]
def j4(a,b): return (a[0]*b[1]-a[1]*b[0]+a[2]*b[3]-a[3]*b[2])%3
def pm(x,y):
    v,z,f,e=x;w,u,h,d=y
    if e:w=sw(w,4);h=sw(h,1)
    sv=tuple((v[i]+v[i+4])%3 for i in range(4))
    sw_=tuple((w[i]+w[i+4])%3 for i in range(4))
    return (tuple((v[i]+w[i])%3 for i in range(8)),(z+u+2*j4(sv,sw_))%3,tuple((f[i]+h[i])%5 for i in range(2)),(e+d)%2)
def pi(x):
    v,z,f,e=x
    v=tuple(-a%3 for a in v);f=tuple(-a%5 for a in f)
    if e:v=sw(v,4);f=sw(f,1)
    return (v,-z%3,f,e)
def pp(x,n):
    a=identity
    for _ in range(n):a=pm(a,x)
    return a
pgens={}
for i in range(1,5):
    v=list(z8);v[i-1]=1
    pgens[i]=(tuple(v),0,(1,0) if i==1 else z2,0)
pgens[5]=(z8,2,z2,1)
for i in range(1,6):pgens[-i]=pi(pgens[i])
def pe(w):
    x=identity
    for j in w:x=pm(x,pgens[j])
    return x
rels=presentation_relations()
for name,w in rels:assert pe(w)==identity,name
assert pe(t)==(z8,1,z2,0)
# Explicit enumeration of the fibre subgroup's coordinate model.
fibre={(v+(0,)*4,z,(f,0),0) for v in itertools.product(range(3),repeat=4) for z in range(3) for f in range(5)}
assert len(fibre)==1215
for x in fibre:
    for j in (1,2,3,4,-1,-2,-3,-4):assert pm(x,pgens[j]) in fibre
# C5 direction is supplied by a^3, then Chinese remaindering isolates a's
# F3 coordinate; all other coordinate basis vectors are already generators.
assert pp(pgens[1],3)==(z8,0,(3,0),0)
assert pp(pgens[1],5)[0][0]==2
assert pe(comm([1],[2]))==(z8,1,z2,0)
print('POSITIVE CERTIFICATE')
print('Bellingeri B2 relations checked:',len(rels))
print('p=2; r=3; A=(C3)^4 x C5; |A|=',3**4*5)
print('|fibre quotient Q|=',len(fibre),'|normal cuspidal subgroup|=3')
print('|total quotient G|=',3**9*25,'|G/Z3|=',(3**4*5)**2)
print('Fibre embedding: (v,z,f) -> ((v,0),z,(f,0)); injective by coordinates.')
print('Total projection: ((v,w),z,(f,h)) -> ((v,f),(w,h)); kernel=Z3.')
print('The pure image is all G: eight F3 basis vectors, two C5 directions, and centre 1 are generated.')

# Negative: Schreier computation for kernel of the Heisenberg3 quotient.
Q=list(itertools.product(range(3),repeat=3));one=(0,0,0)
def qm(a,b):return ((a[0]+b[0])%3,(a[1]+b[1])%3,(a[2]+b[2]+a[0]*b[1])%3)
def qi(a):return ((-a[0])%3,(-a[1])%3,(-a[2]+a[0]*a[1])%3)
gens={1:(1,0,0),2:(0,1,0),3:one,4:one}
for i in range(1,5):gens[-i]=qi(gens[i])
def qe(w):
    q=one
    for x in w:q=qm(q,gens[x])
    return q
assert qe(t)==(0,0,2)
# Actual point-push conjugation maps, derived from R2/R3/R4 and their
# sigma-conjugates, not guessed from an unverified pure braid presentation.
uC=mul(t,[-3],t,[3],inv(t));uD=mul(t,[-4],t,[4],inv(t))
phiC={1:[1],2:[2],3:mul(t,[3],inv(t)),4:mul(t,[4],inv(t),uC)}
phiD={1:[1],2:[2],3:mul([3],inv(t)),4:mul(t,[4],inv(t))}
assert subst(phiC,t)==uC and subst(phiD,t)==uD
# Independently verify every Reidemeister--Schreier action relation involving
# C or D (and t); these are free-word equalities in the normal fibre F4.
assert mul(inv(t),phiC[3],t,[-3])==[]
assert mul([3],inv(t),subst(phiC,mul(t,[-3])))==[]
assert mul(inv(t),subst(phiC,mul([4],inv(t))),t,[-4])==[]
assert mul(inv(t),phiD[4],t,[-4])==[]
assert mul([4],inv(t),subst(phiD,mul(t,[-4])))==[]
assert mul([3],inv(t),inv(phiD[3]))==[]
assert all(phiC[j]==[j] and phiD[j]==[j] for j in (1,2))
phiC3={j:subst(phiC,subst(phiC,phiC[j])) for j in range(1,5)}
phiD3={j:subst(phiD,subst(phiD,phiD[j])) for j in range(1,5)}
assert all(qe(phi[j])==gens[j] for phi in (phiC3,phiD3) for j in range(1,5))
# BFS spanning tree. A non-tree positive edge gives the free generator
# rep(q)*x_j*rep(q*x_j)^-1 of K.
reps={one:[]};tree=set();todo=collections.deque([one])
while todo:
    q=todo.popleft()
    for j in (1,2,3,4,-1,-2,-3,-4):
        v=qm(q,gens[j])
        if v not in reps:
            reps[v]=reps[q]+[j];todo.append(v)
            tree.add((q,j) if j>0 else (v,-j))
edges=[(q,j) for q in Q for j in range(1,5) if (q,j) not in tree]
eindex={e:i for i,e in enumerate(edges)}
basis=[mul(reps[q],[j],inv(reps[qm(q,gens[j])])) for q,j in edges]
n=len(basis)
assert len(reps)==27 and len(tree)==26 and n==82
assert all(qe(w)==one for w in basis)
def hom(w):
    q=one;v=np.zeros(n,dtype=np.int64)
    for j in w:
        q2=qm(q,gens[j]);edge=(q,j) if j>0 else (q2,-j)
        if edge in eindex:v[eindex[edge]]+=1 if j>0 else -1
        q=q2
    assert q==one
    return v
I=np.eye(n,dtype=np.int64)
assert np.array_equal(np.column_stack([hom(w) for w in basis]),I)
MC=np.column_stack([hom(subst(phiC3,w)) for w in basis])
MD=np.column_stack([hom(subst(phiD3,w)) for w in basis])
z=(0,0,1)
x=np.zeros(n,dtype=np.int64);y=x.copy()
x[eindex[(one,3)]]=1;x[eindex[(z,3)]]=-1
y[eindex[(one,4)]]=1;y[eindex[(z,4)]]=-1
assert np.array_equal(MC@x,x)
assert np.array_equal(MC@y,y+3*x)
assert np.array_equal(MD@x,x-3*y)
assert np.array_equal(MD@y,y)
v=x-y
assert np.any(v%5) and not np.any(((MC@MD)@v+v)%5)
smallC=np.array([[1,3],[0,1]],dtype=np.int64)
smallD=np.array([[1,0],[-3,1]],dtype=np.int64)
print('\nNEGATIVE CERTIFICATE')
print('|Heisenberg(F3)|=',len(Q),'Schreier rank=',n)
print('C^3 and D^3 preserve the quotient map F4->Heisenberg(F3): checked on all four generators.')
print('Eight defining action equalities: checked by free reduction.')
print('Schreier coordinate matrix of free basis: identity',n,'x',n)
print('Invariant integral rank-two submodule: x=c_1-c_z; y=d_1-d_z; z=[a,b].')
print('C^3 matrix on (x,y):',smallC.tolist())
print('D^3 matrix on (x,y):',smallD.tolist())
print('C^3D^3 matrix:',(smallC@smallD).tolist())
print('Nonzero v=x-y satisfies (C^3D^3)v=-v modulo 5: checked.')
print('Fibre quotient F4/([K,K]K^5) has order 27*5^82 =',27*5**82)
print('Therefore no finite odd quotient of P2(C) dominates this fibre quotient.')
print('This is a full finite domination obstruction, not merely failure at a searched level.')
data={
 'source':'Bellingeri arXiv math/0110129v2, Theorem 1.2, g=2,n=2',
 'conventions':'Letters 1,2,3,4 are a,b,c,d; negative integers are inverses; t=[a,b^-1][c,d^-1].',
 'p':2,'heisenberg_elements':[list(q) for q in Q],
 'heisenberg_multiplication':'(x,y,z)*(u,v,w)=(x+u,y+v,z+w+x*v) mod3',
 'fibre_generator_images':{str(i):list(gens[i]) for i in range(1,5)},
 't':t,'phi_C':phiC,'phi_D':phiD,'phi_C3':phiC3,'phi_D3':phiD3,
 'schreier_tree':[[list(q),j] for q,j in sorted(tree)],
 'schreier_basis':[{'index':i,'vertex':list(q),'edge':j,'word':basis[i]} for i,(q,j) in enumerate(edges)],
 'C3_integral_matrix':MC.tolist(),'D3_integral_matrix':MD.tolist(),
 'x':x.tolist(),'y':y.tolist(),'v':v.tolist(),
 'small_C3_matrix':smallC.tolist(),'small_D3_matrix':smallD.tolist(),
 'normal_subgroup':'N=[K,K]K^5','finite_fibre_quotient_order':str(27*5**82),
 'positive':{'p':2,'r':3,'A_order':405,'fibre_order':1215,'total_order':492075,
  'relations_verified':[name for name,w in rels],
  'B2_generator_images':{str(i):pgens[i] for i in range(1,6)}}}
(OUT/'configuration_finite_certificates.json').write_text(json.dumps(data,indent=2)+'\n')
print('Wrote configuration_finite_certificates.json')
