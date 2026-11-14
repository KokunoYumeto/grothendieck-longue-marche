#!/usr/bin/env python3
"""E.45: finite orbit coinvariants, actual transitions and representatives.

The infinite theorem is proved by integral measures and orbit decomposition.
This program verifies the finite group-ring maps from which those measures
are defined, their complete Smith invariants, and the proposed section
representatives.  No U-adic-only convergence is assumed.
"""
from pathlib import Path
from collections import Counter
import json
import numpy as np


def vp3(n):
    if n == 0:
        return 10**9
    n=abs(n)
    ans=0
    while n%3 == 0:
        n//=3
        ans+=1
    return ans


def orbits(q,b,n):
    unseen=set(range(n))
    answer=[]
    while unseen:
        start=min(unseen)
        cycle=[]
        x=start
        while x not in cycle:
            cycle.append(x)
            unseen.remove(x)
            x=(q*x+b)%n
        assert x == start
        answer.append(cycle)
    return answer


def operator_U(q,b,n):
    a=np.zeros((n-1,n-1),dtype=np.int64)
    for j in range(1,n):
        to=(q*j+b)%n
        if to:
            a[to-1,j-1]+=q
        a[j-1,j-1]-=1
        base=b%n
        if base:
            a[base-1,j-1]-=q
    return a


def dirac_difference(x,y,n):
    v=np.zeros(n-1,dtype=np.int64)
    if x%n:
        v[x%n-1]+=1
    if y%n:
        v[y%n-1]-=1
    return v


