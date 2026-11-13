#!/usr/bin/env python3
"""Isolated exact replay of both frozen D49 surface and cover certificates."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def main():
    start = time.time()
    manifest_path = HERE / 'a_v4_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    protected = {row['path']: row['sha256'] for row in manifest['files']}
    protected['code/a_v4_manifest.json'] = digest(manifest_path)
    proof = 'sections/D_v4_refinement_agent.tex'
    assert protected[proof] == '2de18a22aa4b8e2dba00888a3c316e9c56331d980b44a587f439ae4b6026c40c'
    for name, expected in protected.items():
        assert digest(ROOT / name) == expected, name
    replay = HERE / 'root_v4_refinement_replay'
    replay.mkdir(exist_ok=False)
    for name in protected:
        path = Path(name)
        if path.parts[0] == 'code':
            shutil.copy2(ROOT / name, replay / path.name)
    rows = []
    for stem in ('a_v4_surface', 'a_v4_cover'):
        tick = time.time()
        output = replay / (stem + '_root_check.out')
        with output.open('x') as log:
            run = subprocess.run([sys.executable, '-u', stem + '.py'], cwd=replay,
                                 stdout=log, stderr=subprocess.STDOUT)
        assert run.returncode == 0, stem
        expected = json.loads((HERE / (stem + '.json')).read_text())
        actual = json.loads((replay / (stem + '.json')).read_text())
        assert expected == actual, stem
        assert (HERE / (stem + '.json')).read_bytes() == (replay / (stem + '.json')).read_bytes()
        assert (HERE / (stem + '.out')).read_bytes() == output.read_bytes()
        row = {'program': stem, 'exit_code': 0, 'all_JSON_and_log_bytes_equal': True,
               'json_sha256': digest(replay / (stem + '.json')),
               'seconds': round(time.time() - tick, 3)}
        rows.append(row)
        print(json.dumps(row), flush=True)
    assert all(digest(ROOT / name) == value for name, value in protected.items())
    result = {'all_passed': True, 'steps': rows, 'original_artifacts_unchanged': True,
              'proof_sha256': protected[proof], 'protected_sha256': protected,
              'seconds': round(time.time() - start, 3)}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print('ROOT_V4_REFINEMENT_FULL_REPLAY_PASS', flush=True)


if __name__ == '__main__':
    main()
