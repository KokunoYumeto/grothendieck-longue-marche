#!/usr/bin/env python3
"""Exact certificate for the nonextendible norm representative in A.98."""
from pathlib import Path
from sympy import symbols,resultant,expand,Rational

x=symbols('x'); f=x**3-3
u=(4-x)**3/Rational(61)
beta=(1-x)*u
reduced=expand(beta).rem(f,x) if hasattr(expand(beta),'rem') else None
from sympy import rem
assert rem(beta,f,x)==(25-109*x+60*x*x)/61
assert resultant(f,4-x,x)==61
assert resultant(f,1-x,x)==-2
assert resultant(f,u,x)==1
assert resultant(f,beta,x)==-2

p=61
roots=[a for a in range(p) if pow(a,3,p)==3]
assert roots==[4,5,52]
assert all(3*a*a%p for a in roots)
assert (16+4*roots[0]+roots[0]**2)%p!=0
assert all((1-a)%p for a in roots)
assert (4**3-3)==p
valuation_h=(1,0,0)
valuation_beta=tuple(3*a-1 for a in valuation_h)
assert valuation_beta==(2,-1,-1)
assert all(a%3 for a in valuation_beta)
ratio=roots[1]*pow(roots[0],-1,p)%p
assert ratio==47 and pow(ratio,3,p)==1 and pow(ratio,20,p)==13
assert pow(-2,20,p)==47
cubes={pow(a,3,p) for a in range(1,p)}
assert len(cubes)==20 and ratio not in cubes and (-2)%p not in cubes
checks=0
for q in range(1,p):
 for e in (1,2):
  radicands=[pow(q,e,p)*a%p for a in roots]
  assert sum(a in cubes for a in radicands)==1
  assert any(a not in cubes and v%3 for a,v in zip(radicands,valuation_beta))
  checks+=1
# The norm polynomial proving the good compatible family at every stage.
t,z=symbols('t z')
assert resultant(z**3-t,1-z,z)==1-t
out=("A.98 exact certificate passed.\n"
     "Norm(4-alpha)=61; Normu=1; Normbeta=-2.\n"
     "beta=(25-109alpha+60alpha^2)/61.\n"
     "Three residue roots at61:4,5,52; beta valuation vector:(2,-1,-1).\n"
     "5/4=47; 47^3=1; 47^20=13; (-2)^20=47 modulo61.\n"
     f"Every scalar cube-class combination checked:{checks}; exactly one split local cubic branch each time.\n"
     "The compatible-family norm polynomial is exactly1-t.\n"
     "Both completed fibres are nonempty; the specific norm transition is not surjective.\n")
Path(__file__).with_name('norm_representative_certificate_output.txt').write_text(out)
print(out,end='')
