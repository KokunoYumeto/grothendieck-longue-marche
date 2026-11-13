#!/usr/bin/env python3
"""Independent literal replay of the full-rank central relation certificate."""
from pathlib import Path
from hashlib import sha256
import json,time
import numpy as np
from de_a6_gl_common_quotient import evaluate_selected
from de_ferrari_sl2_5_model import FerrariSL2Five,matmul,matinv

HERE=Path(__file__).resolve().parent


def main():
    started=time.time();names=['de_a6_gl_central.json','de_a6_gl_central_prepare.npz',
        'de_a6_gl_central_prepare.json','de_a6_gl_central.cpp','de_a6_schreier_residual_derived.bin']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    raw=json.loads((HERE/names[0]).read_text());data=np.load(HERE/names[1]);H=FerrariSL2Five()
    assert raw['complete_Schreier_relations']==720615 and raw['complete_original_to_normal_form_relations']==10
    assert raw['all_complete_relations_evaluated'] and raw['all_relator_images_central']
    nodes=raw['literal_word_DAG'];targets=raw['relation_basis_word_nodes'];rows=raw['relation_basis_rows']
    assert len(targets)==len(rows)==13
    values,count=evaluate_selected(nodes,set(targets),data['C_original_source_permutations'])
    assert all(np.array_equal(v,np.arange(len(v))) for v in values.values())
    # Use actual 2x2 matrix multiplication independently of the C++
    # 120-by120 lookup table used for the complete presentation run.
    one=((1,0,0,1),)*3;minus=(4,0,0,4)
    original=[tuple(H.sl[int(j)] for j in row) for row in data['C_original_SL2_values']]
    def mul(a,b):return tuple(matmul(x,y) for x,y in zip(a,b))
    def inv(a):return tuple(matinv(x) for x in a)
    needed=set(targets);todo=list(targets)
    while todo:
        j=todo.pop();op,a,b=nodes[j]
        for k in ([a,b] if op in (2,4,5) else [a] if op==3 else []):
            if k not in needed:needed.add(k);todo.append(k)
    sv={};ab={}
    for j in sorted(needed):
        op,a,b=nodes[j]
        if op==0:v=one;e=0
        elif op==1:v=original[a];e=1<<a
        elif op==2:v=mul(sv[a],sv[b]);e=ab[a]^ab[b]
        elif op==3:v=inv(sv[a]);e=ab[a]
        elif op==4:v=mul(mul(mul(sv[a],sv[b]),inv(sv[a])),inv(sv[b]));e=0
        elif op==5:v=mul(mul(sv[a],sv[b]),inv(sv[a]));e=ab[b]
        else:raise AssertionError(op)
        sv[j]=v;ab[j]=e
    for node,row in zip(targets,rows):
        center=0
        for j,v in enumerate(sv[node]):
            assert v in ((1,0,0,1),minus)
            if v==minus:center|=1<<j
        assert row==ab[node]|(center<<10)
    A=np.array([[(row>>j)&1 for j in range(13)] for row in rows],dtype=np.int64)
    aug=np.c_[A,np.eye(13,dtype=np.int64)]
    for j in range(13):
        k=next(k for k in range(j,13) if aug[k,j]);aug[[j,k]]=aug[[k,j]]
        for k in range(13):
            if k!=j and aug[k,j]:aug[k]^=aug[j]
    assert np.array_equal(aug[:,:13],np.eye(13,dtype=np.int64))
    inverse=aug[:,13:];assert np.array_equal(inverse@A%2,np.eye(13,dtype=np.int64))
    assert np.array_equal(A[:10,:10],np.eye(10,dtype=np.int64))
    assert not np.any(A[10:,:10])
    # A central extension of a perfect group has abelianization generated
    # by its center.  Here the full center has exponent2.  The complete
    # mod2 relation matrix therefore proves integral perfection.
    out={'status':'PASS_INDEPENDENT_CENTRAL_PERFECTION',
         'all13_basis_words_identity_in_full_A6_source':True,
         'all13_lift_values_verified_by_direct_2x2_matrix_multiplication':True,
         'all10_original_generator_sign_freedoms_retained':True,
         'relation_rank':13,'source_generator_exponent_rank':10,
         'independent_central_relation_rank':3,
         'actual_pullback_is_perfect':True,
         'actual_pullback':'C_A6 fibre product over the three specified A5 factors with SL2(F5)^3',
         'source_word_ancestors_replayed':count,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    np.savez_compressed(HERE/'de_a6_gl_central_replay.npz',relation_matrix=A,
                        relation_matrix_inverse=inverse,central_relation_matrix=A[10:,10:])
    (HERE/'de_a6_gl_central_replay.json').write_text(json.dumps(out,indent=2)+'\n')
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps(out,indent=2),flush=True)


if __name__=='__main__':main()
