#!/usr/bin/env python3
"""Exhaustive finite arity-three audit for all marked B3 quotients <=1000.

Input: e_b3_quotients_complete.json, exported from the complete LINS search.
Uses integer permutation tables (NumPy only); no floating point arithmetic.
For every noncyclic quotient Q and every m mod N_ord, gcd(2m+1,N_ord)=1,
and f in [<a^2,b^2>,<a^2,b^2>], tests both exact DLL braid hexagons.
It then tests surjectivity on H=<a^2,b^2>, the braid and full-twist formulas,
and identifies the source kernel of the resulting surjection B3 -> Q.

A kernel K inside PB3 is marked deletion-compatible exactly when
| (PB3/K)_ab |= ord(a^2)^3 and ord((ab)^3)=ord(a^2).
For these K, intersection of the four forgetful kernel pullbacks in PB4
induces precisely K at arity three; the pentagon for commutator f is
identically true in every forgetful coordinate.  Thus the listed pairs
are all charming DLL shadows for THAT declared arity-four extension.
They are not asserted genuine; genuine means survival at every refinement.
For other kernels, the script certifies only necessary arity-three tests.
"""
from pathlib import Path
from collections import Counter
from math import gcd,lcm
import sys,json,time,hashlib
import numpy as np

BASE=Path(__file__).resolve().parent
SRC=BASE/'e_b3_quotients_complete.json'
DST=BASE/'e_b3_hexagons.json'
started=time.time()
data=json.loads(SRC.read_text())
assert data['bound']==1000 and data['kernel_count']==1946
assert len(data['quotients'])==1946

from e_braid_core import Table, signature

# Canonical regular actions identify normal kernels, not abstract groups.
sigs={};canons={};byordinal={}
for ordinal,row in enumerate(data['quotients'],1):
    n=row['index']
    p=np.array(row['a_permutation'],dtype=np.uint16)-1
    q=np.array(row['b_permutation'],dtype=np.uint16)-1
    sig,canon=signature(p,q,n)
    assert sig not in sigs,'A marked normal kernel was duplicated'
    sigs[sig]=ordinal;canons[sig]=canon;byordinal[ordinal]=row

Table.kernel_sigs=sigs
Table.kernel_canons=canons

