#!/usr/bin/env python3
"""Independent exact identities; not a test of the profinite pentagon."""
import itertools
import sympy as s


def check(label, assertion):
    assert assertion, label
    print('PASS', label)


# The finite D8 group, as t -> i^a t, i -> (-1)^b i.
D=list(itertools.product(range(4),range(2)))
def mul(x,y):
    a,b=x; c,d=y
    return ((a+(-1)**b*c)%4,(b+d)%2)
Ki=[(a,0) for a in range(4)]
K3=[(a,b) for a,b in D if (a+b)%2==0]
check('D8 associativity',all(mul(mul(a,b),c)==mul(a,mul(b,c))
                            for a,b,c in itertools.product(D,repeat=3)))
check('D8 is nonabelian',any(mul(a,b)!=mul(b,a) for a,b in itertools.product(D,repeat=2)))
check('subgroup fixing i is abelian of order four',len(Ki)==4 and
      all(mul(a,b)==mul(b,a) and mul(a,b) in Ki for a,b in itertools.product(Ki,repeat=2)))
check('subgroup fixing sqrt(-3) is abelian of order four',len(K3)==4 and
      all(mul(a,b)==mul(b,a) and mul(a,b) in K3 for a,b in itertools.product(K3,repeat=2)))

t=s.symbols('t')
w=4*t*(1-t)
check('Legendre/harmonic factorization',s.cancel(64*(4-w)**3/w**2-
      256*(1-t+t*t)**3/(t*t*(1-t)**2))==0)

d=s.sqrt(3); r=s.root(s.Rational(3,4),4)
check('E3 ordinate-square identity',s.simplify((d*(d-1)*r)**2-(-9+6*d))==0)
for sign in [-1,1]:
    x=-1+sign*d
    check(f'E3 half abscissa sign {sign}',s.simplify(x**3+1-(-9+sign*6*d))==0)

W=s.symbols('W',nonzero=True)
a=(W+2/W)/2
b=(W-2/W)/(2*s.I)
for label,expr in [('a',3*a**4-6*a*a-1),('b',3*b**4-6*b*b-1),
                   ('w=a+ib',a+s.I*b-W)]:
    numerator=s.together(expr).as_numer_denom()[0]
    check('E4 division polynomial '+label,s.rem(numerator,3*W**4-4,W)==0)

def singular_affine(p,c):
    # F=y^2-x^3+c*x-b; curves specified as y^2=x^3+A*x+B.
    A,B=c
    return [(x,y) for x in range(p) for y in range(p)
            if (y*y-x**3-A*x-B)%p==0
            and (-3*x*x-A)%p==0 and 2*y%p==0]

for p in [2,3]:
    for name,curve in [('E3',(0,1)),('E4',(-1,0))]:
        points=singular_affine(p,curve)
        print(f'{name} modulo {p}: affine singular points {points}')
        check(f'{name} mod {p} claimed smoothness', bool(points)==(p==2 or name=='E3'))

# Twist counterexample over any field of odd characteristic or characteristic 0.
Dmat=s.diag(1,-1)
P=s.Matrix([[0,1],[1,0]])
check('1 plus sign is isomorphic to its sign twist',P*Dmat==(-Dmat)*P and P.det()!=0)
for omega in [0,1]:
    lifts=[(a,b) for a,b in itertools.product(range(2),repeat=2) if (a+b)%2==omega]
    check(f'torsor fibre {omega} has no diagonal-translation fixed point',
          len(lifts)==2 and all((a^1,b^1)!=(a,b) for a,b in lifts))
print('All exact algebra checks passed.')
