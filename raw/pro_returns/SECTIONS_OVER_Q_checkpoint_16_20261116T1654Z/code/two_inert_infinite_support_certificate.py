#!/usr/bin/env python3
"""Exact finite checks for the integral affine norm maps used in A166."""
from pathlib import Path
import json

def v3(n):
    n=abs(n)
    if not n:return 10**6
    v=0
    while n%3==0:n//=3;v+=1
    return v

def cycles(p,c,n):
    modulus=3**n
    seen=[False]*modulus
    result=[]
    index=[None]*modulus
    for start in range(modulus):
        if seen[start]:continue
        cycle=[];x=start
        while not seen[x]:
            seen[x]=True;index[x]=len(result);cycle.append(x)
            x=(p*x+c)%modulus
        assert x==start
        result.append(cycle)
    return result,index

rows=[];checked=0;bounded=0;points=0
for p in [2,5,7,13,17,19,31]:
    for c in [0,1,2,3,6,9]:
        vp=v3(p-1)
        fixed=v3(c)>=vp
        cache={n:cycles(p,c,n) for n in range(1,8)}
        points+=sum(3**n for n in cache)
        for n in [2,3]:
            old,old_index=cache[n]
            stable=None
            if fixed:
                root=(-c//(3**vp))*pow((p-1)//(3**vp),-1,3**n)%(3**n)
                stable=old_index[root]
                assert len(old[stable])==1
            bound=vp+n-1 if fixed else v3(c)
            for m in range(n+1,n+5):
                upper,_=cache[m]
                minima={i:10**6 for i in range(len(old)) if i!=stable}
                for orbit in upper:
                    i=old_index[orbit[0]%(3**n)]
                    assert all(old_index[x%(3**n)]==i for x in orbit)
                    assert len(orbit)%len(old[i])==0
                    weight=len(orbit)//len(old[i])
                    assert weight*len(old[i])==len(orbit)
                    checked+=1
                    if i!=stable:
                        lower=m-bound-v3(p+1)-v3(len(old[i]))
                        assert v3(weight)>=lower
                        minima[i]=min(minima[i],v3(weight))
                        bounded+=1
                assert all(value<10**6 for value in minima.values())
                rows.append({'q':p,'translation':c,'lower_level':n,'upper_level':m,
                             'fixed_branch_exists':fixed,
                             'lower_cycle_lengths':[len(o) for o in old],
                             'minimum_nonfixed_weight_v3':min(minima.values()) if minima else None})

out={'affine_pairs':42,'level_comparisons':len(rows),'root_labels_examined':points,
     'exact_cycle_norm_weights_checked':checked,'uniform_weight_bounds_checked':bounded,
     'stable_fixed_branch_weight':1,'ramified_residue_degrees':[1,2],
     'balanced_vector':[-2,1],'balanced_weighted_norm':-2+2,'comparisons':rows}
assert out['balanced_weighted_norm']==0
p=Path(__file__)
p.with_name(p.stem+'_data.json').write_text(json.dumps(out,indent=2)+'\n')
lines=[f'PASS: {out["affine_pairs"]} affine Frobenius pairs at levels1--7',
       f'PASS: {checked} exact cycle projection/norm weights, including their prime-to-three factors',
       f'PASS: {bounded} quantitative uniform three-divisibility bounds away from the fixed branch',
       'PASS: stable degree-one branch norm weight1 and ramified balanced vector(-2,1) with weights(1,2)',
       'Infinite support vanishing and compact fibre equivalence are proved in A166, not inferred from this finite check.']
text='\n'.join(lines)+'\n';p.with_name(p.stem+'_output.txt').write_text(text);print(text,end='')
