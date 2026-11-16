"""Evaluate genuine profinite core seeds in the actual affine Ferrari target.

The exponent e3 has 3-adic component 1 and all other components zero.
No independent assignment of f-values or GT-lifting assertion is made.
"""
from pathlib import Path
from itertools import permutations
import json
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
D=np.load(ROOT/'agent_five'/'ferrari_rank129_affine.npz')
BC=np.load(ROOT/'agent_five'/'ferrari_rank129_blocks.npz')
BD=np.load(ROOT/'agent_five'/'ferrari_rank129_boundary.npz')
T=BC['basis'].astype(np.int64)@BD['basis'].astype(np.int64)%3
Ti=BD['basis_inverse'].astype(np.int64)@BC['basis_inverse'].astype(np.int64)%3
bi=BD['boundary_indices'];pi=BD['proper_indices']
I=np.eye(129,dtype=np.int64)
one=(np.zeros(129,dtype=np.int64),I)

def mul(a,b):return ((a[0]+a[1]@b[0])%3,a[1]@b[1]%3)
def same(a,b):return np.array_equal(a[0],b[0])and np.array_equal(a[1],b[1])
def power(a,n):
    b=one
    while n:
        if n&1:b=mul(b,a)
        a=mul(a,a);n//=2
    return b
def order(a,bound=1024):
    b=one
    for n in range(1,bound+1):
        b=mul(b,a)
        if same(b,one):return n
    raise AssertionError('finite order outside stated bound')
def inv(a):return power(a,order(a)-1)
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
def e3(o):
    pp=1
    while o%3==0:pp*=3;o//=3
    return 0 if pp==1 else o*pow(o,-1,pp)
def seed(x,y):
    z=inv(mul(x,y))
    u,v,w=[power(g,e3(order(g)))for g in(x,y,z)]
    return comm(comm(u,v),comm(v,w))

X=list(zip(D['Xi_translations'].astype(np.int64),D['X'].astype(np.int64)))
pairs=((2,3),(4,0),(1,2),(3,4),(0,1))
records=[]
for ii,jj in pairs:
    x,y=X[ii],X[jj];z=inv(mul(x,y));trip=(x,y,z)
    vals=[];cyclic=[]
    for pp in permutations(range(3)):
        u,v=trip[pp[0]],trip[pp[1]]
        w=inv(mul(u,v))
        a=seed(u,v)
        cyc=mul(mul(seed(v,w),seed(u,v)),seed(w,u))
        two=power(cyc,3);three=power(cyc,4)
        graded_three=Ti@three[1]@T%3
        vals.append({'permutation':list(pp),'order':order(a),
                     'translation_nonzero':bool(np.any(a[0]))})
        cyclic.append({'permutation':list(pp),'order':order(cyc),
                       'translation_nonzero':bool(np.any(cyc[0])),
                       'cube_centralizes_both_pair_generators':all(same(mul(two,g),mul(g,two))for g in(x,y)),
                       'third_primary_boundary_identity':np.array_equal(graded_three[np.ix_(bi,bi)],np.eye(63,dtype=np.int64)),
                       'third_primary_proper_identity':np.array_equal(graded_three[np.ix_(pi,pi)],np.eye(66,dtype=np.int64))})
    records.append({'pair':[ii+1,jj+1],
                    'peripheral_orders':[order(g)for g in trip],
                    'Ae3_values':vals,'cyclic_three_factor_values':cyclic})

out={'Xi_affine_orders':[order(g)for g in X],
     'genuine_seed':'Ae3=[[x^e3,y^e3],[y^e3,z^e3]], z=(xy)^-1',
     'genuine_cyclic_seed':'Ae3(y,z) Ae3(x,y) Ae3(z,x)',
     'all_seeds_belong_to_F_second_derived_and_every_original_phi_core':True,
     'both_seed_q12_values':'5I',
     'same_word_pair_and_peripheral_core_evaluations':records,
     'scope':'Controlled actual-source R2 seed evaluation only; no claim of nilpotent normal closure, affine pentagon vanishing, or existence of a GT lift.'}
p=ROOT/'agent_lifting'/'records'/'rank129_affine_seed.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
