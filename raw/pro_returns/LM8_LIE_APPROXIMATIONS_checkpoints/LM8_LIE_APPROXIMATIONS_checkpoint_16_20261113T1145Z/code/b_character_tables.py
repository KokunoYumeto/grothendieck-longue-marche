#!/usr/bin/env python3
"""Exact Witt characters and symmetric-group invariants, not modular estimates."""
from pathlib import Path
from collections import Counter
from math import factorial
import json,csv
import sympy as S
from b_lie_core import s3_table
from b_tripod14 import d_odd

def partitions(n,minimum=1):
    if n==0:yield []
    for k in range(minimum,n+1):
        for rest in partitions(n-k,k):yield [k]+rest
def freechar(n,cycle):
    return sum(int(S.mobius(d))*(sum(k for k in cycle if d%k==0)-1)**(n//d)
               for d in S.divisors(n))//n
def sphere(q,N):
    rows=[]
    for n in range(1,N+1):
        tr=[];total=0
        for cycle in partitions(q):
            counts=Counter(cycle);z=1
            for k,m in counts.items():z*=k**m*factorial(m)
            size=factorial(q)//z;v=cycle.count(1)-1
            c=v*freechar(n,cycle)-freechar(n+1,cycle)
            if n==1:c-=cycle.count(1)
            tr.append({'cycle_type':cycle,'class_size':size,'trace':c});total+=size*c
        assert total%factorial(q)==0
        rows.append({'degree':n,'special_outer':next(v['trace'] for v in tr if v['cycle_type']==[1]*q),
                     'invariants':total//factorial(q),'characters':tr})
    return rows
def main():
    out={'tripod':sphere(3,14),'sphere4':sphere(4,6),'odd_generator_free_Lie':d_odd(14)[1:]}
    for a,b in zip(out['tripod'],s3_table(14)):
        assert a['special_outer']==b['dimension'] and a['invariants']==b['trivial']
    p=Path(__file__).parent
    (p/'b_character_tables.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
    rows=list(csv.DictReader((p/'b_tripod_dimensions.csv').open()))
    tex=[r'\begin{center}\begin{tabular}{r|rrrr}',r'\toprule Degree&All special outer&Raw cycles&Special invariants&Odd free Lie\\\midrule']
    for row in rows:
        tex.append(' & '.join(row[k] for k in ['weight','outer_special','two_three_only','S3_invariant_outer_special','odd_free_d'])+r'\\')
    tex +=[r'\bottomrule\end{tabular}\end{center}']
    (p.parent/'sections/B_tripod_table.tex').write_text('\n'.join(tex))
if __name__=='__main__':main()
