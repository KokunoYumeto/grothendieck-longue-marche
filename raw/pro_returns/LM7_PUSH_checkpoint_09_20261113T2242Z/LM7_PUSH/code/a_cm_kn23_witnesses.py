#!/usr/bin/env python3
"""Literal full-source witnesses for every complete Kn23 finite fibre.

The DAG is over all 97 fixed N_B generators.  The exact integral lattice
words supply the additional K6-intersect-F-prime generators; every saved
word is checked to have zero integral F exponents and zero N exponents
modulo six.  All word values are replayed on the original 11691 points.
"""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np

from de_a6_schreier_certificate import read_certificate,verify_words
from a_cm_kn23_fibres import PrefixTransversals


HERE=Path(__file__).resolve().parent


class Words:
    def __init__(self):
        self.nodes=[(0,0,0)];self.cache={(0,0,0):0}
    def make(self,op,a,b=0):
        a,b=int(a),int(b)
        if op==2:
            if a==0:return b
            if b==0:return a
        if op in (3,4,5) and a==0:
            return b if op==5 else 0
        if op in (4,5) and b==0:return 0
        if op==4 and a==b:return 0
        key=(op,a,b)
        if key not in self.cache:
            self.cache[key]=len(self.nodes);self.nodes.append(key)
        return self.cache[key]
    def product(self,a,b):return self.make(2,a,b)
    def inverse(self,a):return self.make(3,a)
    def power(self,a,n):
        if n<0:a,n=self.inverse(a),-n
        out=0
        while n:
            if n&1:out=self.product(out,a)
            a=self.product(a,a);n//=2
        return out
    def substitute(self,cert,original_nodes):
        assert len(original_nodes)==len(cert['original'])
        mapping=[]
        for op,a,b in cert['nodes']:
            op,a,b=map(int,(op,a,b))
            if op==0:v=0
            elif op==1:v=original_nodes[a]
            else:v=self.make(op,mapping[a],mapping[b] if op in (2,4,5) else 0)
            mapping.append(v)
        return [mapping[int(w)] for w in cert['words']]


