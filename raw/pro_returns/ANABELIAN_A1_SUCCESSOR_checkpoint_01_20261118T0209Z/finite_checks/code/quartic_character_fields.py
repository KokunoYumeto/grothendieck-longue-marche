"""Exact first possible constant-character field for the smallest prime.
Uses only the Weil polynomial, which suffices for existence of a nonzero
fixed vector; it does not infer its dimension in nonsemisimple cases.
"""
from pathlib import Path
from collections import Counter
import csv,json,itertools
import sympy as sp
root=Path(__file__).resolve().parent;x=sp.symbols('x');all_summary={}
for p,l in [(3,5),(5,3)]:
 cache={};hist=Counter();exact=[]
 for row in csv.DictReader((root/f'quartic_F{p}_weil.csv').open()):
  a1,a2,a3=map(int,[row['a1'],row['a2'],row['a3']]);key=(a1%l,a2%l,a3%l)
  if key not in cache:
   P=sp.Poly(x**6+a1*x**5+a2*x**4+a3*x**3+p*a2*x*x+p*p*a1*x+p**3,x,modulus=l)
   facts=sp.factor_list(P)[1];orders=[]
   for f,mult in facts:
    d=f.degree();r=sp.Poly(x,x,modulus=l);one=sp.Poly(1,x,modulus=l);order=l**d-1
    for pr in sp.factorint(order):
     while order%pr==0:
      n=order//pr;a=r;b=one
      while n:
       if n%2:b=(b*a)%f
       a=(a*a)%f;n//=2
      if b!=one:break
      order//=pr
    orders.append({'irreducible_coefficients':list(map(int,f.all_coeffs())),
                   'degree':d,'multiplicity':mult,'root_order':int(order)})
   cache[key]={'first_degree':min(r['root_order'] for r in orders),'factors':orders}
  m=cache[key]['first_degree'];hist[m]+=1
  exact.append({**row,'ell':l,'first_possible_character_degree':m})
 with (root/f'quartic_F{p}_first_character_fields.csv').open('w') as f:
  w=csv.DictWriter(f,fieldnames=list(exact[0]));w.writeheader();w.writerows(exact)
 all_summary[p]={'ell':l,'classes':len(exact),'first_degree_histogram':dict(sorted(hist.items())),
  'residue_types':[{'a1_a2_a3':key,**val} for key,val in sorted(cache.items())],
  'scope':'First field where any constant nonzero ell-character exists, not a witness test.'}
(root/'quartic_first_character_fields.json').write_text(json.dumps(all_summary,indent=2)+'\n')
print(json.dumps({p:{k:v for k,v in a.items() if k!='residue_types'} for p,a in all_summary.items()},indent=2))
