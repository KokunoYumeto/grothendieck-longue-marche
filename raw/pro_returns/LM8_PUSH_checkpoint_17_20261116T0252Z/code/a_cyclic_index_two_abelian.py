#!/usr/bin/env python3
"""Exact presentation normalization support for A76; no geometry inferred."""
from pathlib import Path
import json,math


def run():
    rows=[]
    for a in range(0,11):
        modulus=2**a
        roots=[k for k in range(modulus) if math.gcd(k,modulus)==1 and k*k%modulus==1%modulus]
        expected=([0] if a==0 else [1] if a==1 else [1,3] if a==2 else sorted([1,modulus-1,1+modulus//2,modulus//2-1]))
        assert roots==expected
        cases=[]
        for k in roots:
            allowed=[h for h in range(modulus) if ((k-1)*h)%modulus==0]
            for h in allowed:
                orbit=sorted({(h+(1+k)*b)%modulus for b in range(modulus)})
                if a<=1 or k==1:
                    kind='cyclic' if h%2 or a==0 else 'cyclic_times_C2'
                    if h%2:assert 1 in orbit
                    else:assert 0 in orbit
                elif k==modulus-1:
                    assert h in [0,modulus//2]
                    kind='dihedral' if h==0 else 'quaternion'
                elif k==modulus//2-1:
                    assert a>=3 and h in [0,modulus//2] and 0 in orbit
                    kind='semidihedral'
                else:
                    assert a>=3 and k==modulus//2+1 and h%2==0 and 0 in orbit
                    kind='modular'
                cases.append({'k':k,'h':h,'normalized_type':kind,'contains_zero_after_generator_change':0 in orbit})
        rows.append({'cyclic_subgroup_exponent_a':a,'cyclic_subgroup_order':modulus,'roots_of_one':roots,'all_consistent_presentations':cases})
    return {'status':'PASS','candidate':'A.76, registered after full audits','rows':rows,'scope':'Exact congruence and generator-change checks, including all small orders. The actual connected fibre-product, model and rational-path comparisons are structural and proved in the draft.'}


if __name__=='__main__':
    out=run();Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'levels':len(out['rows']),'largest_cyclic_subgroup_order':out['rows'][-1]['cyclic_subgroup_order'],'consistent_presentations':sum(len(r['all_consistent_presentations']) for r in out['rows'])},indent=2))
