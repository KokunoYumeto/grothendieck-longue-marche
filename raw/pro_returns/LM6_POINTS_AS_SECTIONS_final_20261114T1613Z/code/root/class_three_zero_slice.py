#!/usr/bin/env python3
"""The actual coefficient group for the zero-abelian-slice action class.

Reuse the constructed, verified integral matrices, not supplied matrices.
The vector representing the arithmetic action itself is not asserted known.
"""
from pathlib import Path
from collections import Counter
from contextlib import redirect_stdout
import io,json,runpy
import numpy as np
buf=io.StringIO()
with redirect_stdout(buf):
    data=runpy.run_path(str(Path(__file__).with_name('class_three_fibre.py')))
T,J=data['T'],data['J'];I=np.eye(330,dtype=object)
M=(T-7*I)@(I-J)
precision=10;mod=3**precision
M=[[int(x)%mod for x in row] for row in M]
def val(x):
    if not x:return precision
    v=0
    while x%3==0:x//=3;v+=1
    return v
values=[]
for k in range(330):
    best=(precision,None,None)
    for i in range(k,330):
        for j in range(k,330):
            v=val(M[i][j])
            if v<best[0]:best=(v,i,j)
            if v==0:break
        if best[0]==0:break
    v,i,j=best
    if i is None:break
    M[k],M[i]=M[i],M[k]
    for row in M:row[k],row[j]=row[j],row[k]
    pp=3**v;inverse=pow(M[k][k]//pp,-1,mod//pp)
    for i in range(k+1,330):
        assert M[i][k]%pp==0
        c=(M[i][k]//pp*inverse)%(mod//pp)
        if c:M[i]=[(x-c*y)%mod for x,y in zip(M[i],M[k])]
    values.append(v)
assert len(values)==166
counts=dict(sorted(Counter(values).items()))
out={'dimension':330,'coefficient_module':'Lie_3(V)(-1)',
     'relation_matrix':'(T-7I)(I-J)', 'relation_rank':166,
     'free_rank':164,'Smith_3_valuations':counts,'precision':precision,
     'exact_rank_upper_bound':'rank(I-J)=(330+2)/2=166',
     'action_class_vector_evaluated':False,
     'upstream_matrix_certificate':json.loads(buf.getvalue()),
     'checks_passed':True}
Path(__file__).with_name('class_three_zero_slice_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='upstream_matrix_certificate'},indent=2))
