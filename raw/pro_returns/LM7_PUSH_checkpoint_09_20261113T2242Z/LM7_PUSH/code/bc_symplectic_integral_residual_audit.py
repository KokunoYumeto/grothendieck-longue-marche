#!/usr/bin/env python3
"""Isolated replay plus additional K2/action checks for the root residual."""
from contextlib import redirect_stdout
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import shutil
import time
import sympy as sp

HERE = Path(__file__).resolve().parent
STEM = 'bc_symplectic_integral_residual_audit'
ROOT = 'e_symplectic_five_integral_residual_root'


def main():
    start = time.time()
    protected = [ROOT+'.py',ROOT+'.json',ROOT+'.out',
                 'e_symplectic_five_integral_probe_root.json']
    before = {n:sha256((HERE/n).read_bytes()).hexdigest() for n in protected}
    outdir = HERE.parent/'research'/'audit_geometry_integral_residual'
    outdir.mkdir(parents=True,exist_ok=True)
    for n in ('e_symplectic_five_integral_probe_root.json',
              'de_ferrari_a6_source_data.py'):
        shutil.copy2(HERE/n,outdir/n)
    spec = importlib.util.spec_from_file_location('geometry_integral_root_replay',HERE/(ROOT+'.py'))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.HERE = outdir
    with (outdir/(ROOT+'.out')).open('w') as output,redirect_stdout(output):
        mod.main()
    original = json.loads((HERE/(ROOT+'.json')).read_text())
    replay = json.loads((outdir/(ROOT+'.json')).read_text())
    def mathematical(d):
        return {k:v for k,v in d.items() if k != 'seconds'}
    assert mathematical(original) == mathematical(replay)
    model = mod.IntegralModel()
    data = model.source
    A = {name:sp.Matrix(rec['matrix']) for name,rec in original['conjugation_actions'].items()}
    # Row coordinates give an antihomomorphism in the conjugating word.
    def action_word(word):
        ans = sp.eye(5)
        for b in word:
            g = A['s'] if b == 0 else A['r']**b
            ans = g*ans
        return ans
    assert action_word(data['xword']) == A['x']
    assert action_word(data['yword']) == A['y']
    count = 0
    for rec in model.d['K2_full_Schreier_basis_factorizations']:
        w = rec['B_word']; _,v,_ = model.factor(w)
        assert v == sp.Matrix(rec['radical_coordinates'])
        for name,b in (('s',[0]),('r',[1]),('x',data['xword']),('y',data['yword'])):
            _,actual,_ = model.factor(b+w+data['binv'](b))
            assert actual == v*A[name]
            count += 1
    signs = {r['coordinate']:(r['x_signs'],r['y_signs']) for r in original['standard_signs']}
    assert signs[18] == ([1],[1])
    assert signs[10] == ([1],[-1]) and signs[26] == ([-1],[1])
    derived = sp.Matrix(original['derived_basis'])
    assert derived.rank() == 3
    assert derived[:,original['derived_pivot_columns']].det() == -sp.Rational(1,3)
    assert original['derived_lattice']['integer_lattice_Smith'] == [1,1,1]
    assert original['stable_commutator_lattice']['integer_lattice_Smith'] == [1,1,4]
    assert sp.Matrix(original['x2_y2_character_matrix']).det() == sp.Rational(1,6)
    after = {n:sha256((HERE/n).read_bytes()).hexdigest() for n in protected}
    assert before == after
    result = {'status':'PASS_ISOLATED_INTEGRAL_RESIDUAL_AND_K2_AUDIT',
              'all_mathematical_JSON_entries_identical':True,
              'conjugated_N_replay_count':388,
              'additional_literal_K2_conjugation_checks':count,
              'row_antihomomorphism_checked_on_actual_x_y_words':True,
              'actual_parity_coordinates':[10,26],
              'derived_rank':3,'derived_pivot_determinant':'-1/3',
              'derived_Smith':[1,1,1],'stable_commutator_Smith':[1,1,4],
              'x2_y2_character_determinant':'1/6',
              'protected_input_sha256':before,'all_originals_unchanged':True,
              'seconds':round(time.time()-start,3)}
    (HERE/(STEM+'.json')).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
