from fractions import Fraction as F
from pathlib import Path
import sys,json
sys.path.insert(0,'work/code')
from harmonic_tripod_obstruction_search import vu,hilbert,fourth_roots_units
from sympy import nthroot_mod
d=json.loads(Path('work/code/harmonic_twist_repair_data.json').read_text())
cs=(F(0),F(1),F(1,2))
a=tuple(F(x) for x in d['a'])
B=[[(c-ck)/ak for ck,ak in zip(cs,a) if ck!=c] for c in cs]
special={}
nonzero=[]
for ps,Ts in d['local_T'].items():
 p=int(ps);T=F(Ts)
 for i,(c,ai) in enumerate(zip(cs,a)):
  w=(T-c)/ai;v,un=vu(w,p,32 if p==2 else p)
  assert v%4==0
  if p in (2,3,191):
   if p==2:
    roots=fourth_roots_units(w,p)
   else:
    roots=[F(int(z))*F(p)**(v//4) for z in nthroot_mod(un,4,p,all_roots=True)]
   values=[([str(z),[hilbert(z,b,p) for b in B[i]]]) for z in roots]
   special[(p,i)]=values
  else:
   values=[['unramified', [hilbert(F(p)**(v//4),b,p) for b in B[i]]]]
   if any(values[0][1]):nonzero.append((p,i,v//4,values))
print('SPECIAL ROOT OPTIONS',special)
print('NONZERO UNRAMIFIED ROOT SYMBOLS',nonzero)
print('ALL',len(d['local_T']),'LOCAL WITNESSES CHECKED')

