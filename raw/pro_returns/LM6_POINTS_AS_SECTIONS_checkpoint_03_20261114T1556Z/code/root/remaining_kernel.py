#!/usr/bin/env python3
"""Exact integral certificate for the E.30 ambient-metabelian kernel."""
from pathlib import Path
import json

n=10
basis=[(i,j,k) for j in range(n) for i in range(j+1,n) for k in range(j,n)]
kernel={v for v in basis if v[2]>=2}
quotient=set(basis)-kernel
assert len(basis)==330 and len(kernel)==304 and len(quotient)==26

def hall(i,j,k):
    if i==j:return {}
    if i<j:return {a:-b for a,b in hall(j,i,k).items()}
    if k>=j:return {(i,j,k):1}
    return {(i,k,j):1,(j,k,i):-1}

generators=[]
for w in range(2,n):
    for i in range(n):
        for j in range(i):
            v={a:-b for a,b in hall(i,j,w).items()}
            assert set(v)<=kernel
            generators.append({'w':w,'i':i,'j':j,'hall':[[list(a),b] for a,b in v.items()]})
assert len(generators)==360
witnesses=[]
for i,j,k in sorted(kernel):
    assert hall(i,j,k)=={(i,j,k):1}
    witnesses.append({'basis':[i,j,k],'negative_generator':[k,i,j]})
assert len(witnesses)==304
assert quotient=={(1,0,0),(1,0,1)}|{
    v for w in range(2,n) for v in [(w,0,0),(w,0,1),(w,1,1)]}

out={'rank_A':330,'rank_kernel':304,'rank_quotient':26,
     'all_generators':generators,'unit_basis_witnesses':witnesses,
     'quotient_basis':[list(v) for v in sorted(quotient)],
     'integral_saturation':'Kernel is exactly a subset of the integral Hall basis.',
     'arithmetic_cocycle_evaluated':False,'checks_passed':True}
Path(__file__).with_name('remaining_kernel_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['all_generators','unit_basis_witnesses']},indent=2))
