"""Compare all four Cartier cases with direct rational-point characters.

Runs all cubic covers in the104 monic F4 normal-form models, then all
quintic covers in two F16 models chosen to exercise low-degree and branch
cases. Duplicate models are intentional; this is coefficient validation,
not a moduli census.
"""
import sys,json
from pathlib import Path
from collections import Counter
from itertools import product
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'code'))
from finite_jacobian import BinaryField,Jacobian
from A4_first_models import models
from verify_mixed_certificates import independent_double
stats=Counter();rows=[]
def check(F,name,h,f,ell):
 J=Jacobian(F,h,f);elts=J.enumerate();stats['models_checked']+=1
 tors=[D for D in elts if D!=J.zero and J.scale(D,ell)==J.zero]
 if not tors:return
 assert (F.q-1)%ell==0
 stats['models_with_covers']+=1
 seen=set();pred=0;number=0
 for D in tors:
  if D in seen:continue
  ds=[J.zero]
  for _ in range(1,ell):ds.append(J.add(ds[-1],D))
  seen.update(ds[1:]);number+=1;coeff=[0]*ell
  for i in range(1,ell):
   out,c,case=independent_double(J,ds[i]);assert out==ds[2*i%ell]
   coeff[i]=c;stats['case_'+case]+=1
  As=[]
  for i in range(1,ell):
   a=1;j=i
   for _ in range(F.m):a=F.mul(F.mul(a,a),coeff[j]);j=2*j%ell
   assert j==i;As.append(a)
  pred+=int(all(a!=1 for a in As))
 coords,basis,H=J.quotient(ell);r=len(basis);actual=0;actualn=0
 zeta=F.power(F.generator,(F.q-1)//ell)
 for v in product(range(ell),repeat=r):
  if not any(v) or next(a for a in v if a)!=1:continue
  actualn+=1;S=0
  for _,D in J.points():
   e=sum(a*b for a,b in zip(v,coords[D]))%ell
   S^=F.power(zeta,e)
  actual+=int(S!=1)
 assert (pred,number)==(actual,actualn),(name,pred,number,actual,actualn)
 rows.append({'field':F.q,'model':name,'h':h,'f':f,'J_order':len(elts),
  'prime':ell,'covers':number,'Cartier_good':pred,'point_character_good':actual})
F=BinaryField(7)
for name,h,f in models(F):
 if f[-1]==1:check(F,name,h,f,3)
F=BinaryField(19)
check(F,'Fermat_five',(1,),(0,0,0,0,0,1),5)
check(F,'rank_one_branch',(0,1),(0,1,0,1,0,1),5)
assert all(stats['case_'+k]>0 for k in ('branch','one_two','two_one','two_two'))
print(json.dumps({'statistics':dict(stats),'all_four_cases_exercised':True,
 'all_direct_comparisons_passed':True,'rows':rows},indent=2))
