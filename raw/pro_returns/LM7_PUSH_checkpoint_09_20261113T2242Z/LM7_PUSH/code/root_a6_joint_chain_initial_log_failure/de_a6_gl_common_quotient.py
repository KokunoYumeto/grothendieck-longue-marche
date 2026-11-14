#!/usr/bin/env python3
"""Literal maximum common source quotients for the A6 and signed A5 tests.

The maps use one B-induced A5 epikernel (its B orbit has three distinct
F-epikernels), together with ordinary exponent sums modulo15 or30.
Complete source-presentation tests prove the epikernel factorizations.
The independent whole-source order certificates prove maximality only
after these specified quotient maps have been constructed.
"""
from pathlib import Path
from collections import deque
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_a5_model import FerrariA5
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent


def json_read(name):return json.loads((HERE/name).read_text())
def last(name):return json.loads((HERE/name).read_text().splitlines()[-1])


def evaluate_selected(nodes,targets,originals):
    """Independent right-permutation DAG evaluation, retaining only ancestors."""
    wanted=set(targets);stack=list(targets)
    while stack:
        i=stack.pop();op,a,b=nodes[i]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            assert 0<=j<i
            if j not in wanted:wanted.add(j);stack.append(j)
    refs={i:0 for i in wanted}
    for i in wanted:
        op,a,b=nodes[i]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):refs[j]+=1
    values={};answer={};identity=np.arange(len(originals[0]),dtype=np.int64)
    for i in sorted(wanted):
        op,a,b=nodes[i]
        if op==0:v=identity
        elif op==1:v=originals[a]
        elif op==2:v=values[b][values[a]]
        elif op==3:v=np.argsort(values[a])
        elif op==4:
            v=np.argsort(values[b])[np.argsort(values[a])[values[b][values[a]]]]
        elif op==5:v=np.argsort(values[a])[values[b][values[a]]]
        else:raise AssertionError(op)
        if i in targets:answer[i]=v.copy()
        values[i]=v
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            refs[j]-=1
            if refs[j]==0:values.pop(j)
        if refs[i]==0:values.pop(i)
    return answer,len(wanted)


