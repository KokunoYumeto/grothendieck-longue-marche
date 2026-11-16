"""Independent Witt/complex-conjugation dimension audit through degree eight."""
from pathlib import Path
from sympy import divisors,mobius
import json
full=[];meta=[]
for n in range(1,9):
 rank=int(sum(mobius(d)*2**(n//d) for d in divisors(n))//n)
 trace=int(sum(mobius(d)*(2 if d%2==0 else 0)**(n//d) for d in divisors(n))//n)
 minus=(rank-trace)//2
 full.append({'n':n,'rank':rank,'conjugation_trace':trace,'minus_dimension':minus})
 meta.append({'n':n,'rank':2 if n==1 else n-1,'minus_dimension':1 if n==1 else n//2})
tables={}
locals={}
for typ,layers in [('full',full),('metabelian',meta)]:
 tables[typ]=[];local=[1]
 for n in range(2,9):local.append(local[-1]+layers[n-1]['rank'])
 locals[typ]=local
 for r in (0,1):
  for s in range(3):
   vals=[r,r+s]
   for n in range(3,9):vals.append(vals[-1]+layers[n-1]['minus_dimension'])
   first=next(n for n,(a,b) in enumerate(zip(vals,local),1) if a<b)
   tables[typ].append({'r':r,'s':s,'global_dimensions':vals,'first_strict_level':first})
assert [r['first_strict_level'] for r in tables['full']]==[1,1,1,2,3,4]
assert [r['first_strict_level'] for r in tables['metabelian']]==[1,1,1,2,3,4]
out={'full_layers':full,'metabelian_layers':meta,'local_dimensions':locals,'tables':tables}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
