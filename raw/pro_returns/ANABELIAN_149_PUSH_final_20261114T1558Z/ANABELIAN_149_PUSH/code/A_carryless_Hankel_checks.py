#!/usr/bin/env python3
"""Compare accelerated complete Hankel outputs with saved canonical runs."""
from pathlib import Path
import json,time
import A_theta_F4_moduli_scan as scan
from A_carryless_accelerator import clmul,DIGEST

ROOT=Path(__file__).parent

def main():
    main=json.loads((ROOT/'A_theta_F4_moduli_scan.json').read_text())
    targets=[]
    for key,n in [('203',25),('102',49)]:
        row=next(r for r in main['curves'] if r['moduli_key']==key)
        old=next(t for t in row['tests'] if t['n']==n)
        targets.append((key,row['coefficients'],old))
    extra=json.loads((ROOT/'A_theta_F4_remaining_73_89.json').read_text())
    old=next(t for t in extra['tests'] if t['n']==73)
    targets.append(('203',[1,9,14],old))
    scan.clmul=clmul;A=scan.Arithmetic(4,19);results=[]
    for key,abc,old in targets:
        new=A.test(abc,old['n'])
        for field in ['theta_n_exists','coordinate_polynomial_degree','coordinate_polynomial_masks','coordinate_polynomial_coefficients','all_minors_or_unit_gcd']:
            assert new[field]==old[field],(key,old['n'],field)
        results.append({'moduli_key':key,'n':old['n'],'canonical_seconds':old['runtime_seconds'],
                        'accelerated_seconds':new['runtime_seconds'],'theta_n_exists':new['theta_n_exists'],
                        'coordinate_degree':new['coordinate_polynomial_degree'],'exact_gcd_agrees':True})
        print(results[-1],flush=True)
    out={'status':'PASS','C_source_sha256':DIGEST,'comparisons':results,
         'scope':'Negative, positive high-order, and partial-primitive high-order complete gcds agree with separate earlier canonical runs.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
