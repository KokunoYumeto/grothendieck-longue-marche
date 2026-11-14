#!/usr/bin/env python3
"""Actual E69 central words in the complete E71 matrix source.

The existing central words and all E71 inputs are read only.  Prime-to-three
powers, when present, are retained as literal common-kernel words; their
Gaussian values are independently evaluated in the twelve original groups.
"""
from pathlib import Path
from hashlib import sha256
from math import gcd,lcm
import json
import time
import numpy as np

from bc_gaussian_heisenberg_structure import Evaluations

HERE=Path(__file__).resolve().parent


def permutation_order(p):
    seen=np.zeros(len(p),dtype=bool);answer=1
    for i in range(len(p)):
        if seen[i]:continue
        j=i;length=0
        while not seen[j]:seen[j]=True;length+=1;j=int(p[j])
        assert j==i;answer=lcm(answer,length)
    return answer


def main():
    start=time.monotonic();model=np.load(HERE/'a_cm_kn23_model.npz')
    metadata=json.loads((HERE/'a_cm_kn23_model.json').read_text())
    sourcepoints=np.load(HERE/'a_cm_kn23_source.npz')['retained_projection_points']
    new=np.load(HERE/'bc_gaussian_heisenberg_joint.npz')
    newmeta=json.loads((HERE/'bc_gaussian_heisenberg_joint.json').read_text())
    indices=list(map(int,new['original_N_indices']))
    nwords=metadata['source_basis_words_in_F']
    assert [nwords[i] for i in indices]==newmeta['original_N_words_in_F']
    nodes=[tuple(map(int,row)) for row in new['word_DAG']]
    targets=list(map(int,new['central_nodes']));ancestors=set(targets);todo=list(targets)
    while todo:
        op,a,b=nodes[todo.pop()]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            if j not in ancestors:ancestors.add(j);todo.append(j)
    refs={i:0 for i in ancestors}
    for i in ancestors:
        op,a,b=nodes[i]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):refs[j]+=1
    E=Evaluations();Eoriginal=[E.word(nwords[i]) for i in indices]
    original=model['common_N'][indices];one=np.arange(original.shape[1],dtype=np.uint16)
    inverse=np.full(len(one),-1,dtype=np.int64);inverse[sourcepoints]=np.arange(len(sourcepoints))
    def pinv(p):
        q=np.empty_like(p);q[p]=one;return q
    values={};group={};depth={};saved={}
    for i in sorted(ancestors):
        op,a,b=nodes[i]
        if op==0:p=one;v=E.one;d=99
        elif op==1:p=original[a];v=Eoriginal[a];d=0
        elif op==2:p=values[b][values[a]];v=E.mul(group[a],group[b]);d=min(depth[a],depth[b])
        elif op==3:p=pinv(values[a]);v=E.inv(group[a]);d=depth[a]
        elif op==4:
            p=pinv(values[b])[pinv(values[a])[values[b][values[a]]]]
            v=E.comm(group[a],group[b]);d=min(depth[a],depth[b])+1
        elif op==5:p=pinv(values[a])[values[b][values[a]]];v=E.conj(group[a],group[b]);d=depth[b]
        else:raise AssertionError(op)
        values[i]=p;group[i]=v;depth[i]=d
        if i in targets:saved[i]=(p.copy(),v,d)
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            refs[j]-=1
            if refs[j]==0:values.pop(j);group.pop(j);depth.pop(j)
        if refs[i]==0:values.pop(i);group.pop(i);depth.pop(i)
    rows=[];newnodes=[];values_out=[];expected=[]
    def multiply(a,b):
        if not a:return b
        if not b:return a
        nodes.append((2,a,b));return len(nodes)-1
    def wordpower(node,k):
        answer=0
        while k:
            if k&1:answer=multiply(answer,node)
            node=multiply(node,node);k//=2
        return answer
    for j,node in enumerate(targets):
        p,v,d=saved[node]
        assert d>=2 and np.array_equal(E.vector(v),new['central_vectors'][j])
        projected=inverse[p[sourcepoints]];assert np.all(projected>=0)
        order=permutation_order(p);smallorder=permutation_order(projected)
        row={'basis_index':j,'actual_word_node':node,'derived_depth_at_least':d,
             'full_E71_source_order':order,'retained_E71_source_order':smallorder,
             'prime_to_three':gcd(order,3)==1}
        if gcd(order,3)==1:
            exponent=order*pow(order,-1,3)
            q=one.copy();b=p.copy();k=exponent
            while k:
                if k&1:q=b[q]
                b=b[b];k//=2
            assert np.array_equal(q,one) and exponent%3==1
            gv=E.one
            for _ in range(exponent%3):gv=E.mul(gv,v)
            assert gv==v
            newnode=wordpower(node,exponent);newnodes.append(newnode)
            row.update({'power_exponent':exponent,'new_actual_word_node':newnode,
                        'kills_all_11691_E71_points':True,
                        'retains_exact_Gaussian_central_basis_value':True})
            values_out.append(q);expected.append(E.vector(gv))
        rows.append(row)
    out={'status':'PASS_LITERAL_E69_CENTRAL_WORDS_IN_E71_SOURCE',
         'all_basis_words_in_actual_N_second_derived':True,
         'source_words_replayed':len(ancestors),'records':rows,
         'independent_common_kernel_central_words':len(newnodes),
         'full_E71_E69_central_kernel_obtained':len(newnodes)==3,
         'input_sha256':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in
                         ['a_cm_kn23_model.json','a_cm_kn23_model.npz','a_cm_kn23_source.npz',
                          'bc_gaussian_heisenberg_joint.json','bc_gaussian_heisenberg_joint.npz',
                          'bc_gaussian_heisenberg_structure.py']},
         'scope':'Actual common-kernel words for the displayed matrix and Gaussian maps. No full-GT claim.',
         'seconds':round(time.monotonic()-start,6)}
    np.savez_compressed(HERE/'a_cm_matrix_gaussian_join.npz',word_DAG=np.array(nodes,dtype=np.uint32),
                        new_central_word_nodes=np.array(newnodes,dtype=np.uint32),
                        original_N_indices=indices,actual_common_kernel_values=np.array(values_out),
                        exact_Gaussian_central_values=np.array(expected,dtype=np.uint8))
    (HERE/'a_cm_matrix_gaussian_join.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
