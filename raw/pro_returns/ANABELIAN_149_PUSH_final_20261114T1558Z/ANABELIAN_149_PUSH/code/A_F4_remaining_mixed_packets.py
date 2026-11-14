#!/usr/bin/env python3
"""Exact mixed-primary Frobenius certificates for moduli keys203 and302.

This does not rerun or modify the long Hankel scans. It verifies the finite
operator identities and links each resulting exponent to an already saved
complete geometric theta-exclusion certificate. The finite-support fixed-
field lemma is A.C2.14; no A1 conclusion is made for these two curves.
"""
from pathlib import Path
from math import lcm,prod
import json
import sympy as sp
import A_F4_remaining_frobenius_packets as packet

ROOT=Path(__file__).parent
SOURCES=[
    'A_theta_F4_moduli_scan.json',
    'A_theta_F4_moduli_other_orbits.json',
    'A_theta_F4_remaining_multi_orbits.json',
    'A_theta_F4_remaining_75_79.json',
    'A_theta_F4_remaining_good_mixed.json',
]

def negative_records(data,key=None):
    if isinstance(data,dict):
        key=data.get('moduli_key',data.get('key',key))
        if key=='203' and data.get('theta_n_exists') is False:
            assert data['all_minors_or_unit_gcd']
            assert data['coordinate_polynomial_coefficients']==[1]
            yield data['n']
        for value in data.values():
            yield from negative_records(value,key)
    elif isinstance(data,list):
        for value in data:
            yield from negative_records(value,key)

def main():
    packet.P=sp.Poly(packet.X**4+2*packet.X**3+packet.X**2+8*packet.X+16,packet.X)
    packet.M=[[0,0,0,-16],[1,0,0,-8],[0,1,0,-1],[0,0,1,-2]]
    negatives={}
    for name in SOURCES:
        for n in negative_records(json.loads((ROOT/name).read_text())):
            negatives.setdefault(n,[]).append(name)
    rows=[]
    for support in [(3,5),(3,7),(5,7),(3,11),(7,11)]:
        first=[packet.packet(ell) for ell in support]
        m=lcm(*(r['torsion_splitting_exponent_m'] for r in first))
        results=[packet.packet(ell,forced_m=m) for ell in support]
        n=prod(r['theta_order_divides'] for r in results)
        assert n in negatives
        rows.append({
            'prime_support':list(support),
            'common_splitting_exponent':m,
            'all_supported_theta_order_divides':n,
            'packets':results,
            'complete_theta_n_exclusion_sources':negatives[n],
            'entire_supported_theta_packet_empty':True,
        })
    out={'status':'PASS','moduli_keys':['203','302'],
         'actual_F4_Weil_polynomial_ascending':[16,8,1,2,1],
         'records':rows,
         'scope':'All powers with the displayed prime support are excluded. This does not exclude other supports, nonabelian towers, or A1.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    print('PASS',[(r['prime_support'],r['all_supported_theta_order_divides']) for r in rows])

if __name__=='__main__':main()
