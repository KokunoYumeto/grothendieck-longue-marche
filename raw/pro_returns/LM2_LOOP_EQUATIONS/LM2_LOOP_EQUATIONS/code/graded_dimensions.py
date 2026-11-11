#!/usr/bin/env python3
"""Exact rational graded tripod computations, independent of supplied review code.
Uses Lyndon brackets in the free associative algebra; rational ranks are computed
with SymPy DomainMatrix. Character formulas supply independent dimension checks.
"""
from functools import cache
from itertools import product
from math import gcd
from pathlib import Path
import csv,json,time
import sympy as sp
from sympy.polys.matrices import DomainMatrix

OUT=Path(__file__).resolve().parent

def add(a,b,s=1):
 c=a.copy()
 for w,v in b.items():
  c[w]=c.get(w,0)+s*v
  if not c[w]: del c[w]
 return c

def mul(a,b):
 c={}
 for u,v in a.items():
  for w,t in b.items():
   k=u+w;c[k]=c.get(k,0)+v*t
 return {w:v for w,v in c.items() if v}

def bracket(a,b):return add(mul(a,b),mul(b,a),-1)
x={(0,):1};y={(1,):1};z={(0,):-1,(1,):-1}
@cache
def lyndon(w):return all(w<w[i:]+w[:i] for i in range(1,len(w)))
@cache
def words(n):return tuple(w for w in product((0,1),repeat=n) if lyndon(w))
@cache
def LB(w,mode=0):
 imgs=((x,y),(y,x),(y,z),(z,x),(x,z),(z,y))
 if len(w)==1:return imgs[mode][w[0]]
 k=next(i for i in range(1,len(w)) if lyndon(w[i:]))
 return bracket(LB(w[:k],mode),LB(w[k:],mode))

