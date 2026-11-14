"""All ordered epimorphisms F_2 -> G in the 74 group models |G|<=24.

Computes Cayley-graph cycle bases, integral abelianization comparison,
deck characters, and lower-central/free-metabelian invariants of the
Schreier kernel. The mathematical completeness of the invariant formulas
is proved in section E; no finite nilpotent quotient stands for an
uncomputed infinite metabelian group.
"""
from pathlib import Path
from collections import deque,Counter
from itertools import combinations
from math import gcd
import csv,json
import sympy as sp

BASE=Path(__file__).resolve().parent
data=json.loads((BASE/'e_group_input.json').read_text())

def compose(a,b):return tuple(a[b[i]] for i in range(len(a)))

def model(cycles):
    degree=max([1]+[a for gen in cycles for cyc in gen for a in cyc])
    gens=[]
    for gen in cycles:
        p=list(range(degree))
        for c in gen:
            for i,a in enumerate(c):p[a-1]=c[(i+1)%len(c)]-1
        gens.append(tuple(p))
    ident=tuple(range(degree));elts=[ident];idx={ident:0}
    for a in elts:
        for b in gens:
            c=compose(a,b)
            if c not in idx:idx[c]=len(elts);elts.append(c)
    tab=[[idx[compose(a,b)] for b in elts] for a in elts]
    inv=[next(j for j in range(len(elts)) if tab[i][j]==0) for i in range(len(elts))]
    return elts,tab,inv

def subgroup(tab,gens):
    out={0};queue=[0]
    for a in queue:
        for b in gens:
            c=tab[a][b]
            if c not in out:out.add(c);queue.append(c)
    return out

def comm(tab,inv,a,b):return tab[tab[tab[a][b]][inv[a]]][inv[b]]

def commsub(tab,inv,A,B):
    return subgroup(tab,{comm(tab,inv,a,b) for a in A for b in B})

def schreier(tab,a,b):
    n=len(tab);gens=[a,b];paths={0:[]};tree=set();queue=[0]
    for v in queue:
        for j,g in enumerate(gens):
            w=tab[v][g];edge=2*v+j
            if w not in paths:
                paths[w]=paths[v]+[edge];tree.add(edge);queue.append(w)
    assert len(queue)==n
    chords=[e for e in range(2*n) if e not in tree]
    C=[]
    for e in chords:
        v,j=divmod(e,2);w=tab[v][gens[j]]
        c=[0]*(2*n)
        for f in paths[v]:c[f]+=1
        c[e]+=1
        for f in paths[w]:c[f]-=1
        C.append(c)
        boundary=[0]*n
        for f,k in enumerate(c):
            u,t=divmod(f,2)
            boundary[u]-=k;boundary[tab[u][gens[t]]]+=k
        assert not any(boundary)
    assert len(C)==n+1
    P=[[sum(c[j::2]) for c in C] for j in range(2)]
    minors=[P[0][i]*P[1][j]-P[1][i]*P[0][j] for i,j in combinations(range(n+1),2)]
    detindex=0
    for v in minors:detindex=gcd(detindex,abs(v))
    traces=[]
    for g in range(n):
        trace=0
        for j,e in enumerate(chords):
            v,t=divmod(e,2)
            # preimage under left multiplication by g
            u=next(u for u in range(n) if tab[g][u]==v)
            trace+=C[j][2*u+t]
        traces.append(trace)
        assert trace==(n+1 if g==0 else 1)
    return C,chords,P,detindex,traces

