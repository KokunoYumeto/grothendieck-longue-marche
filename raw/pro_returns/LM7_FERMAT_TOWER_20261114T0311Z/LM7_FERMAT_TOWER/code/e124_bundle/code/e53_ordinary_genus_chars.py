from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
import sympy as S
R=Path(__file__).resolve().parents[1]
P=R/'inputs/e123_presentation.out'
rows=[json.loads(x) for x in P.read_text().splitlines() if x.startswith('{')]
G=next(x for x in rows if x.get('type')=='full_S_class_presentation')
def val(x,p=53):
 x=Q(x)
 if not x:return 10**9
 a,b=abs(x.numerator),x.denominator;e=0
 while a%p==0:a//=p;e+=1
 while b%p==0:b//=p;e-=1
 return e
def red(x):
 x=Q(x);assert x.denominator%53
 return x.numerator*pow(x.denominator,-1,53)%53
def mul(x,y):
 a,b=x;c,d=y
 return ((a*c-b*d)%53,(a*d+b*c-b*d)%53)
def power(x,n):
 z=(1,0)
 while n:
  if n&1:z=mul(z,x)
  n//=2
  if n:x=mul(x,x)
 return z
logs={power((0,1),i):i for i in range(3)}
def symbol(co):
 co=list(map(Q,co));terms=[]
 for i in range(9):
  a,b=co[i],53*co[i+9];k=min(val(a),val(b))
  if k==10**9:continue
  u=mul((red(a/Q(53)**k),red(b/Q(53)**k)),power((0,1),(-k)%3))
  terms.append((i+9*k,u))
 v=min(x[0] for x in terms);us=[u for e,u in terms if e==v];assert len(us)==1
 u=us[0];ph=power(u,936);ch=(-logs[ph])%3
 return {'valuation53':v,'residue':u,'cubic_power':ph,'chi53':ch}
fr=[json.loads(x) for x in (R/'code/e53_ordinary_frobenius.out').read_text().splitlines() if x.startswith('{')]
assert fr[-1]['status']=='PASS'
assert '***   at ' not in (R/'code/e53_ordinary_frobenius.err').read_text()
ideals=fr[:-1];frob=fr[-1]['actual_Frobenius_columns']
rel=[]
for r in rows:
 if r.get('type')=='class_power_relation':
  a=symbol(r['generator_coefficients']);assert a['valuation53']==0
  a.update({'index':r['index'],'power':r['exponent'],'chi3':(-a['chi53'])%3})
  rel.append(a)
q=next(x for x in rows if x.get('type')=='S_prime_relation' and x['prime']==3)
qc=symbol(q['generator_coefficients']);assert qc['valuation53']==0
qc['lower_class']=q['class_column'];qc['chi3']=(sum(a*b for a,b in zip(q['class_column'],frob))-qc['chi53'])%3
out={'status':'PASS','generator_ideals':ideals,'principal_power_characters':rel,
 'three_prime_correction':qc,'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
 'scope':'Actual finite tame symbols. The three-place entries follow from global reciprocity and the retained exact complete principal divisors, with the norm uniformizer1+beta2 having zero local character.'}
(R/'inputs/e53_ordinary_genus_input.txt').write_text(json.dumps([frob,[[r['chi3'],r['chi53'],r['power']] for r in rel],q['class_column'],[qc['chi3'],qc['chi53']]])+'\n')
s=json.dumps(out,indent=2)+'\n';(R/'code/e53_ordinary_genus_chars.json').write_text(s);print(s,end='')
