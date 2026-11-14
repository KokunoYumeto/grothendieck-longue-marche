#!/usr/bin/env python3
"""Exact invariant wedge comparison on the four actual character blocks.

Hermitian matrices realize the Delta-invariant exterior module.  All maps
are taken from the marked order46656 graph computed in the companion.
The arithmetic cusp error itself is not evaluated by this program.
"""
from pathlib import Path
from collections import deque
import json,time,hashlib
import numpy as np
OUT=Path(__file__).resolve().parent;start=time.time()
path=OUT/'d_arithmetic_A4_twisted.json';D=json.loads(path.read_text())
A=json.loads((OUT/'d_arithmetic_affine_base.json').read_text())
T=np.array(D['Q_multiplication'],dtype=np.int16);K=D['A4_states'];to_star=A['Q_to_linear_image']
MUL=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
FROB=np.array([0,1,3,2],dtype=np.uint8);INV=FROB
def mm(a,b):
 out=np.zeros((len(a),b.shape[1]),dtype=np.uint8)
 for k in range(a.shape[1]):out^=MUL[a[:,k,None],b[k,None,:]]
 return out
def echelon(a):
 a=np.array(a,dtype=np.uint8,copy=True);row=0;piv=[]
 for c in range(a.shape[1]):
  ids=np.flatnonzero(a[row:,c])
  if not len(ids):continue
  j=row+int(ids[0]);a[[row,j]]=a[[j,row]];a[row]=MUL[INV[a[row,c]],a[row]]
  f=a[:,c].copy();f[row]=0;a^=MUL[f[:,None],a[row,None,:]];piv.append(c);row+=1
  if row==len(a):break
 return a,piv
def outer(u,v):return MUL[u[:,None],FROB[v[None,:]]]
def elementary_image(M,i,j,z=1):
 if i==j:return outer(M[:,i],M[:,i])
 return MUL[z,outer(M[:,i],M[:,j])]^MUL[FROB[z],outer(M[:,j],M[:,i])]
def pack(H):
 n=len(H);assert np.array_equal(H,FROB[H.T]);assert np.all(H.diagonal()<2)
 values=list(map(int,H.diagonal()))
 for i in range(n):
  for j in range(i+1,n):values.extend([int(H[i,j])&1,int(H[i,j])>>1])
 return sum(v<<i for i,v in enumerate(values))
def combine(cols,v):
 out=0
 while v:
  b=v&-v;out^=cols[b.bit_length()-1];v^=b
 return out
def solve_columns(cols):
 bas={};null=[];ind=[]
 for j,v in enumerate(cols):
  w=1<<j
  while v:
   p=v.bit_length()-1
   if p not in bas:bas[p]=(v,w);ind.append(j);break
   a,b=bas[p];v^=a;w^=b
  if not v:null.append(w)
 def solve(v):
  w=0
  for p in sorted(bas,reverse=True):
   if v>>p&1:a,b=bas[p];v^=a;w^=b
  assert not v
  return w
 return solve,len(bas),null,ind
