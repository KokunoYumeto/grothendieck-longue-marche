#!/usr/bin/env python3
"""Isolated root replay of the two exact affine orbifold source maps."""
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
    destination = ROOT/'research/root_orbifold_CM_replay'
    destination.mkdir(exist_ok=False)
    work = destination/'code'
    work.mkdir()
    names = ['bc_orbifold_CM_characters.py', 'bc_hyperelliptic_sewing.py',
             'bc_cm_literal_words.json', 'bc_orbifold_CM_characters.json',
             'bc_orbifold_CM_characters.out']
    protected = {name:sha256((ROOT/'code'/name).read_bytes()).hexdigest() for name in names}
    note = ROOT/'research/BC_orbifold_sign_reduction.md'
    note_hash = sha256(note.read_bytes()).hexdigest()
    for name in names[:3]:
        shutil.copy2(ROOT/'code'/name, work/name)
    with (work/'bc_orbifold_CM_characters.out').open('w') as out, (work/'bc_orbifold_CM_characters.err').open('w') as err:
        subprocess.run([sys.executable, 'bc_orbifold_CM_characters.py'], cwd=work,
                       stdout=out, stderr=err, check=True)
    for name in names[3:]:
        assert (ROOT/'code'/name).read_bytes() == (work/name).read_bytes()
    assert all(sha256((ROOT/'code'/name).read_bytes()).hexdigest() == digest
               for name, digest in protected.items())
    assert sha256(note.read_bytes()).hexdigest() == note_hash
    result = {
        'status':'PASS_ROOT_EXACT_ORBIFOLD_CHARACTER_REPLAY',
        'JSON_and_stdout_byte_identical':True,
        'protected_originals_unchanged':6,
        'complete_root_proof_and_program_reads':True,
        'scope':'The proved positive Mordell sign and actual Gaussian finite character and source maps; no whole-GT discrepancy value.',
        'input_sha256':protected, 'proof_note_sha256':note_hash,
        'seconds':round(time.monotonic()-started, 6),
    }
    (destination/'result.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
