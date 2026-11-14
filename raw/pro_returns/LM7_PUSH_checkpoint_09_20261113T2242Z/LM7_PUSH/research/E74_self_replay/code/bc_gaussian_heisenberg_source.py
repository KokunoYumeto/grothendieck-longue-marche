#!/usr/bin/env python3
"""Complete same-N_B correction image with the Gaussian central layer.

The Gaussian factors are class-two exponent-three groups. Lie addition
is realized by the actual word a*b*[a,b], so every row operation has
a retained group-word DAG preimage. This file is new research after E67.
"""
from pathlib import Path
import hashlib
import json
import time
import numpy as np

from bc_orbifold_CM_characters import Affine,R,mv
from bc_gaussian_heisenberg_model import Gaussian,wedge

HERE=Path(__file__).resolve().parent


class DAG:
    def __init__(self):self.nodes=[(0,0,0)];self.cache={(0,0,0):0}
    def make(self,op,a,b=0):
        if op==2:
            if not a:return b
            if not b:return a
        if op==3 and not a:return 0
        if op==4 and (not a or not b):return 0
        key=(op,a,b)
        if key not in self.cache:self.cache[key]=len(self.nodes);self.nodes.append(key)
        return self.cache[key]
    def scalar(self,c,a):return 0 if c%3==0 else a if c%3==1 else self.make(3,a)
    def add(self,a,b):
        return self.make(2,self.make(2,a,b),self.make(4,a,b))


class LieSpan:
    def __init__(self,dag):self.rows={};self.words={};self.dag=dag
    def reduce(self,v):
        v=list(v);coeff={}
        for p,r in sorted(self.rows.items()):
            c=v[p]
            if c:coeff[p]=c;v=[(a-c*b)%3 for a,b in zip(v,r)]
        return v,coeff
    def add(self,v,node):
        v,coeff=self.reduce(v)
        if not any(v):return False
        for p,c in coeff.items():node=self.dag.add(node,self.dag.scalar(-c,self.words[p]))
        p=next(i for i,a in enumerate(v) if a)
        if v[p]==2:v=[2*a%3 for a in v];node=self.dag.scalar(2,node)
        self.rows[p]=tuple(v);self.words[p]=node
        return True
    def preimage(self,v):
        residue,coeff=self.reduce(v)
        if any(residue):return None
        node=0
        for p,c in coeff.items():node=self.dag.add(node,self.dag.scalar(c,self.words[p]))
        return node,coeff


def bracket(v,w):
    out=[0]*30
    for i in range(6):
        j=12+3*i;out[j+2]=wedge(v[j:j+2],w[j:j+2])
    return tuple(out)


def bch(v,w):
    return tuple((a+b+2*c)%3 for a,b,c in zip(v,w,bracket(v,w)))


