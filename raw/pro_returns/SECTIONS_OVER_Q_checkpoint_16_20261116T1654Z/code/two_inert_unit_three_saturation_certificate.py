"""Finite residue detectors for three-saturation of four explicit units.
The determinant test uses only literal power-basis evaluations modulo primes.
"""
from pathlib import Path
from fractions import Fraction as F
import json,sys,itertools
import sympy as sp
sys.set_int_max_str_digits(0)
base=Path(__file__).resolve().parent
raw=json.loads((base/'two_inert_relative_unit_repair_certificate_data.json').read_text())
units=[[F(x)for x in row['candidate']]for row in raw['units']]
assert len(units)==4
rad=raw['radicand']

def rank(rows,p=3):
 a=[r[:]for r in rows];rr=0
 for j in range(4):
  pivot=next((i for i in range(rr,len(a))if a[i][j]%p),None)
  if pivot is None:continue
  a[rr],a[pivot]=a[pivot],a[rr]
  a[rr]=[(v*pow(a[rr][j],-1,p))%p for v in a[rr]]
  for i in range(len(a)):
   if i!=rr:
    c=a[i][j];a[i]=[(x-c*y)%p for x,y in zip(a[i],a[rr])]
  rr+=1
 return rr
rows=[];witnesses=[]
for p in sp.primerange(5,100000):
 p=int(p)
 if p%3!=1 or rad%p==0:continue
 if any(v.denominator%p==0 for u in units for v in u):continue
 roots=sp.nthroot_mod(rad%p,9,p,all_roots=True)
 if not roots:continue
 primitive=int(sp.primitive_root(p));omega=pow(primitive,(p-1)//3,p)
 assert omega!=1 and pow(omega,3,p)==1
 for root in roots:
  root=int(root)
  vals=[];characters=[];exponents=[]
  for u in units:
   value=0
   for v in reversed(u):value=(value*root+v.numerator*pow(v.denominator,-1,p))%p
   assert value
   character=pow(value,(p-1)//3,p)
   exponent=next(i for i in range(3)if pow(omega,i,p)==character)
   vals.append(value);characters.append(character);exponents.append(exponent)
  if rank(rows+[exponents])>len(rows):
   rows.append(exponents)
   witnesses.append({'p':p,'root':root,'primitive_root':primitive,'omega':omega,'unit_values':vals,'unit_characters':characters,'exponents':exponents})
   print('INDEPENDENT ROW',witnesses[-1],flush=True)
  if len(rows)==4:break
 if len(rows)==4:break
assert len(rows)==4,'No full-rank certificate found in the search range; no saturation conclusion.'
det=int(sp.Matrix(rows).det());assert det%3
# Recheck all 3^4 combinations: a cubic combination has zero detector
# vector, which happens only for the zero vector.
count=0
for e in itertools.product(range(3),repeat=4):
 z=[sum(x*y for x,y in zip(row,e))%3 for row in rows]
 assert (not any(z))==(not any(e));count+=1
out={'matrix':rows,'integer_determinant':det,'witnesses':witnesses,'exponent_combinations_checked':count}
(base/'two_inert_unit_three_saturation_certificate_data.json').write_text(json.dumps(out,indent=2)+'\n')
print('DETERMINANT',det,'MOD3',det%3)
print('PASS: all81 exponent combinations; only the zero combination can be a cube.')
print('Together with Dirichlet rank4, the explicitly generated positive-norm unit subgroup has index prime to3.')