rows=[];summary=Counter();compat=[]
for ordinal,row in enumerate(data['quotients'],1):
    n=row['index'];pa=row['a_permutation'];pb=row['b_permutation']
    if pa==pb:
        # The braid abelianization is Z, hence exactly one cyclic kernel at
        # each index. All units give genuine cyclotomic actions and f=1.
        phi=sum(gcd(k,n)==1 for k in range(n))
        rows.append({'kernel':ordinal,'order':n,'cyclic':True,'number_of_genuine_power_actions':phi,'formula':'a=b -> a^lambda, lambda in (Z/n)^*','source_kernel':ordinal})
        summary['cyclic_kernels']+=1;summary['cyclic_power_actions']+=phi
        continue
    t=Table(row);a,b=t.a,t.b;M=t.M;iv=t.inv
    assert t.mul(a,b,a)==t.mul(b,a,b)
    X,Y=t.pow(a,2),t.pow(b,2);C=t.pow(t.mul(a,b),3)
    x13=t.mul(b,X,int(iv[b]))
    assert t.mul(X,x13,Y)==C
    assert t.mul(a,C)==t.mul(C,a) and t.mul(b,C)==t.mul(C,b)
    H=t.closure([X,Y]);P=t.closure([X,Y,C])
    assert len(P)==row['pure_image_order']
    comm=t.mul(X,Y,int(iv[X]),int(iv[Y]))
    conjugates=np.unique(M[M[H,comm],iv[H]])
    derived=sorted(t.closure(conjugates))
    assert all(int(M[M[h,d],iv[h]]) in derived for h in (X,Y) for d in derived)
    nx=t.order(X);nc=t.order(C);Nord=lcm(nx,nc)
    assert t.order(Y)==nx and t.order(x13)==nx
    assert Nord==lcm(nx,t.order(Y),t.order(t.mul(X,x13)),t.order(t.mul(x13,Y)))
    pure_ab=len(P)//len(derived)
    compatible=row['kernel_contained_in_PB3'] and pure_ab==nx**3 and nc==nx
    if compatible:compat.append(ordinal)
    passed=[];hexagon_count=0;full_count=0;self_count=0;Hfail=0
    candidate_count=0
    for m in range(Nord):
        lam=2*m+1
        if gcd(lam,Nord)!=1:continue
        ap=t.mul(a,t.pow(X,m));bl=t.mul(b,t.pow(Y,m))
        h1=t.mul(a,b,t.pow(t.mul(x13,Y),m))
        h2=t.mul(b,a,t.pow(t.mul(X,x13),m))
        for f in derived:
            candidate_count+=1;fi=int(iv[f])
            bp=t.mul(fi,bl,f)
            if t.mul(ap,bp)!=t.mul(fi,h1):continue
            if t.mul(bp,ap)!=t.mul(h2,f):continue
            hexagon_count+=1
            assert t.mul(ap,bp,ap)==t.mul(bp,ap,bp)
            assert t.pow(t.mul(ap,bp),3)==t.pow(C,lam)
            full_count+=1
            hp=t.closure([t.pow(ap,2),t.pow(bp,2)])
            if len(hp)!=len(H):Hfail+=1;continue
            assert set(hp)==set(H)
            assert len(t.closure([ap,bp]))==n
            source=t.source(ap,bp)
            is_self=t.self_descent(ap,bp)
            assert is_self==(source==ordinal)
            self_count+=is_self
            passed.append([m,f+1,source])
    # Identity and complex conjugation are actual GT elements. Their
    # reductions must pass, although conjugation may move a normal kernel.
    assert any(m==0 and f==1 for m,f,s in passed)
    assert any(m==Nord-1 and f==1 for m,f,s in passed)
    by_m=Counter(v[0] for v in passed)
    friendly_count=sum(gcd(2*m+1,Nord)==1 for m in range(Nord))
    assert len(by_m)==friendly_count
    known_genuine=[v for v in passed if by_m[v[0]]==1 or (v[1]==1 and v[0] in (0,Nord-1))]
    class_two=t.mul(comm,X)==t.mul(X,comm) and t.mul(comm,Y)==t.mul(Y,comm)
    cyclotomic_modulus=None;exact_genuine=None
    if class_two:
        dc=t.order(comm)
        assert dc==len(derived) and Nord%dc==0
        cyclotomic_modulus=lcm(2*Nord,24*dc)
        pairmap={(v[0],v[1]):v for v in passed}
        images=set()
        for chi in range(cyclotomic_modulus):
            if gcd(chi,cyclotomic_modulus)!=1:continue
            assert (chi*chi-1)%24==0
            key=(((chi-1)//2)%Nord,t.pow(comm,((chi*chi-1)//24)%dc)+1)
            assert key in pairmap
            images.add(key)
        exact_genuine=[pairmap[k] for k in sorted(images)]
        assert all((v[0],v[1]) in images for v in known_genuine)
        known_genuine=exact_genuine
    all_genuine=len(passed)==len(known_genuine)
    image_complete=class_two or all_genuine
    rec={'kernel':ordinal,'order':n,'smallgroup_id':row['smallgroup_id'],'cyclic':False,
         'kernel_contained_in_PB3':row['kernel_contained_in_PB3'],
         'H_order':len(H),'pure_image_order':len(P),'derived_order':len(derived),
         'pure_abelianization_order':pure_ab,'order_x12':nx,'order_full_twist':nc,
         'N_ord':Nord,'friendly_m_count':friendly_count,'candidate_count':candidate_count,'two_hexagon_count':hexagon_count,
         'braid_and_full_twist_checks':full_count,'H_nonsurjective_hexagon_pairs':Hfail,
         'surjective_arity_three_pair_count':len(passed),'self_automorphism_pair_count':self_count,
         'forgetful_extension_induces_same_kernel':bool(compatible),
         'pentagon_for_every_commutator_f':bool(compatible),
         'all_charming_shadows_for_declared_extension':len(passed) if compatible else None,
         'gentle_GT_shadow_count':len(passed) if row['kernel_contained_in_PB3'] else None,
         'known_genuine_full_GT_pairs':known_genuine,
         'genuineness_reason':'For class<=2 H, f=[X,Y]^((chi^2-1)/24) and all cyclotomic residues occur; otherwise a unique surviving f at fixed m is forced genuine, and identity/complex-conjugation pairs are genuine.',
         'H_nilpotency_class_at_most_two':class_two,
         'class_two_cyclotomic_modulus':cyclotomic_modulus,
         'complete_full_GT_image_known':image_complete,
         'exact_full_GT_image_pairs_if_class_two':exact_genuine,
         'all_arity_three_pairs_genuine':all_genuine,
         'pairs_m_fpoint_sourcekernel':passed}
    rows.append(rec)
    summary['noncyclic_kernels']+=1
    summary['noncyclic_known_genuine_full_GT_pairs']+=len(known_genuine)
    summary['noncyclic_kernels_with_complete_full_GT_image']+=image_complete
    summary['noncyclic_class_two_H_kernels']+=class_two
    if class_two:summary['class_two_provably_nongenuine_arity_three_pairs']+=len(passed)-len(exact_genuine)
    if row['kernel_contained_in_PB3']:summary['gentle_GT_shadow_pairs']+=len(passed)
    for key in ('candidate_count','two_hexagon_count','surjective_arity_three_pair_count','self_automorphism_pair_count'):
        summary[key]+=rec[key]
    summary['kernels_contained_in_PB3']+=row['kernel_contained_in_PB3']
    if compatible:
        summary['forgetful_compatible_kernels']+=1
        summary['charming_shadows_for_forgetful_extensions']+=len(passed)
    if ordinal%50==0 or compatible:
        print('kernel',ordinal,'order',n,'H',len(H),'derived',len(derived),'Nord',Nord,'pairs',len(passed),'compatible',compatible,'seconds',round(time.time()-started,2),flush=True)
    if ordinal%100==0:
        DST.with_suffix('.checkpoint.json').write_text(json.dumps({'completed_kernel':ordinal,'summary':dict(summary),'rows':rows},separators=(',',':'))+'\n')
assert summary['cyclic_kernels']==1000 and summary['noncyclic_kernels']==946
out={'scope':'All 1946 marked B3 quotients of order <=1000. Exhaustive arity-three necessary GT tests; exact DLL charming shadows only for explicitly declared compatible forgetful extensions; no general genuineness claim.',
     'input':SRC.name,'bound':1000,'GAP':data['GAP'],'LINS':data['LINS'],'numpy':np.__version__,
     'regular_action_convention':'Input permutations act on right cosets; point 1 is the identity. fpoint is its one-based regular-action point. Source kernels are identified by exact canonical regular actions.',
     'summary':dict(summary),'compatible_kernel_ordinals':compat,'rows':rows,'seconds':round(time.time()-started,3)}
DST.write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',dict(summary),'seconds',out['seconds'],flush=True)
