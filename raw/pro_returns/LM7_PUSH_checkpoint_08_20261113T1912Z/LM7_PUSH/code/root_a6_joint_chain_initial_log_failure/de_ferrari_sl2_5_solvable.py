#!/usr/bin/env python3
"""Exact maximal solvable quotient of the SL2(F5) Ferrari target.

The perfect normal free factor SL2(F5)^19 is killed explicitly.
The remaining quotient C2^2 semidirect Nielsen image is represented
faithfully on251 points.  Its terminal derived subgroup is computed,
and the resulting quotient is compared with the actual binary target.
"""
from pathlib import Path
import json,time
import numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
from de_ferrari_sl2_5_model import FerrariSL2Five
from de_ferrari_two_model import FerrariTwo

here=Path(__file__).resolve().parent

def automorphism_permutation(H,g):
    p,c=g[:19],g[19:38];old=np.r_[p,c,c]
    first=H.old.permutation(old,True).array_form
    E=g[38:76].reshape(19,2);M=g[76:80].reshape(2,2)
    Mi=np.array([[M[1,1],M[0,1]],[M[1,0],M[0,0]]],dtype=np.int64)
    points=[(0,0),(1,0),(0,1),(1,1)];second=[]
    for j in range(19):
        for z in range(2):
            for t in points:
                u=Mi@np.array(t)%2;zz=(z+E[j]@u)%2
                second.append(95+8*int(p[j])+4*int(zz)+points.index(tuple(u)))
    return first+second

def quotient_permutation(H,g):
    first=automorphism_permutation(H,g)
    inverse=H.inv(g);M=inverse[76:80].reshape(2,2);t=inverse[99:]
    points=[(0,0),(1,0),(0,1),(1,1)]
    return Permutation(first+[247+points.index(tuple((M@np.array(v)+t)%2)) for v in points])

def main():
    start=time.time();H=FerrariSL2Five();gs=[H.a,H.b,H.c]
    perms=[quotient_permutation(H,g) for g in gs]
    for a in gs+[H.inv(g) for g in gs]:
        for b in gs:assert quotient_permutation(H,H.mul(a,b))==quotient_permutation(H,a)*quotient_permutation(H,b)
    R=PermutationGroup(perms);order=int(R.order())
    nielsen=json.loads((here/'de_ferrari_sl2_5_nielsen.json').read_text())
    assert order==4*nielsen['lifted_group_order']
    print('faithful quotient by perfect free factor order',order,flush=True)
    D=R;orders=[order];identity=Permutation(list(range(251)))
    for stage in range(1,15):
        selected=[];C=PermutationGroup([identity])
        for g in sorted(D.generators,key=lambda p:int(p.order()),reverse=True):
            if not C.contains(g):
                selected.append(g);C=PermutationGroup(selected)
                if int(C.order())==orders[-1]:break
        assert int(C.order())==orders[-1] and all(C.contains(g) for g in D.generators)
        E=C.derived_subgroup();eo=int(E.order());orders.append(eo)
        print('derived stage',stage,'index',order//eo,flush=True)
        D=E
        if eo==orders[-2]:break
    else:raise AssertionError('derived series did not stabilize')
    qorder=order//int(D.order());reps=[identity];words=[[]];table=[]
    for i,g in enumerate(reps):
        row=[]
        for letter,a in enumerate(perms,1):
            h=g*a;j=next((j for j,u in enumerate(reps) if D.contains(h*(u**-1))),None)
            if j is None:j=len(reps);reps.append(h);words.append(words[i]+[letter])
            row.append(j)
        table.append(row)
    assert len(reps)==qorder
    for g in D.generators:
        for a in perms:assert D.contains(a*g*(a**-1))
    table=np.array(table,dtype=np.int64)
    controls=[];factor_degree=None
    for degree in (2,3):
        B=FerrariTwo(degree);seen={tuple(B.one):0};elements=[B.one];quotient=[0];bwords=[[]];failure=None
        for i,g in enumerate(elements):
            for letter,a in enumerate((B.a,B.b,B.c),1):
                h=B.mul(g,a);key=tuple(h);q=int(table[quotient[i],letter-1]);j=seen.get(key)
                if j is None:
                    j=len(elements);seen[key]=j;elements.append(h);quotient.append(q);bwords.append(bwords[i]+[letter])
                elif quotient[j]!=q:
                    failure={'first_word':bwords[j],'second_word':bwords[i]+[letter],
                             'first_quotient_value':quotient[j],'second_quotient_value':q};break
            if failure:break
        controls.append({'binary_degree':degree,'elements_checked':len(elements),'factorization_verified':failure is None,
                         'failure':failure})
        if failure is None:
            assert len(elements)==({2:1536,3:12288}[degree])
            assert set(quotient)==set(range(qorder));factor_degree=degree;break
    out={'quotient_by_perfect_free_factor_order':order,'complete_derived_orders':orders,
         'terminal_subgroup_is_perfect':True,'maximal_solvable_quotient_order':qorder,
         'solvable_quotient_cayley_table_generators':table.tolist(),
         'solvable_quotient_representative_B4_words':words,
         'binary_comparison_controls':controls,'binary_factor_degree':factor_degree,
         'seconds':round(time.time()-start,3)}
    here.joinpath('de_ferrari_sl2_5_solvable.json').write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(here/'de_ferrari_sl2_5_solvable.npz',
        terminal_perfect_generators=np.array([p.array_form for p in D.generators]),
        a=np.array(perms[0].array_form),b=np.array(perms[1].array_form),c=np.array(perms[2].array_form))
    print(json.dumps({k:v for k,v in out.items() if k not in ('solvable_quotient_cayley_table_generators','solvable_quotient_representative_B4_words')},indent=2),flush=True)

if __name__=='__main__':main()
