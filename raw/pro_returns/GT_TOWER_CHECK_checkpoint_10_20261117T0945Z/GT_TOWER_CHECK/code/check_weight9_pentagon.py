#!/usr/bin/env python3
"""Exact infinitesimal five-point pentagon on the four-dimensional F11 stratum.

We use t_4/(sum t_ij) = Lie(a,b,c) semidirect Lie(u,v),
where a=t14,b=t24,c=t34,u=t12,v=t23.
All polynomials are expanded in the free associative algebra.
"""
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import json,itertools
base=Path(__file__).parent
data=json.loads((base/"check_weight9_stratum.json").read_text())
p=data["prime"];lyndon=data["lyndon_words"];basis=data["basis"]
def clean(d):return {w:c%p for w,c in d.items() if c%p}
def add(*ps):
    d=defaultdict(int)
    for P in ps:
        for w,c in P.items():d[w]+=c
    return clean(d)
def scale(P,c):return clean({w:c*v for w,v in P.items()})
def mul(P,Q):
    d=defaultdict(int)
    for u,c in P.items():
        for v,e in Q.items():d[u+v]+=c*e
    return clean(d)
def bracket(P,Q):return add(mul(P,Q),scale(mul(Q,P),-1))
def deriv(D,P):
    d=defaultdict(int)
    for w,c in P.items():
        for i,a in enumerate(w):
            for v,e in D[ord(a)-97].items():d[w[:i]+v+w[i+1:]]+=c*e
    return clean(d)
def dbracket(D,E):
    return tuple(add(deriv(D,E[i]),scale(deriv(E,D[i]),-1)) for i in range(3))
zero=({}, {}, {})
Du=({"ab":1,"ba":-1},{"ba":1,"ab":-1},{})
Dv=({},{"bc":1,"cb":-1},{"cb":1,"bc":-1})
Du=tuple(clean(P) for P in Du);Dv=tuple(clean(P) for P in Dv)
def is_lyndon(s):return all(s<s[i:]+s[:i] for i in range(1,len(s)))
def split(s):
    i=next(i for i in range(1,len(s)) if is_lyndon(s[i:]))
    return s[:i],s[i:]
@lru_cache(None)
def Dword(s):
    if s=="x":return Du
    if s=="y":return Dv
    u,v=split(s);return dbracket(Dword(u),Dword(v))
# Each local evaluation specifies P(x),P(y),D(x),D(y), and whether the
# derivative of a mixed Lyndon word is the universal Dword or zero.
specs=[
 ({},{"b":1},Du,Dv,True),
 ({"a":-1,"b":-1,"c":-1},{"c":1},tuple(scale(P,-1) for P in Du),zero,False),
 ({},{"c":1},Dv,zero,False),
 ({"a":-1,"b":-1,"c":-1},{"b":1,"c":1},tuple(scale(P,-1) for P in Dv),zero,False),
]
def evaluator(spec):
    Px,Py,Dx,Dy,mixed=spec
    def D(s):
        if s=="x":return Dx
        if s=="y":return Dy
        return Dword(s) if mixed else zero
    @lru_cache(None)
    def P(s):
        if s=="x":return clean(Px)
        if s=="y":return clean(Py)
        u,v=split(s);A=P(u);B=P(v)
        return add(bracket(A,B),deriv(D(u),B),scale(deriv(D(v),A),-1))
    return P
ev=[evaluator(spec) for spec in specs]
pentagon_columns=[]
for n,s in enumerate(lyndon):
    pentagon_columns.append(add(ev[0](s),ev[1](s),scale(ev[2](s),-1),scale(ev[3](s),-1)))
    if (n+1)%14==0:print("Completed Lyndon columns:",n+1,flush=True)
outputs=[]
for v in basis:
    outputs.append(add(*(scale(P,c) for P,c in zip(pentagon_columns,v) if c)))
keys=sorted(set().union(*(P.keys() for P in outputs)))
matrix=[[P.get(k,0) for P in outputs] for k in keys]
def rref(A,n):
    A=[r[:] for r in A];piv=[];r=0
    for col in range(n):
        j=next((j for j in range(r,len(A)) if A[j][col]),None)
        if j is None:continue
        A[r],A[j]=A[j],A[r];a=pow(A[r][col],-1,p)
        A[r]=[(x*a)%p for x in A[r]]
        for j in range(len(A)):
            if j!=r and A[j][col]:
                a=A[j][col];A[j]=[(x-a*y)%p for x,y in zip(A[j],A[r])]
        piv.append(col);r+=1
    free=[j for j in range(n) if j not in piv];ker=[]
    for col in free:
        v=[0]*n;v[col]=1
        for i,j in enumerate(piv):v[j]=-A[i][col]%p
        ker.append(v)
    return r,ker
rank,kernel=rref(matrix,len(basis))
survivors=[]
for v in itertools.product(range(p),repeat=len(basis)):
    if all(sum(a*b for a,b in zip(row,v))%p==0 for row in matrix):
        survivors.append(list(v))
# Compare the original 2h directly, without the invariant-basis coordinates.
source=data["source_coefficients"]
source_P=add(*(scale(P,c) for P,c in zip(pentagon_columns,source) if c))
assert source_P
record={"prime":p,"source_dimension":len(basis),"pentagon_rank":rank,
 "kernel_basis_in_source_coordinates":kernel,
 "number_of_source_vectors":p**len(basis),"all_pentagon_kernel_vectors":survivors,
 "associative_output_basis":outputs,
 "source_2h_pentagon":source_P}
target=Path(__file__).with_suffix(".json")
target.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
print("Exact free-Lie(a,b,c) pentagon coefficient rows:",len(matrix))
print("Pentagon rank on special invariant source:",rank)
print("Pentagon kernel dimension:",len(kernel))
print("All vectors enumerated:",p**len(basis))
print("All zero pentagon vectors:",len(survivors))
print("Kernel basis:",kernel)
print("Literal 2h pentagon nonzero coefficients:",len(source_P))
print("Certificate:",target.name)
print("This is an exact graded-stratum calculation; full GT images require their lifting map.")
