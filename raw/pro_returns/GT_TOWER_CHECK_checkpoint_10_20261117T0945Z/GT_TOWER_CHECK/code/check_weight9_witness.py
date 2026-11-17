#!/usr/bin/env python3
"""Independent integral checks of LM7 D.52's literal degree-nine source.

The coefficient list represents 2h.  Every algebra operation is exact.
The symmetric-group algebra calculation is only a representation of the
infinitesimal braid algebra; a nonzero image certifies a pentagon failure.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import permutations
from pathlib import Path
import json

COEFF = {
 "xxxxxxyyy":2, "xxxxxyxyy":-18, "xxxxxyyxy":-24,
 "xxxxxyyyy":-6, "xxxxyxxyy":18, "xxxxyxyxy":-12,
 "xxxxyxyyy":19, "xxxxyyxxy":18, "xxxxyyxyy":48,
 "xxxxyyyxy":49, "xxxxyyyyy":6, "xxxyxxxyy":-2,
 "xxxyxxyxy":32, "xxxyxxyyy":-1, "xxxyxyxxy":20,
 "xxxyxyxyy":17, "xxxyxyyxy":11, "xxxyxyyyy":-13,
 "xxxyyxxyy":-20, "xxxyyxyxy":-12, "xxxyyxyyy":-43,
 "xxxyyyxxy":-20, "xxxyyyxyy":-105, "xxxyyyyxy":-49,
 "xxxyyyyyy":-2, "xxyxxyxyy":-41, "xxyxxyyxy":-72,
 "xxyxxyyyy":-17, "xxyxyxxyy":59, "xxyxyxyxy":-18,
 "xxyxyxyyy":-34, "xxyxyyxyy":-18, "xxyxyyyxy":-68,
 "xxyxyyyyy":12, "xxyyxxyyy":-11, "xxyyxyxyy":-51,
 "xxyyxyyyy":30, "xxyyyxyxy":-10, "xxyyyxyyy":40,
 "xxyyyyxyy":60, "xxyyyyyxy":24, "xyxyxyxyy":6,
}
def clean(d): return {k:v for k,v in d.items() if v}
def add(*ps):
    out=defaultdict(int)
    for p in ps:
        for k,v in p.items(): out[k]+=v
    return clean(out)
def scale(p,c): return clean({k:c*v for k,v in p.items()})
def mul(p,q,operation=lambda a,b:a+b):
    out=defaultdict(int)
    for a,c in p.items():
        for b,d in q.items(): out[operation(a,b)]+=c*d
    return clean(out)
def bracket(p,q,operation=lambda a,b:a+b):
    return add(mul(p,q,operation),scale(mul(q,p,operation),-1))
def is_lyndon(w): return all(w<w[i:]+w[:i] for i in range(1,len(w)))
@lru_cache(None)
def lyndon_word(w):
    if len(w)==1: return {w:1}
    assert is_lyndon(w)
    i=next(i for i in range(1,len(w)) if is_lyndon(w[i:]))
    assert is_lyndon(w[:i])
    return bracket(lyndon_word(w[:i]),lyndon_word(w[i:]))
H=add(*(scale(lyndon_word(w),c) for w,c in COEFF.items()))
X={"x":1};Y={"y":1};Z={"x":-1,"y":-1}
def substitute(p,x,y):
    out={}
    for w,c in p.items():
        q={"":c}
        for a in w: q=mul(q,x if a=="x" else y)
        out=add(out,q)
    return out
H_yx=substitute(H,Y,X)
H_zy=substitute(H,Z,Y)
K=scale(substitute(H,Z,X),-1)
checks={
 "antisymmetry":add(H,H_yx),
 "cabling":add(bracket(X,H),scale(bracket(add(X,Y),H_zy),-1)),
 "special":add(bracket(H,Y),scale(bracket(K,add(X,Y)),-1)),
 "cyclic":add(H,substitute(H,Y,Z),substitute(H,Z,X)),
}
assert all(not p for p in checks.values())
fox=defaultdict(int)
for w,c in H.items():
    if w.endswith("y"):
        u=w[:-1];fox[(u.count("x"),u.count("y"))]+=c
fox=clean(fox)
assert fox=={(6,2):2,(5,3):6,(4,4):6,(3,5):2},fox

S4=list(permutations(range(4)))
identity=tuple(range(4))
def compose(a,b):return tuple(a[b[i]] for i in range(4))
def trans(i,j):
    a=list(identity);a[i-1],a[j-1]=a[j-1],a[i-1]
    return {tuple(a):1}
T={(i,j):trans(i,j) for i in range(1,5) for j in range(i+1,5)}
def tij(i,j):return T[tuple(sorted((i,j)))]
for i,j,k in permutations(range(1,5),3):
    assert not bracket(tij(i,j),add(tij(i,k),tij(j,k)),compose)
for i,j,k,l in permutations(range(1,5)):
    assert not bracket(tij(i,j),tij(k,l),compose)
def evaluate(p,x,y):
    out={}
    for w,c in p.items():
        q={identity:c}
        for a in w:q=mul(q,x if a=="x" else y,compose)
        out=add(out,q)
    return out
P=add(
 evaluate(H,tij(1,2),add(tij(2,3),tij(2,4))),
 evaluate(H,add(tij(1,3),tij(2,3)),tij(3,4)),
 scale(evaluate(H,tij(2,3),tij(3,4)),-1),
 scale(evaluate(H,add(tij(1,2),tij(1,3)),add(tij(2,4),tij(3,4))),-1),
 scale(evaluate(H,tij(1,2),tij(2,3)),-1),
)
record={
 "source":"LM7_PUSH D.52.3, coefficients of 2h",
 "lyndon_coefficients":COEFF,
 "associative_coefficients":H,
 "companion_2k":K,
 "identity_remainders":checks,
 "right_y_fox":[[list(k),v] for k,v in sorted(fox.items())],
 "s4_pentagon_remainder":[[list(k),v] for k,v in sorted(P.items())],
}
target=Path(__file__).with_suffix(".json")
target.write_text(json.dumps(record,indent=2,sort_keys=True)+"\n")
print("Literal nonzero Lyndon coefficients:",len(COEFF))
print("Associative support of 2h:",len(H))
for name in checks:print(name+": PASS, every associative coefficient is zero")
print("Right-y abelian Fox polynomial:",sorted(fox.items()))
print("All infinitesimal braid relations in Z[S4]: PASS")
print("Pentagon remainder in Z[S4]:",sorted(P.items()))
print("This image is", "NONZERO: pentagon failure certified" if P else "ZERO: this representation gives no certificate")
print("Certificate:",target.name)
