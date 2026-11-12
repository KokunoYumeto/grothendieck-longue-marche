#!/usr/bin/env python3
"""Exact polynomial and local certificates for the corrected Part D example."""
from sympy import symbols, Poly, discriminant, factor, Rational
from sympy.polys.numberfields import round_two
from itertools import product
from math import prod
import json
x=symbols('x');f=x**3-12*x-14
assert all(f.subs(x,k)!=0 for k in (-14,-7,-2,-1,1,2,7,14))
rows=[]
for p in (2,3,5):
 rows.append(dict(prime=p,factorization=str(factor(f,modulus=p))))
ZK,dK=round_two(Poly(f,x))
assert dK==1620
# Dedekind index criterion at the only primes whose square divides disc(f).
h2=x**3;h3=(x+1)**3
r2=Poly((f-h2)/2,x);r3=Poly((f-h3).expand()/3,x)
assert int(r2.eval(0))%2!=0 and int(r3.eval(-1))%3!=0
# Exact Hilbert symbols for (a,b) at finite primes dividing 2ab and infinity.
def vunit(a,p):
 v=0
 while a%p==0:a//=p;v+=1
 return v,a
def hs(a,b,p):
 va,u=vunit(a,p);vb,v=vunit(b,p)
 if p==2:return (-1)**((((u-1)*(v-1))//4 + va*((v*v-1)//8) + vb*((u*u-1)//8))%2)
 lu=1 if pow(u%p,(p-1)//2,p)==1 else -1
 lv=1 if pow(v%p,(p-1)//2,p)==1 else -1
 return (-1)**(va*vb*((p-1)//2))*lu**vb*lv**va
symbols={str((a,b)):{str(p):hs(a,b,p) for p in (2,3,5)}|{'infinity':-1 if a<0 and b<0 else 1} for a,b in [(-3,3),(-1,-3),(5,-1)]}
assert symbols[str((-3,3))]=={'2':1,'3':1,'5':1,'infinity':1}
assert symbols[str((-1,-3))]=={'2':1,'3':-1,'5':1,'infinity':-1}
# Dirichlet characters modulo 5: 2 generator, chi4(2)=i, chi4^2=Legendre.
chars={pow(2,k,5):k for k in range(4)}
assert all((chars[(a*b)%5]-chars[a]-chars[b])%4==0 for a,b in product(chars,repeat=2))
assert all((-1)**k==(1 if a in (1,4) else -1) for a,k in chars.items())
assert all(next(k for k in range(1,5) if pow(p,k,5)==1)==4 for p in (2,3))
# The two cubic primes are Eisenstein, at 3 after translation.
assert int(Poly(f,x).TC())%4==2
shift=Poly(f.subs(x,x-1).expand(),x)
assert all(int(c)%3==0 for c in shift.all_coeffs()[1:])
assert int(shift.TC())%9!=0
print(json.dumps(dict(cubic=str(f),irreducible_by_rational_root_test=True,polynomial_discriminant=int(discriminant(f,x)),field_discriminant=int(dK),index_certificate_mod2=int(r2.eval(0))%2,index_certificate_mod3=int(r3.eval(-1))%3,local_factorizations=rows,hilbert_symbols=symbols,quartic_character_mod5_exponents=chars,corrected_Dic3_extension={'construction':'splitting field(x^3-12x-14) times Q(zeta5)','degree':12,'quadratic_sign_field':'Q(sqrt5)','ramified_primes':[2,3,5],'ramification_indices':{'2':3,'3':3,'5':4},'residue_degrees':{'2':4,'3':4,'5':1},'number_of_primes':{'2':1,'3':1,'5':3}}),indent=2))
