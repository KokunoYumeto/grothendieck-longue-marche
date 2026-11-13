#!/usr/bin/env python3
"""Exact integer associative/Lyndon arithmetic.
Adapted from the supplied LM3b ab_lie.py; computations rerun here.
"""
from pathlib import Path
from functools import lru_cache
from itertools import product
from collections import defaultdict
from fractions import Fraction
import json, math, sys, time
import sympy as sp

def add(a,b,k=1):
 c=dict(a)
 for w,v in b.items():
  c[w]=c.get(w,0)+k*v
  if not c[w]: del c[w]
 return c

def mul(a,b):
 c=defaultdict(int)
 for u,x in a.items():
  for v,y in b.items():c[u+v]+=x*y
 return {u:v for u,v in c.items() if v}

def bracket(a,b):return add(mul(a,b),mul(b,a),-1)

def gen(i):return {(i,):1}

def is_lyndon(w):return all(w<w[i:] for i in range(1,len(w)))

@lru_cache(None)
def lyndon(r,n):return tuple(w for w in product(range(r),repeat=n) if is_lyndon(w))

@lru_cache(None)
def expand(w):
 if len(w)==1:return {w:1}
 for i in range(1,len(w)):
  if is_lyndon(w[i:]):return bracket(expand(w[:i]),expand(w[i:]))
 raise ValueError(w)

def coords(p,r,n):
 p=dict(p); ans={}
 for i,w in enumerate(lyndon(r,n)):
  v=p.get(w,0)
  if v:
   ans[i]=v;p=add(p,expand(w),-v)
 if p:raise ValueError(('not Lie',r,n,next(iter(p.items()))))
 return ans

def lincomb(v,basis):
 out={}
 for a,p in zip(v,basis):
  if a:out=add(out,p,a)
 return out

def derivative(D,p):
 out=defaultdict(int)
 for w,c in p.items():
  for j,i in enumerate(w):
   for v,a in D[i].items():out[w[:j]+v+w[j+1:]]+=c*a
 return {w:c for w,c in out.items() if c}

def dbracket(D,E):return tuple(add(derivative(D,e),derivative(E,d),-1) for d,e in zip(D,E))

