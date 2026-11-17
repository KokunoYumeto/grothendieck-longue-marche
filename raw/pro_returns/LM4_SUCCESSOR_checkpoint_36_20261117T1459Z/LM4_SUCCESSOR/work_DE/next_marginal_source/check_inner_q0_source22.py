#!/usr/bin/env python3
"""Actual old-cone q0 source lift and its q0-adapted based comparison."""
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[2]
paths=[ROOT/'work_CE/next_symmetric_nodes/inner_bad_orbifold_words22.json',
       ROOT/'records/inner_bad_normalized22.json',ROOT/'records/inner_bad_hnn22.json']
D,N,H=[json.loads(p.read_text()) for p in paths]
def reduce(w,cone=True):
 a=[]
 for x in w:
  x=2 if cone and abs(x)==2 else int(x)
  if a and (a[-1]==-x or cone and a[-1]==x==2):a.pop()
  else:a.append(x)
 return tuple(a)
def inverse(w,cone=True):return reduce((-x for x in reversed(w)),cone)
def mul(*ws,cone=True):return reduce((x for w in ws for x in w),cone)
def sub(w,A,cone=True):
 return mul(*(A[abs(x)] if x>0 else inverse(A[-x],cone) for x in w),cone=cone)
def conj(g,w,cone=True):return mul(g,w,inverse(g,cone),cone=cone)
def push(W):
 A={j:(j,) for j in range(1,7)}
 for letter in W:
  j=abs(letter);step={k:(k,) for k in range(1,7)}
  if letter>0:step[j]=(j,j+1,-j);step[j+1]=(j,)
  else:step[j]=(j+1,);step[j+1]=(-j-1,j,j+1)
  A={k:sub(w,step,False) for k,w in A.items()}
 return A
def even_conjugator(w):
 core=list(reduce(w));v=[]
 while len(core)>1 and (core[0]==-core[-1] or core[0]==core[-1]==2):
  v.append(core.pop(0));core.pop()
 assert core==[2]
 if sum(x==2 for x in v)%2:v.append(2)
 v=reduce(v)
 assert sum(x==2 for x in v)%2==0 and conj(v,(2,))==reduce(w)
 return v

q0=D['loops'][0];W0=tuple(q0['whisker'])
assert W0==(2,1,-2,-2,4,5,-4)
psi=push(q0['chronological_braid'])
psi_inv=push(inverse(q0['chronological_braid'],False))
assert psi=={int(k):tuple(v) for k,v in q0['positive_push'].items()}
assert psi_inv=={int(k):tuple(v) for k,v in q0['negative_pull'].items()}
v0=even_conjugator(psi[2]);vminus=even_conjugator(psi_inv[2])
assert vminus==sub(inverse(v0),psi_inv)
chi={j:conj(inverse(v0),psi[j]) for j in range(1,7)}
chi_inv={j:conj(inverse(vminus),psi_inv[j]) for j in range(1,7)}
assert chi[2]==(2,)==chi_inv[2]
for j in range(1,7):
 assert sub(chi[j],chi_inv)==(j,)==sub(chi_inv[j],chi)

# Literal local coordinates at the same transported q0 node.
J=push(inverse(W0,False));Jinv=push(W0)
for j in range(1,7):
 assert sub(J[j],Jinv,False)==(j,)==sub(Jinv[j],J,False)
Y=J;C=Y[3];F=Y[4];K=(-3,1)
assert C==(-3,1,2,-1,3) and F==(5,6,-5)
assert C==conj(K,(2,),False)
local=push((3,3))
for j in range(1,7):
 assert sub(Y[j],psi,False)==sub(local[j],Y,False)
vC=mul(C,F,C)
adapted={j:conj(inverse(vC),sub(Y[j],psi)) for j in range(1,7)}
assert adapted[3]==reduce(C)
assert adapted[4]==mul(C,F,C)
for j in (1,2,5,6):assert adapted[j]==conj(inverse(vC),Y[j])

