#!/usr/bin/env python3
"""Which explicit Hesse-line Heisenberg maps detect the actual remaining space?

Only geometric abelian characters are used here, obtained from the actual
unit divisors and the A7 lattice comparison. No central path value is inferred.
"""
from pathlib import Path
import importlib.util,json,contextlib,io,itertools
import numpy as np
import sympy as sp
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
spec=importlib.util.spec_from_file_location('gauge',HERE/'a_ihara_gauge.py')
g=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):spec.loader.exec_module(g)
raw=json.loads((HERE/'a_k_lattice.out').read_text())
Psi=sp.Matrix(raw['Weil_graph_matrix'])
B=sp.Matrix(json.loads((HERE/'a_ihara_lattice.json').read_text())['A7_to_Schreier_basis'])
mod9=json.loads((HERE/'a_ihara_mod9_compare.json').read_text())
J=np.array(mod9['Johnson_variations'],dtype=np.int64)
H=np.array(mod9['metabelian_variations'],dtype=np.int64)
blind=J@g.kernel(H)%3
names=['O','P','Q','A','Abar','B','Bbar','C','Cbar']
u0=['O','C','Cbar'];v0=['Q','Bbar','B'];inf=['P','Abar','A']

def divline(k,l):
 d={a:0 for a in names};d[u0[(l-k)%3]]+=1;d[v0[l]]+=1;d[inf[k]]+=1
 for a in ['P','A','Abar']:d[a]-=1
 return sp.Matrix([[d[a] for a in names[1:]]])

def character(d):
 proper=d*Psi/3
 assert all(a.q==1 for a in proper)
 return np.array((d.row_join(proper)*B.inv()).tolist()[0],dtype=np.int64)%3

def form(a,b):return np.array([a[i]*b[j]-a[j]*b[i] for i,j in zip(*f.UP)],dtype=np.int64)%3
out=[];stack=[]
for k in range(3):
 for l1,l2 in itertools.combinations(range(3),2):
  d1,d2=divline(k,l1),divline(k,l2)
  a=character(d1-d2);b=character(-d2);om=form(a,b)
  effect=np.einsum('i,ijk->jk',om,blind.reshape(45,10,-1))%3
  all_effect=np.einsum('i,ijk->jk',om,J.reshape(45,10,-1))%3
  r=f.rank(effect)
  print('Line pencil k,l1,l2',k,l1,l2,'invisible rank',r,'total rank',f.rank(all_effect))
  out.append({'k':k,'l1':l1,'l2':l2,'alpha':a.tolist(),'beta':b.tolist(),'omega':om.tolist(),
              'invisible_effect':effect.tolist(),'all_effect':all_effect.tolist()})
  stack.append(effect)
print('All line pencils invisible detection rank:',f.rank(np.vstack(stack)))
(HERE/'a_heisenberg_detectors.json').write_text(json.dumps(out,indent=2)+'\n')
proper=np.array(f.TATE_QUOTIENT,dtype=np.int64)%3
om=form(proper[0],proper[1])
effect=np.einsum('i,ijk->jk',om,blind.reshape(45,10,-1))%3
print('Filling all but O, proper Heisenberg detector rank:',f.rank(effect))
print('Total Johnson output span rank:',f.rank(J.reshape(45,-1)))
print('Invisible Johnson output span rank:',f.rank(blind.reshape(45,-1)))
# Pair arbitrary coordinate characters with proper quotient characters.
for tt in range(2):
 eff=[]
 for ii in range(10):
  a=np.eye(10,dtype=np.int64)[ii];om=form(a,proper[tt])
  eff.append(np.einsum('i,ijk->jk',om,blind.reshape(45,10,-1))%3)
 print('Mixed proper character',tt,'all detector rank',f.rank(np.vstack(eff)))
Psi_np=np.array(Psi.tolist(),dtype=np.int64)%3
principal_mod3=g.kernel(Psi_np.T)
unitrows=[]
for ii in range(8):
 d=sp.zeros(1,8);d[ii]=3;unitrows.append(character(d))
for col in principal_mod3.T:unitrows.append(character(sp.Matrix([col.tolist()])))
unitrows=np.stack(unitrows,axis=0)
RR,piv=g.rref(unitrows.T)
units=unitrows[piv,:]
assert units.shape[0]==8
uniteffects=[]
for aa,bb in itertools.combinations(units,2):
 om=form(aa,bb);uniteffects.append(np.einsum('i,ijk->jk',om,blind.reshape(45,10,-1))%3)
print('All geometric unit-pair detector rank:',f.rank(np.vstack(uniteffects)))
print('Unit character rank:',f.rank(units))
# Miller f_(3,Q), 3Q=d, has boundary character -e_d. Its two proper
# coordinates can vary with the nine choices of Q but do not affect these
# pure-toric Johnson outputs. Test the simplest unit partners u and v.
coord_units={'u':sp.Matrix([[-1,0,-1,-1,0,0,1,1]]),
             'v':sp.Matrix([[-1,1,-1,-1,1,1,0,0]])}
allm=[]
for dd,name in enumerate(names[1:]):
 ar=np.zeros(10,dtype=np.int64);ar[dd]=2
 alpha=np.array((sp.Matrix([ar.tolist()])*B.inv()).tolist()[0],dtype=np.int64)%3
 for un,drow in coord_units.items():
  beta=character(drow);om=form(alpha,beta)
  effect=np.einsum('i,ijk->jk',om,blind.reshape(45,10,-1))%3
  rr=f.rank(effect)
  if rr:print('Miller 3Q=',name,'with unit',un,'detects rank',rr)
  allm.append(effect)
print('All tested Miller/coordinate unit detector rank:',f.rank(np.vstack(allm)))
miller_pairs=[];picked=[];running=np.zeros((0,blind.shape[1]),dtype=np.int64)
for dd,name in enumerate(names[1:]):
 ar=np.zeros(10,dtype=np.int64);ar[dd]=2
 alpha=np.array((sp.Matrix([ar.tolist()])*B.inv()).tolist()[0],dtype=np.int64)%3
 for uu,beta in enumerate(units):
  om=form(alpha,beta);effect=np.einsum('i,ijk->jk',om,blind.reshape(45,10,-1))%3
  new=np.vstack((running,effect))
  if f.rank(new)>f.rank(running):
   aval=np.array((sp.Matrix([beta.tolist()])*B).tolist()[0],dtype=np.int64)%3
   picked.append({'Miller_3Q':name,'unit_row_A7_mod3':aval.tolist(),'unit_row_Schreier_mod3':beta.tolist(),
                  'effect':effect.tolist()})
   print('Chosen Miller/unit detector:',name,aval.tolist(),'combined rank',f.rank(new))
   running=new
print('All Miller/arbitrary unit detector rank:',f.rank(running))
(HERE/'a_miller_detector_pairs.json').write_text(json.dumps(picked,indent=2)+'\n')
print('PASS: no central cochain/origin value has been assumed.')
