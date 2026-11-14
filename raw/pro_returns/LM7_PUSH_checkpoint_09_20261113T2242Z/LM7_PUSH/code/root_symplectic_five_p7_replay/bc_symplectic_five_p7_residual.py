#!/usr/bin/env python3
"""Literal prime-seven residual and quotient maps, independently checked.

The elementary abelian kernel is certified from generators and exact
orders, without storing its 16807 permutations.  No uniform-prime
formula is assumed.  All input certificates are read only.
"""
from pathlib import Path
from collections import Counter
from itertools import product
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation
from de_ferrari_a6_source_data import load_data
from de_fermat_schreier import NWORDS
from bc_symplectic_five_p5_residual import (
    key,mmkey,pmul,pinv,ppow,word,comm,group,arrays,compact,enum_generated)
from bc_symplectic_five_p5_common import induced_abelian

HERE=Path(__file__).resolve().parent
P=7

def main():
    started=time.time()
    names=['bc_symplectic_five_p7_source_compressed.npz',
           'bc_symplectic_five_p7_source.json',
           'bc_symplectic_five_p7_model.npz',
           'bc_symplectic_five_p7_subgroups.npz',
           'bc_symplectic_five_p7_subgroups.json',
           'bc_symplectic_five_p7_modular_probe.json',
           'bc_symplectic_five_p5_residual.py',
           'bc_symplectic_five_p5_common.py',
           'de_ferrari_a6_source_data.py','de_fermat_schreier.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    saved=np.load(HERE/names[0]);s,r=saved['s'],saved['r'];degree=len(s)
    one=np.arange(degree,dtype=np.int64);letters={0:s,1:r,-1:r[r]}
    assert np.array_equal(s[s],one) and np.array_equal(r[r[r]],one)
    d=load_data();x=word(d['xword'],letters);y=word(d['yword'],letters)
    sub=np.load(HERE/names[3]);ng=np.stack([word(w,letters) for w in d['Nwords']])
    hw=[d['to_B'](w) for w in NWORDS];hg=np.stack([word(w,letters) for w in hw])
    assert np.array_equal(ng,sub['N_images']) and np.array_equal(hg,sub['H_images'])
    G=group([s,r]);F=group([x,y]);N=group(sub['N_generators'])
    H=group(hg);C=group(sub['F_derived_generators']);L=group(sub['N_derived_generators'])
    orders={name:int(A.order()) for name,A in [('G',G),('F',F),('N',N),('H',H),('C',C),('L',L)]}
    assert orders==dict(G=135531648,F=22588608,N=5647152,H=22588608,C=115248,L=336)
    assert all(H.contains(g) for g in F.generators)
    assert all(F.contains(g) for g in H.generators)
    for A in (F,H):
        Ad=A.derived_subgroup();assert int(Ad.order())==115248
        assert all(C.contains(g) for g in Ad.generators)
    for A in (C,N,L):
        Ad=A.derived_subgroup();assert int(Ad.order())==336
        assert all(L.contains(g) for g in Ad.generators)
    hc=[comm(a,b) for a in hg for b in arrays(C)]
    HC,hcgens=compact(hc);assert int(HC.order())==115248
    assert all(C.contains(g) for g in HC.generators)
    for a in (s,r):
        for A in (C,L,N):
            assert all(A.contains(Permutation(pmul(pmul(pinv(a),b),a).tolist())) for b in arrays(A))
    print('Exact source/subgroup orders',orders,flush=True)

    metadata=json.loads((HERE/names[1]).read_text())
    reps=metadata['retained_original_canonical_orders']
    offsets=np.cumsum([0]+[len(v) for v in reps[:-1]]).tolist()
    Q=sorted(d['Q2']);root=Q.index(d['unit']);target_degree=2400
    base=(8*root+2)*target_degree;records=[];covered=[]
    for rec in metadata['orbit_correspondences']:
        old=np.asarray(rec['original_canonical_order'],dtype=np.int64)
        off=offsets[int(rec['retained_orbit_index'])]
        positions=np.flatnonzero((old>=base)&(old<base+target_degree))
        if len(positions):
            records.append((old[positions]-base,off+positions,old,off))
            covered.extend((old[positions]-base).tolist())
    assert sorted(covered)==list(range(target_degree))
    model=np.load(HERE/names[2]);pts=model['points']
    basis_indices=[int(np.flatnonzero(np.all(pts==v,axis=1))[0]) for v in np.eye(4,dtype=np.int64)]
    def coordinate(g):
        out=np.full(target_degree,-1,dtype=np.int64)
        for positions,inputs,old,off in records:
            js=g[inputs]-off;assert np.all((0<=js)&(js<len(old)))
            out[positions]=old[js]-base
        assert np.all((0<=out)&(out<target_degree))
        return out
    def theta(g):
        p=coordinate(g);A=pts[p[basis_indices]].T%P
        assert np.array_equal(pts@A.T%P,pts[p])
        assert not np.any(A[np.ix_([0,3],[1,2])])
        B=A[np.ix_([1,2],[1,2])].T%P
        assert (int(B[0,0])*int(B[1,1])-int(B[0,1])*int(B[1,0]))%P==1
        return B
    assert np.array_equal(coordinate(x),model['x'][2]) and np.array_equal(coordinate(y),model['y'][2])
    lvals,lindex,lparents,llast=enum_generated(arrays(L),336)
    ltheta={mmkey(theta(g)):g for g in lvals}
    allsl={tuple(a) for a in product(range(P),repeat=4) if (a[0]*a[3]-a[1]*a[2])%P==1}
    assert len(lvals)==len(ltheta)==336 and set(ltheta)==allsl
    for a in lvals:
        for b in arrays(L)+[x,y]:
            assert np.array_equal(theta(pmul(a,b)),theta(a)@theta(b)%P)
    print('Actual third-pentagon isomorphism L -> SL2(F7) verified',flush=True)

    def residual(g):
        l=ltheta[mmkey(theta(g))];q=pmul(g,pinv(l))
        assert np.array_equal(theta(q),np.eye(2,dtype=np.int64))
        assert np.array_equal(pmul(q,l),g)
        return q
    qN=[residual(g) for g in arrays(N)];qC=[residual(g) for g in arrays(C)]
    for q in qN+qC:
        assert np.array_equal(ppow(q,P),one)
        assert all(np.array_equal(pmul(q,l),pmul(l,q)) for l in arrays(L))
    assert all(np.array_equal(pmul(a,b),pmul(b,a)) for a in qN+qC for b in qN+qC)
    V,vbasis=compact(qN);Qker,qbasis=compact(qC)
    assert int(V.order())==P**5 and len(vbasis)==5
    assert int(Qker.order())==P**3 and len(qbasis)==3
    assert all(V.contains(g) for g in Qker.generators)
    # The maps theta|L are injective, whereas theta kills V.  The
    # displayed generator decompositions therefore prove actual direct
    # products N=L x V and C=L x Qker.
    for a in (s,r):
        for A,bs in ((V,vbasis),(Qker,qbasis)):
            for b in bs:
                z=pmul(pmul(pinv(a),b),a)
                assert A.contains(Permutation(z.tolist()))
                assert np.array_equal(theta(z),np.eye(2,dtype=np.int64))
    print('Actual splittings N=L x C7^5 and C=L x C7^3 verified',flush=True)

    # Compare the whole B conjugation action on L with the specified
    # ordinary modular map.  The swap P0 is part of the literal map.
    ms=np.array([[0,1],[-1,0]],dtype=np.int64)%P
    mr=np.array([[0,-1],[1,-1]],dtype=np.int64)%P
    swap=np.array([[0,1],[1,0]],dtype=np.int64)
    def minv(a):return np.array([[a[1,1],-a[0,1]],[-a[1,0],a[0,0]]],dtype=np.int64)%P
    for a,ma in ((s,ms),(r,mr)):
        ta=swap@ma@swap%P
        for l in lvals:
            conj=pmul(pmul(pinv(a),l),a)
            assert np.array_equal(theta(conj),minv(ta)@theta(l)@ta%P)
    tx,ty=theta(x),theta(y)
    assert np.array_equal(tx,np.array([[1,0],[2,1]]))
    assert np.array_equal(ty,np.array([[1,5],[0,1]]))
    print('All672 B-conjugation edges match the ordinary projective level7 map',flush=True)

    a14,t14,p14,l14=induced_abelian(d,14);a2,t2,p2,l2=induced_abelian(d,2)
    assert len(a14)==1176 and len(a2)==24
    a2ix={a:i for i,a in enumerate(a2)}
    amap=np.array([a2ix[(p,tuple(tuple(x%2 for x in row) for row in v))] for p,v in a14],dtype=np.int64)
    assert all(np.array_equal(amap[t14[j]],t2[j,amap]) for j in (0,1))
    joint=group([np.r_[s,degree+t14[0]],np.r_[r,degree+t14[1]]])
    assert int(joint.order())==orders['G']
    assert int(Permutation(x.tolist()).order())==int(Permutation(y.tolist()).order())==14
    assert orders['F']//orders['C']==14**2
    print('Exact source quotient A14 order1176 verified',flush=True)

    # Enumerate the matrix multiplication and every normal closure;
    # these certify the precise perfect quotients used in Goursat.
    sl=sorted(allsl);si={a:i for i,a in enumerate(sl)}
    ident=si[(1,0,0,1)];minus=si[(6,0,0,6)]
    def mulmat(a,b):
        A,B,C,D=a;e,f,g,h=b
        return ((A*e+B*g)%P,(A*f+B*h)%P,(C*e+D*g)%P,(C*f+D*h)%P)
    def invmat(a):A,B,C,D=a;return (D%P,-B%P,-C%P,A%P)
    mult=np.array([[si[mulmat(a,b)] for b in sl] for a in sl],dtype=np.int64)
    inv=np.array([si[invmat(a)] for a in sl],dtype=np.int64)
    normal_orders=[]
    for g in range(336):
        conjugates=set(int(mult[mult[a,g],inv[a]]) for a in range(336))
        seen={ident};queue=[ident]
        for a in queue:
            for b in conjugates:
                c=int(mult[a,b])
                if c not in seen:seen.add(c);queue.append(c)
        normal_orders.append(len(seen))
    assert normal_orders[ident]==1 and normal_orders[minus]==2
    assert all(o==336 for i,o in enumerate(normal_orders) if i not in (ident,minus))
    probe=json.loads((HERE/'bc_symplectic_five_p7_modular_probe.json').read_text())
    assert probe['joint_index']==168
    out={'status':'PASS_EXACT_P7_RESIDUAL_AND_SOURCE_MAPS','prime':P,'orders':orders,
         'C_equals_Fprime_Hprime_gamma3H':True,'Cprime_equals_Nprime_equals_L':True,
         'L_perfect':True,'L_theta_image':'all336 determinant-one matrices overF7',
         'N_direct_product':'SL2(F7) x (C7)^5','C_direct_product':'SL2(F7) x (C7)^3',
         'V_basis_rank':len(vbasis),'Q_basis_rank':len(qbasis),
         'V_and_Q_B_normal':True,'B_conjugation_edges_checked':672,
         'B_action_on_L':'theta(a^-1 l a)=(P q7(a) P)^-1 theta(l)(P q7(a) P), P swaps coordinates',
         'theta_x':tx.tolist(),'theta_y':ty.tolist(),
         'A14_order':1176,'A2_order':24,'joint_source_A14_order':int(joint.order()),
         'A14_kernel_in_B':'Fprime F^14','source_to_A14_kernel':'C',
         'A14_to_A2':'all six abelian Schreier coordinate pairs reduced modulo2',
         'SL2_normal_closure_order_distribution':dict(Counter(normal_orders)),
         'literal_H_generator_B_words':hw,'input_sha256':hashes,
         'seconds':round(time.time()-started,3)}
    target=HERE/'bc_symplectic_five_p7_residual'
    target.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(target.with_suffix('.npz'),
       L_generators=np.stack(arrays(L)),L_elements=np.stack(lvals),
       L_theta=np.stack([theta(g) for g in lvals]),L_enumeration_parents=np.array(lparents),
       L_enumeration_last=np.array(llast),V_generators=np.stack(vbasis),Q_generators=np.stack(qbasis),
       A14_s=t14[0],A14_r=t14[1],A14_parents=np.array(p14),A14_last=np.array(l14),
       A14_to_A2=amap,A2_s=t2[0],A2_r=t2[1],
       gamma3H_generators=np.stack(hcgens),H_images=hg,
       SL2_matrices=np.array(sl,dtype=np.int64),SL2_normal_closure_orders=np.array(normal_orders))
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k not in ('input_sha256','literal_H_generator_B_words')},indent=2),flush=True)

if __name__=='__main__':main()
