#!/usr/bin/env python3
"""Literal C3*C3 extension of the nine-point three-division torus.

This computes the actual quotient E/(Pi' Pi^3), of order 3^13,
through its faithful graph-chain representation.  It exhausts all
27 lower residues for centralizers and order-three lifting.  It is
not a census of gentle elements or a finite mapping-class normalizer.
"""
from pathlib import Path
from itertools import product
from collections import deque
import json
import numpy as np

OUT=Path(__file__).with_suffix('')
Q=list(product(range(3),repeat=3)); qi={x:i for i,x in enumerate(Q)}
one=(0,0,0); u=(1,0,0); v=(0,1,0)
def mul(a,b):
    i,j,k=a; I,J,K=b
    return ((i+I)%3,(j+J)%3,(k+K+i*J)%3)
def inv(a):
    i,j,k=a
    return (-i%3,-j%3,(-k+i*j)%3)
def pw(a,n):
    z=one
    for _ in range(n):z=mul(z,a)
    return z
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
c=inv(mul(u,v)); x=mul(v,inv(u)); y=mul(mul(u,v),inv(pw(u,2)))
assert all(pw(g,3)==one for g in Q)
assert len({mul(pw(x,i),pw(y,j)) for i in range(3) for j in range(3)})==9
H={g for g in Q if (g[0]+g[1])%3==0}
assert {mul(pw(x,i),pw(y,j)) for i in range(3) for j in range(3)}==H
assert mul(mul(u,x),inv(u))==y
assert mul(mul(u,y),inv(u))==inv(mul(x,y))

def normal(w):
    a=[]
    for g,n in w:
        n%=3
        if not n:continue
        if a and a[-1][0]==g:
            n=(a.pop()[1]+n)%3
        if n:a.append((g,n))
    return tuple(a)
def wi(w):return tuple((g,-n) for g,n in reversed(w))
U=(('u',1),);V=(('v',1),)
X=normal(V+wi(U));Y=normal(U+V+wi(U)*2);C=normal(wi(U+V))
assert normal(U+X+wi(U))==Y
assert normal(U+Y+wi(U))==normal(wi(X+Y))
assert normal(C*3)==normal(X+Y+wi(X)+wi(Y))
assert normal((U+V)*3)==normal(Y+X+wi(Y)+wi(X))
print('PASS literal free-product identities; c^3=[x,y], Ad(u)=(y,(xy)^-1)')

def cosets(a):
    A=[one,a,pw(a,2)]
    reps=sorted({min(mul(g,h) for h in A) for g in Q})
    idx={q:i for i,q in enumerate(reps)}
    return reps,{g:idx[min(mul(g,h) for h in A)] for g in Q}
vu,iu=cosets(u);vv,iv=cosets(v);vc,ic=cosets(c)
boundary=np.zeros((18,27),dtype=np.int64)
for j,g in enumerate(Q):boundary[iu[g],j]=-1;boundary[9+iv[g],j]=1
def rref(a):
    a=np.array(a,dtype=np.int64,copy=True)%3;r=0;piv=[]
    for j in range(a.shape[1]):
        z=next((i for i in range(r,a.shape[0]) if a[i,j]),None)
        if z is None:continue
        a[[r,z]]=a[[z,r]];a[r]=a[r]*int(a[r,j])%3
        for i in range(a.shape[0]):
            if i!=r and a[i,j]:a[i]=(a[i]-a[i,j]*a[r])%3
        piv.append(j);r+=1
        if r==a.shape[0]:break
    return a,piv
def rank(a):return len(rref(a)[1])
def nullspace(a):
    a,piv=rref(a);free=[i for i in range(a.shape[1]) if i not in piv]
    ans=np.zeros((a.shape[1],len(free)),dtype=np.int64)
    for k,j in enumerate(free):
        ans[j,k]=1
        for i,p in enumerate(piv):ans[p,k]=-a[i,j]%3
    return ans
B=nullspace(boundary)
assert B.shape==(27,10) and rank(boundary)==17
def act(g,a):
    out=np.zeros_like(a)
    for j,h in enumerate(Q):out[qi[mul(g,h)]]=a[j]
    return out
def unit(g):
    z=np.zeros(27,dtype=np.int64);z[qi[g]]=1;return z
Dgen=[np.zeros(27,dtype=np.int64),(unit(one)-unit(v))%3]
def amul(a,b):
    g,A=a;h,Bb=b
    return mul(g,h),(A+act(g,Bb))%3
def apow(a,n):
    z=(one,np.zeros(27,dtype=np.int64))
    for _ in range(n):z=amul(z,a)
    return z
