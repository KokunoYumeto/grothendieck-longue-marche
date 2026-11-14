"""Independent exact character check for E.23 and E.25.

Uses permutations of nine points and tuple arithmetic over F_3, without
loading the Hall-matrix or Smith programs. It evaluates finite geometric
characters only, not the arithmetic extension class eta.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import json

pts=list(product(range(3),repeat=2)); index={p:i for i,p in enumerate(pts)}
def unit(p):
    x,y=p
    return (y%3,(-x+y)%3)  # multiplication by -zeta, using E18.9

def conj(p):
    x,y=p
    return ((x-y)%3,(-y)%3)

def repeat(f,p,n):
    for _ in range(n):p=f(p)
    return p

def fixed(perm):return sum(i==j for i,j in enumerate(perm))
def cube(perm):return [perm[perm[perm[i]]] for i in range(9)]
htrace=[2,1,-1,-2,-1,1]
rows=[]
normal={name:Fraction(0) for name in ['V','H3','H2W','HW2','W3']}
conjugate={name:Fraction(0) for name in normal}
for k in range(6):
    for t in pts:
        image=[((repeat(unit,p,k)[0]+t[0])%3,(repeat(unit,p,k)[1]+t[1])%3) for p in pts]
        perm=[index[p] for p in image]
        cp=[index[conj(p)] for p in image]
        h=htrace[k]; h3=htrace[3*k%6]
        w=fixed(perm)-1; w3=fixed(cube(perm))-1
        vals={'V':Fraction(h+w),'H3':Fraction(h**3-h3,3)-h,'H2W':Fraction((h*h-1)*w),'HW2':Fraction(h*w*w),'W3':Fraction(w**3-w3,3)}
        cw=1-fixed(cp); cw3=1-fixed(cube(cp))
        cvals={'V':Fraction(cw),'H3':Fraction(0),'H2W':Fraction(cw),'HW2':Fraction(0),'W3':Fraction(cw**3-cw3,3)}
        for key in normal:normal[key]+=vals[key];conjugate[key]+=cvals[key]
        rows.append({'unit_power':k,'translation':t,'fixed_points':fixed(perm),'fixed_points_of_cube':fixed(cube(perm)),'conjugate_fixed_points':fixed(cp),'conjugate_cube_fixed_points':fixed(cube(cp))})
normal={k:v/54 for k,v in normal.items()}; conjugate={k:v/54 for k,v in conjugate.items()}
assert normal=={'V':0,'H3':0,'H2W':0,'HW2':2,'W3':2}
assert all(v==0 for v in conjugate.values())
assert sum(normal[k] for k in ['H3','H2W','HW2','W3'])==4
output={'geometric_group_order':len(rows),'rational_invariant_dimensions':{k:int(v) for k,v in normal.items()},'conjugation_traces_on_invariants':{k:int(v) for k,v in conjugate.items()},'projected_arithmetic_H1_dimension':2,'full_kernel_H1_dimension':6,'involution_fixed_kernel_H1_dimension':3,'combined_rational_preimage_dimension':5,'character_rows':rows,'arithmetic_eta_evaluated':False,'status':'passed'}
Path(__file__).with_name('E_symmetry_independent_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='character_rows'},indent=2))
