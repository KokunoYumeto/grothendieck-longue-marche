#!/usr/bin/env python3
"""Isolated, hash-protected standard-library replay of the E65 certificate."""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import shutil
import subprocess
import sys
import time


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def main():
    started = time.monotonic()
    root = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser()
    parser.add_argument('--destination', required=True)
    args = parser.parse_args()
    destination = Path(args.destination)
    if not destination.is_absolute():
        destination = root/destination
    assert not destination.exists(), 'The replay directory must be new.'
    manifest = json.loads((root/'research/E65_authoritative_manifest.json').read_text())
    for name, expected in manifest['protected_sha256'].items():
        assert digest(root/name) == expected, name
    destination.mkdir(parents=True)
    script = root/'code/a_cm_parity_character.py'
    shutil.copyfile(script, destination/script.name)
    with (destination/'a_cm_parity_character.out').open('w') as out, \
         (destination/'a_cm_parity_character.err').open('w') as err:
        subprocess.run([sys.executable, script.name], cwd=destination,
                       stdout=out, stderr=err, check=True)
    old = json.loads((root/'code/a_cm_parity_character.json').read_text())
    new = json.loads((destination/'a_cm_parity_character.json').read_text())
    old.pop('seconds')
    new.pop('seconds')
    assert old == new
    for name, expected in manifest['protected_sha256'].items():
        assert digest(root/name) == expected, name
    result = {'status': 'PASS_ISOLATED_E65_REPLAY',
              'all_mathematical_JSON_fields_identical': True,
              'all_protected_original_hashes_unchanged': True,
              'protected_file_count': len(manifest['protected_sha256']),
              'seconds': round(time.monotonic()-started, 6)}
    (destination/'replay_result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
