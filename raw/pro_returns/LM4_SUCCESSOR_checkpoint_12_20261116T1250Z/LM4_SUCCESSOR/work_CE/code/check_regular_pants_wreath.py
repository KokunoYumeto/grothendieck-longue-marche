"""Exact primitive-cusp wreath quotient; no unknown word is evaluated."""
from itertools import permutations
from pathlib import Path
import json
I=tuple(range(5))
def mul(a,b):return tuple(a[b[i]]for i in range(5))
def inv(a):return tuple(a.index(i)for i in range(5))
def even(a):return sum(a[i]>a[j]for i in range(5)for j in range(i+1,5))%2==0
S=[a for a in permutations(range(5))if even(a)]
a=(1,2,0,3,4);b=(1,2,3,4,0)
def generated(gens,prod,one):
 seen={one};todo=[one]
 while todo:
  g=todo.pop()
  for h in gens:
   x=prod(g,h)
   if x not in seen:seen.add(x);todo.append(x)
 return seen
assert len(S)==60
assert all(len(generated((a,mul(mul(u,b),inv(u))),mul,I))==60 for u in S)
assert all(len(generated((b,mul(mul(u,a),inv(u))),mul,I))==60 for u in S)
def em(g,h):
 x,y,e=g;u,v,f=h
 if e:u,v=v,u
 return(mul(x,u),mul(y,v),e^f)
ONE=(I,I,0);s=(I,I,1);z=(a,b,0)
im=generated((s,z),em,ONE)
assert len(im)==7200
assert sum(g[2]==0 for g in im)==3600
print('A5 order60; all60 conjugates of each3/5 pair generate A5: PASS')
print('Actual source images x=swap,z=(3cycle,5cycle) generate order7200: PASS')
print('Uniform generation for every opposite-coset h follows by isolating the two factors with coprime powers of z.')
out=dict(group='(A5 x A5) semidirect C2 by swap',order=7200,
         x=s,z=z,all_60_three_five_conjugate_tests=True,
         scope='Every g of odd x-exponent generates this actual quotient together with z; no full F generation inferred')
(Path(__file__).resolve().parents[1]/'regular_pants_wreath_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
