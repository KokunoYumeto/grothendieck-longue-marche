#!/usr/bin/env python3
"""Exact joint spinor/ordinary-period image of all360 actual source words."""
import numpy as np,json
from pathlib import Path
D=Path(__file__).parent;W=json.loads((D/'translation_quaternion_homology.json').read_text())['kernel_generator_words']
S=json.loads((D/'translation_quaternion_radical_certificate.json').read_text())['all_generator_spinor_norms']
I=(1,0,0,1);U=(1,1,0,1);L=(1,0,11,1)
def mul(a,b):return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%12 for i in range(2) for j in range(2))
def inv(a):return (a[3],-a[1]%12,-a[2]%12,a[0])
gens=[]
for w,s in zip(W,S):
 M=I
 for j in w:
  G=U if abs(j)==1 else L if abs(j)==2 else I
  M=mul(M,G if j>0 else inv(G))
 gens.append((int(s),M))
Q=[(1,I)];idx={Q[0]:0};words=[()]
for q,(s,A) in enumerate(Q):
 for j,(t,B) in enumerate(gens):
  h=(s*t%3,mul(A,B))
  if h not in idx:idx[h]=len(Q);Q.append(h);words.append(words[q]+(j+1,))
print('JOINT spinor/period order',len(Q),'period image',len({a for s,a in Q}),'spinor fibres',sorted({s for s,a in Q if a==I}),flush=True)
for i,(s,a) in enumerate(gens):
 if s==2:
  print('FIRST NONSQUARE',i,'period',a,'word',W[i],flush=True);break
# Explicit kernel witness if spinor and periods are independent.
witness=words[idx[(2,I)]] if (2,I) in idx else None
print('Nonsquare period-identity witness',witness,flush=True)
Path(__file__).with_suffix('.json').write_text(json.dumps({'scope':'Exact joint image of spinor and ordinary compact-period mod12, on complete quaternion-automorphism-kernel generators',
 'joint_order':len(Q),'period_order':len({a for s,a in Q}),'period_identity_spinor':[s for s,a in Q if a==I],
 'source_generators':[{'spinor':s,'period':a,'word15':w} for (s,a),w in zip(gens,W)],
 'joint_elements':[{'spinor':s,'period':a,'word360':w} for (s,a),w in zip(Q,words)],
 'nonsquare_period_identity_word360':witness},indent=2)+'\n')
# Exact character on the eight mod-four period residues, in the primitive
# upstairs handle basis (A,B); conjugation by the retained swap J exchanges
# beta and gamma and leaves the character unchanged.
eta={}
for s,a in Q:
 a4=tuple(x%4 for x in a)
 if a4 in eta:assert eta[a4]==s
 eta[a4]=s
 alpha=((a4[0]-1)%4)//2;beta=a4[1]//2;gamma=a4[2]//2
 assert a4[3]==a4[0] and a4[0]%2==1 and a4[1]%2==a4[2]%2==0
 assert s==pow(2,alpha+beta+gamma,3)
assert len(eta)==8 and len(Q)==192
report=json.loads(Path(__file__).with_suffix('.json').read_text());report['period_basis']='primitive upstairs compact handle basis (A=b^3,B=a^3); conversion to (3a,3b) is the retained swap J'
report['spinor_character_mod4']=[{'matrix':a,'spinor':s} for a,s in eta.items()]
Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
print('PASS spinor=(-1)^(alpha+beta+gamma) on all eight mod4 residues',flush=True)
