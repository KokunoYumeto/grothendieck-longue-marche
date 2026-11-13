#!/usr/bin/env python3
"""Exact signed Q28 and A14 fibre product for the prime-seven source.

Every matrix, Schreier coordinate, and induced source map is retained.
The old GL comparison is recorded only through already proved exact
maps: its Q4 quotient and the independent projective level-seven map.
"""
from pathlib import Path
from collections import Counter
from itertools import product
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_a6_source_data import load_data
from e_hurwitz_five_source_root import Evaluations,Source
from bc_symplectic_five_p5_common import induced_abelian

HERE=Path(__file__).resolve().parent
MOD=28
ONE=(1,0,0,1)
def canonical(a,m=MOD):
    a=tuple(int(x)%m for x in a)
    return min(a,tuple(-x%m for x in a))
def matmul(a,b,m=MOD):
    A,B,C,D=a;e,f,g,h=b
    return canonical((A*e+B*g,A*f+B*h,C*e+D*g,C*f+D*h),m)
def matinv(a,m=MOD):A,B,C,D=a;return canonical((D,-B,-C,A),m)
S=canonical((0,1,-1,0));R=canonical((0,-1,1,-1))

class OneSL2(Evaluations):
    def __init__(self):
        points=np.array([v for v in product(range(7),repeat=2) if any(v)],dtype=np.int64)
        ix={tuple(v):i for i,v in enumerate(points)}
        def perm(A):return np.array([ix[tuple(v@A%7)] for v in points],dtype=np.int64)
        self.x=perm(np.array([[1,2],[0,1]],dtype=np.int64))[None,:]
        self.y=perm(np.array([[1,0],[5,1]],dtype=np.int64))[None,:]
        self.degree=48;self.count=1;self.one=np.arange(48,dtype=np.int64)

