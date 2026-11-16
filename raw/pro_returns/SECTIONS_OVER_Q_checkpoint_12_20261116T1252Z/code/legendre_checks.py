#!/usr/bin/env python3
"""Exact certificates for A3, A7/L16, and A8/L17; no numerical approximations."""
from fractions import Fraction
import sympy as sp
x,t=sp.symbols('x t')
psi3=3*x**4-4*(1+t)*x**3+6*t*x**2-t**2
lam=sp.Rational(32,27); x3=sp.Rational(4,3)
print('A3 residual-3 example')
print('lambda =',lam,'x-coordinate =',x3)
print('division polynomial value =',sp.factor(psi3.subs({t:lam,x:x3})))
print('curve y-coordinate squared =',sp.factor((x*(x-1)*(x-t)).subs({t:lam,x:x3})))
print('division polynomial factorization =',sp.factor(psi3.subs(t,lam)))
print('\nL16 ordinary local Tate-module counterexample')
f=x*(x-1)*(x-4)
X=x-5+4/x
Y_squared=f*(1-4/x**2)**2
print('2-isogeny identity difference =',sp.factor(Y_squared-X*(X+1)*(X+9)))
for p in (17,):
    for la in (4,9):
        n=1+sum(1 if (a:=r*(r-1)*(r-la)%p)==0 else 2 if pow(a,(p-1)//2,p)==1 else 0 for r in range(p))
        print(f'F_{p}: lambda={la}, #E={n}, trace={p+1-n}, ordinary={(p+1-n)%p != 0}')
    print('roots of -1 mod17 =',[a for a in range(p) if a*a%p==p-1])
    print('roots of 2 mod17 =',[a for a in range(p) if a*a%p==2])
for la in (4,9):
    print(f'j({la}) =',256*Fraction((la*la-la+1)**3,la**2*(1-la)**2))
print('\nL17 modular unit')
j=256*(t*t-t+1)**3/(t*t*(1-t)**2)
u=sp.factor(1-1728/j)
print('u(t) =',u)
print('u(0)=',u.subs(t,0),'u(1)=',u.subs(t,1),'u(infinity)=',sp.limit(u,t,sp.oo))
print('identity numerator difference =',sp.factor(4*(t*t-t+1)**3-27*t*t*(1-t)**2-(t+1)**2*(t-2)**2*(2*t-1)**2))
print('zeros orders: -1:2, 1/2:2, 2:2; poles: t^2-t+1=0:3 each')
print('\nIndependent verification of root L12(i) example')
print('fifth powers of units mod25 =', sorted({pow(a,5,25) for a in range(25) if a%5}))
print('-4 mod25 =',-4%25)
print('E5 discriminant =',16*5**2*(1-5)**2,'c4 =',16*(5**2-5+1))
print('\nRaw R4 counterexample at the infinity cusp of the Fermat quintic')
C=sp.Matrix([[1,-2],[2,-3]])
print('C =',C)
print('(C+I)^2 =',(C+sp.eye(2))**2)
print('C^5 =',C**5)
print('C^5 mod5 =',(C**5).applyfunc(lambda n:n%5))
print('\nUniform residual support: conductor congruence check')
for prime in list(sp.primerange(5,200)):
    if prime%72==5:
        group_order=prime*(prime-1)**2*(prime+1)
        fac=sp.factorint(group_order)
        print('l =',prime,'v2(GL2) =',fac.get(2,0),'v3(GL2) =',fac.get(3,0))
print('\nPositive-rank cubic C9 and its infinite point')
XX,YY,ZZ=sp.symbols('XX YY ZZ')
ell_x=12*ZZ/(XX+YY)
ell_y=12*(XX-YY)/(XX+YY)
print('(y^2-x^3+48)*(X+Y)^3 =',sp.factor((ell_y**2-ell_x**3+48)*(XX+YY)**3))
print('C9 point (1,2,1) maps to =',(ell_x.subs({XX:1,YY:2,ZZ:1}),ell_y.subs({XX:1,YY:2,ZZ:1})))
point=(sp.Rational(4),sp.Rational(-4))
slope=3*point[0]**2/(2*point[1])
double_x=slope**2-2*point[0]
double_y=slope*(point[0]-double_x)-point[1]
print('2P =',(double_x,double_y))
for p in (5,13):
    n=1+sum(1 if (v:=(r**3-48)%p)==0 else 2 if pow(v,(p-1)//2,p)==1 else 0 for r in range(p))
    print(f'#E(F_{p}) =',n)
print('gcd of counts =',sp.gcd(6,21))
print('P is not killed by3 because 2P differs from -P =',(point[0],-point[1]))
print('t(P) =',sp.Rational(1,9),'1-t(P) =',sp.Rational(8,9))
print('\nRank-zero cubic C2 maps')
c2x=6*ZZ/(XX+YY)
c2y=9*(XX-YY)/(XX+YY)
print('(y^2-x^3+27)*(X+Y)^3 =',sp.factor((c2y**2-c2x**3+27)*(XX+YY)**3))
print('C2 point (1,1,1) maps to =',(c2x.subs({XX:1,YY:1,ZZ:1}),c2y.subs({XX:1,YY:1,ZZ:1})))
print('\nQuartic and sextic elliptic-quotient maps')
aa,bb,v,w=sp.symbols('aa bb v w')
qx=w**2/v**2
qy=w*(aa*v**4-bb)/v**3
quartic_identity=sp.factor((qy**2-qx**3+4*aa*bb*qx)*v**6)
print('quartic equation difference times v^6 =',quartic_identity)
print('quartic reduced by w^2=aa*v^4+bb =',sp.factor(quartic_identity.subs(w**2,aa*v**4+bb)))
a,b,c,u=sp.symbols('a b c u')
sx=-b*v**2/a; sy=-b*u**3/a
print('sextic equation difference =',sp.factor(sy**2-sx**3-b**2*c/a**3))
print('\nGeometric monodromy diagonal identity')
A=sp.symbols('A',nonzero=True)
UU=lambda z:sp.Matrix([[1,z],[0,1]])
LL=lambda z:sp.Matrix([[1,0],[z,1]])
diag_product=UU(2)*LL((A-1)/2)*UU(-2/A)*LL(-A*(A-1)/2)
print('product =',sp.simplify(diag_product))
print('difference from diag(A,1/A) =',sp.simplify(diag_product-sp.diag(A,1/A)))
print('\nPotentially multiplicative supports of small integral Legendre parameters')
for la in range(2,10):
    jj=sp.Rational(256*(la*la-la+1)**3,la*la*(1-la)**2)
    print('lambda =',la,'j =',jj,'negative j-valuation primes =',sorted(sp.factorint(sp.denom(jj))))

print('\nA.39 exact cubic quotient of the Legendre mod-three representation')
r1,r2,r3,r4,z,w,v=sp.symbols('r1 r2 r3 r4 z w v')
pair_sums=(r1*r2+r3*r4,r1*r3+r2*r4,r1*r4+r2*r3)
res_sym,res_remainder,res_map=sp.symmetrize(sp.prod(z-r for r in pair_sums),
                                         (r1,r2,r3,r4),formal=True)
assert res_remainder==0
elementary_values=(4*(1+t)/3,2*t,0,-t**2/3)
resolvent=sp.expand(res_sym.subs({symbol:value for (symbol,_),value
                               in zip(res_map,elementary_values)}))
print('pair-partition resolvent =',sp.factor(resolvent))
print('27 R((w+2t)/3) =',sp.factor(27*resolvent.subs(z,(w+2*t)/3)))
D=4*t*(1-t)
assert sp.expand(27*resolvent.subs(z,(w+2*t)/3)-w**3-D**2)==0
print('v=-D/w: (v^3-D) w^3 =',sp.factor(((-D/w)**3-D)*w**3))
print('w=-v^2: w^3+D^2 =',sp.factor((-v**2)**3+D**2))

from itertools import product
lines=((1,0),(0,1),(1,1),(1,2))
partitions=(frozenset((frozenset((0,1)),frozenset((2,3)))),
            frozenset((frozenset((0,2)),frozenset((1,3)))),
            frozenset((frozenset((0,3)),frozenset((1,2)))))
def normalize_line(xx,yy):
    xx%=3; yy%=3
    if xx:
        return (1,yy*pow(xx,-1,3)%3)
    return (0,1)
def partition_action(matrix):
    aa,bb,cc,dd=matrix
    line_perm=tuple(lines.index(normalize_line(aa*xx+bb*yy,cc*xx+dd*yy))
                    for xx,yy in lines)
    return tuple(partitions.index(frozenset(frozenset(line_perm[j] for j in pair)
                                           for pair in partition))
                 for partition in partitions)
gl2=[m for m in product(range(3),repeat=4) if (m[0]*m[3]-m[1]*m[2])%3]
images={partition_action(m) for m in gl2}
kernel=[m for m in gl2 if partition_action(m)==(0,1,2)]
print('GL2(F3) order =',len(gl2),'partition image order =',len(images),
      'kernel order =',len(kernel))
print('partition images of U(1), L(1), diag(-1,1) =',
      [partition_action(m) for m in ((1,1,0,1),(1,0,1,1),(2,0,0,1))])
assert (len(gl2),len(images),len(kernel))==(48,6,8)
print('cubes of units modulo9 =',sorted({pow(k,3,9) for k in range(9) if k%3}))
print('5 and7 modulo9 =',5,7)
for la,prime in ((6,5),(7,7)):
    dd=4*la*(1-la)
    print('lambda =',la,'D =',dd,'v_q(D) =',sp.factorint(abs(dd))[prime],
          'q =',prime)
    assert sp.factorint(abs(dd))[prime]==1
