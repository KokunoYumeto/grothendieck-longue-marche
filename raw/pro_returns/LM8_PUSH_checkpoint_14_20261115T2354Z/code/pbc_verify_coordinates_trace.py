#!/usr/bin/env python3
"""Independently expand the modular source-row proof DAG.

The exact sum is reduced by explicitly derived original diagonal power
identities, then checked coordinatewise to be a multiple of |G|. Genuine source-identity replay is a separate mandatory gate.
"""
from collections import defaultdict
from pbc_source_coordinate_bounds import coordinate_bounds
import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

sys.set_int_max_str_digits(0)
parser = argparse.ArgumentParser()
parser.add_argument('source', type=Path)
parser.add_argument('trace', type=Path)
parser.add_argument('--s-count', type=int, required=True)
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
source_data = json.loads(args.source.read_text())
assert args.s_count == len(source_data['s_centralizers'])
modulus = math.prod(source_data['relative_orders'])
source_hash = hashlib.sha256(args.source.read_bytes()).hexdigest()
coordinate_moduli, all_bound_proofs = coordinate_bounds(source_data)
nodes = [None]
source = success = None
for lineno, line in enumerate(args.trace.open(), 1):
    row = json.loads(line)
    if row[0] == 'source':
        assert source is None and len(nodes) == 1
        source = row
        n = len(source_data['relative_orders'])
        assert row == ['source', source_hash, n, n*(n+1)//2, modulus, coordinate_moduli]
    elif row[0] in ('leaf', 'sub', 'neg', 'mul'):
        assert source is not None and row[1] == len(nodes)
        if row[0] == 'leaf':
            vector = row[4]
            assert len(vector) % 2 == 0
            assert vector[::2] == sorted(set(vector[::2]))
            assert all(1 <= i <= source[3] for i in vector[::2])
            assert all(isinstance(c, int) and c for c in vector[1::2])
            if row[2] == 'modulus':
                assert len(row[3]) == 1 and vector == [row[3][0], modulus]
            elif row[2] == 'coordinate':
                assert len(row[3]) == 1 and row[3][0] in all_bound_proofs
                assert vector == [row[3][0], coordinate_moduli[row[3][0]-1]]
            elif row[2] == 'extra':
                assert row[3][0] >= 3, 'power-word correction is forbidden'
            else:
                assert row[2] in ('target', 'identity')
        elif row[0] == 'sub':
            assert 1 <= row[2] < row[1] and 1 <= row[4] < row[1]
            assert isinstance(row[3], int)
        elif row[0] == 'neg':
            assert 1 <= row[2] < row[1]
        else:
            assert 1 <= row[3] < row[1]
            assert math.gcd(row[2],modulus) == 1
        nodes.append(row)
    elif row[0] == 'success':
        assert success is None
        success = row
    else:
        raise AssertionError(('not a completed success trace', lineno, row[0]))
assert source is not None and success is not None
assert 1 <= success[1] < len(nodes)

coefficients = defaultdict(int)
coefficients[success[1]] = 1
leaves = {}
for node_id in range(len(nodes)-1, 0, -1):
    coefficient = coefficients.pop(node_id, 0) % modulus
    if not coefficient:
        continue
    row = nodes[node_id]
    if row[0] == 'sub':
        coefficients[row[2]] = (coefficients[row[2]] + coefficient) % modulus
        coefficients[row[4]] = (coefficients[row[4]] - coefficient*row[3]) % modulus
    elif row[0] == 'neg':
        coefficients[row[2]] = (coefficients[row[2]] - coefficient) % modulus
    elif row[0] == 'mul':
        coefficients[row[3]] = (coefficients[row[3]] + coefficient*row[2]) % modulus
    else:
        leaves[node_id] = coefficient
assert not coefficients

total = defaultdict(int)
target_coefficient = 0
extra_coefficients = defaultdict(int)
identities = []
source_leaves = []
modulus_leaves = 0
used_bounds = set()
for node_id, coefficient in sorted(leaves.items()):
    row = nodes[node_id]
    for index, value in zip(row[4][::2], row[4][1::2]):
        total[index] += coefficient*value
    if row[2] == 'target':
        target_coefficient += coefficient
        source_leaves.append(node_id)
    elif row[2] == 'extra':
        extra_coefficients[row[3][0]] += coefficient
        source_leaves.append(node_id)
    elif row[2] == 'identity':
        identities.append([node_id, coefficient, row[3]])
        source_leaves.append(node_id)
    elif row[2] == 'coordinate':
        used_bounds.add(row[3][0])
    else:
        assert row[2] == 'modulus'
        modulus_leaves += 1
assert target_coefficient == 1
assert all(value % coordinate_moduli[i-1] == 0 for i,value in total.items())
for i,value in total.items():
    if value and coordinate_moduli[i-1] < modulus:
        used_bounds.add(i)
coordinate_eliminations = [[i,total[i]//coordinate_moduli[i-1]] for i in sorted(used_bounds) if total[i]]
bound_proofs = {i:all_bound_proofs[i] for i in sorted(used_bounds)}
corrected_total = dict(total)
for i,multiple in coordinate_eliminations:
    proof = bound_proofs[i]
    correction = multiple * sum(r['coefficient']*r['value'] for r in proof['rows'])
    assert correction == total[i]
    corrected_total[i] -= correction
assert all(value % modulus == 0 for value in corrected_total.values())
returned = success[2]
assert returned[0:2] == [0, 0]
assert extra_coefficients[1] == extra_coefficients[2] == 0
for i, value in enumerate(returned, 1):
    c = extra_coefficients[i]
    if i <= 2:
        assert c == value == 0
    elif i <= args.s_count+2:
        assert (c-value) % 2 == 0
    else:
        assert (c-value) % 3 == 0

certificate = dict(
    verified_original_modular_identity=True,
    original_integer_residual_divisible_by_modulus=True,
    source_header=source,
    modulus=modulus,
    source_sha256=source_hash,
    trace_sha256=hashlib.sha256(args.trace.read_bytes()).hexdigest(),
    dag_nodes=len(nodes)-1,
    nonzero_leaf_coefficients=[[i,c] for i,c in sorted(leaves.items())],
    used_original_source_leaf_ids=source_leaves,
    used_source_identities=identities,
    used_modulus_leaves=modulus_leaves,
    target_coefficient=target_coefficient,
    forbidden_power_word_coefficients=[0,0],
    extra_coefficients_mod_N=[extra_coefficients[i] % modulus for i in range(1,len(returned)+1)],
    returned_boundary_coefficients=returned,
    integer_modulus_quotient=[[i,v//modulus] for i,v in sorted(corrected_total.items()) if v],
    coordinate_bound_proofs=bound_proofs,
    coordinate_eliminations=coordinate_eliminations,
    coordinate_moduli=coordinate_moduli,
    original_coordinate_power_relations_checked=True,
    label_reduction_verified=True,
    source_identity_replay_still_required=True,
    hopf_torsion_faithfulness_comparison='notes/pbc_C31_modular_gate.md',
)
args.out.write_text(json.dumps(certificate,indent=2)+'\n')
print(json.dumps({k:certificate[k] for k in (
    'verified_original_modular_identity', 'original_integer_residual_divisible_by_modulus',
    'modulus','dag_nodes','used_modulus_leaves','target_coefficient',
    'forbidden_power_word_coefficients','label_reduction_verified',
    'source_identity_replay_still_required')},indent=2))
print('used_original_source_leaves',len(source_leaves))
print('used_source_identities',len(identities))
