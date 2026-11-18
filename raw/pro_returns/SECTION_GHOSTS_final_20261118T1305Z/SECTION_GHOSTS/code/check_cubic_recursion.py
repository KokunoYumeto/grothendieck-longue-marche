#!/usr/bin/env python3
"""Exact finite certificate for the prescribed1129 cubic-exponent recursion.

The analytic bijections, Chebotarev intersection and infinite ordinary
limit are proved in E.82–E.83; no enormous recursive prime is simulated.
"""
from math import factorial, gcd

p=1129; n=factorial(6); D=144*n**3
assert n==720 and D==53747712000
assert all(p%d for d in range(2,34))
assert gcd(D,p-1)==24 and D%p!=0
targets=[pow(59,D,p),pow(28,D,p),1]
assert targets==[276,978,1]
assert (3*targets[0]-2*targets[1])%p==1
assert ((3*targets[0])%p,(-2*targets[1])%p)==(828,302)
bad={u for u in range(1,p) if pow(u,2,p)==1 or pow(u,3,p)==1}
assert len(bad)==4
exponents=[e for e in range(p-1) if gcd(e,p-1)==24]
assert len(exponents)==46
minimum=p
for e in exponents:
    for t in targets:
        roots={u for u in range(1,p) if pow(u,e,p)==t}
        assert len(roots)==24
        legal=roots-bad
        assert len(legal)>=20
        minimum=min(minimum,len(legal))
print('p,n,D =',p,n,D)
print('p-1=24*47; gcd(D,p-1)=24; D is a1129-adic unit.')
print('Targets59^D,28^D,1 modulo1129:',targets)
print('Updated coefficients modulo1129: (828,302,1), sum relation holds.')
print('Forbidden nonzero residues:',sorted(bad))
print(f'All{len(exponents)} exponent classes and all3 targets checked;')
print(f'every target has24 roots, with at least{minimum} legal roots.')
for small in [7,11,13]:
    forbidden={u for u in range(1,small)
               if pow(u,2,small)==1 or pow(u,3,small)==1}
    assert len(forbidden)<=4 and len(forbidden)<small-1
    print(f'p={small}: forbidden={sorted(forbidden)}, legal residues remain.')
print('PASS: full finite first-stage specialization certificate.')

# All original1129 cover-sheet Kummer vectors, with literal branch order.
theta=[16,430,699,1113]
assert all(pow(a,4,p)==54 and (4*pow(a,3,p))%p for a in theta)
def bit(a):
    a%=p
    assert a
    return 0 if pow(a,(p-1)//2,p)==1 else 1
def bits(x): return ''.join(str(bit(x-a)) for a in theta)
assert bits(0)=='0000' and bits(3)=='1111'
t=828; rad=(-t*pow(1-t,3,p)*pow(24,-1,p))%p
roots=[z for z in range(p) if pow(z,8,p)==rad]
assert roots==[35,44,235,511,618,894,1085,1094]
expected=[(35,28,454,'0101'),(44,941,603,'1100'),
          (235,1101,629,'1010'),(511,188,306,'0011'),
          (618,188,823,'0011'),(894,1101,500,'1010'),
          (1085,941,526,'1100'),(1094,28,675,'0101')]
got=[]
for z in roots:
    x=(-6*z*z*pow(1-t,-1,p))%p
    y=(-18*z*pow(1-t,-1,p))%p
    assert (y*y-x**5+54*x)%p==0 and (8*pow(z,7,p))%p
    b=bits(x)
    # Opposite roots: (16,1113) and (430,699).
    assert ((int(b[0])+int(b[3]))%2,(int(b[1])+int(b[2]))%2)==(1,1)
    got.append((z,x,y,b))
assert got==expected
print('Original branch order:',theta,'; radicand=',rad)
print('z,x,y, four full local Kummer bits:')
for row in got: print(*row,sep=',')
print('All8 vectors project to(1,1); E70 proves the global projected image is(0,0).')
print('PASS: every original cover sheet and its full finite Kummer vector.')
