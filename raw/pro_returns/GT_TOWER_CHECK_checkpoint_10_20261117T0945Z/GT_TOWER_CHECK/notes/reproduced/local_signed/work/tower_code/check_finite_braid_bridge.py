#!/usr/bin/env python3
"""Faithful Artin checks for the explicit genus-one/B4 finite gauge.
The f-dependent cancellation is proved symbolically in the companion
LaTeX fragment; no finite tuple is asserted to lift to a full GT element.
"""
import json
from pathlib import Path
from functools import lru_cache
def red(w):
 o=[]
 for x in w:
  if o and o[-1]==-x:o.pop()
  else:o.append(x)
 return tuple(o)
def inv(w):return tuple(-x for x in reversed(w))
def mul(*ws):return red(x for w in ws for x in w)
def pw(w,n):return mul(*([w if n>=0 else inv(w)]*abs(n)))
def sub(w,im):return mul(*(im[x-1] if x>0 else inv(im[-x-1]) for x in w))
def gen(j):
 k=abs(j);a=[(i,) for i in range(1,5)]
 if j>0:a[k-1]=(k,k+1,-k);a[k]=(k,)
 else:a[k-1]=(k+1,);a[k]=(-k-1,k,k+1)
 return tuple(a)
@lru_cache(None)
def art(w):
 a=tuple((i,) for i in range(1,5))
 for j in w:a=tuple(sub(v,gen(j)) for v in a)
 return a
checks=[]
def check(name,l,r=()):
 assert art(tuple(l))==art(tuple(r)),name
 checks.append({'name':name,'left':l,'right':r});print('PASS',name,flush=True)
def comm(a,b):return mul(a,b,inv(a),inv(b))
a,b,d=(1,),(2,),(3,);V=pw((1,2,1),2);omega=pw((1,2,3),4);y3=(2,1,1,2)
check('V=a^2 y3',V,mul(pw(a,2),y3))
check('V=(ab)^3',V,pw((1,2),3))
check('boundary e=V^2=(ab)^6',pw(V,2),pw((1,2),6))
check('[a,V]=1',comm(a,V))
check('[b,V]=1',comm(b,V))
check('[a,d]=1',comm(a,d))
check('[a,y3]=1',comm(a,y3))
check('third mixed Schreier generator',mul(b,pw(a,2),inv(b)),mul(inv(a),pw(b,2),a))
check('(dV)^2=omega a^2',pw(mul(d,V),2),mul(omega,pw(a,2)))
for nm,x in [('a',a),('b',b),('d',d)]:check('[omega,'+nm+']=1',comm(omega,x))
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Exact faithful Artin verification of every discrete commutation and central-product word used in the direct quilt-to-braid gauge',
 'chain_generators':{'a':a,'b':b,'d':d},'V':V,'omega':omega,'third_Jucys_word':y3,
 'gauge':'a^(8c) V^(-4c)','checks':checks,'check_count':len(checks)},indent=2)+'\n')
print('PASS all12 discrete identities for the single explicit finite braid gauge',flush=True)
