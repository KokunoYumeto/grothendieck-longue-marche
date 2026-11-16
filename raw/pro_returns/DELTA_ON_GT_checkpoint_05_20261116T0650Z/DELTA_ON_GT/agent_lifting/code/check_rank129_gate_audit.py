"""Independent direct-word check of the rank129 nonnilpotence witness.
No matrix inverse routine or group-order search from the original test is used.
Written by GPT-6 Astra, OpenAI, 16 November 2026.
"""
from pathlib import Path
import hashlib,json
import numpy as np

root=Path(__file__).resolve().parents[2]
source=root/'agent_five'/'ferrari_rank129.npz'
data=np.load(source);X=data['X'].astype(np.int64);I=np.eye(129,dtype=np.int64)
def mul(a,b):return a@b%3
def power(a,n):
    out=I
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a);n//=2
    return out
x,y=X[0],X[1]
assert np.array_equal(power(x,6),I)and np.array_equal(power(y,6),I)
letters={1:x,2:y,-1:power(x,5),-2:power(y,5)}
def wi(w):return tuple(-x for x in w[::-1])
def wc(u,v):return u+v+wi(u)+wi(v)
def evaluate(w):
    out=I
    for z in w:out=mul(out,letters[z])
    return out
comm=wc((1,),(2,));conjugate=(1,)+comm+(-1,)
w=wc(comm,conjugate);W=evaluate(w)
assert np.array_equal(power(W,12),I)
assert not np.array_equal(power(W,6),I)
assert not np.array_equal(power(W,4),I)
a=power(W,6);u=(1,-2)
b=evaluate(u+w*6+wi(u))
assert np.array_equal(power(a,2),I)and np.array_equal(power(b,2),I)
assert not np.array_equal(a,I)and not np.array_equal(b,I)
ab=mul(a,b)
assert np.array_equal(power(ab,6),I)
assert not np.array_equal(power(ab,3),I)and not np.array_equal(power(ab,2),I)
out={'source_npz_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
     'independent_method':'int64 direct evaluation of free words, generator inverses by sixth powers',
     'second_derived_word_letters':w,'second_derived_word_order':12,
     'involution_exponent':6,'conjugator_letters':u,'involution_product_order':6,
     'conclusion':'The actual harmonic pair second derived group is not nilpotent.',
     'scope':'No Delta identity, finite GT lift, or nonexistence of another actual R2 seed is inferred.'}
dest=Path(__file__).resolve().parents[1]/'records'/'rank129_gate_audit.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
