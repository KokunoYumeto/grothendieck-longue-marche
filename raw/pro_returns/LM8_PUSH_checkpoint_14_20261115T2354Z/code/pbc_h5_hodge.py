#!/usr/bin/env python3
"""Exact monomial count for the H5 cyclic cover's holomorphic eigenspaces."""
from collections import Counter
from pathlib import Path
import hashlib
import json

rows=[]
for j in range(1,5):
    bound=(24*j+4)//5
    assert bound==5*j
    basis=[]
    for a in range(bound//2+1):
        basis.append({'monomial':['x',a],'pole_order':2*a,'tau_exponent_mod4':(2*a+1)%4})
    for b in range((bound-3)//2+1):
        basis.append({'monomial':['y*x',b],'pole_order':3+2*b,'tau_exponent_mod4':(2*b+2)%4})
    counts=Counter(m['tau_exponent_mod4'] for m in basis)
    assert len(basis)==5*j
    tau=[counts[k] for k in (0,2,1,3)]
    residual=[tau[1]-j,tau[2]-j,tau[3]-j]
    assert sum(residual)==j and residual[0] in (0,1)
    assert all(0<=t<=2 for t in residual[1:])
    rows.append({'j':j,'central_character':'zeta5^(-j)','pole_bound':bound,
                 'dimension':len(basis),'tau_counts_order_1_minus1_i_minusi':tau,
                 'residual_counts_under_trace_one_Fourier_convention':residual,'basis':basis})
assert sum(r['dimension'] for r in rows)+1==51
assert sum(r['tau_counts_order_1_minus1_i_minusi'][0] for r in rows)==10
assert sum(sum(r['tau_counts_order_1_minus1_i_minusi'][:2]) for r in rows)==22
for j in range(4):
    a=rows[j]['residual_counts_under_trace_one_Fourier_convention']
    b=rows[3-j]['residual_counts_under_trace_one_Fourier_convention']
    assert a[0]+b[0]==1 and a[1]+b[2]==2 and a[2]+b[1]==2
result={'curve':'E:y^2=x^3-x, z^5=psi5(x)',
        'branch_divisor_orders':[1]*24+[-24],
        'genus':51,'tau_quotient_genus':10,'tau_square_quotient_genus':22,
        'rows':rows,
        'B8_balanced_at_every_K_embedding':False,
        'unconditional_obstruction':'B10 F-Hodge totals 1,2,3,4 cannot be a CM rank-one F factor plus a rank-two K factor balanced at every embedding.',
        'scope':'Intrinsic central and tau differential counts are exact. Residual T labels assume the stated trace-one Fourier projector; the imbalance obstruction does not require that convention.',
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
for row in rows:
    print(row['j'],row['dimension'],row['tau_counts_order_1_minus1_i_minusi'],row['residual_counts_under_trace_one_Fourier_convention'])
