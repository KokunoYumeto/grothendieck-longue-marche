"""Independent D4 chain/controlled-seed audit from Fox Laurent input.

No arithmetic, group operations, or generator matrices are imported from
the construction.  The other certificate's arrays are compared only after
the independent calculation.
"""
from pathlib import Path
from math import lcm
import json
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
N=1024;d=5
F=json.loads((ROOT/'agent_lifting'/'records'/'f5_nielsen_fox.json').read_text())
chars=np.array([[(k//(4**j))%4 for j in range(5)]for k in range(N)],dtype=np.int64)
weights=np.array([4**j for j in range(5)],dtype=np.int64)
ADD=np.array([[(a%3+b%3)%3+3*((a//3+b//3)%3)for b in range(9)]for a in range(9)],dtype=np.int64)
MUL=np.array([[((a%3)*(b%3)-(a//3)*(b//3))%3+3*(((a%3)*(b//3)+(a//3)*(b%3))%3)for b in range(9)]for a in range(9)],dtype=np.int64)
ROOTS=np.array([1,3,2,6],dtype=np.int64)
IP=np.arange(N);IM=np.broadcast_to(np.eye(d,dtype=np.int64),(N,d,d)).copy();ONE=(IP,IM)

def mm(A,B):
    C=np.zeros(np.broadcast_shapes(A.shape[:-2],B.shape[:-2])+(A.shape[-2],B.shape[-1]),dtype=np.int64)
    for k in range(A.shape[-1]):C=ADD[C,MUL[A[..., :,k,None],B[...,None,k,:]]]
    return C
def mul(g,h):return(g[0][h[0]],mm(g[1][h[0]],h[1]))
def same(g,h):return np.array_equal(g[0],h[0])and np.array_equal(g[1],h[1])
def power(g,n):
    h=ONE
    while n:
        if n&1:h=mul(h,g)
        g=mul(g,g);n//=2
    return h
def prod(*args):
    h=ONE
    for g in args:h=mul(h,g)
    return h
def generator(name):
    inverse_name=name[:-4]if name.endswith('_inv')else name+'_inv'
    Tinv=np.array(F['abelianization_matrices'][inverse_name],dtype=np.int64)
    eta=chars@Tinv%4;p=eta@weights;J=np.zeros((N,5,5),dtype=np.int64)
    for i,row in enumerate(F['fox_abelianized'][name]):
        for j,terms in enumerate(row):
            for term in terms:
                phases=eta@np.array(term['monomial'],dtype=np.int64)%4
                J[:,i,j]=ADD[J[:,i,j],MUL[term['coefficient']%3,ROOTS[phases]]]
    boundary=ADD[ROOTS[chars],2]
    assert np.array_equal(mm(boundary[p,None,:],J)[:,0,:],boundary)
    return p,J
G={name:generator(name)for name in F['free_group_images']}
for name in('a','b','c'):
    assert same(mul(G[name],G[name+'_inv']),ONE)
    assert same(mul(G[name+'_inv'],G[name]),ONE)
a,b,c=[G[k]for k in('a','b','c')]
assert same(prod(a,b,a),prod(b,a,b))
assert same(prod(b,c,b),prod(c,b,c))
assert same(mul(a,c),mul(c,a))
assert same(power(prod(a,b,c),4),ONE)
X=[power(a,2),power(b,2),power(c,2),power(prod(a,b,a),2),power(prod(c,b,c),2)]
control=np.load(ROOT/'agent_five'/'ferrari_d4_fox.npz')
assert np.array_equal(chars,control['characters'])
for j,g in enumerate((a,b,c)):
    assert np.array_equal(g[0],control['generator_permutations'][j])
    assert np.array_equal(g[1],control['generator_blocks'][j])
for j,g in enumerate(X):
    assert np.array_equal(g[0],control['X_permutations'][j])
    assert np.array_equal(g[1],control['X_blocks'][j])

# Canonical harmonic triple, with orders independently checked.
x,y=X[:2];xi,yi=power(x,11),power(y,11)
assert same(power(x,12),ONE)and not same(power(x,6),ONE)and not same(power(x,4),ONE)
assert same(power(y,12),ONE)and not same(power(y,6),ONE)and not same(power(y,4),ONE)
z=mul(yi,xi);zi=mul(x,y)
assert same(power(z,24),ONE)and not same(power(z,12),ONE)and not same(power(z,8),ONE)
u=[power(x,4),power(y,4),power(z,16)]
ui=[power(xi,4),power(yi,4),power(zi,16)]
for g in u:assert same(power(g,3),ONE)
def A(i,j,k):
    c1=prod(u[i],u[j],ui[i],ui[j]);c1i=prod(u[j],u[i],ui[j],ui[i])
    c2=prod(u[j],u[k],ui[j],ui[k]);c2i=prod(u[k],u[j],ui[k],ui[j])
    return prod(c1,c2,c1i,c2i)
s=prod(A(1,2,0),A(0,1,2),A(2,0,1))
assert np.array_equal(s[0],IP)
assert same(power(s,6),ONE)and not same(power(s,3),ONE)and not same(power(s,2),ONE)
stored=np.load(ROOT/'agent_five'/'ferrari_d4_controlled_seed.npz')['seed_blocks']
assert np.array_equal(s[1],stored[24])
t=power(s,3);assert same(power(t,2),ONE)

EXP=9*lcm(*(9**j-1 for j in range(1,6)))
PRIMES=(2,3,5,7,11,13,41,61)
def block_order(g):
    assert np.array_equal(g[0],IP)
    assert same(power(g,EXP),ONE)
    n=EXP
    for p in PRIMES:
        while n%p==0 and same(power(g,n//p),ONE):n//=p
    return n
reports=[]
for name,g,gi in(('x',x,xi),('y',y,yi),('yx',mul(y,x),mul(xi,yi))):
    v=prod(g,t,gi);assert same(power(v,2),ONE)
    tv=mul(t,v);oo=block_order(tv)
    central=same(mul(t,g),mul(g,t))
    bad=np.flatnonzero(np.any(tv[1]!=IM,axis=(1,2)))
    first=int(bad[0])if len(bad)else None
    reports.append({'conjugating_generator':name,'two_involutions_product_order':oo,
                    'seed_involution_centralizes_generator':central,
                    'first_nonidentity_character_index':first,
                    'first_nonidentity_character':chars[first].tolist()if first is not None else None})
    if name=='yx':
        index=81
        assert chars[index].tolist()==[1,0,1,1,0]
        uu,vv,uv=t[1][index],v[1][index],tv[1][index]
        I5=np.eye(5,dtype=np.int64)
        assert np.array_equal(mm(uu,uu),I5)and np.array_equal(mm(vv,vv),I5)
        uv3=mm(mm(uv,uv),uv);uv9=mm(mm(uv3,uv3),uv3)
        assert np.array_equal(uv9,I5)and not np.array_equal(uv3,I5)
        local={'character_index':index,'character':chars[index].tolist(),
               'conjugating_word':'yx','u_is_S_cubed':True,
               'u_matrix':uu.tolist(),'v_matrix':vv.tolist(),
               'uv_matrix':uv.tolist(),'uv_exact_order':9,
               'normal_closure_of_this_seed_nonnilpotent':True}
out={'independent_F9_table_arithmetic':True,
     'all_six_Fox_boundary_identities_all1024_characters':True,
     'all_L_relators_independently_verified':True,
     'all_generator_and_Xi_arrays_match_independent_calculation':True,
     'canonical_harmonic_peripheral_orders':[12,12,24],
     'CRT_e3_exponents':[4,4,16],
     'same_genuine_cyclic_seed_matches_saved_value':True,
     'cyclic_seed_order':6,'seed_cube_is_involution':True,
     'conjugate_involution_reports':reports,
     'local_odd_order_product_certificate':local,
     'scope':'The normal closure of this particular controlled seed S is nonnilpotent. This neither rules out another actual core seed with the same signed value nor proves a Delta implication for GT.'}
path=ROOT/'agent_lifting'/'records'/'d4_seed_independent.json'
path.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
