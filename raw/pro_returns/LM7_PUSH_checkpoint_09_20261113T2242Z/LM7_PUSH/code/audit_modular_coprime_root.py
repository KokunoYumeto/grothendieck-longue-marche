#!/usr/bin/env python3
"""Independent isolated replay of the exact D44 word and cusp-gauge certificate."""
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
    start = time.time()
    stem = 'a_modular_coprime'
    dependencies = ['a_peripheral_count.py', stem + '.py']
    names = dependencies + [stem + '.out', stem + '.json']
    protected = {name: digest(HERE / name) for name in names}
    replay = HERE / 'root_modular_coprime_replay'
    replay.mkdir(exist_ok=False)
    for name in dependencies:
        shutil.copy2(HERE / name, replay / name)
    with (replay / (stem + '_root_check.out')).open('x') as log:
        run = subprocess.run([sys.executable, str(replay / (stem + '.py'))],
                             cwd=replay, stdout=log, stderr=subprocess.STDOUT)
    assert run.returncode == 0
    old, new = HERE / (stem + '.json'), replay / (stem + '.json')
    assert old.read_bytes() == new.read_bytes()
    data = json.loads(new.read_text())
    assert str(data['status']).startswith('PASS')
    assert all(digest(HERE / name) == value for name, value in protected.items())
    result = {'all_passed': True, 'entire_JSON_byte_identical': True,
              'source_status': data['status'],
              'original_artifacts_unchanged': True,
              'protected_sha256': protected,
              'seconds': round(time.time() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
