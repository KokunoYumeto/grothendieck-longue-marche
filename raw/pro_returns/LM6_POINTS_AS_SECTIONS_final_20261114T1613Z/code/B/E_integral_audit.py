#!/usr/bin/env python3
"""Independent tensor-coordinate check of E.37--38.

The Hall-coordinate conversion below uses elimination in the free associative
tensor algebra, rather than the Jacobi reduction in the root certificate.
The input is the actual integral degree-one arithmetic matrix already recorded
in E.18. No regulator value is inferred from this calculation.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json

work = Path(__file__).resolve().parents[2]
data = json.loads((work / 'code/root/class_three_fibre_output.json').read_text())
F, C = data['A_tau'], data['C_V']
d = 10
hall = [(i,j,k) for j in range(d) for i in range(j+1,d) for k in range(j,d)]
assert len(hall) == 330

def add(dst, src, scale=1):
    for key,value in src.items():
        out = dst.get(key,0) + scale*value
        if out: dst[key] = out
        else: dst.pop(key,None)

def tensor(word):
    i,j,k = word
    out = {}
    for term,sgn in [((i,j,k),1),((j,i,k),-1),((k,i,j),-1),((k,j,i),1)]:
        add(out,{term:sgn})
    return out

# Each row is a unit-pivot tensor together with its exact Hall coordinates.
echelon = []
for idx,word in enumerate(hall):
    v,coeff = tensor(word),{idx:1}
    for pivot,u,c in echelon:
        q = v.get(pivot,0)
        if q:
            add(v,u,-q)
            add(coeff,c,-q)
    pivot = min(v)
    q = v[pivot]
    assert abs(q) == 1
    v = {a:b*q for a,b in v.items()}
    coeff = {a:b*q for a,b in coeff.items()}
    echelon.append((pivot,v,coeff))

def coordinates(v):
    v,coeff = dict(v),{}
    for pivot,u,c in echelon:
        q = v.get(pivot,0)
        if q:
            add(v,u,-q)
            add(coeff,c,q)
    assert not v
    return coeff

def multiply(A,B):
    return [[sum(A[i][r]*B[r][j] for r in range(d)) for j in range(d)] for i in range(d)]

def substitute(v,M):
    cols = [[(i,M[i][j]) for i in range(d) if M[i][j]] for j in range(d)]
    out = {}
    for (i,j,k),a in v.items():
        for (r,b),(s,c),(t,e) in product(cols[i],cols[j],cols[k]):
            add(out,{(r,s,t):a*b*c*e})
    return out

ell = [0,2,0,0,0,3,0,0,0,0]
def determinant(j,k):
    return int((j,k)==(0,1))-int((j,k)==(1,0))
def contraction(v):
    return sum(a*ell[i]*determinant(j,k) for (i,j,k),a in v.items())

detector = [contraction(tensor(w)) for w in hall]
assert all(a%3 == 0 for a in detector)
primitive = [a//3 for a in detector]
assert any(abs(a)==1 for a in primitive)
for w,a in zip(hall,detector):
    assert contraction(substitute(tensor(w),F)) == 49*a
    assert contraction(substitute(tensor(w),C)) == a

F3 = multiply(multiply(F,F),F)
assert all((F3[i][j]-int(i==j))%3==0 for i in range(d) for j in range(d))
precision = 12
modulus = 3**precision
inv343 = pow(343,-1,modulus)
M = [[0]*330 for _ in range(330)]
for j,w in enumerate(hall):
    for i,a in coordinates(substitute(tensor(w),F3)).items():
        M[i][j] = (a*inv343)%modulus
    M[j][j] = (M[j][j]-1)%modulus
assert all(a%3==0 for row in M for a in row)

def valuation(a):
    if a==0: return precision
    v=0
    while a%3==0:
        a//=3
        v+=1
    return v

pivots=[]
for k in range(330):
    v,i,j = min((valuation(M[i][j]),i,j) for i in range(k,330) for j in range(k,330))
    assert v < precision
    M[k],M[i] = M[i],M[k]
    for row in M: row[k],row[j] = row[j],row[k]
    pv = 3**v
    unit_inverse = pow(M[k][k]//pv,-1,modulus//pv)
    M[k] = [(a*unit_inverse)%modulus for a in M[k]]
    assert M[k][k] == pv
    for i in range(k+1,330):
        assert M[i][k]%pv==0
        scale=M[i][k]//pv
        if scale:
            M[i] = [(a-scale*b)%modulus for a,b in zip(M[i],M[k])]
        assert M[i][k]==0
    # These are column operations using the now-zero lower part of column k.
    for j in range(k+1,330):
        assert M[k][j]%pv==0
        M[k][j]=0
    pivots.append(v)

assert Counter(pivots)==Counter({1:132,2:82,3:52,4:49,5:14,6:1})
assert sum(pivots)==724
assert pow(4,9,19)==1 and pow(4,3,19)!=1
assert pow(3,2,19)==pow(4,4,19)
assert (6*4)%9==6

out={
  'status':'passed',
  'method':'Associative tensor substitution and unit-pivot tensor-to-Hall elimination',
  'hall_dimension':330,
  'primitive_detector':[{'word':list(w),'value':a} for w,a in zip(hall,primitive) if a],
  'F_equivariance':49,
  'C_equivariance':1,
  'smith_valuations':dict(sorted(Counter(pivots).items())),
  'determinant_valuation':sum(pivots),
  'precision':precision,
  'p19_kummer_coordinate_mod9':4,
  'p19_obstruction_mod9':6,
  'scope':'Finite integral calculations only; continuity and arithmetic class comparisons audited in prose.'
}
(Path(__file__).with_suffix('.out.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
