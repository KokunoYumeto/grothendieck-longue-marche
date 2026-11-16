#!/usr/bin/env python3
"""Exact actual elliptic maps and residual marked A4 geometry for A67."""
from pathlib import Path
from itertools import product
import json
import sympy as s

x,y,a,b,r,v=s.symbols('x y a b r v')
relation=y*y+(a*x+b)*y-x**3
def reduce_curve(expr):
    num,den=s.fraction(s.cancel(expr))
    rem=s.rem(num,relation,y)
    return s.factor(rem),s.factor(den)

xp=-b*y/x**2
xm=b*(y+b+a*x)/x**2
assert reduce_curve(x*xp*xm+b*b)[0]==0
X=x+a*b/x+b*b/x**2
Y=((x**3-a*b*x-2*b*b)*y-b*(a*x+b)**2)/x**3
target=Y*Y+a*X*Y+b*Y-X**3+5*a*b*X+a**3*b+7*b*b
assert reduce_curve(target)[0]==0

def invariants(a1,a2,a3,a4,a6):
    b2=a1*a1+4*a2
    b4=a1*a3+2*a4
    b6=a3*a3+4*a6
    b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    c4=s.expand(b2*b2-24*b4)
    delta=s.factor(-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6)
    return c4,delta

c4,dis=invariants(a,0,b,-5*a*b,-a**3*b-7*b*b)
assert s.factor(c4-a*(a**3+216*b))==0
assert s.factor(dis-b*(a**3-27*b)**3)==0
targetj=r*(r+216)**3/(r-27)**3
P=s.expand(r*(r+216)**3-1728*(r-27)**3)
assert s.factor(P-(r*r-540*r-5832)**2)==0

f4,fd=invariants(0,2*a*b,0,a*a*b*b,4*b**4)
assert s.factor(f4-16*a*a*b*b)==0
assert s.factor(fd-256*b**7*(a**3-27*b))==0
jF=16*r*r/(r-27)
for sign in (-1,1):
    rr=270+sign*162*s.sqrt(3)
    assert s.simplify(targetj.subs(r,rr)-1728)==0
    assert s.simplify(jF.subs(r,rr)-(4608+sign*2688*s.sqrt(3)))==0
assert s.factor((r*r-540*r-5832).subs(r,27))!=0

# Residual rational centre. Each equality is a polynomial identity over F3.
U=(v*v+1)**2/(v**3-v)
def zero_mod3(expr):
    num=s.fraction(s.cancel(expr))[0]
    return s.Poly(num,v,modulus=3).is_zero
assert zero_mod3(U.subs(v,v+1)-U-1)
assert zero_mod3(U.subs(v,-1/v)-U)
assert zero_mod3(s.diff(U,v)-(v**6+v**4+v*v+1)/(v**3-v)**2)
assert s.rem(v**9-v,(v**3-v)*(v**6+v**4+v*v+1),v)==0

# F9 = F3[i], i^2=-1; tuples give actual cusp and node orbits.
def add(z,w):return ((z[0]+w[0])%3,(z[1]+w[1])%3)
def mul(z,w):return ((z[0]*w[0]-z[1]*w[1])%3,
                     (z[0]*w[1]+z[1]*w[0])%3)
def powf(z,n):
    out=(1,0)
    for _ in range(n):out=mul(out,z)
    return out
def neg(z):return((-z[0])%3,(-z[1])%3)
def div(z,w):
    assert w!=(0,0)
    return mul(z,powf(w,7))
def mob(M,z):
    aa,bb,cc,dd=M
    if z is None:return None if cc==0 else (aa*pow(cc,-1,3)%3,0)
    num=add(mul((aa,0),z),(bb,0))
    den=add(mul((cc,0),z),(dd,0))
    return None if den==(0,0) else div(num,den)
def canonical(M):
    lead=next(t for t in M if t)
    inv=pow(lead,-1,3)
    return tuple((t*inv)%3 for t in M)
matrices={canonical(M) for M in product(range(3),repeat=4)
          if (M[0]*M[3]-M[1]*M[2])%3==1}
assert len(matrices)==12
nodes={(0,0),(1,0),(2,0),None}
cusps={(aa,bb) for aa in range(3) for bb in (1,2)}
assert len(cusps)==6
for M in matrices:
    assert {mob(M,z) for z in nodes}==nodes
    assert {mob(M,z) for z in cusps}==cusps
assert {sum(mob(M,z)==z for M in matrices) for z in cusps}=={2}
T=canonical((1,1,0,1))
assert sum(mob(T,z)==z for z in nodes)==1
assert not any(mob(T,z)==z for z in cusps)
W={z:add(powf(z,3),neg(z)) for z in cusps}
assert set(W.values())=={(0,1),(0,2)}
assert all(sum(val==w for val in W.values())==3 for w in set(W.values()))
node_values={None if z is None else add(powf(z,3),neg(z)) for z in nodes}
assert node_values=={None,(0,0)}
I=canonical((0,2,1,0))
assert not any(mob(I,z)==z for z in nodes)
assert sum(mob(I,z)==z for z in cusps)==2
cusporbits={frozenset((z,mob(I,z))) for z in cusps}
assert len(cusporbits)==4

counts=[
 {'subgroup':'1','degree':12,'genus':4,'cusps':6},
 {'subgroup':'C2','degree':6,'genus':2,'cusps':4},
 {'subgroup':'C3','degree':4,'genus':2,'cusps':2},
 {'subgroup':'V4','degree':3,'genus':1,'cusps':3},
 {'subgroup':'A4','degree':1,'genus':1,'cusps':1}]
assert all(2*z['genus']-2+z['cusps']==z['degree'] for z in counts)
result={'status':'PASS','scope':'Exact actual maps, j invariants and residual marked-centre calculations. Stable-model and arithmetic conclusions are proved separately in A67.',
 'actual_translation_x_formulas':[str(xp),str(xm)],
 'product_translation_functions':'-b^2',
 'actual_three_isogeny':[str(X),str(Y)],
 'target_j':str(targetj),
 'target_j1728_numerator_factor':str(s.factor(P)),
 'complement_j':str(jF),
 'complement_j_values':['4608-2688*sqrt(3)','4608+2688*sqrt(3)'],
 'residual_V4_quotient':str(U),'residual_C3_quotient':'v^3-v',
 'A4_matrix_count':len(matrices),'node_count':4,'cusp_count':6,
 'C3_cusp_values':[[0,1],[0,2]],'C3_node_values':['0','infinity'],
 'C2_quotient_cusps':len(cusporbits),'intermediate_counts':counts,
 'formal_torsion_radius_assumed':False}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS: actual translation/product/3-isogeny identities, complementary j, residual A4 centre and all marked quotient counts.')
