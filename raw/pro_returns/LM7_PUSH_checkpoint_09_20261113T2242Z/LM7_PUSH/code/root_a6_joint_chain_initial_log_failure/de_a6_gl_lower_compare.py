#!/usr/bin/env python3
"""Exact source comparison retaining both lower/full A6 projection maps."""
from pathlib import Path
import json
from hashlib import sha256

HERE=Path(__file__).resolve().parent
def last(n):return json.loads((HERE/n).read_text().splitlines()[-1])
lower=json.loads((HERE/'de_ferrari_a6_perm_source.json').read_text())['source_image_order']
ga=json.loads((HERE/'de_ferrari_a5_source.json').read_text())['induced_B_image_order']
gl=json.loads((HERE/'de_ferrari_sl2_5_source.json').read_text())['lifted_group_order']
full=int(last('de_a6_schreier_full_ordered.out')['order'])
base=int(last('de_a6_gl_lower_chain.out')['order'])
small=json.loads((HERE/'de_a6_gl_lower_kernel.json').read_text())
large=json.loads((HERE/'de_a6_gl_kernel_replay.json').read_text())
assert small['all_Schreier_relators_evaluated'] and small['kernel_dimension']==42
lower_joint=base*2**small['kernel_dimension']
assert lower*ga%base==0 and lower*gl%lower_joint==0
common_base=lower*ga//base;common_signed=lower*gl//lower_joint
assert common_base==1350 and common_signed==5400
full_joint=large['full_joint_source_order'];fiber_order=full*lower_joint//lower
assert fiber_order%full_joint==0
out={'status':'PASS_EXACT_LOWER_FULL_COMPARISON',
     'lower_A6_A5_common_order':common_base,
     'lower_A6_GL_common_order':common_signed,
     'full_A6_GL_common_order':large['maximum_common_G6_GL_quotient_order'],
     'actual_full_joint_index_in_lower_fiber_product':fiber_order//full_joint,
     'source_morphism':'(rho_A6,rho_L)(B) -> G_A6 x_(G_A6_lower) (rho_A6_lower,rho_L)(B), induced by the literal full-to-kernel-permutation projection',
     'full_common_quotient_factors_through_lower_A6':fiber_order==full_joint,
     'remaining_common_component_order':fiber_order//full_joint,
     'no_structure_assigned_by_order_alone':True,
     'lower_complete_kernel_relations':small['complete_base_relator_count']}
assert out['remaining_common_component_order']==216000
(HERE/'de_a6_gl_lower_compare.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
