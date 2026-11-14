#!/usr/bin/env python3
"""Exact Sylow-two comparison on both remaining arithmetic orbit12 blocks."""
from pathlib import Path
from itertools import combinations
import numpy as np
import json,hashlib,time

OUT=Path(__file__).resolve().parent;start=time.time()
path=OUT/'d_arithmetic_A4_twisted.json';D=json.loads(path.read_text())
T=np.array(D['Q_multiplication'],dtype=np.int16);A4=D['A4_states']
MUL=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
FB=np.array([0,1,3,2],dtype=np.uint8)
def mm(a,b):
 out=np.zeros((a.shape[0],b.shape[1]),dtype=np.uint8)
 for j in range(a.shape[1]):out^=MUL[a[:,j,None],b[j,None,:]]
 return out
def rr(a):
 a=np.array(a,dtype=np.uint8,copy=True);p=[];row=0
 for c in range(a.shape[1]):
  at=np.flatnonzero(a[row:,c])
  if not len(at):continue
  j=row+int(at[0]);a[[row,j]]=a[[j,row]];a[row]=MUL[FB[a[row,c]],a[row]]
  v=a[:,c].copy();v[row]=0;a^=MUL[v[:,None],a[row,None,:]]
  p.append(c);row+=1
  if row==len(a):break
 return a,p
def rank(a):return len(rr(a)[1])
def inv(a):
 n=len(a);r,p=rr(np.column_stack([a,np.eye(n,dtype=np.uint8)]))
 assert p[:n]==list(range(n));return r[:,n:]
def quotient(c):
 r,p=rr(c.T);free=[j for j in range(c.shape[0]) if j not in p]
 q=np.zeros((len(free),c.shape[0]),dtype=np.uint8);q[np.arange(len(free)),free]=1
 q[:,p]=r[:len(p),free].T
 j=np.zeros((c.shape[0],len(free)),dtype=np.uint8);j[free,np.arange(len(free))]=1
 assert not np.any(mm(q,c));assert np.array_equal(mm(q,j),np.eye(len(free),dtype=np.uint8))
 return q,j
def right_inverse(a):
 p=rr(a)[1];assert len(p)==len(a)
 b=np.zeros((a.shape[1],len(a)),dtype=np.uint8);b[p]=inv(a[:,p]);return b
def generated(gens):
 todo=[0];seen={0}
 for g in todo:
  for h in gens:
   k=int(T[g,h])
   if k not in seen:seen.add(k);todo.append(k)
 return sorted(seen)
def order(g):
 h=0
 for k in range(1,100):
  h=int(T[h,g])
  if h==0:return k
 raise AssertionError(g)
V4=[g for g in A4 if order(g)<=2];assert len(V4)==4
rows=[]
for B in D['character_blocks']:
 if len(B['orbit'])!=12:continue
 acts={a['q_state']:(np.array(a['columns'],dtype=np.uint8).T,a['flip']) for a in B['all_stabilizer_actions']}
 H0=sorted(g for g,(m,f) in acts.items() if not f);H=sorted(acts)
 assert len(H0)==24 and len(H)==48
 P=next(generated([g,h]) for g,h in combinations(H0,2) if len(generated([g,h]))==8)
 assert set(P)<=set(H0) and set(V4)<=set(P)
 tau=next(g for g in P if g not in A4)
 F=np.array(B['regular_A4_basis_columns'],dtype=np.uint8).T
 C=np.array(B['cusp_columns'],dtype=np.uint8).T
 smallC=np.array(B['target_cusp_columns'],dtype=np.uint8).T
 theta=np.array(B['regular_projection_columns'],dtype=np.uint8).T
 qc0,jc0=quotient(C);qc=mm(qc0,F);jc=mm(inv(F),jc0)
 qs,js=quotient(smallC)
 jtheta=right_inverse(theta)
 Creg=mm(inv(F),C);jC=right_inverse(Creg.T).T
 jCs=right_inverse(smallC.T).T
 modules={n:{} for n in ['source','cusp','compact','target','target_cusp','target_compact']}
 for g in P:
  M=acts[g][0]
  ms=mm(mm(theta,M),jtheta)
  assert np.array_equal(mm(theta,M),mm(ms,theta))
  mods={
    'source':M,
    'cusp':mm(mm(jC,M),Creg),
    'compact':mm(mm(qc,M),jc),
    'target':ms,
    'target_cusp':mm(mm(jCs,ms),smallC),
    'target_compact':mm(mm(qs,ms),js)}
  assert np.array_equal(mm(M,Creg),mm(Creg,mods['cusp']))
  assert np.array_equal(mm(qc,M),mm(mods['compact'],qc))
  for n,m in mods.items():modules[n][g]=m
 # Source restriction to Sylow2; target restriction to its actual C2 image.
 norms={};details={}
 for n,mats in modules.items():
  index=P if not n.startswith('target') else [0,tau]
  total=np.zeros_like(mats[0])
  for g in index:total^=mats[g]
  d=len(total);r=rank(total);expected=d//len(index)
  norms[n]={'dimension_F4':d,'group_order':len(index),'norm_rank':r,
            'free_rank_required':expected,'projective':r==expected}
  # A regular projective module has this norm rank, and equality of the
  # norm rank with dim/|P| proves all its projective summands exhaust it.
  details[n]={'all_sylow_action_columns':{str(g):m.T.tolist() for g,m in mats.items()},
              'norm_columns':total.T.tolist()}
 rec={'character':B['character'],'oriented_stabilizer_order':24,'unordered_stabilizer_order':48,
      'Sylow2_states':P,'Sylow2_orders':[order(g) for g in P],
      'target_C2_lift':tau,'norms':norms,'matrices':details}
 rows.append(rec)
 print(json.dumps({k:v for k,v in rec.items() if k!='matrices'}),flush=True)
out={'summary':{'status':'PASS','actual_arithmetic_base_order':46656,
                'actual_target_order':3888,'two_orbit12_blocks_checked':True,
                'elapsed_seconds':time.time()-start},'blocks':rows,
     'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
(OUT/'d_orbit12_projectivity.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
print(json.dumps(out['summary'],indent=2),flush=True)
