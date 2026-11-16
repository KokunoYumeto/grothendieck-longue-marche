"""Exact Gaussian-integer full Fox-chain peripheral identities for D4.

All1024 fourth-root characters and all five chain coordinates are retained.
Integer arithmetic is checked for overflow before every matrix product.
No identity is extrapolated from a finite-field reduction.
"""
from pathlib import Path
from math import lcm
import json
import numpy as np

ROOT=Path(__file__).resolve().parents[2]
F=json.loads((ROOT/'agent_lifting'/'records'/'f5_nielsen_fox.json').read_text())
N=1024;d=5
chars=np.array([[(k//(4**j))%4 for j in range(5)]for k in range(N)],dtype=np.int64)
weights=np.array([4**j for j in range(5)],dtype=np.int64)
IP=np.arange(N);IR=np.broadcast_to(np.eye(d,dtype=np.int64),(N,d,d)).copy();ZI=np.zeros_like(IR)
ONE=(IP,IR,ZI)
rr=np.array([1,0,-1,0],dtype=np.int64);ri=np.array([0,1,0,-1],dtype=np.int64)
max_entry=0
def cmm(ar,ai,br,bi):
    global max_entry
    ma=max(int(np.max(np.abs(ar))),int(np.max(np.abs(ai))))
    mb=max(int(np.max(np.abs(br))),int(np.max(np.abs(bi))))
    assert 2*ar.shape[-1]*ma*mb < 2**62,'integer product overflow guard'
    cr=ar@br-ai@bi;ci=ar@bi+ai@br
    max_entry=max(max_entry,int(np.max(np.abs(cr))),int(np.max(np.abs(ci))))
    return cr,ci
def mul(g,h):
    r,i=cmm(g[1][h[0]],g[2][h[0]],h[1],h[2]);return g[0][h[0]],r,i
def same(g,h):return all(np.array_equal(a,b)for a,b in zip(g,h))
def prod(*gg):
    out=ONE
    for g in gg:out=mul(out,g)
    return out
def power(g,n):
    out=ONE
    while n:
        if n&1:out=mul(out,g)
        g=mul(g,g);n//=2
    return out
def generator(name):
    ni=name[:-4]if name.endswith('_inv')else name+'_inv'
    eta=chars@np.array(F['abelianization_matrices'][ni],dtype=np.int64)%4
    p=eta@weights;ar=np.zeros((N,d,d),dtype=np.int64);ai=np.zeros_like(ar)
    for i,row in enumerate(F['fox_abelianized'][name]):
        for j,terms in enumerate(row):
            for t in terms:
                phase=eta@np.array(t['monomial'],dtype=np.int64)%4
                ar[:,i,j]+=t['coefficient']*rr[phase]
                ai[:,i,j]+=t['coefficient']*ri[phase]
    br,bi=rr[chars]-1,ri[chars]
    pr,pi=cmm(br[p,None,:],bi[p,None,:],ar,ai)
    assert np.array_equal(pr[:,0,:],br)and np.array_equal(pi[:,0,:],bi)
    return p,ar,ai
G={n:generator(n)for n in F['free_group_images']}
for name in('a','b','c'):
    assert same(mul(G[name],G[name+'_inv']),ONE)
    assert same(mul(G[name+'_inv'],G[name]),ONE)
a,b,c=[G[n]for n in('a','b','c')];aa,bb,cc=[G[n+'_inv']for n in('a','b','c')]
assert same(prod(a,b,a),prod(b,a,b))
assert same(prod(b,c,b),prod(c,b,c))
assert same(mul(a,c),mul(c,a))
assert same(power(prod(a,b,c),4),ONE)
X=[power(a,2),power(b,2),power(c,2),power(prod(a,b,a),2),power(prod(c,b,c),2)]
Xi=[power(aa,2),power(bb,2),power(cc,2),power(prod(aa,bb,aa),2),power(prod(cc,bb,cc),2)]
assert all(same(mul(g,h),ONE)and same(mul(h,g),ONE)for g,h in zip(X,Xi))

def perm_order(p):
    unseen=set(range(N));oo=1
    while unseen:
        q=min(unseen);length=0
        while q in unseen:unseen.remove(q);length+=1;q=int(p[q])
        oo=lcm(oo,length)
    return oo
def certify(name,g):
    po=perm_order(g[0]);assert po&(po-1)==0
    # A harmless extra factor two allows semisimple signs on fixed characters.
    for m in (po,2*po,4*po):
        h=power(g,m);assert np.array_equal(h[0],IP)
        nr,ni=h[1]-IR,h[2];vr,vi=nr.copy(),ni.copy()
        for exponent in range(1,6):
            if not np.any(vr)and not np.any(vi):
                return {'peripheral':name,'character_permutation_order':po,
                        'two_power_m':m,'nilpotence_exponent_r':exponent,
                        'exact_identity':'(g^m-I)^r=0 over Z[i]'}
            if exponent<5:vr,vi=cmm(vr,vi,nr,ni)
    raise AssertionError('No certified two-power unipotent exponent in stated bounds')

reports=[certify('X'+str(i+1),g)for i,g in enumerate(X)]
for i,j in((2,3),(4,0),(1,2),(3,4),(0,1)):
    reports.append(certify('(X'+str(i+1)+'X'+str(j+1)+')^-1',mul(Xi[j],Xi[i])))

# Verify the exact model reduces to the previously independent F9 target.
D=np.load(ROOT/'agent_five'/'ferrari_d4_fox.npz')
for i,g in enumerate(X):
    assert np.array_equal(g[0],D['X_permutations'][i])
    assert np.array_equal(g[1]%3+3*(g[2]%3),D['X_blocks'][i])
out={'coefficient_ring':'Z[i], i^2=-1; separate exact int64 real and imaginary arrays',
     'characters':1024,'full_chain_dimension_per_character':5,
     'all_six_integral_Fox_boundary_identities':True,
     'all_L_relators_and_inverses_over_Z_i':True,
     'exact_reduction_matches_F9_model':True,
     'overflow_guard_checked_before_every_product':True,
     'largest_absolute_intermediate_integer':max_entry,
     'peripheral_certificates':reports,
     'consequence':'At every odd prime ell, each peripheral has procyclic image with primes only2 andell. Thus e3 kills all five Xi whenever ell differs from3.',
     'scope':'Exact integral source identities; no GT lift or full pentagon conclusion is inferred without the separate controlled-seed argument.'}
dest=ROOT/'agent_lifting'/'records'
(dest/'d4_integral_peripherals.json').write_text(json.dumps(out,indent=2)+'\n')
np.savez_compressed(dest/'d4_integral_fox.npz',characters=chars,
    generator_permutations=np.stack([g[0]for g in(a,b,c)]),
    generator_real=np.stack([g[1]for g in(a,b,c)]),generator_imag=np.stack([g[2]for g in(a,b,c)]),
    X_permutations=np.stack([g[0]for g in X]),X_real=np.stack([g[1]for g in X]),X_imag=np.stack([g[2]for g in X]))
print(json.dumps(out,indent=2))