def witt(r,k):
    return int(sum(sp.mobius(d)*r**(k//d) for d in sp.divisors(k))//k)

def isomorphism_from_pairs(t1,t2,p1,p2):
    n=len(t1);mapping={0:0};queue=[0]
    for a in queue:
        for b,c in zip(p1,p2):
            x=t1[a][b];y=t2[mapping[a]][c]
            if x in mapping:
                if mapping[x]!=y:return False
            else:mapping[x]=y;queue.append(x)
    return len(mapping)==n and len(set(mapping.values()))==n

summary=[];pairsrows=[];models=[];witnesses=[]
for record in data:
    elts,tab,inv=model(record['cycles']);n=len(elts)
    assert n==record['order'],record['name']
    allg=set(range(n));derived=commsub(tab,inv,allg,allg)
    second=commsub(tab,inv,derived,derived)
    lower=allg;lc=[n]
    for _ in range(1,6):
        lower=commsub(tab,inv,lower,allg);lc.append(len(lower))
    pairs=[(a,b) for a in range(n) for b in range(n) if len(subgroup(tab,[a,b]))==n]
    common=None
    for a,b in pairs:
        C,chords,P,index,traces=schreier(tab,a,b)
        assert index==n//len(derived)
        pairsrows.append({'order':n,'smallgroup_id':record['id'],'group':record['name'],
                          'x_index':a,'y_index':b,'N_rank':n+1,'H1_map_rank':2,
                          'H1_image_index':index,'H1_kernel_rank':n-1,
                          'meta_Alexander_generic_rank':n,
                          'gamma1_rank':n+1,'gamma2_rank':witt(n+1,2),
                          'gamma3_rank':witt(n+1,3),'gamma4_rank':witt(n+1,4)})
        if common is None:
            common=(C,chords,P,traces)
    if common:
        C,chords,P,traces=common
        witnesses.append({'order':n,'id':record['id'],'name':record['name'],'pair':pairs[0],
                          'cycle_basis_rows':C,'non_tree_edges':chords,'pushforward_rows':P,
                          'deck_traces':traces,'multiplication_table':tab})
    models.append({'record':record,'table':tab,'pairs':pairs})
    row={'order':n,'id':record['id'],'name':record['name'],'epimorphisms':len(pairs),
         'derived_order':len(derived),'second_derived_order':len(second),
         'lower_central_orders':lc,'N_rank':n+1 if pairs else None,
         'N_meta_Alexander_generic_rank':n if pairs else None,
         'N_lower_central_ranks_1_to_4':[witt(n+1,k) for k in range(1,5)] if pairs else [],
         'ab_exact':n==1,'meta_exact':n==1,'nilpotent_exact':n==1,
         'pro_p_exact_primes':[int(p) for p,e in sp.factorint(n).items()] if len(sp.factorint(n))==1 else [],
         'pro_unipotent_exact':n==1}
    summary.append(row)
    print(f"{n:2},{record['id']:2} {record['name']:12} epis={len(pairs):3} N_rank={row['N_rank']} Nmeta_generic={row['N_meta_Alexander_generic_rank']} gamma1..4={row['N_lower_central_ranks_1_to_4']} G'={len(derived)} G''={len(second)}")

# Distinctness for every two-generated model is checked by exhausting the
# possible images of a generating pair in every other model of its order.
nonisomorphism_tests=0
for i,A in enumerate(models):
    if not A['pairs']:continue
    for B in models[i+1:]:
        if B['record']['order']!=A['record']['order'] or not B['pairs']:continue
        for pair in B['pairs']:
            nonisomorphism_tests+=1
            assert not isomorphism_from_pairs(A['table'],B['table'],A['pairs'][0],pair), (A['record']['name'],B['record']['name'])

assert len(summary)==74
counts=Counter(r['order'] for r in summary)
assert [counts[n] for n in range(1,25)]==[1,1,1,2,1,2,1,5,2,2,1,5,1,2,1,14,1,5,1,5,2,2,1,15]
(BASE/'e_smallgroups.json').write_text(json.dumps({'summary':summary,'total_epimorphisms':len(pairsrows),'nonisomorphism_pair_tests':nonisomorphism_tests,'all_checks':True},indent=2)+'\n')
(BASE/'e_smallgroups_witnesses.json').write_text(json.dumps(witnesses,indent=2)+'\n')
with (BASE/'e_all_surjections.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(pairsrows[0]));w.writeheader();w.writerows(pairsrows)
print('Models:',len(summary),'two-generated:',sum(r['epimorphisms']>0 for r in summary),'epimorphisms:',len(pairsrows),'nonisomorphism tests:',nonisomorphism_tests)
print('All Cayley-cycle boundaries, Smith indices, deck characters and distinctness tests PASS.')
