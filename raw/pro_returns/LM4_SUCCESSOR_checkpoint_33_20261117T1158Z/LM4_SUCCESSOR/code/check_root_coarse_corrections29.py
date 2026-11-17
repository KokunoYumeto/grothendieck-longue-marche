"""Exact marked coarse-section corrections in the proved family-kernel module.

This is one fixed-input symbolic calculation. It is not an orbit census,
finite-group search, or solution of the remaining fixed-kernel problem.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    'work_CE/next_symmetric_nodes/annular_two_operator25.json': '9108133f3959df9a53c9b0e5590b4f3ddd1958cff9361d53d86940b8da464e92',
    'work_CE/next_symmetric_nodes/m_star_relative_face27.json': 'ad9d32fdea2a7a830cddd432fbf428ce22b80f4ca18f73e8d7da8335fa030334',
    'work_CE/next_symmetric_nodes/family_kernel_schreier25.json': 'f1f12e21935c05d0c4aa6846624c16a480be55752c5781832c49cb5f2afe1e5e',
}
loaded = []
for rel, digest in INPUTS.items():
    data = (ROOT / rel).read_bytes()
    assert hashlib.sha256(data).hexdigest() == digest
    loaded.append(json.loads(data))
D, LOCAL, PREVIOUS = loaded
FAMILY = {1, 2, 3, 4, 6, 7, 8, 9}
TO_T = {5: 1, 10: 2, 11: 3}
FROM_T = {1: (5,), 2: (10,), 3: (11,)}
CONES = {6, 7}

def reduce_word(word, cones=()):
    out = []
    for letter in word:
        letter = abs(letter) if abs(letter) in cones else letter
        if out and (out[-1] == -letter or letter in cones and out[-1] == letter):
            out.pop()
        else:
            out.append(letter)
    return tuple(out)

def inverse(word, cones=()):
    return reduce_word((-letter for letter in reversed(word)), cones)

def substitute(word, images, cones=()):
    return reduce_word((letter for j in word for letter in
                       (images[j] if j > 0 else inverse(images[-j], cones))), cones)

def ordinary(word):
    state, out = 0, []
    for letter in reduce_word(word, CONES):
        if letter == 6:
            state ^= 1
        elif letter == 7:
            out.append(11 if state == 0 else -11)
            state ^= 1
        else:
            out.append((abs(letter) + 5 * state) * (1 if letter > 0 else -1))
    assert state == 0
    return reduce_word(out)

def schreier(word):
    head, out = (), []
    for letter in word:
        if abs(letter) in FAMILY:
            emitted = (1 if letter > 0 else -1, head, abs(letter))
            if out and out[-1] == (-emitted[0], head, abs(letter)):
                out.pop()
            else:
                out.append(emitted)
        else:
            head = reduce_word((*head, TO_T[abs(letter)] * (1 if letter > 0 else -1)))
    return tuple(out), head

def expand_schreier(word, head=()):
    out = []
    for sign, t, family in word:
        prefix = substitute(t, FROM_T)
        out.extend((*prefix, sign * family, *inverse(prefix)))
    out.extend(substitute(head, FROM_T))
    return reduce_word(out)

L2G = {int(i): tuple(w) for i, w in D['minus_local_to_global'].items()}
G2L = {int(i): tuple(w) for i, w in D['minus_global_to_local'].items()}
assert L2G == {1: (1,), 2: (-1,6,1,2,-1,6,1), 3: (3,), 4: (4,),
               5: (5,), 6: (-1,6,1), 7: (7,)}
for i in range(1, 8):
    assert substitute(L2G[i], G2L, CONES) == (i,)
    assert substitute(G2L[i], L2G, CONES) == (i,)
ordinary_basis = {int(i): tuple(w) for i, w in D['ordinary_fiber11_to_fiber7'].items()}
for i, word in ordinary_basis.items():
    assert ordinary(word) == (i,)
operators = {name: {int(i): tuple(w) for i, w in action.items()}
             for name, action in D['source_ordinary_actions'].items()}
for name, action in operators.items():
    local = {int(i): tuple(w) for i, w in LOCAL['all_four_source_operators_local7'][name].items()}
    for i, word in ordinary_basis.items():
        transported = substitute(substitute(substitute(word, G2L, CONES), local, CONES), L2G, CONES)
        assert ordinary(transported) == action[i], (name, i)
    for i in TO_T:
        emitted, head = schreier(action[i])
        old = PREVIOUS['all_four_signed_source_operators'][name]['retained_images'][str(i)]
        assert json.loads(json.dumps(emitted)) == old['kernel_correction']
        assert list(head) == old['retained_head']
        assert expand_schreier(emitted, head) == action[i]

sections = {
    'old_c_section': {1: (5,), 2: (10,), 3: (11,)},
    'local_C_section': {i: ordinary(substitute(word, L2G, CONES)) for i, word in
                        {1: (5,), 2: (6,5,6), 3: (7,6)}.items()},
}
rows = []
for section_name, section in sections.items():
    for i, word in section.items():
        assert schreier(word)[1] == (i,)
    for operator_name, action in operators.items():
        for i, generator in section.items():
            actual = substitute(generator, action)
            coarse_head = schreier(actual)[1]
            section_lift = substitute(coarse_head, section)
            defect = reduce_word((*actual, *inverse(section_lift)))
            emitted, remainder = schreier(defect)
            assert not remainder
            assert expand_schreier(emitted) == defect
            coefficients = Counter()
            for sign, t, family in emitted:
                coefficients[(t, family)] += sign
            terms = [{'retained_word_T': list(t), 'family_index_F11': family,
                      'coefficient': coefficient}
                     for (t, family), coefficient in sorted(coefficients.items()) if coefficient]
            rows.append({'section': section_name, 'operator': operator_name,
                         'retained_generator': i, 'section_generator_F11': generator,
                         'actual_image_F11': actual, 'coarse_head_T': coarse_head,
                         'same_section_lift_F11': section_lift, 'defect_F11': defect,
                         'exact_kernel_word': emitted, 'module_coefficients': terms,
                         'nonzero_module_class': bool(terms),
                         'witness_coefficient': terms[0] if terms else None})

out = {'status': 'PASS_EXACT_MARKED_COARSE_CORRECTION_EXTRACTION',
       'created_utc': datetime.now(timezone.utc).isoformat(), 'inputs': INPUTS,
       'actual_basis_change_round_trips': 14, 'actual_signed_operator_comparisons': 44,
       'existing_retained_rewrite_comparisons': 12,
       'module_basis': 'e_(t,i), t in T=F(f,cfc,tau c), i in (1,2,3,4,6,7,8,9)',
       'section_generators_F11': sections, 'rows': rows,
       'scope': 'Exact integral classes in the previously proved actual J_ab. Zero classes do not prove invariance. Any nonzero class is a post-node obstruction for the precisely named section. No arbitrary corrected-section nonexistence or fixed-source conclusion.'}
target = ROOT / 'records/root_coarse_corrections29.json'
assert not target.exists()
target.write_text(json.dumps(out, indent=2) + '\n')
for row in rows:
    print(row['section'], row['operator'], row['retained_generator'],
          'support', len(row['module_coefficients']), 'witness', row['witness_coefficient'])
print('PASS14 inverse basis checks;44 signed actual operator comparisons;12 complete previous rewrite comparisons;24 exact module classes.')
print('OUTPUT', target.relative_to(ROOT))
