#!/usr/bin/env python3
"""Literal 72-element quotient of the full source by the entire N image.

The quotient action comes from exact normal cosets.  This program gives
the actual map from the specified 576-element modular group, computes
the pure image, and identifies it with the ordinary exponent lattice.
"""
from pathlib import Path
from collections import deque
import json,time
import numpy as np
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent

def main():
    start=time.time();d=load_data()
    raw=json.loads((HERE/'de_a6_source_mod_N.json').read_text())
    assert raw['status']=='PASS' and raw['quotient_order']==72
    s,r=map(lambda p:np.array(p,dtype=np.int64),raw['generators'])
    one=np.arange(len(s));letters={0:s,1:r,-1:r[r]}
    def word(w):
        p=one.copy()
        for a in w:p=letters[a][p]
        return p
    assert np.array_equal(s[s],one) and np.array_equal(r[r[r]],one)
    assert all(np.array_equal(word(w),one) for w in d['Nwords'])
    Q=d['Q'];Qindex={q:i for i,q in enumerate(Q)}
    qimages=np.array([word(d['Bpaths'][q]) for q in Q])
    # Every modular Cayley edge is an actual equality under the literal
    # word map.  This proves factorization through this specified Q.
    for i,q in enumerate(Q):
        for letter,g in ((0,d['ss']),(1,d['rr'])):
            assert np.array_equal(letters[letter][qimages[i]],qimages[Qindex[d['times'](q,g)]])
    image={tuple(p) for p in qimages};kernel=[i for i,p in enumerate(qimages) if np.array_equal(p,one)]
    assert len(image)==72 and len(kernel)==8
    x,y=word(d['xword']),word(d['yword'])
    assert np.array_equal(x[y],y[x])
    found={tuple(one)};queue=deque([one])
    while queue:
        p=queue.popleft()
        for g in (x,y):
            v=g[p];key=tuple(v)
            if key not in found:found.add(key);queue.append(v)
    assert len(found)==12
    fab=np.array([[sum(1 if a==j else -1 if a==-j else 0 for a in d['fword'](w))
                   for w in d['Nwords']] for j in (1,2)],dtype=np.int64)
    smith=smith_normal_form(Matrix(fab.tolist()),domain=ZZ)
    diagonal=[abs(int(smith[i,i])) for i in range(2)];assert diagonal==[2,6]
    # N lies in the exponent lattice L, and both the displayed abelian
    # quotient of F and Z^2/L have order12.  This identifies the map
    # by the actual images of x and y, including its entire kernel.
    G=int(json.loads((HERE/'de_a6_schreier_full_ordered.out').read_text().splitlines()[-1])['order'])
    P=int(raw['subgroup_order']);assert G==72*P
    out={'status':'PASS','source_mod_N_order':72,'pure_quotient_order':12,
         'modular_source_order':len(Q),'modular_kernel_order':len(kernel),
         'all_modular_generator_edges_checked':2*len(Q),
         'all_97_N_basis_words_killed':True,'pure_generators_commute':True,
         'N_exponent_lattice_Smith_diagonal':diagonal,
         'quotient_identification':'B/(F-prime N), by the actual images of s,r,x,y',
         'source_F_prime_lies_in_source_N':True,'seconds':round(time.time()-start,3)}
    np.savez_compressed(HERE/'de_ferrari_a6_N_quotient.npz',s=s,r=r,x=x,y=y,
                        modular_element_images=qimages,modular_kernel_indices=np.array(kernel),N_F_abelianization=fab)
    (HERE/'de_ferrari_a6_N_quotient.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
