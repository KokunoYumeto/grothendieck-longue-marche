"""Local free-word calculation using exactly the generator images on scans 005–006."""
import json
from pathlib import Path
E=Path(__file__).resolve().parents[1]
def red(w):
 s=[]
 for x in w:
  if s and s[-1]==-x:s.pop()
  else:s.append(x)
 return tuple(s)
def inv(w):return tuple(-x for x in reversed(w))
def apply(f,w):return red(y for x in w for y in (f[x] if x>0 else inv(f[-x])))
def compose(f,g):return {i:apply(f,g[i]) for i in (1,2)}
def conj(w,v):return red(w+v+inv(w))
a=(1,);b=(2,);c=(-2,-1)
rho={1:b,2:c}
sinf={1:b,2:a}
s0={1:red(inv(b)+inv(c)),2:c}
s1={1:c,2:red(inv(c)+inv(a))}
rows=[]
for name,f,g,w in [('sigma0 sigma1',s0,s1,inv(b)),('sigma1 sigmainfty',s1,sinf,inv(c)),('sigmainfty sigma0',sinf,s0,inv(a))]:
 lhs=compose(f,g);rhs={i:conj(w,rho[i]) for i in (1,2)}
 rows.append({'equation':name+' = int(conjugator) rho','conjugator':w,'left_generator_images':lhs,'right_generator_images':rhs,'equal':lhs==rhs})
 assert lhs==rhs
out={'encoding':'1=l0, 2=l1; a negative integer denotes inverse; linfty=(-2,-1). Cancellation is adjacent x,-x only.','checks':rows}
(E/'reader_reports/145_scan006_word_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out))
