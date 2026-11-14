#!/usr/bin/env python3
"""Independent exact replay of D38's actual class and A6 maps."""
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
    stems = ('a_weight5_class_preserving', 'a_weight5_a6_odd')
    inputs = ['a_weight5_characteristic.py', 'a_peripheral_count.py',
              'a_peripheral_a6_outer.json']
    names = inputs + [s + ext for s in stems for ext in ('.py', '.json', '.out')]
    protected = {n: digest(HERE / n) for n in names}
    replay = HERE / 'root_weight5_constraints_replay'
    replay.mkdir(exist_ok=False)
    for n in inputs + [s + '.py' for s in stems]:
        shutil.copy2(HERE / n, replay / n)
    results = []
    for stem in stems:
        with (replay / (stem + '_root_check.out')).open('x') as log:
            run = subprocess.run([sys.executable, str(replay / (stem + '.py'))],
                                 cwd=replay, stdout=log, stderr=subprocess.STDOUT)
        assert run.returncode == 0, stem
        a, b = HERE / (stem + '.json'), replay / (stem + '.json')
        assert json.loads(a.read_text()) == json.loads(b.read_text()), stem
        assert a.read_bytes() == b.read_bytes(), stem
        results.append({'program': stem + '.py', 'entire_JSON_byte_identical': True})
        print('PASS', stem, flush=True)
    assert all(digest(HERE / n) == h for n, h in protected.items())
    result = {'all_passed': True, 'programs': results,
              'original_artifacts_unchanged': True,
              'protected_sha256': protected, 'seconds': round(time.time()-start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'protected_sha256'}, indent=2))


if __name__ == '__main__':
    main()
