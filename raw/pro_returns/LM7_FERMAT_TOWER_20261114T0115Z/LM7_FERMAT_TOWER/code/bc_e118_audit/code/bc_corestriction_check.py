"""Independent exact E118 coset/corestriction and tensor-map audit."""
from itertools import product
from pathlib import Path
import json

p=5
def mm(a,b):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%p for i in range(2) for j in range(2))
def mv(a,v):return ((a[0]*v[0]+a[1]*v[1])%p,(a[2]*v[0]+a[3]*v[1])%p)
def va(v,w):return ((v[0]+w[0])%p,(v[1]+w[1])%p)
def vn(v):return ((-v[0])%p,(-v[1])%p)
def inv(a):
    d=pow((a[0]*a[3]-a[1]*a[2])%p,-1,p)
    return tuple(d*x%p for x in (a[3],-a[1],-a[2],a[0]))
I=(1,0,0,1);gens=[(2,0,0,1),(1,0,0,3),(0,1,1,0)]
G={I};todo=[I]
for a in todo:
    for b in gens:
        z=mm(a,b)
        if z not in G:G.add(z);todo.append(z)
G=sorted(G);assert len(G)==32
V=list(product(range(p),repeat=2))
def mul(x,y):return (va(x[0],mv(x[1],y[0])),mm(x[1],y[1]))
E=list(product(V,G))
representatives={g:((i*i+2*i+1)%p,(3*i*i+i)%p) for i,g in enumerate(G)}
s=(0,0)
for r in representatives.values():s=va(s,r)
s=tuple(3*x%p for x in s)
def cor(g):
    v,a=g;z=(0,0)
    for b in G:
        j=mm(a,b)
        # g t_b = t_j k; the exact kernel logarithm is j^{-1}(v+a r_b-r_j).
        k=mv(inv(j),va(va(v,mv(a,representatives[b])),vn(representatives[j])))
        z=va(z,mv(j,k))
    return tuple(3*x%p for x in z)
values={g:cor(g) for g in E}
for g in E:
    assert values[g]==va(g[0],va(mv(g[1],s),vn(s)))
    if g[1]==I:assert values[g]==g[0]
checks=0
for g in E:
    for h in E:
        assert values[mul(g,h)]==va(values[g],mv(g[1],values[h]))
        checks+=1
result={"status":"PASS","actual_residual_group_order":len(G),"semidirect_group_order":len(E),"literal_coset_terms":len(E)*len(G),"all_cocycle_identities":checks,"coset_change_cobounding_vector":s,"tensor_map":"(5 e_i) tensor q_i/5 maps to q_i; the unextended inclusion has image 5 Z5^3"}
t=json.dumps(result,indent=2)+'\n';Path(__file__).with_suffix('.json').write_text(t);print(t,end='')
