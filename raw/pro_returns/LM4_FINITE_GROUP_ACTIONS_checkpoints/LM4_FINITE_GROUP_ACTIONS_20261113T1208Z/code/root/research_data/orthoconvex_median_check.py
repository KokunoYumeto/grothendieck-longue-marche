"""Exact finite exploratory check; does not prove the continuous assertion."""
import itertools,json
from pathlib import Path
n=4
pts=list(itertools.product(range(n),repeat=2))
count=0
counter=None
for mask in range(1,1<<len(pts)):
 S={pts[i] for i in range(len(pts)) if mask>>i&1}
 valid=True
 for axis in [0,1]:
  for v in range(n):
   a=sorted(p[1-axis] for p in S if p[axis]==v)
   if a and len(a)!=a[-1]-a[0]+1:valid=False;break
  if not valid:break
 if not valid:continue
 seen={next(iter(S))};todo=list(seen)
 while todo:
  x,y=todo.pop()
  for p in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
   if p in S and p not in seen:seen.add(p);todo.append(p)
 if seen!=S:continue
 count+=1
 for triple in itertools.combinations(S,3):
  median=tuple(sorted(p[i] for p in triple)[1] for i in [0,1])
  if median not in S:
   counter={"set":sorted(S),"triple":triple,"median":median};break
 if counter:break
result={"grid":n,"connected_row_and_column_convex_sets_checked":count,"counterexample":counter,"scope":"Finite grid exploration only; no continuous theorem is inferred."}
Path(__file__).with_suffix(".json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
