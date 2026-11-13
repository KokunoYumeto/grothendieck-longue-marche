#!/usr/bin/env python3
"""Literal mutual word maps for the two variable derived-generator lists.

The source s,r,x,y actions and every point map are compared entry by entry.
Only SymPy's returned generators for the same embedded derived subgroup
vary. Every generator in each saved list is explicitly expressed as a
signed word in the other list, and replayed with independent NumPy arrays.
"""
from pathlib import Path
from hashlib import sha256
import inspect
import json
import time
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup

HERE = Path(__file__).resolve().parent
REPLAY = HERE / 'root_a6_joint_quotient_replay'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def words_in(targets, generators):
    group = PermutationGroup([Permutation(p.tolist()) for p in generators])
    group.schreier_sims()
    letters = {}
    for i, row in enumerate(generators, 1):
        letters.setdefault(tuple(row), i)
        letters.setdefault(tuple(np.argsort(row)), -i)
    inverse = np.argsort(generators, axis=1)
    result = []
    for target in targets:
        p = Permutation(target.tolist())
        assert group.contains(p)
        factors = group.generator_product(p, original=True)
        # SymPy documents g = s_n * ... * s_1.  Reverse that list
        # to record our left-to-right right-permutation word convention.
        word = [letters[tuple(q.array_form)] for q in reversed(factors)]
        value = np.arange(len(target), dtype=np.int64)
        for letter in word:
            row = generators[letter - 1] if letter > 0 else inverse[-letter - 1]
            value = row[value]
        assert np.array_equal(value, target), ('literal word replay', word)
        result.append(word)
    return result


def main():
    started = time.time()
    name = 'de_a6_gl_common_quotient.npz'
    old_path, new_path = HERE / name, REPLAY / name
    protected = {str(p): digest(p) for p in (old_path, new_path)}
    variants = {'m15_Fprime_generators', 'm30_Fprime_generators'}
    rows = []
    with np.load(old_path) as a, np.load(new_path) as b:
        assert set(a.files) == set(b.files)
        literal = []
        for key in a.files:
            if key not in variants:
                assert np.array_equal(a[key], b[key]), key
                literal.append(key)
                continue
            old, new = a[key], b[key]
            assert old.ndim == new.ndim == 2 and old.shape[1] == new.shape[1]
            identity = np.arange(old.shape[1])
            assert all(np.array_equal(np.sort(row), identity) for row in [*old, *new])
            for values in (old, new):
                assert np.all(values[:, 30:] == identity[30:])
            old_in_new = words_in(old, new)
            new_in_old = words_in(new, old)
            rows.append({
                'array': key,
                'ambient_degree': int(old.shape[1]),
                'old_generators': old.tolist(),
                'replayed_generators': new.tolist(),
                'old_generators_as_signed_words_in_replayed': old_in_new,
                'replayed_generators_as_signed_words_in_old': new_in_old,
                'word_convention': 'one-based signed indices; p*q=q[p]; read words left to right',
                'comparison_morphism': 'identity permutation map on the same labelled ambient points',
                'mutual_literal_generator_word_replays_passed': True,
                'both_induced_homomorphisms_are_inverse_identity_maps': True,
            })
    assert {row['array'] for row in rows} == variants
    source = inspect.getsource(PermutationGroup.normal_closure)
    assert 'random' in source
    assert all(digest(Path(path)) == value for path, value in protected.items())
    result = {'all_passed': True, 'literal_arrays': sorted(literal),
              'exact_identity_morphisms': rows,
              'installed_derived_subgroup_implementation': inspect.getsource(PermutationGroup.derived_subgroup),
              'installed_normal_closure_implementation': source,
              'original_and_replayed_inputs_unchanged': True,
              'protected_sha256': protected, 'seconds': round(time.time() - started, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'all_passed': True, 'literal_array_count': len(literal),
                      'identity_morphisms': [{k: v for k, v in row.items()
                                             if k not in ('old_generators', 'replayed_generators')}
                                            for row in rows],
                      'seconds': result['seconds']}, indent=2))


if __name__ == '__main__':
    main()
