"""Exact mod-5 Iwasawa coefficients from level-32 rational paths.

Finite certificates only: outputs do not themselves identify Selmer groups.
Generator gamma=6 in 1+5 Z5; a=omega(a)*6^t modulo 5^n.
For k<5^(n-1), binomial(t,k) modulo5 is locally constant modulo5^n.
"""
from fractions import Fraction
from functools import lru_cache
from pathlib import Path
from math import comb
import json
from F_advanced_symbols import symbol

HERE=Path(__file__).resolve().parent
source=json.loads((HERE/'F_advanced_symbols.json').read_text())
Phi=source['integral_period_dual_basis_columns']
chi={int(a):e for a,e in source['twist_character'].items()}

@lru_cache(None)
def value(r):
    vec=symbol(r)
    return tuple(sum(vec[a]*Phi[a][i] for a in range(len(vec))) for i in range(2))

@lru_cache(None)
def raw(d,r):
    if d==1:return value(r)
    assert d==6
    return tuple(sum(e*value(r+Fraction(a,24))[i] for a,e in chi.items() if e)
                 for i in range(2))

def main():
    out={'prime':5,'gamma':6,'alpha_mod_5':3,'levels':{}}
    for n in [1,2,3]:
        modulus=5**n
        order=5**(n-1)
        gamma_log={pow(6,t,modulus):t for t in range(order)}
        assert len(gamma_log)==order
        units=[a for a in range(1,modulus) if a%5]
        logs={}
        for a in units:
            omega=pow(a,order,modulus)
            assert pow(omega,4,modulus)==1 and omega%5==a%5
            logs[a]=gamma_log[a*pow(omega,-1,modulus)%modulus]
        lev={'modulus':modulus,'gamma_logs':logs,'curves':{}}
        for d in [1,6]:
            raw_values={a:raw(d,Fraction(a,modulus)) for a in units}
            parent_values={a:raw(d,Fraction(a,modulus//5)) for a in units}
            measure={a:[(pow(3,-n,5)*raw_values[a][i]
                         -pow(3,-n-1,5)*parent_values[a][i])%5
                        for i in range(2)] for a in units}
            coefficients={j:[[sum(pow(a,j,5)*comb(logs[a],k)*measure[a][i]
                                  for a in units)%5 for i in range(2)]
                             for k in range(order)] for j in range(4)}
            first={j:next((k for k,v in enumerate(coefficients[j]) if any(v)),None)
                   for j in range(4)}
            exact_quadratic_moment=[sum((1 if a%5 in [1,4] else -1)*raw_values[a][i]
                                       for a in units) for i in range(2)] if n==1 else None
            lev['curves'][d]={
                'raw_path_values':raw_values,'raw_parent_values':parent_values,
                'ordinary_measure_mod_5':measure,
                'Iwasawa_coefficients_mod_5':coefficients,
                'first_nonzero_coefficient':first,
                'quadratic_character_raw_central_value':exact_quadratic_moment,
            }
            if n>1:
                prev=out['levels'][n-1]['curves'][d]['Iwasawa_coefficients_mod_5']
                for j in range(4):assert coefficients[j][:5**(n-2)]==prev[j]
            print('n,d,first',n,d,first,flush=True)
            if n==2:print('n2coeff',d,coefficients,flush=True)
        out['levels'][n]=lev
    out['scope']='Complete mod5 coefficients through degree24 for all four branches on E1 and E6, checked for compatibility at levels5,25,125. Theorems require the separate analytic and cohomological argument.'
    (HERE/'F_advanced_even_branches.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
