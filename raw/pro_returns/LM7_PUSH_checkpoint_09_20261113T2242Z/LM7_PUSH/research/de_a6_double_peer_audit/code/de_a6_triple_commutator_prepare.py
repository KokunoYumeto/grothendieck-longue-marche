#!/usr/bin/env python3
"""Actual N-word lifts of the nine ternary source-module generators.

The old binary complement corrections are retained literally. Taking
fourth powers keeps their order-three quotient values and kills their
level-twelve commutator image, placing every lift in the actual N.
All cube/commutator queries lie over the certified perfect C and are
exported for exact normal-form evaluation in its full preimage.
"""
from pathlib import Path
from hashlib import sha256
import json,struct,time
import numpy as np
from de_a6_triple_model import FerrariA6Triple
from de_ferrari_a6_source_data import load_data
from de_ferrari_degree4_lift import InducedCombined
from de_ferrari_a6_solvable import SolvableF,word_interfaces
from de_a6_triple_kernel_replay import selected_group
from de_a6_triple_base_prepare import evaluate
from de_a6_triple_kernel_prepare import pack
from de_ferrari_mod9_lift import rref,solve
from de_a6_schreier_certificate import read_certificate

HERE=Path(__file__).resolve().parent

def main():
    started=time.time()
    names=['de_a6_binary_module.json','de_ferrari_a6_metafibres.npz',
           'de_a6_triple_central_replay.npz','de_a6_triple_kernel_replay.npz',
           'de_a6_gl_central_prepare.npz','de_a6_triple_base_generators.npz',
           'de_a6_triple_modular_generators.npz']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    H=FerrariA6Triple();d=load_data();W=InducedCombined(H,d);F=SolvableF()
    fn,ft,wn,wt=word_interfaces();nodes=[[0,0,0],[1,0,0],[1,1,0]]
    def node(op,a,b=0):
        if op==2 and not a:return b
        if op==2 and not b:return a
        if op==3 and not a:return 0
        nodes.append([int(op),int(a),int(b)]);return len(nodes)-1
    def subst(local,original):
        out=[]
        for op,a,b in local:
            op,a,b=map(int,(op,a,b))
            if op==0:v=0
            elif op==1:v=original[a]
            elif op==3:v=node(op,out[a])
            else:v=node(op,out[a],out[b])
            out.append(v)
        return out
    def power(a,n):
        if n<0:return power(node(3,a),-n)
        out=0
        while n:
            if n&1:out=node(2,out,a)
            a=node(2,a,a);n//=2
        return out
    fm=subst(fn,[1,2]);e=[fm[int(j)] for j in ft]
    wm=subst(wn,e);w=[wm[int(j)] for j in wt]
    assert len(e)==9 and len(w)==6
    corrections=json.loads((HERE/names[0]).read_text())['complement_basis_corrections']
    lifts=[]
    for i,a in enumerate(e):
        for j in range(6):
            if corrections[i]>>j&1:a=node(2,a,w[j])
        lifts.append(power(a,4))
    V=np.load(HERE/names[1])['complete_correction_basis'];assert V.shape==(9,6)
    stable=[]
    for v in V.T:
        a=0
        for g,k in zip(lifts,v):a=node(2,a,power(g,int(k)))
        stable.append(a)
    queries=[];labels=[]
    for i,a in enumerate(lifts):queries.append(power(a,3));labels.append(['module_cube',i])
    for i,a in enumerate(lifts):
        for j in range(i+1,9):queries.append(node(4,a,lifts[j]));labels.append(['module_commutator',i,j])
    for i,a in enumerate(stable):
        for j in range(i+1,6):queries.append(node(4,a,stable[j]));labels.append(['stable_commutator',i,j])
    targets=lifts+stable+queries
    original=[W.word(d['xword']),W.word(d['yword'])]
    actual,count=selected_group(nodes,targets,W,original)
    fp=np.load(HERE/'de_a6_gl_central_prepare.npz')['original_F_source_permutations']
    base=evaluate(nodes,fp,targets)
    old_values,_=selected_group(nodes,targets,F,[F.x,F.y])
    modular=np.load(HERE/names[-1]);qs=modular['modular_s'];qr=modular['modular_r']
    qletters={0:qs,1:qr,-1:qr[qr]}
    def qword(w):
        out=np.arange(576,dtype=np.uint16)
        for a in w:out=qletters[a][out]
        return out
    qvalues=evaluate(nodes,np.array([qword(d['xword']),qword(d['yword'])]),lifts)
    for i,a in enumerate(lifts):
        assert np.array_equal(old_values[a],np.r_[0,0,F.E.complement[i]])
        assert np.array_equal(actual[a][0],W.id)
        assert np.array_equal(qvalues[a],np.arange(576))
        assert np.array_equal(H.project_affine3(actual[a][1])[...,:4],np.broadcast_to([1,0,0,1],(6,6,4)))
    for i,a in enumerate(stable):
        assert np.array_equal(old_values[a],np.r_[0,0,V[:,i],0])
    for a in queries:
        assert np.array_equal(old_values[a],F.one)
        assert np.array_equal(H.project_affine3(actual[a][1]),np.broadcast_to([1,0,0,1,0,0],(6,6,6)))
    old=read_certificate(HERE/'de_a6_schreier_residual_derived.bin')
    assert old['degree']==9462
    kernel=np.load(HERE/names[3])['kernel_basis'];L=np.load(HERE/names[2])['kernel_to_preimage_abelianization']
    piv=np.array(rref(kernel.T)[1]);inv=np.column_stack([solve(kernel[piv],np.eye(79,dtype=np.int64)[:,i])[0] for i in range(79)])
    proj=L@inv%3;hom=np.load(HERE/names[2])['C_lift_abelianization_values']
    assert np.array_equal(proj@kernel[piv]%3,L)
    with (HERE/'de_a6_triple_commutator_queries.bin').open('wb') as f:
        f.write(struct.pack('<5I',0xA63C0033,1,len(queries),9462,3))
        f.write(np.asarray(piv,dtype='<u4').tobytes());f.write(np.asarray(proj,dtype=np.uint8).tobytes())
        f.write(np.asarray(hom,dtype=np.uint8).tobytes())
        for a in queries:
            f.write(pack(actual[a]).astype('<u2').tobytes());f.write(np.asarray(base[a],dtype='<u2').tobytes())
    np.savez_compressed(HERE/'de_a6_triple_commutator_prepare.npz',
        literal_F_word_DAG=np.array(nodes,dtype=np.int64),module_word_nodes=np.array(lifts),
        stable_word_nodes=np.array(stable),query_word_nodes=np.array(queries),
        query_source_values=np.array([actual[a][1] for a in queries]),
        query_A6_permutations=np.array([base[a] for a in queries]),
        module_source_values=np.array([actual[a][1] for a in lifts]),
        module_A6_permutations=np.array([base[a] for a in lifts]),
        stable_module_coordinates=V)
    out={'status':'PASS_LITERAL_N_MODULE_AND_STABLE_COMMUTATOR_QUERIES',
         'query_labels':labels,'query_count':len(queries),
         'module_lifts_have_actual_Q12_identity':True,
         'module_lifts_have_affine_linear_identity':True,
         'query_values_have_entire_affine_identity':True,
         'all_query_old_solvable_values_are_identity':True,
         'literal_F_word_ancestors_replayed':count,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    (HERE/'de_a6_triple_commutator_prepare.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
