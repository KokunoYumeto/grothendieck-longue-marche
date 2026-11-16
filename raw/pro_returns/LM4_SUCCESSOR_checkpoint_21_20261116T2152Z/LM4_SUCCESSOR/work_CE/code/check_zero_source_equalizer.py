#!/usr/bin/env python3
"""Actual paired-map order64 detector for the specific B86 zero-source word.
All possible central coordinates compatible with the actual peripheral
markings are checked. No larger source-membership search is performed.
"""
from itertools import product
from pathlib import Path
import json, hashlib
import sympy as S
v,w=S.symbols('v w')
f1=v;f2=v*(w-1)/(1-v)
assert S.cancel(f2.subs(w,2-v)-v)==0
assert S.cancel(f2-1-(v*w-1)/(1-v))==0
base={v:S.Rational(399,200),w:S.Rational(1,200)}
assert f1.subs(base)==f2.subs(base)==S.Rational(399,200)
# Primitive local orders of f_i and f_i-1 at a(v=1), b(vw=1),
# and the source zero point (v=0,w=2) establish all abelian coordinates.
t=S.symbols('t')
def order(expr):
    e=S.cancel(expr);num,den=S.fraction(e)
    def valuation(poly):
        P=S.Poly(poly,t)
        return min(m[0] for m,c in P.terms() if c!=0)
    return valuation(num)-valuation(den)
charts={'a':{v:1+t,w:S.Rational(1,200)},
        'b':{v:200*(1+t),w:S.Rational(1,200)},
        'z':{v:t,w:2-t}}
orders={}
for label,chart in charts.items():
    orders[label]=[]
    for f in [f1,f2]:
        orders[label].append([order(f.subs(chart,simultaneous=True)),order((f-1).subs(chart,simultaneous=True))])
assert orders=={'a':[[0,1],[-1,-1]],'b':[[0,0],[0,1]],'z':[[1,0],[1,0]]}
E=(0,0,0);center=(0,0,1)
def mul(a,b):return (a[0]^b[0],a[1]^b[1],a[2]^b[2]^(a[0]&b[1]))
def inv(a):return (a[0],a[1],a[2]^(a[0]&a[1]))
def conj(a,x):return mul(mul(inv(a),x),a)
def pmul(a,b):return (mul(a[0],b[0]),mul(a[1],b[1]))
D=list(product(range(2),repeat=3))
assert len(D)==8
for a,b,c in product(D,repeat=3):assert mul(mul(a,b),c)==mul(a,mul(b,c))
for a in D:assert mul(a,inv(a))==mul(inv(a),a)==E
rows=[]
# Z and U are the same images in both coordinates of actual source
# meridians at v=0 and v=1. A1,A2,B2 have arbitrary allowed central terms.
# B1 is literally identity, since v extends across the product-one divisor.
for zc,uc,a1c,a2c,b2c in product(range(2),repeat=5):
    Z=(1,0,zc);U=(0,1,uc)
    A1=(0,1,a1c);A2=(1,1,a2c);B1=E;B2=(0,1,b2c)
    G1=mul(B1,A1);G2=mul(B2,A2)
    h=mul(G2,inv(G1))
    left=conj(G1,Z);right=conj(G2,Z)
    assert left==(1,0,zc^1) and right==(1,0,zc)
    assert mul(left,inv(right))==center
    assert mul(mul(h,Z),mul(inv(h),inv(Z)))==center
    gens=[(Z,Z),(U,U),(A1,A2),(B1,B2)]
    reached={(E,E)};queue=[(E,E)]
    while queue:
        a=queue.pop()
        for b in gens:
            c=pmul(a,b)
            if c not in reached:reached.add(c);queue.append(c)
    assert len(reached)==64
    rows.append({'central_coordinates':[zc,uc,a1c,a2c,b2c],
                 'Zprime_images':[left,right],'central_difference':center,
                 'actual_generating_image_order':len(reached)})
assert len(rows)==32
out={'statement':'B88 specific zero-source membership is false',
     'based_maps':['v','v*(w-1)/(1-v)'],
     'target':'UT3(F2) x UT3(F2)', 'target_order':64,
     'source_image':'diagonal UT3(F2)',
     'exact_local_orders':[{'meridian':k,'orders_f1_f2':x} for k,x in orders.items()],
     'orientation_independence':'All primitive signs become1 modulo2; all whisker dependence is a checked central coordinate.',
     'all_central_cases':rows,
     'claims_excluded':['nonmembership of other normalized zero words','whole marginal failure','failure of I=R','a new source-kernel separator'],
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
path=Path('work_CE/zero_source_equalizer_certificate.json');path.write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact based maps agree on the actual source; f2-1=(vw-1)/(1-v).')
print('PASS actual primitive peripheral orders: a:(01,11), b:(00,01), z:(10,10) modulo2.')
print('PASS all32 possible central-coordinate assignments: actual image order64; Zprime differs from the diagonal by the nontrivial central element.')
print('PASS actual source image is diagonal, so the specific Zprime lies outside H and its actual compact closure.')
print('No marginal-kernel failure or nonmembership of other words is inferred.')
