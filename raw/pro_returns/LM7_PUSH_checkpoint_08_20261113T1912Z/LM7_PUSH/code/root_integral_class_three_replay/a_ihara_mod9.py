#!/usr/bin/env python3
"""Lift the actual finite symmetry/hexagon constraints from3 to9.

Only necessary GT equations are imposed.  Every allowed lift retains the
actual A7 linear action modulo9.  We solve simultaneously for the unknown
mod3 central parameters and all55 next digits, so no arbitrary mod3 choice
is represented as arithmetic or as known liftable.
"""
from pathlib import Path
from functools import cache
import importlib.util,json
import numpy as np
import sympy as sp
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('fermat',HERE/'de_fermat_schreier.py')
f=importlib.util.module_from_spec(spec);spec.loader.exec_module(f)
gt=json.loads((HERE/'a_ihara_gt_constraints.json').read_text())
comparison=json.loads((HERE/'a_ihara_lattice.json').read_text())
araw=json.loads((HERE/'a_k_lattice.out').read_text())
MOD=9;HALF=5
UP=f.UP

def zero():return np.zeros(10,dtype=np.int64),np.zeros(45,dtype=np.int64)
def mul(g,h):
 a,z=g;b,w=h
 return (a+b)%MOD,(z+w+HALF*(np.outer(a,b)-np.outer(b,a))[UP])%MOD
def inv(g):return tuple(-v%MOD for v in g)
def ext(A):
 return np.stack([(np.outer(A[:,i],A[:,j])-np.outer(A[:,j],A[:,i]))[UP]%MOD for i,j in zip(*UP)],axis=1)
def literal(word):
 out=zero()
 for l in f.schreier(word):
  a,z=zero();a[abs(l)-1]=1 if l>0 else -1
  out=mul(out,(a,z))
 return out
@cache
def action(q):
 w=f.section(q);vals=[literal(w+n+f.inverse_word(w)) for n in f.NWORDS]
 A=np.stack([a for a,z in vals],axis=1);J=np.stack([z for a,z in vals],axis=1)
 return A,J,ext(A)
def acted(g,A,J,W):
 a,z=g
 return A@a%MOD,(J@a+W@z)%MOD
def collect(word):
 out=zero();q=(0,0)
 for token in word:
  if isinstance(token,tuple):out=mul(out,acted(token,*action(q)));continue
  qn=f.step(q,token);a=f.EDGES[q,token] if token>0 else -f.EDGES[qn,-token]
  if a:
   b,z=zero();b[abs(a)-1]=1 if a>0 else -1;out=mul(out,(b,z))
  q=qn
 assert q==(0,0)
 return out
def mixedinv(w):return [inv(t) if isinstance(t,tuple) else -t for t in reversed(w)]
def images(fa,fz):
 g=(fa,fz);im={1:[1]*7,2:[inv(g)]+[2]*7+[g]}
 im[-1]=mixedinv(im[1]);im[-2]=mixedinv(im[2])
 vals=[collect([a for l in w for a in im[l]]) for w in f.NWORDS]
 return np.stack([a for a,z in vals],axis=1),np.stack([z for a,z in vals],axis=1)
def autom(im):
 vals=[]
 for w in f.NWORDS:
  ww=[]
  for a in w:ww+=im[a] if a>0 else f.inverse_word(im[-a])
  vals.append(literal(ww))
 A=np.stack([a for a,z in vals],axis=1);J=np.stack([z for a,z in vals],axis=1)
 return A,J,ext(A)
SA,SJ,SW=autom({1:[2],2:[1]})
RA,RJ,RW=autom({1:[2],2:[-2,-1]})
R2A=RA@RA%9;R2J=(RJ@RA+RW@RJ)%9;R2W=RW@RW%9
x3,y3,z3=literal([1]*3),literal([2]*3),literal([-2,-1]*3)
B=sp.Matrix(comparison['A7_to_Schreier_basis'])
target=np.array((B*sp.Matrix(araw['V_generator_matrices'][0])*B.inv()).tolist(),dtype=np.int64)%9

