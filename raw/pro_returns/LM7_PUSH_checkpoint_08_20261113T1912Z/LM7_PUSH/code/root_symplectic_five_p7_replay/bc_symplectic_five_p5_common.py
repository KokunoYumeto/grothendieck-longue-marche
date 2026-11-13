#!/usr/bin/env python3
"""The exact 72000-element common source, with both maps to A2.

A10 and A2 are constructed from the actual six-coset abelian Schreier
maps.  Q20 is the signed modular quotient.  Its 144-point induced
SL2(F5) action is compared on every element and every generator edge.
The complete fibre product is enumerated, and its joint map with the
original five-strand source is certified without modifying any input.
"""
from pathlib import Path
from collections import deque,Counter
from itertools import product
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_a6_source_data import load_data
from e_hurwitz_five_source_root import Evaluations,Source
from bc_symplectic_five_p5_signed import matmul,matinv,canonical,value,ONE

HERE=Path(__file__).resolve().parent
def induced_abelian(d,m):
    Q=sorted(d['Q2']);ix={q:i for i,q in enumerate(Q)}
    sect={d['unit']:[]};todo=deque(sect)
    while todo:
        q=todo.popleft()
        for a,g in ((0,d['s2']),(1,d['r2'])):
            qn=d['mul2'](q,g)
            if qn not in sect:sect[qn]=sect[q]+[a];todo.append(qn)
    def fab(w):return tuple(sum(1 if a==j else -1 if a==-j else 0 for a in w)%m for j in (1,2))
    letters=[]
    for a,g in ((0,d['s2']),(1,d['r2'])):
        p=[];v=[]
        for q in Q:
            qn=d['mul2'](q,g);p.append(ix[qn])
            v.append(fab(d['fword'](sect[q]+[a]+d['binv'](sect[qn]))))
        letters.append((tuple(p),tuple(v)))
    identity=(tuple(range(6)),((0,0),)*6)
    def mul(a,b):
        p,u=a;q,v=b
        return tuple(q[j] for j in p),tuple(tuple((u[i][k]+v[p[i]][k])%m for k in (0,1)) for i in range(6))
    vals=[identity];ixv={identity:0};par=[-1];last=[-1]
    for at,a in enumerate(vals):
        for j,b in enumerate(letters):
            z=mul(a,b)
            if z not in ixv:ixv[z]=len(vals);vals.append(z);par.append(at);last.append(j)
    table=np.array([[ixv[mul(a,b)] for a in vals] for b in letters],dtype=np.int64)
    return vals,table,par,last

class OneSL2(Evaluations):
    def __init__(self):
        points=np.array([v for v in product(range(5),repeat=2) if any(v)],dtype=np.int64)
        ix={tuple(v):i for i,v in enumerate(points)}
        def perm(A):return np.array([ix[tuple(v@A%5)] for v in points],dtype=np.int64)
        self.x=perm(np.array([[1,2],[0,1]],dtype=np.int64))[None,:]
        self.y=perm(np.array([[1,0],[3,1]],dtype=np.int64))[None,:]
        self.degree=24;self.count=1;self.one=np.arange(24,dtype=np.int64)

