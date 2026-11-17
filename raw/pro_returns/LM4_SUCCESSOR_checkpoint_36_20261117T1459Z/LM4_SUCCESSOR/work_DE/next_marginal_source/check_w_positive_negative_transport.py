"""Exact common-marked comparison of the five filled nodes and positive triples.

The actual source-based positive action on a conjugated triple includes
the change of the diagonal conjugator.  This correction is checked, not
suppressed.  A local centrality relation is not by itself an action by an
element of the whole source subgroup in that new marking.
"""
from pathlib import Path
import json,hashlib
from weighted_stallings import multiply as m,inverse as inv,substitute as sub,WeightedFold
P=Path(__file__).resolve().parent
local=json.loads((P/'w_local_markings.json').read_text())
b=json.loads((P/'w_source_adapted_basis.json').read_text())
back={int(k):tuple(w) for k,w in b['initial_basis_in_new'].items()}
source={int(k):tuple(w) for k,w in b['all_source_words_in_new'].items()}
source_order=sorted(source)
fold=WeightedFold([source[j] for j in source_order],allow_relations=True)
def comm(x,y):return m(x,y,inv(x),inv(y))
def peel(w):
    h=[]
    while len(w)>1 and w[0]==-w[-1]:h.append(w[0]);w=w[1:-1]
    return tuple(h),tuple(w)
def conjugate(h,w):return m(h,w,inv(h))
z,c1,c2,c3,c4,p1,p2,p3,p4,a,d,bb=[(j,) for j in range(1,13)]
T=m(bb,a,d,bb)
minus={j:source[i] for j,i in enumerate([17,19,21,23],1)}
M=m(z,c3,c4)
expected_nodes=[
    conjugate(m(inv(m(bb,a)),M),bb),
    conjugate(m(inv(m(bb,a)),inv(c3),inv(z),T),inv(p2)),
    conjugate(inv(a),inv(minus[4])),
    inv(minus[1]),
    conjugate(inv(conjugate(bb,c1)),inv(minus[3]))]
nodes=[];triples=[]
for rr in local['all_local_markings'][1:11]:
    k=int(rr['name'].rsplit('_',1)[1]);pn=7+(2*k)%5
    per={int(j):sub(w,back) for j,w in rr['transported_peripheral_words_by_label'].items()}
    h,core=peel(per[6]);assert core==d
    normalized={j:conjugate(inv(h),per[j]) for j in [6,pn]}
    if rr['name'].startswith('filled_negative_'):
        q=expected_nodes[k]
        raw=normalized[pn]
        assert raw==(conjugate(inv(d),q) if k==0 else q)
        r=comm(d,raw)
        assert comm(per[6],per[pn])==conjugate(h,r)
        simple=comm(d,q)
        assert r==(conjugate(inv(d),simple) if k==0 else simple)
        nodes.append({'index':k,'actual_diagonal_conjugator':h,'normalized_product_meridian':raw,'simplified_commuting_word':q,'relation':simple,'literal_source_expression':fold.rewrite(q)})
        print('negative',k,'relation [d,Q]=1; Q=',list(q))
    elif k:
        normalized[1+k]=conjugate(inv(h),per[1+k])
        order=[j for j in rr['local_order'] if j in normalized]
        K=m(*(normalized[j] for j in order))
        act={int(j):tuple(w) for j,w in b['actions_in_new'][str(rr['index'])].items()}
        L=m(inv(sub(h,act)),h,K)
        for v in normalized.values():assert sub(v,act)==conjugate(L,v)
        expected_L=m(comm(a,inv(minus[k])),K) if k in [1,2] else K
        assert L==expected_L
        if k in [1,2]:assert normalized[1+k]==conjugate(bb,inv((k+1,)))
        if k==1:assert normalized[pn]==inv(minus[2])
        triples.append({'index':k,'actual_diagonal_conjugator':h,'normalized_triple':normalized,'local_boundary_order':order,'boundary_word':K,'actual_source_action_conjugator':L,'correction_before_boundary':m(L,inv(K))})
        print('positive',k,'actual normalized action is Inn(L), L=',list(L),'correction=',list(m(L,inv(K))))
assert len(nodes)==5 and len(triples)==4
out={'description':__doc__,'basis_names':['z','c1','c2','c3','c4','p1','p2','p3','p4','a','d','b'],'negative_nodes':nodes,'positive_triples':triples,'source_minus_products':minus,'input_sha256':{n:hashlib.sha256((P/n).read_bytes()).hexdigest() for n in ['w_local_markings.json','w_source_adapted_basis.json']},'scope':'Every relation is a genuine based transported relation of the actual surface. The filled-node equations hold in the actual group. The source action is literal. No new whole partial-kernel normalizer or local-subgroup injection is inferred.'}
(P/'w_positive_negative_transport.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS all5 actual filled nodes, all4 actual normalized triple actions, and compact matching identities')
