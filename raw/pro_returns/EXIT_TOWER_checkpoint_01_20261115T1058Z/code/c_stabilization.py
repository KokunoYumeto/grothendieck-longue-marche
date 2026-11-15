#!/usr/bin/env python3
"""Independent bit-mask enumeration of genus-zero stabilization/lift data.

This implementation does not import the supplied RESIDUE program. Splits
are normalized by requiring their first leg to lie outside the recorded
part. Compatibility is tested as laminarity of the rooted subsets.
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import csv,json

OUT=Path(__file__).resolve().parent

def splits(n):
    allbits=(1<<n)-1
    return [m for m in range(allbits+1) if m&1==0 and 2<=m.bit_count()<=n-2]

def compatible(a,b):
    return not(a&b) or a&b==a or a&b==b

def systems(n):
    ss=splits(n);found=[()]
    def extend(prefix,start):
        for j in range(start,len(ss)):
            m=ss[j]
            if all(compatible(m,p) for p in prefix):
                new=prefix+(m,);found.append(new);extend(new,j+1)
    extend((),0)
    assert max(map(len,found),default=0)<=n-3
    return sorted(found,key=lambda x:(len(x),x))

def image(m,n):
    new=m&((1<<(n-1))-1)
    return new if 2<=new.bit_count()<=n-3 else None

def subsets(seq):
    for b in range(1<<len(seq)):
        yield tuple(seq[i] for i in range(len(seq)) if b>>i&1)

def labels(mask):
    return [i+1 for i in range(mask.bit_length()) if mask>>i&1]

def compute(n):
    counts=Counter();rows=[];special=[]
    for sig in systems(n):
        imgs=tuple(image(x,n) for x in sig)
        tau=sorted(set(imgs)-{None})
        for eta in subsets(tau):
            obj=[s for s in subsets(tuple(range(len(sig))))
                 if set(imgs[i] for i in s)-{None}==set(eta)]
            h_rank=len(sig)-len(set(tau)-set(eta))
            initial=[s for s in obj if h_rank==len(s) and all(set(s)>=set(t) for t in obj)]
            # Every relation is a sum over a disjoint block of columns.
            # Its coefficient vector is primitive, so all quotients are free.
            if initial:
                kind='contractible'
            else:
                assert len(obj)==1 and h_rank-len(obj[0])==1
                kind='BZ'
            mult=Counter(x for x in imgs if x is not None)
            predicted=any(k==2 and im not in eta for im,k in mult.items())
            assert (kind=='BZ')==predicted
            hom=[(s,t,h_rank-len(s)) for s in obj for t in obj if set(s)>=set(t)]
            row={'upstairs_n':n,'sigma':list(sig),'images':imgs,'eta':eta,
                 'H_rank':h_rank,'objects':obj,'hom_free_ranks':hom,'type':kind,
                 'initial_objects':initial}
            rows.append(row);counts[kind]+=1
            if kind=='BZ':special.append({'sigma':[labels(x) for x in sig],
                  'eta':[labels(x) for x in eta]})
    (OUT/f'c_lifts_{n}_to_{n-1}.json').write_text(json.dumps(rows,indent=2)+'\n')
    print(json.dumps({'upstairs_n':n,'strata':len(systems(n)),
          'by_codimension':dict(sorted(Counter(map(len,systems(n))).items())),
          'normalized_cases':len(rows),'types':dict(counts)}))
    if n==5:print(json.dumps({'three_bridge_cases':special}))
    return counts

def filling_pair_certificate():
    # a12=x1*x2; a13=x1*x2*x3*x2^-1;
    # a14=(x2*x3)^-1 after x1*x2*x3*x4=1.
    import sympy as s
    A=s.Matrix([[1,1,0],[1,0,-1],[0,1,-1]])
    assert abs(A.det())==2
    # Exact quotient simplification: a12=1 -> x2=x1^-1;
    # a14=1 -> x3=x1; a13 then equals x1^2.
    # Check every relator in the explicit nontrivial C2 quotient.
    rel_exponents=[[1,1,0],[1,0,1],[0,-1,-1]]
    assert all(sum(e)%2==0 for e in rel_exponents)
    certificate={'pair_loop_columns':list(map(list,zip(*rel_exponents))),
                 'determinant':int(A.det()),'abelian_index':2,
                 'normal_quotient':'C2',
                 'elimination':['x2=x1^-1','x3=x1','x1^2=1'],
                 'nontrivial_quotient_map':'each puncture meridian -> 1 in Z/2'}
    (OUT/'c_pair_loops.json').write_text(json.dumps(certificate,indent=2)+'\n')
    print(json.dumps(certificate))

if __name__=='__main__':
    assert compute(5)==Counter(contractible=44,BZ=3)
    assert compute(6)==Counter(contractible=696,BZ=70)
    filling_pair_certificate()
