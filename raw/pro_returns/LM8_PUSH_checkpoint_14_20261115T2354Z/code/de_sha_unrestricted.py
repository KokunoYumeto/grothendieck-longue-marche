#!/usr/bin/env python3
"""Exact CRT/valuation support for the D.80 rational-point examples."""
from pathlib import Path
import json

def valuation(n,p):
    assert n
    e=0
    while n%p==0:
        n//=p
        e+=1
    return e

rows=[]
for d in range(1,31):
    N=5**(d+1)
    modulus=5*N
    k=((23-N)*pow(modulus,-1,36))%36
    t=N-1+modulus*k
    assert t%36==22 and (t-(N-1))%modulus==0
    assert [valuation(t,2),valuation(1-t,3),
            valuation(1-t,2),valuation(t,3)]==[1,1,0,0]
    assert t%5!=0 and (1-t)%5!=0
    assert valuation(t**4-1,5)==d+1
    assert (1-t)%25==2
    rows.append({'d':d,'k_d':k,'t_d':str(t),
                 'v5_t_fourth_minus_one':d+1,
                 'global_inertia_determinant':1,
                 'local_beta_mod5':2})

result={
    'status':'PASS',
    'scope':'Exact CRT and rational-point valuation certificate; infinite-ramification duality and uniform coefficient-level arguments are proved in the written D.80 proof.',
    'ranks_checked':list(range(1,31)),
    'rows':rows,
}

if __name__=='__main__':
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
