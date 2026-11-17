#!/usr/bin/env python3
"""Exact basis and operator certificate for the whole one-sided m subgroup."""
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source/one_sided_source_detector26.json'
D=json.loads(P.read_text())
def red(w):
 o=[]
 for z in w:
  if o and o[-1]==-z:o.pop()
  else:o.append(z)
 return o
def inv(w):return [-z for z in w[::-1]]
def mul(*ws):return red([z for w in ws for z in w])
def sub(w,M):return red([z for x in w for z in (M[abs(x)] if x>0 else inv(M[abs(x)]))])
def con(h,w):return mul(h,w,inv(h))
new_to_old={1:[1],2:[2],3:[3],4:[5,3,4,-3,-5],5:[5],6:[-1,6,1],7:[7,1,5]}
old_to_new={1:[1],2:[2],3:[3],4:[-3,-5,4,5,3],5:[5],6:[1,6,-1],7:[7,-5,-1]}
for i in range(1,8):
 assert sub(new_to_old[i],old_to_new)==[i]
 assert sub(old_to_new[i],new_to_old)==[i]
maps={}
for s in ['m','m_inverse']:
 mp={int(k):v for k,v in D['all_four_signed_free7_source_actions'][s].items()}
 maps[s]={i:sub(sub(new_to_old[i],mp),old_to_new) for i in range(1,8)}
kappa=[-5,6]
expected={1:[1],2:con(kappa,[2]),3:[3],4:con(kappa,[4]),5:[-5,6,5],6:[5],7:[7]}
assert maps['m']==expected
expected_inverse={1:[1],2:con([6,-5],[2]),3:[3],4:con([6,-5],[4]),5:[6],6:[6,5,-6],7:[7]}
assert maps['m_inverse']==expected_inverse
q=[6,5];qp=[5,6]
assert sub(q,maps['m'])==q
for i in [5,6]:
 assert sub(sub([i],maps['m']),maps['m'])==con(inv(q),[i])
kappa2=mul(sub(kappa,maps['m']),kappa)
assert kappa2==mul(inv(q),qp)
assert qp==con([5],q)
assert mul(kappa,[5])==[-5,6,5]

# Four actual source contacts are changed by literal free basis maps.
# Input source alphabet is s1,s2,s3,s4; output a,B,d,E.
As=[1,-4,-1]
Bs=con(inv(As),[-1])
Ds=[2,1,-3,-1,-2]
Es=[-2]
four_to_source={1:As,2:Bs,3:Ds,4:Es}
source_to_four={1:[1,-2,-1],2:[-4],
               3:[1,2,-1,4,-3,-4,1,-2,-1],
               4:[1,2,-1,-2,-1]}
for i in range(1,5):
 assert sub(four_to_source[i],source_to_four)==[i]
 assert sub(source_to_four[i],four_to_source)==[i]
source_old={int(k):v for k,v in D['source_contact_plus_retained_basis'].items()}
for i in range(1,5):
 assert sub(four_to_source[i],source_old)==new_to_old[i]

out={'status':'PASS','input':str(P.relative_to(ROOT)),'input_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),
 'new_basis':['a','B','d','E=f d e d^-1 f^-1','f','h=a^-1 g a','y=x a f'],
 'new_to_old':new_to_old,'old_to_new':old_to_new,'actual_signed_m_actions':maps,
 'kappa':kappa,'q':q,'qprime':qp,'kappa2':kappa2,
 'four_to_source':four_to_source,'source_to_four':source_to_four,
 'universal_formula':'kappa_(2n)=(hf)^(-n)(fh)^n; kappa_(2n+1)=(hf)^(-n)(f^-1 h)(fh)^n for every n in Z',
 'checks':{'free7_basis_inverse':14,'signed_m_generator_comparisons':14,'source_four_inverse':8,'source_to_actual_basis':4},
 'scope':'Exact entire m-direction subgroup in the one-sided quotient only. Actual [m,D_s] is not asserted.'}
Q=ROOT/'work_CE/next_symmetric_nodes/one_sided_m_normal_form26.json'
Q.write_text(json.dumps(out,indent=2)+'\n')
print('PASS all14 free7 basis inverses and14 signed m generator images.')
print('PASS exact alpha(q)=q, alpha^2=Inn(q^-1) on F(f,h), and kappa2=q^-1 qprime.')
print('PASS all8 contact-basis inverse identities and4 actual quotient comparisons.')
print('A_s=',As,'; B_s=',Bs,'; D_s=',Ds,'; E_s=',Es)
print('The all-integer orbit and whole-subgroup conclusion are proved in the companion note, not inferred from a finite orbit test.')
