"""One exact regional prefix-basis obstruction, with a prescribed finite detector.

No group census: construct the orbit map of one S3 representation of the
proved m=4 graph head, and check every actual regional relation.
"""
from pathlib import Path
from itertools import product as cartesian
import json,hashlib
from datetime import datetime, timezone
ROOT=Path(__file__).resolve().parents[1]
src=ROOT/'work_CE/next_symmetric_nodes/annular_neck_presentation23.json'
D=json.loads(src.read_text())
def red(w):
    r=[]
    for x in w:
        if r and r[-1]==-x:r.pop()
        else:r.append(x)
    return tuple(r)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(z for x in w for z in(A[x]if x>0 else inv(A[-x])))
O={1:(1,2,-1),2:(1,),3:(5,3,4,-3,-5),4:(3,),5:(-3,5,3)}
KO={1:(2,),2:(-2,1,2),3:(4,),4:(-5,-4,3,4,5),5:(4,5,-4)}
P={i:tuple(range(1,i+1))for i in range(1,6)}
Pinv={1:(1,),**{i:(-(i-1),i)for i in range(2,6)}}
phi={i:sub(sub(KO[i],P),O)for i in range(1,6)}
phi_inv={i:sub(sub(KO[i],Pinv),O)for i in range(1,6)}
for i in range(1,6):
    assert sub(phi[i],phi_inv)==sub(phi_inv[i],phi)==(i,)
assert phi[1]==(1,2) # a maps to a B, in the ACTUAL common K basis.

identity=(0,1,2);s=(1,0,2);t=(1,2,0)
def pm(p,q):return tuple(p[q[i]]for i in range(3))
def pi(p):return tuple(p.index(i)for i in range(3))
F=list(cartesian(range(4),range(2)))
vertices=[(u,n,b)for u in 'abde'for n in range(4)for b in range(2)]+[('k',0,b)for b in range(2)]
def act(v,h,p):
    u,n,b=v
    return (u,0,b^(h%2)^p)if u=='k'else(u,(n+h)%4,b^p)
def adjacent(v,w):
    u,n,b=v;u2,n2,b2=w
    if v==w:return True
    if u==u2=='k':return False
    if u=='k':return b==((n2%2)^b2)
    if u2=='k':return b2==((n%2)^b)
    if u==u2 and n==n2 and b!=b2:return True
    pair=frozenset((u,u2))
    if n==n2:
        if pair==frozenset(('a','b')):return b==b2
        if pair in[frozenset(x)for x in[('a','d'),('a','e'),('d','e')]]:return b!=b2
    if u=='b'and u2 in'de'and n2==(n+1)%4:return b==b2
    if u2=='b'and u in'de'and n==(n2+1)%4:return b==b2
    return False
def seed(v):return s if v==('k',0,0)else t if v==('b',0,1)else identity
edges=[]
for i,v in enumerate(vertices):
    for w in vertices[i+1:]:
        if adjacent(v,w):
            edges.append((v,w))
            assert pm(seed(v),seed(w))==pm(seed(w),seed(v))
        for h,p in F:assert adjacent(v,w)==adjacent(act(v,h,p),act(w,h,p))
assert not adjacent(('k',0,0),('b',0,1))
# Actual Y labels:1a,2b,3C,4f,5d,6e,7h,8k; f=h k^-1.
def evaluate(w):
    expanded=[]
    for x in w:expanded.extend((7,-8)if x==4 else(8,-7)if x==-4 else(x,))
    values=[identity for _ in F];h=p=0
    ordinary={1:'a',2:'b',5:'d',6:'e'}
    for x in expanded:
        if abs(x)==3:p^=1
        elif abs(x)==7:h=(h+(1 if x>0 else -1))%4
        else:
            v=('k',0,0)if abs(x)==8 else(ordinary[abs(x)],0,0)
            v=act(v,h,p)
            for j,(q,r)in enumerate(F):
                image=seed(act(v,-q,r))
                values[j]=pm(values[j],image if x>0 else pi(image))
    return tuple(values),(h,p)
unit=(tuple(identity for _ in F),(0,0))
GY={1:(1,),2:(3,2,3),3:(5,),4:(6,),5:(4,),6:(3,),8:(8,)}
regional=[r for r in D['regional_relators']if r['side']=='minus']
for r in regional:assert evaluate(sub(r['word'],GY))==unit,r['name']
assert evaluate((3,3))==unit
before=(8,1,-8,-1)
after=sub((8,1,-8,-1),{8:(8,),1:sub(phi[1],GY)})
assert evaluate(before)==unit
value=evaluate(after);assert value!=unit and value[1]==(0,0)
out={'status':'PASS_EXACT_FIXED_BASE_PREFIX_OBSTRUCTION',
 'recorded_at':datetime.now(timezone.utc).isoformat(),
 'input_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),
 'prefix_automorphism_on_K':phi,'inverse_on_K':phi_inv,
 'regional_finite_head':{'period':4,'graph_vertices':len(vertices),'graph_edges':len(edges),'acting_group':'C4 times C2'},
 'finite_target':'S3^8 semidirect (C4 times C2), with regular coordinate action',
 'seed_nontrivial_vertices':{'k0':s,'bar_b0':t},
 'all_graph_relations_and_acting_automorphisms_checked':True,
 'actual_regional_relations_checked':len(regional)+1,
 'original_commutator':before,'prefix_image_commutator':after,
 'image_coordinate_permutations':value[0],
 'nonidentity_coordinates':[F[j]for j,p in enumerate(value[0])if p!=identity],
 'scope':'The actual automorphism O_i -> O1...Oi of common K cannot extend to a regional homomorphism fixing k, in either discrete or full profinite category. No arbitrary simultaneous graph-basis change or section correction is excluded.'}
(ROOT/'records/prefix_fixed_base_obstruction23.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS ten literal inverse prefix substitutions; phi(a)=a B.')
print('PASS finite graph and action:',len(vertices),'vertices,',len(edges),'edges; all17 actual regional relators.')
print('PASS [k,a]=1 but [k,phi(a)] has nonidentity finite image at',out['nonidentity_coordinates'])
print('Scope: any extension fixing the actual regional k is excluded; simultaneous corrected sections remain open.')
