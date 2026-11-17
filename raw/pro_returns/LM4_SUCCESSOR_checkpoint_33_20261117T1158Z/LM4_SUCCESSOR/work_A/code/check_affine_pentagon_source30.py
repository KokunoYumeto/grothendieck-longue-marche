"""Exact free-word input check for the uniform affine P4 proof; no targets enumerated."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
def red(w):
 o=[]
 for x in w:
  if o and o[-1]==-x:o.pop()
  else:o.append(x)
 return o
def inv(w):return [-x for x in reversed(w)]
def co(a,b):return red(a+b+inv(a))
def sub(w,d):return red([y for x in w for y in (d[abs(x)] if x>0 else inv(d[abs(x)]))])
d,e,f=[1],[2],[3]
A={1:co(d+e,d),2:co(d,e),3:f}
B={1:co(d+f,d),2:co(red(d+f+inv(d)+inv(f)),e),3:co(d,f)}
C={1:d,2:co(e+f,e),3:co(e,f)}
checks=[]
for i in (1,2,3):
 v=sub(sub(sub([i],A),B),C)
 expected=co(d+e+f,[i])
 assert v==expected,('central_action',i,v,expected)
 checks.append({'generator':i,'phi_c_phi_b_phi_a':v,'boundary_conjugate':expected})
record={'status':'PASS','scope':'Three literal central-action identities only; no finite target, parameter, source-word or exponent census.','actual_pure_actions':{'a_inverse':A,'b_inverse':B,'c_inverse':C},'checks':checks}
target=ROOT/'work_A/affine_pentagon_source30.json';assert not target.exists();target.write_text(json.dumps(record,indent=2)+'\n')
print('PASS: all three exact actual pure-action identities for (abc)^-1 equal conjugation by def')
print('Uniform affine classification and pentagon consequences are proved in the separate note, not inferred from this check.')