def main():
    started=time.monotonic();meta=json.loads((HERE/'a_cm_kn23_model.json').read_text())
    model=np.load(HERE/'a_cm_kn23_model.npz')
    sourceinfo=json.loads((HERE/'a_cm_kn23_source.json').read_text())
    whole=json.loads((HERE/'a_cm_kn23_full.json').read_text())
    fibreinfo=json.loads((HERE/'a_cm_kn23_fibres.json').read_text())
    fibres=np.load(HERE/'a_cm_kn23_fibres.npz')
    upper=read_certificate(HERE/'a_cm_kn23_N_derived.bin')
    middle=read_certificate(HERE/'a_cm_kn23_projected.bin')
    source=read_certificate(HERE/whole['source_certificate'])
    kernel=read_certificate(HERE/whole['kernel_certificate'])
    for c in (upper,middle,source,kernel):verify_words(c)
    assert upper['derived'] and not middle['derived'] and not source['derived']
    sourcepoints=np.load(HERE/'a_cm_kn23_source.npz')['retained_projection_points']
    fulln=model['common_N'].shape[1];inverse=np.full(fulln,-1,dtype=np.int64)
    inverse[sourcepoints]=np.arange(len(sourcepoints))
    indices=sourceinfo['common_N_source']['selected_original_indices']
    assert np.array_equal(upper['original'],model['common_N'][indices])
    assert np.array_equal(inverse[upper['strong'][:,sourcepoints]],middle['original'])

    W=Words();original_nodes=[W.make(1,i) for i in range(97)]
    upper_nodes=W.substitute(upper,[original_nodes[i] for i in indices])
    middle_nodes=W.substitute(middle,upper_nodes)
    lattice=np.load(HERE/'a_cm_kn23_ab_lattice.npz')
    columns=lattice['unimodular_columns'];extra_nodes=[]
    for j in range(2,97):
        node=0
        for i,k in enumerate(columns[:,j]):
            if k:node=W.product(node,W.power(original_nodes[i],int(k)))
        extra_nodes.append(W.power(node,6))
    source_input_nodes=middle_nodes+extra_nodes
    assert np.array_equal(source['original'],np.r_[middle['strong'],
                         lattice['kernel_basis_sixth_projected_values']])
    source_nodes=W.substitute(source,source_input_nodes)
    kernel_indices=np.load(HERE/'a_cm_kn23_full.npz')['kernel_strong_indices_in_selected_source']
    assert np.array_equal(kernel['original'],source['strong'][kernel_indices,4957:]-4957)
    kernel_nodes=W.substitute(kernel,[source_nodes[int(i)] for i in kernel_indices])

    top=PrefixTransversals(source,whole['old_prefix_base_length'])
    bottom=PrefixTransversals(kernel,len(model['fixed_targets_in_projection']))
    def word_transversals(trans,strongnodes):
        answer=[]
        for level in trans.levels:
            row={}
            for point,path in zip(level['orbit'],level['paths']):
                node=0
                for i in path:node=W.product(node,strongnodes[i])
                row[point]=node
            answer.append(row)
        return answer
    top_words=word_transversals(top,source_nodes)
    bottom_words=word_transversals(bottom,kernel_nodes)
    old_nodes=[]
    for points in fibres['old_sift_points']:
        node=0
        for row,point in zip(top_words,points):node=W.product(row[int(point)],node)
        old_nodes.append(node)
    wanted=[]
    for (old_index,a,b),points in zip(fibres['success_parameters'],fibres['success_kernel_sift_points']):
        node=old_nodes[int(old_index)]
        for row,point in zip(bottom_words,points):
            node=W.product(node,W.inverse(row[int(point)]))
        wanted.append(node)
    assert len(wanted)==fibreinfo['successful_finite_corrections']==18432

    # Every comparison is made against the projected value already used
    # in the full fixed-tuple query, with a replay in the larger source.
    checks={}
    expected=fibres['success_values']
    for i,node in enumerate(wanted):checks.setdefault(node,[]).append(('witness',i))
    for i,node in enumerate(old_nodes):checks.setdefault(node,[]).append(('old',i))
    for i,node in enumerate(extra_nodes):checks.setdefault(node,[]).append(('extra',i))
    for i,node in enumerate(source_nodes):checks.setdefault(node,[]).append(('source',i))
    for i,node in enumerate(kernel_nodes):checks.setdefault(node,[]).append(('kernel',i))
    ancestors=set(checks);todo=list(ancestors)
    while todo:
        op,a,b=W.nodes[todo.pop()]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            if j not in ancestors:ancestors.add(j);todo.append(j)
    refs=np.zeros(len(W.nodes),dtype=np.int64)
    for i in ancestors:
        op,a,b=W.nodes[i]
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):refs[j]+=1
    fullone=np.arange(fulln,dtype=np.uint16)
    def pinv(p):
        ans=np.empty_like(p);ans[p]=fullone;return ans
    values={};evalues={};avalues={};peak=0;checked=0
    exponents=lattice['integral_exponent_matrix']
    original_ab=np.eye(97,dtype=np.int8)
    for step,i in enumerate(sorted(ancestors)):
        op,a,b=W.nodes[i]
        if op==0:p=fullone;e=(0,0);ab=np.zeros(97,dtype=np.int8)
        elif op==1:
            p=model['common_N'][a];e=tuple(map(int,exponents[:,a]));ab=original_ab[a]
        elif op==2:
            p=values[b][values[a]]
            e=tuple(x+y for x,y in zip(evalues[a],evalues[b]));ab=(avalues[a]+avalues[b])%6
        elif op==3:
            p=pinv(values[a]);e=tuple(-x for x in evalues[a]);ab=(-avalues[a])%6
        elif op==4:
            p=pinv(values[b])[pinv(values[a])[values[b][values[a]]]]
            e=(0,0);ab=np.zeros(97,dtype=np.int8)
        elif op==5:
            p=pinv(values[a])[values[b][values[a]]];e=evalues[b];ab=avalues[b]
        else:raise AssertionError(op)
        values[i]=p;evalues[i]=e;avalues[i]=ab
        if i in checks:
            projected=inverse[p[sourcepoints]];assert np.all(projected>=0)
            for typ,j in checks[i]:
                if typ=='witness':
                    assert np.array_equal(projected,expected[j]);checked+=1
                    assert e==(0,0) and not np.any(ab)
                elif typ=='old':
                    assert np.array_equal(projected,fibres['old_preimages'][j])
                    assert e==(0,0) and not np.any(ab)
                elif typ=='extra':
                    assert np.array_equal(p,lattice['kernel_basis_sixth_full_values'][j])
                    assert e==(0,0) and not np.any(ab)
                elif typ=='source':
                    assert np.array_equal(projected,source['strong'][j])
                    assert e==(0,0) and not np.any(ab)
                elif typ=='kernel':
                    assert np.array_equal(projected[:4957],np.arange(4957))
                    assert np.array_equal(projected[4957:]-4957,kernel['strong'][j])
                    assert e==(0,0) and not np.any(ab)
        peak=max(peak,len(values))
        for j in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            refs[j]-=1
            if refs[j]==0:
                values.pop(j);evalues.pop(j);avalues.pop(j)
        if refs[i]==0:
            values.pop(i);evalues.pop(i);avalues.pop(i)
        if step and step%20000==0:print('Replayed actual source nodes',step,'witnesses',checked,flush=True)
    assert checked==len(wanted)
    inputs=['a_cm_kn23_model.json','a_cm_kn23_model.npz','a_cm_kn23_source.json',
            'a_cm_kn23_N_derived.bin','a_cm_kn23_projected.bin',
            'a_cm_kn23_source.npz','a_cm_kn23_ab_lattice.npz','a_cm_kn23_full.json',
            'a_cm_kn23_full.npz',whole['source_certificate'],whole['kernel_certificate'],
            'a_cm_kn23_fibres.json','a_cm_kn23_fibres.npz']
    out={'status':'PASS_ALL_18432_LITERAL_FULL_K6_FPRIME_KN23_WITNESSES',
         'witness_count':len(wanted),'original_N_generator_count':97,
         'full_source_degree':fulln,'retained_source_degree':len(sourcepoints),
         'global_word_DAG_nodes':len(W.nodes),'all_source_ancestors_replayed':len(ancestors),
         'peak_retained_full_source_values':peak,
         'all_witnesses_have_zero_integral_F_exponents':True,
         'all_witnesses_have_zero_N_exponents_mod_six':True,
         'all_95_lattice_sixth_words_replayed_in_full_source':True,
         'all_selected_source_and_kernel_strong_words_replayed':True,
         'all_18432_actual_fixed_tuple_and_old_values_replayed':True,
         'exact_domain':'K6 intersect F-prime',
         'input_sha256':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in inputs},
         'scope':'Actual common-source finite witnesses with their exact K6 and F-prime memberships. No full-GT realization or uncomputed source-generation assertion.',
         'seconds':round(time.monotonic()-started,6)}
    np.savez_compressed(HERE/'a_cm_kn23_witnesses.npz',
                        word_DAG=np.array(W.nodes,dtype=np.uint32),
                        witness_nodes=np.array(wanted,dtype=np.uint32),
                        witness_parameters=fibres['success_parameters'],
                        old_parameters=fibres['old_parameters'],
                        old_preimage_nodes=np.array(old_nodes,dtype=np.uint32),
                        extra_lattice_sixth_nodes=np.array(extra_nodes,dtype=np.uint32),
                        source_strong_nodes=np.array(source_nodes,dtype=np.uint32),
                        kernel_strong_nodes=np.array(kernel_nodes,dtype=np.uint32),
                        full_original_N_values=model['common_N'])
    (HERE/'a_cm_kn23_witnesses.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
