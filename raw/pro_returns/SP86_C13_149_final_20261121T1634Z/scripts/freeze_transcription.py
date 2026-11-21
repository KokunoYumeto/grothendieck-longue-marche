"""Freeze the completed transcription, or verify its unchanged bytes at delivery."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import sys
import validate

BASE = Path(__file__).resolve().parents[1]
MANIFEST = BASE / 'transcription_sha256.json'
FINAL_MANIFEST = BASE / 'transcription_sha256_final.json'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def run(verify=False):
    stamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    if verify:
        selected_manifest = FINAL_MANIFEST if FINAL_MANIFEST.exists() else MANIFEST
        record = json.loads(selected_manifest.read_text())
        failed = [name for name, digest in record['files'].items() if sha(BASE / name) != digest]
        assert not failed, f'Frozen transcription changed: {failed}'
        with (BASE / 'progress.log').open('a') as log:
            log.write(f'transcription hashes verified unchanged {stamp}: all 23 page files and combined transcription match {selected_manifest.name}; earlier superseded records remain preserved\n')
        print(json.dumps({'verified_utc': stamp, 'files': len(record['files']), 'manifest': selected_manifest.name, 'unchanged': True}))
        return
    assert not MANIFEST.exists(), 'Transcription already frozen'
    assert not validate.validate(final=True)['errors']
    paths = sorted((BASE / 'pages').glob('149_scan*.tex'))
    assert len(paths) == 23
    paths.append(BASE / 'SP86_C13_149_transcription.tex')
    record = {'frozen_utc': stamp, 'files': {str(path.relative_to(BASE)): sha(path) for path in paths}}
    MANIFEST.write_text(json.dumps(record, indent=2) + '\n')
    with (BASE / 'progress.log').open('a') as log:
        log.write(f'transcription frozen {stamp}\n')
        for name, digest in record['files'].items():
            log.write(f'SHA-256 {digest} {name}\n')
    print(json.dumps({'frozen_utc': stamp, 'files': len(paths)}))

def freeze_after_recorded_separator_correction():
    """Record the final bytes after the documented single TeX delimiter fix.

    This preserves the earlier manifest and verifies the exact changed-file set
    and both before/after digests from the correction record before proceeding.
    """
    assert not FINAL_MANIFEST.exists(), 'Final transcription already frozen'
    correction=json.loads((BASE/'serialization_corrections.json').read_text())
    old=json.loads(MANIFEST.read_text())
    assert sha(MANIFEST)==correction['earlier_manifest_sha256']
    assert correction['before']==r'\midK' and correction['after']==r'\mid K'
    page='pages/149_scan075.tex';combined='SP86_C13_149_transcription.tex'
    changed={name for name,digest in old['files'].items() if sha(BASE/name)!=digest}
    assert changed=={page,combined},changed
    assert old['files'][page]==correction['page_before_sha256']
    assert old['files'][combined]==correction['combined_before_sha256']
    assert sha(BASE/page)==correction['page_after_sha256']
    assert sha(BASE/combined)==correction['combined_after_sha256']
    assert not validate.validate(final=True)['errors']
    stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    record={'frozen_utc':stamp,'supersedes':'transcription_sha256.json',
            'reason':'The single recorded TeX control-word delimiter correction; manuscript readings and fixed audits unchanged.',
            'correction_record':'serialization_corrections.json',
            'files':{name:sha(BASE/name) for name in old['files']}}
    FINAL_MANIFEST.write_text(json.dumps(record,indent=2)+'\n')
    with (BASE/'progress.log').open('a') as log:
        log.write(f'transcription frozen {stamp}: final manifest transcription_sha256_final.json; earlier manifest retained after the documented TeX delimiter correction\n')
        for name,digest in record['files'].items():log.write(f'SHA-256 {digest} {name}\n')
    print(json.dumps({'frozen_utc':stamp,'files':len(record['files']),'manifest':FINAL_MANIFEST.name,'earlier_manifest_preserved':True}))

if __name__ == '__main__':
    if '--after-recorded-separator-correction' in sys.argv:
        freeze_after_recorded_separator_correction()
    else:
        run('--verify' in sys.argv)
