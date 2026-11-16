"""Exact normal-closure gate for the fixed cyclic R2 seed in D4 Fox chains.

Builds the complete augmentation / boundary / proper chain filtration,
and closes the six two-primary core values under the two pair generators.
"""
from pathlib import Path
import json
import numpy as np
from check_ferrari_d4_fox import (ROOT, N, IP, IM, ONE, ADD, NEG, MUL, INV,
 characters, ROOTS, mm, minv, mul, inv, eq, prod, power, comm, fox_at)

data=np.load(ROOT/'ferrari_d4_fox.npz')
X=list(zip(data['X_permutations'],data['X_blocks']))
seeds=np.load(ROOT/'ferrari_d4_controlled_seed.npz')['seed_blocks']
cusp_words=[[1,-4,-2],[1,3,5,-1],[2,4,-5,-2],[1,-5,-3,2,-1,5,-1]]
cusp_vectors=fox_at(cusp_words+[[]],characters)[:,:,:4]
cusp_exp=np.zeros((4,5),dtype=np.int16)
for j,w in enumerate(cusp_words):
    for l in w:cusp_exp[j,abs(l)-1]+=1 if l>0 else -1
cusp_trivial=characters@cusp_exp.T%4==0
cusp_vectors=np.where(cusp_trivial[:,None,:],cusp_vectors,0)
boundary_rows=ADD[ROOTS[characters],NEG[1]]

def independent_columns(vectors):
    echelon={};keep=[]
    for v in vectors:
        w=v.copy()
        for j,row in sorted(echelon.items()):
            w=ADD[w,NEG[MUL[w[j],row]]]
        nz=np.flatnonzero(w)
        if len(nz):
            j=int(nz[0]);echelon[j]=MUL[INV[w[j]],w];keep.append(v.copy())
    return keep

T=[];bdims=[];hdims=[]
for k in range(N):
    basis=independent_columns(cusp_vectors[k].T)
    b=len(basis);r=boundary_rows[k];nz=np.flatnonzero(r)
    if len(nz):
        j=int(nz[0]);p=np.zeros(5,dtype=np.int16);p[j]=INV[r[j]]
        candidates=[]
        for z in range(5):
            v=np.eye(5,dtype=np.int16)[z]
            candidates.append(ADD[v,NEG[MUL[r[z],p]]])
        basis=independent_columns(basis+candidates)
        assert len(basis)==4
        basis.append(p);h=4
    else:
        basis=independent_columns(basis+list(np.eye(5,dtype=np.int16)));h=5
    assert len(basis)==5
    T.append(np.stack(basis,axis=1));bdims.append(b);hdims.append(h)
T=np.stack(T);Ti=minv(T);bdims=np.array(bdims);hdims=np.array(hdims)
assert sum(bdims)==1023 # Four cusps, each with 4^4 lifts; one relation.
assert sum(hdims)==4097
assert sum(hdims-bdims)==3074
for g in [(data['generator_permutations'][j],data['generator_blocks'][j]) for j in range(3)]:
    adapted=mm(Ti[g[0]],mm(g[1],T))
    assert np.array_equal(bdims[g[0]],bdims)
    for k in range(N):
        b,h=bdims[k],hdims[k]
        assert not np.any(adapted[k,b:,:b])
        assert not np.any(adapted[k,h:,:h])

def orbit_twoparts(gens,initial,max_orbit=2048):
    gs=gens+[inv(g) for g in gens]
    queue=[];seen=set()
    for h in initial:
        key=h[1].astype(np.uint8).tobytes()
        if key not in seen:seen.add(key);queue.append(h)
    for h in queue:
        for g in gs:
            v=prod(g,h,inv(g));assert np.array_equal(v[0],IP)
            key=v[1].astype(np.uint8).tobytes()
            if key not in seen:
                seen.add(key);queue.append(v)
                if len(queue)>max_orbit:return queue,False
    return queue,True

reports=[]
for row,(i,j) in enumerate(((2,3),(4,0),(1,2),(3,4),(0,1))):
    ss=[(IP,seeds[6*row+k]) for k in range(6)]
    two=[power(s,3) for s in ss]
    three=[power(s,4) for s in ss]
    defects=[]
    for k,s in enumerate(three):
        adapted=mm(Ti,mm(s[1],T))
        bad=[]
        for ch in range(N):
            b,h=bdims[ch],hdims[ch];m=adapted[ch]
            if (np.any(m[b:,:b]) or np.any(m[h:,:h]) or
                not np.array_equal(m[:b,:b],np.eye(b,dtype=np.int16)) or
                not np.array_equal(m[b:h,b:h],np.eye(h-b,dtype=np.int16)) or
                not np.array_equal(m[h:,h:],np.eye(5-h,dtype=np.int16))):bad.append(ch)
        defects.append(bad)
    orbit,closed=orbit_twoparts([X[i],X[j]],two)
    noncommuting=None
    if closed:
        for k,g in enumerate(orbit):
            for l in range(k):
                if not eq(mul(g,orbit[l]),mul(orbit[l],g)):
                    noncommuting=[k,l];break
            if noncommuting:break
    report={'pair':[i+1,j+1],'three_part_graded_defect_counts':[len(v) for v in defects],
            'three_part_first_graded_defects':[v[:8] for v in defects],
            'two_part_conjugacy_orbit_size':len(orbit),'conjugacy_orbit_closed':closed,
            'two_part_conjugates_pairwise_commute':noncommuting is None if closed else None,
            'first_noncommuting_conjugates':noncommuting}
    reports.append(report);print(json.dumps(report),flush=True)
np.savez_compressed(ROOT/'ferrari_d4_filtration.npz',basis=T,basis_inverse=Ti,
 boundary_dimensions=bdims,homology_dimensions=hdims,cusp_vectors=cusp_vectors)
(ROOT/'ferrari_d4_seed_normal_closure.json').write_text(json.dumps(reports,indent=2)+'\n')
print(json.dumps({'total_homology_dimension':int(sum(hdims)),
 'boundary_dimension':int(sum(bdims)),'proper_dimension':int(sum(hdims-bdims)),
 'all_L_generators_preserve_filtration':True},indent=2))
