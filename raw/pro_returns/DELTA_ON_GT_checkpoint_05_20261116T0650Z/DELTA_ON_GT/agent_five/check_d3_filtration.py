"""Exact augmentation/boundary/proper filtration for the D3 F4 chains."""
import json
import numpy as np
from check_ferrari_d3_fox import *

D=np.load(ROOT/'ferrari_d3_fox.npz')
cusps=[[1,-4,-2],[1,3,5,-1],[2,4,-5,-2],[1,-5,-3,2,-1,5,-1]]
exp=np.zeros((4,5),dtype=np.int16)
for j,w in enumerate(cusps):
    for l in w:exp[j,abs(l)-1]+=1 if l>0 else -1
V=fox_at(cusps+[[]],characters)[:,:,:4]
V=np.where((characters@exp.T%3==0)[:,None,:],V,0)
boundary=ROOTS[characters]^1
def independent(vectors):
    ech={};out=[]
    for v in vectors:
        w=v.copy()
        for j,r in sorted(ech.items()):w^=MUL[w[j],r]
        nz=np.flatnonzero(w)
        if len(nz):
            j=int(nz[0]);ech[j]=MUL[INV[w[j]],w];out.append(v.copy())
    return out
T=[];bd=[];hd=[]
for ch in range(N):
    b=independent(V[ch].T);bd.append(len(b));r=boundary[ch];nz=np.flatnonzero(r)
    if len(nz):
        j=int(nz[0]);p=np.zeros(5,dtype=np.int16);p[j]=INV[r[j]]
        basis=independent(b+[v^MUL[r[k],p] for k,v in enumerate(np.eye(5,dtype=np.int16))])
        assert len(basis)==4;basis.append(p);hd.append(4)
    else:basis=independent(b+list(np.eye(5,dtype=np.int16)));hd.append(5)
    assert len(basis)==5;T.append(np.stack(basis,axis=1))
T=np.stack(T);Ti=minv(T);bd=np.array(bd);hd=np.array(hd)
assert sum(bd)==323 and sum(hd)==973 and sum(hd-bd)==650
adapted=[]
for p,m in zip(D['generator_permutations'],D['generator_blocks']):
    a=mm(Ti[p],mm(m,T));adapted.append(a)
    assert np.array_equal(bd[p],bd)
    for k in range(N):
        b,h=int(bd[k]),int(hd[k]);assert not np.any(a[k,b:,:b]) and not np.any(a[k,h:,:h])
XA=np.stack([mm(Ti[p],mm(m,T)) for p,m in zip(D['X_permutations'],D['X_blocks'])])
fixed=np.flatnonzero(np.all(D['X_permutations'][:2]==IP,axis=0))
harmonic_orbits=orbits(list(D['X_permutations'][:2]))
assert sum(len(o)==1 for o in harmonic_orbits)==27
assert sum(len(o)==8 for o in harmonic_orbits)==27
assert all(len(o) in (1,8) for o in harmonic_orbits)
fixed3=[int(k) for k in fixed if hd[k]-bd[k]==3]
assert fixed3==[41,43,77,79,125,161,202,238]
np.savez_compressed(ROOT/'ferrari_d3_filtration.npz',basis=T,basis_inverse=Ti,
 boundary_dimensions=bd,homology_dimensions=hd,cusp_vectors=V,
 generator_adapted_blocks=np.stack(adapted),X_adapted_blocks=XA)
np.savez_compressed(ROOT/'ferrari_d3_fixed_proper3.npz',character_indices=fixed3,
 characters=characters[fixed3],X_blocks=XA[:,fixed3,1:4,1:4])
out={'homology_dimension':973,'boundary_dimension':323,'proper_dimension':650,
 'all_L_generators_preserve_filtration':True,'harmonic_fixed_character_count':len(fixed),
 'harmonic_character_orbit_sizes':[len(o) for o in harmonic_orbits],
 'fixed_proper3_characters':fixed3,'fixed_proper3_cusp_phases':(characters[fixed3]@exp.T%3).tolist()}
(ROOT/'ferrari_d3_filtration.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
