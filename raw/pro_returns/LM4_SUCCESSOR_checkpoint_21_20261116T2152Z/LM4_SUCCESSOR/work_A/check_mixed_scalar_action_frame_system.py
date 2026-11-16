"""Add the complete negative-invariant mixed cusp-inner action family.
Also retain the six integral free offdiagonal center values literally.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json
HERE=Path(__file__).resolve().parent
model=HERE/'check_mixed_scalar_action.py'
D={'__file__':str(model),'__name__':'__mixed704_model__'}
with redirect_stdout(StringIO()):exec(compile(model.read_text().split('out=dict(scope=')[0],str(model),'exec'),D)
globals().update({k:v for k,v in D.items()if k not in('__file__','__name__')})
base=json.loads((HERE/'mixed_scalar_frame_system.json').read_text())
labels=[tuple(v)for v in base['labels']];cols=list(base['columns']);target=base['target']
JF=tup(base['Z_joint_basis']);SF3=tup(base['S3_basis']);TJ=tup(base['T_joint_basis']);OMK=tup(base['old_M_norm_kernel']);CBAS=tup(base['new_scalar_norm_preimages'])
NB=(0,1,2,3,5,4,6,7);zp=[zi[NB[i],NB[j]]for i,j in slots]
SHIFT_CLASS=432;SHIFT_NORM=1392;SHIFT_INT=2352
freeoff=[mi[i,j]for i in range(4)for j in range(i+1,4)]
def pack(v):return sum(int(x)<<(3*j)for j,x in enumerate(v))
def h3(key,v):return act(key,(v,),3)[0]
def d3(v):return h3(O['HB'],h3('c',v))
# Enforce the exact integral-retention constraint as extra rows.
for j,(kind,i,k,a)in enumerate(labels):
 if kind=='M':
  m=oldm(fsm(a,OMK[i]));cols[j]|=pack(tuple(m[t]for t in freeoff))<<SHIFT_INT
TF3=tuple(j3(v)for v in O['TF']);assert all(h3('c',v)==v and h3(O['HT'],v)==v for v in TF3)
NegW=av(PW,permrows(CW,P));ADIRS=[]
def comm_formula(z,a):return fva(fcoc(A0,z,a,Z0),fcoc(a,Z0,A0,z))
for i,(r,s)in enumerate(slots):
 if (r<4)==(s<4)or i>zp[i]:continue
 for j,v in enumerate(TF3):
  for a in(1,2,4):
   z=[zero]*48;z[i]=fsm(a,v)
   if i!=zp[i]:z[zp[i]]=z[i]
   z=tuple(z);q=(A0,M0,z,U0,H0)
   assert act(O['HT'],z,3)==z and permz(act('c',z,3),NB)==z
   k=comm_formula(z,T[0]);n=comm_formula(z,NegW)
   if j==0 and a==1:
    actual=gm(gin(q,T),gi(T));assert actual== (A0,M0,Z0,k,H0)
    assert gm(q,na(q))==(A0,M0,Z0,n,H0)
   cols.append((pack(k)<<SHIFT_CLASS)|(pack(n)<<SHIFT_NORM));labels.append(('ACTION',i,j,a));ADIRS.append(z)
assert len(ADIRS)==288
sol,rank=O['bit_solve'](cols,target)
print('Action+frame+integral simultaneous system:',len(cols),'bits; rank',rank,'; target solvable',sol is not None,flush=True)
out=dict(scope='Full stated288-bit mixed cusp-inner action family plus2343 homogeneous frame directions; six integral free halves retained. No arbitrary affine exhaustion.',
 labels=labels,columns=cols,target=target,rank=rank,solution_mask=sol,action_basis=TF3,integral_free_offdiag_indices=freeoff)
if sol is not None:
 z=Z0;m=M0;uc=U0;tc=[zero]*6;uu=[zero]*4;oldmc=M0;aa=Z0;chk=0
 for jj,(kind,i,j,a)in enumerate(labels):
  if not(sol>>jj&1):continue
  chk^=cols[jj]
  if kind=='Z':
   zz=[zero]*48;zz[i]=fsm(a,JF[j]if i==zp[i]else SF3[j])
   if i!=zp[i]:zz[zp[i]]=d3(zz[i])
   z=av(z,tuple(zz))
  elif kind=='M':oldmc=fva(oldmc,fsm(a,OMK[i]));m=fva(m,oldm(fsm(a,OMK[i])))
  elif kind=='SCALAR':uc=fva(uc,CBAS[i])
  elif kind=='T':tc[i]=fva(tc[i],fsm(a,TJ[j]))
  elif kind=='U':uu[i]=fva(uu[i],fsm(a,SF3[j]))
  else:
   zz=[zero]*48;zz[i]=fsm(a,TF3[j])
   if i!=zp[i]:zz[zp[i]]=zz[i]
   aa=av(aa,tuple(zz))
 assert chk==target and all(m[t]==0 for t in freeoff)
 AACT=(A0,M0,aa,U0,H0);kc=comm_formula(aa,T[0])
 def ph_new(g):
  a,m,z,u,h=gin(AACT,ph(g))
  if O['eps'](g[4]):u=fva(u,kc)
  return a,m,z,u,h
 def na_new(g):return ph_new(ca(g))
 assert ph_new(T)==T
 assert na_new(na_new(S))==S and na_new(na_new(R))==R
 q=(A0,m,z,uc,H0);nb=gm(gm(AACT,B),q)
 assert gin(nb,S)==ph_new(S)
 assert gm(gi(nb),na_new(gi(nb)))==ONE
 print('Actual704 law: new positive cusp, negative square, exact s-conjugacy and norm PASS.',flush=True)
 out.update(action_inner=aa,cusp_character=kc,ordinary_correction=z,old_center_correction=oldmc,new_scalar_correction=uc,T_correction=tc,U_correction=uu,corrected_scalar_frame=nb,direct704='PASS')
else:
 piv={}
 for c in cols:
  v=c
  while v:
   j=v.bit_length()-1
   if j in piv:v^=piv[j]
   else:piv[j]=v;break
 rem=target
 for j in sorted(piv,reverse=True):
  if rem>>j&1:rem^=piv[j]
 row=1<<(rem.bit_length()-1)
 for j in sorted(piv):
  if(row&piv[j]).bit_count()%2:row^=1<<j
 assert all((row&c).bit_count()%2==0 for c in cols)and(row&target).bit_count()%2==1
 out.update(annihilator=row,remainder=rem)
 print('Exact dual annihilator saved for this expanded family.',flush=True)
(HERE/'mixed_scalar_action_frame_system.json').write_text(json.dumps(out,indent=2)+'\n')
