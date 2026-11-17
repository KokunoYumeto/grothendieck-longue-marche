#!/usr/bin/env python3
"""Literal normalization of the actual B139 operators; no source-word scan."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
INPUT=ROOT/'work_CE/next_symmetric_nodes/one_family_face28.json'
j=json.loads(INPUT.read_text())
def red(w):
 out=[]
 for x in w:
  if abs(x) in (3,4): x=abs(x)
  if out and ((abs(x) in (3,4) and out[-1]==x) or out[-1]==-x): out.pop()
  else:out.append(x)
 return out
def inv(w):return red([-x for x in reversed(w)])
def sub(w,d):
 out=[]
 for x in w:out+=d[abs(x)] if x>0 else inv(d[abs(x)])
 return red(out)
ops={k:{int(i):red(w) for i,w in d.items()} for k,d in j['signed_orbifold_operators'].items()}
ops['u']={i:sub(ops['v'][i],ops['m_inverse']) for i in (1,2,3,4)}
ops['u_inverse']={i:sub(ops['m'][i],ops['v_inverse']) for i in (1,2,3,4)}
# Old alphabet: a=1,f=2,C=3,tau=4. New free fiber: r=1,bar_r=2,w=3.
new_old={1:[4,-2,3],2:[-2,3,4],3:[4,3],4:[4]}
def f_red(w):
 out=[]
 for x in w:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return out
def tau(w):return [{1:2,2:1,3:-3}[abs(x)]*(1 if x>0 else -1) for x in w]
def new_nf(w):
 out=[];p=0
 for x in w:
  if abs(x)==4:p^=1
  else:out=f_red(out+(tau([x]) if p else [x]))
 return (out,p)
def expand_new(w):
 out=[]
 for x in w:out+=new_old[abs(x)] if x>0 else inv(new_old[abs(x)])
 return red(out)
old_new={2:[-3,-2],3:[4,3],4:[4]}
def convert_old(w):
 out=[]
 for x in w:out+=old_new[abs(x)] if x>0 else [-y for y in reversed(old_new[abs(x)])]
 return new_nf(out)
checks=[]
def ck(label,a,b):
 assert a==b,(label,a,b)
 checks.append({'label':label,'value':a})
for i in (2,3,4):ck('old_basis_inverse_'+str(i),expand_new(old_new[i]),[i])
for i in (1,2,3,4):ck('new_basis_inverse_'+str(i),convert_old(new_old[i]),new_nf([i]))
expected={
 'm':{1:[1],2:[2],3:[1,-3,-2]},
 'm_inverse':{1:[1],2:[2],3:[-2,-3,1]},
 'u':{1:[-3,1,3],2:[3,2,-3],3:[3]},
 'u_inverse':{1:[3,1,-3],2:[-3,2,3],3:[3]}}
for s,d in expected.items():
 for i,w in d.items():ck(s+'_new_generator_'+str(i),sub(new_old[i],ops[s]),expand_new(w))
 ck(s+'_tau_fixed',ops[s][4],[4])
# Exact t basis and the ordered conjugators, verified from the actual a image.
t=[-2,3]
ck('m_t_fixed',sub(t,ops['m']),t)
ck('u_t',sub(t,ops['u']),red([4,3]+t+[4,3]))
h_u=expand_new([-3,1]);h_ui=expand_new([3,-1])
ck('u_a_conjugator',ops['u'][1],red(h_u+[1]+inv(h_u)))
ck('u_inverse_a_conjugator',ops['u_inverse'][1],red(h_ui+[1]+inv(h_ui)))
ck('ordered_inverse_cocycle',red(sub(h_ui,ops['u'])+h_u),[])
ck('H_generator_from_m_inverse_fv',ops['m_inverse'][2],expand_new([-1,3]))
# The section element h_u^-1 u centralizes the actual primitive r.
ck('H_generator_centralizes_r',red(inv(h_u)+sub(new_old[1],ops['u'])+h_u),new_old[1])
# chi_x=(1,-1,1) on the new free fiber, invariant under all four signed maps.
chi=lambda w:sum(({1:1,2:-1,3:1}[abs(x)])*(1 if x>0 else -1) for x in w)
for s,d in expected.items():
 for i,w in d.items():ck(s+'_chi_x_'+str(i),chi(w),chi([i]))
ck('chi_x_h_u',chi([-3,1]),0)
ck('chi_x_h_u_inverse',chi([3,-1]),0)
ck('chi_x_r',chi([1]),1)
out={'status':'PASS','input':str(INPUT.relative_to(ROOT)),'input_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),'new_basis':{'r':new_old[1],'bar_r':new_old[2],'w':new_old[3]},'old_inverse':old_new,'signed_actions_new':expected,'h_u_new':[-3,1],'h_u_inverse_new':[3,-1],'checks':checks,'scope':'Exact finite input and basis checks only. All-word cocycle, centralizer, and stabilizer arguments are proved in the companion note; no orbit scan.'}
DEST=ROOT/'work_CE/next_symmetric_nodes/one_family_stabilizer_normalization30.json'
DEST.write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',len(checks),'literal basis/action/cocycle/character checks from the actual B139 input')
print('Exact H=<m,r^-1*w*u>; C_E0(r)=<r> x H; L=C_S(r), proved uniformly in companion note')
print('No L=<m> or fixed-source equality is inferred.')