def equations(fa,fz):
 A,J=images(fa,fz);g=(fa,fz)
 s=mul(g,acted(g,SA,SJ,SW));h=zero()
 for a in (g,x3,acted(g,R2A,R2J,R2W),z3,acted(g,RA,RJ,RW),y3):h=mul(h,a)
 return np.concatenate(((A-target).reshape(-1),f.F_AB_DIV3@fa,s[0],h[0],s[1],h[1]))%9

def solve(A,b):
 A=A.copy()%3;aug=np.hstack((A,b[:,None]%3));r=0;p=[]
 for j in range(A.shape[1]):
  ids=np.flatnonzero(aug[r:,j])
  if not len(ids):continue
  i=r+int(ids[0]);aug[[r,i]]=aug[[i,r]];aug[r]=aug[r]*int(aug[r,j])%3
  coeff=aug[:,j].copy();coeff[r]=0;aug=(aug-coeff[:,None]*aug[r][None,:])%3
  p.append(j);r+=1
  if r==A.shape[0]:break
 if np.any(aug[r:,-1]):return None
 part=np.zeros(A.shape[1],dtype=np.int64)
 for rr,col in enumerate(p):part[col]=aug[rr,-1]
 free=[j for j in range(A.shape[1]) if j not in p];ker=np.zeros((A.shape[1],len(free)),dtype=np.int64)
 for kk,j in enumerate(free):
  ker[j,kk]=1
  for rr,col in enumerate(p):ker[col,kk]=-aug[rr,j]%3
 assert np.array_equal(A@part%3,b%3) and not np.any(A@ker%3)
 return part,ker,r

K=np.array(gt['central_kernel'],dtype=np.int64)
results=[]
for branch,(aa,zz) in enumerate(zip(gt['f_homology_representatives'],gt['f_central_representatives'])):
 fa=np.array(aa,dtype=np.int64);fz=np.array(zz,dtype=np.int64)
 base=equations(fa,fz);assert not np.any(base%3)
 nextcols=[]
 for j in range(55):
  a=fa.copy();z=fz.copy()
  if j<10:a[j]+=3
  else:z[j-10]+=3
  diff=(equations(a,z)-base)%9;assert not np.any(diff%3);nextcols.append(diff//3)
 nextmat=np.stack(nextcols,axis=1)
 oldcols=[]
 for col in K.T:
  diff=(equations(fa,fz+col)-base)%9;assert not np.any(diff%3);oldcols.append(diff//3)
 oldmat=np.stack(oldcols,axis=1)
 sol=solve(np.hstack((nextmat,oldmat)),-base//3)
 print('Branch',branch,'next-digit rank',f.rank(nextmat),'all-digit rank',f.rank(np.hstack((nextmat,oldmat))),
       'lift exists',sol is not None)
 if sol is None:continue
 pp,kk,rr=sol
 oldp=pp[55:];oldk=kk[55:,:]
 print('Allowed old central parameter dimension:',f.rank(oldk))
 fa0=fa%3;fz0=(fz+K@oldp)%3
 _,J0=f.generator_images(fa0,fz0,7)
 variations=[]
 for col in oldk.T:
  _,J=f.generator_images(fa0,(fz0+K@col)%3,7)
  variations.append((J-J0).reshape(-1)%3)
 Vm=np.stack(variations,axis=1) if variations else np.zeros((450,0),dtype=np.int64)
 print('Johnson variation surviving mod9 lift:',f.rank(Vm))
 results.append({'fa':fa0.tolist(),'fz':fz0.tolist(),'base_J':J0.tolist(),
                 'old_parameter_part':oldp.tolist(),'old_parameter_kernel':oldk.tolist(),
                 'Johnson_variations':Vm.tolist()})
assert results
allv=[np.array(r['Johnson_variations'],dtype=np.int64) for r in results]
base=np.array(results[0]['base_J'],dtype=np.int64)
allv += [(np.array(r['base_J'],dtype=np.int64)-base).reshape(-1,1)%3 for r in results]
print('Total Johnson uncertainty after mod9 lifting:',f.rank(np.hstack(allv)))
(HERE/'a_ihara_mod9.json').write_text(json.dumps(results,indent=2)+'\n')
print('PASS: necessary constraints retained, with all next-digit freedom.')
