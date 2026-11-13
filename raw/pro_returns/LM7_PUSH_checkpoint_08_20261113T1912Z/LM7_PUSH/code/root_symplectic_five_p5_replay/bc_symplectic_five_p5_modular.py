#!/usr/bin/env python3
"""Actual PSL2(F5) conjugation quotient of the five-strand source.

The conjugation homomorphism is computed on the identified normal
SL2(F5), with central signs retained before projectivization.  The
ordinary modular comparison and the Ferrari A5 source comparison use
the literal B generators, never an abstract group-order identification.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_a6_source_data import load_data
from bc_symplectic_five_p5_residual import key,mmkey,pmul,pinv,word

HERE=Path(__file__).resolve().parent
def inverse(a):
    return np.array([[a[1,1],-a[0,1]],[-a[1,0],a[0,0]]],dtype=np.int64)%5
def projective(a):
    a=np.asarray(a)%5
    return min(mmkey(a),mmkey(-a%5))
def main():
    started=time.time()
    names=['bc_symplectic_five_p5_residual.npz','bc_symplectic_five_p5_residual.json',
           'e_symplectic_five_p5_source_root_compressed.npz',
           'de_ferrari_a5_source_compressed.npz','de_ferrari_a5_source_compressed.json']
    hashes={n:sha256((HERE/n).read_bytes()).hexdigest() for n in names}
    data=np.load(HERE/names[0]);src=np.load(HERE/names[2]);s,r=src['s'],src['r']
    L=data['L_elements'];Lt=data['L_theta'];lg=data['L_generators']
    th={key(g):a for g,a in zip(L,Lt)}
    matrices=[np.array(a,dtype=np.int64).reshape(2,2) for a in product(range(5),repeat=4)
              if (a[0]*a[3]-a[1]*a[2])%5==1]
    lifts=[]
    for g in (s,r):
        targets=[th[key(pmul(pmul(pinv(g),a),g))] for a in lg]
        matches=[A for A in matrices if all(np.array_equal(inverse(A)@th[key(a)]@A%5,b)
                                            for a,b in zip(lg,targets))]
        assert len(matches)==2 and np.array_equal(matches[0],-matches[1]%5)
        lifts.append(matches[0])
    hs,hr=lifts
    assert projective(hs@hs)==(1,0,0,1)
    assert projective(np.linalg.matrix_power(hr,3)%5)==(1,0,0,1)
    # All elements of the original source act by the computed inner
    # automorphisms since s,r generate it.  The central signs above are
    # part of the certificate, not discarded during the computation.
    ps=projective(hs);pr=projective(hr)
    vals=[(1,0,0,1)];indices={vals[0]:0};parents=[-1];last=[-1]
    for at,a in enumerate(vals):
        A=np.array(a,dtype=np.int64).reshape(2,2)
        for j,B in enumerate((hs,hr)):
            c=projective(A@B%5)
            if c not in indices:indices[c]=len(vals);vals.append(c);parents.append(at);last.append(j)
    assert len(vals)==60
    pg=np.array([[indices[projective(np.array(a).reshape(2,2)@B%5)] for a in vals]
                 for B in (hs,hr)],dtype=np.int64)
    assert np.array_equal(pg[0][pg[0]],np.arange(60))
    assert np.array_equal(pg[1][pg[1][pg[1]]],np.arange(60))
    # Compare with the ordinary matrices of the project's modular B map.
    ms=np.array([[0,1],[-1,0]],dtype=np.int64)%5
    mr=np.array([[0,-1],[1,-1]],dtype=np.int64)%5
    gl=[np.array(a,dtype=np.int64).reshape(2,2) for a in product(range(5),repeat=4)
        if (a[0]*a[3]-a[1]*a[2])%5]
    comparisons=[A for A in gl if projective(inverse(A)*pow(int(round(np.linalg.det(A)))%5,-1,5)@ms@A%5)==ps
          and projective(inverse(A)*pow(int(round(np.linalg.det(A)))%5,-1,5)@mr@A%5)==pr]
    # inverse() is adjugate for GL2; divide by its determinant here.
    assert comparisons
    P=comparisons[0];Pinv=inverse(P)*pow(int(round(np.linalg.det(P)))%5,-1,5)%5
    assert projective(Pinv@ms@P%5)==ps and projective(Pinv@mr@P%5)==pr
    d=load_data();bl={0:pg[0],1:pg[1],-1:pg[1][pg[1]]}
    x=word(d['xword'],bl);y=word(d['yword'],bl)
    theta_x=np.array(json.loads((HERE/names[1]).read_text())['theta_x'])
    theta_y=np.array(json.loads((HERE/names[1]).read_text())['theta_y'])
    assert vals[int(x[0])]==projective(theta_x) and vals[int(y[0])]==projective(theta_y)
    # The actual joint source decides whether this quotient factors
    # through the retained Ferrari A5 source.
    old=np.load(HERE/'de_ferrari_a5_source_compressed.npz')
    oldorder=int(json.loads((HERE/'de_ferrari_a5_source_compressed.json').read_text())['source_image_order'])
    deg=len(old['s']);joint=PermutationGroup([Permutation(np.r_[old[a],deg+pg[j]].tolist())
                                            for j,a in enumerate(('s','r'))])
    print('Computing literal Ferrari/modular joint source',flush=True)
    jointorder=int(joint.order());assert jointorder%oldorder==0
    ratio=jointorder//oldorder;assert ratio in (1,60)
    out={'status':'PASS_ACTUAL_P5_MODULAR_COMPARISON','normal_L_order':120,
         'conjugation_image_order':60,'conjugation_s_lift':hs.tolist(),'conjugation_r_lift':hr.tolist(),
         's_lift_square':(hs@hs%5).tolist(),'r_lift_cube':(np.linalg.matrix_power(hr,3)%5).tolist(),
         'ordinary_modular_s':ms.tolist(),'ordinary_modular_r':mr.tolist(),
         'modular_change_of_basis':P.tolist(),'Ferrari_A5_source_order':oldorder,
         'Ferrari_A5_modular_joint_order':jointorder,'joint_index':ratio,
         'actual_modular_quotient_factors_through_Ferrari_A5_source':ratio==1,
         'input_sha256':hashes,'seconds':round(time.time()-started,3)}
    target=HERE/'bc_symplectic_five_p5_modular'
    target.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(target.with_suffix('.npz'),s=pg[0],r=pg[1],
                        projective_matrices=np.array(vals,dtype=np.int64).reshape(-1,2,2),
                        s_lift=hs,r_lift=hr,modular_change_of_basis=P,
                        parents=np.array(parents),last=np.array(last))
    assert all(sha256((HERE/n).read_bytes()).hexdigest()==h for n,h in hashes.items())
    print(json.dumps({k:v for k,v in out.items() if k!='input_sha256'},indent=2),flush=True)

if __name__=='__main__':main()
