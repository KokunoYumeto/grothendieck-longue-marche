#!/usr/bin/env python3
"""Full all-point certificate for the genus-two cyclic-13 example.

The cover is the infinity-pointed Lang cover associated to the quotient
chi:J(F64)->F13 obtained by multiplication by304 and a specified generator.
This file gives every point, its class and quotient coordinate, the entire
13-subgroup table, and the full Frobenius polynomial.
"""
from pathlib import Path
from collections import Counter
import json
import sympy as sp
from b5_char2_probe import BinaryField, Jacobian

T=sp.symbols('T')
K=BinaryField(6,67)  # F2[z]/(z^6+z+1), binary polynomial encoding.
J=Jacobian(K,0);J.h=(0,0,1);J.f=(0,1,0,0,0,1)
H2=T**4+T**3+2*T+4
assert sp.Poly(H2,T,modulus=3).is_irreducible
M=sp.Matrix([[0,0,0,-4],[1,0,0,-2],[0,1,0,0],[0,0,1,-1]])
H64=(M**6).charpoly(T).as_expr()
assert H64==T**4-T**3-80*T**2-64*T+4096
order=int(H64.subs(T,1));assert order==3952==16*13*19
points=J.points();assert len(points)==64
projected=[J.multiple(J.pointclass(P),304) for P in points]
generator=next(D for D in projected if D!=J.O)
assert J.multiple(generator,13)==J.O
log={};subgroup=[];D=J.O
for j in range(13):
    assert D not in log
    log[D]=j;subgroup.append({'j':j,'u':D[0],'v':D[1]})
    D=J.add(D,generator)
assert D==J.O
table=[]
for P,D in zip(points,projected):
    assert J.multiple(D,13)==J.O
    table.append({'point':P,'u':D[0],'v':D[1],'chi':log[D]})
counts=Counter(row['chi'] for row in table)
assert [counts[i] for i in range(13)]==[16]+[4]*12
Q=1+12*T+64*T**2
PC=1-T-80*T**2-64*T**3+4096*T**4
PD=sp.Poly(PC*Q**12,T)
certificate={
    'curve':'Y^2+X^2Y=X^5+X',
    'basepoint':'the unique point at infinity',
    'field':{'characteristic':2,'degree':6,'modulus_bits':67,'modulus':'z^6+z+1'},
    'F2_Frobenius_characteristic_polynomial':str(H2),
    'F64_Frobenius_characteristic_polynomial':str(H64),
    'jacobian_order':order,'projection_multiplier':304,
    'generator':{'u':generator[0],'v':generator[1]},
    'subgroup_table':subgroup,'point_table':table,
    'point_occupancies':[counts[i] for i in range(13)],
    'twisted_L_polynomial_all_nontrivial_characters':[1,12,64],
    'D_F64_zeta_numerator_factorization':'(1-T-80*T^2-64*T^3+4096*T^4)*(1+12*T+64*T^2)^12',
    'D_F64_zeta_numerator_coefficients_ascending':[int(PD.nth(i)) for i in range(29)],
    'relative_class_number':77**12,
    'newton_slopes_new_factor':{'1/3':12,'2/3':12},
    'genus_C':2,'genus_D':14,
    'conclusions':['connected pointed cyclic etale degree13 cover',
                   'primitive factor has 2-rank zero',
                   'relative class number is odd',
                   'D has no nonzero supersingular Jacobian factor even geometrically']}
Path(__file__).with_suffix('.json').write_text(json.dumps(certificate,indent=2)+'\n')
print('generator',generator)
print('occupancies',[counts[i] for i in range(13)])
print('F64 characteristic polynomial',H64)
print('full D numerator',PD.as_expr())
print('relative class number',77**12)
