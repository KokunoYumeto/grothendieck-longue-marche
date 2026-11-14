#!/usr/bin/env python3
"""Refine the alternate CM pair in the characteristic class-two Z/4 model.

The free kernel is N/(gamma3 N [N,N]^4 N^8), of order2^9603.
Every evaluation retains all Magnus coefficients, not just projections.
The first pass also permits changing the previous central corrections
while retaining the same mod2 homology masks and CM matrix pair.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,json,runpy,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):T=runpy.run_path(str(OUT/'d_cm_class2_two.py'))
D=T['D'];one,qs,qr,qr2,qm,ix=T['one'],T['qs'],T['qr'],T['qr2'],T['qm'],T['ix']
Nwords,reps,invert,chord=T['Nwords'],T['reps'],T['invert'],T['chord']
pairs,cdim=T['pairs'],T['cdim'];d=97
ii=np.array([a for a,b in pairs]);jj=np.array([b for a,b in pairs]);diag=ii==jj
J=json.loads((OUT/'d_cm_quadratic_search.json').read_text())['witness']
qa=D['canon'](tuple(J['A']));qb=D['canon'](tuple(J['beta']))

def nword(mask):
 ans=[]
 for i,w in enumerate(Nwords):
  if (mask>>i)&1:ans+=w
 return ans
def cword(mask,power=1):
 ans=[]
 while mask:
  bit=mask&-mask;k=bit.bit_length()-1;i,j=pairs[k]
  w=(Nwords[i]*2 if i==j else Nwords[i]+Nwords[j]+invert(Nwords[i])+invert(Nwords[j]))
  ans+=w*power;mask^=bit
 return ans
wa=cword(int(J['central_A_coefficients'],16))+nword(int(J['homology_A_cycles'],16))+reps[qa]
wb=cword(int(J['central_beta_coefficients'],16))+nword(int(J['homology_beta_cycles'],16))+reps[qb]
right=int(J['beta_right_s_centralizer_coefficients'],16)
for j,v in enumerate(T['fixed_s']):
 if (right>>j)&1:wb+=nword(v)

def evaluate(word,startq=one,second=True):
 q=startq;v=np.zeros(d,dtype=np.int16);w=np.zeros((d,d),dtype=np.int16)
 def append(e,sign):
  i=chord.get(e)
  if i is None:return
  if second:
   w[:,i]=(w[:,i]+sign*v)%4
   if sign<0:w[i,i]=(w[i,i]+1)%4
  v[i]=(v[i]+sign)%4
 for a in word:
  if a==0:q=qm(q,qs)
  else:
   qq=qm(q,qr if a==1 else qr2);append(ix[q],1);append(ix[qq],-1);q=qq
 return q,v,w
def upper(w):return w[ii,jj].copy()
def bits(v):return sum(1<<int(i) for i in np.flatnonzero(v%2))
def matrix(v):
 a=np.zeros((d,d),dtype=np.int16);a[ii,jj]=v;return a
def kernel_bits(word):
 q,v,w=evaluate(word)
 assert q==one and not np.any(v) and not np.any(w%2)
 assert np.array_equal(w,w.T)
 return bits(upper(w)//2)
for i,nw in enumerate(Nwords):
 q,v,w=evaluate(nw);assert q==one and v[i]==1 and np.count_nonzero(v)==1 and not np.any(w)
 q,v,w=evaluate(nw*4);assert q==one and not np.any(v) and w[i,i]==2 and np.count_nonzero(w)==1

cusp=wb+[0]+invert(wb)+wa+[1]+invert(wa)+[2,0]
target=kernel_bits(cusp)
fixed,solution,rem=T['solve'](target)
print('Exact Z/4 target computed; fixed upper corrections:',fixed,flush=True)

# Exact action on the abelian preimage C of the previous central layer.
# C has basis ai^2 and [ai,aj], coefficients in Z/4. Its coordinates
# are upper Magnus coefficients; v=2*diag(w) and w is antisymmetric
# off the diagonal. Conjugation by an open graph word adds v_g wedge v.
def action_data(word,qexpected):
 q,vg,_=evaluate(word,second=False);assert q==qexpected
 cols=[];Ws=[]
 for nw in Nwords:
  q,v,w=evaluate(nw,startq=qexpected);assert q==qexpected
  w=(w+np.outer(vg,v)-np.outer(v,vg))%4
  cols.append(v);Ws.append(w)
 return np.stack(cols,axis=1),np.stack(Ws)
Sdata=action_data(wb+[0]+invert(wb),qs)
Rdata=action_data(wa+[1]+invert(wa),qr)
def dual_action(e,data):
 M,W=data;E=matrix(e).astype(np.int64);M=M.astype(np.int64)
 K=M.T@E@M
 ans=(K[ii,jj]-K[jj,ii])%4
 square=(2*np.einsum('ij,kij->k',E,W,dtype=np.int64)+np.diag(K))%4
 ans[diag]=square;return ans.astype(np.int16)

free=[i for i in range(cdim) if i not in T['bas']];assert len(free)==15
duals=[]
for j in free:
 e=1<<j
 for k in sorted(T['bas']):
  if (e&T['bas'][k][0]).bit_count()%2:e^=1<<k
 assert all((e&b[0]).bit_count()%2==0 for b in T['bas'].values())
 duals.append(e)
q,vt,wt=evaluate([0,1]*72);assert q==one
ct=upper(wt);assert np.array_equal(vt,(2*np.diag(wt))%4)
B=[]
for e in duals:
 er=np.array([(e>>i)&1 for i in range(cdim)],dtype=np.int16)
 es=dual_action(er,Sdata);esr=dual_action(es,Rdata)
 b=np.concatenate([(er-es)%4,(es-esr)%4,np.array([-int(er@ct)%4],dtype=np.int16)])
 assert not np.any(b%2)
 B.append(bits(b//2))
ob= sum(((target&e).bit_count()%2)<<i for i,e in enumerate(duals))

# Kernel of the previous central correction map. Retain exact relation
# vectors, then test the induced second-layer obstruction map.
obas={};nullity=0
for j,col in enumerate(T['columns']+[T['c2']]):
 good,w,rr=T['solve'](col);assert good and not rr
 z=w^(1<<j)
 if not z:continue
 nullity+=1
 zz=sum(((b&z).bit_count()%2)<<i for i,b in enumerate(B));cert=z
 while zz:
  k=zz.bit_length()-1
  if k not in obas:obas[k]=(zz,cert);break
  zz^=obas[k][0];cert^=obas[k][1]
z=0;obrem=ob
while obrem:
 k=obrem.bit_length()-1
 if k not in obas:break
 obrem^=obas[k][0];z^=obas[k][1]
changed_success=not obrem
print('Previous central relation nullity:',nullity,'new obstruction rank:',len(obas),
      'remaining:',obrem,'solvable:',changed_success,flush=True)

summary={'Q_order':576,'N_rank':97,'kernel_definition':'gamma3(N) [N,N]^4 N^8',
 'kernel_order':'2^9603','new_central_dimension':cdim,
 'fixed_previous_conjugators_lift':fixed,
 'previous_central_relations':nullity,'obstruction_dimension_before':15,
 'rank_from_changing_previous_central_corrections':len(obas),
 'same_homology_masks_lift':changed_success,
 'obstruction_remainder':hex(obrem)}
witness=None
if changed_success:
 zb=z&((1<<cdim)-1);za=(z>>cdim)&((1<<cdim)-1);h=(z>>(2*cdim))&1
 wbb=cword(zb)+wb;waa=cword(za)+wa;lam=1+72*h
 lowcusp=wbb+[0]+invert(wbb)+waa+[1]+invert(waa)+[2,0]*lam
 newtarget=kernel_bits(lowcusp)
 good,sol,rr=T['solve'](newtarget);assert good and not rr
 # A twice-C correction is in the new central kernel; the multiplier
 # adds another144, preserving the chosen lower exponent.
 bb=sol&((1<<cdim)-1);aa=(sol>>cdim)&((1<<cdim)-1);eta=(sol>>(2*cdim))&1
 wbb=cword(bb,2)+wbb;waa=cword(aa,2)+waa;lam+=144*eta
 finalcusp=wbb+[0]+invert(wbb)+waa+[1]+invert(waa)+[2,0]*lam
 q,v,w=evaluate(finalcusp);assert q==one and not np.any(v) and not np.any(w)
 witness={'previous_beta_central_change':hex(zb),'previous_A_central_change':hex(za),
  'previous_multiplier_change':h,'upper_beta_correction':hex(bb),'upper_A_correction':hex(aa),
  'upper_multiplier_change':eta,'lambda_mod288':lam,
  'corrected_cusp_word_length':len(finalcusp),'direct_Z4_Magnus_identity_checked':True,
  'retains_homology_masks_from':'d_cm_quadratic_search.json',
  'generation':'same invertible rank97 mod2 map; finite2-kernel Frattini theorem'}
summary['elapsed_seconds']=round(time.time()-started,3)
(OUT/'d_cm_exponent4.json').write_text(json.dumps({'summary':summary,'witness':witness,
 'second_obstruction_functionals':[hex(v) for v in B]},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
