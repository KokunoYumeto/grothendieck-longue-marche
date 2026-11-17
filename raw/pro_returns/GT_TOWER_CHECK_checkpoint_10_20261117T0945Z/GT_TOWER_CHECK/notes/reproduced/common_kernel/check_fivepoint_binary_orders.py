#!/usr/bin/env python3
"""Exact generator orders and divided abelian map of the common source."""
from pathlib import Path
import json
import numpy as np
HERE=Path(__file__).resolve().parent
d=np.load(HERE/'check_fivepoint_binary_module.npz')
m=json.loads((HERE/'check_fivepoint_binary_module.json').read_text())
table=d['source_table'];gens=d['source_generators'];chords=d['source_chords']
Q=d['common_projection'];L=d['projection_left_inverse']
ci={tuple(row):i for i,row in enumerate(chords.tolist())}
inv=np.array([int(np.flatnonzero(table[q]==0)[0]) for q in range(288)])
def mul(a,b):return int(table[a,b])
def power(a,n):
    q=0
    for _ in range(n):q=mul(q,a)
    return q
assert all(power(int(g),6)==0 for g in gens)
assert all(power(int(g),n)!=0 for g in gens for n in (1,2,3))
x,y=map(int,gens)
c=mul(mul(mul(x,y),inv[x]),inv[y])
conjugates={mul(mul(q,c),inv[q]) for q in range(288)}
derived={0};todo=[0]
for q in todo:
    for g in conjugates:
        v=mul(q,g)
        if v not in derived:derived.add(v);todo.append(v)
assert len(derived)==8

def chain_positive(j,n):
    q=0;v=np.zeros(289,dtype=np.int16)
    for _ in range(n):
        edge=(q,j)
        if edge in ci:v[ci[edge]]+=1
        q=mul(q,int(gens[j]))
    assert q==0
    return v%2
powers=np.array([chain_positive(j,6)@Q%2 for j in (0,1)])
assert all(np.any(v) for v in powers)
assert not np.any(2*powers%2)
print('PASS actual base generators have order6; their sixth powers are nonzero in C2^97',flush=True)
print('PASS actual common-source x,y have exact order12',flush=True)

exponents=np.array([[sum((1 if z==j else -1 if z==-j else 0) for z in w)
                     for j in (1,2)] for w in m['Schreier_words']],dtype=np.int16)
assert not np.any(exponents%6)
divided=exponents//6%2
factor=L@divided%2
assert np.array_equal(Q@factor%2,divided)
assert np.array_equal(powers@factor%2,np.eye(2,dtype=np.int16))
print('PASS divided exponent map factors exactly through the97-dimensional source kernel',flush=True)
print('PASS F-image abelianization is exactly C12^2 with the original named generators',flush=True)

# Modulo two, the same original signed marking has independent x,y values.
theta=json.loads((HERE/'check_fivepoint_signed_retraction.json').read_text())['theta_generators']
red4=[tuple(v%4 for v in g) for g in theta]
assert red4==[(1,2,0,1),(1,0,2,1)]
print('PASS source C2^2 abelian reduction is already retained in the signed modulo-four map',flush=True)
out={'scope':'Exact source orders and abelian normalization, not a profinite lifting theorem',
     'base_order':288,'base_derived_order':8,'base_abelianization':'C6^2',
     'x_order':12,'y_order':12,'pure_abelianization':'C12^2',
     'divided_exponent_factorization':True,'mod2_abelian_retained_in_theta4':True,
     'sixth_power_coordinates':powers.tolist(),'all_assertions_passed':True}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(Path(__file__).with_suffix('.npz'),exponents=exponents,
                    divided_exponents=divided,common_exponent_factor=factor,
                    sixth_powers=powers)
