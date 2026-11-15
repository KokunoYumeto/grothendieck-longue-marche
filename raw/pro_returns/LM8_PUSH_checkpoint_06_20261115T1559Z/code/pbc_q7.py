"""Independent integral certificate for LM8 B.12.

Sparse associative polynomials over Z, standard Lyndon brackets, and
infinitesimal pure braid derivations. No input program is imported.
"""
from collections import defaultdict
from functools import lru_cache
import json
from pathlib import Path

def add(*ps):
    z=defaultdict(int)
    for p in ps:
        for w,c in p.items(): z[w]+=c
    return {w:c for w,c in z.items() if c}
def neg(p): return {w:-c for w,c in p.items()}
def scale(p,n): return {w:c*n for w,c in p.items() if c*n}
def mul(p,q):
    z=defaultdict(int)
    for a,c in p.items():
        for b,d in q.items():z[a+b]+=c*d
    return {w:c for w,c in z.items() if c}
def br(p,q):return add(mul(p,q),neg(mul(q,p)))
def letter(c):return {c:1}
def lyndon(w):return all(w<w[i:] for i in range(1,len(w)))
@lru_cache(None)
def standard(w):
    if len(w)==1:return letter(w)
    assert lyndon(w)
    for i in range(1,len(w)):
        if lyndon(w[i:]):return br(standard(w[:i]),standard(w[i:]))
def subst(p,values):
    z={}
    for w,c in p.items():
        t={'':c}
        for s in w:t=mul(t,values[s])
        z=add(z,t)
    return z
q_spec=[('xxxyxyy',3),('xxxyyxy',3),('xxyxyxy',1),
        ('xxyxyyy',-3),('xxyyxyy',-3),('xxyyyxy',-3),('xyxyxyy',-1)]
q=add(*(scale(standard(w),n) for w,n in q_spec))
x,y=letter('x'),letter('y')
anti=add(q,subst(q,{'x':y,'y':x}))
J=add(br(x,q),neg(br(add(x,y),subst(q,{'x':neg(add(x,y)),'y':y}))))
cycle=add(q,subst(q,{'x':y,'y':neg(add(x,y))}),
          subst(q,{'x':neg(add(x,y)),'y':x}))
assert not anti and not J and not cycle

abc='abc'
zero=({}, {}, {})
def dadd(*ds):return tuple(add(*(d[i] for d in ds)) for i in range(3))
def dneg(d):return tuple(neg(p) for p in d)
def dscale(d,n):return tuple(scale(p,n) for p in d)
def apply(d,p):
    z=defaultdict(int)
    for w,c in p.items():
        for i,s in enumerate(w):
            for v,e in d[abc.index(s)].items():z[w[:i]+v+w[i+1:]]+=c*e
    return {w:c for w,c in z.items() if c}
def dbr(d,e):return tuple(add(apply(d,p),neg(apply(e,q))) for p,q in zip(e,d))
def inner(s):return tuple(br(letter(s),letter(t)) for t in abc)
def edge(i,j):
    d=[{}, {}, {}]
    d[i]=br(letter(abc[i]),letter(abc[j]))
    d[j]=neg(d[i])
    return tuple(d)
t={(1,2):edge(0,1),(1,3):edge(0,2),(2,3):edge(1,2),
   (1,4):inner('a'),(2,4):inner('b'),(3,4):inner('c')}
def get(i,j):return t[tuple(sorted((i,j)))]
braid_checks=0
from itertools import combinations,permutations
for i,j,k in permutations(range(1,5),3):
    assert not any(dbr(get(i,j),dadd(get(i,k),get(j,k))))
    braid_checks+=1
for i,j,k,l in permutations(range(1,5),4):
    assert not any(dbr(get(i,j),get(k,l)))
    braid_checks+=1
def dq(d,e):
    @lru_cache(None)
    def rec(w):
        if len(w)==1:return d if w=='x' else e
        for i in range(1,len(w)):
            if lyndon(w[i:]):return dbr(rec(w[:i]),rec(w[i:]))
    return dadd(*(dscale(rec(w),n) for w,n in q_spec))
defect=dadd(dq(get(1,2),get(2,3)),
            dq(dadd(get(1,2),get(1,3)),dadd(get(2,4),get(3,4))),
            dq(get(2,3),get(3,4)),
            dneg(dq(get(1,2),dadd(get(2,3),get(2,4)))),
            dneg(dq(dadd(get(1,3),get(2,3)),get(3,4))))
print('raw coefficient',defect[0].get('aaaaabcb'),flush=True)
assert defect[0].get('aaaaabcb') in (16,-16)
out={'standard_lyndon_terms':q_spec,'q_associative_terms':len(q),
     'antisymmetry':not anti,'special_J':not J,'cycle':not cycle,
     'infinitesimal_braid_checks':braid_checks,
     'pentagon_nonzero_terms_by_generator':[len(p) for p in defect],
     'pentagon_coefficient_a_on_aaaaabcb':defect[0]['aaaaabcb'],
     'full_defect':dict(zip(abc,[dict(sorted(p.items())) for p in defect]))}
path=Path(__file__).with_suffix('.json')
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='full_defect'},indent=2))
