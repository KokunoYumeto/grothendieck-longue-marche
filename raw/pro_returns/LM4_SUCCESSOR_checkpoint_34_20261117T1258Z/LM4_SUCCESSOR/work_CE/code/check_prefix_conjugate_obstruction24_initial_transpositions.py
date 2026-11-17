#!/usr/bin/env python3
"""One prescribed actual regional quotient: (F_2)^12 semidirect S_3.
Independent evaluator; no root/DE producer imports, no quotient census.
"""
from pathlib import Path
from itertools import permutations
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
paths=[P/'annular_neck_presentation23.json',P/'inner_q0_adapted_basis22.json']
G,Y=[json.loads(p.read_text())for p in paths]
#Functional composition: p*q means first q, then p. Positions are0,1,2.
idp=(0,1,2); kperm=(1,0,2); Cperm=(0,2,1)
def pm(p,q):return tuple(p[q[i]]for i in range(3))
def pinv(p):return tuple(p.index(i)for i in range(3))
def sign(p):return sum(p[i]>p[j]for i in range(3)for j in range(i+1,3))%2
def act(p,v):
 w=0
 for fam in range(4):
  for pos in range(3):
   if (v>>(3*fam+pos))&1:w^=1<<(3*fam+p[pos])
 return w
def mul(x,y):
 v,p=x;w,q=y
 return v^act(p,w),pm(p,q)
def inv(x):
 v,p=x;q=pinv(p)
 return act(q,v),q
unit=(0,idp)
def word(w,D):
 x=unit
 for j in w:x=mul(x,D[j]if j>0 else inv(D[-j]))
 return x
def comm(x,y):return mul(mul(mul(x,y),inv(x)),inv(y))
def vector(fam,pos):return (1<<(3*fam+pos),idp)
U={name:vector(i,2)for i,name in enumerate(('a','b','d','e'))}
C=(0,Cperm);k=(0,kperm);h=C;f=mul(h,inv(k));z=mul(C,h)
assert z==unit
#Actual Y order: a,b,C,f,d,e,h,k.
DY={1:U['a'],2:U['b'],3:C,4:f,5:U['d'],6:U['e'],7:h,8:k}
B=mul(mul(C,U['b']),C)
assert B==vector(1,1)
#Whole direct input's global minus regional labels a,B,d,e,f,Cminus,kminus.
DG={1:U['a'],2:B,3:U['d'],4:U['e'],5:f,6:C,8:k}
regional=[r for r in G['regional_relators']if r['side']=='minus']
assert len(regional)==16
relchecks=[]
for r in regional:
 val=word(r['word'],DG);assert val==unit,r['name']
 relchecks.append({'name':r['name'],'word':r['word'],'value':val})
assert word((6,6),DG)==unit
#Separate literal actual inputs: all ten original adapted node words,
#both six-generator source actions, and both six-generator old q0 maps.
rawchecks=[]
for row in Y['all_ten_relations']:
 assert word(row['new_relation'],DY)==unit,row['name']
 rawchecks.append({'name':row['name'],'word':row['new_relation']})
sourcechecks=[]
for j in range(1,7):
 plus=word(Y['source_h_action'][str(j)],DY)
 minus=word(Y['source_h_inverse_action'][str(j)],DY)
 assert mul(mul(inv(h),DY[j]),h)==plus
 assert mul(mul(h,DY[j]),inv(h))==minus
 oldplus=word(Y['positive_q0_in_new'][str(j)],DY)
 oldminus=word(Y['negative_q0_in_new'][str(j)],DY)
 assert mul(mul(inv(k),DY[j]),k)==oldplus
 assert mul(mul(k,DY[j]),inv(k))==oldminus
 sourcechecks.append({'generator':j,'h_positive':plus,'h_negative':minus,'old_positive':oldplus,'old_negative':oldminus})
#Independent exact prefix theta and both inverse K substitutions.
def red(w):
 s=[]
 for j in w:
  if s and s[-1]==-j:s.pop()
  else:s.append(j)
 return tuple(s)
