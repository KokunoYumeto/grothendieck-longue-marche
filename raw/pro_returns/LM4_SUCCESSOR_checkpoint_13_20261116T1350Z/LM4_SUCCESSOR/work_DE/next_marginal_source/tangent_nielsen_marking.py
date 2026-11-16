"""Exact source-contained Nielsen marking for the smaller tangent bundle.

The four killed basis generators belong to the actual source image.
This is a finite marking statement; whole retained normalization is open.
"""
from pathlib import Path
import json
from weighted_stallings import multiply as mul,inverse as inv,substitute as sub
HERE=Path(__file__).resolve().parent
d=json.loads((HERE/'tangent_bundle_fiber_data.json').read_text())
f=json.loads((HERE/'tangent_seed_basis.json').read_text())
actions={int(k)+1:{int(i):tuple(w) for i,w in A.items()} for k,A in d['old_actions'].items()}
actions.update({-int(k)-1:{int(i):tuple(w) for i,w in A.items()} for k,A in d['old_inverse_actions'].items()})
rows=f['source_orbit_words'][:f['fold_steps'][1]['word_count']]
words={i+1:tuple(r['word']) for i,r in enumerate(rows)}
for r in rows:
 w=inv(d['new_fiber_words'][str(r['seed'])])
 for a in r['action_path']:w=sub(w,actions[a])
 assert w==tuple(r['word'])
exp={int(i):None if w is None else tuple(w) for i,w in f['fold_steps'][1]['expansions'].items()}
for i in (2,4,6):assert sub(exp[i],words)==(i,)
new_old={i:(i,) for i in range(1,8)};new_old[1]=(-3,-2,1,2,3)
old_new={i:(i,) for i in range(1,8)};old_new[1]=(2,3,1,-3,-2)
for i in range(1,8):assert sub(new_old[i],old_new)==(i,) and sub(old_new[i],new_old)==(i,)
# Original positive seed2 is x6^-1*(new generator1)*x6.
exp[1]=mul(exp[6],(2,),inv(exp[6]))
for i in (1,2,4,6):assert sub(exp[i],words)==new_old[i]
print('All52 source-orbit words re-evaluated from the original four seeds: PASS')
print('Four killed Nielsen generators lie in the actual source image; both basis changes invert: PASS')
keep={3,5,7}
def fill(w):return mul(tuple(a for a in w if abs(a) in keep))
def peripheral(w):
 j=0
 while len(w)-2*j>1 and w[j]==-w[-1-j]:j+=1
 return w[j:len(w)-j],w[:j]
def support(w):
 g=();out=[]
 for a in w:
  if abs(a) in keep:g=mul(g,(a,))
  else:
   term=(g,abs(a),1 if a>0 else -1)
   if out and out[-1][0:2]==term[0:2] and out[-1][2]==-term[2]:out.pop()
   else:out.append(term)
 return g,out
out={};inverses={};support_data={}
for k in range(6):
 A={i:sub(sub(new_old[i],actions[k+1]),old_new) for i in range(1,8)}
 Ai={i:sub(sub(new_old[i],actions[-k-1]),old_new) for i in range(1,8)}
 for i in range(1,8):assert sub(A[i],Ai)==(i,) and sub(Ai[i],A)==(i,)
 out[k]=A;inverses[k]=Ai
 sup={}
 for i in (1,2,4,6):
  core,c=peripheral(A[i]);assert core==(i,)
  v,s=support(c);sup[i]={'filled_conjugator':v,'free_kernel_support':s}
 if k>=2:assert all(fill(A[i])==(i,) for i in keep)
 support_data[k]=sup
assert out[0][1]==(3,-5,1,5,-3) and out[0][4]==(3,-5,4,5,-3)
assert out[0][2]==(2,) and out[0][6]==(6,)
print('Six actual automorphisms and inverses in the new marking: PASS')
print('q0 sends U1,U4 by conjugation with x3*x5^-1, fixes U2,U6; other four old actions fill to identity: PASS')
result={'scope':__doc__,'source_orbit_words':rows,'killed_basis_source_expansions':exp,'new_basis_in_old':new_old,'old_basis_in_new':old_new,'old_actions_new_basis':out,'old_inverse_actions_new_basis':inverses,'peripheral_kernel_support':support_data,'retained_basis':[3,5,7],'killed_basis':[1,2,4,6],'not_proved':['uniform invariance under retained conjugations','source image equals R']}
(HERE/'tangent_bundle_nielsen_actions.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS; the whole source-kernel normality condition is not inferred.')
