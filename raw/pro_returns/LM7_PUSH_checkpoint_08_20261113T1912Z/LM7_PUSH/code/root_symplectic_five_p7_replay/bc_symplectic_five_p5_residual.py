#!/usr/bin/env python3
"""Exact residual and common abelian source for the prime-five B5 test.

Every map is evaluated on the literal B=C2*C3 source.  The normal
SL2(F5) factor is identified through the third pentagon coordinate,
including the right-permutation/transpose convention.  The root's
source and subgroup certificates remain read only.
"""
from pathlib import Path
from collections import deque
from itertools import product
from hashlib import sha256
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_a6_source_data import load_data
from de_fermat_schreier import NWORDS

HERE=Path(__file__).resolve().parent

def key(a):return np.asarray(a,dtype=np.uint16).tobytes()
def mmkey(a):return tuple(int(x) for x in np.asarray(a).ravel())
def pmul(a,b):return b[a]
def pinv(a):return np.argsort(a)
def ppow(a,n):
    if n<0:return ppow(pinv(a),-n)
    ans=np.arange(len(a),dtype=np.int64)
    while n:
        if n&1:ans=pmul(ans,a)
        a=pmul(a,a);n//=2
    return ans
def word(w,letters):
    ans=np.arange(len(letters[0]),dtype=np.int64)
    for a in w:ans=letters[a][ans]
    return ans
def comm(a,b):return pmul(pmul(pmul(a,b),pinv(a)),pinv(b))
def group(gs):return PermutationGroup([Permutation(np.asarray(g).tolist()) for g in gs])
def arrays(G):return [np.array(g.array_form,dtype=np.int64) for g in G.generators]
def compact(gs):
    chosen=[];G=group([np.arange(len(gs[0]),dtype=np.int64)])
    for g in gs:
        if not G.contains(Permutation(g.tolist())):
            chosen.append(g);G=group(chosen)
    assert all(G.contains(Permutation(g.tolist())) for g in gs)
    return G,chosen
def enum_generated(gs,limit):
    one=np.arange(len(gs[0]),dtype=np.int64)
    vals=[one];indices={key(one):0};parents=[-1];last=[-1]
    for at,a in enumerate(vals):
        for j,g in enumerate(gs):
            b=pmul(a,g);kb=key(b)
            if kb not in indices:
                indices[kb]=len(vals);vals.append(b);parents.append(at);last.append(j)
                assert len(vals)<=limit
    return vals,indices,parents,last