def main():
    start=time.monotonic();M=Affine(R,6,((0,0),1),((1,0),3),((1,0),2));G=Gaussian()
    pairs=lambda T:[(T.X,T.Y),(T.Y,T.X),(T.Z,T.X),(T.X,T.Z),(T.Y,T.Z),(T.Z,T.Y)]
    maps=[(T,a,b) for T in (M,G) for a,b in pairs(T)]
    def evaluate(w):return tuple(T.word(w,a,b) for T,a,b in maps)
    def mul(a,b):return tuple(T.mul(x,y) for (T,_,_),x,y in zip(maps,a,b))
    def inv(a):return tuple(T.inv(x) for (T,_,_),x in zip(maps,a))
    def comm(a,b):return mul(mul(mul(a,b),inv(a)),inv(b))
    def conj(a,b):return mul(mul(a,b),inv(a))
    one=tuple(T.one for T,_,_ in maps)
    def vector(a):
        assert all(g[1]==0 for g in a[:6]) and all(g[3]==0 for g in a[6:])
        return tuple(c for v,e in a[:6] for c in v)+tuple(c for g in a[6:] for c in g[:3])
    def element(v):
        return tuple((tuple(v[2*i:2*i+2]),0) for i in range(6))+tuple(tuple(v[12+3*i:15+3*i])+(0,) for i in range(6))
    source=json.loads((HERE/'bc_cm_literal_words.json').read_text());nwords=source['N_B_basis_in_F']
    nv=[evaluate(w) for w in nwords]
    assert len(nv)==97
    for a in nv:
        assert all(g[1]%2==0 for g in a[:6]) and all(g[3]%2==0 for g in a[6:])
        assert all(T.power(g,6)==T.one for (T,_,_),g in zip(maps,a))
    dag=DAG();ngen=[dag.make(1,i) for i in range(97)];span=LieSpan(dag)
    commvectors=[]
    for i in range(97):
        for j in range(i):
            v=vector(comm(nv[i],nv[j]));commvectors.append(v)
            span.add(v,dag.make(4,ngen[i],ngen[j]))
    initial=len(span.rows);added_conj=0;added_bracket=0
    changed=True
    while changed:
        changed=False
        rows=list(span.rows.items())
        for p,v in rows:
            for i,n in enumerate(nv):
                cv=vector(conj(n,element(v)))
                if span.add(cv,dag.make(5,ngen[i],span.words[p])):
                    changed=True;added_conj+=1
        rows=list(span.rows.items())
        for i,(p,v) in enumerate(rows):
            for q,w in rows[:i]:
                if span.add(bracket(v,w),dag.make(4,span.words[p],span.words[q])):
                    changed=True;added_bracket+=1
    for v in commvectors:assert not any(span.reduce(v)[0])
    for p,v in span.rows.items():
        for n in nv:assert not any(span.reduce(vector(conj(n,element(v))))[0])
        for w in span.rows.values():assert not any(span.reduce(bracket(v,w))[0])

    # Exact projection to the accepted E67 image, on the identical domain.
    projection=list(range(12))+[12+3*i+j for i in range(6) for j in range(2)]
    e67=json.loads((HERE/'bc_orbifold_CM_six.json').read_text())
    from bc_orbifold_CM_six import Span
    oldspan=Span(24)
    for r in e67['exact_basis']:oldspan.add(r['vector'],())
    projected=Span(24)
    for v in span.rows.values():projected.add([v[j] for j in projection],())
    assert len(projected.rows)==9
    assert all(not any(oldspan.reduce(v)[0]) for v in projected.rows.values())
    assert all(not any(projected.reduce(v)[0]) for v in oldspan.rows.values())

    gtargets=json.loads((HERE/'bc_gaussian_heisenberg_model.json').read_text())['records']
    export=json.loads((HERE/'bc_orbifold_CM_export.json').read_text())
    origins=json.loads((HERE/'de_ferrari_fibres.json').read_text())['records']
    records=[];witnesses=[]
    for i,rec in enumerate(origins):
        word=rec['actual_commutator_word_f'];fval=evaluate(word);fvec=vector(fval)
        assert word==export['families']['E17_E62_actual'][i]['literal_origin_F_word']
        mi=export['families']['E17_E62_actual'][i]['complete_four_finite_norm_values'][0]['Mordell_index']
        mt=export['Mordell_framed_targets'][mi]['six_values']
        allowed=[]
        for gi,gr in enumerate(gtargets):
            gt=[tuple(g) for g in gr['six_absolute_values']]
            target=tuple((tuple(mt[2*j:2*j+2]),0) for j in range(6))+tuple(gt)
            correction=vector(mul(inv(fval),target))
            assert correction==bch(tuple(-x%3 for x in fvec),vector(target))
            solution=span.preimage(correction)
            if solution is None:continue
            node,coeff=solution
            allowed.append({'Gaussian_framed_target_index':gi,'Gaussian_B':gr['B'],
                            'actual_word_DAG_node':node,'correction_vector':correction,
                            'basis_pivot_coefficients':sorted(coeff.items())})
            witnesses.append((node,correction))
        records.append({'E17_index':i,'missing_coset':rec['missing_coset'],
                        'Mordell_framed_target_index':mi,'finite_framed_lift_count':len(allowed),
                        'distinct_Gaussian_homology_actions':len({json.dumps(a['Gaussian_B']) for a in allowed}),
                        'allowed':allowed})

    # Replay every retained row and every successful fibre word in the
    # original twelve groups, including the nonzero deck coordinates of N.
    wanted=set(span.words.values())|{node for node,v in witnesses};ancestors=set(wanted);todo=list(wanted)
    while todo:
        op,a,b=dag.nodes[todo.pop()]
        for n in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            if n not in ancestors:ancestors.add(n);todo.append(n)
    values={}
    for i in sorted(ancestors):
        op,a,b=dag.nodes[i]
        if op==0:value=one
        elif op==1:value=nv[a]
        elif op==2:value=mul(values[a],values[b])
        elif op==3:value=inv(values[a])
        elif op==4:value=comm(values[a],values[b])
        elif op==5:value=conj(values[a],values[b])
        else:raise AssertionError(op)
        values[i]=value
    for p,v in span.rows.items():assert vector(values[span.words[p]])==v
    for node,v in witnesses:assert vector(values[node])==v

    out={'status':'PASS_COMPLETE_GAUSSIAN_CENTRAL_LAYER_SOURCE_AND_FINITE_FIBRES',
         'initial_commutator_rank':initial,'normal_conjugation_additions':added_conj,
         'bracket_additions':added_bracket,'complete_N_derived_Lie_dimension':len(span.rows),
         'complete_N_derived_order':3**len(span.rows),
         'image_equals_K6_image_by_exponent_six':True,
         'old_E67_projection_rank':len(projected.rows),'central_projection_kernel_dimension':len(span.rows)-9,
         'vector_order':'Mordell six translation pairs, then Gaussian six (v1,v2,central) triples',
         'exact_basis':[{'pivot':p,'vector':span.rows[p],'word_DAG_node':span.words[p]} for p in sorted(span.rows)],
         'word_DAG_opcodes':{'0':'identity','1':'original N generator','2':'product','3':'inverse','4':'commutator a b a^-1 b^-1','5':'conjugate a b a^-1'},
         'all_exact_word_ancestors_replayed':len(ancestors),
         'records':records,
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_sha256':{n:hashlib.sha256((HERE/n).read_bytes()).hexdigest() for n in
             ['bc_gaussian_heisenberg_model.py','bc_gaussian_heisenberg_model.json',
              'bc_orbifold_CM_six.json','bc_orbifold_CM_export.json','bc_cm_literal_words.json','de_ferrari_fibres.json']},
         'scope':'Complete central-layer finite source and framed norm fibres over actual E17 origins. '
                 'No joint E66 source, full-GT lift, or omitted relation is assigned.',
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'bc_gaussian_heisenberg_source.npz',
                        word_DAG=np.array(dag.nodes,dtype=np.uint32),
                        exact_basis=np.array([span.rows[p] for p in sorted(span.rows)],dtype=np.uint8),
                        basis_nodes=np.array([span.words[p] for p in sorted(span.rows)],dtype=np.uint32),
                        projection_indices=np.array(projection,dtype=np.uint8))
    (HERE/'bc_gaussian_heisenberg_source.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['status','initial_commutator_rank','normal_conjugation_additions',
                     'bracket_additions','complete_N_derived_Lie_dimension','complete_N_derived_order',
                     'central_projection_kernel_dimension','all_exact_word_ancestors_replayed','seconds']},indent=2))
    print('Finite framed lift counts:',[r['finite_framed_lift_count'] for r in records])
    print('Gaussian action counts:',[r['distinct_Gaussian_homology_actions'] for r in records])


if __name__=='__main__':main()
