#!/usr/bin/env python3
"""Exploratory self-residue data in Q(zeta5); NOT legal original first primes.

This exact finite experiment tests possible identities in E202's matrix.
It never asserts the enormous original CRT/splitting conditions or
first-gate consistency, and supplies no counterexample to the main problem.
"""
from itertools import product
from pathlib import Path
import json
from sympy import isprime, primitive_root

def norm(a,b,c,d):
    return (a**4-a**3*b-a**3*c-a**3*d+a*a*b*b+2*a*a*b*c+2*a*a*b*d+a*a*c*c-3*a*a*c*d+a*a*d*d-a*b**3-3*a*b*b*c+2*a*b*b*d+2*a*b*c*c-a*b*c*d-3*a*b*d*d-a*c**3+2*a*c*c*d+2*a*c*d*d-a*d**3+b**4-b**3*c-b**3*d+b*b*c*c+2*b*b*c*d+b*b*d*d-b*c**3-3*b*c*c*d+2*b*c*d*d-b*d**3+c**4-c**3*d+c*c*d*d-c*d**3+d**4)

rows=[];seen=set()
for co in product(range(-6,7),repeat=4):
    p=norm(*co)
    if p in seen or p<=5 or p%5!=1 or not isprime(p):continue
    seen.add(p)
    g=int(primitive_root(p));omegas=[pow(g,(p-1)//5*i,p) for i in range(1,5)]
    def evaluate(t):return sum(a*pow(t,i,p) for i,a in enumerate(co))%p
    roots=[w for w in omegas if evaluate(w)==0]
    assert len(roots)==1
    w=roots[0]
    def log(t):
        residue=pow(t%p,(p-1)//5,p)
        return next(i for i in range(5) if pow(w,i,p)==residue)
    u=1
    for a in range(2,5):u=u*pow(evaluate(pow(w,a,p)),a-1,p)%p
    rows.append({'p':p,'prime_generator':co,'omega':w,'self':log(u),
                 'alpha_3':log(3),'beta_minus2':log(-2),
                 'q_diagonal':log(3*u),'r_diagonal':log(-2*u),
                 'p_mod25':p%25,'p_mod120':p%120,
                 'minus2_24_power':p%24==1 and pow(-2%p,(p-1)//24,p)==1})
rows.sort(key=lambda r:r['p'])
groups={}
for r in rows:groups.setdefault(str(r['p_mod25']),set()).add(r['self'])
shell=[r for r in rows if r['p_mod25']==6 and r['p_mod120']==1 and r['minus2_24_power']]
result={'scope':'Exploratory exact residues only. None of these primes is certified legal for E102; no first matrix or affine constant is solved.',
        'prime_count':len(rows),'self_values_by_mod25':{k:sorted(v) for k,v in sorted(groups.items())},
        'selected_partial_q_constraints':shell,'rows':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
