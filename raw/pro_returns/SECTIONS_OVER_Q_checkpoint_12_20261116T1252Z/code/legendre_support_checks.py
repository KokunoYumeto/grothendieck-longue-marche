#!/usr/bin/env python3
"""Exact finite certificates for the support/logarithm continuation.

All logarithm valuations below are computed from Fermat quotients;
no real or p-adic floating-point approximation is used.
"""
from fractions import Fraction
import sympy as sp

def vp(n,p):
    n=Fraction(n)
    def vint(a):
        a=abs(a); v=0
        assert a
        while a%p==0:
            a//=p; v+=1
        return v
    return vint(n.numerator)-vint(n.denominator)

def odd_unit_mod8(n):
    v=vp(n,2)
    u=Fraction(n)/(Fraction(2)**v)
    return (u.numerator*pow(u.denominator,-1,8))%8

def possible_2_contacts(la):
    """Valuations allowed by squareclasses and potentially good j at2."""
    av,bv=vp(la,2)%2,vp(1-la,2)%2
    au,bu=odd_unit_mod8(la),odd_unit_mod8(1-la)
    ans=[]
    for m in range(1,5):
        if m%2==av and bv==0 and (1-2**m*au)%8==bu:
            ans.append((m,0))
        if av==0 and m%2==bv and (1-2**m*bu)%8==au:
            ans.append((0,m))
        if av==bv==m%2 and (2**m-au)%8==bu:
            ans.append((-m,-m))
    return sorted(ans)

def recognition_family(la):
    odd=la if la%2 else la-1
    even=la-1 if la%2 else la
    return odd>1 and len(sp.factorint(odd))==1 and vp(even,2)%2==1

print('A.41 prime-power odd-neighbour recognition test, 2<=lambda<=100')
print([la for la in range(2,101) if recognition_family(la)])

print('\nPotentially good 2-adic contact certificates')
for la in (6,7,10,11,12,13,15,16,17,20,21,22,28,29):
    jj=Fraction(256*(la*la-la+1)**3,la*la*(1-la)**2)
    print('lambda=',la,'v2(j)=',vp(jj,2),
          'square units=',(odd_unit_mod8(la),odd_unit_mod8(1-la)),
          'contact pairs=',possible_2_contacts(la),
          'v2(4lambda(1-lambda)) mod3=',vp(4*la*(1-la),2)%3)
    assert vp(jj,2)>=0

print('\nExact valuations of p-adic logarithms of rational units')
for p,base in ((5,2),(5,3),(5,7),(11,3),(11,7)):
    fermat=base**(p-1)-1
    print('p=',p,'base=',base,'base^(p-1)-1=',fermat,
          'v_p(log_p(base))=',vp(fermat,p))

print('\nCubic-quotient orientation checks')
print('lambda15: v5(D)=',vp(4*15*(1-15),5),
      'v7(D)=',vp(4*15*(1-15),7))
print('lambda15 cusp0 at3: unit residues of -2*7^b modulo9=',
      [(b,(-2*pow(7,b,9))%9) for b in range(3)])
print('lambda28: v2(D) mod3=',vp(4*28*(1-28),2)%3,
      'negative contact D-valuation mod3=',(-2)%3,
      'v7(D) mod3=',vp(4*28*(1-28),7)%3)
print('lambda28 cusp1 at3: unit residues of 7^a modulo9=',
      [(a,pow(7,a,9)) for a in range(3)],'target4')

print('\nExploratory exact Frobenius traces at good small primes')
for la in range(10,21):
    vals=[]
    for p in (7,11,13,17,19,23):
        if la%p in (0,1):
            continue
        n=1+sum(1 if (v:=x*(x-1)*(x-la)%p)==0 else
                2 if pow(v,(p-1)//2,p)==1 else 0 for x in range(p))
        vals.append((p,p+1-n))
    print('lambda=',la,'(p,a_p)=',vals)
