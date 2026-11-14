#!/usr/bin/env python3
"""Exact lattice/finite-quotient checks for the B.16u thickness formula.

The proof of JSJ reconstruction is not a finite test. These calculations
check the integral local gluing and its profinite finite-quotient images.
"""
import json
from math import gcd
from pathlib import Path

import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

checks=[]

def record(name,passed,details):
    assert passed,(name,details)
    checks.append({'name':name,'passed':bool(passed),'details':details})

m=sp.symbols('m',integer=True,positive=True)
for eps in (-1,1):
    gluing=sp.Matrix([[-1,eps*m],[0,1]])
    slopes=sp.Matrix([[0,eps*m],[1,1]])
    record(f'orientation_and_fibre_determinant_sign_{eps}',
           gluing.det()==-1 and slopes.det()==-eps*m,
           'The orientation-reversing torus gluing sends the time fibre '
           'to (epsilon*m,1); adjacent fibre slopes have determinant -epsilon*m.')

smith_cases=0
for mm in range(1,129):
    for eps in (-1,1):
        normal=smith_normal_form(sp.Matrix([[0,eps*mm],[1,1]]),domain=ZZ)
        assert sorted(abs(normal[i,i]) for i in range(2))==[1,mm]
        smith_cases+=1
record('integer_cokernel',True,
       {'smith_cases':smith_cases,'m_range':[1,128],
        'conclusion':'Cokernel is cyclic of order m, including m=1.'})

finite_cases=0
unit_cases=0
for modulus in range(1,33):
    for mm in range(1,65):
        subgroup={((b*mm)%modulus,(a+b)%modulus)
                  for a in range(modulus) for b in range(modulus)}
        assert modulus**2//len(subgroup)==gcd(mm,modulus)
        finite_cases+=1
        for unit in (u for u in range(modulus) if gcd(u,modulus)==1):
            # The matrix [[unit,1],[0,1]] is an invertible coordinate
            # change modulo the modulus, hence preserves subgroup index.
            # Check its actual image set.
            image={((unit*x+y)%modulus,y) for x,y in subgroup}
            assert len(image)==len(subgroup)
            unit_cases+=1
record('finite_quotient_index_and_coordinate_units',True,
       {'finite_cases':finite_cases,'unit_basis_changes':unit_cases,
        'moduli':[1,32],'m_range':[1,64],
        'conclusion':'Index modulo N is gcd(m,N), invariant under tested GL2 basis changes.'})

base_change_cases=0
for mm in range(1,65):
    for degree in range(1,17):
        changed=sp.Matrix([[0,degree*mm],[1,1]])
        assert abs(changed.det())==degree*mm
        base_change_cases+=1
record('ramified_base_change_thickness',True,
       {'cases':base_change_cases,'formula':'m maps to d*m under inertia subgroup d*Zhat.'})

result={'passed':len(checks),'checks':checks,
        'scope':'Exact local arithmetic only; full proof and source hypotheses are in B.16u.'}
Path(__file__).with_name('BC_jsj_checks_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
