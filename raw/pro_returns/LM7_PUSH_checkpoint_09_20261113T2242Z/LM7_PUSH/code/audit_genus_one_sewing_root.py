#!/usr/bin/env python3
"""Independent isolated E.61 replay with every frozen original protected."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / 'research/E61_authoritative_manifest.json'
DEST = ROOT / 'research/root_E61_replay'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    started = time.monotonic()
    inventory = json.loads(MANIFEST.read_text())
    protected = inventory['files']
    for name, record in protected.items():
        assert sha(ROOT / name) == record['sha256'], name
    assert not DEST.exists(), 'Replay destination already exists.'
    code = DEST / 'code'
    code.mkdir(parents=True)
    for name in ('bc_genus_one_sewing.py', 'bc_cm_literal_words.json'):
        shutil.copyfile(ROOT / 'code' / name, code / name)
    with (code / 'bc_genus_one_sewing.out').open('w') as out:
        with (code / 'bc_genus_one_sewing.err').open('w') as err:
            run = subprocess.run([sys.executable, 'bc_genus_one_sewing.py'],
                                 cwd=code, stdout=out, stderr=err)
    assert run.returncode == 0, run.returncode
    for name in ('bc_genus_one_sewing.json', 'bc_genus_one_sewing.out'):
        assert (code / name).read_bytes() == (ROOT / 'code' / name).read_bytes(), name
    result = json.loads((code / 'bc_genus_one_sewing.json').read_text())
    assert result['status'] == 'PASS_LITERAL_SEWING_COMPARISONS'
    assert len(result['braid_identities']) == 16
    assert len(result['records']) == 24
    assert len(result['complete_mod3_frame_classification']) == 24
    assert result['good_mod3_frames'] == 12
    assert result['central_carries_in_four_IV_substitutions'] == [2, -2, 2, -2]
    assert result['central_carry_sum'] == 0
    assert result['same_G6_beta_correction_contrast'] is None
    for name, record in protected.items():
        assert sha(ROOT / name) == record['sha256'], name
    audit = {
        'status': 'PASS_ISOLATED_COMPLETE_E61_ROOT_REPLAY',
        'manifest_sha256': sha(MANIFEST),
        'all_output_bytes_identical': True,
        'protected_original_files_unchanged': len(protected),
        'literal_braid_identities': 16,
        'complete_mod3_frames': 24,
        'signed_cubic_passing_frames': 12,
        'framed_CM_words': 24,
        'seconds': round(time.monotonic() - started, 3),
    }
    (DEST / 'result.json').write_text(json.dumps(audit, indent=2) + '\n')
    print(json.dumps(audit, indent=2), flush=True)


if __name__ == '__main__':
    main()
