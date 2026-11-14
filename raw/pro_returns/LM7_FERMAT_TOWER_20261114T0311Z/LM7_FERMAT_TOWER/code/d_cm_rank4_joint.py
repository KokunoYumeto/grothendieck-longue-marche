#!/usr/bin/env python3
"""Change the central seed while retaining its homology and CM pair.

Impose simultaneously the15 Z/4 class-two lifting constraints and
the13 degree6 gamma3N coinvariant constraints. A successful seed
is checked in both complete group models and extends through D29's
stable tower because subsequent corrections begin in D8(K).
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,time
import numpy as np
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):E=runpy.run_path(str(OUT/'d_cm_exponent4.py'))
with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
T=E['T'];d=97;cdim=4753;mp=R['mulpoly'];bp=R['bitpoly'];pol=R['poly'];inv=R['inverse']
Nwords=R['Nwords'];wa,wb=R['wa'],R['wb'];q0e=R['e'];q0s=R['s'];q0t=R['m0'](R['s'],R['r'])
def collapse_at(word,q):
 ans=[]
 def add(j,sgn):
  i=R['chord'].get(j)
  if i is None:return
  a=sgn*(i+1)
  if ans and ans[-1]==-a:ans.pop()
  else:ans.append(a)
 for a in word:
  if a==0:q=R['m0'](q,R['s'])
  else:
   qq=R['m0'](q,R['r'] if a==1 else R['r2'])
   add(R['ix'][q],1);add(R['ix'][qq],-1);q=qq
 return q,ans
def low_images(g,qexpected):
 q,gw=collapse_at(g,q0e);assert q==qexpected;P=pol(gw,2);b1,b2=bp(P[1]),bp(P[2]);b11=mp(b1,b1,1)
 ans=[]
 for nw in Nwords:
  q,cw=collapse_at(nw,qexpected);assert q==qexpected;A=pol(cw,4);assert not A[1].any()
  a2,a3,a4=(bp(A[n]) for n in (2,3,4))
  c3=a3^mp(b1,a2,2)^mp(a2,b1,1)
  c4=a4^mp(b1,a3,3)^mp(a3,b1,1)^mp(b2,a2,2)^mp(a2,b2,2)^mp(mp(b1,a2,2),b1,1)^mp(a2,b11,2)
  ans.append((a2,c3,c4))
 return ans
A0=low_images([],q0e);AS=low_images(wb+[0]+inv(wb),q0s);AT=low_images([0,1],q0t)
def square6(a):
 x,y,z=a;return mp(x,z,4)^mp(y,y,3)^mp(z,x,2)
def comm6(a,b):
 a2,a3,a4=a;b2,b3,b4=b
 ans=mp(a2,b4,4)^mp(a3,b3,3)^mp(a4,b2,2)^mp(b2,a4,4)^mp(b3,a3,3)^mp(b4,a2,2)
 ans^=mp(mp(a2,b2,2),a2,2)^mp(b2,mp(a2,a2,2),4)^mp(a2,mp(b2,b2,2),4)^mp(mp(b2,a2,2),b2,2)
 return ans
def central6(data,i,j):return square6(data[i]) if i==j else comm6(data[i],data[j])
W=R['W'];we=R['echelon'](W);wd=len(W)
def w_project(v):
 out=0
 for k in sorted(we,reverse=True):
  if (v>>k)&1:v^=we[k][0];out^=we[k][1]
 return out,v
WS=[R['action'](w,R['MS']) for w in W];WST=[R['action'](w,R['MSR']) for w in W]
wcols=[]
for x in [w^s for w,s in zip(W,WS)]+[s^t for s,t in zip(WS,WST)]:
 c,rem=w_project(x);assert not rem;wcols.append(c)
wbas=R['echelon'](wcols);assert len(wbas)==227
wduals=[]
for j in range(wd):
 if j in wbas:continue
 z=1<<j
 for k in sorted(wbas):
  if (z&wbas[k][0]).bit_count()%2:z^=1<<k
 assert all((z&a[0]).bit_count()%2==0 for a in wbas.values());wduals.append(z)
assert len(wduals)==13
def obstruction13(v):
 c,_=w_project(v);return sum(((e&c).bit_count()%2)<<i for i,e in enumerate(wduals))
obcols=[];first=[];second=[]
for i,j in E['pairs']:
 v0,vs,vt=(central6(a,i,j) for a in (A0,AS,AT))
 first.append(obstruction13(v0^vs));second.append(obstruction13(vs^vt))
q,tw=R['collapse']([0,1]*72);assert q==q0e;tp=pol(tw);assert all(not tp[n].any() for n in range(1,4))
obcols=first+second+[obstruction13(bp(tp[6]))]
obrows=[sum(1<<j for j,c in enumerate(obcols) if (c>>i)&1) for i in range(13)]
jointrows=E['B']+obrows;assert len(jointrows)==28
target13=obstruction13(R['target']);target=target13<<15
bas={};nullity=0
for j,col in enumerate(T['columns']+[T['c2']]):
 good,z,rem=T['solve'](col);assert good and not rem;z^=1<<j
 if not z:continue
 nullity+=1;c=sum(((r&z).bit_count()%2)<<i for i,r in enumerate(jointrows));cert=z
 while c:
  k=c.bit_length()-1
  if k not in bas:bas[k]=(c,cert);break
  c^=bas[k][0];cert^=bas[k][1]
rem=target;z=0
while rem:
 k=rem.bit_length()-1
 if k not in bas:break
 rem^=bas[k][0];z^=bas[k][1]
print('Joint relation map rank:',len(bas),'of28; target solved:',not rem,flush=True)
witness=None
if not rem:
 cb=z&((1<<cdim)-1);ca=(z>>cdim)&((1<<cdim)-1);h=(z>>(2*cdim))&1
 waa=E['cword'](ca)+wa;wbb=E['cword'](cb)+wb;lam=1+72*h
 cusp=wbb+[0]+inv(wbb)+waa+[1]+inv(waa)+[2,0]*lam
 ntarget=E['kernel_bits'](cusp);good,sol,rr=T['solve'](ntarget);assert good and not rr
 ub=sol&((1<<cdim)-1);ua=(sol>>cdim)&((1<<cdim)-1);eta=(sol>>(2*cdim))&1
 waa=E['cword'](ua,2)+waa;wbb=E['cword'](ub,2)+wbb;lam+=144*eta
 cusp=wbb+[0]+inv(wbb)+waa+[1]+inv(waa)+[2,0]*lam
 nq,nv,nw=E['evaluate'](cusp);assert nq==E['one'] and not np.any(nv) and not np.any(nw)
 q,cw=R['collapse'](cusp);assert q==q0e;PP=pol(cw);assert all(not PP[n].any() for n in range(1,6))
 tt=bp(PP[6]);coord,rr=w_project(tt);assert not rr
 good,wsol,rr=R['solve'](coord,wbas);assert good and not rr
 bw=wsol&((1<<wd)-1);aw=wsol>>wd
 ww_b=[];ww_a=[]
 for i,w in enumerate(R['Wwords']):
  if (bw>>i)&1:ww_b+=w
  if (aw>>i)&1:ww_a+=w
 waa=ww_a+waa;wbb=ww_b+wbb
 final=wbb+[0]+inv(wbb)+waa+[1]+inv(waa)+[2,0]*lam
 nq,nv,nw=E['evaluate'](final);assert nq==E['one'] and not np.any(nv) and not np.any(nw)
 q,cw=R['collapse'](final);assert q==q0e;PP=pol(cw);assert all(not PP[n].any() for n in range(1,7))
 witness={'previous_Z4_beta_central_change':hex(cb),'previous_Z4_A_central_change':hex(ca),
  'previous_multiplier_change':h,'upper_beta_correction':hex(ub),'upper_A_correction':hex(ua),
  'upper_multiplier_change':eta,'lambda_mod288':lam,
  'gamma3N_beta_correction':hex(bw),'gamma3N_A_correction':hex(aw),
  'corrected_B_word_length':len(final),'collapsed_rank4_word_length':len(cw),
  'direct_Z4_N_Magnus_identity_checked':True,'direct_rank4_degree6_Magnus_identity_checked':True,
  'preserved_data':'Original D27 homology masks plus right-s-centralizer word; original G3 conjugators; central representative is replaced explicitly'}
summary={'central_relation_dimension':nullity,'Z4_constraints':15,'degree6_constraints':13,
 'joint_rank':len(bas),'found':not rem,'obstruction':hex(rem),
 'common_quotient_order':'576 * 2^753','combined_two_primary_quotient_order':'576 * 2^9843',
 'infinite_stability':'Every later C_k correction (k>=2) lies in D8(K), so the constructed rank4 D7 action and conjugators remain fixed',
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_rank4_joint.json').write_text(json.dumps({'summary':summary,'witness':witness,
 'joint_basis_certificates':{str(k):{'image':v[0],'relation':hex(v[1])} for k,v in bas.items()}},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
