#!/usr/bin/env python3
"""Exact order consequences of the proved common central-cover target maps."""
from pathlib import Path
from hashlib import sha256
import json
import math

HERE = Path(__file__).resolve().parent


def value(factors):
    return math.prod(int(p) ** int(e) for p, e in factors.items())


def main():
    names = ['e_a6_double_target_certificate_root.json',
             'de_a6_triple_target_certificate.json',
             'de_a6_triple_target_quotient.json',
             'e_a6_double_target_quotient_root.json']
    hashes = {name: sha256((HERE / name).read_bytes()).hexdigest() for name in names}
    double, triple, q3, q2 = [json.loads((HERE / name).read_text()) for name in names]
    for record in (double, triple):
        assert record['full_kernel_including_perfect_free_factors_is_perfect']
        assert value(record['actual_full_joint_target_factorization']) == int(record['actual_full_joint_target_order'])
    k2 = int(double['full_target_kernel_over_old_A6_signed_target_order'])
    k3 = int(triple['full_target_kernel_over_old_A6_signed_target_order'])
    assert k2 == 2**151 and k3 == 8 * 3**108
    old2, rem2 = divmod(int(double['actual_full_joint_target_order']), k2)
    old3, rem3 = divmod(int(triple['actual_full_joint_target_order']), k3)
    assert rem2 == rem3 == 0 and old2 == old3
    assert q3['small_complete_derived_orders'] == [20736, 3456, 288, 9, 1]
    assert q3['signed_order'] == 96 and q3['affine_three_order'] == 216
    # The full literal S_L Cayley calculation retained in the double target
    # has order96 and derived order48; together with the proved direct
    # product Sigma this determines the affine abelianization exactly.
    assert double['specified_solvable_quotient_order'] == 96
    assert triple['specified_solvable_quotient_order'] == 20736
    affine_derived = q3['small_complete_derived_orders'][1] // 48
    assert affine_derived == 72 and 216 // affine_derived == 3
    assert k3 // 216 == 3**105 and k3 % 216 == 0
    factors = dict(triple['actual_full_joint_target_factorization'])
    factors['2'] += 151
    total = int(triple['actual_full_joint_target_order']) * k2
    assert value(factors) == total
    assert factors == {'2': 557, '3': 271, '5': 117, '7': 8, '11': 3, '13': 2}
    result = {'status': 'PASS_EXACT_JOINT_CENTRAL_COVER_TARGET_ORDERS',
              'old_target_order': str(old2),
              'double_relative_kernel_order': str(k2),
              'triple_relative_kernel_order': str(k3),
              'triple_kernel_affine_three_projection_order': 216,
              'triple_kernel_affine_three_projection_kernel_order': str(3**105),
              'affine_three_abelianization_order': 3,
              'actual_joint_target_order': str(total),
              'actual_joint_target_factorization': factors,
              'specified_solvable_quotient_order': 20736,
              'proof': 'sections/E_a6_double_triple_target_root.tex',
              'input_sha256': hashes}
    assert all(sha256((HERE / name).read_bytes()).hexdigest() == h for name, h in hashes.items())
    (HERE / 'e_a6_double_triple_target_root.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
