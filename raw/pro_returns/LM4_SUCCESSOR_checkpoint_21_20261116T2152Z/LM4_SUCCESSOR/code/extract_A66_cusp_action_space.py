"""Exact quotient of the old affine-choice kernel by zero cusp action.

This is linear algebra on the complete saved 360-column matrix.  It does
not solve any old or new normalizer norm, or assert a full involution.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'records/A66_zero_cusp_action_free_frame_feasibility.json'
raw = source.read_bytes()
data = json.loads(raw)
columns = data['columns']
target = data['target']
assert len(columns) == 360 and data['equations'] == 540
mask = (1 << 108)-1


def linear(values, coefficients):
    out = 0
    for j, value in enumerate(values):
        if (coefficients >> j) & 1:
            out ^= value
    return out


old_pivots = {}
old_kernel = []
for j, full in enumerate(columns):
    value = full & mask
    lift = 1 << j
    while value:
        lead = value.bit_length()-1
        if lead not in old_pivots:
            old_pivots[lead] = value, lift
            break
        p, q = old_pivots[lead]
        value ^= p
        lift ^= q
    if not value:
        old_kernel.append(lift)
assert len(old_pivots) == 83 and len(old_kernel) == 277
assert all(linear(columns, v) & mask == 0 for v in old_kernel)

w_pivots = {}
w_values = []
w_lifts = []
zero_w_kernel = []
for lift in old_kernel:
    value = linear(columns, lift) >> 108
    while value:
        lead = value.bit_length()-1
        if lead not in w_pivots:
            w_pivots[lead] = value, lift
            w_values.append(value)
            w_lifts.append(lift)
            break
        p, q = w_pivots[lead]
        value ^= p
        lift ^= q
    if not value:
        zero_w_kernel.append(lift)
assert len(w_values) == 19 and len(zero_w_kernel) == 258
assert all(linear(columns, v) == 0 for v in zero_w_kernel)
assert all(linear(columns, v) == (w << 108)
           for v, w in zip(w_lifts, w_values))
base = data['solution_mask']
assert linear(columns, base) == target

# Check independence of all277 source directions, not only their images.
source_pivots = {}
for v in w_lifts + zero_w_kernel:
    while v:
        lead = v.bit_length()-1
        if lead not in source_pivots:
            source_pivots[lead] = v
            break
        v ^= source_pivots[lead]
    assert v
assert len(source_pivots) == 277

record = dict(
    scope='All old s-class affine solutions, before old/new normalizer norms.',
    source=str(source.relative_to(ROOT)),
    source_sha256=hashlib.sha256(raw).hexdigest(),
    variables=360, old_class_rank=83, old_homogeneous_dimension=277,
    free_cusp_action_dimension=19, zero_cusp_action_dimension=258,
    zero_action_base_mask=base,
    cusp_action_basis=w_values, cusp_action_lift_masks=w_lifts,
    zero_action_kernel_masks=zero_w_kernel,
    formula='base XOR sum(e_i*W_lift_i) XOR sum(t_j*zero_kernel_j)',
    coefficient_field='F2',
    output_encoding='four rows,36 F8 coordinates each;3 bits per coordinate',
    direct_checks='all277 independent; each19 lift has prescribed W; all258 kernel images zero')
out = ROOT/'records/A66_cusp_action_space.json'
out.write_text(json.dumps(record, indent=2)+'\n')
print('Original affine variables:',360)
print('Old s-class rank:',len(old_pivots))
print('Old homogeneous dimension:',len(old_kernel))
print('Free-cusp W quotient dimension:',len(w_values))
print('Zero-W kernel dimension:',len(zero_w_kernel))
print('All source independence and direct equation checks: PASS')
print('No old or new normalizer norm conclusion.')
