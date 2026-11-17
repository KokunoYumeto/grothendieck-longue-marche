#!/usr/bin/env python3
"""Finite, exact checks for B.CF4 and B.CF6.

The infinite arc is defined in the proof by continuing a fair enumeration of
all rational irreducible dominant surface correspondences and nonzero plane
polynomials. These initial stages are certificates for the finite elimination
mechanism, not a finite substitute for that infinite construction.
"""
import json
from itertools import combinations
from pathlib import Path
import sympy as s
x, xp, y, yp, q, w = s.symbols('x xp y yp q w')
base = Path(__file__).parent

def order(expr, variable=x):
    expr = s.cancel(expr)
    if expr == 0:
        return None
    num, den = s.fraction(expr)
    def poly_order(poly):
        P = s.Poly(poly, variable)
        return min(m[0] for m, c in P.terms() if c != 0)
    return poly_order(num) - poly_order(den)

def initial(expr, variable=x):
    n = order(expr, variable)
    if n is None:
        return 0
    return s.cancel(expr / variable**n).subs(variable, 0)

# Fixed initial entries in an enumeration of eligible correspondences.
graphs = [
    ('quadratic_parameter', x + x*x, y),
    ('simultaneous_dilation', 2*x, 2*y),
    ('vertical_shear', x, y + x*x),
    ('factorial_series_involution', -x, y - 2*x),
    ('horizontal_shear', x + y, y),
]
pairs = [(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]
jet = s.Integer(0)
precision = 1
records = []
for name, fx, fy in graphs:
    chosen = None
    for a,b in pairs:
        P = s.expand(jet + a*x**precision + b*x**(precision+1))
        Q1 = xp - fx.subs(y,P)
        Q2 = P.subs(x,xp) - fy.subs(y,P)
        quotient, remainder = s.div(Q2,Q1,xp)
        R = s.expand(remainder)
        if R == 0:
            continue
        assert not R.has(xp)
        assert s.expand(R - (Q2-quotient*Q1)) == 0
        chosen=(a,b,P,Q1,Q2,quotient,R)
        break
    assert chosen is not None
    a,b,P,Q1,Q2,quotient,R=chosen
    next_precision=max(precision+1,s.degree(P,x)+1,order(R)+1)
    records.append({'name':name,'input_precision':precision,'chosen_pair':[a,b],
                    'polynomial_P':str(P),'Q1':str(Q1),'Q2':str(Q2),
                    'elimination_R':str(R),'R_order':order(R),
                    'certificate_A1':str(-quotient),'certificate_A2':'1',
                    'output_precision':int(next_precision)})
    jet,precision=P,int(next_precision)
    print(f'{name}: P={P}; ord(R)={order(R)}; precision={precision}; identity verified')

# A genuine degree-four correspondence, rather than the graph of a map.
P=jet
Q1=xp**2-x**2-x**3
Q2=P.subs(x,xp)**2-P**2-P**3
A,B,g=s.gcdex(Q1,Q2,xp)
assert s.cancel(A*Q1+B*Q2-g)==0
assert g == 1
D=s.lcm(s.denom(s.cancel(A)),s.denom(s.cancel(B)))
A=s.cancel(D*A); B=s.cancel(D*B); R=s.expand(D)
assert not R.has(xp)
assert s.cancel(A*Q1+B*Q2-R)==0
next_precision=max(precision+1,s.degree(P,x)+1,order(R)+1)
records.append({'name':'quadratic_correspondence','input_precision':precision,
                'polynomial_P':str(P),'Q1':str(Q1),'Q2':str(Q2),
                'elimination_R':str(R),'R_order':order(R),
                'certificate_A1':str(A),'certificate_A2':str(B),
                'output_precision':int(next_precision)})
precision=int(next_precision)
print(f'quadratic_correspondence: ord(R)={order(R)}; precision={precision}; identity verified')

# Exact supported-scaling checks, including a ramified constant extension
# with t=q^2 and points of odd q-valuation.
t=q*q
lam=1+t
points=[s.Integer(0),s.Integer(1),s.Integer(-2),q,q*q,q+q**3,1+q,q**-1]
def F(a):
    va=order(a,q)
    return s.expand(lam*a) if a == 0 or va>0 else a
pair_records=[]
for a,b in combinations(points,2):
    ratio=s.cancel((F(a)-F(b))/(a-b))
    assert initial(ratio,q)==1 and order(ratio,q)==0
    delta=order(ratio-1,q)
    assert delta is None or delta>0
    pair_records.append({'a':str(a),'b':str(b),'ratio':str(ratio),'difference_order':delta})
print(f'supported_scaling: {len(pair_records)} exact pair differences preserve valuation and initial form')
cr_records=[]
for a,b,c,d in combinations(points,4):
    cr=s.cancel((a-c)*(b-d)/((a-d)*(b-c)))
    crf=s.cancel((F(a)-F(c))*(F(b)-F(d))/((F(a)-F(d))*(F(b)-F(c))))
    assert order(cr,q)==order(crf,q) and initial(cr,q)==initial(crf,q)
    assert order(1-cr,q)==order(1-crf,q) and initial(1-cr,q)==initial(1-crf,q)
    cr_records.append({'points':list(map(str,(a,b,c,d))),'v_crossratio':order(cr,q),
                       'initial_crossratio':str(initial(cr,q)),
                       'v_one_minus':order(1-cr,q),'initial_one_minus':str(initial(1-cr,q))})
print(f'cross_ratios: {len(cr_records)} exact quadruples preserve both cross-ratio and one-minus leading data')
print(f'finite_initial_jet: u(t)={jet}+O(t^{precision})')
print('These finite certificates verify the construction steps; the paper proves the infinite avoidance and whole-site assertions.')
output={'arc_stages':records,'initial_jet':str(jet),'precision':precision,
        'supported_scaling_pairs':pair_records,'cross_ratios':cr_records}
(base/'reconstruction_arc_certificates.json').write_text(json.dumps(output,indent=2)+'\n')
