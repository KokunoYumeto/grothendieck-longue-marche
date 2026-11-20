#!/usr/bin/env python3
"""Exhaustive finite check of the A5 simplicity and noncommutativity claim."""
from itertools import permutations
from pathlib import Path
from datetime import datetime,timezone
import json

def compose(p,q):
    return tuple(p[q[i]] for i in range(5))
def inverse(p):
    return tuple(p.index(i) for i in range(5))
def even(p):
    return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2==0
def cycles(p):
    out=[];seen=set()
    for i in range(5):
        if i in seen:continue
        cyc=[];j=i
        while j not in seen:
            seen.add(j);cyc.append(j+1);j=p[j]
        if len(cyc)>1:out.append('('+' '.join(map(str,cyc))+')')
    return ''.join(out) or 'id'
G=set(filter(even,permutations(range(5))))
identity=tuple(range(5))
assert len(G)==60
assert all(compose(p,q) in G for p in G for q in G)
assert all(inverse(p) in G for p in G)
remaining=set(G);classes=[]
while remaining:
    g=min(remaining)
    conj={compose(compose(h,g),inverse(h)) for h in G}
    assert conj<=remaining
    remaining-=conj
    closure={identity}|conj
    while True:
        enlarged=closure|{compose(x,y) for x in closure for y in closure}
        if enlarged==closure:break
        closure=enlarged
    assert closure<=G
    classes.append({'representative':list(x+1 for x in g),'cycles':cycles(g),'class_size':len(conj),'normal_closure_size':len(closure)})
assert sorted(c['class_size'] for c in classes)==[1,12,12,15,20]
assert all(c['normal_closure_size']==(1 if c['cycles']=='id' else 60) for c in classes)
p=(1,2,0,3,4);q=(0,1,3,4,2)
assert p in G and q in G and compose(p,q)!=compose(q,p)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'method':'Enumerate even permutations of five symbols; compose p after q. Compute every conjugacy class and close each class with identity under all products until stable.','group_size':len(G),'classes':classes,'noncommuting_pair':{'p':cycles(p),'q':cycles(q),'p_after_q':cycles(compose(p,q)),'q_after_p':cycles(compose(q,p))},'scope':'A5 is nonabelian and each nonidentity element normally generates all A5. The minimal-order claim is not checked by this enumeration.'}
target=Path(__file__).resolve().parents[1]/'decisions/scan031_A5_check.json'
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
