#!/usr/bin/env python3
"""Complete N, K6 and F-prime correction images in the small A6 targets.

The finite groups are exact permutation groups of the faithfully compressed
six-coset/six-evaluation source.  The integral 95-column kernel used for
K6 intersect F-prime is checked for equality with the saturated kernel of
the literal rank-97 N-basis abelianization map.
"""
from pathlib import Path
import argparse,json,time
import numpy as np
from sympy import factorint,Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form
from sympy.combinatorics import PermutationGroup,Permutation
from de_ferrari_a6_source_data import load_data

HERE=Path(__file__).resolve().parent

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--outer',action='store_true')
    args=parser.parse_args();start=time.time();d=load_data()
    tag='de_ferrari_a6_'+('outer' if args.outer else 'perm')
    data=np.load(HERE/(tag+'_source_compressed.npz'))
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
    D=P.derived_subgroup();dn=int(D.order())
    print('N derived image order',dn,'abelianization',pn//dn,flush=True)
    assert all(D.contains(~a*g*a) for a in selected for g in D.generators)
    assert all(D.contains(a*b*~a*~b) for a in selected for b in selected)
    # In P/D these images commute.  The products below give the exact
    # images of N-prime N^6 and its intersection with the literal F-prime.
    def enlarge(generators):
        Q=D;extra=[]
        for g in generators:
            if not Q.contains(g):
                extra.append(g);Q=PermutationGroup(list(D.generators)+extra)
                print('abelian enlargement generators',len(extra),'order',Q.order(),flush=True)
        assert all(Q.contains(g) for g in generators)
        return Q,extra
    powers=[g**6 for g in N];K,kextra=enlarge(powers)
    integral=np.load(HERE/'de_ferrari_mod9_module.npz')['integral_abelianization_kernel']
    fab=np.array([[sum(1 if a==j else -1 if a==-j else 0 for a in d['fword'](w))
                   for w in d['Nwords']] for j in (1,2)],dtype=np.int64)
    assert integral.shape==(97,95) and not np.any(fab@integral)
    assert Matrix(fab.tolist()).rank()==2
    smith=smith_normal_form(Matrix(integral.tolist()),domain=ZZ)
    assert [abs(int(smith[i,i])) for i in range(95)]==[1]*95
    primegens=[]
    for v in integral.T:
        g=identity
        for i,a in enumerate(v):
            if a:g=g*(powers[i]**int(a))
        primegens.append(g)
    C,cextra=enlarge(primegens);kn,cn=int(K.order()),int(C.order())
    for a in (Permutation(s.tolist()),Permutation(r.tolist())):
        assert all(C.contains(~a*g*a) for g in C.generators)
        assert all(K.contains(~a*g*a) for g in K.generators)
    print('complete K6 and F-prime correction orders',kn,cn,flush=True)
    # Remove redundant derived generators before a second complete
    # derived-subgroup calculation; containment is checked in both ways.
    chosen=[];compact=PermutationGroup([identity])
    for p in sorted(C.generators,key=lambda p:int(p.order()),reverse=True):
        if not compact.contains(p):
            chosen.append(p);compact=PermutationGroup(chosen)
            print('compact correction generators',len(chosen),'order',compact.order(),flush=True)
    assert int(compact.order())==cn and all(compact.contains(p) for p in C.generators)
    second=compact.derived_subgroup();second_order=int(second.order())
    print('correction derived order',second_order,flush=True)
    F=PermutationGroup([word(d['xword']),word(d['yword'])]);Forder=int(F.order())
    E=F.derived_subgroup();Eorder=int(E.order())
    assert all(E.contains(g) for g in C.generators)
    print('F image / derived / derived mod correction',Forder,Eorder,Eorder//cn,flush=True)
    gout=json.loads((HERE/(tag+'_source.json')).read_text())['source_image_order']
    out={'source_order':gout,'N_image_order':pn,'source_mod_N_order':gout//pn,
         'N_derived_image_order':dn,'N_abelianization_order':pn//dn,
         'full_K6_image_order':kn,'F_prime_K6_image_order':cn,
         'source_mod_K6_order':gout//kn,'source_mod_F_prime_K6_order':gout//cn,
         'N_selected_generator_indices':selected_indices,
         'N_selected_literal_B_words':[d['Nwords'][i] for i in selected_indices],
         'full_power_enlargement_generators':len(kextra),'prime_power_enlargement_generators':len(cextra),
         'integral_abelianization_kernel_rank':95,'integral_kernel_saturation_checked':True,
         'both_images_stable_under_B':True,'correction_derived_order':second_order,
         'correction_group_is_perfect':second_order==cn,'compact_correction_generator_count':len(chosen),
         'F_image_order':Forder,'F_derived_image_order':Eorder,
         'F_derived_mod_correction_order':Eorder//cn,
         'factorizations':{name:factorint(n) for name,n in
            [('N',pn),('derived',dn),('K6',kn),('prime',cn),('second',second_order),('F',Forder),('Fprime',Eorder)]},
         'seconds':round(time.time()-start,3)}
    (HERE/(tag+'_corrections.json')).write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(HERE/(tag+'_corrections.npz'),N_images=np.array([g.array_form for g in N]),
        derived_generators=np.array([g.array_form for g in D.generators]),
        full_generators=np.array([g.array_form for g in K.generators]),
        prime_generators=np.array([g.array_form for g in C.generators]),
        compact_prime_generators=np.array([g.array_form for g in chosen]),
        second_derived_generators=np.array([g.array_form for g in second.generators]),
        F_derived_generators=np.array([g.array_form for g in E.generators]),
        integral_abelianization_kernel=integral,N_F_abelianization=fab)
    print(json.dumps({k:v for k,v in out.items() if k!='N_selected_literal_B_words'},indent=2),flush=True)

if __name__=='__main__':main()
