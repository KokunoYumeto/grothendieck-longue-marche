#!/usr/bin/env python3
"""Independent literal-input audit of the prescribed D-source free pair.

This reads the two original CE certificates, not A's target or evaluator.
The integer character check proves the omission for the whole signed/deck
orbit; the two raw defects are then projected without a class-two oracle.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
paths = [ROOT / 'work_CE/next_symmetric_nodes/family_kernel_schreier25.json',
         ROOT / 'work_CE/next_symmetric_nodes/annular_two_operator25.json']
F, S = [json.loads(p.read_text()) for p in paths]

def red(word):
    out = []
    for a in word:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return out

def inv(word):
    return [-a for a in reversed(word)]

def mul(*words):
    return red(a for word in words for a in word)

def sub(word, images):
    return mul(*(images[str(abs(a))] if a > 0 else inv(images[str(-a)])
                 for a in word))

def chi(word):
    return (sum((1 if a > 0 else -1) for a in word if abs(a) in (1, 2)),
            sum((1 if a > 0 else -1) for a in word if abs(a) == 3))

characters = {}
for name, op in F['all_four_signed_source_operators'].items():
    retained = [op['retained_images'][str(i)]['retained_head'] for i in (5, 10, 11)]
    assert [chi(w) for w in retained] == [(1, 0), (1, 0), (0, 1)]
    heads = []
    for key, row in op['family_images'].items():
        assert row['signed_core'] == int(key)
        heads.append(chi(row['retained_head']))
    expected = (0, 0) if name.startswith('m') else ((-1, 0) if name == 'v' else (1, 0))
    assert set(heads) == {expected}
    characters[name] = {'retained_character_images': [chi(w) for w in retained],
                        'common_family_head_character': expected}
print('All four signed retained operators preserve (chi_sum,chi_x).')
print('All32 family heads have their asserted common character shifts.')

relevant = []
for row in F['all40_node_factor_pairs']:
    a, b = row['first_factor'], row['second_factor']
    if {abs(a['signed_core']), abs(b['signed_core'])} != {2, 8}:
        continue
    if abs(a['signed_core']) == 8:
        a, b = b, a
    ca, cb = chi(a['retained_head']), chi(b['retained_head'])
    difference = tuple(u-v for u, v in zip(ca, cb))
    assert difference[0] % 2 == 1
    relevant.append({'side': row['side'], 'name': row['name'], 'sheet': row['sheet'],
                     'B_character': ca, 'bar_d_character': cb, 'difference': difference})
assert len(relevant) == 2
assert [r['difference'][0] for r in relevant] == [-1, 1]
print('Exactly two B/bar_d seeds; chi_sum differences -1,+1 are odd.')

retained_indices = {5: 0, 10: 1, 11: 2}
def project(word):
    """Free fiber of F64 semidirect (C2)^3, followed by its free retraction."""
    residue = [0, 0, 0]
    out = []
    for a in word:
        if abs(a) in retained_indices:
            residue[retained_indices[abs(a)]] ^= 1
        elif abs(a) == 2 and residue == [0, 0, 0]:
            out.append(1 if a > 0 else -1)
        elif abs(a) == 8 and residue == [0, 0, 1]:
            out.append(2 if a > 0 else -2)
    assert residue == [0, 0, 0]
    return red(out)

def matrix(word):
    # Multiply the actual three-by-three binary matrices independently.
    identity = [[1,0,0],[0,1,0],[0,0,1]]
    X = [[1,1,0],[0,1,0],[0,0,1]]
    Y = [[1,0,0],[0,1,1],[0,0,1]]
    out = identity
    for a in word:
        q = X if abs(a) == 1 else Y  # X and Y are involutions.
        out = [[sum(out[i][k]*q[k][j] for k in range(3)) % 2
                for j in range(3)] for i in range(3)]
    return out

sources = [r['fiber11'] for r in S['actual_six_source_normal_forms'][:4]]
Ds = mul(sources[1], sources[0], inv(sources[2]), inv(sources[0]), inv(sources[1]))
Us = mul(sources[0], inv(sources[3]), inv(sources[0]))
results = []
for name in ('m', 'm_inverse'):
    images = S['source_ordinary_actions'][name]
    Ddefect = mul(sub(Ds, images), inv(Ds))
    Udefect = mul(sub(Us, images), inv(Us))
    projected = project(Ddefect)
    assert projected == [2, -1, -2, 1]
    assert matrix(projected) == [[1,0,1],[0,1,0],[0,0,1]]
    assert project(Udefect) == []
    results.append({'operator': name, 'defect_length': len(Ddefect),
                    'projected_D_defect': projected, 'projected_U_defect': [],
                    'UT3_matrix': matrix(projected), 'literal_D_defect_F11': Ddefect})
    print(name, 'D defect length', len(Ddefect), 'free image', projected,
          'UT3 central entry 1; known U control empty.')
assert project([2]) == [1]
assert project([11, 8, -11]) == [2]
print('Literal free-two section B, x bar_d x^-1 PASS.')

out = {'status': 'PASS_INDEPENDENT_LITERAL_AND_UNIFORM_CHARACTER_AUDIT',
       'inputs': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in paths},
       'signed_character_data': characters, 'all_relevant_color_pairs': relevant,
       'selected_residues': {'B': [0,0,0], 'bar_d': [0,0,1]},
       'results': results, 'section_F11': [[2], [11,8,-11]],
       'scope': 'The integer pair-difference argument includes every signed source/deck translate. The free-two projection is not asserted source-equivariant. Compact descent is proved separately using the actual finite-index retained cover.'}
(ROOT / 'work_CE/next_symmetric_nodes/review_D_source_free_pair26.json').write_text(
    json.dumps(out, indent=2) + '\n')
