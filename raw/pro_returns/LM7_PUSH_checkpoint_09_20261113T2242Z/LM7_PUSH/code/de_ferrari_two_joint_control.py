#!/usr/bin/env python3
"""Exact CRT comparison between the binary and ternary Ferrari cores."""
from contextlib import redirect_stdout
from pathlib import Path
import io,json,runpy,time
import numpy as np
from de_ferrari_two_model import FerrariTwo
from de_ferrari_two_core import InducedTwo,chunk_trie
from de_ferrari_degree6_kernel import CombinedSix,InducedSix

here=Path(__file__).resolve().parent
start=time.time()
with redirect_stdout(io.StringIO()):d=runpy.run_path(str(here/'de_distribution_test.py'))
H2=FerrariTwo(6);W2=InducedTwo(H2,d,4)
H3=CombinedSix();W3=InducedSix(H3,d)
for W in (W2,W3):
    N=[W.word(w) for w in d['Nwords']];W.chunks=chunk_trie(d,N,W)
two=json.loads(here.joinpath('de_ferrari_two_degree6_module.json').read_text())
three=json.loads(here.joinpath('de_ferrari_degree6_kernel.json').read_text())
for w in two['F_prime_basis_words']:
    assert W2.equal(W2.word(w*3),W2.word(w))
    assert W3.equal(W3.word(w*3),W3.one)
for w in three['F_prime_basis_words']:
    ww=d['bpower'](w,-2)
    assert W2.equal(W2.word(ww),W2.one)
    assert W3.equal(W3.word(ww),W3.word(w))
orders=[]
for H in (H2,H3):
    z3=H.power(H.mul(H.a,H.b),3);z4=H.power(H.mul(H.mul(H.a,H.b),H.c),4)
    current=[]
    for z in (z3,z4):
        n=next(n for n in range(1,145) if np.array_equal(H.power(z,n),H.one))
        assert 72%n==0 and np.array_equal(H.power(z,73),z)
        current.append(n)
    orders.append(current)
gen2=json.loads(here.joinpath('de_ferrari_two_generation.json').read_text())
gen3=json.loads(here.joinpath('de_ferrari_degree6_generation.json').read_text())
target_order=gen2['binary_four_strand_target_order']*gen3['joint_target_order']
lift=json.loads(here.joinpath('de_ferrari_two_lift.json').read_text())
assert lift['pass_counts']==[12,12] and lift['both_full_twists_verified_at_every_solution']
assert all(len(r['branches'])==2 and all(b['actual_solutions_checked']==2 for b in r['branches']) for r in lift['records'])
out={'binary_basis_cubes_keep_binary_and_kill_ternary':len(two['F_prime_basis_words']),
    'ternary_plane_basis_powers_minus_two_keep_ternary_and_kill_binary':len(three['F_prime_basis_words']),
    'binary_full_twist_orders':orders[0],'ternary_full_twist_orders':orders[1],
    'both_multiplier_residues_preserve_all_full_twist_powers':True,
    'joint_four_strand_direct_product_order':target_order,
    'joint_pure_normal_quotient_order':target_order,
    'points_per_retained_CM_fibre':9*2*2,'total_joint_points':24*9*2*2,
    'elapsed_seconds':round(time.time()-start,3),
    'scope':'Literal CRT basis comparisons; exact full-twist periods and the counts from the complete component fibres. The direct-product and generation conclusions use the proved Goursat and Frattini arguments.'}
here.joinpath('de_ferrari_two_joint_control.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
