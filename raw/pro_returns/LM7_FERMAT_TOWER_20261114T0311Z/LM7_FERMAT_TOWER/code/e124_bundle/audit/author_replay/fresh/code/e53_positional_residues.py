from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
R=Path(__file__).resolve().parents[1]
D=json.loads((R/'inputs/e122_witnesses.json').read_text())
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
rows=[]
for j,co in enumerate(D['upper_candidates'],1):
 co=list(map(Q,co));terms=[]
 for i in range(9):
  a,b=co[i],53*co[i+9];k=min(val(a),val(b))
  if k==10**9:continue
  unit=mul((red(a/Q(53)**k),red(b/Q(53)**k)),power((0,1),(-k)%3))
  terms.append((i+9*k,unit))
 v=min(x[0] for x in terms);us=[u for e,u in terms if e==v];assert len(us)==1
 u=us[0];ph=power(u,936);c=(-logs[ph])%3
 if j<=9:assert v==0
 else:assert v==1
 rows.append({'candidate':j,'v53':v,'residue_after_beta_power':u,'cubic_power':ph,'positive_chi53':c})
out={'status':'PASS','scope':'Ten literal S-units only; first eight ordinary by the existing full divisor checks. No claim of ordinary-unit completeness.',
 'rows':rows,'ordinary_character_rank':int(any(r['positive_chi53'] for r in rows[:8])),
 'input_sha256':hashlib.sha256((R/'inputs/e122_witnesses.json').read_bytes()).hexdigest()}
s=json.dumps(out,indent=2)+'\n';(R/'code/e53_positional_residues.json').write_text(s);print(s,end='')
