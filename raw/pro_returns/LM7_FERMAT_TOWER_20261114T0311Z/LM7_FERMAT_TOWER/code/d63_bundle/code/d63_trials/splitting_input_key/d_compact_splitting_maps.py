#!/usr/bin/env python3
"""Actual compact, cusp, target and projective-type comparison maps.

The compact decomposition markings are checked against the actual target
map and the retained affine embeddings.  All cross-module actions and norms
use the literal arithmetic stabilizers.  Integral orthogonal transport and
the source automorphism are proved separately.
"""
from pathlib import Path
from itertools import combinations
import numpy as np
import json,hashlib,time
OUT=Path(__file__).resolve().parent;start=time.time()
path=OUT/'d_arithmetic_A4_twisted.json';D=json.loads(path.read_text())
T=np.array(D['Q_multiplication'],dtype=np.int16);A4=D['A4_states']
MUL=np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8)
FB=np.array([0,1,3,2],dtype=np.uint8);Z=np.array([1,2,3],dtype=np.uint8)
def mm(a,b):
 out=np.zeros((a.shape[0],b.shape[1]),dtype=np.uint8)
 for k in range(a.shape[1]):out^=MUL[a[:,k,None],b[k,None,:]]
 return out
def rr(a):
 a=np.array(a,dtype=np.uint8,copy=True);row=0;p=[]
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
 n=len(a);r,p=rr(np.column_stack([a,np.eye(n,dtype=np.uint8)]));assert p[:n]==list(range(n));return r[:,n:]
def solve(a,b):
 n=a.shape[1];r,p=rr(np.column_stack([a,b]));assert all(c<n for c in p)
 x=np.zeros((n,b.shape[1]),dtype=np.uint8)
 for i,c in enumerate(p):x[c]=r[i,n:]
 assert np.array_equal(mm(a,x),b);return x
def right_inverse(a):
 p=rr(a)[1];assert len(p)==len(a)
 out=np.zeros((a.shape[1],len(a)),dtype=np.uint8);out[p]=inv(a[:,p]);return out
def null(a):
 r,p=rr(a);free=[j for j in range(a.shape[1]) if j not in p]
 n=np.zeros((a.shape[1],len(free)),dtype=np.uint8);n[free,np.arange(len(free))]=1
 n[np.array(p),:]=r[:len(p),free]
 assert not np.any(mm(a,n));return n
def quotient(c):
 r,p=rr(c.T);free=[j for j in range(c.shape[0]) if j not in p]
 q=np.zeros((len(free),c.shape[0]),dtype=np.uint8);q[np.arange(len(free)),free]=1
 q[:,p]=r[:len(p),free].T
 j=np.zeros((c.shape[0],len(free)),dtype=np.uint8);j[free,np.arange(len(free))]=1
 assert not np.any(mm(q,c));assert np.array_equal(mm(q,j),np.eye(len(free),dtype=np.uint8))
 return q,j
def generated(gens):
 seen={0};todo=[0]
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
def inverse(g):return next(j for j in range(576) if T[g,j]==0)
def xor_rank(cols):
 b={}
 for v in cols:
  while v:
   p=v.bit_length()-1
   if p not in b:b[p]=v;break
   v^=b[p]
 return len(b)
def pack(a):return sum(int(v)<<(2*j) for j,v in enumerate(a.ravel()))
def hermpack(a):
 assert np.array_equal(a,FB[a.T]);assert np.all(a.diagonal()<2)
 v=list(map(int,a.diagonal()))
 for i in range(len(a)):
  for j in range(i+1,len(a)):v.extend([int(a[i,j])&1,int(a[i,j])>>1])
 return sum(x<<j for j,x in enumerate(v))

paths=[OUT/'d_arithmetic_A4_twisted.json',OUT/'d_arithmetic_A4_projective.json',OUT/'d_orbit12_projective_kernel.json']
Old=json.loads(paths[1].read_text());New=json.loads(paths[2].read_text())
V4=[g for g in A4 if order(g)<=2];assert len(V4)==4
def realcols(A,flip):
 return [pack(MUL[FB[z] if flip else z,A[:,j]]) for j in range(A.shape[1]) for z in [1,2]]