def wi(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(x for j in w for x in(A[abs(j)]if j>0 else wi(A[-j])))
O={1:(1,2,-1),2:(1,),3:(5,3,4,-3,-5),4:(3,),5:(-3,5,3)}
KO={1:(2,),2:(-2,1,2),3:(4,),4:(-5,-4,3,4,5),5:(4,5,-4)}
for j in range(1,6):assert sub(O[j],KO)==sub(KO[j],O)==(j,)
prefix={i:tuple(range(1,i+1))for i in range(1,6)}
prefix_inv={1:(1,),**{i:(-(i-1),i)for i in range(2,6)}}
theta={i:sub(sub(KO[i],prefix),O)for i in range(1,6)}
theta_inv={i:sub(sub(KO[i],prefix_inv),O)for i in range(1,6)}
for j in range(1,6):assert sub(theta[j],theta_inv)==sub(theta_inv[j],theta)==(j,)
assert theta[1]==(1,2)
v=word(theta[1],DG);assert v==(U['a'][0]^B[0],idp)
assert v[0]==(1<<2)^(1<<4)
assert comm(k,U['a'])==unit
#No translation can change conjugation of the pure vector v:
#(m,p)(v,1)(m,p)^-1=(p.v,1), by the semidirect product law.
#Check the linear evaluator on0 and the twelve basis translations for each
#of the three prescribed transpositions; the algebra proves all m at once.
transpositions=[p for p in permutations(range(3))if sign(p)==1]
assert len(transpositions)==3
transchecks=[]
for p in transpositions:
 delta=act(p,v[0])^v[0];assert delta
 for m in [0]+[1<<i for i in range(12)]:
  g=(m,p)
  assert comm(g,v)==(delta,idp)
 transchecks.append({'permutation':p,'permutation_1based':[i+1 for i in p],
   'moved_theta_a_vector':act(p,v[0]),'commutator_vector':delta,
   'nonzero_lamp_coordinates':[(('a','b','d','e')[i//3],i%3+1)for i in range(12)if(delta>>i)&1]})
#Every conjugate of image(k) has a transposition head. Verify all six
#head conjugations only; arbitrary translations are already immaterial.
allp=list(permutations(range(3)))
for p in allp:assert pm(pm(p,kperm),pinv(p))in transpositions
#Coarse compatibility: graph U-lamps have identity head, C/k as prescribed,
#z=1. More strongly sign(head)=orientation+geometric base winding mod2.
#Use the actual seven regional free-product generators a,B,d,e,f,C,k.
orientation={1:0,2:0,3:0,4:0,5:0,6:1,8:0}
winding={1:0,2:0,3:0,4:0,5:0,6:0,8:1}
for j,img in DG.items():assert sign(img[1])==(orientation[j]+winding[j])%2
assert sign(h[1])==1 and sign(z[1])==0
#This is an epimorphism onto the entire declared finite group: C,k generate
#S3 and their conjugates of each family lamp give all twelve independent axes.
heads={idp};changed=True
while changed:
 changed=False
 for p in list(heads):
  for q in(Cperm,kperm):
   r=pm(p,q)
   if r not in heads:heads.add(r);changed=True
assert len(heads)==6
axes={act(p,U[name][0])for p in heads for name in U}
assert axes=={1<<i for i in range(12)}
out={'status':'PASS_FULL_REGIONAL_PREFIX_CONJUGATE_OBSTRUCTION',
 'inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths},
 'target':{'name':'(F_2)^({a,b,d,e} x {1,2,3}) semidirect S3','order':2**12*6,
   'permutation_convention':'functional composition p*q=p after q','generators_Y':DY,
   'surjective':True,'coarse_factor':'(C2(C)*Z(k)) x Z(z) -> S3, C=(23),k=(12),z=1'},
 'actual_seventeen_relations':relchecks+[{'name':'cone_square','word':[6,6],'value':unit}],
 'ten_original_node_relations':rawchecks,'all_signed_source_and_old_actions':sourcechecks,
 'theta_K':theta,'theta_K_inverse':theta_inv,'theta_a_word':theta[1],'theta_a_image':v,
 'all_transposition_obstructions':transchecks,
 'coarse_parity_identity':{'formula':'sign(head)=orientation+geometric_base_winding mod2','orientation':orientation,'base_winding':winding},
 'proved_strength':['No element with transposition coarse head centralizes image(theta(a)).',
 'No regional conjugate of k, nor any graph-kernel correction retaining such a head, centralizes theta(a).',
 'No ordinary regional element of odd geometric base winding centralizes theta(a), discretely or in the full profinite completion.',
 'Thus theta cannot extend to a regional endomorphism sending k to an ordinary odd-base-winding element; no proposed cone image is needed.'],
 'scope':'One explicit surjective finite quotient of the whole actual regional group. No post-cross survival, arbitrary changed-presentation exclusion, final one-neck centralizer or main decision is asserted.'}
(P/'prefix_conjugate_obstruction24.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all17 complete actual regional defining relators')
print('PASS all10 original adapted node words and24 signed source/old-action comparisons')
print('PASS both five-generator prefix inverses; literal theta(a)=aB')
print('PASS prescribed quotient onto2^12 semidirect S3, order',2**12*6)
for row in transchecks:print('Transposition',row['permutation_1based'],'commutator lamps',row['nonzero_lamp_coordinates'])
print('PASS arbitrary translation-independent obstruction, all three transposition heads')
print('PASS coarse identity sign=orientation+base_winding mod2')
print('CONCLUSION no conjugate-k or ordinary odd-base-winding extension of theta, in discrete/full profinite scope')