AU=(u,Dgen[0]);AV=(v,Dgen[1]);AC=apow(amul(AU,AV),8)
assert apow(AU,3)[0]==one and not np.any(apow(AU,3)[1])
assert apow(AV,3)[0]==one and not np.any(apow(AV,3)[1])
# In the desired quotient c=(uv)^-1, and uv has order nine.
assert not np.any(apow(amul(AU,AV),9)[1])
assert AC[0]==c
paths={one:np.zeros(27,dtype=np.int64)};words={one:[]};todo=deque([one])
while todo:
    g=todo.popleft()
    for j,h in enumerate((u,v)):
        gh=mul(g,h)
        if gh not in paths:
            paths[gh]=(paths[g]+act(g,Dgen[j]))%3
            words[gh]=words[g]+[j+1];todo.append(gh)
assert len(paths)==27
sch=[]
for g in Q:
    for j,h in enumerate((u,v)):
        z=(paths[g]+act(g,Dgen[j])-paths[mul(g,h)])%3
        assert not np.any(boundary@z%3);sch.append(z)
assert rank(sch)==10
print('PASS actual graph extension: 18 vertices, 27 edges, kernel rank10, order3^13')

records={}
for name,(t,Dt) in [('u',AU),('v',AV),('c',AC)]:
    L=(act(t,B)-B)%3;lr=rank(L);cases=[];allowed=[]
    for h in Q:
        commutes=mul(h,t)==mul(t,h)
        rhs=(act(h,Dt)-Dt-act(t,paths[h])+paths[h])%3
        soluble=commutes and rank(np.column_stack((L,rhs)))==lr
        if soluble:allowed.append(h)
        cases.append({'residue':h,'base_commutes':commutes,'lift_exists':bool(soluble)})
    assert set(allowed)=={one,t,pw(t,2)}
    records[name]={'matrix_rank':lr,'fibre_dimension':10-lr,'allowed_residues':allowed,'cases':cases}
    print(f'PASS {name} centralizer projection exactly C3; kernel fibre dimension {10-lr}')

torsion=[]
for h in Q:
    L=(B+act(h,B)+act(pw(h,2),B))%3
    rhs=-(paths[h]+act(h,paths[h])+act(pw(h,2),paths[h]))%3
    soluble=rank(np.column_stack((L,rhs)))==rank(L)
    torsion.append({'residue':h,'cube_one_lift_exists':bool(soluble)})
vertex_types={mul(mul(g,pw(t,e)),inv(g)) for g in Q for t in (u,v) for e in (1,2)}
assert {tuple(z['residue']) for z in torsion if z['cube_one_lift_exists']}==vertex_types|{one}
assert len(vertex_types)==12
cycle=apow(AC,3)[1]
assert np.any(cycle) and not np.any(boundary@cycle%3)
assert not np.any(apow(AC,9)[1])
stabilizers=[g for g in Q if np.array_equal(act(g,cycle),cycle)]
assert set(stabilizers)=={one,c,pw(c,2)}
print('PASS all27 torsion-lift tests: 12 nonidentity vertex residues lift; marked cusp lifts have order9')

R=np.array([[0,-1],[1,-1]],dtype=np.int64)
def affmul(a,b):
    t,k=a;s,l=b
    return ((np.array(t)+np.linalg.matrix_power(R,k)@np.array(s))%3).tolist(),(k+l)%3
Tu=([1,0],1);Tv=([1,1],1)
amap={one:([0,0],0)}
for g in Q:
    a=([0,0],0)
    for j in words[g]:a=affmul(a,Tu if j==1 else Tv)
    amap[g]=a
assert len({(tuple(t),k) for t,k in amap.values()})==27
for g in Q:
    for h in Q:assert affmul(amap[g],amap[h])==amap[mul(g,h)]
assert amap[c]==([0,0],1)
fixed={}
for name,g in [('u',u),('v',v),('c',c)]:
    t,k=amap[g];Rm=np.linalg.matrix_power(R,k)
    pts=[z for z in product(range(9),repeat=2)
         if np.all((Rm@np.array(z)+3*np.array(t)-np.array(z))%9==0)]
    marked=[z for z in pts if z[0]%3==z[1]%3==0]
    assert len(pts)==3
    assert len(marked)==(3 if name=='c' else 0)
    fixed[name]={'ninth_lattice_numerators':pts,'marked_third_torsion':marked}
print('PASS exact affine marking: c fixes three marked points; u,v fixed triples are unmarked')

payload={'scope':__doc__,'order':3**13,'P_elements':Q,'u':u,'v':v,'c':c,'x':x,'y':y,
         'source_words':{str(q):words[q] for q in Q},'centralizers':records,
         'torsion_lifts':torsion,'fixed_points':fixed,'R0':R.tolist(),
         'c_cubed_chain':cycle.tolist(),'c_cycle_stabilizer':stabilizers,
         'schreier_kernel_rank':10,'vertices':18,'edges':27}
OUT.with_suffix('.json').write_text(json.dumps(payload,indent=2)+'\n')
np.savez_compressed(OUT.with_suffix('.npz'),boundary=boundary,homology_basis=B,
                    schreier_rows=np.array(sch),sections=np.array([paths[q] for q in Q]),
                    D_u=AU[1],D_v=AV[1],D_c=AC[1],c_cube=cycle)
