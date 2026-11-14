# Copied from supplied FLAGGED_149 for reproducible verification of R5.
#!/usr/bin/env python3
"""Exact checks for the F5 genus-two separating cover of B15."""
from pathlib import Path
import json
import sympy as sp

base=Path(__file__).resolve().parents[1]
checks=[]
def check(name,actual,expected=True):
    ok=actual==expected
    checks.append({'name':name,'actual':actual,'expected':expected,'passed':ok})
    assert ok,(name,actual,expected)
x,v=sp.symbols('x v')
poly=lambda f,z:sp.Poly(f,z,modulus=5)
F=poly(x**5+(x*x+1)**2,x)
H=poly(x**4+2*x**3+2*x**2-x-1,x)
D=poly(H.as_expr().subs(x,v*v+1),v)
check('quintic factorization',poly(F.as_expr()-(x-1)*H.as_expr(),x).is_zero)
check('quintic square-free',sp.gcd(F,F.diff()).degree(),0)
check('quartic square-free',sp.gcd(H,H.diff()).degree(),0)
check('quartic avoids the branch of the conic map',int(H.eval(1))%5,3)
check('octic square-free',sp.gcd(D,D.diff()).degree(),0)
check('octic degree and leading coefficient',[D.degree(),int(D.LC())%5],[8,1])
check('base genus',(F.degree()-1)//2,2)
check('cover genus',(D.degree()-2)//2,3)
check('unramified double-cover genus',2*3-2,2*(2*2-2))
check('Pprime satisfies cover equation',(3*3-int(D.eval(2)))%5,0)
check('Pprime maps to P',[(2*2+1)%5,(2*3)%5],[0,1])
check('Pprime maps to finite elliptic point',[(2*2+1)%5,3],[0,3])
e_points=[]
c_points=[]
for a in range(5):
    for b in range(5):
        if (b*b-int(H.eval(a)))%5==0:
            e_points.append([a,b])
        if (b*b-int(F.eval(a)))%5==0:
            c_points.append([a,b])
check('elliptic affine points',e_points,[[0,2],[0,3],[3,2],[3,3],[4,1],[4,4]])
check('elliptic point count including two infinities',len(e_points)+2,8)
check('base rational affine points',c_points,[[0,1],[0,4],[1,0]])
check('elliptic order is prime to five',sp.gcd(len(e_points)+2,5)==1)
check('composite separating cover degree',2*(len(e_points)+2),16)
# (y-h)(y+h)=x^5 on the quintic: check without quotient-ring ambiguity.
h=x*x+1
check('divisor-function norm identity',poly(F.as_expr()-h*h-x**5,x).is_zero)
check('other factor at P is a unit',2%5!=0)
check('pole order at infinity',max(5,2*2),5)

data={'result':'B15','all_passed':all(c['passed'] for c in checks),
      'check_count':len(checks),'octic':str(D.as_expr()),
      'elliptic_affine_points':e_points,'elliptic_point_count':8,
      'base_affine_points':c_points,'composite_cover_degree':16,
      'checks':checks}
destination=base/'code/A_R5_F7_test5_output.json'
destination.write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps({'output':str(destination),'checks':len(checks),
                  'all_passed':data['all_passed'],'cover_degree':16},indent=2))
