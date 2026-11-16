#!/usr/bin/env python3
"""Exact first-depth unit and branch-direction probe; no global repair claim."""
from pathlib import Path
import sympy as sp

x=sp.Symbol('x')
norm=sp.resultant(x**3-3,x**2-2,x)
assert norm==1
q=61;g=int(sp.primitive_root(q));roots=[4,5,52]
assert all(pow(a,3,q)==3 for a in roots)
zeta=roots[1]*pow(roots[0],-1,q)%q
assert roots==[roots[0]*pow(zeta,i,q)%q for i in range(3)]
units=[(a*a-2)%q for a in roots]
characters=[int(sp.discrete_log(q,u,g))%3 for u in units]
quotient=(characters[1]+2*characters[2])%3
assert units==[14,23,18] and characters==[2,0,1] and quotient==2
cyclo=next(j for j in range(3) if q%9 in {pow(4,j,9),-pow(4,j,9)%9})
assert cyclo==quotient
out=(f'Norm of alpha^2-2 for alpha^3=3: {norm}.\n'
     f'q={q}; primitive residue unit {g}; root labels {roots}.\n'
     f'Unit residues {units}; cubic characters {characters}.\n'
     f'Relative coinvariant {quotient}; cyclotomic cubic value {cyclo}.\n'
     'The exact field identification additionally uses unramified-away-three '
     'Kummer ramification and the unique cubic character of the cyclotomic '
     'three-power unit group; no sheared-support existence theorem is claimed.\n')
Path(__file__).with_name('cyclotomic_relative_unit_probe_output.txt').write_text(out)
print(out,end='')
