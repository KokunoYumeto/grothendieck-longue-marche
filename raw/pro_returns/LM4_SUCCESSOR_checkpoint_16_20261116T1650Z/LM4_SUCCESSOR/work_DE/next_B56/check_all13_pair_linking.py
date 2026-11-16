"""Exact labelled pair-linking check for the thirteen certified braids.

Finite labels are (4,6,1,3,9,12).  The normalized points with labels
4 and 6 are constant 0 and 1.  This script obtains their initial
positions from the exact rational coordinates, and checks that
forgetting the other four strands kills every braid image in PB2.
"""
from pathlib import Path
import itertools,json
import sympy as s
from membership_rigid7 import BRAIDS

HERE=Path(__file__).resolve().parent
certificate=json.loads((HERE/'all13_exact_certificate.json').read_text())
u=s.Symbol('u'); I=s.I
base=s.Rational(371,100)+I*s.Rational(237,100)
rotation=1+I*s.Rational(317,1000)
values=[s.cancel(s.sympify(f,locals={'u':u}).subs(u,base)*rotation)
        for f in certificate['finite_functions']]
initial=tuple(sorted(range(6),key=lambda j:s.re(values[j])))
assert len({s.re(v) for v in values})==6
labels=certificate['labels'][1:]
assert labels==[4,6,1,3,9,12]
assert s.simplify(values[0])==0 and s.simplify(values[1]-rotation)==0
pairs=list(itertools.combinations(range(6),2))

def linking(word):
    order=list(initial);twice={pair:0 for pair in pairs}
    for a in word:
        j=abs(a)-1
        pair=tuple(sorted(order[j:j+2]))
        twice[pair]+=1 if a>0 else -1
        order[j],order[j+1]=order[j+1],order[j]
    assert tuple(order)==initial
    assert all(v%2==0 for v in twice.values())
    return {pair:v//2 for pair,v in twice.items()}

full=linking((1,2,3,4,5)*6)
assert set(full.values())=={1}
rows=[]
print('Exact real-projection order of named finite strands:',[labels[j] for j in initial])
print('Full twist has pair linking1 on each of15 labelled pairs: PASS')
for j,word in sorted(BRAIDS.items()):
    row=linking(word)
    assert row[0,1]==0
    assert sum(row.values())*2==sum(1 if a>0 else -1 for a in word)
    rows.append([row[pair] for pair in pairs])
    print('basis',j,'linking of fixed labels4,6:',row[0,1])
print('All13 normalized braid images have zero fixed-pair linking: PASS')
print('Therefore the image meets the full-twist subgroup trivially, discretely and in completion.')
(HERE/'all13_pair_linking.json').write_text(json.dumps({
    'initial_label_order':[labels[j] for j in initial],
    'pair_columns':[[labels[i],labels[j]] for i,j in pairs],
    'matrix_rows_basis1_to13':rows,
    'fixed_pair':[4,6],
    'full_twist_linking':1
},indent=2)+'\n')
