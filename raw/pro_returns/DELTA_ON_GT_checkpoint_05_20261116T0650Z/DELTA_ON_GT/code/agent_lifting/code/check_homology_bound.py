#!/usr/bin/env python3
"""Exact arithmetic for the proved full-multiplier homology bound LH.1."""
import json
from pathlib import Path

def valuation(n,p):
    assert n
    out=0
    while n%p==0:out+=1;n//=p
    return out

def main():
    d=97
    # Directly value the exact finite GL order, without logarithms or
    # constructing its enormous decimal expansion.
    direct={ell:sum((e-1)*d*d*(p==ell)
                    +sum(valuation(p**d-p**i,ell)for i in range(d))
                    for p,e in ((2,6),(3,2))) for ell in (2,3)}
    cross2=sum(valuation(3**i-1,2)for i in range(1,d+1))
    cross3=sum(valuation(2**i-1,3)for i in range(1,d+1))
    # Independent LTE forms for the two cross-characteristic sums.
    lte2=sum(1 if i%2 else 2+valuation(i,2)for i in range(1,d+1))
    lte3=sum(1+valuation(i//2,3)for i in range(2,d+1,2))
    assert (cross2,cross3)==(239,70)==(lte2,lte3)
    expected={2:5*d*d+d*(d-1)//2+cross2,
              3:d*d+d*(d-1)//2+cross3}
    assert direct==expected=={2:51940,3:14135}
    nexp={2:direct[2]+2,3:direct[3]+1}
    assert nexp=={2:51942,3:14136}
    assert nexp[2]>=6 and nexp[3]>=2
    quotient={2:6+d*nexp[2],3:2+d*nexp[3]}
    assert quotient=={2:5038380,3:1371194}
    data=dict(rank=d,base_modulus=576,base_modulus_prime_exponents={2:6,3:2},
              gl_order_valuations=direct,cross_sums={2:cross2,3:cross3},
              full_modulus_prime_exponents=nexp,
              modular_quotient_order_prime_exponents=quotient,
              scope='arithmetic check; full-character factorization proved in LH.1')
    (Path(__file__).resolve().parents[1]/'records'/'homology_bound.json').write_text(
        json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
    print('PASS: exact GL valuations, LTE checks, full modulus and quotient order.')

if __name__=='__main__':main()
