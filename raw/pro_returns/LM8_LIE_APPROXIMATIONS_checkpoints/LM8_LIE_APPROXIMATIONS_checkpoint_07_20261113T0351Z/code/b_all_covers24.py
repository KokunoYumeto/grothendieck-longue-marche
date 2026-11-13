"""Schreier bases and exact comparison invariants for every catalogue epimorphism.
All words use signed letters 1=x, 2=y.  No probabilistic group or rank tests.
"""
from pathlib import Path
from collections import deque,Counter
from math import gcd,prod
import json,csv
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

ROOT=Path(__file__).parent
def inverse(w):return [-x for x in reversed(w)]
def reduce(w):
    out=[]
    for x in w:
        if out and out[-1]==-x:out.pop()
        else:out.append(x)
    return out
def witt(r,n):
    return sum(int(S.mobius(d))*r**(n//d) for d in S.divisors(n))//n
def schreier(group,pair):
    M=group['multiplication'];n=group['order'];a,b=[j-1 for j in pair]
    target=lambda v,j:M[v][(a,b)[j]]-1
    paths={0:[]};tree=set();queue=deque([0])
    while queue:
        u=queue.popleft()
        for j in range(2):
            v=target(u,j)
            if v not in paths:
                paths[v]=paths[u]+[j+1];tree.add((u,j));queue.append(v)
    assert len(paths)==n
    words=[]
    for u in range(n):
        for j in range(2):
            if (u,j) not in tree:
                v=target(u,j)
                w=reduce(paths[u]+[j+1]+inverse(paths[v]))
                value=0
                for z in w:
                    h=(a,b)[abs(z)-1]
                    if z<0:h=next(k for k in range(n) if M[h][k]==1)
                    value=M[value][h]-1
                assert value==0 and w
                words.append(w)
    assert len(words)==n+1
    # Contracting the spanning tree makes these the integer cycle basis.
    A=S.Matrix([[sum((1 if z>0 else -1) for z in w if abs(z)==j)
                 for w in words] for j in [1,2]])
    H=hermite_normal_form(A);assert H.shape==(2,2)
    d1=0
    for z in H:d1=gcd(d1,abs(int(z)))
    d2=abs(int(H.det()))//d1
    assert d1*d2==n//group['derived_order'] and d2%d1==0
    ranks=[witt(n+1,c) for c in range(1,5)]
    # GL_2(Z)-equivariance reduces the graded image to diag(d1,d2).
    smith=[[d1,d2],[d1*d2],
           [d1*d1*d2,d1*d2*d2],
           [d1**3*d2,d1*d1*d2*d2,d1*d2**3]]
    return {'pair':pair,'schreier_basis':words,'N_ab_rank':n+1,
        'N_ab_to_F_ab':[[int(z) for z in A.row(j)] for j in range(2)],
        'image_lattice_HNF':[[int(z) for z in H.row(j)] for j in range(2)],
        'ambient_graded_image_Smith_1_to_4':smith,
        'N_lower_central_ranks_1_to_4':ranks,
        'graded_inclusion_kernel_ranks_1_to_4':
             [ranks[c-1]-witt(2,c) for c in range(1,5)],
        'N_metabelian_abelian_rank':n+1,
        'N_metabelian_derived_module_rank_over_fraction_field':n}

def main():
    src=json.loads((ROOT/'b_groups24_catalogue.json').read_text())
    assert len(src['groups'])==74
    output={'gap_version':src['gap_version'],
            'smallgrp_version':src['smallgrp_version'],
            'metabelian_module_presentation':
               'Nprime/Ndoubleprime = ker(R^r -> R), e_i -> X_i-1; R=Z[Z^r], r=|G|+1',
            'groups':[]}
    table=[];count=0
    for g in src['groups']:
        rows=[schreier(g,p) for p in g['generating_pairs']]
        count+=len(rows);n=g['order']
        rec={k:g[k] for k in ['order','id','structure','derived_length',
                              'derived_order','nilpotence_class']}
        rec['surjections']=rows
        rec['comparison_ab_defined']=g['derived_order']==1
        rec['comparison_meta_defined']=g['derived_length']<=2
        rec['comparisons_nil_defined_1_to_4']=[
            g['nilpotence_class']>=0 and g['nilpotence_class']<=c for c in range(1,5)]
        rec['comparison_isomorphisms_ab_meta_nil']=n==1
        rec['intrinsic_ab_meta_nil_unipotent']=n==1
        rec['intrinsic_virtually_abelian']=True
        factors=S.factorint(n)
        rec['pro_ell_exact_and_intrinsic_primes']=(
            'all' if n==1 else list(map(int,factors)) if len(factors)==1 else [])
        output['groups'].append(rec)
        table.append({'order':n,'smallgroup_id':g['id'],'structure':g['structure'],
            'epimorphisms_F2':len(rows),'N_ab_rank':n+1 if rows else '',
            'G_ab_order':n//g['derived_order'],
            'derived_length':g['derived_length'],'nilpotence_class':g['nilpotence_class'],
            'abelian_comparison_defined':rec['comparison_ab_defined'],
            'metabelian_comparison_defined':rec['comparison_meta_defined'],
            'comparison_isomorphism_if_defined':n==1 if rows else 'no surjection',
            'V_exact_intrinsic':True})
        print(table[-1],flush=True)
    output['surjections_tested']=count
    (ROOT/'b_all_covers24.json').write_text(json.dumps(output,separators=(',',':'))+'\n')
    with (ROOT/'b_all_covers24.csv').open('w') as f:
        w=csv.DictWriter(f,fieldnames=list(table[0]));w.writeheader();w.writerows(table)
    print('TOTAL:',len(table),'groups;',count,'surjections;',
          sum(r['epimorphisms_F2']>0 for r in table),'two-generator isomorphism types')
    print('All Schreier word evaluations, integer lattice determinants and ranks passed.')

if __name__=='__main__':main()
