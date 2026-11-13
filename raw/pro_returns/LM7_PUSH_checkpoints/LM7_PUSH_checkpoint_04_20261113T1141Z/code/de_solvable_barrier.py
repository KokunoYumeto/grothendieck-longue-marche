#!/usr/bin/env python3
"""Literal class-three exponent-five witness for the E.16 comparison."""
from pathlib import Path
import json
import numpy as np

p=5;I=np.eye(4,dtype=np.int64)
def mul(a,b):return a@b%p
def power(a,j):
    out=I.copy()
    for _ in range(j):out=mul(out,a)
    return out
def inv(a):return power(a,4)
def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
a=I.copy();a[0,1]=a[2,3]=1
b=I.copy();b[1,2]=1
w=comm(comm(a,b),a)
expected=I.copy();expected[0,3]=2
assert np.array_equal(w,expected)
assert np.array_equal(power(a,5),I) and np.array_equal(power(b,5),I)
assert not np.array_equal(w,I)
assert np.array_equal(comm(w,a),I) and np.array_equal(comm(w,b),I)
out={'prime':p,'n0_image':a.tolist(),'n1_image':b.tolist(),
     'word':'[[n0,n1],n0]','commutator_convention':'[a,b]=a*b*a^-1*b^-1',
     'word_image':w.tolist(),'word_image_nontrivial':True,
     'target':'UT4(F5), of class3 and exponent5',
     'scope':'The literal word lies in gamma3(N) but not in gamma4(N) N^5. This proves the solvable class-three comparison obstruction used in E.16.'}
here=Path(__file__).resolve().parent
(here/'de_solvable_barrier.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
