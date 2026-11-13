#!/usr/bin/env python3
"""Independent isolated replay of D42's exact Q8 cover certificate."""
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
    stem = 'a_coprime_even'
    dependencies = ['a_coprime_intersection.py', 'a_coprime_frattini.py',
                    'a_peripheral_count.py', stem + '.py']
    names = dependencies + [stem + '.out', stem + '.json']
    protected = {name: digest(HERE / name) for name in names}
    replay = HERE / 'root_coprime_even_replay'
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
    assert data['status'] == 'PASS_EVEN_BASE_EXACT_COVER_FORMS_AND_LIFTS'
    covers = data['executed_covers']
    assert [c['p'] for c in covers] == [3, 5]
    assert all(len(c['matched_boundary_cases']) == 4 for c in covers)
    assert all(len(a['hensel_steps']) == 5 for c in covers
               for a in c['matched_boundary_cases'])
    assert all(digest(HERE / n) == h for n, h in protected.items())
    result = {'all_passed': True, 'entire_JSON_byte_identical': True,
              'actual_Q8_pants_covers': 2, 'matched_boundary_maps': 8,
              'exact_precision_levels': [3**6, 5**6],
              'original_artifacts_unchanged': True,
              'protected_sha256': protected,
              'seconds': round(time.time() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
