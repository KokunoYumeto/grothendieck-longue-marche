#!/usr/bin/env python3
"""Both actual rank-nine branches in the complete order3888 boundary.

Rebuilds the exact local-transgression certificate, then retains every
one of the forty homology parameters and all ten reduced coordinates.
The remaining integral s-centralizer ambiguity is exhaustively retained.
"""
from pathlib import Path
from fractions import Fraction
from collections import deque
import json,time,random,runpy
import numpy as np
import sympy as sp
from sympy import ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

OUT=Path(__file__).resolve().parent;started=time.time()
C=runpy.run_path(str(OUT/'d_arithmetic_local_transgression.py'))
for name in ['rho','size','D','H','I','M','mi','S4','R4','mt','ma','va','gm','s','r','t',
             'rs','rr','ch','ci','BW','IC','invword','combine','solver','rank','evaluate',
             'obs','cross','bitmask','EA','W','SM','TM','HS','HR','csolve','moving',
             'integral_pair','obstruction','collected','params','local','Frows']:
 globals()[name]=C[name]
QH=json.loads((OUT/'d_arithmetic_rank9_seed.json').read_text())
QC=json.loads((OUT/'d_arithmetic_rank9_conjugators.json').read_text())
qsi=mi[S4];qri=mi[R4];qrs=[mt[g][qsi] for g in range(48)];qrr=[mt[g][qri] for g in range(48)]
qch=QH['rank9_cycle_chords'];qci={e:j for j,e in enumerate(qch)}
def qeval(word):
 q=0;p=[0]*48
 for tok in word:
  if tok==0:q=qrs[q]
  else:
   h=qrr[q] if tok==1 else qrr[qrr[q]]
   p[q]+=1;p[h]-=1;q=h
 return q,p
qwords={0:[]};todo=[0]
for q in todo:
 for tok,h in [(0,qrs[q]),(1,qrr[q])]:
  if h not in qwords:qwords[h]=qwords[q]+[tok];todo.append(h)
P=np.array([[qeval(w)[1][e] for w in BW] for e in qch],dtype=np.int16)%4
assert not np.any((P@EA-P)%4)
_,pr,_,pi=solver([bitmask(P[:,j]) for j in range(rho)]);assert pr==9
def invert4(a):
 a=a.copy()%4;n=len(a);b=np.eye(n,dtype=np.int16)
 for j in range(n):
  p=next(i for i in range(j,n) if a[i,j]%2)
  a[[j,p]]=a[[p,j]];b[[j,p]]=b[[p,j]]
  iv=pow(int(a[j,j]),-1,4);a[j]=a[j]*iv%4;b[j]=b[j]*iv%4
  for i in range(n):
   if i!=j:
    v=int(a[i,j]);a[i]=(a[i]-v*a[j])%4;b[i]=(b[i]-v*b[j])%4
 assert np.array_equal(a,np.eye(n,dtype=np.int16));return b
Pinv=invert4(P[:,pi])
def pluslift(v):
 a=np.zeros(rho,dtype=np.int16);a[pi]=Pinv@np.array(v,dtype=np.int16)%4
 a=EA@a%4;assert np.array_equal(P@a%4,np.array(v,dtype=np.int16)%4)
 assert np.array_equal(EA@a%4,a);return a

# Exact saturated integral fixed lattices, not the larger mod2 fixed spaces.
Qfixed={};smith={}
for name in ('s','r'):
 a=sp.Matrix(9,9,lambda i,j:QH['homology_'+name+'_columns'][j][i])-sp.eye(9)
 ad,au,av=smith_normal_decomp(DomainMatrix.from_Matrix(a).convert_to(ZZ))
 sd,uu,vv=ad.to_Matrix(),au.to_Matrix(),av.to_Matrix()
 assert sd==uu*a*vv and abs(vv.det())==1
 zero=[j for j in range(9) if not sd[j,j]]
 Qfixed[name]=[[int(vv[i,j]) for i in range(9)] for j in zero]
 smith[name]=[int(sd[j,j]) for j in range(9)]
 assert all(a*sp.Matrix(v)==sp.zeros(9,1) for v in Qfixed[name])
assert len(Qfixed['s'])==3 and len(Qfixed['r'])==1

