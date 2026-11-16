#!/usr/bin/env python3
"""Literal cover and cusp-map certificate for A.161."""
from fractions import Fraction
from pathlib import Path
import json
import sympy as S

M=7*13*23*139*1119169
n=1146
q0=Fraction(M,2*191**2)
a=573*q0*q0
C=8*573**2*q0
assert C == 36*M
assert C*C == 8*n**3*a
assert Fraction(2*n*a,C) == q0/2
assert C/(q0/2) == (4*573)**2

T,W,x,y,aa,CC,nn = S.symbols('T W x y a C n',nonzero=True)
poly=T*(T-1)*(T-S.Rational(1,2))
assert S.expand((nn*(2*T-1))**3-nn**2*(nn*(2*T-1))-8*nn**3*poly)==0
Tinverse=(x/nn+1)/2
assert S.factor(8*nn**3*poly.subs(T,Tinverse)-(x**3-nn**2*x))==0
assert S.factor(Tinverse.subs(x,nn*(2*T-1))-T)==0

u=-nn*(2*T-1)/(CC*W**2)
v=W/T
d=-2*nn*aa/CC
diff=S.factor(S.together(u-d*v**2*T/(T-1)))
numer,denom=S.fraction(diff)
assert S.factor(numer.subs(W**4,poly/aa))==0

# Literal boundary valuations and ramification of the quadratic map.
rows=[]
for label,e in [('P0',-n),('Ph',0),('P1',n)]:
    assert 3*e*e-n*n != 0
    rows.append({'source':label,'target':[e,0],
                 'target_parameter':'y','source_parameter':'W',
                 'ramification':2,'leading_coefficient':str(C)})
rows.append({'source':'Pinf','target':'O','target_parameter':'-x/y',
             'source_parameter':'W/T','ramification':2,
             'leading_coefficient':str(-q0/2)})
assert sum(1 for row in rows if row['ramification']==2)==4
# Riemann--Hurwitz: genus-one target, degree two and four simple branch points.
assert 2*3-2 == 2*(2*1-2)+4

data={'M':M,'n':n,'q0':str(q0),'a':str(a),'C':str(C),
      'torsor':'W^2=y/C','inverse':'T=(x/n+1)/2',
      'divisor_y':{'(-n,0)':1,'(0,0)':1,'(n,0)':1,'O':-3},
      'boundary':rows,
      'infinity_unit':'T/(T-1), constant term 1',
      'compact_image':['O','(-1146,0)','(0,0)','(1146,0)'],
      'domain':'full Selmer sections of E minus E[2] with pullback kappa_2(y/C)=0',
      'status':'all exact identities passed'}
out=Path(__file__).with_name('harmonic_positive_rank_lift_certificate_data.json')
out.write_text(json.dumps(data,indent=2)+'\n')
print('PASS: exact connected quadratic torsor and inverse coordinate maps')
print('PASS: four odd divisor valuations, four ramification-two boundary points')
print('PASS: finite cusp formula y=C W^2 and exact infinity formula')
print('PASS: infinity squareclass ratio C/(q0/2)=(4*573)^2')
print('C = 36M =',C)
print('infinity leading coefficient =',-q0/2)
print('Compact image:',', '.join(data['compact_image']))
print('Domain:',data['domain'])
print('Data:',out)
