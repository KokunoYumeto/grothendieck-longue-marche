#!/usr/bin/env python3
"""Actual projective compact kernel summands and their cross-wedge norms.

The source is the marked order46656 quotient.  This constructs literal
mod-two idempotents in the kernel of its map to the solved order3888 source.
The integral homology correction and arithmetic lift require the separate
proof; no guessed arithmetic matrix is input here.
"""
from pathlib import Path
from itertools import product,combinations
import json,hashlib,time
import numpy as np
OUT=Path(__file__).resolve().parent;start=time.time()
path=OUT/'d_arithmetic_A4_twisted.json';D=json.loads(path.read_text())
T=np.array(D['Q_multiplication'],dtype=np.int16);K=D['A4_states'];states=[tuple(x) for x in D['Q_states']]
MUL=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
FB=np.array([0,1,3,2],dtype=np.uint8);ZP=np.array([1,2,3],dtype=np.uint8)
def mm(a,b):
 a=np.asarray(a,dtype=np.uint8);b=np.asarray(b,dtype=np.uint8)
 out=np.zeros((a.shape[0],b.shape[1]),dtype=np.uint8)
 for k in range(a.shape[1]):out^=MUL[a[:,k,None],b[k,None,:]]
 return out
def rr(a):
 a=np.array(a,dtype=np.uint8,copy=True);row=0;piv=[]
 for c in range(a.shape[1]):
  ids=np.flatnonzero(a[row:,c])
  if not len(ids):continue
  j=row+int(ids[0]);a[[row,j]]=a[[j,row]];a[row]=MUL[FB[a[row,c]],a[row]]
  f=a[:,c].copy();f[row]=0;a^=MUL[f[:,None],a[row,None,:]];piv.append(c);row+=1
  if row==len(a):break
 return a,piv
def rank(a):return len(rr(a)[1])
def independent(a):return rr(a)[1]
def null(a):
 r,p=rr(a);free=[j for j in range(a.shape[1]) if j not in p]
 n=np.zeros((a.shape[1],len(free)),dtype=np.uint8);n[free,np.arange(len(free))]=1
 n[np.array(p),:]=r[:len(p),free]
 assert not np.any(mm(a,n));return n
def inv(a):
 n=len(a);r,p=rr(np.column_stack([a,np.eye(n,dtype=np.uint8)]));assert p[:n]==list(range(n))
 return r[:,n:]
def right_inverse(a):
 cols=independent(a);assert len(cols)==len(a)
 out=np.zeros((a.shape[1],len(a)),dtype=np.uint8);out[cols]=inv(a[:,cols]);return out
def solve(a,b):
 r,p=rr(np.column_stack([a,b]));n=a.shape[1]
 assert all(c<n for c in p)
 out=np.zeros((n,b.shape[1]),dtype=np.uint8)
 for i,c in enumerate(p):out[c]=r[i,n:]
 assert np.array_equal(mm(a,out),b);return out
def quotient_subspace(columns):
 r,p=rr(columns.T);free=[j for j in range(columns.shape[0]) if j not in p]
 q=np.zeros((len(free),columns.shape[0]),dtype=np.uint8);q[np.arange(len(free)),free]=1
 q[:,p]=r[:len(p),free].T
 j=np.zeros((columns.shape[0],len(free)),dtype=np.uint8);j[free,np.arange(len(free))]=1
 assert not np.any(mm(q,columns)) and np.array_equal(mm(q,j),np.eye(len(free),dtype=np.uint8))
 return q,j
def power(g,n):
 q=0
 for _ in range(n):q=int(T[q,g])
 return q
def group_generated(gens):
 out={0};todo=[0]
 for x in todo:
  for g in gens:
   y=int(T[x,g])
   if y not in out:out.add(y);todo.append(y)
 return sorted(out)