def main():
    started=time.time()
    names=['e_symplectic_five_p5_source_root_compressed.npz',
           'e_symplectic_five_p5_source_root_generators.npz',
           'e_symplectic_five_p5_source_root.json',
           'e_symplectic_five_p5_model_root.npz',
           'e_symplectic_five_p5_subgroups_root.npz',
           'e_symplectic_five_p5_subgroups_root.json',
           'de_ferrari_a6_source_data.py','de_fermat_schreier.py']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    saved=np.load(HERE/names[0]);s,r=saved['s'],saved['r'];degree=len(s)
    one=np.arange(degree,dtype=np.int64);letters={0:s,1:r,-1:r[r]}
    assert np.array_equal(s[s],one) and np.array_equal(r[r[r]],one)
    d=load_data();x=word(d['xword'],letters);y=word(d['yword'],letters)
    sub=np.load(HERE/'e_symplectic_five_p5_subgroups_root.npz')
    ng=np.stack([word(w,letters) for w in d['Nwords']])
    hw=[d['to_B'](w) for w in NWORDS]
    hg=np.stack([word(w,letters) for w in hw])
    assert np.array_equal(ng,sub['N_images']) and np.array_equal(hg,sub['H_images'])
    G=group([s,r]);F=group([x,y]);N=group(sub['N_generators'])
    H=group(hg);C=group(sub['F_derived_generators']);L=group(sub['N_derived_generators'])
    orders={name:int(A.order()) for name,A in [('G',G),('F',F),('N',N),('H',H),('C',C),('L',L)]}
    assert orders==dict(G=9000000,F=1500000,N=375000,H=1500000,C=15000,L=120)
    assert all(N.contains(Permutation(a.tolist())) for a in ng)
    assert all(key(a) in {key(b) for b in ng} for a in arrays(N))
    assert all(H.contains(g) for g in F.generators)
    assert all(F.contains(g) for g in H.generators)
    for A in (F,H):
        Ad=A.derived_subgroup();assert int(Ad.order())==15000
        assert all(C.contains(g) for g in Ad.generators)
    Cd=C.derived_subgroup();assert int(Cd.order())==120
    assert all(L.contains(g) for g in Cd.generators)
    Nd=N.derived_subgroup();assert int(Nd.order())==120
    assert all(L.contains(g) for g in Nd.generators)
    Ld=L.derived_subgroup();assert int(Ld.order())==120
    # Exact gamma_3 image: generate all [H generators,C generators],
    # and verify the resulting subgroup is C (which is normal).
    hc=[comm(a,b) for a in hg for b in arrays(C)]
    HC,hcgens=compact(hc);assert int(HC.order())==15000
    assert all(C.contains(g) for g in HC.generators)
    for a in (s,r):
        assert all(C.contains(Permutation(pmul(pmul(pinv(a),b),a).tolist())) for b in arrays(C))
        assert all(L.contains(Permutation(pmul(pmul(pinv(a),b),a).tolist())) for b in arrays(L))
    print('Exact source/subgroup orders',orders,flush=True)

    # Decode the faithful compressed action back to the original third
    # pentagon coordinate at the identity B/F coset.
    metadata=json.loads((HERE/'e_symplectic_five_p5_source_root.json').read_text())
    reps=metadata['retained_original_canonical_orders']
    offsets=np.cumsum([0]+[len(v) for v in reps[:-1]]).tolist()
    Q=sorted(d['Q2']);root=Q.index(d['unit']);base=(8*root+2)*624
    records=[];covered=[]
    for rec in metadata['orbit_correspondences']:
        old=np.asarray(rec['original_canonical_order'],dtype=np.int64)
        ri=int(rec['retained_orbit_index']);off=offsets[ri]
        positions=np.flatnonzero((old>=base)&(old<base+624))
        if len(positions):
            records.append((old[positions]-base,off+positions,old,off))
            covered.extend((old[positions]-base).tolist())
    assert sorted(covered)==list(range(624))
    model=np.load(HERE/'e_symplectic_five_p5_model_root.npz')
    pts=model['points'];basis_indices=[int(np.flatnonzero(np.all(pts==v,axis=1))[0]) for v in np.eye(4,dtype=np.int64)]
    def coordinate(g):
        out=np.full(624,-1,dtype=np.int64)
        for positions,inputs,old,off in records:
            js=g[inputs]-off;assert np.all((0<=js)&(js<len(old)))
            out[positions]=old[js]-base
        assert np.all((0<=out)&(out<624))
        return out
    def theta(g):
        p=coordinate(g)
        A=pts[p[basis_indices]].T%5
        assert np.array_equal(pts@A.T%5,pts[p])
        # The stable plane is span(e_2,e_3).  Transpose converts the
        # right-permutation multiplication into ordinary matrix product.
        assert not np.any(A[np.ix_([0,3],[1,2])])
        B=A[np.ix_([1,2],[1,2])].T%5
        assert int(round(np.linalg.det(B)))%5==1
        return B
    assert np.array_equal(coordinate(x),model['x'][2])
    assert np.array_equal(coordinate(y),model['y'][2])
    thgens=[theta(g) for g in arrays(L)]
    lvals,lindex,lparents,llast=enum_generated(arrays(L),120)
    assert len(lvals)==120
    ltheta={mmkey(theta(g)):g for g in lvals}
    assert len(ltheta)==120
    allsl={tuple(a) for a in product(range(5),repeat=4) if (a[0]*a[3]-a[1]*a[2])%5==1}
    assert set(ltheta)==allsl
    for a in lvals:
        for b in arrays(L)+[x,y]:
            assert np.array_equal(theta(pmul(a,b)),theta(a)@theta(b)%5)
    print('Actual third-pentagon isomorphism L -> SL2(F5)',len(ltheta),flush=True)

    # Split N and C through theta, not through an abstract order match.
    def residual(g):
        l=ltheta[mmkey(theta(g))]
        q=pmul(g,pinv(l));assert np.array_equal(theta(q),np.eye(2,dtype=np.int64))
        assert np.array_equal(pmul(q,l),g)
        return q
    qN=[residual(g) for g in arrays(N)]
    qC=[residual(g) for g in arrays(C)]
    for q in qN+qC:
        assert np.array_equal(ppow(q,5),one)
        assert all(np.array_equal(pmul(q,l),pmul(l,q)) for l in arrays(L))
    assert all(np.array_equal(pmul(a,b),pmul(b,a)) for a in qN+qC for b in qN+qC)
    vvals,vindex,vparents,vlast=enum_generated(qN,3125)
    qvals,qindex,qparents,qlast=enum_generated(qC,125)
    assert len(vvals)==3125 and len(qvals)==125
    assert all(key(q) in vindex for q in qvals)
    assert all(key(q) not in lindex for q in vvals[1:])
    # Choose an F5 basis, retaining coordinates for every element.
    vbasis=[];vtable={key(one):(0,)*5};values=[one];coords=[()]
    for g in qN:
        if key(g) in {key(v) for v in values}:continue
        oldv,oldc=values,coords;vbasis.append(g);values=[];coords=[]
        for j in range(5):
            p=ppow(g,j)
            values.extend(pmul(a,p) for a in oldv)
            coords.extend(c+(j,) for c in oldc)
    assert len(vbasis)==5 and len(values)==3125
    vcoord={key(v):np.array(c,dtype=np.int64) for v,c in zip(values,coords)}
    Bactions=[]
    for a in (s,r):
        columns=[]
        for v in vbasis:
            av=pmul(pmul(pinv(a),v),a)
            # The theta-kernel is not presumed B-stable.  Its projection
            # modulo L is the canonical N/L coordinate.
            columns.append(vcoord[key(residual(av))])
        Bactions.append(np.column_stack(columns))
    assert np.array_equal(Bactions[0]@Bactions[0]%5,np.eye(5,dtype=np.int64))
    assert np.array_equal(np.linalg.matrix_power(Bactions[1],3)%5,np.eye(5,dtype=np.int64))
    qcoords=np.stack([vcoord[key(g)] for g in qC],axis=1)
    print('Actual splittings N=L x C5^5 and C=L x C5^3 verified',flush=True)

    # Construct A_10 directly from six induced abelian Schreier values.
    # Its kernel in B is exactly F'F^10: restriction to the identity
    # coset is the ordinary F-abelianization modulo 10, and every other
    # coset is its actual conjugate.
    ix={q:i for i,q in enumerate(Q)};sect={d['unit']:[]};todo=deque(sect)
    while todo:
        q=todo.popleft()
        for a,g in ((0,d['s2']),(1,d['r2'])):
            qn=d['mul2'](q,g)
            if qn not in sect:sect[qn]=sect[q]+[a];todo.append(qn)
    def fab(w):return tuple(sum(1 if a==j else -1 if a==-j else 0 for a in w)%10 for j in (1,2))
    al=[]
    for a,g in ((0,d['s2']),(1,d['r2'])):
        p=[];v=[]
        for q in Q:
            qn=d['mul2'](q,g);p.append(ix[qn])
            v.append(fab(d['fword'](sect[q]+[a]+d['binv'](sect[qn]))))
        al.append((tuple(p),tuple(v)))
    ai=(tuple(range(6)),((0,0),)*6)
    def amul(a,b):
        p,u=a;q,v=b
        return tuple(q[j] for j in p),tuple(tuple((u[i][k]+v[p[i]][k])%10 for k in (0,1)) for i in range(6))
    av=[ai];aindex={ai:0};apar=[-1];alas=[-1]
    for at,a in enumerate(av):
        for j,b in enumerate(al):
            z=amul(a,b)
            if z not in aindex:aindex[z]=len(av);av.append(z);apar.append(at);alas.append(j)
    assert len(av)==600
    ag=np.array([[aindex[amul(a,b)] for a in av] for b in al],dtype=np.int64)
    assert np.array_equal(ag[0][ag[0]],np.arange(600))
    assert np.array_equal(ag[1][ag[1][ag[1]]],np.arange(600))
    # Verify the literal source quotient through the faithful joint map.
    joint=group([np.r_[s,degree+ag[0]],np.r_[r,degree+ag[1]]])
    assert int(joint.order())==orders['G']
    assert int(Permutation(x.tolist()).order())==int(Permutation(y.tolist()).order())==10
    assert orders['F']//orders['C']==100
    print('Exact common quotient A10 order600; faithful joint order',int(joint.order()),flush=True)

    out={
      'status':'PASS_EXACT_P5_RESIDUAL_AND_A10_SOURCE',
      'orders':orders,'C_equals_Fprime_Hprime_gamma3H':True,
      'Cprime_equals_Nprime_equals_L':True,'L_is_perfect':True,
      'third_pentagon_coordinate_index':2,'identity_coset_index':root,
      'theta_matrix_convention':'transpose of the stable e2,e3 block; ordinary matrix multiplication',
      'theta_L_image':'all 120 determinant-one matrices over F5',
      'N_direct_product':'SL2(F5) x (C5)^5',
      'C_direct_product':'SL2(F5) x (C5)^3',
      'C_abelianization_order':125,
      'C_has_no_nontrivial_solvable_2_3_quotient':True,
      'source_A10_order':600,'joint_source_A10_order':int(joint.order()),
      'A10_kernel_in_B':'Fprime F^10',
      'source_map_to_A10_kernel':'C',
      'literal_H_generator_B_words':hw,
      'N_mod_L_s_r_matrices':[a.tolist() for a in Bactions],
      'C_mod_L_columns':qcoords.tolist(),
      'theta_x':theta(x).tolist(),'theta_y':theta(y).tolist(),
      'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    target=HERE/'bc_symplectic_five_p5_residual'
    target.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(target.with_suffix('.npz'),
       L_generators=np.stack(arrays(L)),L_elements=np.stack(lvals),
       L_theta=np.stack([theta(g) for g in lvals]),
       L_enumeration_parents=np.array(lparents),L_enumeration_last=np.array(llast),
       V_generators=np.stack(vbasis),Q_generators=np.stack(qC),
       N_mod_L_s_r=np.stack(Bactions),Q_coordinates=qcoords,
       A10_s=ag[0],A10_r=ag[1],A10_enumeration_parents=np.array(apar),A10_enumeration_last=np.array(alas),
       gamma3H_generators=np.stack(hcgens),H_images=hg)
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k not in ('input_sha256','literal_H_generator_B_words')},indent=2),flush=True)

if __name__=='__main__':main()
