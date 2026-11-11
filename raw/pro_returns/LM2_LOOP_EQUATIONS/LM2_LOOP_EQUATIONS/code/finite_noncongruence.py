"""Construct and certify SL2(F8), its simplicity, and a (2,3)-generating pair."""
from itertools import product
from pathlib import Path
import json
from finite_groups import Group

def fmul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1
        if a&8:a^=11 # X^3+X+1
        b>>=1
    return r

def matmul(a,b):
    return (fmul(a[0],b[0])^fmul(a[1],b[2]),fmul(a[0],b[1])^fmul(a[1],b[3]),
            fmul(a[2],b[0])^fmul(a[3],b[2]),fmul(a[2],b[1])^fmul(a[3],b[3]))

def main():
    es=[a for a in product(range(8),repeat=4) if fmul(a[0],a[3])^fmul(a[1],a[2])==1]
    G=Group(es,matmul,(1,0,0,1),'SL2(F8)')
    assert G.n==504
    A=G.index[(1,1,0,1)]
    pair=None
    for alpha in range(2,8):
        ai=next(b for b in range(1,8) if fmul(alpha,b)==1)
        B=G.index[(0,alpha,ai,1)]
        if G.orders[B]==3 and len(G.generated([A,B]))==G.n:
            pair=(A,B);break
    assert pair
    classes=[]
    for c in sorted(set(G.classes)):
        orb={p[c] for p in G.conj}
        normal_order=len(G.generated(orb))
        if c!=G.e:assert normal_order==G.n
        classes.append(dict(representative=G.elements[c],class_size=len(orb),
                            element_order=G.orders[c],normal_closure_order=normal_order))
    result=dict(field='F2[a]/(a^3+a+1), binary coefficient encoding',
                order=G.n,A=G.elements[pair[0]],B=G.elements[pair[1]],
                order_A=G.orders[pair[0]],order_B=G.orders[pair[1]],
                generated_order=len(G.generated(pair)),conjugacy_classes=classes,
                simple=True)
    out=Path(__file__).resolve().parent
    (out/'finite_noncongruence.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
