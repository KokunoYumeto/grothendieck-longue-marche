"""Exact depth-two Ihara calculations, with a second noncommutative check.

Run with Python 3 and sympy. No floating-point operations are used.
The normalization is sigma_{2m+1}=ad_x^{2m}(y) modulo depth >=2.
"""
from pathlib import Path
from collections import defaultdict
import json
import sympy as s

BASE=Path(__file__).resolve().parent
X,Y=s.symbols('X Y')

def poly_bracket(a,b):
    return s.expand(X**a*(Y**b-(Y-X)**b)+(Y-X)**a*(X**b-Y**b)+Y**a*((Y-X)**b-X**b))

def add(*terms):
    ans=defaultdict(int)
    for scale,p in terms:
        for w,c in p.items(): ans[w]+=scale*c
    return {w:c for w,c in ans.items() if c}

def mul(a,b):
    ans=defaultdict(int)
    for u,c in a.items():
        for v,d in b.items():ans[u+v]+=c*d
    return {w:c for w,c in ans.items() if c}

def comm(a,b):return add((1,mul(a,b)),(-1,mul(b,a)))

def deriv(f,p):
    dy=comm({'y':1},f)
    ans=defaultdict(int)
    for w,c in p.items():
        for i,ch in enumerate(w):
            if ch=='y':
                for v,d in dy.items():ans[w[:i]+v+w[i+1:]]+=c*d
    return {w:c for w,c in ans.items() if c}

def ihara(f,g):return add((1,comm(f,g)),(1,deriv(f,g)),(-1,deriv(g,f)))

def sig(n):
    p={'y':1}
    for _ in range(n-1):p=comm({'x':1},p)
    return p

def reduced(p):
    # Read words from the right: x^a y x^b y x^c maps to 0^a Y^b X^c.
    # This convention gives the displayed polynomial Ihara bracket.
    out=0
    for w,v in p.items():
        parts=w.split('y')
        assert len(parts)==3
        if not parts[0]:out+=v*Y**len(parts[1])*X**len(parts[2])
    return s.expand(out)

records=[]
for w in range(1,15):
    pairs=[(a,w-a) for a in range(3,w,2) if 3<=w-a and a<w-a and (w-a)%2]
    cols=[]
    ncs=[]
    polys=[]
    for a,b in pairs:
        p=poly_bracket(a-1,b-1)
        nc=ihara(sig(a),sig(b))
        assert s.expand(reduced(nc)-p)==0
        polys.append(str(p)); ncs.append(nc)
        cols.append([p.coeff(X,i).coeff(Y,w-2-i) for i in range(w-1)])
    mat=s.Matrix.hstack(*[s.Matrix(c) for c in cols]) if cols else s.zeros(max(0,w-1),0)
    rec={'weight':w,'pairs':pairs,'depth_one_dimension':int(w>=3 and w%2==1),
         'depth_two_dimension':mat.rank(),'kernel':[[str(x) for x in v] for v in mat.nullspace()],
         'polynomials':polys,'noncommutative_terms':[len(x) for x in ncs]}
    records.append(rec)
    print(f"weight {w:2}: depth1={rec['depth_one_dimension']} depth2={rec['depth_two_dimension']} pairs={pairs} relations={rec['kernel']}")

p12=s.expand(X**2*Y**2*(X-Y)**3*(X+Y)**3)
assert s.expand(p12+p12.xreplace({X:Y,Y:X}))==0
assert s.expand(p12+p12.subs({X:X-Y,Y:X}, simultaneous=True)+p12.subs({X:-Y,Y:X-Y},simultaneous=True))==0
assert poly_bracket(2,8)-3*poly_bracket(4,6)==0
assert not ihara(sig(3),sig(5))=={}
assert add((1,ihara(sig(3),sig(9))),(-3,ihara(sig(5),sig(7))))=={}
print('Weight-12 relation: {sigma3,sigma9}-3{sigma5,sigma7}=0 in depth two, verified in both polynomial models.')
print('Period polynomial:',p12)
print('Underlying free-Lie depth-two dimensions through 14:',[(n,(n-1)//2) for n in range(2,15)])
(BASE/'e_depth.json').write_text(json.dumps({'rows':records,'period_polynomial':str(p12),'all_checks':True},indent=2)+'\n')
