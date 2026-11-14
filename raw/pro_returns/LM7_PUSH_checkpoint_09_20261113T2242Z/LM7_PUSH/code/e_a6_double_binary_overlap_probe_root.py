#!/usr/bin/env python3
"""Exact binary coinvariants of the retained stable A6 source quotient."""
from pathlib import Path
from hashlib import sha256
import json
import time
import numpy as np
from de_ferrari_a6_solvable import EGroup
from de_ferrari_two_core import rref2

HERE = Path(__file__).resolve().parent
STEM = 'e_a6_double_binary_overlap_probe_root'


def main():
    started = time.monotonic()
    names = ['de_a6_binary_module.json', 'de_a6_module.json',
             'de_ferrari_a6_metafibres.npz', 'de_ferrari_a6_solvable.py',
             'e_a6_double_commutator_replay_root.npz']
    hashes = {n: sha256((HERE / n).read_bytes()).hexdigest() for n in names}
    E = EGroup()
    V = np.load(HERE / 'de_ferrari_a6_metafibres.npz')['complete_correction_basis']
    assert V.shape == (9, 6)
    actions = []
    for v in V.T:
        code = int(v @ E.weights)
        columns = []
        for j in range(6):
            value = int(E.plus[code, 1 << j])
            columns.append([(value >> i) & 1 for i in range(6)])
        actions.append(np.array(columns, dtype=np.int64).T)
    matrix = np.concatenate([a ^ np.eye(6, dtype=np.int64) for a in actions], axis=1)
    rank = len(rref2(matrix)[1])
    pairing = np.load(HERE / 'e_a6_double_commutator_replay_root.npz')['alternating_pairing']
    pairing_rank = len(rref2(pairing.reshape(3, -1))[1])
    np.savez_compressed(HERE / (STEM + '.npz'),
                        stable_ternary_basis=V, binary_conjugation_actions=np.array(actions),
                        binary_commutator_matrix=matrix, binary_central_pairing=pairing)
    result = {'status': 'PASS_LITERAL_STABLE_BINARY_ACTION_COMPUTATION',
              'actual_stable_ternary_dimension': 6,
              'old_binary_module_dimension': 6,
              'stable_ternary_commutator_rank_on_binary_module': rank,
              'new_binary_central_commutator_rank': pairing_rank,
              'scope': 'Actual matrices and their ranks only; the comparison proof is separate.',
              'input_sha256': hashes,
              'seconds': round(time.monotonic() - started, 6)}
    (HERE / (STEM + '.json')).write_text(json.dumps(result, indent=2) + '\n')
    assert all(sha256((HERE / n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