def mobius(n):return int(sp.mobius(n))
def divs(n):return sp.divisors(n)
def char(n,g):
 def tr(d):
  if g==0:return 2
  if g==1:return 2 if d%2==0 else 0
  return 2 if d%3==0 else -1
 return sum(mobius(d)*tr(d)**(n//d) for d in divs(n))//n

def d_odd(N):
 a=[0]*(N+1);a[0]=1
 for n in range(1,N+1):a[n]=sum(a[n-k] for k in range(3,n+1,2))
 ds=[0]*(N+1);p=[1]+[0]*N
 for n in range(1,N+1):
  ds[n]=a[n]-p[n]
  for j in range(ds[n]):
   for k in range(n,N+1):p[k]+=p[k-n]
 return ds

def select_mod(cols,p=1000003):
 piv={};sel=[]
 for j,v in enumerate(cols):
  v=[int(a)%p for a in v]
  while any(v):
   k=next(i for i,a in enumerate(v) if a)
   if k in piv:
    q=v[k];v=[(a-q*b)%p for a,b in zip(v,piv[k])]
   else:
    q=pow(v[k],-1,p);piv[k]=[(a*q)%p for a in v];sel.append(j);break
 return sel

def matrix_null(cols):
 if not cols:return [],0
 dm=DomainMatrix.from_Matrix(sp.Matrix.hstack(*[sp.Matrix(c) for c in cols])).convert_to(sp.QQ)
 ker=dm.nullspace().to_Matrix()
 return [list(ker.row(j)) for j in range(ker.rows)],dm.shape[1]-ker.rows

def normalize(v):
 den=sp.ilcm(*[a.q for a in v]) if len(v)>1 else v[0].q
 q=[int(a*den) for a in v];g=0
 for a in q:g=gcd(g,abs(a))
 if g:q=[a//g for a in q]
 if next((a for a in q if a),1)<0:q=[-a for a in q]
 return q

def lincomb(v,b):
 p={}
 for c,q in zip(v,b):
  if c:p=add(p,q,int(c))
 return p

def substitute(p,a,b):
 r={}
 for w,c in p.items():
  t={():c}
  for i in w:t=mul(t,(a,b)[i])
  r=add(r,t)
 return r

def special(p):return add(bracket(x,p),bracket(add(x,y),substitute(p,z,y)),-1)

def coordinates(p):
 if not p:return {}
 n=len(next(iter(p)));r=p.copy();out={}
 for w in words(n):
  c=r.get(w,0)
  if c:out[''.join('x' if i==0 else 'y' for i in w)]=int(c);r=add(r,LB(w),-c)
 assert not r,('not Lie',r)
 return out

def test_two_three(p):
 assert not add(p,substitute(p,y,x))
 assert not add(add(p,substitute(p,y,z)),substitute(p,z,x))

def main():
 rows=[];witnesses={};d=d_odd(20)
 for n in range(1,13):
  start=time.time();W=words(n);basis=[LB(w) for w in W]
  # (1-s)(2-r-r^2) is six times the projector to s-odd standard vectors.
  proj=[]
  for w in W:
   q=lincomb([2,-2,-1,-1,1,1],[LB(w,i) for i in range(6)]);proj.append(q)
  cols=[[q.get(w,0) for w in W] for q in proj]
  sel=select_mod(cols);P=[proj[i] for i in sel]
  ms=(char(n,0)-char(n,2))//3
  assert len(P)==ms
  if n<=8:
   for p in P:test_two_three(p)
  # Evaluate the same projector at (z,y) using the six S3 substitutions;
  # this avoids exponentially expanding each already expanded polynomial.
  Qzy=[lincomb([1,-1,-2,1,-1,2],[LB(W[i],j) for j in range(6)]) for i in sel]
  J=[add(bracket(x,p),bracket(add(x,y),q),-1) for p,q in zip(P,Qzy)]
  colsJ=[[q.get(w,0) for w in words(n+1)] for q in J]
  ker,rankJ=matrix_null(colsJ)
  if n>=2:
   dimout=2*char(n,0)-char(n+1,0)
   diminv=ms-(char(n+1,0)+3*char(n+1,1)+2*char(n+1,2))//6
  else:dimout=diminv=0
  # At weight one x-y satisfies cabling but represents an inner derivation; normalized f in the commutator subgroup removes this line.
  assert n==1 or len(ker)==diminv,(n,len(ker),diminv)
  row={'weight':n,'free_lie':len(W),'two_three_only':ms,'normalized_two_three':ms if n>=2 else 0,'outer_special':dimout,'S3_invariant_outer_special':diminv,'odd_free_d':d[n],'special_rank_on_two_three':rankJ}
  rows.append(row);print(row,'seconds',round(time.time()-start,3),flush=True)
  if n in (4,7):
   two=[normalize([sp.Rational(1 if i==j else 0) for i in range(len(P))]) for j in range(len(P))]
   extra=[]
   for v in ker:
    v=normalize(v);p=lincomb(v,P);test_two_three(p);assert not special(p)
    extra.append({'lyndon_coefficients':coordinates(p),'associative_coefficients':{''.join('x' if i==0 else 'y' for i in w):int(c) for w,c in sorted(p.items())}})
   witnesses[str(n)]={'two_three_basis':[coordinates(p) for p in P],'special_basis':extra}
 a=witnesses['7']['special_basis'][0]['lyndon_coefficients'];b=witnesses['7']['special_basis'][1]['lyndon_coefficients']
 c={k:7*a.get(k,0)-2*b.get(k,0) for k in a.keys()|b.keys()};c={k:v for k,v in c.items() if v};g=0
 for v in c.values():g=gcd(g,abs(v))
 c={k:-v//g for k,v in sorted(c.items())};p={}
 for w,k in c.items():p=add(p,LB(tuple(0 if t=='x' else 1 for t in w)),k)
 test_two_three(p);assert not special(p)
 witnesses['7']['simple_witness']={'lyndon_coefficients':c,'associative_coefficients':{''.join('x' if t==0 else 'y' for t in w):v for w,v in p.items()}}
 q={}
 for w,k in witnesses['4']['two_three_basis'][0].items():q=add(q,LB(tuple(0 if t=='x' else 1 for t in w)),-k)
 witnesses['4']['special_obstruction']={'witness':coordinates(q),'special':coordinates(special(q))}
 with (OUT/'graded_dimensions.csv').open('w') as f:
  wr=csv.DictWriter(f,fieldnames=list(rows[0]));wr.writeheader();wr.writerows(rows)
 (OUT/'graded_witnesses.json').write_text(json.dumps(witnesses,indent=2))
 (OUT/'graded_odd_dimensions.json').write_text(json.dumps({'weights':list(range(1,21)),'d':d[1:]},indent=2))
 print('All exact identities and independent character dimension checks passed.')

if __name__ == "__main__":
 main()
