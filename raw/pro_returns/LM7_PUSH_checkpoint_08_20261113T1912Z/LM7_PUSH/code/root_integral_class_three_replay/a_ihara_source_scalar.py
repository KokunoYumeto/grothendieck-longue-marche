#!/usr/bin/env python3
"""Impose the exact source coefficient f2=(7^2-1)/24=2 modulo9.

The actual map F->Heisenberg(Z/9) kills D8(F), so this scalar is
well-defined on the complete source degree<=7 quotient.  In particular,
the true-kernel correction [x,y]^3 changes it by3 and is retained.
"""
from pathlib import Path
import importlib.util,contextlib,io,json
import numpy as np
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('gauge',HERE/'a_ihara_gauge.py')
g=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(g)

def coeff(word):
    a=b=c=0
    for z in word:
        if z==1:c-=b;a+=1
        elif z==-1:c+=b;a-=1
        elif z==2:b+=1
        elif z==-2:b-=1
        else:raise AssertionError(z)
    assert (a,b)==(0,0)
    return c
assert coeff([1,2,-1,-2])==1

source=json.loads((HERE/'a_ihara_pentagon_inputs.json').read_text())
pent=json.loads((HERE/'de_fermat_pentagon_arithmetic_fast.json').read_text())
values=[coeff(r['literal_word']) for r in source['candidate_records']]
kernel=[coeff(w) for w in pent['true_kernel_literal_words']]
assert kernel==[3,0,0,0,0]
print('Exact degree2 coefficients of five source kernel words:',kernel)
out=[]
for r in pent['branch_results']:
    ids=r['input_record_indices'];v0=values[ids[0]]
    assert (v0-2)%3==0
    differences=[values[i]-v0 for i in ids[1:]]+kernel
    assert all(a%3==0 for a in differences)
    row=np.array([a//3 for a in differences],dtype=np.int64)%3
    rhs=((2-v0)//3)%3
    part=np.array(r['particular_parameters'],dtype=np.int64)
    hom=np.array(r['homogeneous_parameters'],dtype=np.int64)
    rr=row@hom%3;bb=(rhs-row@part)%3
    nonzero=np.flatnonzero(rr)
    assert len(nonzero) or bb==0
    lam=np.zeros(hom.shape[1],dtype=np.int64)
    if len(nonzero):lam[nonzero[0]]=bb*int(rr[nonzero[0]])%3
    newpart=(part+hom@lam)%3
    newhom=hom@g.kernel(rr[None,:])%3
    assert row@newpart%3==rhs and not np.any(row@newhom%3)
    result=dict(r)
    result['particular_parameters']=newpart.tolist()
    result['homogeneous_parameters']=newhom.tolist()
    result['source_f2_base_mod9']=v0%9
    result['source_f2_divided_row']=row.tolist()
    result['source_f2_divided_rhs']=int(rhs)
    result['source_f2_target_mod9']=2
    result.pop('candidate_coordinate_solution',None)
    result.pop('candidate_coordinate_kernel',None)
    out.append(result)
    print('Branch',r['branch'],'canonical f2 mod9',v0%9,
          'added source scalar rank',int(bool(len(nonzero))),
          'homogeneous parameter dimension',newhom.shape[1])
pent['branch_results']=out
pent['source_scalar_condition']='Integral hexagon gives f2=(chi^2-1)/24; atchi7 it equals2. Exact combined source word imposed modulo9.'
(HERE/'a_ihara_pentagon_scalar.json').write_text(json.dumps(pent,separators=(',',':'))+'\n')
print('PASS: source coordinate imposed after, and including, every true-kernel correction.')
