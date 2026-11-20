"""Exact small permutation checks for statements appearing on scan 009."""
from itertools import permutations
from pathlib import Path
import json
def compose(a,b):return tuple(a[b[i]] for i in range(len(a)))
def inverse(a):
 r=[0]*len(a)
 for i,j in enumerate(a):r[j]=i
 return tuple(r)
def cycles(a):
 seen=set();cs=[]
 for i in range(len(a)):
  if i in seen:continue
  c=[];j=i
  while j not in seen:seen.add(j);c.append(j+1);j=a[j]
  cs.append(c)
 return cs
def parity(a):return sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))%2
def classes(group):
 left=set(group);out=[]
 while left:
  a=min(left);orb={compose(compose(g,a),inverse(g)) for g in group}
  assert orb<=left
  left-=orb
  out.append(dict(representative=list(a),cycles_1_based=cycles(a),size=len(orb)))
 return out
result={'convention':'tuple a sends zero-based i to a[i]; listed cycles use labels 1,...,n','groups':{}}
for n in (2,3,4):
 s=list(permutations(range(n)));a=[p for p in s if parity(p)==0]
 for name,g in [(f'S{n}',s),(f'A{n}',a)]:
  c=classes(g);result['groups'][name]={'order':len(g),'class_count':len(c),'classes':c}
assert [result['groups'][f'S{n}']['class_count'] for n in (2,3,4)]==[2,3,5]
assert [result['groups'][f'A{n}']['class_count'] for n in (2,3,4)]==[1,3,4]
bad=(1,0,3,2);cs=cycles(bad);counts={}
for c in cs:counts[len(c)]=counts.get(len(c),0)+1
assert len(counts)==1 and len(cs)==2
result['transitivity_counterexample']={'permutation':list(bad),'cycles_1_based':cs,'orbit_type_counts':counts,'nonzero_type_count':len(counts),'orbit_count':len(cs),'transitive':False}
fourcycle=(1,2,3,0)
assert parity(fourcycle)==1
result['canceled_A4_candidate']={'permutation':list(fourcycle),'cycles_1_based':cycles(fourcycle),'parity':'odd','belongs_to_A4':False,'status':'conditional on visual reading of canceled index 1234'}
root=Path(__file__).resolve().parents[1]
(root/'decisions/scan009_permutation_certificate.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'groups':{k:(v['order'],v['class_count']) for k,v in result['groups'].items()},'transitivity_counterexample':result['transitivity_counterexample'],'assertions':'passed'}))
