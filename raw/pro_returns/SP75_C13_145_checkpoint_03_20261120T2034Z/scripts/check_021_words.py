"""Local automorphism checks for scan021; no inference of handwriting."""
from pathlib import Path
import json
E=Path(__file__).resolve().parents[1]
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def prod(*ws):return red(x for w in ws for x in w)
def apply(f,w):return red(y for x in w for y in (f[x] if x>0 else inv(f[-x])))
def comp(f,g):return {i:apply(f,g[i]) for i in (1,2)}
a=(1,);b=(2,);c=(-1,-2);I={1:a,2:b}
r={1:b,2:c}
s=[{1:prod(inv(c),inv(b)),2:c},{1:c,2:prod(inv(a),inv(c))},{1:b,2:a}]
t=[{1:inv(a),2:inv(c)},{1:inv(c),2:inv(b)},{1:inv(b),2:inv(a)}]
checks=[]
def check(claim,left,right):
 checks.append({'claim':claim,'left':left,'right':right,'equal':left==right})
 assert left==right,claim
for i in range(3):
 check('tilde sigma '+str(i)+' squared',comp(t[i],t[i]),I)
 check('cyclic tilde sigma product '+str(i),comp(t[i],t[(i+1)%3]),r)
 check('rho conjugation '+str(i),comp(r,t[i]),comp(t[(i+1)%3],r))
 check('sigma and tilde sigma commute '+str(i),comp(s[i],t[i]),comp(t[i],s[i]))
 q=comp(s[i],t[i]);check('tau '+str(i)+' squared',comp(q,q),I)
check('tilde sigma0 on linfinity',apply(t[0],c),inv(b))
out={'encoding':'1=l0,2=l1,linfinity=(-1,-2); right map acts first. Indices 0,1,2 in labels mean 0,1,infinity.','scope':'Free-group automorphism images only. Confirms formula14, relation13, cyclic covariance and the commuting/square images in15–16. Does not by itself prove that an abstract extension is faithfully represented by these automorphisms.','checks':checks}
(E/'reader_reports/145_scan021_word_check.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'checks':len(checks),'all_passed':all(x['equal'] for x in checks)}))
