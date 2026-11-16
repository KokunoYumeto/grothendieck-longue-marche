#!/usr/bin/env python3
"""Independent symbolic and finite checks for the first elliptic covers.

No program or computed output from the supplied returns is imported.
Run with Python 3 and SymPy. The geometric arguments accompanying these
identities are in statements A.4 and A.10 of the paper.
"""
import itertools,json,pathlib
import sympy as S
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
w,v,x,y,a,b,c,t,u=S.symbols('w v x y a b c t u')
checks={}
def check(name,expr):
    expr=S.factor(expr)
    assert expr==0,(name,expr)
    checks[name]='zero'
check('S3_map_to_E', (w*v)**2-(w**9+a*w**6+b*w**3)-w**2*(v**2-(w**7+a*w**4+b*w)))
check('D8_map_to_E',(w**2*v)**2-(w**12+a*w**8+b*w**4)-w**4*(v**2-(w**8+a*w**4+b)))
xp=x+a+b/x;yp=y*(1-b/x**2)
check('Velu_2_isogeny', (yp**2-(xp**3-2*a*xp**2+(a*a-4*b)*xp)).subs(y**2,x**3+a*x*x+b*x))
for aa in [6,-6]:
    check('E_source_to_target_'+str(aa),((xp**3-2*a*xp**2+(a*a-4*b)*xp)/64-((xp-S.Rational(2,3)*a)/4)**3+(xp-S.Rational(2,3)*a)/4).subs({a:aa,b:1}))
check('stable_two_isogeny', (-(1+S.I)/4)**2*(xp**3+4*xp)-((-S.I*xp/2)**3-(-S.I*xp/2)))
for eps in [1,-1]:
    tt=w+eps/w
    # eps=1 for b=1; eps=-1 for b=-1.
    check('S3_elliptic_quotient_'+str(eps),tt**3-3*eps*tt-(w**3+eps/w**3))
    check('S3_genus2_factor_'+str(eps),(w-eps/w)**2-(tt**2-4*eps))
tt=w+c/w
check('D8_elliptic_quotient',tt**4-4*c*tt**2+2*c*c-(w**4+c**4/w**4))
check('D8_genus2_factor',(w-c/w)**2-(tt**2-4*c))
dd=(t*t-4*c)*(t**4-4*c*t*t+a+2*c*c)
check('D8_genus2_cusp_divisor',dd-(t**3-4*c*t)**2-(a+2*c*c)*(t*t-4*c))
check('D8_cyclic_parameter',((b+t*((a-2*b*t)/(t*t-1)))**2-(((a-2*b*t)/(t*t-1))**2+a*((a-2*b*t)/(t*t-1))+b*b)))
# The preceding identity uses b as a chosen square root of the old b.
check('Q8_quotient_E', ((S.I/2)*x*y*(x**4-y**4))**2-((x*y)**6-(x*y)**2)+(x*y)**2*((x**4+y**4)**2-4)/4)

def elliptic_count(p,A,B):
    return 1+sum(1 if (q:=(z**3+A*z+B)%p)==0 else 2 if pow(q,(p-1)//2,p)==1 else 0 for z in range(p))
def quartic_count(p,A,B):
    return 2+sum(1 if (q:=(z**4+A*z*z+B)%p)==0 else 2 if pow(q,(p-1)//2,p)==1 else 0 for z in range(p))
counts={
 'E_at5':elliptic_count(5,-1,0),
 'E_at13':elliptic_count(13,-1,0),
 'S3_complement_at5':elliptic_count(5,-3,6),
 'E_at3':elliptic_count(3,-1,0),
 'D8_stable_complement_at3':quartic_count(3,-4,2),
 'E_at7':elliptic_count(7,-1,0),
 'D8_plus_complement_at7':quartic_count(7,-4,8),
 'D8_minus_complement_at7':quartic_count(7,-4,-4),
}
assert counts=={'E_at5':8,'E_at13':8,'S3_complement_at5':7,'E_at3':4,'D8_stable_complement_at3':2,'E_at7':8,'D8_plus_complement_at7':12,'D8_minus_complement_at7':4},counts
jquartic=lambda A,B:S.factor(16*(A*A+12*B)**3/(S.Rational(B)*(A*A-4*B)**2))
jvalues={str(B):str(jquartic(-4,B)) for B in [2,8,-4]}
assert jvalues=={'2':'8000','8':'10976','-4':'128'}

def compose(p,q):return tuple(p[q[i]] for i in range(len(p)))
def subgroup(gens,n):
    identity=tuple(range(n));seen={identity};todo=[identity]
    while todo:
        z=todo.pop()
        for g in gens:
            zz=compose(z,g)
            if zz not in seen:seen.add(zz);todo.append(zz)
    return seen
S3=list(itertools.permutations(range(3)))
s3pairs=sum(len(subgroup([p,q],3))==6 for p in S3 for q in S3)
rot=tuple((i+1)%4 for i in range(4));ref=tuple(-i%4 for i in range(4))
D8=sorted(subgroup([rot,ref],4))
d8pairs=sum(len(subgroup([p,q],4))==8 for p in D8 for q in D8)
# Q8 represented by signed basis 1,i,j,k, with indices 0..3 and sign +/-1.
qels=[(s,i) for s in [1,-1] for i in range(4)]
def qmul(a,b):
    s,i=a;r,j=b
    if i==0:return(s*r,j)
    if j==0:return(s*r,i)
    if i==j:return(-s*r,0)
    return(s*r*(1 if (i,j) in [(1,2),(2,3),(3,1)] else -1),6-i-j)
def qgen(g,h):
    seen={(1,0)};todo=[(1,0)]
    while todo:
        z=todo.pop()
        for t in [g,h]:
            zz=qmul(z,t)
            if zz not in seen:seen.add(zz);todo.append(zz)
    return seen
q8pairs=sum(len(qgen(g,h))==8 for g in qels for h in qels)
assert (s3pairs,d8pairs,q8pairs)==(18,24,24)
# Relations in degree-zero divisors on the four fully ramified cusps.
# In the basis P1-P4,P2-P4,P3-P4, add the Kummer relation.
snfs={}
for name,relation in [('D8',[1,1,-1]),('Q8',[1,1,1])]:
    mat=S.Matrix([[4,0,0],[0,4,0],[0,0,4],relation]).T
    snf=smith_normal_form(mat,domain=ZZ)
    diag=[abs(int(snf[i,i])) for i in range(3)]
    assert diag==[1,4,4],diag
    snfs[name]=diag

out={'symbolic_checks':checks,'point_counts':counts,'quartic_j':jvalues,
     'generating_pairs':{'S3':s3pairs,'D8':d8pairs,'Q8':q8pairs},
     'cover_counts_mod_group_automorphisms':{'S3':s3pairs//6,'D8':d8pairs//8,'Q8':q8pairs//24},
     'cuspidal_smith_forms':snfs}
path=pathlib.Path(__file__).with_suffix('.json');path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