def main():
    started=time.time()
    names=['de_a6_gl_epikernels.npz','de_a6_gl_A6_factors.json',
           'de_a6_gl_A5_factors.json','de_a6_schreier_full_ordered.npz',
           'de_ferrari_a5_source_compressed.npz','de_ferrari_a5_source.json',
           'de_ferrari_a5_compare.json','de_ferrari_a6_abelian_compare.json',
           'de_sl2_boundary_quotient.json','de_a6_gl_kernel_replay.json',
           'de_a6_a5_common_source_order.out','de_a6_schreier_full_ordered.out',
           'de_a6_gl_presentation_gate.json']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    ep=np.load(HERE/names[0]);epgens=[ep[k] for k in ('s','r')]
    a6=json_read(names[1]);a5=json_read(names[2])
    shared=sorted(set(a6['factoring_epikernel_indices'])&set(a5['factoring_epikernel_indices']))
    assert shared==[4,12,18]
    assert a6['complete_relator_count']==865049 and a5['complete_relator_count']==23945
    # Replay every recorded nonfactorization word independently on its full
    # base and every induced A5 block.  The complete positive tests remain
    # the all-relator certificates, not this selected-word replay.
    rejection=[]
    for label,raw,base_name in [('A6',a6,names[3]),('A5',a5,names[4])]:
        nodes=raw['literal_word_DAG'];targets={v for v in raw['rejection_word_nodes'] if v>=0}
        base=np.load(HERE/base_name)
        bs,count=evaluate_selected(nodes,targets,[base[k] for k in ('s','r')])
        es,count2=evaluate_selected(nodes,targets,epgens)
        assert count==count2
        for v in bs.values():assert np.array_equal(v,np.arange(len(v)))
        for j,node in enumerate(raw['rejection_word_nodes']):
            if node>=0:assert np.any(es[node][30*j:30*j+30]!=np.arange(30*j,30*j+30))
        rejection.append({'source':label,'literal_rejection_words':len(targets),
                          'nonfactoring_epikernels':sum(v>=0 for v in raw['rejection_word_nodes']),
                          'word_DAG_ancestors_replayed':count})
    d=load_data();H=FerrariA5();Q=sorted(d['Q2']);ix={q:i for i,q in enumerate(Q)}
    paths={d['unit']:[]};todo=deque(paths)
    while todo:
        q=todo.popleft()
        for a,g in ((0,d['s2']),(1,d['r2'])):
            qn=d['mul2'](q,g)
            if qn not in paths:paths[qn]=paths[q]+[a];todo.append(qn)
    def fexponent(w):
        return np.array([sum((a==j)-(a==-j) for a in w) for j in (1,2)],dtype=np.int64)
    def abelian_induced(m):
        ps=[]
        for a,g in ((0,d['s2']),(1,d['r2'])):
            p=np.empty(6*m,dtype=np.int64)
            for q in Q:
                qn=d['mul2'](q,g)
                w=d['fword'](paths[q]+[a]+d['binv'](paths[qn]))
                shift=int(fexponent(w)[0])
                p[m*ix[q]:m*ix[q]+m]=m*ix[qn]+(np.arange(m)+shift)%m
            assert np.array_equal(np.sort(p),np.arange(6*m));ps.append(p)
        return ps
    def word(w,ps):
        bl={0:ps[0],1:ps[1],-1:np.argsort(ps[1])};v=np.arange(len(ps[0]))
        for a in w:v=bl[a][v]
        return v
    def group(ps):return PermutationGroup([Permutation(p.tolist()) for p in ps])
    points=np.arange(4*30,5*30)
    simple=[p[points]-4*30 for p in epgens]
    simple_group=group(simple);simple_F=group([word(d[k],simple) for k in ('xword','yword')])
    assert int(simple_group.order())==6*60**3 and int(simple_F.order())==60**3
    assert int(simple_F.derived_subgroup().order())==60**3
    # The single induced factor4 contains exactly the actual three source
    # epikernels4,12,18.  Test its six root-conjugate pairs against the
    # exhaustive Aut(A5) orbit dictionary.
    pair_to_kernel={}
    for j,(g,h) in enumerate(H.generating_pairs):
        for a in range(120):
            pair_to_kernel[(int(H.sm[H.sm[a,g],H.si[a]]),
                            int(H.sm[H.sm[a,h],H.si[a]]))]=j
    permutation_index={tuple(p):j for j,p in enumerate(H.permutations)}
    sx,sy=[word(d[k],simple) for k in ('xword','yword')]
    coset_kernels=[]
    for i in range(6):
        vals=[]
        for p in (sx,sy):
            arr=p[5*i:5*i+5]-5*i
            assert np.array_equal(np.sort(arr),np.arange(5))
            vals.append(int(H.si[permutation_index[tuple(arr)]]))
        coset_kernels.append(pair_to_kernel[tuple(vals)])
    assert sorted(set(coset_kernels))==shared
    # The distinguished source abelian quotient maps have already been
    # proved: mod120 on G_A6, mod15 on G_A, and mod30 on G_L.
    assert json_read(names[7])['actual_full_A6_abelian_F_quotient_order']==6*120**2
    ac=json_read(names[6]);assert ac['F_image_order']//ac['F_derived_image_order']==15**2
    signed=json_read(names[8]);assert signed['actual_F_abelianization_order']==30**2
    records=[];arrays={'simple_s':simple[0],'simple_r':simple[1],
                      'induced_coset_epikernel_indices':np.array(coset_kernels)}
    g6=int(last(names[11])['order']);ga=json_read(names[5])['induced_B_image_order']
    maximum15=g6*ga//int(last(names[10])['order'])
    maximum30=json_read(names[9])['maximum_common_G6_GL_quotient_order']
    for m,maximum in [(15,maximum15),(30,maximum30)]:
        ab=abelian_induced(m);abG=group(ab)
        assert int(abG.order())==6*m*m
        abx,aby=[word(d[k],ab) for k in ('xword','yword')]
        assert np.array_equal(abx[aby],aby[abx]) and int(group([abx,aby]).order())==m*m
        assert Permutation(abx.tolist()).order()==m and Permutation(aby.tolist()).order()==m
        ps=[np.r_[p,len(p)+q] for p,q in zip(simple,ab)]
        G=group(ps);order=int(G.order());assert order==6*60**3*m*m==maximum
        fx,fy=[word(d[k],ps) for k in ('xword','yword')]
        F=group([fx,fy]);E=F.derived_subgroup();Eorder=int(E.order())
        assert int(F.order())==60**3*m*m and Eorder==60**3
        assert int(E.derived_subgroup().order())==Eorder
        # Each displayed quotient map is the same literal B s/r map.
        # This verifies the commuting projections of the model itself.
        for p,u,v in zip(ps,simple,ab):
            assert np.array_equal(p[:30],u) and np.array_equal(p[30:]-30,v)
        arrays.update({f'm{m}_s':ps[0],f'm{m}_r':ps[1],f'm{m}_x':fx,f'm{m}_y':fy,
                       f'm{m}_Fprime_generators':np.array([p.array_form for p in E.generators])})
        records.append({'modulus':m,'degree':len(ps[0]),'actual_B_image_order':order,
                        'actual_F_image_order':int(F.order()),'actual_Fprime_image_order':Eorder,
                        'actual_Fprime_is_perfect':True,
                        'specified_F_map':'three indexed A5 epikernels and ordinary exponent sums',
                        'F_map_image':'A5^3 times (Z/m)^2',
                        'maximum_common_order_from_independent_complete_source':maximum,
                        'specified_map_is_the_entire_maximum_common_quotient':True})
    # The mod30 -> mod15 projection is retained by explicit point maps
    # on the induced cyclic set, and the identity on the A5 component.
    reduction=np.r_[np.arange(30),30+np.repeat(np.arange(6),30)*15+np.tile(np.arange(30)%15,6)]
    for k in ('s','r'):assert np.array_equal(reduction[arrays['m30_'+k]],arrays['m15_'+k][reduction])
    arrays['m30_to_m15_point_map']=reduction
    out={'status':'PASS_LITERAL_MAXIMUM_COMMON_QUOTIENTS',
         'shared_source_A5_epikernels':shared,'six_induced_coset_epikernels':coset_kernels,
         'complete_positive_factorization_relations':{'G_A6':865049,'G_A':23945},
         'independent_negative_word_replays':rejection,'quotients':records,
         'mod30_to_mod15_literal_point_map_verified':True,
         'scope':'Exact common-source quotients; no simultaneous corrected-fibre assertion.',
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_gl_common_quotient.npz',**arrays)
    (HERE/'de_a6_gl_common_quotient.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