# h_C=g0 CFC centralizes C, while h0=K^-1 h_C K centralizes
# the original cone c.  Moving K^-1 across g0 uses the actual
# g0^-1 x g0=psi(x) convention, so the right factor is literal.
candidate=mul(sub(inverse(K),psi),C,F,C,K)
assert candidate==v0
old_new={int(k):tuple(v) for k,v in N['old_in_new'].items()}
new_old={int(k):tuple(v) for k,v in N['new_in_old'].items()}
f_w={j:(j,) for j in range(1,7)};f_w[6]=tuple(H['branch_f_in_new_generators'])
vnew=sub(v0,old_new);vw=sub(vnew,f_w)
assert sub(K,old_new)==(1,-3)
new_chi={j:sub(sub(new_old[j],chi),old_new) for j in range(1,7)}
def reduce_at(word,cone):
 ans=[]
 for x in word:
  x=cone if abs(x)==cone else int(x)
  if ans and (ans[-1]==-x or ans[-1]==x==cone):ans.pop()
  else:ans.append(x)
 return tuple(ans)
contact_sources=[]
for loop in D['loops'][1:]:
 if len(loop['nodes'])!=1 or loop['nodes'][0]['kind']!='cone_contact':continue
 vi=even_conjugator(loop['positive_push']['2'])
 at_C=conj(K,vi)
 at_Y=reduce_at(sub(at_C,Jinv,False),3)
 assert sub(at_Y,Y)==at_C
 contact_sources.append({'name':loop['name'],'old_cone_source_word':vi,
                         'source_word_at_conjugate_cone_C':at_C,
                         'source_word_in_q0_adapted_Y_basis':at_Y})
assert len(contact_sources)==4

out={'status':'PASS','inputs':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
 'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'q0_whisker':W0,'geometric_positive_push':psi,'negative_pull':psi_inv,
 'unique_even_v0':v0,'unique_even_negative_conjugator':vminus,
 'actual_source_word':'h0=g0*v0; g0 is retained',
 'old_cone_corrected_operator':chi,'old_cone_corrected_inverse':chi_inv,
 'both_six_generator_inverse_compositions':12,
 'q0_adapted_basis_in_old':Y,'old_basis_in_q0_adapted':Jinv,
 'twelve_free_basis_inverse_compositions':12,
 'transported_cone_C':C,'transported_branch_F':F,'literal_even_connector_K':K,
 'K_in_same_sheet_basis':[1,-3],
 'adapted_source_word':'h_C=g0*C*F*C',
 'adapted_source_operator_on_Y_in_old':adapted,
 'actual_source_bridge':'h0=K^-1*h_C*K=g0*psi(K)^-1*C*F*C*K',
 'bridge_right_factor_equals_v0':candidate,
 'v0_in_same_sheet_basis':vnew,'v0_in_root_w_basis':vw,
 'corrected_operator_in_same_sheet_basis':new_chi,
 'four_contact_source_words_in_common_q0_marking':contact_sources,
 'fifth_source_generator_in_q0_marking':'h_C=g0*C*F*C',
 'scope':'Actual source F5 generators are four contact images plus h0. No injectivity or whole annular centralizer equality is inferred; corrected maps are automorphisms of the generic fiber, not asserted on the slit quotient.'}
Path(__file__).with_name('inner_q0_source22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS actual chronological q0 maps and unique even v0 / inverse conjugator.')
print('PASS corrected old-cone operator fixes c; both six-generator inverse compositions.')
print('PASS q0-adapted twelve basis inverses and all six corrected source images.')
print('PASS exact source bridge h0=K^-1(g0 CFC)K, K=x3^-1 x1=a b^-1.')
print('PASS all four contact-source round trips in the same q0-adapted cone marking.')
print('v0_raw',v0)
print('v0_same_sheet',vnew)
print('v0_root_w',vw)
