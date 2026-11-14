#!/usr/bin/env python3
"""Isolated root replay of the exact quartic CM comparison program."""
from pathlib import Path
from hashlib import sha256
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent.parent


def main():
    started = time.monotonic()
    names = ['code/bc_cm_norm_characters.py', 'code/bc_cm_norm_characters.json',
             'code/bc_cm_norm_characters.out', 'code/bc_hyperelliptic_sewing.py',
             'research/BC_CM_norm_character_next.md']
    hashes = {name: sha256((ROOT / name).read_bytes()).hexdigest() for name in names}
    dest = ROOT / 'research/root_cm_norm_characters_replay'
    dest.mkdir(exist_ok=False)
    for name in (names[0], names[3]):
        shutil.copyfile(ROOT / name, dest / Path(name).name)
    with (dest / 'replay.out').open('w') as out, (dest / 'replay.err').open('w') as err:
        subprocess.run([sys.executable, 'bc_cm_norm_characters.py'], cwd=dest,
                       stdout=out, stderr=err, check=True)
    assert (dest / 'bc_cm_norm_characters.json').read_bytes() == (ROOT / names[1]).read_bytes()
    assert (dest / 'replay.out').read_bytes() == (ROOT / names[2]).read_bytes()
    data = json.loads((dest / 'bc_cm_norm_characters.json').read_text())
    assert data['comparison_count'] == 14
    assert all(sha256((ROOT / name).read_bytes()).hexdigest() == value
               for name, value in hashes.items())
    result = {'status': 'PASS_ROOT_EXACT_QUARTIC_CM_REPLAY',
              'all_JSON_and_stdout_bytes_identical': True,
              'literal_braid_comparisons': 14,
              'full_free_by_cyclic_comparison_replayed': True,
              'integral_and_finite_centralizer_checks_replayed': True,
              'both_positive_CM_tables_and_signed_covariances_replayed': True,
              'protected_original_sha256': hashes,
              'seconds': round(time.monotonic()-started, 3)}
    (dest / 'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2), flush=True)


if __name__ == '__main__':
    main()
