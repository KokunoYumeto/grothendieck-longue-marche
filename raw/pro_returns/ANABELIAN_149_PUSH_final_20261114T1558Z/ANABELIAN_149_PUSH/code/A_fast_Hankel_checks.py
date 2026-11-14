#!/usr/bin/env python3
"""Reproduce the saved full-C versus canonical complete Hankel comparisons."""
from pathlib import Path
import json
from A_fast_polynomials import FastArithmetic,DIGEST

ROOT=Path(__file__).parent

def main():
    data=json.loads((ROOT/'A_theta_F4_moduli_scan.json').read_text());cases=[]
    for key,n in [('203',25),('102',49)]:
        row=next(r for r in data['curves'] if r['moduli_key']==key)
        old=next(t for t in row['tests'] if t['n']==n)
        cases.append((key,row['coefficients'],old))
    data=json.loads((ROOT/'A_theta_F4_remaining_73_89.json').read_text())
    cases.append(('203',[1,9,14],next(t for t in data['tests'] if t['n']==73)))
    A=FastArithmetic(4,19);out={'status':'PASS','source_sha256':DIGEST,'comparisons':[]}
    for key,abc,old in cases:
        new=A.test(abc,old['n'])
        for field in ['theta_n_exists','coordinate_polynomial_degree','coordinate_polynomial_masks','coordinate_polynomial_coefficients','all_minors_or_unit_gcd']:
            assert new[field]==old[field],(key,old['n'],field)
        result={'moduli_key':key,'n':old['n'],'canonical_seconds':old['runtime_seconds'],
                'accelerated_seconds':new['runtime_seconds'],'theta_n_exists':new['theta_n_exists'],
                'coordinate_degree':new['coordinate_polynomial_degree'],'exact_gcd_agrees':True}
        out['comparisons'].append(result);print(result,flush=True)
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
