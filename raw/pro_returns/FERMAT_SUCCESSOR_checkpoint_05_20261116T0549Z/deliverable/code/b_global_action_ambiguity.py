#!/usr/bin/env python3
"""Independent projective-matrix check of the global homogeneous torsion.

All 54 automorphisms are constructed from diagonal cube roots and
coordinate permutations on the original Fermat plane.  Four such
projective generators are used in a transposed rectangular Smith
calculation, independently of the translation-based construction.
"""
import ast
from collections import Counter
from itertools import permutations
import json
from pathlib import Path
import numpy as np

PREC=10
MOD=3**PREC
hall=[(i,j,k) for i in range(10) for j in range(i) for k in range(j,10)]
lookup={t:i for i,t in enumerate(hall)}
source=ast.parse(Path('deliverable/code/b_char2_symmetry.py').read_text())
exec(compile(ast.Module(body=[x for x in source.body
       if isinstance(x,ast.FunctionDef) and x.name in {'bracket','lie3','smith_transport'}],
       type_ignores=[]),'b_Hall_functions','exec'))
I2=np.eye(2,dtype=np.int64)
I10=np.eye(10,dtype=np.int64)
I330=np.eye(330,dtype=np.int64)
U=np.array([[0,-1],[2,-2],[1,0],[0,-2],[1,-1],[2,0],[1,-2],[2,-1]],dtype=np.int64)
R=np.array([[0,-1],[1,-1]],dtype=np.int64)
CE=np.array([[1,-1],[0,-1]],dtype=np.int64)

def normalize(point):
    leading=next(x for x in point if x is not None)
    return tuple(None if x is None else (x-leading)%6 for x in point)

# C_i=[1:-zeta^i:0]; the original tangent O is C_0, full index six.
points=[normalize((None,3+2*i,0)) for i in range(3)]
points += [normalize((3+2*i,None,0)) for i in range(3)]
points += [normalize((0,3+2*i,None)) for i in range(3)]
assert len(set(points))==9
O=6
nonorigin=[0,1,2,3,4,5,7,8]
position={p:j for j,p in enumerate(nonorigin)}
coords=[(1,0),(2,2),(0,1),(2,0),(1,1),(0,2),(0,0),(2,1),(1,2)]

def boundary(perm):
    P=np.zeros((8,8),dtype=np.int64)
    for j,p in enumerate(nonorigin):
        target=perm[p]
        if target==O:P[:,j]=-1
        else:P[position[target],j]=1
    return P

def full_matrix(compact,torus):
    raw=U@compact-torus@U
    assert not np.any(raw%3)
    return np.block([[compact,np.zeros((2,8),dtype=np.int64)],
                     [raw//3,torus]])

automorphisms={}
for permutation in permutations(range(3)):
    sign=(-1)**sum(permutation[i]>permutation[j] for i in range(3) for j in range(i+1,3))
    for a in range(3):
        for b in range(3):
            exponents=(2*a,2*b,0)
            perm=[]
            for point in points:
                image=normalize(tuple(None if point[permutation[i]] is None
                                      else point[permutation[i]]+exponents[i]
                                      for i in range(3)))
                perm.append(points.index(image))
            compact=sign*np.linalg.matrix_power(R,(a+b)%3)
            origin=np.array(coords[perm[O]],dtype=np.int64)
            residual=np.column_stack((np.array(coords[perm[0]])-origin,
                                      np.array(coords[perm[2]])-origin))%3
            assert np.array_equal(compact%3,residual)
            automorphisms[(permutation,a,b)]=full_matrix(compact,boundary(perm))
assert len({tuple(M.flatten()) for M in automorphisms.values()})==54
selected=[((0,1,2),1,0),((0,1,2),0,1),((1,0,2),0,0),((1,2,0),0,0)]
geometry=[automorphisms[key] for key in selected]
group={tuple(I10.flatten()):I10}
pending=[I10]
while pending:
    A=pending.pop()
    for g in geometry:
        product=g@A
        key=tuple(product.flatten())
        if key not in group:
            group[key]=product;pending.append(product)
            assert len(group)<=54
assert set(group)=={tuple(M.flatten()) for M in automorphisms.values()}
print('All54 projective Fermat automorphisms and independent four-generator closure agree: PASS',flush=True)

T=full_matrix(I2+3*R,7*np.eye(8,dtype=np.int64))
Tbar=full_matrix(I2+3*R@R,7*np.eye(8,dtype=np.int64))
conjugate_perm=[points.index(normalize(tuple(None if x is None else -x for x in point)))
                for point in points]
C=full_matrix(CE,-boundary(conjugate_perm))
assert np.array_equal(C@C,I10)
assert np.array_equal(C@T@C,Tbar)
for g in automorphisms.values():
    assert np.array_equal(g@T,T@g)
    assert np.array_equal(g@Tbar,Tbar@g)
    assert tuple((C@g@C).flatten()) in group

arith=[lie3(T)*pow(7,-1,MOD)%MOD,lie3(Tbar)*pow(7,-1,MOD)%MOD]
c_action=-lie3(C)%MOD
geo=[lie3(g) for g in geometry]
stages=[('arithmetic_Q',arith+[c_action]),
        ('arithmetic_K_and_geometry',arith+geo),
        ('arithmetic_Q_and_geometry',arith+geo+[c_action])]
expected=[{0:237,1:59,2:27,3:7},{0:325,1:4,2:1},{0:326,1:4}]
records=[]
stored={}
for (name,actions),expected_hist in zip(stages,expected):
    horizontal=np.hstack([(g-I330).T%MOD for g in actions])
    vals,rows=smith_transport(horizontal)
    histogram=dict(sorted(Counter(vals).items()))
    assert histogram==expected_hist
    positive=[j for j,e in enumerate(vals) if e]
    # Transposing the Smith identity gives exact coset numerators.
    columns=rows.T[:,positive]
    denominators=np.array([3**vals[j] for j in positive],dtype=np.int64)
    for g in actions:
        assert not np.any(((g-I330)@columns)%denominators[None,:])
    print(name,'Smith:',histogram,'; order3^',sum(vals),flush=True)
    records.append({'stage':name,'Smith_histogram':histogram,'log3_order':sum(vals),
                    'positive_exponents':[vals[j] for j in positive]})
    stored[name+'_coset_numerators']=columns
    stored[name+'_coset_denominators']=denominators

result={'status':'independent projective-generator and transposed-Smith verification passed',
        'geometric_group_order':54,'projective_generators':[
            {'permutation':list(p),'diagonal_exponents':[a,b,0]} for p,a,b in selected],
        'stages':records,
        'conclusion':'With fixed rational class and all54 global automorphism/path identities, the homogeneous arithmetic-Q action-class ambiguity is (F3)^4.',
        'scope':'This is the exact group of cohomological differences satisfying the specified constraints; geometric realization of every difference is not asserted.'}
Path('deliverable/code/b_global_action_ambiguity.json').write_text(json.dumps(result,indent=2)+'\n')
np.savez_compressed('deliverable/code/b_global_action_ambiguity_matrices.npz',
                    modulus=np.array([MOD]),projective_automorphisms=np.stack(list(automorphisms.values())),
                    projective_generators=np.stack(geometry),Tau_V=T,Tau_bar_V=Tbar,
                    Conjugation_V=C,arithmetic_actions=np.stack(arith),
                    conjugation_action=c_action,geometric_actions=np.stack(geo),**stored)