def main():
    started=time.time()
    names=['bc_symplectic_five_p5_residual.npz','bc_symplectic_five_p5_residual.json',
           'bc_symplectic_five_p5_modular.json','bc_symplectic_five_p5_signed.npz',
           'bc_symplectic_five_p5_signed.json','e_symplectic_five_p5_source_root_compressed.npz',
           'de_ferrari_a6_source_data.py','e_hurwitz_five_source_root.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    assert json.loads((HERE/names[4]).read_text())['Q20_factors_through_G_L']
    d=load_data();a10,t10,p10,l10=induced_abelian(d,10);a2,t2,p2,l2=induced_abelian(d,2)
    assert len(a10)==600 and len(a2)==24
    old=np.load(HERE/names[0]);assert np.array_equal(t10[0],old['A10_s']) and np.array_equal(t10[1],old['A10_r'])
    amap=np.zeros(600,dtype=np.int64)
    for at in range(1,600):amap[at]=t2[l10[at],amap[p10[at]]]
    assert all(np.array_equal(amap[t10[j]],t2[j,amap]) for j in (0,1))
    # The reduction map of the actual six-coset coordinates is also
    # checked directly, independently of the representative words.
    ai2={v:i for i,v in enumerate(a2)}
    assert all(amap[i]==ai2[(p,tuple(tuple(x%2 for x in row) for row in v))]
               for i,(p,v) in enumerate(a10))
    signed=np.load(HERE/names[3]);qvals=[tuple(int(x) for x in row) for row in signed['Q20_elements']]
    qindex={a:i for i,a in enumerate(qvals)};qpar=signed['Q20_parents'];qlast=signed['Q20_last']
    qgens=[value([0]),value([1])]
    qt=np.array([[qindex[matmul(a,b)] for a in qvals] for b in qgens],dtype=np.int64)
    qmap=np.zeros(2880,dtype=np.int64)
    for at in range(1,2880):qmap[at]=t2[qlast[at],qmap[qpar[at]]]
    assert all(np.array_equal(qmap[qt[j]],t2[j,qmap]) for j in (0,1))
    # q4 and A2 are compared through every actual Q20 matrix.
    def q4(a):return min(tuple(x%4 for x in a),tuple(-x%4 for x in a))
    q4map={}
    for a,b in zip(qvals,qmap):
        k=q4(a)
        if k in q4map:assert q4map[k]==int(b)
        else:q4map[k]=int(b)
    assert len(q4map)==len(set(q4map.values()))==24
    assert Counter(amap)==Counter({i:25 for i in range(24)})
    assert Counter(qmap)==Counter({i:120 for i in range(24)})

    # Faithful small Q20 representation through the actual signed F map.
    W=Source(OneSL2(),d);small=np.stack([W.permutation(W.letters[j]) for j in (0,1)])
    one=np.arange(144,dtype=np.int64);qp=[one]
    for at in range(1,2880):qp.append(small[qlast[at]][qp[qpar[at]]])
    qpa=np.stack(qp);assert len({a.astype(np.uint8).tobytes() for a in qpa})==2880
    for j in (0,1):assert np.array_equal(small[j][qpa],qpa[qt[j]])

    # Enumerate the complete literal fibre product, retaining all words.
    pairs=[(0,0)];pi={(0,0):0};parents=[-1];last=[-1]
    for at,(a,b) in enumerate(pairs):
        assert amap[a]==qmap[b]
        for j in (0,1):
            nxt=(int(t10[j,a]),int(qt[j,b]))
            if nxt not in pi:pi[nxt]=len(pairs);pairs.append(nxt);parents.append(at);last.append(j)
    assert len(pairs)==600*2880//24==72000
    assert set(pairs)=={(a,b) for a in range(600) for b in np.flatnonzero(qmap==amap[a])}
    jt=np.array([[pi[(int(t10[j,a]),int(qt[j,b]))] for a,b in pairs] for j in (0,1)],dtype=np.int64)
    assert np.array_equal(jt[0,jt[0]],np.arange(72000))
    assert np.array_equal(jt[1,jt[1,jt[1]]],np.arange(72000))
    # The specified J map really factors through the original source.
    raw=np.load(HERE/names[5]);degree=len(raw['s'])
    gletters=[np.r_[raw[n],degree+t10[j],degree+600+small[j]] for j,n in enumerate(('s','r'))]
    G=PermutationGroup([Permutation(a.tolist()) for a in gletters]);jointorder=int(G.order())
    assert jointorder==9000000 and jointorder//len(pairs)==125
    print('Actual J fibre product72000 and joint original source9000000 verified',flush=True)

    # Every noncentral element of SL2(F5) normally generates it.  This
    # exact finite proof supplies the normal-5 exclusion used in Goursat.
    sl=[tuple(a) for a in product(range(5),repeat=4) if (a[0]*a[3]-a[1]*a[2])%5==1]
    si={a:i for i,a in enumerate(sl)};ident=si[(1,0,0,1)];minus=si[(4,0,0,4)]
    def mul5(a,b):
        A,B,C,D=a;e,f,g,h=b
        return ((A*e+B*g)%5,(A*f+B*h)%5,(C*e+D*g)%5,(C*f+D*h)%5)
    def inv5(a):A,B,C,D=a;return (D%5,-B%5,-C%5,A%5)
    mult=np.array([[si[mul5(a,b)] for b in sl] for a in sl],dtype=np.int64)
    inv=np.array([si[inv5(a)] for a in sl],dtype=np.int64)
    normal_orders=[]
    for g in range(120):
        conjugates=set(int(mult[mult[a,g],inv[a]]) for a in range(120))
        seen={ident};queue=[ident]
        for a in queue:
            for b in conjugates:
                c=int(mult[a,b])
                if c not in seen:seen.add(c);queue.append(c)
        normal_orders.append(len(seen))
    assert normal_orders[ident]==1 and normal_orders[minus]==2
    assert all(o==120 for i,o in enumerate(normal_orders) if i not in (ident,minus))
    out={'status':'PASS_EXACT_P5_COMMON_FIBRE_PRODUCT',
         'A10_order':600,'A2_order':24,'Q20_order':2880,'J_order':72000,
         'A10_to_A2':'literal six-coset free exponent sums reduced modulo2',
         'Q20_to_A2':'projective reduction modulo4, with all24 values identified on s,r',
         'A10_map_fibre_size':25,'Q20_map_fibre_size':120,
         'all72000_matching_pairs_generated':True,'all_Q20_small_action_edges_checked':5760,
         'joint_original_source_order':jointorder,'kernel_Q_order':125,
         'Q_is_actual_O5_C':'kernel of the signed-F theta map inside C, as in residual certificate',
         'SL2_normal_closure_order_distribution':dict(Counter(normal_orders)),
         'Q20_to_A2_matrix_dictionary':[{'matrix_mod4':list(k),'A2_index':v} for k,v in sorted(q4map.items())],
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    target=HERE/'bc_symplectic_five_p5_common'
    target.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(target.with_suffix('.npz'),A10_to_A2=amap,Q20_to_A2=qmap,
        A2_s=t2[0],A2_r=t2[1],Q20_small_s=small[0],Q20_small_r=small[1],Q20_small_elements=qpa,
        J_elements=np.array(pairs,dtype=np.int64),J_s=jt[0],J_r=jt[1],
        J_parents=np.array(parents),J_last=np.array(last),SL2_normal_closure_orders=np.array(normal_orders))
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k not in ('input_sha256','Q20_to_A2_matrix_dictionary')},indent=2),flush=True)

if __name__=='__main__':main()
