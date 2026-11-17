"""Exploratory numerical discovery of seven-point tetrahedral monodromy.
The braid words are checked algebraically, but numerical path extraction alone
is NOT a certified proof of the induced topological homomorphism.
"""
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
import json,itertools,math,sys
import sympy as sp
HERE=Path(__file__).resolve().parent
u=sp.symbols('u')
pts=[u,-u,1/u,(u+sp.I)/(u-sp.I),-1/u,-(u+sp.I)/(u-sp.I),(u-sp.I)/(u+sp.I),-(u-sp.I)/(u+sp.I),(u+1)/(-sp.I*u+sp.I),(u+1)/(sp.I*u-sp.I),(u-1)/(sp.I*u+sp.I),(u-1)/(-sp.I*u-sp.I)]
S=[0,1,2,3,5,8,11]
# First S point infinity, second zero, third one.
f=[sp.cancel((pts[i]-pts[1])/(pts[i]-pts[0])*(pts[2]-pts[0])/(pts[2]-pts[1])) for i in S[1:]]
rot=1+0.317j
funcs=[sp.lambdify(u,v,'numpy') for v in f]
def config(v):return np.array([complex(q(v)) for q in funcs])*rot
base=3.71+2.37j
roots=sorted([0,1,-1,1j,-1j]+list(np.roots([1,0,0,0,14,0,0,0,1])),key=lambda z:math.atan2((z-base).imag,(z-base).real))
def braid_segment(a,b,steps=1500):
 def z(t):return config(a+(b-a)*t)
 grid=np.linspace(0,1,steps+1)
 values=np.array([z(t) for t in grid]);events=[]
 for i,j in itertools.combinations(range(6),2):
  v=values[:,i].real-values[:,j].real
  for k in np.where(v[:-1]*v[1:]<0)[0]:
   rt=brentq(lambda t:(z(t)[i]-z(t)[j]).real,grid[k],grid[k+1],xtol=1e-13)
   delta=(z(min(rt+1e-7,1))[i]-z(min(rt+1e-7,1))[j]-(z(max(rt-1e-7,0))[i]-z(max(rt-1e-7,0))[j])).real
   sep=(z(rt)[i]-z(rt)[j]).imag
   assert abs(sep)>1e-9
   sign=1 if delta*sep<0 else -1
   events.append((rt,i,j,sign))
 events.sort();order=list(np.argsort(z(0).real));word=[]
 for rt,i,j,sign in events:
  a0,b0=order.index(i),order.index(j)
  assert abs(a0-b0)==1,(rt,i,j,a0,b0)
  word.append(sign*(min(a0,b0)+1));order[a0],order[b0]=order[b0],order[a0]
 assert order==list(np.argsort(z(1).real))
 return word

def reduce(w):
 r=[]
 for a in w:
  if r and r[-1]==-a:r.pop()
  else:r.append(a)
 return tuple(r)
def inverse(w):return tuple(-a for a in reversed(w))
def mul(*ws):return reduce(itertools.chain.from_iterable(ws))
def action(w):
 images=[(i+1,) for i in range(6)]
 for a in w:
  i=abs(a)-1;v,w=images[i:i+2]
  images[i:i+2]=[mul(v,w,inverse(v)),v] if a>0 else [w,mul(inverse(w),v,w)]
 return images

def main():
 out=[]
 for k,e in enumerate(roots):
  # Rational square surrounding one algebraic exceptional point.
  c=round(e.real,5)+1j*round(e.imag,5);eps=0.012
  corners=[c+eps*(1+1j),c+eps*(-1+1j),c+eps*(-1-1j),c+eps*(1-1j),c+eps*(1+1j)]
  path=[base]+corners+[base]
  w=mul(*(braid_segment(a,b) for a,b in zip(path,path[1:])))
  a=action(w)
  assert a!=[(i+1,) for i in range(6)]
  out.append({'root':[float(e.real),float(e.imag)],'path':[[float(z.real),float(z.imag)] for z in path],'braid':list(w),'action':[list(v) for v in a]})
  print(k,'root',e,'braid length',len(w),'action length',sum(map(len,a)),flush=True)
 (HERE/'rigid7_monodromy_probe.json').write_text(json.dumps({'warning':__doc__,'labels':[i+1 for i in S],'normalization':[1,2,3],'functions':[str(v) for v in f],'rotation':[1,.317],'base':[base.real,base.imag],'loops':out},indent=2)+'\n')
 same=[];comm=[]
 for i,j in itertools.combinations(range(len(out)),2):
  a,b=out[i]['braid'],out[j]['braid']
  if action(a)==action(b):same.append((i,j))
  if action(a+b)==action(b+a):comm.append((i,j))
 print('Equal monodromy generators:',same)
 print('Commuting generator pairs:',comm)
 print('PROBE ONLY: braid extraction has not yet been certified by exact root isolation.')
if __name__=='__main__':main()