def smith_mod(matrix,exponent,retain=False):
    modulus=3**exponent
    a=matrix.copy()%modulus
    m,n=a.shape
    left=np.eye(m,dtype=np.int64)
    right=np.eye(n,dtype=np.int64)
    vals=[]
    for k in range(min(m,n)):
        sub=a[k:,k:]
        if not np.any(sub):
            break
        found=None
        for v in range(exponent):
            p=3**v
            candidates=np.argwhere((sub%p==0)&(sub%(3*p)!=0))
            if len(candidates):
                found=candidates[0]+k
                break
        assert found is not None
        i,j=map(int,found)
        a[[i,k]]=a[[k,i]]
        left[[i,k]]=left[[k,i]]
        a[:,[j,k]]=a[:,[k,j]]
        right[:,[j,k]]=right[:,[k,j]]
        p=3**v
        inverse=pow(int(a[k,k])//p,-1,modulus)
        assert inverse%3
        a[k]=(a[k]*inverse)%modulus
        left[k]=(left[k]*inverse)%modulus
        factors=a[:,k]//p
        factors[k]=0
        a=(a-factors[:,None]*a[k][None,:])%modulus
        left=(left-factors[:,None]*left[k][None,:])%modulus
        factors=a[k,:]//p
        factors[k]=0
        a=(a-a[:,k][:,None]*factors[None,:])%modulus
        right=(right-right[:,k][:,None]*factors[None,:])%modulus
        vals.append(v)
    diag=np.zeros_like(a)
    for i,v in enumerate(vals):
        diag[i,i]=3**v
    assert np.array_equal(a,diag)
    assert np.array_equal(((left@(matrix%modulus))%modulus@right)%modulus,diag)
    cert={'modulus':modulus,'valuations':vals}
    if retain:
        cert.update({'left_transform':left.tolist(),'right_transform':right.tolist(),
                     'matrix':matrix.tolist()})
    return cert


def representatives(q,b,k):
    n=3**k
    s=vp3(q-1)
    if vp3(b)>=s:
        r=((b//3**s)*pow((q-1)//3**s,-1,n))%n
        cols=[]
        for j in range(k):
            for unit in range(1,3**s):
                if unit%3:
                    cols.append(dirac_difference(3**j*unit-r,-r,n))
        return np.array(cols,dtype=np.int64).T
    t=vp3(b)
    cols=[q*dirac_difference(0,b,n)]
    cols += [dirac_difference(i,0,n) for i in range(1,3**t)]
    return np.array(cols,dtype=np.int64).T


def transition(q,b,k):
    n=3**k
    old,new=orbits(q,b,n),orbits(q,b,3*n)
    s=vp3(q-1)
    old_exps=[s+vp3(len(c)) for c in old]
    new_exps=[s+vp3(len(c)) for c in new]
    old_index={x:(i,j) for i,c in enumerate(old) for j,x in enumerate(c)}
    new_index={x:(i,j) for i,c in enumerate(new) for j,x in enumerate(c)}
    coeff=[[0]*len(new) for _ in old]
    for j,c in enumerate(new):
        i,offset=old_index[c[0]%n]
        assert new_exps[j]>=old_exps[i]
        coeff[i][j]=pow(q,-offset,3**old_exps[i])
    for x in range(3*n):
        i,a=old_index[x%n]
        j,z=new_index[x]
        modulus=3**old_exps[i]
        assert (coeff[i][j]*pow(q,-z,modulus)-pow(q,-a,modulus))%modulus==0
        assert all(coeff[h][j]==0 for h in range(len(old)) if h!=i)
    reduction=np.zeros((n-1,3*n-1),dtype=np.int64)
    for j in range(1,3*n):
        if j%n:
            reduction[j%n-1,j-1]=1
    assert np.array_equal(reduction@operator_U(q,b,3*n),operator_U(q,b,n)@reduction)
    return {'level':k,'lower_orbit_lengths':[len(c) for c in old],
            'upper_orbit_lengths':[len(c) for c in new],
            'lower_modulus_exponents':old_exps,'upper_modulus_exponents':new_exps,
            'weighted_integral_transition':coeff,
            'verified_group_ring_intertwining':True,
            'verified_weighted_integral_transition_on_every_dirac_mass':True}


cases=[(4,0),(4,3),(7,6),(19,0),(19,3),(19,6),(19,18),
       (37,0),(37,36),(109,3),(109,9),(109,108)]
results=[]
transitions=[]
for q,b in cases:
    s=vp3(q-1)
    integral=vp3(b)>=s
    for k in range(1,5):
        n=3**k
        cycles=orbits(q,b,n)
        exps=sorted(s+vp3(len(c)) for c in cycles)
        expected=sorted([exps[0]-s]+exps[1:])
        expected=[v for v in expected if v]
        matrix=operator_U(q,b,n)
        cert=smith_mod(matrix,max(exps)+1,
                       retain=(k==4 and (q,b) in [(19,0),(19,3),(109,9)]))
        assert len(cert['valuations'])==n-1
        assert sorted(v for v in cert['valuations'] if v)==expected
        assert sum(cert['valuations'])==sum(exps)-s
        if integral:
            r=((b//3**s)*pow((q-1)//3**s,-1,n))%n
            translation=np.column_stack([dirac_difference(j+r,r,n) for j in range(1,n)])
            assert np.array_equal(translation@matrix,operator_U(q,0,n)@translation)
            assert len(cycles)>=2
        else:
            t=vp3(b)
            assert len(cycles)==min(n,3**t)
            assert all(len(c)==max(1,3**(k-t)) for c in cycles)
        reps=representatives(q,b,k)
        generation=smith_mod(np.column_stack([matrix,reps]),max(exps)+1)
        assert generation['valuations']==[0]*(n-1)
        counts=dict(sorted(Counter(cert['valuations']).items()))
        print(f'q={q}, b={b}, k={k}, integral_shift={integral}, '
              f'orbits={len(cycles)}, Smith={counts}; representatives span.',flush=True)
        results.append({'q':q,'b':b,'level':k,'integral_shift':integral,
                        'orbit_cycles':cycles,'Smith':cert,
                        'predicted_positive_valuations':expected,
                        'representative_matrix':reps.tolist(),
                        'representatives_generate':True})
    for k in range(1,4):
        transitions.append({'q':q,'b':b,**transition(q,b,k)})

# The centered infinite series has a particularly direct continuity check:
# all terms with j>=k vanish in the group ring of Z/3^k.
for k in range(1,5):
    n=3**k
    for j in range(k,k+8):
        assert not np.any(dirac_difference(3**j,0,n))
print('Verified36 exact weighted-integral transitions and group-ring reductions.',flush=True)
print('Verified centered-series continuity in the profinite (3,U)-adic topology.',flush=True)
result={'status':'PASS','finite_cases':results,'transitions':transitions,
        'number_of_finite_cases':len(results),'number_of_transitions':len(transitions),
        'topology':'profinite completed group ring, equivalently (3,U)-adic; not U-adic alone',
        'infinite_scope':'The all-level measure and orbit proof is in E.45; finite checks verify actual maps and representatives.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
print('PASS: finite coinvariants, exact transitions, both representative families and topology checks.',flush=True)
