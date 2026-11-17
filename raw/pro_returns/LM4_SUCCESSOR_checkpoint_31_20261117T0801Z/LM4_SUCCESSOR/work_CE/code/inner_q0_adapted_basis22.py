#!/usr/bin/env python3
"""One actual q0-adapted basis and all ten regional relators simultaneously.

The change is made in the unfilled free group first.  The cone relation
then has index 3.  No claim that the q0 action descends to the slit
quotient is made (B111 proves that it does not).
"""
from pathlib import Path
import json,hashlib,time
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_CE/next_symmetric_nodes'
source=P/'inner_bad_orbifold_words22.json'
D=json.loads(source.read_text());q0=D['loops'][0]
def red(w,cone=0):
    out=[]
    for x in w:
        x=int(x)
        if cone and abs(x)==cone:x=cone
        if out and (out[-1]==-x or (cone and out[-1]==x==cone)):out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w,cone=0):return red((-x for x in reversed(w)),cone)
def mul(*words,cone=0):return red((x for w in words for x in w),cone)
def sub(w,A,cone=0):return mul(*(A[abs(x)] if x>0 else inv(A[-x],cone) for x in w),cone=cone)
def comp(A,B):return {i:sub(B[i],A) for i in range(1,7)}
def elementary(s):
    i=abs(s);A={j:(j,) for j in range(1,7)}
    if s>0:A[i]=(i,i+1,-i);A[i+1]=(i,)
    else:A[i]=(i+1,);A[i+1]=(-(i+1),i,i+1)
    return A
def push(word):
    A={j:(j,) for j in range(1,7)}
    for s in word:A=comp(elementary(s),A)
    return A
def conjugate(a,b,cone=0):return mul(a,b,inv(a,cone),cone=cone)
def peel(w,cone):
    w=list(red(w,cone));p=[]
    while len(w)>1 and (w[-1]==-w[0] or abs(w[0])==abs(w[-1])==cone):
        p.append(w.pop(0));w.pop()
    return tuple(p),tuple(w)
start=time.monotonic()
W=tuple(q0['whisker'])
J=push(tuple(-x for x in W[::-1]));Ji=push(W)
psi={int(k):tuple(v) for k,v in q0['positive_push'].items()}
psiinv={int(k):tuple(v) for k,v in q0['negative_pull'].items()}
L=push((3,3));Linv=push((-3,-3))
for i in range(1,7):
    assert sub(J[i],Ji)==(i,) and sub(Ji[i],J)==(i,)
    assert sub(sub(J[i],psi),Ji)==L[i]
    assert sub(sub(J[i],psiinv),Ji)==Linv[i]
    assert sub(sub((i,),psi),psiinv)==(i,)
C=J[3];F=J[4];K=(-3,1)
assert C==conjugate(K,(2,))
assert F==(5,6,-5)
cone_inverse=peel(Ji[2],3)
assert cone_inverse[1]==(3,)
v=(3,4,3)
source_action={i:conjugate(inv(v,3),L[i],3) for i in range(1,7)}
source_inverse={i:sub(conjugate(v,(i,),3),Linv,3) for i in range(1,7)}
for i in range(1,7):
    expected=(3,) if i==3 else ((3,4,3) if i==4 else conjugate(inv(v,3),(i,),3))
    assert source_action[i]==expected
    assert sub(source_action[i],source_inverse,3)==(i,)
    assert sub(source_inverse[i],source_action,3)==(i,)
rels=[]
for loop in D['loops'][1:]:
    for node in loop['nodes']:
        raw=tuple(node['relation']);new=sub(raw,Ji,3)
        assert sub(new,J,2)==red(raw,2)
        mer=[sub(tuple(w),Ji,3) for w in node['meridians']]
        pp,cc=peel(new,3)
        assert conjugate(pp,cc,3)==new
        rels.append({'name':loop['name'],'physical_labels':node['physical_labels'],
           'kind':node['kind'],'old_relation':raw,'new_relation':new,
           'new_meridians':mer,'cyclic_prefix':pp,'cyclic_core':cc})
        print(loop['name'],node['physical_labels'],'old',len(red(raw,2)),
              'new',len(new),'cyclic',len(cc),flush=True)
assert len(rels)==10
out={'status':'PASS','elapsed_seconds':time.monotonic()-start,
 'inputs':{str(source.relative_to(ROOT)):hashlib.sha256(source.read_bytes()).hexdigest()},
 'q0_whisker':W,'Y_in_old':J,'old_in_Y':Ji,
 'cone_index':3,'branch_index':4,'other_indices':[1,2,5,6],
 'old_cone_in_new':Ji[2],'old_cone_peeling':cone_inverse,
 'C_in_old':C,'F_in_old':F,'old_cone_connector_K':K,
 'positive_q0_in_new':L,'negative_q0_in_new':Linv,
 'source_h_equals_g0_times_CFC':v,'source_h_action':source_action,
 'source_h_inverse_action':source_inverse,'all_ten_relations':rels,
 'scope':'Exact change of the entire annular presentation, including all ten filled relators and the source stable generator. No slit-quotient automorphism, edge injection, or annular centralizer is inferred.'}
(P/'inner_q0_adapted_basis22.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS twelve free-basis inverses; twelve q0 local comparisons')
print('PASS simultaneous ten relation round trips; source h action and inverse')
print('PASS',round(out['elapsed_seconds'],6),'seconds')
