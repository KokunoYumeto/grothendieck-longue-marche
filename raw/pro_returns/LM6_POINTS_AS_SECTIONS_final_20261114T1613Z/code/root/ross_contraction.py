#!/usr/bin/env python3
"""Exact Fermat-cubic automorphism projector and Ross-divisor contraction.

All matrices are rational.  This checks the actual action of the 54
monomial projective automorphisms on H tensor exterior^2 W, where W is
the quotient of the cusp permutation module by its diagonal sum.
It does not evaluate an arithmetic cocycle or a p-adic regulator.
"""
from itertools import permutations, product
from pathlib import Path
import json
import sympy as s

R=s.Matrix([[0,-1],[1,-1]])
I=s.eye(2)
# A_i=[0:-zeta^i:1], B_i=[-zeta^i:0:1], C_i=[-zeta^i:1:0].
points=[]
labels=[]
for letter in 'ABC':
    for i in range(3):
        p={'A':(None,(-1,i),(1,0)),
           'B':((-1,i),None,(1,0)),
           'C':((-1,i),(1,0),None)}[letter]
        points.append(p);labels.append(letter+str(i))

def normalized(p):
    sg,ex=next(x for x in p if x is not None)
    return tuple(None if x is None else (x[0]*sg,(x[1]-ex)%3) for x in p)

point_index={normalized(p):i for i,p in enumerate(points)}
assert len(point_index)==9
pi=s.eye(8).row_join(-s.ones(8,1))
lift=s.eye(9)[:,:8]
pairs=[(i,j) for i in range(8) for j in range(i+1,8)]

def exterior2(M):
    return s.Matrix([[M[i,k]*M[j,l]-M[i,l]*M[j,k]
                      for k,l in pairs] for i,j in pairs])

S=s.zeros(56)
group=[]
for p in permutations(range(3)):
    parity=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
    for a,b in product(range(3),repeat=2):
        exps=(a,b,0)
        cp=[]
        for point in points:
            diag=tuple(None if x is None else (x[0],(x[1]+exps[j])%3)
                       for j,x in enumerate(point))
            cp.append(point_index[normalized(tuple(diag[p[j]] for j in range(3)))])
        P=s.zeros(9)
        for j,k in enumerate(cp):P[k,j]=1
        W=pi*P*lift
        assert pi*P==W*pi
        H=parity*(R**((a+b)%3))
        M=s.kronecker_product(H,exterior2(W))
        S+=M
        group.append((p,a,b,cp,H,W,M))

assert len({tuple(g[3]) for g in group})==54
average=S/54
assert average*average==average
assert average.rank()==2
for *_,M in group:
    assert M*average==average

# div(1-x)=3B_0-C_0-C_1-C_2 and div(1-y)=3A_0-C_0-C_1-C_2.
lf=s.Matrix([[0,0,0,3,0,0,-1,-1,-1]])
lg=s.Matrix([[3,0,0,0,0,0,-1,-1,-1]])
assert (lf*s.ones(9,1))[0]==(lg*s.ones(9,1))[0]==0
f=lf*lift;g=lg*lift
b=s.Matrix([[f[i]*g[j]-f[j]*g[i] for i,j in pairs]])
contraction=s.kronecker_product(I,b)
images=contraction*average
assert images.rank()==2
pivots=list(images.rref()[1])
assert len(pivots)==2
chosen=average[:,pivots]
coordinate_matrix=contraction*chosen
assert coordinate_matrix.det()!=0
inverse=chosen*coordinate_matrix.inv()
assert contraction*inverse==I
assert average*inverse==inverse
block_sums=[]
for p in permutations(range(3)):
    block=s.zeros(2)
    for gp,a,bb,cp,H,W,M in group:
        if gp==p:block+=contraction*M[:,pivots]
    block_sums.append({'permutation':list(p),'sum':[[int(x) for x in row] for row in block.tolist()]})
assert sum((s.Matrix(r['sum']) for r in block_sums),s.zeros(2))==54*coordinate_matrix

# Arithmetic complex conjugation on H sends zeta to zeta^{-1};
# on W it reverses each cusp meridian and sends i to -i.
CH=s.Matrix([[1,-1],[0,-1]])
assert CH*R*CH==R**2
Pc=s.zeros(9)
for j,label in enumerate(labels):
    k=labels.index(label[0]+str((-int(label[1]))%3))
    Pc[k,j]=-1
CW=pi*Pc*lift
CM=s.kronecker_product(CH,exterior2(CW))
assert CM*average==average*CM
assert contraction*CM==CH*contraction
assert CM*inverse==inverse*CH

def matrix(M):return [[str(x) for x in row] for row in M.tolist()]
out={
 'claim':'Exact geometric projector and its nonzero Ross-divisor contraction',
 'basis':'H=(1,zeta); W=(A0,A1,A2,B0,B1,B2,C0,C1), C2=-sum; exterior pairs lexicographic',
 'group_order':len(group),'ambient_dimension':56,'invariant_dimension':average.rank(),
 'f_divisor':[int(x) for x in lf],'g_divisor':[int(x) for x in lg],
 'selected_projector_columns':pivots,
 'contraction_matrix_on_selected_columns':matrix(coordinate_matrix),
 'determinant':str(coordinate_matrix.det()),
 'nine_diagonal_automorphism_sums_by_coordinate_permutation':block_sums,
 'invariant_basis_normalized_by_contraction':matrix(inverse),
 'projector_numerator_S':matrix(S),
 'projector_denominator':54,
 'conjugation_H':matrix(CH),'conjugation_W':matrix(CW),
 'arithmetic_cocycle_evaluated':False,'checks_passed':True
}
Path(__file__).with_name('ross_contraction_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in
                 {'invariant_basis_normalized_by_contraction','projector_numerator_S','conjugation_W'}},indent=2))
