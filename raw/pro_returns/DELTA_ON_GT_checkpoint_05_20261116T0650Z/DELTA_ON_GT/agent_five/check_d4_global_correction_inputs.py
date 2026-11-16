"""Exact full-chain hypotheses for the actual source correction at D4.

The only remaining step is the stated elementary Goursat argument,
not any search over independently assigned f-values.
"""
import json
import numpy as np
from check_ferrari_d4_fox import *

D=np.load(ROOT/'ferrari_d4_fox.npz');F=np.load(ROOT/'ferrari_d4_filtration.npz')
S=np.load(ROOT/'ferrari_d4_controlled_seed.npz')['seed_blocks']
T,Ti=F['basis'],F['basis_inverse'];bd,hd=F['boundary_dimensions'],F['homology_dimensions']
a,b,c=list(zip(D['generator_permutations'],D['generator_blocks']))
X=list(zip(D['X_permutations'],D['X_blocks']))
rotation=prod(a,b,c)
assert eq(prod(rotation,X[0],inv(rotation)),X[1])
assert eq(prod(rotation,X[1],inv(rotation)),X[2])
reports=[]
for row,(i,j) in enumerate(((2,3),(4,0),(1,2),(3,4),(0,1))):
    for core in range(6):
        s=S[6*row+core];adapted=mm(Ti,mm(s,T));counts={}
        for ch in range(N):
            b,h=int(bd[ch]),int(hd[ch]);m=adapted[ch]
            assert not np.any(m[b:,:b]) and not np.any(m[h:,:h])
            assert np.array_equal(m[:b,:b],np.eye(b,dtype=np.int16))
            assert np.array_equal(m[h:,h:],np.eye(5-h,dtype=np.int16))
            if np.any(m[b:h,b:h]!=np.eye(h-b,dtype=np.int16)):
                label=('primitive' if np.any(characters[ch]%2) else 'old')+str(h-b)
                counts[label]=counts.get(label,0)+1
        if row in (0,1,3):assert np.array_equal(s,IM)
        else:assert counts=={'old2':1,'primitive3':48}
        reports.append({'pair':[i+1,j+1],'core':core,
                        'boundary_and_augmentation_identity':True,
                        'active_proper_counts':counts})
classification=json.loads((ROOT/'d4_proper_seed_classification.json').read_text())
simple=json.loads((ROOT/'d4_proper_simple_conjugacies.json').read_text())
assert len(classification)==40 and len(simple['conjugacies'])==40
assert all(r['normal_image_order']==6048 and r['perfect'] for r in classification)
assert all(r['simple'] and r['all_conjugated_generators_in_reference_simple_group'] for r in simple['conjugacies'])
assert sum(r['orbit_size']==8 for r in classification)==32
assert sum(r['orbit_size']==16 for r in classification)==8
out={'all30_full_chain_seed_checks':reports,
 'harmonic_pair_conjugacy_by_abc':True,
 'active_primitive_proper_character_orbits':40,
 'size8_orbits':32,'size16_orbits':8,'total_transported_primitive_support':384,
 'every_active_proper_normal_image_is_certified_centreless_simple6048':True,
 'finite_group_conclusion':'The simultaneous primitive chain image of the B-normal source closure of S is a finite3-extension of a subdirect product of centreless nonabelian simple groups. Its abelianization is a3-group, hence it has noC2 quotient.',
 'actual_source_conclusion':'Goursat gives an actual A in that source normal closure, with all primitive chain images1 and q12(A)=5I. It preserves every previously retained source core.',
 'scope':'The finite group conclusion is a structural proof from these hypotheses. No assignment of independent pentagon factors is used.'}
(ROOT/'d4_global_correction_inputs.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
