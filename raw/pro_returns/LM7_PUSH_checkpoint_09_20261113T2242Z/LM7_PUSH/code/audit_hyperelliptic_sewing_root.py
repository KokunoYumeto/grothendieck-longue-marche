#!/usr/bin/env python3
"""Root's isolated byte-for-byte replay of the45 exact braid comparisons."""
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
    names = ['code/bc_hyperelliptic_sewing.py', 'code/bc_hyperelliptic_sewing.json',
             'code/bc_hyperelliptic_sewing.out', 'research/BC_hyperelliptic_CM_comparison.md']
    hashes = {n: sha256((ROOT/n).read_bytes()).hexdigest() for n in names}
    dest = ROOT/'research/root_hyperelliptic_sewing_replay'
    dest.mkdir(exist_ok=False)
    shutil.copyfile(ROOT/names[0], dest/'bc_hyperelliptic_sewing.py')
    with (dest/'replay.out').open('w') as out, (dest/'replay.err').open('w') as err:
        subprocess.run([sys.executable, str(dest/'bc_hyperelliptic_sewing.py')],
                       cwd=dest, stdout=out, stderr=err, check=True)
    assert (dest/'bc_hyperelliptic_sewing.json').read_bytes() == (ROOT/names[1]).read_bytes()
    assert (dest/'replay.out').read_bytes() == (ROOT/names[2]).read_bytes()
    result = json.loads((dest/'bc_hyperelliptic_sewing.json').read_text())
    assert result['comparison_count'] == 45 and all(result['matrix_checks'].values())
    assert all(sha256((ROOT/n).read_bytes()).hexdigest() == h for n, h in hashes.items())
    output = {'status': 'PASS_ROOT_EXACT_HYPERELLIPTIC_SEWING_REPLAY',
              'all_JSON_and_stdout_bytes_identical': True, 'literal_braid_comparisons': 45,
              'all_integral_genus_two_matrix_comparisons': True,
              'protected_original_sha256': hashes, 'seconds': round(time.monotonic()-started, 3)}
    (dest/'result.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(output, indent=2), flush=True)


if __name__ == '__main__':
    main()