def normq(a):return min(tuple(a),tuple(-x%12 for x in a))
sig=states.index(normq((5,0,0,5)))
V4=[q for q in K if power(q,2)==0]
assert len(V4)==4
v4gens=next(list(v) for v in combinations([q for q in V4 if q],2) if group_generated(v)==V4)
def xor_rank(cols):
 basis={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in basis:basis[p]=v;break
   v^=basis[p]
 return len(basis)
def pack(a):
 out=0
 for j,z in enumerate(a.ravel()):out|=int(z)<<(2*j)
 return out

records=[]
for B in D['character_blocks']:
 if len(B['orbit'])!=8:continue
 acts={a['q_state']:(np.array(a['columns'],dtype=np.uint8).T,a['flip']) for a in B['all_stabilizer_actions']}
 H=sorted(acts);H0=[q for q in H if not acts[q][1]]
 assert len(H)==72 and len(H0)==36 and acts[sig][1]
 assert all(int(T[q,sig])==int(T[sig,q]) for q in H)
 third=[q for q in H0 if q and power(q,3)==0]
 c9gens=next(list(x) for x in combinations(third,2) if T[x[0],x[1]]==T[x[1],x[0]] and len(group_generated(x))==9)
 C9=group_generated(c9gens);assert set(C9)&set(V4)=={0}
 assert set(group_generated(v4gens+c9gens))==set(H0)
 assert set(group_generated(v4gens+c9gens+[sig]))==set(H)
 c9coord={(i,j):int(T[power(c9gens[0],i),power(c9gens[1],j)]) for i,j in product(range(3),repeat=2)}
 F=np.array(B['regular_A4_basis_columns'],dtype=np.uint8).T
 theta=np.array(B['regular_projection_columns'],dtype=np.uint8).T
 cusps=np.array(B['cusp_columns'],dtype=np.uint8).T
 smallcusps=np.array(B['target_cusp_columns'],dtype=np.uint8).T
 qc0,jc0=quotient_subspace(cusps);qsmall,jsmall=quotient_subspace(smallcusps)
 assert qc0.shape==(48,96) and qsmall.shape==(4,8)
 qc=mm(qc0,F);jc=mm(inv(F),jc0)
 phi=mm(mm(qsmall,theta),jc)
 assert rank(phi)==4 and np.array_equal(mm(phi,qc),mm(qsmall,theta))
 mc={}
 for q,(M,flip) in acts.items():
  mc[q]=mm(mm(qc,M),FB[jc] if flip else jc)
  assert np.array_equal(mm(qc,M),mm(mc[q],FB[qc] if flip else qc))
 qt,jt=quotient_subspace(np.column_stack([mc[q]^np.eye(48,dtype=np.uint8) for q in v4gens]))
 assert qt.shape==(12,48)
 phit=mm(phi,jt);assert np.array_equal(mm(phit,qt),phi)
 assert rank(phit)==4
 eker=null(phit);assert eker.shape==(12,8)
 projectors={};uprojectors={};weights=[]
 for a,b in product(range(3),repeat=2):
  P=np.zeros((48,48),dtype=np.uint8);PU=np.zeros((96,96),dtype=np.uint8)
  for (i,j),q in c9coord.items():
   z=ZP[(-a*i-b*j)%3];P^=MUL[z,mc[q]];PU^=MUL[z,acts[q][0]]
  assert np.array_equal(mm(P,P),P)
  pt=mm(mm(qt,P),jt);ee=mm(pt,eker)
  projectors[a,b]=P;uprojectors[a,b]=PU
  weights.append({'weight':[a,b],'source_top_multiplicity':rank(pt),
                  'target_multiplicity':rank(mm(phit,pt)),
                  'extra_multiplicity':rank(ee)})
 assert sum(w['source_top_multiplicity'] for w in weights)==12
 assert sum(w['target_multiplicity'] for w in weights)==4
 assert sum(w['extra_multiplicity'] for w in weights)==8
 sigma=lambda v:mm(mc[sig],FB[v])
 sigmaU=lambda v:mm(acts[sig][0],FB[v])
 items=[];covers=[]
 for a,b in product(range(3),repeat=2):
  wt=(a,b);opp=tuple(-x%3 for x in wt)
  if wt>opp:continue
  P=projectors[wt];PU=uprojectors[wt]
  pt=mm(mm(qt,P),jt)
  if wt==(0,0):
   # Descent under the literal central semilinear involution, including
   # trace-one lifts in the prescribed actual kernel.
   ek=mm(mm(P,jt),mm(pt,eker));cand=[]
   for j in range(ek.shape[1]):
    for z in [1,2]:
     v=MUL[z,ek[:,j:j+1]];cand.append(v^sigma(v))
   if cand:
    mat=np.column_stack(cand);at=mm(qt,mat);chosen=independent(at)
    for j in chosen:
     v=mat[:,j:j+1];assert np.array_equal(sigma(v),v)
     assert not np.any(mm(phi,v));items.append({'weight':wt,'vectors':[v],'kind':'fixed'})
   allcand=[]
   raw=mm(P,jt)
   for j in range(raw.shape[1]):
    for z in [1,2]:
     v=MUL[z,raw[:,j:j+1]];allcand.append(v^sigma(v))
   mat=np.column_stack(allcand);chosen=independent(mm(phi,mat))
   for j in chosen:covers.append({'weight':wt,'vectors':[mat[:,j:j+1]],'kind':'fixed'})
  else:
   ek=mm(mm(P,jt),mm(pt,eker));chosen=independent(mm(qt,ek))
   for j in chosen:
    v=ek[:,j:j+1];assert not np.any(mm(phi,v));items.append({'weight':wt,'vectors':[v,sigma(v)],'kind':'pair'})
   raw=mm(P,jt);chosen=independent(mm(phi,raw))
   for j in chosen:
    v=raw[:,j:j+1];covers.append({'weight':wt,'vectors':[v,sigma(v)],'kind':'pair'})
 def induced(item):return np.column_stack([mm(mc[q],v) for v in item['vectors'] for q in V4])
 assert sum(4*len(i['vectors']) for i in items)==32
 assert sum(4*len(i['vectors']) for i in covers)==16
 inds=next(set(c) for n in range(len(items)+1) for c in combinations(range(len(items)),n) if sum(4*len(items[j]['vectors']) for j in c)==16)
 e0items=[item for j,item in enumerate(items) if j in inds];e1items=[item for j,item in enumerate(items) if j not in inds]
 E0=np.column_stack([induced(i) for i in e0items]);E1=np.column_stack([induced(i) for i in e1items]);P0=np.column_stack([induced(i) for i in covers])
 full=np.column_stack([E0,E1,P0]);assert full.shape==(48,48) and rank(full)==48
 fullinv=inv(full);assert not np.any(mm(phi,E0)) and not np.any(mm(phi,E1))
 assert rank(mm(phi,P0))==4
 # Lift the projective generators to actual affine homology with both
 # the compact marking and the small-source map prescribed exactly.
 combined=np.vstack([qc,theta])
 def lift_item(item):
  v=item['vectors'][0];wt=item['weight'];PU=uprojectors[wt]
  factor=2 if item['kind']=='fixed' else 1
  rhs=np.vstack([MUL[factor,v],np.zeros((8,1),dtype=np.uint8)])
  w=mm(PU,solve(combined,rhs))
  if item['kind']=='fixed':w^=sigmaU(w)
  vs=[w] if item['kind']=='fixed' else [w,sigmaU(w)]
  for a,b in zip(vs,item['vectors']):
   assert np.array_equal(mm(qc,a),b) and not np.any(mm(theta,a))
  return np.column_stack([mm(acts[q][0],w) for w in vs for q in V4])
 U0=np.column_stack([lift_item(i) for i in e0items]);U1=np.column_stack([lift_item(i) for i in e1items])
 assert np.array_equal(mm(qc,U0),E0) and np.array_equal(mm(qc,U1),E1)
 proj0=mm(mm(U0,fullinv[:16]),qc);proj1=mm(mm(U1,fullinv[16:32]),qc)
 assert np.array_equal(mm(proj0,proj0),proj0) and np.array_equal(mm(proj1,proj1),proj1)
 assert not np.any(mm(proj0,proj1)) and not np.any(mm(proj1,proj0))
 assert not np.any(mm(theta,proj0)) and not np.any(mm(theta,proj1))
 assert not np.any(mm(proj0,mm(inv(F),cusps))) and not np.any(mm(proj1,mm(inv(F),cusps)))
 em=[]
 for E,U,sl,proj in [(E0,U0,slice(0,16),proj0),(E1,U1,slice(16,32),proj1)]:
  dic={}
  for q,(M,flip) in acts.items():
   mat=mm(mm(fullinv[sl],mc[q]),FB[E] if flip else E)
   assert np.array_equal(mm(M,FB[U] if flip else U),mm(U,mat))
   assert np.array_equal(mm(proj,M),mm(M,FB[proj] if flip else proj))
   dic[q]=mat
  em.append(dic)
 # The full cross block has an F4-linear matrix coordinate, and the
 # order-two character exchange is genuinely semilinear on it.
 norm=[0]*512;relations=[];gens=v4gens+c9gens+[sig]
 for q in H:
  m0,m1=em[0][q],em[1][q];flip=acts[q][1];cols=[]
  for i in range(16):
   for j in range(16):
    outer=MUL[m0[:,i,None],FB[m1[None,:,j]]]
    for z in [1,2]:cols.append(pack(MUL[FB[z] if flip else z,outer]))
  assert xor_rank(cols)==512
  norm=[a^b for a,b in zip(norm,cols)]
  if q in gens:relations.extend(v^(1<<j) for j,v in enumerate(cols))
 normrank=xor_rank(norm);coinv=512-xor_rank(relations)
 assert normrank==coinv and coinv>0
 record={'character':B['character'],'orbit_size':8,'oriented_stabilizer_order':36,
         'normal_V4_states':V4,'odd_complement_generators':c9gens,'central_exchange_state':sig,
         'all_top_weight_multiplicities':weights,'compact_source_dimension_F4':48,
         'compact_target_dimension_F4':4,'projective_cover_dimension_F4':16,
         'extra_projective_dimensions_F4':[16,16],
         'actual_small_projection_kills_both':True,'actual_cusp_projection_kills_both_idempotents':True,
         'compactification_injective_on_both':True,
         'cross_wedge_dimension_per_pair_F2':512,'global_cross_wedge_dimension_F2':4096,
         'cross_full_norm_rank':normrank,'cross_coinvariant_dimension':coinv,
         'cross_full_norm_isomorphism':True,
         'compact_projection_rows':qc.tolist(),'compact_target_projection_rows':phi.tolist(),
         'compact_decomposition_columns':full.T.tolist(),'compact_decomposition_inverse_rows':fullinv.tolist(),
         'first_actual_affine_embedding_columns':U0.T.tolist(),'second_actual_affine_embedding_columns':U1.T.tolist(),
         'first_idempotent_rows':proj0.tolist(),'second_idempotent_rows':proj1.tolist(),
         'all_first_actions':{str(q):m.T.tolist() for q,m in em[0].items()},
         'all_second_actions':{str(q):m.T.tolist() for q,m in em[1].items()},
         'all_cross_norm_columns':[hex(v) for v in norm]}
 records.append(record)
 print(json.dumps({k:v for k,v in record.items() if not isinstance(v,(dict,list)) or k in ['character','extra_projective_dimensions_F4']}),flush=True)

result={'summary':{'status':'PASS','actual_base_order':46656,'target_base_order':3888,
                   'actual_orbit8_blocks_checked':2,'new_cross_wedge_dimension':sum(r['global_cross_wedge_dimension_F2'] for r in records),
                   'new_invariant_obstruction_coordinates':sum(r['cross_coinvariant_dimension'] for r in records),
                   'all_maps_and_norm_isomorphisms_checked':True,
                   'scope':'Actual finite projectors and norm maps. Integral and arithmetic lifting is proved separately.',
                   'elapsed_seconds':time.time()-start},'blocks':records,
        'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
(OUT/'d_arithmetic_A4_projective.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)
