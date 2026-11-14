#!/usr/bin/env python3
"""Integral degree-three kernel of N/gamma4(N) -> N/(F'' gamma4(N)).

N is free pro-3 on e0,e1,t0,...,t7.  The subgroup F' is the inverse
image of span(t0,...,t7) in N^ab.  All linear algebra is over Z;
the certificates are integral right inverses, not modular rank tests.
"""
from pathlib import Path
from collections import defaultdict
import json
import numpy as np

D = 10
T = set(range(2,D))
B2 = [(i,j) for i in range(D) for j in range(i)]
B3 = [(i,j,k) for i in range(D) for j in range(i) for k in range(j,D)]
I3 = {x:i for i,x in enumerate(B3)}
assert len(B2) == 45 and len(B3) == 330

def reduce_word(w):
    out=[]
    for a in w:
        if out and out[-1]==-a:
            out.pop()
        else:
            out.append(a)
    return out

def inv_word(w):
    return [-x for x in reversed(w)]

def comm_word(u,v):
    return reduce_word(u+v+inv_word(u)+inv_word(v))

def power_letter(x,n):
    return [x if n>=0 else -x]*abs(n)

# Verify the actual nine-sheeted cover relation in the free group on x,y.
x,y=[1],[2]
z=inv_word(comm_word(x,y))
peripheral=[]
grid=[]
for j in range(9):
    s=0
    while (s+1)**2<=j:
        s+=1
    r=j-s*s
    a,b=(r,s) if r<=s else (s,2*s-r)
    grid.append([a,b])
    if a>=b:
        p=power_letter(1,a)+power_letter(2,b)
    else:
        p=power_letter(1,b)+power_letter(2,b)+power_letter(1,a-b)
    peripheral.append(reduce_word(p+z+inv_word(p)))
cover_relation=comm_word([1]*3,[2]*3)
for w in peripheral:
    cover_relation+=w
assert reduce_word(cover_relation)==[]
assert grid==[[0,0],[0,1],[1,1],[1,0],[0,2],[1,2],[2,2],[2,1],[2,0]]

def triple(i,j,k):
    """Integral Hall coordinates of [[i,j],k]."""
    if i == j:
        return {}
    s = 1
    if i < j:
        i,j,s = j,i,-1
    if k >= j:
        return {I3[i,j,k]:s}
    return {I3[i,k,j]:s,I3[j,k,i]:-s}

def tensor_bracket(a,b):
    out=defaultdict(int)
    for x,v in a.items():
        for y,w in b.items():
            out[x+y]+=v*w
            out[y+x]-=v*w
    return {x:v for x,v in out.items() if v}

def tensor_hall(t):
    i,j,k=t
    return tensor_bracket(tensor_bracket({(i,):1},{(j,):1}),{(k,):1})

# Verify the integral Jacobi reducer independently in the tensor algebra.
hall_tensor=[tensor_hall(x) for x in B3]
tensor_checks=0
for i in range(D):
    for j in range(D):
        for k in range(D):
            expected=tensor_hall((i,j,k))
            actual=defaultdict(int)
            for row,c in triple(i,j,k).items():
                for word,a in hall_tensor[row].items():
                    actual[word]+=c*a
            actual={w:a for w,a in actual.items() if a}
            assert actual == expected
            tensor_checks+=1

# The degree-three ideal is [T, Lie_2(V)].
labels=[]
cols=[]
for t in sorted(T):
    for i,j in B2:
        labels.append([t,i,j])
        col=np.zeros(len(B3),dtype=np.int64)
        for row,c in triple(i,j,t).items():
            col[row]=-c
        cols.append(col)
M=np.stack(cols,axis=1)

# Explicit quotient: Lie_3(E) + Sym^2(E) tensor T.
retained=[]
for row,(i,j,k) in enumerate(B3):
    if i<2 and j<2 and k<2:
        retained.append(row)
    elif i in T and j<2 and k<2:
        retained.append(row)
assert len(retained)==26
discarded=[i for i in range(len(B3)) if i not in retained]
assert len(discarded)==304
assert not np.any(M[retained,:])

# Column elimination records each pivot as an integral combination of
# the original 360 relations.  Every pivot is a unit in Z.
pivots={}
for c in range(M.shape[1]):
    v=M[:,c].copy()
    expr=np.zeros(M.shape[1],dtype=np.int64)
    expr[c]=1
    for r in sorted(pivots):
        if v[r]:
            a=int(v[r])
            v-=a*pivots[r][0]
            expr-=a*pivots[r][1]
    nz=np.flatnonzero(v)
    if not len(nz):
        continue
    r=int(nz[0])
    assert abs(int(v[r]))==1
    s=int(v[r])
    v*=s
    expr*=s
    assert r not in pivots
    pivots[r]=(v,expr)
