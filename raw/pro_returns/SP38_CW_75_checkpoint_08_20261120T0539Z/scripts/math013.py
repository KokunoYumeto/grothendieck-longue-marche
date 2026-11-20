"""Exact finite action certificates for scan013; no image/text recognition."""
from itertools import product,permutations
from pathlib import Path
import json

def compose(p,q):return tuple(p[q[i]] for i in range(len(p)))
vectors=((1,0),(0,1),(1,1))
def act(m,v):
 a,b,c,d=m;x,y=v
 return ((a*x+b*y)%2,(c*x+d*y)%2)
def mul(m,n):
 a,b,c,d=m;e,f,g,h=n
 return ((a*e+b*g)%2,(a*f+b*h)%2,(c*e+d*g)%2,(c*f+d*h)%2)
matrices=[m for m in product(range(2),repeat=4) if (m[0]*m[3]-m[1]*m[2])%2==1]
mp={m:tuple(vectors.index(act(m,v)) for v in vectors) for m in matrices}
assert len(matrices)==6 and len(set(mp.values()))==6
for m in matrices:
 for n in matrices:assert mp[mul(m,n)]==compose(mp[m],mp[n])
affines=[(b,a) for b in range(3) for a in (1,2)]
ap={(b,a):tuple((b+a*x)%3 for x in range(3)) for b,a in affines}
assert set(mp.values())==set(ap.values())==set(permutations(range(3)))
for b,a in affines:
 for d,c in affines:
  assert ap[((b+a*d)%3,(a*c)%3)]==compose(ap[(b,a)],ap[(d,c)])
def sign(p):return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
assert all(sign(ap[(b,1)])==1 for b in range(3))
assert all(sign(ap[(b,2)])==-1 for b in range(3))
aff2=[tuple((b+x)%2 for x in range(2)) for b in range(2)]
assert set(aff2)==set(permutations(range(2)))
out={'GL2_F2':{'vectors':vectors,'matrices_and_actions':[{'matrix':m,'permutation':mp[m]} for m in matrices],'all_36_products_action_compatible':True},'Aff1_F3':{'maps_and_actions':[{'b':b,'a':a,'permutation':ap[(b,a)],'sign':sign(ap[(b,a)])} for b,a in affines],'all_36_products_action_compatible':True},'permutation_images_equal_S3':True,'Aff1_F2_actions':aff2,'A3_exactly_translations':True,'source':'Exact finite enumeration executed in this run; interpretations conditional on the stated group definitions.'}
dest=Path(__file__).resolve().parents[1]/'decisions/scan013_finite_certificate.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'path':str(dest),'GL2_F2_size':6,'Aff1_F3_size':6,'action_product_checks':72,'Aff1_F2_size':2,'assertions':'passed'}))
