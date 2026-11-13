#!/usr/bin/env python3
"""Resolve equivalent permutation generating sets by their exact identity map.

The preceding replay's final byte-array guard rejected different terminal
derived generating sets.  This program verifies both subgroup inclusions
inside the same Sym(251), preserving the actual quotient generators and
Cayley table.  It also separates a concurrently written exploratory stdout
file from the protected mathematical inputs and certificates.
"""
from pathlib import Path
import json
import time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
from audit_sl2_source_root import digest, mathematical

HERE = Path(__file__).resolve().parent
REPLAY = HERE/'root_e24_binary_replay'
EXPECTED = REPLAY/'expected_sl2'


def main():
    begin = time.time()
    prior = json.loads((HERE/'audit_sl2_source_root.json').read_text())
    assert len(prior['programs']) == 6
    assert all(r['exit_code'] == 0 and r['json_mathematical_equal'] for r in prior['programs'])
    assert all(r['all_artifacts_equal'] for r in prior['programs'][:-1])
    assert prior['programs'][-1]['program'] == 'de_ferrari_sl2_5_solvable.py'
    with np.load(EXPECTED/'de_ferrari_sl2_5_solvable.npz') as a, np.load(REPLAY/'de_ferrari_sl2_5_solvable.npz') as b:
        assert set(a.files) == set(b.files)
        assert all(np.array_equal(a[k],b[k]) for k in ('a','b','c'))
        ga = [Permutation(p.tolist()) for p in a['terminal_perfect_generators']]
        gb = [Permutation(p.tolist()) for p in b['terminal_perfect_generators']]
    A, B = PermutationGroup(ga), PermutationGroup(gb)
    assert all(A.contains(g) for g in gb)
    assert all(B.contains(g) for g in ga)
    oa, ob = int(A.order()), int(B.order())
    expected = json.loads((EXPECTED/'de_ferrari_sl2_5_solvable.json').read_text())
    assert oa == ob == expected['complete_derived_orders'][-1]
    current = json.loads((REPLAY/'de_ferrari_sl2_5_solvable.json').read_text())
    assert mathematical(current) == mathematical(expected)
    changed = [n for n,h in prior['protected_sha256'].items() if digest(HERE/n) != h]
    assert changed == ['de_ferrari_sl2_5_derived_replay.out'], changed
    stable = {n:h for n,h in prior['protected_sha256'].items() if n not in changed}
    assert all(digest(HERE/n) == h for n,h in stable.items())
    result = {'all_passed': True, 'original_artifacts_unchanged': True,
              'scope_of_original_guard': 'All original mathematical programs and certificates; the separately running exploratory replay stdout is excluded and explicitly recorded.',
              'prior_attempt': 'audit_sl2_source_root.json',
              'retained_prior_guard_failure': True,
              'identity_permutation_map_compares_both_terminal_subgroups': True,
              'terminal_subgroup_order': oa,
              'original_generator_count': len(ga), 'replay_generator_count': len(gb),
              'both_subgroup_inclusions_verified': True,
              'actual_braid_generator_permutations_identical': True,
              'complete_solvable_quotient_Cayley_table_identical': True,
              'all_six_mathematical_programs_passed': True,
              'concurrently_written_stdout': changed,
              'protected_sha256': stable,
              'elapsed_seconds': round(time.time()-begin,3)}
    (HERE/'audit_sl2_source_resolution_root.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k != 'protected_sha256'},indent=2),flush=True)
    print('ROOT_SL2_FERRARI_SOURCE_EXACT_PERMUTATION_COMPARISON_PASS',flush=True)


if __name__ == '__main__':
    main()
