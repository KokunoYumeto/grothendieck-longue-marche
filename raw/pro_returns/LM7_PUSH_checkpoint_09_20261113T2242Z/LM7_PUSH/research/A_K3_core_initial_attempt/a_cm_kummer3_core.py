#!/usr/bin/env python3
"""The complete B-core of the literal degree-three cyclic-cover quotient.

The map is induced from F <= B, with the actual six Schreier paths from
the retained modular source. Its 432-point permutation model retains all
three cyclic-cover origins in all six B/F cosets. No abstract subgroup or
unproved full-GT relation is substituted for this map.
"""
from pathlib import Path
from collections import deque
from hashlib import sha256
import subprocess
import time
import json
import numpy as np

from a_cm_kummer3_orbit import CyclicThree
from de_ferrari_a6_source_data import load_data
from de_a6_schreier_certificate import read_certificate, verify_words

HERE = Path(__file__).resolve().parent


def certify(name, gens, derived=False):
    prefix = HERE/name
    with prefix.with_suffix('.input').open('w') as f:
        f.write(f'{len(gens[0])} {len(gens)}\n')
        for g in gens:
            f.write(' '.join(map(str, g))+'\n')
    command = [str(HERE/'de_a6_schreier_fast')]
    if derived:
        command.append('--derived')
    command += [str(prefix.with_suffix('.input')), str(prefix.with_suffix('.bin'))]
    with prefix.with_suffix('.out').open('w') as out, prefix.with_suffix('.err').open('w') as err:
        subprocess.run(command, stdout=out, stderr=err, check=True)
    info = json.loads(next(x for x in reversed(prefix.with_suffix('.out').read_text().splitlines())
                           if x.startswith('{')))
    cert = read_certificate(prefix.with_suffix('.bin'))
    verify_words(cert)
    assert np.array_equal(cert['original'], gens)
    with Path(str(prefix)+'_replay.out').open('w') as out, Path(str(prefix)+'_replay.err').open('w') as err:
        subprocess.run([str(HERE/'de_a6_schreier_fast'), '--replay',
                        str(prefix.with_suffix('.bin'))], stdout=out, stderr=err, check=True)
    info['all_literal_word_DAGs_independently_replayed'] = True
    info['complete_Schreier_relations_replayed'] = True
    return info, cert


def main():
    start = time.monotonic()
    data = load_data()
    W = CyclicThree()
    Q = data['Q2']
    ix = {q:i for i,q in enumerate(Q)}
    root = ix[data['unit']]
    section = {data['unit']: []}
    todo = deque(section)
    while todo:
        q = todo.popleft()
        for a,g in ((0,data['s2']), (1,data['r2'])):
            qg = data['mul2'](q,g)
            if qg not in section:
                section[qg] = section[q]+[a]
                todo.append(qg)
    def wp(a):
        return np.array([24*((j+a[0]) % 3)+W.table[z][a[j+1]]
                         for j in range(3) for z in range(24)], dtype=np.uint16)
    for a in (W.x,W.y,W.inv(W.x),W.inv(W.y)):
        for b in (W.x,W.y,W.inv(W.x),W.inv(W.y)):
            assert np.array_equal(wp(W.mul(a,b)), wp(b)[wp(a)])
    letters, transition_words, transition_values = {}, {}, {}
    for a,g in ((0,data['s2']), (1,data['r2']), (-1,data['r22'])):
        blocks, words, values = [], [], []
        for q in Q:
            qg = data['mul2'](q,g)
            word = data['fword'](section[q]+[a]+data['binv'](section[qg]))
            val = W.word(word)
            blocks.append(72*ix[qg]+wp(val))
            words.append(list(word))
            values.append(val)
        letters[a] = np.concatenate(blocks)
        transition_words[a] = words
        transition_values[a] = values
    one = np.arange(432,dtype=np.uint16)
    assert np.array_equal(letters[0][letters[0]],one)
    assert np.array_equal(letters[1][letters[1][letters[1]]],one)
    assert np.array_equal(letters[-1],np.argsort(letters[1]))
    def bword(word):
        a = one.copy()
        for letter in word:
            a = letters[letter][a]
        return a
    x, y = bword(data['xword']), bword(data['yword'])
    assert np.array_equal(x[root*72:(root+1)*72]-root*72,wp(W.x))
    assert np.array_equal(y[root*72:(root+1)*72]-root*72,wp(W.y))
    N = np.array([bword(w) for w in data['Nwords']])
    for word, value in zip(data['Nwords'],N):
        fw = data['fword'](word)
        assert np.array_equal(value[root*72:(root+1)*72]-root*72,wp(W.word(fw)))
    info = {}
    info['B'], Bcert = certify('a_cm_kummer3_core_B',np.array([letters[0],letters[1]]))
    print('B',info['B']['order'],flush=True)
    info['N'], Ncert = certify('a_cm_kummer3_core_N',N)
    print('N',info['N']['order'],flush=True)
    info['N_derived'], Ccert = certify('a_cm_kummer3_core_N_derived',N,True)
    print('N derived',info['N_derived']['order'],flush=True)
    info['N_second_derived'], CCcert = certify('a_cm_kummer3_core_N_second_derived',Ccert['strong'],True)
    print('N second derived',info['N_second_derived']['order'],flush=True)
    bo,no,co,cco = [int(info[k]['order']) for k in ('B','N','N_derived','N_second_derived')]
    assert bo % no == no % co == co % cco == 0
    out = {
        'status':'PASS_COMPLETE_BASED_CYCLIC_THREE_B_CORE',
        'literal_degree':432,
        'B_over_F_coset_section':[section[q] for q in Q],
        'root_coset_index':root,
        'B_generators_as_F_transition_words':transition_words,
        'B_generators_as_cyclic_transition_values':transition_values,
        'all_literal_source_and_transition_maps_checked':True,
        'groups':info,
        'B_over_N_index':bo//no,
        'N_abelianization_order':no//co,
        'N_derived_abelianization_order':co//cco,
        'N_derived_has_nontrivial_two_group_quotient':(co//cco)%2==0,
        'scope':'Actual six-coset core of all three based cyclic coordinates. Relations are imposed only through their literal source maps.',
        'input_sha256':{n:sha256((HERE/n).read_bytes()).hexdigest() for n in (
            'a_cm_kummer3_orbit.py','de_ferrari_a6_source_data.py',
            'de_ferrari_sl2_5_N.json','de_a6_schreier.cpp','de_a6_schreier_certificate.py')},
        'seconds':round(time.monotonic()-start,6),
    }
    np.savez_compressed(HERE/'a_cm_kummer3_core.npz',s=letters[0],r=letters[1],
                        x=x,y=y,N_generators=N)
    (HERE/'a_cm_kummer3_core.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in {
        'B_generators_as_F_transition_words','B_generators_as_cyclic_transition_values'}},indent=2),flush=True)


if __name__=='__main__':
    main()
