"""Exact algebra and finite certificates for A.25--A.35 and D.3."""
import json,itertools
from fractions import Fraction
import sympy as s

u,v,A,B,b=s.symbols('u v A B b',nonzero=True)
XX=2*b*(v+b)/u**2; YY=4*b*b*(v+b)/u**3
quartic_num=s.together(YY**2-XX**3+4*A*b*b*XX).as_numer_denom()[0]
assert s.rem(quartic_num,s.Poly(v*v-A*u**4-b*b,v),v)==0
print('Quartic Jacobian birational identity: exact zero remainder.')
XX=A*u*u;YY=A*u*v
assert s.expand((YY**2-XX**3-A*B*XX).subs(v*v,A*u**4+B))==0
print('Quartic torsor to its 2-isogenous elliptic target: exact identity.')

x,y,alpha,beta=s.symbols('x y alpha beta',nonzero=True)
coeff=[alpha,beta,-s.Integer(1)];coords=[x,y,s.Integer(1)]
relation=alpha*x**6+beta*y**6-1
Bs=[]
for i,j,k in itertools.permutations(range(3)):
 ai,aj,ak=coeff[i],coeff[j],coeff[k]
 xi,xj,xk=coords[i],coords[j],coords[k]
 X=-ai*aj*(xi/xk)**2;Y=ai*aj**2*(xj/xk)**3
 C=-ai**2*aj**3*ak
 numerator=s.together(Y*Y-X**3-C).as_numer_denom()[0]
 assert s.rem(numerator,s.Poly(relation,y),y)==0
 Bs.append(str(C))
print('Six sextic triangle maps checked:',json.dumps(Bs))
for i,j,k in [(0,1,2),(0,2,1),(1,2,0)]:
 ai,aj,ak=coeff[i],coeff[j],coeff[k]
 xi,xj,xk=coords[i],coords[j],coords[k]
 w=xi*xj/(xk*xk);t=-ai*xi**6/(ak*xk**6)
 X=w**-2;Y=(2*t-1)*w**-3;C=-4*ai*aj/ak**2
 numerator=s.together(Y*Y-X**3-C).as_numer_denom()[0]
 assert s.rem(numerator,s.Poly(relation,y),y)==0
print('Three extra sextic maps checked exactly.')
holomorphic={(a,b) for a in range(1,6) for b in range(1,6-a)}
triangle={p[:2] for p in itertools.permutations((1,2,3))}
extra={p[:2] for p in set(itertools.permutations((1,1,4)))}
assert triangle|extra|{(2,2)}==holomorphic
assert not triangle&extra
print('Ten independent differential characters:',sorted(holomorphic))

def orbit(t):
 return {t,1-t,1/t,1/(1-t),t/(t-1),(t-1)/t}
six=sorted(orbit(Fraction(-1))|orbit(Fraction(-8))|orbit(Fraction(4)))
assert len(six)==15
four=sorted(orbit(Fraction(-1)))
def power_class(q,n):
 q=Fraction(q)
 result=Fraction(-1 if q<0 and n%2==0 else 1)
 for p,e in s.factorint(abs(q.numerator)).items():result*=int(p)**(int(e)%n)
 for p,e in s.factorint(q.denominator).items():result*=int(p)**((-int(e))%n)
 return result
for n,values in [(4,four),(6,six)]:
 print('Uniform point list for n=',n)
 for t in values:
  print(json.dumps({'t':str(t),'alpha':str(power_class(t,n)),
                   'beta':str(power_class(1-t,n))}))

for n in range(2,33):
 for m in range(1,4):
  annihilator=list(itertools.product([e for e in range(n) if 2*e%n==0],repeat=m))
  image={tuple(2*a%n for a in v) for v in itertools.product(range(n),repeat=m)}
  assert len(image)*len(annihilator)==n**m
  assert all(sum(a*b for a,b in zip(v,e))%n==0 for v in image for e in annihilator)
print('D.3 finite annihilator certificates: all n=2..32, m=1..3 passed.')
print('Supported class counts:',{n:(n**4*(2 if n%2==0 else 1)) for n in (3,4,6)})
