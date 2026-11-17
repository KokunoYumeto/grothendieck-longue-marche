"""Exact whole-block transport and based infinity check in the tangent bundle.

This proves a complete one-direction free-factor intersection, not full normality.
"""
from pathlib import Path
import json
from weighted_stallings import WeightedFold,multiply as mul,inverse as inv,substitute as sub
HERE=Path(__file__).resolve().parent
ns={'__file__':str(HERE/'extract_tangent_bundle_fiber.py')}
s=(HERE/'extract_tangent_bundle_fiber.py').read_text();exec(s[:s.index('def A_i')],ns)
d=json.loads((HERE/'tangent_bundle_nielsen_actions.json').read_text())
new_old={int(i):tuple(w) for i,w in d['new_basis_in_old'].items()};old_new={int(i):tuple(w) for i,w in d['old_basis_in_new'].items()}
new2_old1={i:(i,) for i in range(1,8)};new2_old1[3]=(-6,3,6);new2_old1[5]=(-6,5,6)
old1_new2={i:(i,) for i in range(1,8)};old1_new2[3]=(6,3,-6);old1_new2[5]=(6,5,-6)
new2_old={i:sub(new2_old1[i],new_old) for i in range(1,8)};old_new2={i:sub(old_new[i],old1_new2) for i in range(1,8)}
for i in range(1,8):assert sub(new2_old[i],old_new2)==(i,) and sub(old_new2[i],new2_old)==(i,)
A1={int(i):tuple(w) for i,w in d['old_actions_new_basis']['1'].items()};A1={i:sub(sub(new2_old1[i],A1),old1_new2) for i in range(1,8)}
D=(5,7);assert sub(D,A1)==D
U=(1,2,4,6)
psi={j:mul(D,A1[j],inv(D)) for j in U}
assert all(all(abs(a) in U for a in w) for w in psi.values())
f=WeightedFold(list(psi.values()));back={j:f.rewrite((j,)) for j in U};assert all(w is not None for w in back.values())
print('alpha1(D)=D for D=BC: PASS')
print('alpha1(U)=D^-1 U D; internal U automorphism and explicit inverse verified: PASS')
# Verify the exact minimal six-action orbit reformulation.
raw=json.loads((HERE/'tangent_bundle_fiber_data.json').read_text())
source=[sub(w,old_new2) for w in raw['new_fiber_words'].values()]
generators=[(j,) for j in U]+[A1[j] for j in U]
g=WeightedFold(generators,allow_relations=True)
seed_back=[g.rewrite(w) for w in source];assert all(w is not None for w in seed_back)
print('Original four source seeds lie in <U,alpha1(U)>; reverse U containment is certified separately: PASS')
inf=json.loads((HERE/'tangent_infinity_braid.json').read_text());A=ns['action'](tuple(inf['word']));Ai=ns['action'](inv(inf['word']))
A={i:sub(sub(new2_old[i],A),old_new2) for i in range(1,8)};Ai={i:sub(sub(new2_old[i],Ai),old_new2) for i in range(1,8)}
for i in range(1,8):assert sub(A[i],Ai)==(i,) and sub(Ai[i],A)==(i,)
filled={}
for j in U:
 w=A[j];k=0
 while len(w)-2*k>1 and w[k]==-w[-1-k]:k+=1
 assert w[k:len(w)-k]==(j,)
 filled[j]=mul(tuple(a for a in w[:k] if abs(a) in (3,5,7)))
print('Actual infinity action/inverse PASS; filled U-conjugator indices:',filled)
assert len(set(filled.values()))>1
print('Infinity does not present one common retained conjugator in this marking; no additional normalizer inferred.')
out={'description':__doc__,'basis_new2_in_original':new2_old,'basis_original_in_new2':old_new2,'D':D,'alpha1_in_new2':A1,'internal_U_automorphism':psi,'internal_U_inverse_expressions':back,'source_seed_expressions_in_U_and_alpha1U':seed_back,'alpha_infinity_in_new2':A,'alpha_infinity_inverse_in_new2':Ai,'infinity_filled_U_conjugators':filled,'proved_scope':'For every integer n, D^n U D^-n lies in I. Thus I intersect (U*<D>) equals ker(U*<D>-><D>), also for actual compact images under free-factor completion.','not_proved':['D normalizes all I','all retained directions normalize I','I=R']}
(HERE/'tangent_infinity_action.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS exact whole-block certificate; only the stated one-direction intersection is proved.')
