#!/usr/bin/env python3
"""Vary the initial homology corrections in an extra CM matrix pair.

The complete lower-conjugator/central equation at2 has five obstructions.
Their exact invariant quadratic forms are evaluated on the98-dimensional
affine cusp-solution space; generation is separately checked.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,random,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):T=runpy.run_path(str(OUT/'d_cm_class2_two.py'))
D3,D=T['D3'],T['D'];Q,ix,one,qs,qr,qm=T['Q'],T['ix'],T['one'],T['qs'],T['qr'],T['qm']
qr2=T['qr2'];qt=qm(qs,qr);C=T['C'];M=T['M'];pairs=T['pairs'];d=97
Nwords,reps,invert=T['Nwords'],T['reps'],T['invert'];chord=T['chord']
row=next(r for r in D['records'] if r['A']==(1,0,0,1) and r['beta']==(9,8,4,9))
qa=D['canon'](tuple(row['A']));qb=D['canon'](tuple(row['beta']))
aug,extras=T['augmented'](qb);cdim=T['cdim']
free=[i for i in range(cdim) if i not in aug];assert len(free)==5
duals=[]
for j in free:
 v=1<<j
 for k in sorted(aug):
  if (v&aug[k][0]).bit_count()%2:v^=1<<k
 assert all((v&a[0]).bit_count()%2==0 for a in aug.values())
 duals.append(v)
forms=np.zeros((5,d,d),dtype=np.int16)
for k,v in enumerate(duals):
 for j,(a,b) in enumerate(pairs):forms[k,a,b]=(v>>j)&1
form_masks=[[sum(1<<i for i in range(d) if forms[k,i,j]) for j in range(d)] for k in range(5)]
def signature(word,startq=one):
 q=startq;v=0;z=np.zeros(5,dtype=np.int16)
 def append(e,sgn):
  nonlocal v,z
  i=chord.get(e)
  if i is None:return
  for k in range(5):z[k]^=(v&form_masks[k][i]).bit_count()%2
  if sgn<0:z^=forms[:,i,i]
  v^=1<<i
 for letter in word:
  if letter==0:q=qm(q,qs)
  else:
   qq=qm(q,qr if letter==1 else qr2)
   append(ix[q],1);append(ix[qq],-1);q=qq
 return q,np.array([(v>>i)&1 for i in range(d)],dtype=np.int16),z

blocks={}
for q in (one,qs,qt):
 zs=[]
 for i,word in enumerate(Nwords):
  qq,v,z=signature(word,q);assert qq==q and np.array_equal(v,M[q][:,i]);zs.append(z)
 Bq=np.stack([M[q].T@F@M[q]%2 for F in forms])
 blocks[q]=(np.stack(zs,axis=1),np.triu(Bq,1))
def cross(v,w):return ((v@forms)%2@w)%2
def nblock(a,q,negative=False):
 Z,Qform=blocks[q];v=M[q]@a%2
 z=(Z@a+np.sum((a@Qform%2)*a,axis=1))%2
 if negative:z=(z+cross(v,v))%2
 return v,z
const_b=signature(reps[qb]+[0]+invert(reps[qb]),one)
const_a=signature(reps[qa]+[1]+invert(reps[qa]),qs)
const_t=signature([2,0],qt)
assert const_b[0]==qs and const_a[0]==qt and const_t[0]==one
def obstruction(w):
 b,a=w[:d],w[d:];v=np.zeros(d,dtype=np.int16);z=np.zeros(5,dtype=np.int16)
 pieces=[nblock(b,one),const_b[1:],nblock(b,qs,True),nblock(a,qs),const_a[1:],nblock(a,qt,True),const_t[1:]]
 for vv,zz in pieces:z=(z+zz+cross(v,vv))%2;v=(v+vv)%2
 assert not np.any(v)
 return z
part=np.array([((int(row['beta_cycle_coefficients'],16)>>i)&1) for i in range(d)]+
              [((int(row['A_cycle_coefficients'],16)>>i)&1) for i in range(d)],dtype=np.int16)
L=np.concatenate([np.eye(d,dtype=np.int16)-M[qs],M[qs]-M[qt]],axis=1)%2
def null2(A):
 A=A.copy()%2;n,m=A.shape;row=0;piv=[]
 for col in range(m):
  hits=np.flatnonzero(A[row:,col])
  if not len(hits):continue
  k=row+int(hits[0]);A[[row,k]]=A[[k,row]]
  factors=A[:,col].copy();factors[row]=0;A^=factors[:,None]*A[row]
  piv.append(col);row+=1
  if row==n:break
 ans=[]
 for j in range(m):
  if j in piv:continue
  v=np.zeros(m,dtype=np.int16);v[j]=1
  for k,col in enumerate(piv):v[col]=A[k,j]
  assert not np.any(A@v%2);ans.append(v)
 return np.stack(ans,axis=1)
ker=null2(L);assert ker.shape==(194,98)
def masks(w):return tuple(sum(1<<i for i in range(d) if c[i]) for c in (w[:d],w[d:]))
def words(w):
 b,a=masks(w);wa=[];wb=[]
 for i,nw in enumerate(Nwords):
  if (a>>i)&1:wa+=nw
  if (b>>i)&1:wb+=nw
 return wa+reps[qa],wb+reps[qb]
def direct_obstruction(w):
 wa,wb=words(w);cusp=wb+[0]+invert(wb)+wa+[1]+invert(wa)+[2,0]
 q,v,z=T['evaluate'](cusp);assert q==one and v==0
 cb=T['central'](z)
 return np.array([(cb&f).bit_count()%2 for f in duals],dtype=np.int16),cb
for coeff in [np.zeros(98,dtype=np.int16),np.ones(98,dtype=np.int16),np.arange(98,dtype=np.int16)%2]:
 w=(part+ker@coeff)%2
 assert np.array_equal(obstruction(w),direct_obstruction(w)[0])

rng=np.random.default_rng(20261114);hist={};zero=0;rankfail=0;answer=None
for trial in range(1,20001):
 coeff=rng.integers(0,2,98,dtype=np.int16);w=(part+ker@coeff)%2
 ob=obstruction(w);key=''.join(map(str,ob.tolist()));hist[key]=hist.get(key,0)+1
 if np.any(ob):continue
 zero+=1;b,a=masks(w)
 edge=D['P'][qa]^D['P'][qb]^(1<<ix[qa])^D['cycle_sum'](a)^D['cycle_sum'](b)
 rank=D['module_rank'](edge)
 if rank!=97:rankfail+=1;continue
 direct,cb=direct_obstruction(w);assert not np.any(direct)
 good,sol,rem=T['solve'](cb,aug);assert good and not rem
 val=0;rest=sol
 while rest:
  bit=rest&-rest;k=bit.bit_length()-1
  val^=T['columns'][k] if k<2*cdim else T['c2'] if k==2*cdim else extras[k-2*cdim-1]
  rest^=bit
 assert val==cb
 def central_word(bits):
  ans=[]
  while bits:
   bit=bits&-bits;k=bit.bit_length()-1;i,j=pairs[k]
   ans+=(Nwords[i]+Nwords[i]) if i==j else (Nwords[i]+Nwords[j]+invert(Nwords[i])+invert(Nwords[j]))
   bits^=bit
  return ans
 wa,wb=words(w);right=sol>>(2*cdim+1);cw=[]
 for j,v in enumerate(T['fixed_s']):
  if (right>>j)&1:
   for i,nw in enumerate(Nwords):
    if (v>>i)&1:cw+=nw
 wb=central_word(sol&((1<<cdim)-1))+wb+cw
 wa=central_word((sol>>cdim)&((1<<cdim)-1))+wa
 eta=(sol>>(2*cdim))&1;lam=1+72*eta
 exact_cusp=wb+[0]+invert(wb)+wa+[1]+invert(wa)+[2,0]*lam
 cq,cv,cw=T['evaluate'](exact_cusp)
 assert cq==one and cv==0 and not any(cw)
 answer={'trial':trial,'A':list(row['A']),'beta':list(row['beta']),
   'homology_beta_cycles':hex(b),'homology_A_cycles':hex(a),'kernel_rank':rank,
   'central_beta_coefficients':hex(sol&((1<<cdim)-1)),
   'central_A_coefficients':hex((sol>>cdim)&((1<<cdim)-1)),
   'multiplier_bit':(sol>>(2*cdim))&1,
   'beta_right_s_centralizer_coefficients':hex(sol>>(2*cdim+1)),
   'corrected_cusp_word_length':len(exact_cusp),
   'direct_corrected_Magnus_identity_checked':True,
   'mod3_certificate':'D25 same matrix pair; its class-two mod3 lift has zero central correction',
   'obstruction_check':'five invariant quadratic equations zero and direct4753-coordinate equation solvable'}
 print('Found invertible two-prime class-two extra CM witness on trial',trial,flush=True)
 break
summary={'matrix_pair':{'A':list(row['A']),'beta':list(row['beta'])},'affine_nullity_mod2':98,
 'quadratic_obstructions':5,'trials':trial,'zero_obstruction_candidates':zero,
 'zero_obstruction_rank_failures':rankfail,'found':answer is not None,
 'obstruction_histogram':hist,'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_quadratic_search.json').write_text(json.dumps({'summary':summary,'witness':answer,
 'obstruction_functionals':[hex(v) for v in duals]},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
