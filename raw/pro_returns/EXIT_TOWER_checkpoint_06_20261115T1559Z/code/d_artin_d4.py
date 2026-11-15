"""Exact classical Garside normal forms in A(D4) and Gamma_{1,3}.
Letters1,2,3 are the three commuting leaves;4 is the central Coxeter vertex.
Coxeter simples are even signed permutations of4 letters. Delta=(1234)^3
is central. In the mapping class quotient discard only its integral exponent.
"""
from pathlib import Path
from collections import deque
from functools import lru_cache
import json,random
P=Path(__file__).resolve().parent
I=(1,2,3,4)
S=[(2,1,3,4),(1,2,4,3),(1,2,-4,-3),(1,3,2,4)]
def mul(a,b):return tuple((1 if x>0 else -1)*a[abs(x)-1] for x in b)
def wi(a):
 out=[0]*4
 for i,x in enumerate(a):out[abs(x)-1]=(i+1)*(1 if x>0 else -1)
 return tuple(out)
reps={I:()};todo=deque([I])
while todo:
 w=todo.popleft()
 for j,s in enumerate(S,1):
  v=mul(w,s)
  if v not in reps:reps[v]=reps[w]+(j,);todo.append(v)
W=sorted(reps,key=lambda x:(len(reps[x]),x));index={w:i for i,w in enumerate(W)}
length=[len(reps[w]) for w in W];one=index[I];D=index[(-1,-2,-3,-4)]
assert len(W)==192 and length[D]==12 and one==0
mult=[[index[mul(a,b)] for b in W] for a in W]
inverse=[index[wi(w)] for w in W]
gen=[index[s] for s in S]
complement=[mult[inverse[a]][D] for a in range(192)]
leftdiv=[]
for b in range(192):
 leftdiv.append(frozenset(a for a in range(192) if length[a]+length[mult[inverse[a]][b]]==length[b]))
gcd={}
for a in range(192):
 for b in range(192):
  candidates=leftdiv[a]&leftdiv[b]
  n=max(length[x] for x in candidates)
  maxima=[x for x in candidates if length[x]==n]
  assert len(maxima)==1,(a,b,maxima)
  gcd[a,b]=maxima[0]

def inv(w):return tuple(-x for x in reversed(w))
def red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def cat(*ws):return red(x for w in ws for x in w)
def conj(a,b):return cat(a,b,inv(a))
def greedy(factors):
 factors=[a for a in factors if a!=one];power=0
 while True:
  count=factors.count(D)
  if count:power+=count;factors=[a for a in factors if a!=D]
  changed=False
  for i in range(len(factors)-1):
   a,b=factors[i:i+2];d=gcd[complement[a],b]
   if d!=one:
    ap=mult[a][d];bp=mult[inverse[d]][b]
    assert length[ap]==length[a]+length[d]
    assert length[b]==length[d]+length[bp]
    factors[i:i+2]=[ap,bp];changed=True
  factors=[a for a in factors if a!=one]
  if not changed and D not in factors:return power,tuple(factors)
@lru_cache(maxsize=200000)
def normal(w):
 power=0;factors=()
 for x in w:
  s=gen[abs(x)-1]
  if x<0:power-=1;s=complement[s]
  p,factors=greedy(factors+(s,));power+=p
 assert sum(1 if x>0 else -1 for x in w)==12*power+sum(length[a] for a in factors)
 return power,factors
def equal(u,v,quotient=True):
 p,f=normal(cat(u,inv(v)))
 return not f and (quotient or p==0)
def display(nf):
 p,f=nf
 return {'Delta_power':p,'simple_words':[reps[W[a]] for a in f]}
DELTA=(1,2,3,4)*3
assert normal(DELTA)==(1,())
if __name__=='__main__':
 checks=[]
 for i in (1,2,3):
  assert equal((i,4,i),(4,i,4),False);checks.append(['braid',i,4])
 for i,j in ((1,2),(1,3),(2,3)):
  assert equal((i,j),(j,i),False);checks.append(['commute',i,j])
 for i in range(1,5):
  assert equal(DELTA+(i,),(i,)+DELTA,False);checks.append(['Delta_central',i])
 rng=random.Random(1302026)
 for z in range(100):
  w=tuple(rng.choice((-4,-3,-2,-1,1,2,3,4)) for _ in range(16))
  assert normal(cat(w,inv(w)))==(0,())
  l=rng.randrange(17);prefix=w[:l];suffix=w[l:]
  i=rng.randrange(1,4)
  assert normal(prefix+(i,4,i)+suffix)==normal(prefix+(4,i,4)+suffix)
  assert normal(prefix+(1,2)+suffix)==normal(prefix+(2,1)+suffix)
  n=normal(w);expanded=cat(DELTA*n[0] if n[0]>=0 else inv(DELTA)*(-n[0]),*(reps[W[a]] for a in n[1]))
  assert normal(expanded)==n
 out={'coxeter_order':len(W),'Delta_length':12,'Delta_word':DELTA,'finite_gcd_checks':192**2,'defining_checks':checks,'randomized_rewrite_checks':400,
      'algorithm':'left greedy factors: transfer gcd_left(partial(a),b) from b to a; Delta central; negative atom=Delta^-1 partial(atom)',
      'simples':[{'signed_permutation':w,'word':reps[w],'length':len(reps[w])} for w in W]}
 (P/'d_artin_d4.json').write_text(json.dumps(out,indent=2)+'\n')
 print('A(D4):192 Coxeter simples; Delta length12; all36864 weak-order gcds unique.')
 print('All6 Artin relations,4 centrality relations and400 seeded reduction checks passed.')
 print('Exact quotient Gamma1,3=A(D4)/<Delta> is compared by the proper greedy factors.')
