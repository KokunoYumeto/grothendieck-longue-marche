#!/usr/bin/env python3
"""Exact N, K6 and K6-intersect-F-prime images in the A5 induced source."""
from pathlib import Path
from contextlib import redirect_stdout
import io,json,runpy,time
import numpy as np
from sympy.combinatorics import PermutationGroup,Permutation
from sympy import factorint

def main():
    start=time.time();here=Path(__file__).resolve().parent
    with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
    data=np.load(here/'de_ferrari_a5_source_compressed.npz')
    s,r=data['s'],data['r'];identity=Permutation(list(range(len(s))))
    letters={0:s,1:r,-1:r[r]}
    def word(w):
        out=np.arange(len(s))
        for t in w:out=letters[t][out]
        return Permutation(out.tolist())
    N=[word(w) for w in d['Nwords']]
    indices=sorted(range(97),key=lambda i:int(N[i].order()),reverse=True)
    selected=[];selected_indices=[];P=PermutationGroup([identity])
    for i in indices:
        if not P.contains(N[i]):
            selected.append(N[i]);selected_indices.append(i);P=PermutationGroup(selected)
            print('N generators',len(selected),'order',P.order(),flush=True)
    assert all(P.contains(g) for g in N)
    pn=int(P.order());print('N image order',pn,flush=True)
    D=P.derived_subgroup();dn=int(D.order());print('N derived image order',dn,'abelianization',pn//dn,flush=True)
    # In P/P-prime all factors commute, so adjoining these actual powers
    # and integral-kernel products gives precisely the two required images.
    def enlarge(generators):
        Q=D;selected=[]
        for g in generators:
            if not Q.contains(g):
                selected.append(g);Q=PermutationGroup(list(D.generators)+selected)
                print('abelian enlargement generators',len(selected),'order',Q.order(),flush=True)
        assert all(Q.contains(g) for g in generators)
        return Q,selected
    powers=[g**6 for g in N]
    K,kextra=enlarge(powers)
    integer_kernel=np.load(here/'de_ferrari_mod9_module.npz')['integral_abelianization_kernel']
    primegens=[]
    for v in integer_kernel.T:
        g=identity
        for i,a in enumerate(v):
            if a:g=g*(powers[i]**int(a))
        primegens.append(g)
    C,cextra=enlarge(primegens)
    kn,cn=int(K.order()),int(C.order())
    for a in (Permutation(s.tolist()),Permutation(r.tolist())):
        assert all(C.contains(~a*g*a) for g in C.generators)
        assert all(K.contains(~a*g*a) for g in K.generators)
    gout=json.loads((here/'de_ferrari_a5_source.json').read_text())['induced_B_image_order']
    out={'source_order':gout,'N_image_order':pn,'source_mod_N_order':gout//pn,
         'N_derived_image_order':dn,'N_abelianization_order':pn//dn,
         'full_K6_image_order':kn,'F_prime_K6_image_order':cn,
         'source_mod_K6_order':gout//kn,'source_mod_F_prime_K6_order':gout//cn,
         'N_selected_generator_indices':selected_indices,
         'full_power_enlargement_generators':len(kextra),'prime_power_enlargement_generators':len(cextra),
         'integral_abelianization_kernel_rank':95,'both_images_stable_under_B':True,
         'factorizations':{name:{str(p):e for p,e in factorint(n).items()} for name,n in [('N',pn),('derived',dn),('K6',kn),('prime',cn)]},
         'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_a5_corrections.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_a5_corrections.npz',N_images=np.array([g.array_form for g in N]),
                       derived_generators=np.array([g.array_form for g in D.generators]),
                       full_generators=np.array([g.array_form for g in K.generators]),
                       prime_generators=np.array([g.array_form for g in C.generators]))
    print(json.dumps(out,indent=2),flush=True)

if __name__=='__main__':main()
