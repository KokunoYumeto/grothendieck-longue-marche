#!/usr/bin/env python3
"""Literal common-marked source formulas printed in B112."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=ROOT/'work_CE/next_symmetric_nodes/annular_source_detector_independent23.json'
D=json.loads(p.read_text())
def red(w):
    out=[]
    for x in w:
        x=3 if abs(x)==3 else x
        if out and (out[-1]==-x or out[-1]==x==3):out.pop()
        else:out.append(x)
    return tuple(out)
def mul(*ww):return red(x for w in ww for x in w)
def inv(w):return red(-x for x in reversed(w))
def bar(w):return mul((3,),w,(3,))
def comm(x,y):return mul(x,y,inv(x),inv(y))
def conj(g,x):return mul(g,x,inv(g))
a=(1,);b=(2,);c=(3,);f=(4,);d=(5,);e=(6,)
delta=lambda x:mul(x,bar(x))
E=conj(mul(f,d),e)
T=mul(c,b,c,b,c,E,c,inv(b),c,inv(b))
expected=[mul(bar(b),b),mul(T,T),
          mul(conj(mul(c,b),comm(d,bar(d))),delta(d)),
          mul(conj(mul(c,b),comm(a,bar(a))),delta(a))]
for row,w in zip(D['source_reconstructed_from_original_positive_push'],expected):
    assert red(row['Y_word'])==w,row['name']
    print('PASS literal source formula',row['name'],len(w),'letters')
out={'status':'PASS','input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
     'E':E,'T':T,'four_literal_source_words':expected,
     'scope':'Exact raw source formula table; subsequent reductions use the established graph relations as written in B112.'}
(ROOT/'work_CE/next_symmetric_nodes/B112_source_formulas_independent23.json').write_text(json.dumps(out,indent=2)+'\n')
