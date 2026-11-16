"""Seek one actual frame reselection with the original positive action fixed.
Local sets are exhausted for linear feasibility; this producer seeks a witness,
not an exhaustive old quadratic search.
"""
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
import json,runpy
HERE=Path(__file__).resolve().parent
with redirect_stdout(StringIO()):G=runpy.run_path(str(HERE/'check_Q6_central_cover.py'))
def tup(x):return tuple(tup(v)for v in x)if isinstance(x,list)else x
old=json.loads((HERE/'Q6_actual_central_solution.json').read_text());G['phi0'].__globals__['WE']=tup(old['WE']);G['ph'].__globals__['PSHIFT']=tup(old['PSHIFT'])
BF=tup(old['BFRAME']);ONE=G['ONE'];SS=G['SS'];em,ei,ein,na=[G[k]for k in('em','ei','ein','na')]
assert em(ei(BF),na(ei(BF)))==ONE
space=json.loads((HERE/'A76_fixed_action_frame_space.json').read_text());loc=json.loads((HERE/'A76_fixed_action_local_feasibility.json').read_text())
V=tup(space['frame_basis_vectors']);AA0=G['AA0'];ZA=G['ZA'];HN0=G['HN0'];av=G['av'];fva=G['fva']
found=None
for j,entry in enumerate(loc['solutions']):
 a=AA0;mask=entry['affine_mask']
 for i,v in enumerate(V):
  if mask>>i&1:a=av(a,v)
 q=(a,ZA,HN0);assert ein(q,SS)==SS
 beta=em(BF,q);n=em(ei(beta),na(ei(beta)));assert n[0]==AA0 and n[2]==HN0
 z=G['fsolve'](G['ZNORM'],n[1])
 if z is not None:
  beta=(beta[0],fva(beta[1],z),beta[2]);assert ein(beta,SS)==G['ph'](SS)and em(ei(beta),na(ei(beta)))==ONE
  found=dict(candidate_index=j,local_entry=entry,right_affine_correction=a,central_correction=z,BFRAME=beta)
  print('Original action fixed: old-group frame norm solved by linear candidate',j,flush=True);break
if found is None:
 print('No direct linear representative among',len(loc['solutions']),'has a centrally correctable oldnorm;198-dimensional homogeneous oldquadratic freedom untested.',flush=True)
else:
 # Actual six-cup reconstruction, retaining the original source/action.
 path=HERE/'check_A63_cross_cup.py';D={'__file__':str(path),'__name__':'__fixed_action_cup_verify__'}
 with redirect_stdout(StringIO()):exec(compile(path.read_text().split('out=dict(scope=')[0],str(path),'exec'),D)
 b=(found['BFRAME'],D['TZ']);target=D['ph'](D['SS']);bs=D['ein'](b,D['SS']);co=[]
 cols=[D['fva'](v,D['h2v'](target[0][2],v))for v in D['O']['VB']]
 for k in range(6):
  x=D['O']['fsolve'](cols,D['fva'](target[1][k],bs[1][k]));assert x is not None;co.append(x)
 b=(b[0],tuple(co));assert D['ein'](b,D['SS'])==target
 n=D['em'](D['ei'](b),D['na'](D['ei'](b)));assert n[0]==D['O']['ONE']
 sf=[D['sqv'](v)for v in D['O']['SF']]
 nc=[D['fva'](v,D['h2v'](D['O']['HB'],D['cv2'](v)))for v in sf]
 corr=[]
 for k in range(6):
  x=D['O']['fsolve'](nc,n[1][k]);assert x is not None,('unexpected local norm failure',k)
  corr.append(D['flin'](sf,x))
 b=D['em'](b,(D['O']['ONE'],tuple(corr)))
 assert D['ein'](b,D['SS'])==D['ph'](D['SS'])and D['em'](D['ei'](b),D['na'](D['ei'](b)))==D['ONE']
 assert D['na'](D['na'](D['SS']))==D['SS']and D['na'](D['na'](D['RR']))==D['RR']
 found.update(six_cup_BFRAME=b,six_cup_initial_norm=n[1],six_cup_norm_correction=corr,all_direct_checks='PASS',WE=old['WE'],PSHIFT=old['PSHIFT'])
 print('Actual six-cup s-frame norm and conjugacy PASS, with original positive action unchanged.',flush=True)
out=dict(scope='Original A56 positive action fixed; finite s-frame reselected above the sameinitialC; witness search within841 localcompatible affine representatives.',found=found,old_action_unchanged=found is not None)
(HERE/'A76_fixed_action_frame_reselection.json').write_text(json.dumps(out,indent=2)+'\n')
