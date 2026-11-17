"""Exact obstruction to extending the finite-Frattini single-prime argument."""
from pathlib import Path
from collections import deque
import json

MOD=0b1000011
def mul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
        if a&64:a^=MOD
    return c
def power(a,n):
    b=1
    while n:
        if n&1:b=mul(a,b)
        a=mul(a,a);n>>=1
    return b
assert all(power(a,63)==1 for a in range(1,64))
zeta=power(2,7);lam=power(2,9)
assert power(zeta,9)==1 and power(zeta,3)!=1
assert power(lam,7)==1 and lam!=1
sp=[power(zeta,i) for i in range(9)]
span={0}
for x in sp:span|={a^x for a in tuple(span)}
assert len(span)==64
G=[(a,i) for a in range(64) for i in range(9)]
def product(x,y):return x[0]^mul(sp[x[1]],y[0]),(x[1]+y[1])%9
def alpha(x):return mul(lam,x[0]),x[1]
assert all(alpha(product(x,y))==product(alpha(x),alpha(y)) for x in G for y in G)
visited={(0,0)};queue=deque(visited)
while queue:
    x=queue.popleft()
    for g in ((1,0),(0,1)):
        y=product(x,g)
        if y not in visited:visited.add(y);queue.append(y)
assert len(visited)==576
commutators={mul(zeta^1,a) for a in range(64)}
assert commutators==set(range(64))
# Intersection of the conjugates of H={0}xC9 by all translations.
core=set((0,i) for i in range(9))
for a in range(64):
    core.intersection_update((a^mul(sp[i],a),i) for i in range(9))
assert core=={(0,0)}
for x in G:
    y=x
    for _ in range(7):y=alpha(y)
    assert y==x
assert alpha((1,0))!=(1,0)
result={'verified':True,'group':'F64(additive) semidirect C9','group_order':len(G),
        'field_modulus_bits':MOD,'zeta9_bits':zeta,'lambda7_bits':lam,
        'two_generators':[[1,0],[0,1]],'generated_order':len(visited),
        'H_irreducible_module_span':len(span),'complement_core':sorted(core),
        'derived_group_order':len(commutators),'abelianization':'C9',
        'automorphism_order':7,'automorphism_formula':'(a,i) -> (lambda7*a,i)',
        'automorphism_trivial_on_abelianization':True,
        'scope':'Finite group counterexample to an abelianization-kernel inference; not a point-section collision.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
