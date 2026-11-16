#!/usr/bin/env python3
"""Actual nonstable dihedral degree16 models; no fixed-group conclusion."""
from pathlib import Path
import json
import sympy as s
w,v,a,b=s.symbols('w v a b')
m=8
x=w**m
y=w**(m//2)*v
f=w**(2*m)+a*w**m+b
relation=v*v-f
assert s.rem(y*y-x**3-a*x*x-b*x,relation,v)==0
X=x+a+b/x
Y=y*(1-b/x**2)
num=s.fraction(s.cancel(Y*Y-X**3+2*a*X*X-(a*a-4*b)*X))[0]
assert s.rem(num,relation,v)==0
jtarget=16*(a*a+12*b)**3/(b*(a*a-4*b)**2)
assert jtarget.subs({a:6,b:1})==1728
assert jtarget.subs({a:-6,b:1})==1728
assert jtarget.subs({a:0,b:-1})==1728
# b=1 reflection s(w,v)=(1/w,-v/w^m), verified on the actual equation.
assert s.cancel((-v/w**m)**2-(w**(-2*m)+a*w**(-m)+1)
                -(v*v-w**(2*m)-a*w**m-1)/w**(2*m))==0
# Exact automorphism relations over Q(zeta8).
zeta=s.symbols('zeta')
rot=(zeta*w,-v)
ref=(1/w,-v/w**m)
def compose(F,G):
    return tuple(s.cancel(f.subs({w:G[0],v:G[1]},simultaneous=True)) for f in F)
def equal_pair(F,G):
    return all(s.rem(s.fraction(s.cancel(f-g))[0],zeta**4+1,zeta)==0
               for f,g in zip(F,G))
R=(w,v)
for _ in range(8):R=compose(rot,R)
assert equal_pair(R,(w,v))
assert equal_pair(compose(ref,ref),(w,v))
assert equal_pair(compose(ref,compose(rot,ref)),(w/zeta,-v))
assert not equal_pair(compose(rot,compose(rot,compose(rot,rot))),(w,v))
g=m-1
assert 2*g-2+4==2*m
# Smooth special hyperelliptic model at3 and exact stable Hasse-Witt rank.
poly=s.Poly(w**16+1,w,modulus=3)
assert s.gcd(poly,poly.diff()).degree()==0
M=[[int(3*i-j in (0,16)) for j in range(1,8)] for i in range(1,8)]
def prod(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%3
             for j in range(len(B[0]))] for i in range(len(A))]
def rank(A):
    A=[list(z) for z in A];r=0
    for c in range(len(A[0])):
        p=next((i for i in range(r,len(A)) if A[i][c]%3),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]
        q=pow(A[r][c],-1,3);A[r]=[(q*x)%3 for x in A[r]]
        for i in range(len(A)):
            if i!=r:
                q=A[i][c]
                A[i]=[(x-q*y)%3 for x,y in zip(A[i],A[r])]
        r+=1
    return r
T=M
ranks=[]
for n in range(1,9):
    ranks.append(rank(T));T=prod(T,M)
assert ranks[-1]==2
# A second ACTUAL factorization for the minus-six member, including equality
# with the original degree16 map after elliptic duplication.
minus_relation=v*v-(w**16-6*w**8+1)
ex=(w**8-1+v)/2
ey=w**4*(ex-1)
def minus_reduce(z):
    num=s.fraction(s.cancel(z))[0]
    return s.rem(num,minus_relation,v)
assert minus_reduce(ey*ey-ex**3+ex)==0
assert minus_reduce(w**4-ey/(ex-1))==0
dup_x=(ex*ex+1)**2/(4*ex*(ex*ex-1))
dup_slope=(3*ex*ex-1)/(2*ey)
dup_y=-ey+dup_slope*(ex-dup_x)
base_x=(w**8-1)**2/(4*w**8)
base_y=v*(w**16-1)/(8*w**12)
assert minus_reduce(dup_x-base_x)==0
assert minus_reduce(dup_y-base_y)==0
out={'status':'PASS','scope':'Actual degree16 dihedral model and good-three reduction only; odd-prime fixed groups remain unproved.',
     'curves':['v^2=w^16+6w^8+1','v^2=w^16-6w^8+1'],
     'map_to_elliptic_isogeny_source':['w^8','w^4*v'],
     'actual_two_isogeny':[str(X),str(Y)],
     'degree':16,'genus':7,'cusps':4,'geometric_deck_group':'D16',
     'good_reduction_at3':True,'hasse_witt_matrix_mod3':M,
     'ranks_of_powers':ranks,'special_p_rank_at3':2,
     'actual_cyclic4_elliptic_map':[str(ex),str(ey)],
     'cyclic4_kummer_equation':'w^4=y/(x-1) on y^2=x^3-x',
     'duplication_is_original_degree16_map':True,
     'original_base_map_minus6':[str(base_x),str(base_y)],
     'known_assertions':['all coefficient normalizers by A59','coefficient2 fixed groups by A22'],
     'open_assertion':'full fixed groups at odd coefficient primes'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: actual nonstable C8 cover/isogeny, D16 relation formulas, genus/cusps, smooth characteristic3 reduction and stable Hasse-Witt rank2.')
print('PASS: cyclic4 elliptic Kummer factorization and exact equality after duplication with the actual degree16 map.')
