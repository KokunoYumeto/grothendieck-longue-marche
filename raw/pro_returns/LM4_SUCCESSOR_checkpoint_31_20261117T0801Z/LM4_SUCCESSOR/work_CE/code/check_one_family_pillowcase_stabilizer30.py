#!/usr/bin/env python3
"""Exact marked pillowcase quotient of B139: no source-word or exponent scan."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes/one_family_face28.json'
j=json.loads(P.read_text())
def red(w):
 out=[]
 for a in w:
  if abs(a) in (3,4):a=abs(a)
  if out and (out[-1]==-a or (a in (3,4) and out[-1]==a)):out.pop()
  else:out.append(a)
 return out
def wi(w):return red([-a for a in reversed(w)])
def sub(w,d):return red([b for a in w for b in (d[abs(a)] if a>0 else wi(d[abs(a)]))])
ops={s:{int(k):v for k,v in d.items()} for s,d in j['signed_orbifold_operators'].items()}
ops['u']={k:sub(ops['v'][k],ops['m_inverse']) for k in (1,2,3,4)}
ops['u_inverse']={k:sub(ops['m'][k],ops['v_inverse']) for k in (1,2,3,4)}
# Q=Pillowcase semidirect <tau>. Element=(z exponent,w exponent,r parity,tau parity).
one=(0,0,0,0)
def act_tau(a):
 x,y,e=a;return(-x+e,-y,e)
def mul(a,b):
 x,y,e,t=a;X,Y,E,T=b
 if t:X,Y,E=act_tau((X,Y,E))
 sign=(-1)**e
 return(x+sign*X,y+sign*Y,e^E,t^T)
def inverse(a):
 x,y,e,t=a;out=(-((-1)**e)*x,-((-1)**e)*y,e)
 if t:out=act_tau(out)
 return(*out,t)
old={2:(1,-1,1,0),3:(0,-1,0,1),4:(0,0,0,1)}
def ev(w):
 out=one
 for a in w:out=mul(out,old[abs(a)] if a>0 else inverse(old[abs(a)]))
 return out
checks=[]
def ck(label,a,b):
 assert a==b,(label,a,b)
 checks.append({'label':label,'value':a})
for i in (3,4):ck('old_involution_'+str(i),mul(old[i],old[i]),one)
new={'r':[4,-2,3],'bar_r':[-2,3,4],'w':[4,3],'f':[2],'g':[3,2,3]}
for name in ('r','bar_r','f','g'):ck('actual_peripheral_square_'+name,mul(ev(new[name]),ev(new[name])),one)
ck('r_image',ev(new['r']),(0,0,1,0));ck('bar_r_image',ev(new['bar_r']),(1,0,1,0));ck('w_image',ev(new['w']),(0,1,0,0))
z=red(new['bar_r']+new['r']);ck('z_image',ev(z),(1,0,0,0))
matrices={'m':((1,-1),(0,1)),'m_inverse':((1,1),(0,1)),'u':((1,0),(4,1)),'u_inverse':((1,0),(-4,1))}
corrections={'m':(0,0),'m_inverse':(0,0),'u':(0,-2),'u_inverse':(0,2)}
def auto(a,A,b):
 x,y,e,t=a
 return(A[0][0]*x+A[0][1]*y+e*b[0],A[1][0]*x+A[1][1]*y+e*b[1],e,t)
for s,A in matrices.items():
 b=corrections[s]
 for k in (2,3,4):ck(s+'_entire_old_generator_'+str(k),ev(ops[s][k]),auto(old[k],A,b))
 for name,w in [('z',z),('w',new['w']),('r',new['r'])]:ck(s+'_ordinary_'+name,ev(sub(w,ops[s])),auto(ev(w),A,b))
 # Twice the coboundary identity b=(I-A)(1/2,0), exact integers.
 ck(s+'_twice_coboundary',(2*b[0],2*b[1]),(1-A[0][0],-A[1][0]))
 ck(s+'_determinant',A[0][0]*A[1][1]-A[0][1]*A[1][0],1)
ck('scaled_m',((1,2*matrices['m'][0][1]),(matrices['m'][1][0]//2,1)),((1,-2),(0,1)))
ck('scaled_u',((1,2*matrices['u'][0][1]),(matrices['u'][1][0]//2,1)),((1,0),(2,1)))
out={'status':'PASS','input':str(P.relative_to(ROOT)),'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'matrices':matrices,'r_corrections':corrections,'checks':checks,'scope':'All exact signed generator/quotient checks. Faithful whole-source ping-pong and L=<m> are uniform proofs in the companion note; no source-word scan.'}
(ROOT/'work_CE/next_symmetric_nodes/one_family_pillowcase_stabilizer30.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS:',len(checks),'actual signed pillowcase quotient, correction and matrix identities')
print('M=[[1,-1],[0,1]], U=[[1,0],[4,1]]; 2b_s=(I-A_s)e1 on the generators')
print('Whole-source faithfulness and exact L=<m> are proved by ping-pong, not by samples.')