def quotient(cols,n):
 bas={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in bas:bas[p]=v;break
   v^=bas[p]
 free=[j for j in range(n) if j not in bas]
 def q(v):
  for p in sorted(bas,reverse=True):
   if v>>p&1:v^=bas[p]
  return sum(((v>>j)&1)<<i for i,j in enumerate(free))
 return q,free

n=96
perms=[[12*j+K.index(int(T[g,h])) for j in range(8) for h in K] for g in K]
covered=set();groups=[];reps=[];lookup={}
for i in range(n):
 for j in range(i,n):
  if (i,j) in covered:continue
  orbit={};swap=False
  for P in perms:
   a,b=P[i],P[j];p=(min(a,b),max(a,b));flip=a>b
   if p in orbit and orbit[p]!=flip:swap=True
   orbit.setdefault(p,flip)
  covered.update(orbit)
  kind='diag' if i==j else 'trace' if swap else 'field'
  index=len(groups);off=len(reps)
  if kind=='diag':reps.append((i,j,1))
  elif kind=='trace':reps.append((i,j,2))
  else:reps.extend([(i,j,1),(i,j,2)])
  groups.append({'kind':kind,'representative':(i,j),'offset':off,'orbit':[(a,b,int(f)) for (a,b),f in sorted(orbit.items())]})
  for (a,b),f in orbit.items():lookup[a,b]=(index,f)
assert len(reps)==768 and len(covered)==n*(n+1)//2
coords=[(i,j,*lookup[i,j]) for i in range(n) for j in range(i,n)]
ii=np.array([x[0] for x in coords]);jj=np.array([x[1] for x in coords]);gg=np.array([x[2] for x in coords]);ff=np.array([x[3] for x in coords],dtype=bool)
def project(H):
 values=H[ii,jj].copy();values[ff]=FROB[values[ff]]
 totals=np.zeros(len(groups),dtype=np.uint8);np.bitwise_xor.at(totals,gg,values)
 out=0
 for g,a in zip(groups,totals):
  a=int(a);k=g['offset']
  if g['kind']=='diag':assert a<2;out|=a<<k
  elif g['kind']=='trace':out|=(a>>1)<<k
  else:out|=(a&1)<<k;out|=(a>>1)<<(k+1)
 return out
Id=np.eye(n,dtype=np.uint8)
for k,(i,j,z) in enumerate(reps):assert project(elementary_image(Id,i,j,z))==1<<k
# Exact group orbit formulas provide the coinvariant projection and norm.
def norm_matrix(k):
 i,j,z=reps[k];H=np.zeros((n,n),dtype=np.uint8)
 for P in perms:
  a,b=P[i],P[j]
  H[a,b]^=z
  if i!=j:H[b,a]^=FROB[z]
 return H
N=[norm_matrix(k) for k in range(768)]
assert solve_columns([pack(h) for h in N])[1]==768

records=[]
for bi,B in enumerate(D['character_blocks']):
 act={a['q_state']:a for a in B['all_stabilizer_actions']}
 cosets={}
 for q in act:cosets.setdefault(to_star[q],q)
 assert len(cosets) in [4,6]
 leaders=sorted(cosets.values());star_to_leader={to_star[q]:q for q in leaders}
 actions={}
 for q in leaders:
  a=act[q];M=np.array(a['columns'],dtype=np.uint8).T
  cols=[project(elementary_image(M,i,j,int(FROB[z]) if a['flip'] else z)) for i,j,z in reps]
  assert solve_columns(cols)[1]==768
  actions[q]=cols
 assert actions[0]==[1<<i for i in range(768)]
 # Check the entire quotient multiplication table, retaining every map.
 for q in leaders:
  for r in leaders:
   w=star_to_leader[to_star[int(T[q,r])]]
   assert [combine(actions[q],v) for v in actions[r]]==actions[w]
 theta=np.array(B['regular_projection_columns'],dtype=np.uint8).T
 target=[pack(elementary_image(theta,i,j,z)) for i,j,z in reps]
 ksolve,trank,kbasis,_=solve_columns(target);assert trank==64 and len(kbasis)==704
 ks,krank,_,_=solve_columns(kbasis);assert krank==704
 kactions={q:[ks(combine(cols,v)) for v in kbasis] for q,cols in actions.items()}
 qfull,fre=quotient([v^(1<<j) for cols in actions.values() for j,v in enumerate(cols)],768)
 qker,kfre=quotient([v^(1<<j) for cols in kactions.values() for j,v in enumerate(cols)],704)
 normcols=[];knormcols=[]
 for j in range(768):
  v=0
  for cols in actions.values():v^=cols[j]
  normcols.append(v)
 for v in kbasis:knormcols.append(combine(normcols,v))
 normrank=solve_columns(normcols)[1];knormrank=solve_columns(knormcols)[1]
 assert all(qfull(v^(1<<j))==0 for cols in actions.values() for j,v in enumerate(cols))
 # Literal compactification of the marked cusp submodule.
 F=np.array(B['regular_A4_basis_columns'],dtype=np.uint8).T
 C=np.array(B['cusp_columns'],dtype=np.uint8)
 rr,piv=echelon(C);assert len(piv)==48
 free=[i for i in range(96) if i not in piv]
 compact=np.zeros((48,96),dtype=np.uint8);compact[np.arange(48),free]=1
 compact[:,piv]=rr[:,free].T
 assert not np.any(mm(compact,C.T))
 compact=mm(compact,F)
 compact_norm_A4=[]
 for H in N:
  compact_norm_A4.append(pack(mm(mm(compact,H),FROB[compact.T])))
 compact_full_norm=[combine(compact_norm_A4,v) for v in normcols]
 compact_ker_norm=[combine(compact_norm_A4,v) for v in knormcols]
 cnrank=solve_columns(compact_full_norm)[1];kcnrank=solve_columns(compact_ker_norm)[1]
 record={'character':B['character'],'orbit_size':len(B['orbit']),
         'A4_coinvariant_dimension':768,'A4_norm_rank':768,
         'projection_to_small_exterior_rank':64,'kernel_after_A4_coinvariants_dimension':704,
         'source_G_coinvariant_dimension':len(fre),'residual_G_coinvariant_dimension':len(kfre),
         'source_full_norm_rank':normrank,'residual_full_norm_rank':knormrank,
         'source_compact_norm_rank':cnrank,'residual_compact_norm_rank':kcnrank,
         'residual_full_norm_kernel_dimension':len(kfre)-knormrank,
         'residual_compact_norm_kernel_dimension':len(kfre)-kcnrank,
         'stabilizer_quotient_order':len(leaders),'quotient_lifts':leaders,
         'all_quotient_action_columns':{str(q):[hex(x) for x in cols] for q,cols in actions.items()},
         'source_to_small_columns':[hex(x) for x in target],
         'kernel_basis':[hex(x) for x in kbasis],
         'source_coinvariant_representatives':fre,'residual_coinvariant_representatives':kfre,
         'source_norm_columns':[hex(x) for x in normcols],
         'compact_A4_norm_columns':[hex(x) for x in compact_norm_A4]}
 records.append(record)
 print(json.dumps({k:v for k,v in record.items() if not isinstance(v,(dict,list)) or k in ['character','orbit_size']}),flush=True)

result={'summary':{'status':'PASS','actual_source_base_order':46656,'target_base_order':3888,
                   'whole_residual_dimension':366080,'all_four_pair_orbits_checked':True,
                   'source_coinvariant_dimension':sum(r['source_G_coinvariant_dimension'] for r in records),
                   'residual_coinvariant_dimension':sum(r['residual_G_coinvariant_dimension'] for r in records),
                   'source_full_norm_rank':sum(r['source_full_norm_rank'] for r in records),
                   'residual_full_norm_rank':sum(r['residual_full_norm_rank'] for r in records),
                   'source_compact_norm_rank':sum(r['source_compact_norm_rank'] for r in records),
                   'residual_compact_norm_rank':sum(r['residual_compact_norm_rank'] for r in records),
                   'arithmetic_boundary_solved':False,'elapsed_seconds':time.time()-start},
        'A4_coinvariant_orbits':groups,'A4_coinvariant_representatives':reps,
        'blocks':records,'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
(OUT/'d_arithmetic_A4_central.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
