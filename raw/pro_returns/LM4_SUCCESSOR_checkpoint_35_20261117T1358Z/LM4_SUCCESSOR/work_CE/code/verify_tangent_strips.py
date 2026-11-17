"""Independent source-word and whole cyclic-strip input audit.

No producer or Stallings implementation is imported.  All returned source
expansions are checked by direct free substitution from the four real seeds.
"""
from pathlib import Path
import hashlib,json,time
ROOT=Path(__file__).resolve().parents[2]
P=ROOT/'work_DE/next_marginal_source'
raw=json.loads((P/'tangent_bundle_fiber_data.json').read_text())
mark=json.loads((P/'tangent_infinity_action.json').read_text())
data=json.loads((P/'tangent_node_strips.json').read_text())
first=json.loads((P/'tangent_bundle_nielsen_actions.json').read_text())
start=time.monotonic()
def red(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return tuple(out)
def inv(w):return tuple(-x for x in reversed(w))
def sub(w,A):return red(x for i in w for x in (A[i] if i>0 else inv(A[-i])))
def maps(d):return {int(i):tuple(w) for i,w in d.items()}
act={int(k)+1:maps(A) for k,A in raw['old_actions'].items()}
act.update({-int(k)-1:maps(A) for k,A in raw['old_inverse_actions'].items()})
words={}
for i,row in enumerate(data['source_orbit_words'],1):
    w=inv(raw['new_fiber_words'][str(row['seed'])])
    for k in row['action_path']:w=sub(w,act[k])
    assert w==tuple(row['word'])
    words[i]=w
newold=maps(mark['basis_new2_in_original']);oldnew=maps(mark['basis_original_in_new2'])
for i in range(1,8):
    assert sub(newold[i],oldnew)==(i,) and sub(oldnew[i],newold)==(i,)
for i,e in data['adjacent_source_expansions'].items():
    assert sub(e,words)==sub((-5,int(i),5),newold)
first_words={i+1:tuple(r['word']) for i,r in enumerate(first['source_orbit_words'])}
for i,e in first['killed_basis_source_expansions'].items():
    assert sub(e,first_words)==newold[int(i)]
print('All',len(words),'literal source-orbit words and adjacent source expansions PASS.')
A={k:{i:sub(sub(newold[i],act[k+1]),oldnew) for i in range(1,8)} for k in range(6)}
h=tuple(data['tangency_inner_word'])
assert h==(6,5,6,5)
for i in (5,6):assert A[5][i]==red(h+(i,)+inv(h))
assert A[0][5]==(3,) and A[0][6]==(6,)
V=maps(data['V_basis_in_new2']);Vi=maps(data['new2_basis_in_V'])
for i in range(1,8):assert sub(V[i],Vi)==(i,) and sub(Vi[i],V)==(i,)
for row in data['node_restrictions']:
    j,k=row['deleted_label'],row['base_action'];v=tuple(row['v']);q=tuple(row['inner_word'])
    assert v==V[j] and q==red(v+(7,))
    assert sub(v,A[k])==red(q+v+inv(q))
    assert A[k][7]==red(q+(7,)+inv(q))
print('Width-two tangency, root transfer, four width-one nodes, and full V-basis PASS.')
# Whole D-strip input, in the same actual new2 marking.
D=(5,7)
assert sub(D,A[1])==D
theta={1:(2,1,-2),2:(2,1,2,-1,-2),4:(4,6,4,-6,-4),6:(4,6,-4)}
thetai={1:(-1,-2,1,2,1),2:(-1,2,1),4:(-6,4,6),6:(-6,-4,6,4,6)}
for i in theta:
    assert A[1][i]==red(inv(D)+theta[i]+D)
    assert sub(theta[i],thetai)==(i,) and sub(thetai[i],theta)==(i,)
print('Whole D=BC block transport and exact internal inverse PASS.')
result={'scope':__doc__,'source_orbit_count':len(words),'all_literal_checks':True,
        'elapsed_seconds':time.monotonic()-start,
        'input_hashes':{name:hashlib.sha256((P/name).read_bytes()).hexdigest() for name in
         ['tangent_bundle_fiber_data.json','tangent_infinity_action.json','tangent_node_strips.json',
          'tangent_bundle_nielsen_actions.json']},
        'proved_after_elementary_propagation':[
         'I intersect <B,U6> is its filling kernel',
         'I intersect <A,U6> is its filling kernel',
         'I intersect (V*<C>) is its filling kernel',
         'I intersect (U*<BC>) is its filling kernel'],
        'not_proved':['whole I normalization','I=R']}
(ROOT/'work_CE/tangent_strips_independent_review.json').write_text(json.dumps(result,indent=2)+'\n')
