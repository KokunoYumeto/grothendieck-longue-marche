#!/usr/bin/env python3
"""Certify three-saturation of the four actual degree-nine units by residues."""
from pathlib import Path
from fractions import Fraction
import json
import sympy as s

HERE=Path(__file__).resolve().parent
records=[json.loads(x) for x in (HERE/'e53_pure9_norm_witness.out').read_text().splitlines() if x.startswith('{')]
units=[r for r in records if r.get('type')=='actual_upper_S_unit_norm'][:4]
assert len(units)==4 and all(r['S_valuations']==[0,0,0,0] for r in units)
C=[[Fraction(a) for a in r['element']] for r in units]
def rank3(M):
    a=[[v%3 for v in row] for row in M];rr=0
    for j in range(4):
        k=next((i for i in range(rr,len(a)) if a[i][j]),None)
        if k is None:continue
        a[rr],a[k]=a[k],a[rr]
        d=pow(a[rr][j],-1,3);a[rr]=[v*d%3 for v in a[rr]]
        for i in range(len(a)):
            if i!=rr:
                d=a[i][j];a[i]=[(x-d*y)%3 for x,y in zip(a[i],a[rr])]
        rr+=1
    return rr
def ev(c,a,p):
    x=0
    for v in reversed(c):x=(x*a+v.numerator*pow(v.denominator,-1,p))%p
    return x

rows=[];chosen=[];all_seen=[]
for p in s.primerange(7,10000):
    p=int(p)
    if p%3!=1 or p==53:continue
    z=next(pow(g,(p-1)//3,p) for g in range(2,p) if pow(g,(p-1)//3,p)!=1)
    for a in range(1,p):
        if pow(a,9,p)!=53%p:continue
        values=[ev(c,a,p) for c in C];assert all(values)
        characters=[]
        for v in values:
            w=pow(v,(p-1)//3,p)
            ee=[e for e in range(3) if pow(z,e,p)==w]
            assert len(ee)==1;characters.append(ee[0])
        rec={'p':p,'alpha_residue':a,'zeta_residue':z,'unit_residues':values,'cubic_characters':characters}
        all_seen.append(rec)
        if rank3(rows+[characters])>len(rows):rows.append(characters);chosen.append(rec)
        if len(rows)==4:break
    if len(rows)==4:break
assert len(rows)==4
M=s.Matrix(rows);det=int(M.det());assert det%3
inverse=(pow(det,-1,3)*M.adjugate()).applyfunc(lambda a:int(a)%3)
assert (M*inverse).applyfunc(lambda a:int(a)%3)==s.eye(4)
relations=[]
from itertools import product
for e in product(range(3),repeat=4):
    image=[sum(row[i]*e[i] for i in range(4))%3 for row in rows]
    assert any(image) or e==(0,0,0,0)
    relations.append({'exponent':list(e),'image':image})
out={'statement':'E116 pure53 unit saturation','status':'PASS','basis_residue_witnesses':chosen,
     'matrix':rows,'determinant':det,'inverse_mod3':[[int(a) for a in row] for row in inverse.tolist()],
     'all_81_power_class_checks':relations,'all_tested_prime_rows':all_seen,
     'conclusion':'Every nonzero product of the four actual units modulo cubes has a nontrivial finite residue character. They therefore form a basis of the completed ordinary unit group, since the real signature gives rank4 and there is no three-primary root of unity. No full BNF certification is used.'}
text=json.dumps(out,indent=2)+'\n';(HERE/'e53_unit_saturation.json').write_text(text);print(text,end='')
