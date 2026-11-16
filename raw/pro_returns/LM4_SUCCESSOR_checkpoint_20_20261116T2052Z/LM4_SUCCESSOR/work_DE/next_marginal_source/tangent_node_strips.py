"""Exact tangency and node strips in actual source-contained free factors.

These prove specified intersections only, not normality of the whole orbit subgroup.
"""
from pathlib import Path
import json,time
from weighted_stallings import WeightedFold,multiply as mul,inverse as inv,substitute as sub
HERE=Path(__file__).resolve().parent
raw=json.loads((HERE/'tangent_bundle_fiber_data.json').read_text())
mark=json.loads((HERE/'tangent_infinity_action.json').read_text())
new_old={int(i):tuple(w) for i,w in mark['basis_new2_in_original'].items()};old_new={int(i):tuple(w) for i,w in mark['basis_original_in_new2'].items()}
original_actions={int(k)+1:{int(i):tuple(w) for i,w in A.items()} for k,A in raw['old_actions'].items()}
original_actions.update({-int(k)-1:{int(i):tuple(w) for i,w in A.items()} for k,A in raw['old_inverse_actions'].items()})
A={k:{i:sub(sub(new_old[i],original_actions[k+1]),old_new) for i in range(1,8)} for k in range(6)}
Ai={k:{i:sub(sub(new_old[i],original_actions[-k-1]),old_new) for i in range(1,8)} for k in range(6)}
records=json.loads((HERE/'tangent_seed_basis.json').read_text())['source_orbit_words']
for row in records:
 w=inv(raw['new_fiber_words'][str(row['seed'])])
 for a in row['action_path']:w=sub(w,original_actions[a])
 assert w==tuple(row['word'])
words={i+1:tuple(row['word']) for i,row in enumerate(records)}
f=WeightedFold(list(words.values()),allow_relations=True)
source_exp={}
for j in (2,6):
 target=mul((-5,),(j,),(5,));oldtarget=sub(target,new_old)
 back=f.rewrite(oldtarget);assert back is not None and sub(back,words)==oldtarget
 source_exp[j]=back
print('All580 stored orbit words re-evaluated; both adjacent B^-1 U2 B and B^-1 U6 B memberships certified: PASS')
# Tangency at q=u4^2: restriction to <B,U6> is inner by (U6 B)^2.
h=(6,5,6,5)
for j in (5,6):assert A[5][j]==mul(h,(j,),inv(h))
assert A[0][5]==(3,) and A[0][6]==(6,)
print('Actual tangency restriction Inn((U6 B)^2), and alpha0(B,U6)=(A,U6): PASS')
C=(7,)
V={1:(-6,1,6),4:(-6,4,6),6:(-5,6,5),2:(-5,-6,2,6,5)}
which={1:2,6:3,4:4,2:5}
node=[]
for j,k in which.items():
 v=V[j];hh=mul(v,C)
 assert sub(C,A[k])==mul(hh,C,inv(hh)),('C action',j,k)
 assert sub(v,A[k])==mul(hh,v,inv(hh)),('v action',j,k)
 node.append({'deleted_label':j,'base_action':k,'v':v,'inner_word':hh})
 print('Node',k,'on <C,V'+str(j)+'> is exactly Inn(V'+str(j)+' C): PASS')
# V together with the unchanged retained A,B,C is an actual free basis.
v_old={i:(i,) for i in range(1,8)};v_old.update(V)
old_v={i:(i,) for i in range(1,8)}
old_v[6]=(5,6,-5)
old_v[2]=(5,6,2,-6,-5)
old_v[1]=(5,6,-5,1,5,-6,-5)
old_v[4]=(5,6,-5,4,5,-6,-5)
for j in range(1,8):assert sub(v_old[j],old_v)==(j,) and sub(old_v[j],v_old)==(j,)
print('Both inverse maps for the four V generators plus A,B,C: PASS')
# V1,V4 are U words; V6 and V2 use the already certified adjacent words.
assert V[2]==mul(inv(mul((-5,),(6,),(5,))),mul((-5,),(2,),(5,)),mul((-5,),(6,),(5,)))
out={'description':__doc__,'basis_new2_in_original':new_old,'source_orbit_words':records,'adjacent_source_expansions':source_exp,'tangency_inner_word':h,'tangency_action':5,'root_half_action':0,'V_basis_in_new2':v_old,'new2_basis_in_V':old_v,'node_restrictions':node,'proved_intersections':['I intersect <B,U6> = ker(<B,U6>-><B>)','I intersect <A,U6> = ker(<A,U6>-><A>)','I intersect (V*<C>) = ker(V*<C>-><C>)'],'completed_scope':'Same equalities for actual compact intersections by the full free-factor embeddings and dense discrete filling kernels.','not_proved':['C normalizes all I','A or B normalizes all I','I=R']}
(HERE/'tangent_node_strips.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all exact strip inputs; whole I-normality is not asserted.')