def main():
    started=time.time()
    names=['bc_symplectic_five_p7_residual.npz','bc_symplectic_five_p7_residual.json',
           'bc_symplectic_five_p7_modular_probe.npz','bc_symplectic_five_p7_modular_probe.json',
           'bc_symplectic_five_p7_source_compressed.npz',
           'de_ferrari_sl2_5_modular.json','bc_symplectic_five_p5_common.npz',
           'bc_symplectic_five_p5_common.py','de_ferrari_a6_source_data.py','e_hurwitz_five_source_root.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    residual=json.loads((HERE/names[1]).read_text());probe=json.loads((HERE/names[3]).read_text())
    assert residual['orders']['L']==336 and probe['joint_index']==168
    d=load_data();a14,t14,p14,l14=induced_abelian(d,14);a2,t2,p2,l2=induced_abelian(d,2)
    cert=np.load(HERE/names[0]);amap=cert['A14_to_A2']
    assert np.array_equal(t14[0],cert['A14_s']) and np.array_equal(t14[1],cert['A14_r'])
    assert np.array_equal(t2[0],cert['A2_s']) and np.array_equal(t2[1],cert['A2_r'])
    assert Counter(amap)==Counter({i:49 for i in range(24)})

    qvals=[ONE];qindex={ONE:0};qpar=[-1];qlast=[-1]
    for at,a in enumerate(qvals):
        for j,b in enumerate((S,R)):
            z=matmul(a,b)
            if z not in qindex:qindex[z]=len(qvals);qvals.append(z);qpar.append(at);qlast.append(j)
    assert len(qvals)==8064
    assert all((a[0]*a[3]-a[1]*a[2])%28==1 for a in qvals)
    qt=np.array([[qindex[matmul(a,b)] for a in qvals] for b in (S,R)],dtype=np.int64)
    qmap=np.zeros(8064,dtype=np.int64)
    for at in range(1,8064):qmap[at]=t2[qlast[at],qmap[qpar[at]]]
    assert all(np.array_equal(qmap[qt[j]],t2[j,qmap]) for j in (0,1))
    q4map={}
    for a,b in zip(qvals,qmap):
        k=canonical(a,4)
        if k in q4map:assert q4map[k]==int(b)
        else:q4map[k]=int(b)
    assert len(q4map)==len(set(q4map.values()))==24
    assert Counter(qmap)==Counter({i:336 for i in range(24)})
    # The existing GL -> Q12 -> Q4 map has the same literal s,r and
    # the same 24-value dictionary, rather than an abstract isomorphism.
    old=np.load(HERE/'bc_symplectic_five_p5_common.npz')
    assert np.array_equal(t2[0],old['A2_s']) and np.array_equal(t2[1],old['A2_r'])
    assert json.loads((HERE/'de_ferrari_sl2_5_modular.json').read_text())['Q_order']==576

    # The kernel of Q28 -> Q4 is actual SL2(F7), not PSL2(F7).
    qker=np.flatnonzero(qmap==0)
    sl=[]
    for i in qker:
        a=qvals[int(i)]
        if tuple(x%4 for x in a)!=ONE:a=tuple(-x%28 for x in a)
        assert tuple(x%4 for x in a)==ONE
        sl.append(tuple(x%7 for x in a))
    assert len(set(sl))==336
    allsl={tuple(a) for a in product(range(7),repeat=4) if (a[0]*a[3]-a[1]*a[2])%7==1}
    assert set(sl)==allsl
    assert len({canonical(a,7) for a in sl})==168

    W=Source(OneSL2(),d);small=np.stack([W.permutation(W.letters[j]) for j in (0,1)])
    one=np.arange(288,dtype=np.int64);qp=[one]
    for at in range(1,8064):qp.append(small[qlast[at]][qp[qpar[at]]])
    qpa=np.stack(qp);assert len({a.astype(np.uint16).tobytes() for a in qpa})==8064
    for j in (0,1):assert np.array_equal(small[j][qpa],qpa[qt[j]])
    print('All8064 signed Q28 matrices and16128 induced-source edges verified',flush=True)

    pairs=[(0,0)];pi={(0,0):0};parents=[-1];last=[-1]
    for at,(a,b) in enumerate(pairs):
        assert amap[a]==qmap[b]
        for j in (0,1):
            nxt=(int(t14[j,a]),int(qt[j,b]))
            if nxt not in pi:pi[nxt]=len(pairs);pairs.append(nxt);parents.append(at);last.append(j)
    assert len(pairs)==1176*8064//24==395136
    # Containment in the matching-pair set plus this exact size proves
    # equality, without building another copy of its395136 elements.
    jt=np.array([[pi[(int(t14[j,a]),int(qt[j,b]))] for a,b in pairs] for j in (0,1)],dtype=np.int64)
    assert np.array_equal(jt[0,jt[0]],np.arange(395136))
    assert np.array_equal(jt[1,jt[1,jt[1]]],np.arange(395136))
    raw=np.load(HERE/names[4]);degree=len(raw['s'])
    gletters=[np.r_[raw[n],degree+t14[j],degree+1176+small[j]] for j,n in enumerate(('s','r'))]
    G=PermutationGroup([Permutation(a.tolist()) for a in gletters]);jointorder=int(G.order())
    assert jointorder==135531648 and jointorder//len(pairs)==343
    print('Exact A14 x_A2 Q28 image395136 and source kernel343 verified',flush=True)

    out={'status':'PASS_EXACT_P7_SIGNED_QUOTIENT_AND_FIBRE_PRODUCT',
         'A14_order':1176,'A2_order':24,'Q28_order':8064,'J7_order':395136,
         'A14_to_A2':'literal six-coset free exponent sums reduced modulo2',
         'Q28_to_A2':'projective reduction modulo4, with the same24-value GL dictionary',
         'A14_map_fibre_size':49,'Q28_map_fibre_size':336,
         'Q28_kernel_to_A2':'actual SL2(F7), representative normalized to I modulo4',
         'all395136_matching_pairs_generated':True,'all_Q28_induced_edges_checked':16128,
         'joint_original_source_order':jointorder,'kernel_Q7_order':343,
         'Q7_identification':'kernel of theta in C in the residual certificate',
         'GL_projective_level7_joint':'product, by GA product and the elementary2 GL-to-GA kernel',
         'GL_Q28_joint':'GL x_A2 Q28, by the actual Q4 map and perfectness of SL2(F7)',
         'Q28_to_A2_matrix_dictionary':[{'matrix_mod4':list(k),'A2_index':v} for k,v in sorted(q4map.items())],
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    target=HERE/'bc_symplectic_five_p7_common'
    target.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(target.with_suffix('.npz'),A14_to_A2=amap,Q28_to_A2=qmap,
        Q28_elements=np.array(qvals,dtype=np.int64),Q28_parents=np.array(qpar),Q28_last=np.array(qlast),
        Q28_s=qt[0],Q28_r=qt[1],Q28_small_s=small[0],Q28_small_r=small[1],
        Q28_small_elements=qpa,Q28_kernel_indices=qker,Q28_kernel_SL2=np.array(sl,dtype=np.int64),
        J7_elements=np.array(pairs,dtype=np.int64),J7_s=jt[0],J7_r=jt[1],
        J7_parents=np.array(parents),J7_last=np.array(last))
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k not in ('input_sha256','Q28_to_A2_matrix_dictionary')},indent=2),flush=True)

if __name__=='__main__':main()
