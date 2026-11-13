#!/usr/bin/env python3
"""Exact Fox/gamma comparison with the independently computed special images.

Checks every Lyndon basis word of degrees 2..10 in the free associative
algebra, and locates the actual Galois/full-GT gamma line in D.11's image.
This calculation does not infer profinite realization of the extra GT0 line.
"""
import json
from pathlib import Path
import sympy as s
from d_metabelian import words, LB, meta

ROOT=Path(__file__).resolve().parent
X,Y=s.symbols('X Y')
data=json.loads((ROOT/'d_metabelian.json').read_text())
rows=[]
total=0
for n in range(2,11):
    for w in words(n):
        f=LB(w)
        fox=s.expand(sum(c*X**v.count(0)*Y**v.count(1)
                         for v,c in f.items() if v[-1]==1))
        met=s.expand(sum(c*X**a*Y**b for (a,b),c in meta(w).items()))
        assert s.expand(fox-X*Y*met)==0, (n,w,fox,met)
        total+=1
    gamma=s.cancel(((X+Y)**n-X**n-Y**n)/(X*Y)).expand()
    special=s.expand(gamma.subs(Y,-X))==0
    assert special==(n%2==1)
    basis=[s.sympify(p) for p in data['image_bases'][str(n)]['S3_image_basis']]
    def v(p):return s.Matrix([s.expand(p).coeff(X,a).coeff(Y,n-2-a)
                              for a in range(n-1)])
    coords=[]
    if special:
        A=s.Matrix.hstack(*[v(p) for p in basis])
        coeff=A.gauss_jordan_solve(v(gamma))[0]
        assert A*coeff==v(gamma)
        coords=[str(c) for c in coeff]
    rows.append({'weight':n,'lyndon_words_checked':len(words(n)),
                 'gamma_polynomial':str(gamma),
                 'is_special':special,
                 'actual_Galois_and_GT_rational_rank':int(special),
                 'S3_special_image_rank':len(basis),
                 'gamma_coordinates_in_S3_image_basis':coords})
    print(json.dumps(rows[-1],sort_keys=True))

extra=s.sympify(data['image_bases']['9']['S3_image_basis'][0])
g9=s.sympify(next(r['gamma_polynomial'] for r in rows if r['weight']==9))
# Compute the degree7 vectors explicitly, independently of the loop degree.
v9=lambda p:s.Matrix([s.expand(p).coeff(X,a).coeff(Y,7-a) for a in range(8)])
assert s.Matrix.hstack(v9(extra),v9(g9)).rank()==2
result={'fox_identity_words_checked':total,'rows':rows,
        'extra_weight9_polynomial':str(extra),
        'extra_weight9_fails_gamma_line':True,
        'scope':'Exact rational leading equations. Actual full-GT ranks use D.21; no full profinite GT0 lift inferred.'}
(ROOT/'d_gamma.json').write_text(json.dumps(result,indent=2))
print('Checked Fox identity on',total,'Lyndon words; weight9 extra line is independent of gamma line.')
