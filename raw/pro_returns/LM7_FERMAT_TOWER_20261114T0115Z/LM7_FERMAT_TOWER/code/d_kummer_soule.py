#!/usr/bin/env python3
"""Exact finite Kummer pairings and mod-l circular Kummer (Soule) values.
For each odd prime l<=50 and each odd m in [3,l-2], find a prime q=1 mod l^2
where c_m=prod(1-zeta_l^a)^(a^(m-1) mod l) has nonzero l-th power residue.
This is an explicit non-power certificate, with all choices retained.
"""
from pathlib import Path
from itertools import product
from math import gcd
import sympy as s
import json
OUT=Path(__file__).resolve().parent

def residue(l,m,q,r):
 c=1
 for a in range(1,l):c=c*pow((1-pow(r,a,q))%q,pow(a,m-1,l),q)%q
 v=pow(c,(q-1)//l,q)
 table={pow(r,j,q):j for j in range(l)}
 return {'m':m,'unit_residue':c,'power_residue':v,'kummer_value':table[v]}

def main():
 ks=[]
 for n in range(1,25):
  # The annihilator of n | 2a in Z/n is precisely 2(Z/n).
  rel=[a for a in range(n) if 2*a%n==0]
  dual=[b for b in range(n) if all(a*b%n==0 for a in rel)]
  evens=sorted({2*b%n for b in range(n)})
  assert dual==evens
  row={'n':n,'relation_subgroup':rel,'Kummer_image':dual,'index_one_prime':gcd(2,n),'indices_r1_to4':[gcd(2,n)**r for r in range(1,5)]};ks.append(row)
 print('Finite rational-prime Kummer images n<=24 verified by annihilator enumeration.')
 data=[]
 for l in list(s.primerange(3,51)):
  weights=list(range(3,l-1,2));pending=set(weights);certs=[];k=1
  while pending:
   q=1+k*l*l;k+=1
   if not s.isprime(q):continue
   g=int(s.primitive_root(q));r=pow(g,(q-1)//l,q)
   values=[residue(l,m,q,r) for m in weights]
   selected=[v['m'] for v in values if v['m'] in pending and v['kummer_value']]
   if selected:
    certs.append({'q':q,'primitive_root_q':g,'zeta_l_residue':r,'weights_certified':selected,'values':values});pending.difference_update(selected)
  irregular=[i for i in range(2,l-1,2) if int(s.numer(s.bernoulli(i)))%l==0]
  row={'l':l,'weights':weights,'all_nonzero_certificates_found':not pending,'irregular_bernoulli_indices':irregular,'Frobenius_certificates':certs};data.append(row)
  print('l=',l,'weights=',weights,'irregular=',irregular,'witness q=',[a['q'] for a in certs],flush=True)
 out={'kummer_finite_pairings':ks,'soule_mod_l':data,'conventions':'c_m = product_(a=1..l-1)(1-zeta_l^a)^(a^(m-1) mod l); kappa via zeta_l^k=Frob(root)/root. Empty weight list l=3 is intentional. l=2 has no weights 3<=m<=l-2.'}
 (OUT/'d_kummer_soule.json').write_text(json.dumps(out,indent=2))
 print('Every exponent, root and residue appears in d_kummer_soule.json. No class number is inferred merely from a Bernoulli irregularity.')
if __name__=='__main__':main()
