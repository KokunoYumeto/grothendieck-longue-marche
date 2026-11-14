"""Exact certificates for the enlarged metabelian unit family.

The finite computations certify the Fourier idempotent and concrete
peripheral automorphisms. The arithmetic centralizer conclusion is proved
in A.tex using the exact Chen--Deligne outer automorphism formula.
"""
from fractions import Fraction
from itertools import product
from collections import deque
from pathlib import Path
import json

B = list(product(range(4), repeat=2))
S = {(a,b) for a,b in B if a and b and (a+b)%4}
assert len(S) == 6
assert {(b,a) for a,b in S} == S
assert {((-a-b)%4,b) for a,b in S} == S
assert {((-a)%4,(-b)%4) for a,b in S} == S

ipow = [(1,0),(0,1),(-1,0),(0,-1)]
e = {}
for x,y in B:
    pairs = [ipow[(-a*x-b*y)%4] for a,b in S]
    assert sum(v[1] for v in pairs) == 0
    e[x,y] = Fraction(sum(v[0] for v in pairs),16)

def conv(a,b):
    out = {x:Fraction(0) for x in B}
    for (i,j),v in a.items():
        for (k,l),w in b.items():
            out[(i+k)%4,(j+l)%4] += v*w
    return out

assert conv(e,e) == e
assert sum(e.values()) == 0
assert any(e.values())
for step in [(1,0),(0,1),(1,1)]:
    a = {x:Fraction(0) for x in B}
    a[0,0] = -1
    a[step] += 1
    g = {x:Fraction(0) for x in B}
    for k in range(1,4):
        g[(k*step[0])%4,(k*step[1])%4] += Fraction(k,4)
    assert conv(conv(e,a),g) == e

def finite_certificate(n,order,unit):
    # Z/n[z]/(z^2+z+1) for order 3, Z/n[z]/(z^2+1) for 4.
    def add(a,b): return ((a[0]+b[0])%n,(a[1]+b[1])%n)
    def neg(a): return ((-a[0])%n,(-a[1])%n)
    def mul(a,b):
        c = a[0]*b[0]-a[1]*b[1]
        d = a[0]*b[1]+a[1]*b[0]-(a[1]*b[1] if order==3 else 0)
        return c%n,d%n
    z=(0,1); zpow=[(1,0)]
    for _ in range(order): zpow.append(mul(zpow[-1],z))
    assert zpow[-1] == (1,0)
    elems=[((a,b),k) for a,b,k in product(range(n),range(n),range(order))]
    one=((0,0),0)
    def gm(a,b): return add(a[0],mul(zpow[a[1]],b[0])),(a[1]+b[1])%order
    def gi(a): return mul(zpow[-a[1]%order],neg(a[0])),(-a[1])%order
    def conj(a,b): return gm(gm(gi(a),b),a)
    def phi(a): return mul((unit,0),a[0]),a[1]
    x=((0,0),1); y=((1,0),1); xy=gm(x,y)
    seen={one}; todo=deque([one]); gens=[x,y,gi(x),gi(y)]
    while todo:
        a=todo.popleft()
        for g in gens:
            b=gm(a,g)
            if b not in seen: seen.add(b); todo.append(b)
    assert len(seen)==len(elems)
    assert len({phi(a) for a in elems})==len(elems)
    for a in elems:
        assert gm(a,gi(a)) == one
        for b in elems: assert phi(gm(a,b)) == gm(phi(a),phi(b))
    witnesses={}
    for name,g in [('x',x),('y',y),('xy',xy)]:
        choices=[a for a in elems if conj(a,g)==phi(g)]
        assert choices
        witnesses[name]=choices[0]
    inner=[a for a in elems if conj(a,x)==phi(x) and conj(a,y)==phi(y)]
    assert not inner
    return dict(coefficient_modulus=n,complement_order=order,unit=unit,
                group_order=len(elems),generated=True,
                multiplication_pairs_checked=len(elems)**2,
                bijective=True,peripheral_conjugators=witnesses,noninner=True)

result={
    'coefficient_3_idempotent':{
        'character_set':sorted(S),
        'coefficients':{f'{x},{y}':str(v) for (x,y),v in e.items()},
        'idempotent':True,'augmentation_zero':True,
        'scalar_and_S3_invariant':True,
        'X_minus_1_Y_minus_1_XY_minus_1_invertible_on_block':True},
    'finite_certificates':[finite_certificate(4,3,3),finite_certificate(9,4,2)]}
out=Path(__file__).with_name('metabelian_units_certificate_output.json')
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
