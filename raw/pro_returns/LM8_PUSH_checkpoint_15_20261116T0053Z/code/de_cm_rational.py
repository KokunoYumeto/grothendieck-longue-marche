#!/usr/bin/env python3
"""Exact finite certificates for E(Q(i)) and the two rational 2-isogenies.

The descent finiteness proof is in D.25. This script verifies the identities,
the displayed rational points and their doubles, and the reduction counts.
No database or unexecuted rank command is used.
"""
import json
from pathlib import Path
import sympy as s

x, y = s.symbols('x y')
X = x - 1/x
Y = y*(1 + 1/x**2)
phi_identity = s.cancel((Y**2-X**3-4*X).subs(y**2,x**3-x))
assert phi_identity == 0
u, v = s.symbols('u v')
px = (u+4/u)/4
py = v*(1-4/u**2)/8
psi_identity = s.cancel((py**2-px**3+px).subs(v**2,u**3+4*u))
assert psi_identity == 0
double_x = ((3*x*x-1)/(2*y))**2-2*x
composed_x = s.cancel((X+4/X)/4)
assert s.cancel((composed_x-double_x).subs(y**2,x**3-x)) == 0
composed_y=s.cancel(Y*(1-4/X**2)/8)
double_y=(3*x*x-1)/(2*y)*(x-double_x)-y
assert s.cancel(s.together(composed_y-double_y).subs(y**2,x**3-x)) == 0

points = [(0,0),(1,0),(-1,0)]
for a in (s.I,-s.I):
    b = 1-a
    points += [(a,b),(a,-b)]
checks=[]
for a,b in points:
    assert s.expand(b*b-a**3+a)==0
    if b:
        slope=s.simplify((3*a*a-1)/(2*b))
        dx=s.simplify(slope*slope-2*a)
        dy=s.simplify(slope*(a-dx)-b)
        assert (dx,dy)==(0,0)
        dbl=['0','0']
    else:
        dbl='O'
    checks.append({'point':[str(a),str(b)],'double':dbl})

def count_prime(p):
    return 1+sum((b*b-a*a*a+a)%p==0 for a in range(p) for b in range(p))

# F9 = F3[t]/(t^2+1); t^2+1 has no root in F3.
F9=[(a,b) for a in range(3) for b in range(3)]
def add9(a,b): return ((a[0]+b[0])%3,(a[1]+b[1])%3)
def neg9(a): return ((-a[0])%3,(-a[1])%3)
def mul9(a,b):
    return ((a[0]*b[0]-a[1]*b[1])%3,(a[0]*b[1]+a[1]*b[0])%3)
n9=1+sum(mul9(b,b)==add9(mul9(mul9(a,a),a),neg9(a)) for a in F9 for b in F9)
assert (count_prime(3),count_prime(5),n9)==(4,8,16)
out={
    'curve':'y^2=x^3-x',
    'phi_to_Eprime':'(x-1/x, y(1+1/x^2))',
    'psi_to_E':'((u+4/u)/4, v(1-4/u^2)/8)',
    'isogeny_equation_identities':True,
    'composition_is_doubling':True,
    'descent_images':{'E':['1','-1'],'Eprime':['1','2']},
    'Eprime_descent_2_witness':[2,4],
    'points_in_Qi':['O']+checks,
    'finite_field_counts':{'F3':4,'F5':8,'F9':16},
    'conclusion_with_descent_proof':'E(Q)=E[2]; E(Q(i)) has exactly8points and is Z/4 plus Z/2'
}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
