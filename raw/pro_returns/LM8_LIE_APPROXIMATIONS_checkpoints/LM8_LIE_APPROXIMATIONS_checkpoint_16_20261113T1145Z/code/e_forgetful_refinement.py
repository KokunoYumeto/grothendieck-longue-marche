#!/usr/bin/env python3
"""All deletion-after-cabling maps and projected full-GT shadows <=1000.

This implements the proved construction K°=(K∩PB3)∩ker(link mod N_ord).
The declared arity-four target is N4=intersection d_i^{-1}(K∩PB3).
Its induced arity-three kernel is K°. All associator commutator residues
and friendly m residues agree with those of the original quotient. The
pentagon is checked formally in all four forgetful coordinates. Thus
all the recorded arity-three pairs are projections of actual charming
full-GT finite shadows for these explicit targets; genuineness remains
separate. The refined B3 quotient can be MUCH larger than1000.
"""
from pathlib import Path
from math import gcd,lcm
import json
base=Path(__file__).resolve().parent
# Domain generator order X=x12,Y=x23,Z=x13; five DLL cablings.
phis=[('123',(((1,2),),((2,3),),((1,3),))),
      ('12,3,4',(((1,3),(2,3)),((3,4),),((1,4),(2,4)))),
      ('1,23,4',(((1,2),(1,3)),((2,4),(3,4)),((1,4),))),
      ('1,2,34',(((1,2),),((2,3),(2,4)),((1,3),(1,4)))),
      ('234',(((2,3),),((3,4),),((2,4),)))]
name={(1,2):'X',(2,3):'Y',(1,3):'Z'}
records=[];comm_images=[]
for deleted in range(1,5):
    images_f=[]
    for phiname,images in phis:
        composite=[]
        for word in images:
            out=[]
            for i,j in word:
                if deleted in (i,j):continue
                pair=(i-(i>deleted),j-(j>deleted));out.append(name[pair])
            composite.append(''.join(out) or '1')
        if composite==['X','Y','Z']:
            kind='identity';fimage='f'
        else:
            nontrivial=[w for w in composite if w!='1']
            assert len(nontrivial)==1 and nontrivial[0] in ('X','Y','XZ','ZY')
            kind='one_linking_coordinate_into_cyclic_subgroup';fimage='1'
        records.append({'deleted_strand':deleted,'cabling':phiname,'images_X_Y_Z':composite,'kind':kind})
        images_f.append(fimage)
    left=[images_f[k] for k in (4,2,0) if images_f[k]!='1']
    right=[images_f[k] for k in (3,1) if images_f[k]!='1']
    assert left==right==['f']
    comm_images.append({'deleted_strand':deleted,'five_cabling_images_of_f':images_f,'pentagon_left':'f','pentagon_right':'f'})
qrows=json.loads((base/'e_b3_quotients_complete.json').read_text())['quotients']
audit=json.loads((base/'e_b3_hexagons.json').read_text())['rows']
rows=[]
for ordinal,(q,r) in enumerate(zip(qrows,audit),1):
    assert r['kernel']==ordinal
    if r['cyclic']:
        n=q['index'];N=n//gcd(n,2);derived=1;count=r['number_of_genuine_power_actions']
    else:N=r['N_ord'];derived=r['derived_order'];count=r['surjective_arity_three_pair_count']
    order=6*derived*N**3
    pure_cover=6*q['pure_image_order']
    assert pure_cover%q['index']==0 and pure_cover<=6*q['index']
    assert order%pure_cover==0
    rows.append({'original_kernel':ordinal,'original_B3_quotient_order':q['index'],
                 'pure_kernel_cover_B3_order':pure_cover,'N_ord':N,
                 'refined_B3_quotient_order':order,
                 'refined_PB3_derived_order':derived,
                 'target_PB4_quotient_order_upper_bound':q['pure_image_order']**4,
                 'all_charming_full_GT_shadows_for_declared_target':count,
                 'original_kernel_is_induced_arity_three_kernel':order==q['index'],
                 'refined_B3_quotient_still_at_most1000':order<=1000})
summary={'original_quotients':len(rows),'total_projected_charming_shadow_pairs':sum(r['all_charming_full_GT_shadows_for_declared_target'] for r in rows),
         'targets_with_unchanged_B3_kernel':sum(r['original_kernel_is_induced_arity_three_kernel'] for r in rows),
         'original_quotients_whose_refinement_still_has_order_at_most1000':sum(r['refined_B3_quotient_still_at_most1000'] for r in rows),
         'maximum_refined_B3_quotient_order':max(r['refined_B3_quotient_order'] for r in rows),
         'pentagon_coordinates_formally_verified':4,'deletion_cabling_composites_verified':20}
assert summary['original_quotients']==1946 and summary['targets_with_unchanged_B3_kernel']==8
out={'scope':'Exhaustive projected-shadow convention for all original B3 quotients of order<=1000. Shadows live on explicitly declared arity-four targets; their induced arity-three kernels are K°, possibly strict refinements. No universal genuineness inference.',
     'construction':'K°=(K∩PB3)∩ker(PB3→(Z/N_ord)^3); N4=intersection of four forgetful preimages of K∩PB3.',
     'composites':records,'pentagon':comm_images,'summary':summary,'rows':rows}
(base/'e_forgetful_refinement.json').write_text(json.dumps(out,indent=2)+'\n')
print(summary)