def normrank(matrices,flips,group):
 cols=[0]*(2*len(next(iter(matrices.values()))))
 for g in group:cols=[a^b for a,b in zip(cols,realcols(matrices[g],flips[g]))]
 return xor_rank(cols),cols
def hom_rank(E,small,gens):
 # F4-linearity is forced by the literal active Delta character.  These
 # oriented generator equations suffice to prove vanishing; the complete
 # semilinear action and marking are checked independently below.
 ne=len(next(iter(E.values())));nt=len(next(iter(small.values())))
 columns=[]
 for i in range(ne):
  for j in range(nt):
   X=np.zeros((ne,nt),dtype=np.uint8);X[i,j]=1
   columns.append(np.concatenate([(mm(E[g],X)^mm(X,small[g])).ravel() for g in gens]))
 mat=np.column_stack(columns);rk=rank(mat)
 return rk,ne*nt-rk,mat
rows=[]
for B in D['character_blocks']:
 char=B['character'];orbit=len(B['orbit'])
 acts={a['q_state']:(np.array(a['columns'],dtype=np.uint8).T,a['flip']) for a in B['all_stabilizer_actions']}
 H=sorted(acts);H0=[g for g in H if not acts[g][1]];flips={g:acts[g][1] for g in H}
 F=np.array(B['regular_A4_basis_columns'],dtype=np.uint8).T
 theta=np.array(B['regular_projection_columns'],dtype=np.uint8).T
 cusp=np.array(B['cusp_columns'],dtype=np.uint8).T;R=mm(inv(F),cusp)
 q0,j0=quotient(cusp);qc=mm(q0,F);jc=mm(inv(F),j0)
 smallR=np.array(B['target_cusp_columns'],dtype=np.uint8).T;qs,js=quotient(smallR)
 phi=mm(mm(qs,theta),jc);assert rank(phi)==4
 assert np.array_equal(mm(phi,qc),mm(qs,theta))
 # The full actual affine map is onto on its cusp submodule.
 assert rank(mm(theta,R))==4 and not np.any(mm(qs,mm(theta,R)))
 mc={g:mm(mm(qc,m),FB[jc] if flip else jc) for g,(m,flip) in acts.items()}
 jp=right_inverse(phi)
 small={g:mm(mm(phi,m),FB[jp] if flips[g] else jp) for g,m in mc.items()}
 for g in H:assert np.array_equal(mm(phi,mc[g]),mm(small[g],FB[phi] if flips[g] else phi))
 jR=right_inverse(R.T).T
 cr={g:mm(mm(jR,acts[g][0]),FB[R] if flips[g] else R) for g in H}
 for g in H:assert np.array_equal(mm(acts[g][0],FB[R] if flips[g] else R),mm(R,cr[g]))
 weight_record=[]
 if orbit==8:
  P=next(x for x in Old['blocks'] if x['character']==char)
  full=np.array(P['compact_decomposition_columns'],dtype=np.uint8).T
  fullinv=np.array(P['compact_decomposition_inverse_rows'],dtype=np.uint8)
  E=full[:,:32];M=full[:,32:];e=fullinv[:32];m=fullinv[32:]
  assert not np.any(mm(phi,E)) and rank(mm(phi,M))==4
  c9=P['odd_complement_generators'];sig=P['central_exchange_state']
  sylow=generated(V4+[sig]);assert len(sylow)==8
  gens=V4+c9;assert generated(gens)==H0
  def weight_support(mats,dimension):
   qt,jt=quotient(np.column_stack([mats[g]^np.eye(dimension,dtype=np.uint8) for g in V4]))
   top={g:mm(mm(qt,mats[g]),jt) for g in H0}
   answer=[]
   for a in range(3):
    for b in range(3):
     proj=np.zeros_like(next(iter(top.values())))
     for i in range(3):
      for j in range(3):
       q=0
       for _ in range(i):q=int(T[q,c9[0]])
       for _ in range(j):q=int(T[q,c9[1]])
       proj^=MUL[[1,2,3][(-a*i-b*j)%3],top[q]]
     assert np.array_equal(mm(proj,proj),proj)
     answer.append({'weight':[a,b],'multiplicity':rank(proj)})
   assert sum(x['multiplicity'] for x in answer)==qt.shape[0]
   return answer
 else:
  P=next(x for x in New['blocks'] if x['character']==char)
  E=np.array(P['compact_projective_columns'],dtype=np.uint8).T
  M=np.array(P['compact_complement_columns'],dtype=np.uint8).T
  full=np.column_stack([E,M]);fullinv=inv(full);e=fullinv[:32];m=fullinv[32:]
  assert not np.any(mm(phi,E)) and rank(mm(phi,M))==4
  c=P['C3_generator'];tau=P['normalizing_involution'];sig=P['central_semilinear_exchange']
  sylow=generated(V4+[tau,sig]);assert len(sylow)==16
  gens=V4+[c,tau];assert generated(gens)==H0
 em={g:mm(mm(e,mc[g]),FB[E] if flips[g] else E) for g in H}
 cm={g:mm(mm(m,mc[g]),FB[M] if flips[g] else M) for g in H}
 for g in H:
  assert np.array_equal(mm(mc[g],FB[E] if flips[g] else E),mm(E,em[g]))
  assert np.array_equal(mm(mc[g],FB[M] if flips[g] else M),mm(M,cm[g]))
 en,en_cols=normrank(em,flips,sylow);mn,mn_cols=normrank(cm,flips,sylow);rn,rn_cols=normrank(cr,flips,sylow)
 assert en==64//len(sylow) and rn==96//len(sylow)
 if orbit==8:
  assert mn==32//len(sylow)
  ew=weight_support(em,32);mw=weight_support(cm,16)
  es={tuple(x['weight']) for x in ew if x['multiplicity']};ms={tuple(x['weight']) for x in mw if x['multiplicity']}
  assert not es&ms and {tuple(-a%3 for a in w) for w in es}==es
  weight_record={'extra_top_weights':ew,'cover_top_weights':mw,'dual_extra_and_cover_types_disjoint':True}
 else:assert mn==0
 hr,hd,hm=hom_rank(em,small,gens);assert hd==0 and hr==128
 row={'character':char,'orbit_size':orbit,'ordered_stabilizer_generators':gens,
  'unordered_Sylow_states':sylow,'extra_dimension_F4':32,'complement_dimension_F4':16,
  'cusp_dimension_F4':48,'target_compact_dimension_F4':4,
  'extra_Sylow_norm_rank':en,'complement_Sylow_norm_rank':mn,'cusp_Sylow_norm_rank':rn,
  'cusp_projection_rank':4,'target_to_extra_Hom_equation_rank_F4':hr,'target_to_extra_Hom_dimension_F4':hd,
  'target_to_extra_Hom_equation_rows':hm.tolist(),'projective_type_check':weight_record,
  'all_extra_actions':{str(g):a.T.tolist() for g,a in em.items()},
  'all_complement_actions':{str(g):a.T.tolist() for g,a in cm.items()},
  'all_small_compact_actions':{str(g):a.T.tolist() for g,a in small.items()},
  'all_cusp_actions':{str(g):a.T.tolist() for g,a in cr.items()},
  'cusp_Sylow_norm_columns':[hex(v) for v in rn_cols]}
 rows.append(row)
 print(json.dumps({k:v for k,v in row.items() if k not in ['target_to_extra_Hom_equation_rows','projective_type_check'] and not k.startswith('all_') and k!='cusp_Sylow_norm_columns'}),flush=True)
result={'summary':{'status':'PASS','all_four_compact_markings_checked':True,'all_target_to_extra_Hom_spaces_zero':True,
 'all_cusp_modules_projective_on_actual_full_unordered_stabilizer':True,'all_cusp_maps_onto':True,
 'old_extra_dual_types_disjoint_from_cover_types':True,'new_complements_have_zero_Sylow_norm':True,
 'elapsed_seconds':time.time()-start},'cases':rows,
 'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
(OUT/'d_compact_splitting_maps.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print(json.dumps(result['summary'],indent=2),flush=True)

