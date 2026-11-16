"""Actual R2-seed test and canonical signed SL2(F3) quotient at rank129.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
from itertools import permutations
import json,numpy as np

HERE=Path(__file__).resolve().parents[1]
D=np.load(HERE.parent/'agent_five'/'ferrari_rank129.npz')
R=json.loads((HERE/'records'/'integral_ferrari_homology.json').read_text())
chords=[tuple(x)for x in R['non_tree_edges']];ci={e:j for j,e in enumerate(chords)}
Q=D['Q'];edges=D['edges'];cycles=D['cycles'].astype(np.int64)
proj=np.zeros((5,384),dtype=np.int64)
for j,(q,r,i)in enumerate(edges):
    v=int(Q[q,1]);w=v^(1<<int(i));edge=(min(v,w),max(v,w))
    if edge in ci:proj[ci[edge],j]=1 if v<w else -1
P=proj@cycles%3
K=np.zeros((2,5),dtype=np.int64)
for j,word in enumerate(R['free_basis_in_involutions']):
    sg=1
    for t in word:
        if t:K[t-1,j]+=sg
        sg=-sg
    assert sg==1
T=K@P%3
assert any((T[0,i]*T[1,j]-T[0,j]*T[1,i])%3 for i in range(129)for j in range(i+1,129))
U=np.array([[1,1],[0,1]],dtype=np.int64)
L=np.array([[1,0],[2,1]],dtype=np.int64)
for name,M in (('A',U),('B',L),('C',U)):
    assert np.array_equal(T@D[name].astype(np.int64)%3,M@T%3)

X=D['X'].astype(np.int64);I=np.eye(129,dtype=np.int64)
def mul(a,b):return a@b%3
def power(a,n):
    out=I
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
def order(a,bound=256):
    out=I
    for n in range(1,bound+1):
        out=mul(out,a)
        if np.array_equal(out,I):return n
    raise AssertionError('order outside stated bound')
def idempotent3(o):
    p=1
    while o%3==0:p*=3;o//=3
    return 0 if p==1 else o*pow(o,-1,p)
x,y=X[:2];z=mul(power(y,5),power(x,5));trip=(x,y,z)
orders=[order(g)for g in trip];assert orders==[6,6,12]
records=[];first=None
for perm in permutations(range(3)):
    u,v,w=[trip[i]for i in perm];ou,ov,ow=[orders[i]for i in perm]
    zz=mul(power(v,ov-1),power(u,ou-1))
    U1,V1,Z1=power(u,idempotent3(ou)),power(v,idempotent3(ov)),power(zz,idempotent3(ow))
    Ui,Vi,Zi=power(u,-idempotent3(ou)%ou),power(v,-idempotent3(ov)%ov),power(zz,-idempotent3(ow)%ow)
    c1=mul(mul(mul(U1,V1),Ui),Vi);c1i=mul(mul(mul(V1,U1),Vi),Ui)
    c2=mul(mul(mul(V1,Z1),Vi),Zi);c2i=mul(mul(mul(Z1,V1),Zi),Vi)
    value=mul(mul(mul(c1,c2),c1i),c2i)
    o=order(value);assert o==6
    records.append({'peripheral_permutation':perm,'seed_order':o})
    if first is None:first=value
assert np.array_equal(T@first%3,-T%3)
involution=power(first,3)
assert not np.array_equal(mul(involution,x),mul(x,involution))
assert not np.array_equal(mul(involution,y),mul(y,involution))
out={'harmonic_peripheral_orders':orders,'e3_exponents':[idempotent3(o)for o in orders],
     'six_core_seed_values':records,'cube_is_noncentral_involution':True,
     'canonical_signed_compact_quotient_rank':2,
     'canonical_quotient_intertwines_a_b_c_with':['U','L0','U'],
     'seed_projects_to_negative_identity':True,
     'actual_seed_obstruction':'Every source A with q12(A)=5I has signed compact projection -I, hence cannot lie in this full harmonic evaluation kernel. This does not rule out a residual lift through a nilpotent normal image.',
     'scope':'Actual source quotient and controlled R2 seed test; no finite GT assignment or Delta implication.'}
np.savez_compressed(HERE/'records'/'rank129_compact_intertwiner.npz',compact_intertwiner=T,
                    cube_cover_homology_map=P,K_abelianization=K)
(HERE/'records'/'rank129_seed_and_quotient.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