# The complete actual peripheral pair space, its600-dimensional kernel,
# and one actual40-dimensional quotient complement.
WA={g:[int(v,16) for v in H['moving_'+g+'_columns']] for g in ('s','r')}
L=[(1<<j)^WA['s'][j] for j in range(640)]+[
 combine(WA['s'],(1<<j)^WA['r'][j]) for j in range(640)]
_,lr,pk,_=solver(L);assert lr==640 and len(pk)==640
K=[]
for name in ('s','r','t'):
 for hx in H['moving_fixed_bases'][name]:
  v=int(hx,16);K.append(v if name=='s' else (v<<640 if name=='r' else v|(v<<640)))
assert rank(K)==600
_,dr,_,inds=solver(K+pk);assert dr==640
PC=[pk[j-600] for j in inds if j>=600];assert len(PC)==40
IP=[];Qlin=[];first=[];second=[]
for p in PC:
 bm=combine(W,p&((1<<640)-1));am=combine(W,p>>640)
 b,a=integral_pair(bm,am);IP.append((b,a));Qlin.append(obstruction(b,a))
 first.append(bm^combine(HS,bm));second.append(combine(HS,am^bm))
def comm(a,b):return cross(a,b)^cross(b,a)
Qquad=[[0]*40 for _ in range(40)]
for i in range(40):
 for j in range(i+1,40):Qquad[i][j]=comm(first[j],second[i])
rng=random.Random(20261113)
for trial in range(20):
 i,j=sorted(rng.sample(range(40),2))
 b=(IP[i][0]+IP[j][0])%4;a=(IP[i][1]+IP[j][1])%4
 assert obstruction(b,a)==Qlin[i]^Qlin[j]^Qquad[i][j]

gwords={0:[]};todo=[0]
for g in todo:
 for tok,h in [(0,rs[g]),(1,rr[g])]:
  if h not in gwords:gwords[h]=gwords[g]+[tok];todo.append(h)
assert len(gwords)==3888
def repaired_seed(qb,bQ,aQ):
 gw=gwords[qb];qq,p=qeval(gw);assert qq==qb//81
 ref=qeval(qwords[qq])[1]
 diff=[p[e]-ref[e] for e in qch]
 b=pluslift([(x-y)%4 for x,y in zip(bQ,diff)]);a=pluslift(aQ)
 q,dq,_=evaluate(gw+[0]+invword(gw)+[0]);assert q==0
 dq=np.array(dq,dtype=np.int16)
 for stage in (1,2):
  err=(dq+b-SM@b+(SM-TM)@a)%4
  assert not any(P@err%4) and not any(EA@err%4)
  if stage==2:assert not any(err%2)
  cm=csolve(bitmask(err,0 if stage==1 else 1))
  db=combine(W,cm&((1<<640)-1));da=combine(W,cm>>640)
  db=moving(np.array([(db>>i)&1 for i in range(rho)],dtype=np.int16))
  da=moving(np.array([(da>>i)&1 for i in range(rho)],dtype=np.int16))
  b=(b+stage*db)%4;a=(a+stage*da)%4
 assert not any((dq+b-SM@b+(SM-TM)@a)%4)
 aw=collected(a);bw=collected(b)+gw
 word=bw+[0]+invword(bw)+aw+[1]+invword(aw)+[2,0]
 q,ab,c=evaluate(word);assert q==0 and ab==[0]*rho
 q,ds,sc=evaluate(bw+[0]+invword(bw)+[0]);assert q==0
 assert ds==((dq+b-SM@b)%4).tolist()
 return b,a,gw,bitmask(ds),obs(c),len(word)
def reducer(cols,n=74):
 bas={}
 for col in cols:
  v=col
  while v:
   p=v.bit_length()-1
   if p not in bas:bas[p]=v;break
   v^=bas[p]
 free=[j for j in range(n) if j not in bas]
 def red(v):
  for p in sorted(bas,reverse=True):
   if v>>p&1:v^=bas[p]
  return sum(1<<i for i,p in enumerate(free) if v>>p&1)
 return red,free,[red(1<<j) for j in range(n)]
def polynomial(mask,const,lin,qua):
 active=[]
 while mask:
  b=mask&-mask;active.append(b.bit_length()-1);mask^=b
 out=const
 for k,i in enumerate(active):
  out^=lin[i]
  for j in active[k+1:]:out^=qua[i][j]
 return out

