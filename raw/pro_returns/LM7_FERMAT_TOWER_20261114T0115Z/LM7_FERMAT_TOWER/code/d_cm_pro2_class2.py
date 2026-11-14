#!/usr/bin/env python3
"""Test the stabilized two-level class-two correction module at2.

For k>=2, C_k=<ai^(2^k),[ai,aj]^(2^(k-1))> in the
Z/(2^(k+1)) Magnus quotient is abelian of exponent4. Its
conjugation matrices modulo4 depend only on the fixed first
homology masks and are independent of k. The code computes
the exact Bockstein map and verifies one actual Z/8 lift.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):E=runpy.run_path(str(OUT/'d_cm_exponent4.py'))
T=E['T'];one,qs,qr,qr2,qm,ix=E['one'],E['qs'],E['qr'],E['qr2'],E['qm'],E['ix']
Nwords,invert,chord=E['Nwords'],E['invert'],E['chord'];pairs=E['pairs'];d=97;cdim=4753
ii,jj,diag=E['ii'],E['jj'],E['diag'];bits,matrix,upper=E['bits'],E['matrix'],E['upper']
wa,wb,lam=E['waa'],E['wbb'],E['lam'];assert lam==1
duals=E['duals'];Sdata,Rdata=E['Sdata'],E['Rdata']

def dual_action(e,data):
 M,W=data;E0=matrix(e).astype(np.int64);E0[np.arange(d),np.arange(d)]*=3
 M=M.astype(np.int64);K=M.T@E0@M
 ans=(K[ii,jj]-K[jj,ii])%4
 square=(2*np.einsum('ij,kij->k',E0,W,dtype=np.int64)+3*np.diag(K))%4
 ans[diag]=square;return ans.astype(np.int16)
q,v12,w12=E['evaluate']([0,1]*12);assert q==one
ct=upper((2*w12+np.outer(v12,v12))%4);ct[diag]=3*ct[diag]%4
B=[]
for e in duals:
 er=np.array([(e>>i)&1 for i in range(cdim)],dtype=np.int16)
 es=dual_action(er,Sdata);esr=dual_action(es,Rdata)
 b=np.concatenate([(er-es)%4,(es-esr)%4,np.array([-int(er@ct)%4],dtype=np.int16)])
 assert not np.any(b%2);B.append(bits(b//2))
obas={};nullity=0
for j,col in enumerate(T['columns']+[T['c2']]):
 good,w,rr=T['solve'](col);assert good and not rr
 z=w^(1<<j)
 if not z:continue
 nullity+=1;zz=sum(((b&z).bit_count()%2)<<i for i,b in enumerate(B));cert=z
 while zz:
  k=zz.bit_length()-1
  if k not in obas:obas[k]=(zz,cert);break
  zz^=obas[k][0];cert^=obas[k][1]
print('Stabilized k>=2 obstruction rank:',len(obas),'of15',flush=True)

def evaluate(word,modulus=8,startq=one):
 q=startq;v=np.zeros(d,dtype=np.int16);w=np.zeros((d,d),dtype=np.int16)
 def append(e,sign):
  i=chord.get(e)
  if i is None:return
  w[:,i]=(w[:,i]+sign*v)%modulus
  if sign<0:w[i,i]=(w[i,i]+1)%modulus
  v[i]=(v[i]+sign)%modulus
 for a in word:
  if a==0:q=qm(q,qs)
  else:
   qq=qm(q,qr if a==1 else qr2);append(ix[q],1);append(ix[qq],-1);q=qq
 return q,v,w
def central_word(mask,k):
 ans=[]
 while mask:
  bit=mask&-mask;j=bit.bit_length()-1;a,b=pairs[j]
  if a==b:ans+=Nwords[a]*(2**k)
  else:ans+=(Nwords[a]+Nwords[b]+invert(Nwords[a])+invert(Nwords[b]))*(2**(k-1))
  mask^=bit
 return ans
def target_of(word):
 q,v,w=evaluate(word);assert q==one and not np.any(v) and not np.any(w%4)
 assert np.array_equal(w,w.T);return bits(upper(w)//4)
target=target_of(wb+[0]+invert(wb)+wa+[1]+invert(wa)+[2,0]*lam)
ob=sum(((target&e).bit_count()%2)<<i for i,e in enumerate(duals));z=0;rem=ob
while rem:
 k=rem.bit_length()-1
 if k not in obas:break
 rem^=obas[k][0];z^=obas[k][1]
witness=None
if not rem:
 zb=z&((1<<cdim)-1);za=(z>>cdim)&((1<<cdim)-1);h=(z>>(2*cdim))&1
 wbb=central_word(zb,2)+wb;waa=central_word(za,2)+wa;ll=lam+144*h
 tar=target_of(wbb+[0]+invert(wbb)+waa+[1]+invert(waa)+[2,0]*ll)
 good,sol,rr=T['solve'](tar);assert good and not rr
 bb=sol&((1<<cdim)-1);aa=(sol>>cdim)&((1<<cdim)-1);eta=(sol>>(2*cdim))&1
 wbb=central_word(bb,3)+wbb;waa=central_word(aa,3)+waa;ll+=288*eta
 final=wbb+[0]+invert(wbb)+waa+[1]+invert(waa)+[2,0]*ll
 q,v,w=evaluate(final);assert q==one and not np.any(v) and not np.any(w)
 witness={'lower_beta_change':hex(zb),'lower_A_change':hex(za),'lower_multiplier_change':h,
  'upper_beta_correction':hex(bb),'upper_A_correction':hex(aa),'upper_multiplier_change':eta,
  'lambda_mod576':ll,'corrected_cusp_word_length':len(final),
  'direct_Z8_Magnus_identity_checked':True,
  'preserved_action':'Reduction to the H2 action induced by d_cm_exponent4.json; the previously chosen H4 central coordinates may change'}
summary={'stabilized_two_level_module_dimension':4753,
 'mod2_correction_rank':4738,'mod2_cokernel_dimension':15,
 'relation_space_dimension':nullity,'stabilized_Bockstein_rank':len(obas),
 'contains_twice_whole_module':len(obas)==15,
 'Z8_lift_found':witness is not None,'Z8_kernel_order':'2^14356',
 'stabilization':'For k>=2, (2^k-1) is3 modulo4 and the action depends only on unchanged conjugator path parities',
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_pro2_class2.json').write_text(json.dumps({'summary':summary,'witness':witness,
 'stabilized_obstruction_functionals':[hex(v) for v in B],
 'Bockstein_basis_certificates':{str(k):{'image':v[0],'relation':hex(v[1])} for k,v in obas.items()}},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