assert sorted(pivots)==discarded

# Reverse elimination constructs an exact integer right inverse onto
# every discarded Hall coordinate, proving saturation and no torsion.
unit_expr={}
for r in reversed(discarded):
    v,expr=pivots[r]
    v=v.copy();expr=expr.copy()
    for q in discarded:
        if q>r and v[q]:
            a=int(v[q])
            expr-=a*unit_expr[q]
            v[q]=0
    assert np.array_equal(v,np.eye(len(B3),dtype=np.int64)[:,r])
    unit_expr[r]=expr
cert=np.stack([unit_expr[r] for r in discarded],axis=1)
unit_matrix=M@cert
assert np.array_equal(unit_matrix,np.eye(len(B3),dtype=np.int64)[:,discarded])

# Conjugates of the degree-two T-T commutators add no new relation:
# [V,[T,T]] lies in [T,Lie_2(V)], integrally by Jacobi.
normality_checks=0
for i,j in B2:
    if i in T and j in T:
        for k in range(D):
            v=np.zeros(len(B3),dtype=np.int64)
            for r,c in triple(i,j,k).items():
                v[r]=c
            assert not np.any(v[retained])
            assert np.array_equal(unit_matrix@v[discarded],v)
            normality_checks+=1

# Decomposition by the number of T letters, checked independently.
counts={}
for n in range(4):
    rows=[r for r,t in enumerate(B3) if sum(i in T for i in t)==n]
    keep=sum(r in retained for r in rows)
    counts[str(n)]={'ambient':len(rows),'kernel':len(rows)-keep,'quotient':keep}
assert counts == {'0':{'ambient':2,'kernel':0,'quotient':2},
                  '1':{'ambient':32,'kernel':8,'quotient':24},
                  '2':{'ambient':128,'kernel':128,'quotient':0},
                  '3':{'ambient':168,'kernel':168,'quotient':0}}

# The degree-two kernel has an actual subset of the Hall basis.
k2=[i for i,t in enumerate(B2) if all(x in T for x in t)]
assert len(k2)==28

# A concrete based-automorphism ambiguity: w=[t0,t1] belongs to F'',
# but Ad(w) changes e0 modulo gamma4(N) by [[t0,t1],e0] != 0.
inner_witness=triple(2,3,0)
assert inner_witness
assert not any(r in retained for r in inner_witness)

result={
    'status':'PASS',
    'ambient_free_rank':10,
    'intrinsic_graded_ranks':[10,45,330],
    'kernel_graded_ranks':[0,28,304],
    'ambient_metabelian_image_graded_ranks':[10,17,26],
    'kernel_Z3_rank':332,
    'quotient_Z3_hirsch_rank':53,
    'degree_three_T_counts':counts,
    'tensor_reducer_checks':tensor_checks,
    'integral_normality_checks':normality_checks,
    'degree_two_Hall_basis':B2,
    'degree_three_Hall_basis':B3,
    'degree_two_kernel_rows':k2,
    'degree_three_quotient_rows':retained,
    'relation_labels_t_i_j':labels,
    'degree_three_integral_unit_certificates':{
        str(r):[[int(c),int(v)] for c,v in enumerate(unit_expr[r]) if v]
        for r in discarded},
    'maximum_certificate_entry':int(np.max(np.abs(cert))),
    'integer_right_inverse_identity':True,
    'cover_grid_order':grid,
    'free_F_peripheral_words':peripheral,
    'actual_cover_relation_freely_reduces_to_identity':True,
    'based_inner_ambiguity_Hall_coordinates':inner_witness,
}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('Hall ranks: intrinsic [10,45,330]; quotient [10,17,26].')
print('Kernel graded ranks [0,28,304]; abelian kernel rank332.')
print('Integral right inverse certifies all304 degree-three kernel rows.')
print('Tensor identities:',tensor_checks,'normality checks:',normality_checks)
print('T-letter decomposition:',counts)
print('Largest certificate coefficient:',result['maximum_certificate_entry'])
print('Actual nine-sheeted cover relation: freely reduced to identity.')
print('Based inner-automorphism ambiguity:',inner_witness)
print('PASS: exact integral certificates saved; no finite-field rank inference.')
