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
assert np.array_equal(Ti@T%3,I)
for key in ('A','B','C'):
    graded=Ti@D[key].astype(np.int64)@T%3
    assert np.array_equal(graded,BD[key])
    assert not np.any(graded[np.ix_(pi,bi)])
for original,converted in zip(D['X'],BD['X']):
    assert np.array_equal(Ti@original.astype(np.int64)@T%3,converted)

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

# Independent original signed level-twelve value of the same source word.
def m12(a,b):return a@b%12
def i12(a):
    aa,bb,cc,dd=map(int,a.ravel())
    assert (aa*dd-bb*cc)%12==1
    return np.array([[dd,-bb],[-cc,aa]],dtype=np.int64)%12
def p12(a,n):
    b=np.eye(2,dtype=np.int64)
    for _ in range(n):b=m12(b,a)
    return b
def c12(a,b):return m12(m12(m12(a,b),i12(a)),i12(b))
def a12(x,y):
    u,v,w=[p12(g,4)for g in(x,y,i12(m12(x,y)))]
    return c12(c12(u,v),c12(v,w))
x12=np.array([[1,2],[0,1]],dtype=np.int64)
y12=np.array([[1,0],[10,1]],dtype=np.int64)
z12=i12(m12(x12,y12))
for pp in permutations(range(3)):
    u,v=[(x12,y12,z12)[j]for j in pp[:2]]
    w=i12(m12(u,v))
    cyc12=m12(m12(a12(v,w),a12(u,v)),a12(w,u))
    assert np.array_equal(cyc12,5*np.eye(2,dtype=np.int64))

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
        assert order(cyc) in (1,6)
        assert all(same(mul(two,g),mul(g,two))for g in(x,y))
        assert np.array_equal(graded_three[np.ix_(bi,bi)],np.eye(63,dtype=np.int64))
        assert np.array_equal(graded_three[np.ix_(pi,pi)],np.eye(66,dtype=np.int64))
        assert not np.any(graded_three[np.ix_(pi,bi)])
        # The only 2-primary action occurs in the canonical trivial
        # C'/D-character piece of rank five; all other 124 coordinates,
        # including their affine translations, have trivial 2-primary part.
        char_two=BC['basis_inverse'].astype(np.int64)@two[1]@BC['basis'].astype(np.int64)%3
        char_translation=BC['basis_inverse'].astype(np.int64)@two[0]%3
        assert np.array_equal(char_two[5:,5:],np.eye(124,dtype=np.int64))
        assert not np.any(char_two[:5,5:])and not np.any(char_two[5:,:5])
        assert not np.any(char_translation[5:])
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
     'cyclic_seed_has_nilpotent_normal_closure_in_every_pair_core_image':True,
     'two_primary_part_identity_on_all_nontrivial_deck_character_affine_pieces':True,
     'trivial_deck_character_dimension':5,
     'complementary_affine_dimension':124,
     'reason':'Its cube is a central 2-element; its fourth power is in the normal 3-group kernel of the affine boundary/proper graded action.',
     'same_word_pair_and_peripheral_core_evaluations':records,
     'scope':'Controlled actual-source seed plus nilpotent-normal-image certificate. The accompanying RA.3 applies R2 and compactness to obtain an actual gentle Delta1 witness satisfying this affine-source pentagon. No full GT lift is asserted.'}
p=ROOT/'agent_lifting'/'records'/'rank129_affine_seed.json'
p.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
