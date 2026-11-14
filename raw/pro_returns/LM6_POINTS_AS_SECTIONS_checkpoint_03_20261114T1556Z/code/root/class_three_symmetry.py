#!/usr/bin/env python3
"""Exact geometric symmetry constraints on the actual E.19 coefficient module.

The arithmetic cocycle vector is deliberately not asserted evaluated.
Finite character enumeration and integral 3-adic Smith certificates are
independent of any proposed value of that vector.
"""
from pathlib import Path
from collections import Counter
from contextlib import redirect_stdout
from itertools import product
import io,json,runpy
import numpy as np

buf=io.StringIO()
with redirect_stdout(buf):
    d=runpy.run_path(str(Path(__file__).with_name('class_three_fibre.py')))
T,J,U=d['T'],d['J'],d['U']
I=np.eye(330,dtype=object)
P=np.zeros((8,8),dtype=object)
for j,i in enumerate([3,4,5,0,1,2,7,6]): P[i,j]=1
IV=d['block'](-np.eye(2,dtype=object),P)
IA=d['lie3'](IV)
assert np.array_equal(IA@IA,I)
assert np.array_equal(IA@J,J@IA)
assert np.array_equal(IA@T,T@IA)
assert int(np.trace(IA))==-2
assert int(np.trace(J@IA))==-2
M=(T-7*I)@(I-J)@(I+IA)
precision=10;mod=3**precision
M=[[int(x)%mod for x in row] for row in M]
def val(x):
    if not x:return precision
    v=0
    while x%3==0:x//=3;v+=1
    return v
values=[]
for k in range(330):
    best=(precision,None,None)
    for i in range(k,330):
        for j in range(k,330):
            v=val(M[i][j])
            if v<best[0]:best=(v,i,j)
            if v==0:break
        if best[0]==0:break
    v,i,j=best
    if i is None:break
    M[k],M[i]=M[i],M[k]
    for row in M:row[k],row[j]=row[j],row[k]
    pp=3**v;inverse=pow(M[k][k]//pp,-1,mod//pp)
    for i in range(k+1,330):
        assert M[i][k]%pp==0
        cc=(M[i][k]//pp*inverse)%(mod//pp)
        if cc:M[i]=[(x-cc*y)%mod for x,y in zip(M[i],M[k])]
    values.append(v)
assert len(values)==83

# Enumerate E[3] semidirect mu_6 and its conjugation coset.
R=np.array([[0,-1],[1,-1]],dtype=int)%3
C=np.array([[1,-1],[0,-1]],dtype=int)%3
I2=np.eye(2,dtype=int)
points=[np.array(t,dtype=int) for t in product(range(3),repeat=2)]
compact_trace=[2,1,-1,-2,-1,1]
def fix(B,t):
    return sum(np.array_equal((B@x+t)%3,x) for x in points)
def cube(B,t):
    B2=B@B%3
    return B2@B%3,(I2+B+B2)@t%3
rows=[];sums=Counter();weighted=Counter()
for k in range(6):
    B=np.linalg.matrix_power(-R,k)%3
    for t in points:
        B3,t3=cube(B,t)
        h=compact_trace[k];h3=compact_trace[(3*k)%6]
        w=fix(B,t)-1;w3=fix(B3,t3)-1
        v=h+w;v3=h3+w3
        assert (v**3-v3)%3==0
        a=(v**3-v3)//3;q=a-v
        CB=C@B%3;ct=C@t%3
        CB3,ct3=cube(CB,ct)
        cv=1-fix(CB,ct);cv3=1-fix(CB3,ct3)
        assert (cv**3-cv3)%3==0
        ca=(cv**3-cv3)//3;cq=ca+cv
        sums.update({'V':v,'A':a,'Q':q,'cQ':cq})
        weighted.update({'H3':(h**3-h3)//3-h,
                         'H2W':h*h*w-w,
                         'HW2':h*w*w,
                         'W3':(w**3-w3)//3})
        rows.append({'unit_power':k,'translation':t.tolist(),
                     'tr_V':v,'tr_A':a,'tr_Q':q,'tr_cQ':cq})
assert len(rows)==54
assert all(v%54==0 for v in sums.values())
assert all(v%54==0 for v in weighted.values())
dimensions={k:v//54 for k,v in sums.items()}
degrees={k:v//54 for k,v in weighted.items()}
assert dimensions=={'V':0,'A':4,'Q':4,'cQ':0},dimensions
assert degrees=={'H3':0,'H2W':0,'HW2':2,'W3':2},degrees
out={'integral_involution':{
       'matrix_on_V':IV.tolist(),'trace_on_A':int(np.trace(IA)),
       'invariant_dimension':164,'conjugation_trace_on_invariants':-2,
       'relation_matrix':'(T-7I)(I-J)(I+Iota)',
       'relation_rank':83,'cohomology_free_rank':81,
       'Smith_3_valuations':dict(sorted(Counter(values).items())),
       'precision':precision,
       'exact_rank_upper_bound':'(164-(-2))/2=83'},
     'finite_affine_automorphisms':{
       'order':54,'invariant_dimensions':dimensions,
       'multidegree_dimensions':degrees,'character_rows':rows},
     'arithmetic_cocycle_vector_evaluated':False,'checks_passed':True}
Path(__file__).with_name('class_three_symmetry_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({**out,'finite_affine_automorphisms':{k:v for k,v in out['finite_affine_automorphisms'].items() if k!='character_rows'}},indent=2))