# Efficient exact convolution for the final marked cycle map.
left=None;cycles=[sum(1<<e for e,v in c.items() if v%2) for c in IC]
def marked_matrix(b,a,gw):
 global left
 if left is None:
  mt0=np.array(mt,dtype=np.int16);ma0=np.array(ma,dtype=np.int16);va0=np.array(va,dtype=np.int16)
  qh=np.arange(size,dtype=np.int16)//81;vh=np.arange(size,dtype=np.int16)%81
  left=np.empty((size,size),dtype=np.int16)
  for g in range(size):
   q,v=divmod(g,81);left[g]=81*mt0[q,qh]+va0[v,ma0[q,vh]]
  assert np.all(left[:,0]==np.arange(size))
  gi=np.argmin(left,axis=1);left=left[gi]
 z=np.zeros(size,dtype=np.uint8)
 for j,c in enumerate(IC):
  if int(a[j]-b[j])%2:
   for e,v in c.items():z[e]^=v%2
 q=0
 for tok in gw:
  if tok==0:q=rs[q]
  else:
   h=rr[q] if tok==1 else rr[rr[q]];z[q]^=1;z[h]^=1;q=h
 trans=[int.from_bytes(row.tobytes(),'little') for row in np.packbits(z[left],axis=1,bitorder='little')]
 def vc(v):return sum(1<<j for j,e in enumerate(ch) if v>>e&1)
 cols=[(1<<j)^vc(combine(trans,c)) for j,c in enumerate(cycles)]
 assert all(combine(cols,HS[j])==combine(HS,cols[j]) for j in range(rho))
 assert all(combine(cols,HR[j])==combine(HR,cols[j]) for j in range(rho))
 return cols
