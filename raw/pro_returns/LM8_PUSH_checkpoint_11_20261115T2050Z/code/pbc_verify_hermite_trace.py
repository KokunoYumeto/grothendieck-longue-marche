"""Independently verify an exact original-tail integer certificate.

This checks the proof DAG over Z, without reusing GAP's Hermite reduction.
It does not by itself verify the source group identities labelling the
leaf rows; those must be replayed separately in the original presentation.
"""
from collections import defaultdict
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.set_int_max_str_digits(0)
parser = argparse.ArgumentParser()
parser.add_argument("trace", type=Path)
parser.add_argument("--s-count", type=int, required=True)
parser.add_argument("--out", type=Path, required=True)
args = parser.parse_args()

nodes = [None]
source = None
success = None
with args.trace.open() as stream:
    for lineno, line in enumerate(stream, 1):
        row = json.loads(line)
        if row[0] == "source":
            assert source is None and len(nodes) == 1
            source = row
        elif row[0] in {"leaf", "sub", "neg"}:
            assert row[1] == len(nodes), (lineno, row[1], len(nodes))
            if row[0] == "leaf":
                vector = row[4]
                assert len(vector) % 2 == 0
                assert vector[::2] == sorted(set(vector[::2]))
                assert all(1 <= i <= source[3] for i in vector[::2])
                assert all(isinstance(c, int) and c != 0 for c in vector[1::2])
            elif row[0] == "sub":
                assert 1 <= row[2] < row[1] and 1 <= row[4] < row[1]
                assert isinstance(row[3], int)
            else:
                assert 1 <= row[2] < row[1]
            nodes.append(row)
        elif row[0] == "success":
            assert success is None
            success = row
        else:
            raise AssertionError(f"not a completed success trace: {row[0]}")

assert source is not None and success is not None
assert 1 <= success[1] < len(nodes)
coefficients = defaultdict(int)
coefficients[success[1]] = 1
leaf_coefficients = {}
for node_id in range(len(nodes) - 1, 0, -1):
    coefficient = coefficients.pop(node_id, 0)
    if coefficient == 0:
        continue
    row = nodes[node_id]
    if row[0] == "sub":
        coefficients[row[2]] += coefficient
        coefficients[row[4]] -= coefficient * row[3]
    elif row[0] == "neg":
        coefficients[row[2]] -= coefficient
    else:
        leaf_coefficients[node_id] = coefficient
assert not coefficients

total = defaultdict(int)
target_coefficient = 0
extra_coefficients = defaultdict(int)
identities = []
for node_id, coefficient in sorted(leaf_coefficients.items()):
    row = nodes[node_id]
    vector = row[4]
    for index, value in zip(vector[::2], vector[1::2]):
        total[index] += coefficient * value
    if row[2] == "target":
        target_coefficient += coefficient
    elif row[2] == "extra":
        extra_coefficients[row[3][0]] += coefficient
    elif row[2] == "identity":
        identities.append([node_id, coefficient, row[3]])
    else:
        raise AssertionError(row[2])
assert target_coefficient == 1
assert all(value == 0 for value in total.values())

returned = success[2]
for i, value in enumerate(returned, 1):
    coefficient = extra_coefficients[i]
    if i <= 2:
        assert coefficient == value
    elif i <= args.s_count + 2:
        assert (coefficient - value) % 2 == 0
    else:
        assert (coefficient - value) % 3 == 0

certificate = {
    "verified_original_integer_identity": True,
    "source_header": source,
    "trace_sha256": hashlib.sha256(args.trace.read_bytes()).hexdigest(),
    "dag_nodes": len(nodes) - 1,
    "nonzero_leaf_coefficients": [[i, c] for i, c in sorted(leaf_coefficients.items())],
    "used_source_identities": identities,
    "target_coefficient": target_coefficient,
    "extra_coefficients_over_Z": [extra_coefficients[i] for i in range(1, len(returned) + 1)],
    "returned_boundary_coefficients": returned,
    "label_reduction_verified": True,
    "source_identity_replay_still_required": True,
}
args.out.write_text(json.dumps(certificate, indent=2) + "\n")
print(json.dumps({
    "verified_original_integer_identity": True,
    "dag_nodes": certificate["dag_nodes"],
    "used_leaf_rows": len(leaf_coefficients),
    "used_source_identities": len(identities),
    "maximum_coefficient_digits": max(len(str(abs(c))) for c in leaf_coefficients.values()),
    "target_coefficient": target_coefficient,
    "label_reduction_verified": True,
    "source_identity_replay_still_required": True,
}, indent=2))
