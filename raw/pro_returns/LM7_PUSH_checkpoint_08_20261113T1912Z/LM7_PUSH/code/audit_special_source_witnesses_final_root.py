#!/usr/bin/env python3
"""Replay final witness extension and compare the literal printed D52 table."""
from pathlib import Path
from hashlib import sha256
import copy
import difflib
import json
import re
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def strip_timing(record):
    return {k: v for k, v in record.items() if k != 'seconds'}


def main():
    started = time.monotonic()
    stem = 'de_special_source_witnesses'
    first = json.loads((HERE / 'audit_special_source_witnesses_root.json').read_text())
    assert first['all_passed']
    for ext in ('.py', '.json', '.out'):
        assert digest(HERE / (stem + '_initial' + ext)) == first['protected_sha256'][stem + ext]
    old = json.loads((HERE / (stem + '_initial.json')).read_text())
    current = json.loads((HERE / (stem + '.json')).read_text())
    comparison = copy.deepcopy(current)
    del comparison['witnesses'][3]['cyclic_equation']
    del comparison['witnesses'][3]['cyclic_all_associative_coefficients_zero']
    assert strip_timing(old) == strip_timing(comparison)
    assert current['witnesses'][3]['cyclic_all_associative_coefficients_zero']

    names = [stem + '.py', stem + '.json', stem + '.out',
             stem + '_initial.py', stem + '_initial.json', stem + '_initial.out',
             'de_source/d_metabelian.json',
             'audit_special_source_witnesses_root.py',
             'audit_special_source_witnesses_root.json',
             'audit_special_source_witnesses_root.out']
    protected = {'code/' + name: digest(HERE / name) for name in names}
    for path in ('sections/D_pronilpotent_lift_agent.tex',
                 'sections/D_full_weight5_agent.tex', 'sections/D_full_weight9_agent.tex'):
        protected[path] = digest(ROOT / path)
    replay = HERE / 'root_special_source_witnesses_final_replay'
    replay.mkdir(exist_ok=False)
    (replay / 'de_source').mkdir()
    for name in (stem + '.py', 'de_source/d_metabelian.json'):
        shutil.copy2(HERE / name, replay / name)
    with (replay / (stem + '_root_check.out')).open('x') as log:
        run = subprocess.run([sys.executable, stem + '.py'], cwd=replay,
                             stdout=log, stderr=subprocess.STDOUT)
    assert run.returncode == 0
    again = json.loads((replay / (stem + '.json')).read_text())
    assert strip_timing(again) == strip_timing(current)
    for directory, record in ((HERE, current), (replay, again)):
        for name, expected in record['source_sha256'].items():
            assert digest(directory / name) == expected
    assert again['status'] == 'PASS_EXACT_NORMALIZED_SPECIAL_WITNESSES'
    assert again['witnesses'][3]['cyclic_all_associative_coefficients_zero']

    tex = (ROOT / 'sections/D_full_weight9_agent.tex').read_text()
    table = tex.split(r'\begin{array}{lr|lr|lr}', 1)[1].split(r'\end{array}', 1)[0]
    entries = re.findall(r'([xy]{9})&(-?\d+)', table)
    assert len(entries) == len(dict(entries)) == 42
    printed = {word: int(value) for word, value in entries}
    assert printed == current['witnesses'][3]['integral_f_lyndon']
    assert all(digest(ROOT / name) == value for name, value in protected.items())
    diff = list(difflib.unified_diff(
        (HERE / (stem + '_initial.py')).read_text().splitlines(),
        (HERE / (stem + '.py')).read_text().splitlines(),
        fromfile=stem + '_initial.py', tofile=stem + '.py', lineterm=''))
    result = {'all_passed': True, 'initial_audit_and_original_export_preserved_exactly': True,
              'all_four_old_source_vectors_and_maps_unchanged': True,
              'direct_cyclic_identity_extension_reproduced': True,
              'all_mathematical_JSON_equal': True,
              'printed_D52_integral_Lyndon_coefficients_checked': len(printed),
              'actual_rescalings': [w['exact_rescaling'] for w in current['witnesses']],
              'common_denominator': 2, 'original_artifacts_unchanged': True,
              'exact_program_extension_diff': diff, 'protected_sha256': protected,
              'seconds': round(time.monotonic() - started, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
