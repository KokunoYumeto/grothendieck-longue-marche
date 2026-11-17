#!/usr/bin/env python3
"""Exact prescribed coarse-height substitution test; no group census."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[2];P=ROOT/'work_CE/next_symmetric_nodes'
#1=kminus,2=cminus,3=kplus,4=cplus. Cones square to one.
def red(w):
 o=[]
 for x in w:
  if abs(x)in(2,4):x=abs(x)
  if o and(o[-1]==-x or o[-1]==x and x in(2,4)):o.pop()
  else:o.append(x)
 return tuple(o)
def inv(w):return red(-x for x in w[::-1])
def mul(*ws):return red(x for w in ws for x in w)
def sub(w,A):return red(x for y in w for x in(A[abs(y)] if y>0 else inv(A[-y])))
def comm(a,b):return mul(a,b,inv(a),inv(b))
T={1:(1,2,1,2,-1),2:(1,2,-1),3:(4,3,4),4:(4,-3,4,3,4)}
Ti={1:(2,1,2),2:(2,-1,2,1,2),3:(3,4,3,4,-3),4:(3,4,-3)}
for j in range(1,5):
 assert sub(T[j],Ti)==(j,)
 assert sub(Ti[j],T)==(j,)
#Normal form in P=(Z(kminus) x C2(cplus))*(Z(kplus) x C2(cminus)).
def nf(w):
 out=[]
 for x in w:
  f=0 if abs(x)in(1,4) else 1
  z=(1 if x>0 else -1) if abs(x)in(1,3) else 0
  c=1 if abs(x)in(2,4) else 0
  if out and out[-1][0]==f:
   _,zz,cc=out.pop();z+=zz;c=(c+cc)%2
  if z or c:out.append((f,z,c))
 return tuple(out)
r1=comm((4,),(1,));r2=comm((2,),(3,))
assert nf(r1)==nf(r2)==()
records=[]
for label,r in [('r1',r1),('r2',r2)]:
 for sign,A in [(1,T),(-1,Ti)]:
  w=sub(r,A);normal=nf(w);assert normal
  records.append({'relator':label,'height_sign':sign,'word':w,'normal_form_in_candidate_P':normal})
#Independent universal derivation of each regional f-action, from h=f k,
#[h,c]=1 and h k h^-1=c k c: phi_f(c)=c k^-1 c k c,
#phi_f(k)=c k c; inverse phi_f^-1(c)=k c k^-1,
#phi_f^-1(k)=k c k c k^-1. Tested as mutually inverse above.
result={'status':'PASS_REJECT_CANDIDATE_P','generator_labels':{'1':'kminus','2':'cminus','3':'kplus','4':'cplus'},
 'T_conjugation':T,'T_inverse_conjugation':Ti,'untranslated_cross_relators':[r1,r2],
 'factor0':'Z(kminus) x C2(cplus)','factor1':'Z(kplus) x C2(cminus)',
 'translated_relators':records,
 'conclusion':'The candidate P kills the two zero-height cross relations but fails all four one-step signed translates. It cannot be the full coarse actual height kernel. This does not refute the separate K0-normal-generation argument or decide the true coarse group.'}
(P/'annular_coarse_height23.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS both full four-generator substitution inverse identities')
print('PASS the two original cross relations vanish in candidate P')
for r in records:print(r['relator'],r['height_sign'],'nontrivial reduced syllables',len(r['normal_form_in_candidate_P']),r['normal_form_in_candidate_P'])
print('REJECT candidate P as actual whole height kernel: all-height relations are essential')