Omega=[int(v,16) for v in H['pairing_columns_mod2']]
cases=[]
for branch in (1,3):
 record=next(z for z in QC['all_exact_conjugator_records']
             if z.get('integral_over_Z2') and z['quarter_turn_power']==branch and z['r_conjugator_linear_state']==0)
 qbeta=record['beta_linear_state']
 choices=[g for g in range(size) if g//81==qbeta and gm(g,s)==gm(s,g)]
 assert len(choices)==9;qb=choices[0]
 def fmod(s0):
  a=Fraction(s0);return a.numerator*pow(a.denominator,-1,4)%4
 bQ=list(map(fmod,record['beta_cycle_coordinates']));aQ=list(map(fmod,record['r_conjugator_cycle_coordinates']))
 b0,a0,gw,ds,z0,wlen=repaired_seed(qb,bQ,aQ)
 def shift(b,a):return comm(ds,combine(HS,bitmask(a)^bitmask(b)))
 locals0=[v^shift(b,a) for v,(b,a) in zip(local,params)]
 lsolve,lrank,_,linds=solver(locals0)
 red,free,qcols=reducer(locals0)
 lin=[red(v^shift(b,a)) for v,(b,a) in zip(Qlin,IP)]
 qua=[[red(v) for v in row] for row in Qquad]
 plus=[];plus_checks=[]
 for name in ('s','r'):
  for v in Qfixed[name]:
   lift=pluslift([x%4 for x in v]);zero=np.zeros(rho,dtype=np.int16)
   b,a=(lift,zero) if name=='s' else (zero,lift)
   assert not any((b+SM@(a-b)-TM@a)%4)
   value=obstruction(b,a)^shift(b,a)
   doubled=obstruction(2*b%4,2*a%4)^shift(2*b%4,2*a%4)
   assert doubled==0
   plus_checks.append({'type':name,'integral_fixed_vector':v,'obstruction':hex(value),'doubled_obstruction':hex(doubled)})
   if name=='s':plus.append((b,a,value))
   else:assert value==0
 assert len(plus)==3
 constants=[red(z0^combine([z[2] for z in plus],j)) for j in range(8)]
 print('branch',branch,'local rank',lrank,'reduced dimension',len(free),'constants',constants,flush=True)
 remaining={c for c in constants};found={};search=random.Random(20261113+branch)
 trials=0
 while remaining and trials<1000000:
  mask=search.getrandbits(40);value=polynomial(mask,0,lin,qua);trials+=1
  if value in remaining:found[value]=mask;remaining.remove(value)
 print('branch',branch,'search',trials,'remaining',sorted(remaining),flush=True)
 solutions=[]
 for ambiguity,const in enumerate(constants):
  if const not in found:continue
  mask=found[const]
  b=np.zeros(rho,dtype=np.int16);a=np.zeros(rho,dtype=np.int16)
  for j,(bi,ai) in enumerate(IP):
   if mask>>j&1:b=(b+bi)%4;a=(a+ai)%4
  for j,(bi,ai,_) in enumerate(plus):
   if ambiguity>>j&1:b=(b+bi)%4;a=(a+ai)%4
  error=z0^obstruction(b,a)^shift(b,a);assert red(error)==0
  localmask=lsolve(error)
  for j,(bi,ai) in enumerate(params):
   if localmask>>j&1:b=(b+bi)%4;a=(a+ai)%4
  assert z0^obstruction(b,a)^shift(b,a)==0
  ab=(a0+a)%4;bb=(b0+b)%4
  aw=collected(ab);bw=collected(bb)+gw
  word=bw+[0]+invword(bw)+aw+[1]+invword(aw)+[2,0]
  q,ac,cc=evaluate(word);assert q==0 and ac==[0]*rho and obs(cc)==0
  tc=marked_matrix(bb,ab,gw);tr=rank(tc)
  pairing=all(sum(1<<i for i,u in enumerate(tc) if (u&combine(Omega,c)).bit_count()%2)==Omega[j]
              for j,c in enumerate(tc))
  assert tr==649 and pairing
  qT=next(z for z in QH['four_quarter_turn_candidates'] if z['quarter_turn_power']==branch)['columns_moduli']['2']
  pcols=[bitmask(P[:,j]) for j in range(rho)]
  qtcols=[sum(int(v)<<i for i,v in enumerate(col)) for col in qT]
  assert all(combine(pcols,c)==combine(qtcols,pcols[j]) for j,c in enumerate(tc))
  solutions.append({'s_ambiguity_mask':ambiguity,'parameter40_mask':hex(mask),
    'local600_correction_mask':hex(localmask),'beta_mod4':bb.tolist(),'r_mod4':ab.tolist(),
    'literal_cusp_word_length':len(word),'all74_central_coordinates_zero':True,
    'homology_generation_rank':tr,'intersection_pairing_preserved':pairing,
    'rank9_projection_checked':True,'homology_columns':[hex(c) for c in tc]})
 cases.append({'quarter_turn_branch':branch,'beta_base_state':qb,'beta_base_word':gw,
  'seed_beta_mod4':b0.tolist(),'seed_r_mod4':a0.tolist(),'seed_cusp_word_length':wlen,
  'seed_obstruction':hex(z0),'seed_s_displacement':hex(ds),
  'local_image_rank':lrank,'local_image_basis_indices':linds,
  'local_obstruction_columns':[hex(v) for v in locals0],
  'reduced_dimension':len(free),'reduced_quotient_columns':qcols,
  'all40_reduced_linear_coefficients':lin,'all780_reduced_quadratic_coefficients':qua,
  'all8_marking_constants':constants,'fixed_lattice_checks':plus_checks,
  'search_trials':trials,'unreached_constants':sorted(remaining),'solutions':solutions})
summary={'scope':'Complete forty-parameter equations over the actual arithmetic order3888 base.',
 'base_order':3888,'homology_rank':649,'moving_pair_dimension':640,
 'same_homology_parameter_dimension':600,'actual_derivation_dimension':40,
 'arithmetic_quarter_turn_branches':[1,3],
 'all_branch_local_ranks':[c['local_image_rank'] for c in cases],
 'all_branch_reduced_dimensions':[c['reduced_dimension'] for c in cases],
 'integral_s_centralizer_rank':3,'integral_r_centralizer_rank':1,
 'all_doubled_fixed_parameter_obstructions_zero':True,
 'all_r_fixed_parameter_obstructions_zero':True,
 'all16_marking_cases_solved':all(len(c['solutions'])==8 for c in cases),
 'literal_solution_word_checks':sum(len(c['solutions']) for c in cases),
 'all_solution_homology_and_pairing_checks':True,
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'integral_fixed_smith_diagonals':smith,
 'all40_pair_complement_masks':[hex(v) for v in PC],
 'all40_integral_pair_lifts':[{'beta_mod4':b.tolist(),'r_mod4':a.tolist()} for b,a in IP],
 'all_cases':cases}
(OUT/'d_arithmetic_affine_boundary.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
