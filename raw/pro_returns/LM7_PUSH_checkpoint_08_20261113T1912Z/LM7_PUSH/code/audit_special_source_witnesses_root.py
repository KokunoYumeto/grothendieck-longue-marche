#!/usr/bin/env python3
"""Literal isolated replay of the four normalized free-Lie witnesses."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    started = time.time()
    stem = 'de_special_source_witnesses'
    names = [stem + '.py', stem + '.json', stem + '.out', 'de_source/d_metabelian.json']
    protected = {name: digest(HERE / name) for name in names}
    replay = HERE / 'root_special_source_witnesses_replay'
    replay.mkdir(exist_ok=False)
    (replay / 'de_source').mkdir()
    for name in (names[0], names[3]):
        shutil.copy2(HERE / name, replay / name)
    with (replay / (stem + '_root_check.out')).open('x') as log:
        run = subprocess.run([sys.executable, stem + '.py'], cwd=replay,
                             stdout=log, stderr=subprocess.STDOUT)
    assert run.returncode == 0
    a = json.loads((HERE / names[1]).read_text())
    b = json.loads((replay / names[1]).read_text())
    for directory, record in ((HERE, a), (replay, b)):
        for name, expected in record['source_sha256'].items():
            assert digest(directory / name) == expected
    assert {k: v for k, v in a.items() if k != 'seconds'} == {
        k: v for k, v in b.items() if k != 'seconds'}
    assert a['status'] == 'PASS_EXACT_NORMALIZED_SPECIAL_WITNESSES'
    assert len(a['witnesses']) == 4 and a['common_denominator_all_four'] == 2
    assert all(digest(HERE / name) == value for name, value in protected.items())
    result = {'all_passed': True, 'all_mathematical_JSON_equal': True,
              'all_four_literal_free_Lie_witnesses_reproduced': True,
              'actual_rescalings': [w['exact_rescaling'] for w in a['witnesses']],
              'common_denominator': 2, 'original_artifacts_unchanged': True,
              'protected_sha256': protected, 'seconds': round(time.time() - started, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
