"""Freeze all 24 decided transcriptions, then recheck and archive the full record."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, subprocess, sys, zipfile

OUT = Path(__file__).resolve().parents[1]
EXPECTED = [2,3,4,5,6,7,8,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
PREFIX = 'SP40_CW_81'
def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def append(line):
    with (OUT/'progress.log').open('a') as f:
        f.write(line+'\n')
mode = sys.argv[1]
manifest = OUT/'freeze_manifest.json'
if mode == 'freeze':
    assert not manifest.exists(), 'A frozen transcription already exists'
    records = [json.loads(p.read_text()) for p in sorted((OUT/'records').glob('scan*.json'))]
    assert [r['scan'] for r in records] == EXPECTED, 'All 24 scans are required'
    progress = (OUT/'progress.log').read_text()
    for r in records:
        assert r.get('main_adjudicated') is True
        assert f"scan {r['scan']:03d} done " in progress
    subprocess.run([sys.executable, str(OUT/'scripts/build_records.py')], check=True)
    subprocess.run([sys.executable, str(OUT/'scripts/validate.py')], check=True, stdout=subprocess.DEVNULL)
    report = json.loads((OUT/'checks/structural_validation.json').read_text())
    assert report['tex_ok'] and not report['record_issues'], report
    files = [OUT/'pages'/r['filename'] for r in records] + [OUT/(PREFIX+'_transcription.tex')]
    hashes = {str(p.relative_to(OUT)):digest(p) for p in files}
    when = utc()
    manifest.write_text(json.dumps({'frozen_utc':when,'sha256':hashes}, indent=2)+'\n')
    for name, sha in hashes.items():
        append(f'SHA-256 {sha} {name}')
    append('transcription frozen '+when)
    print(json.dumps({'frozen':True,'files':len(files),'utc':when}))
elif mode == 'archive':
    frozen = json.loads(manifest.read_text())
    for name, sha in frozen['sha256'].items():
        assert digest(OUT/name) == sha, 'Frozen file changed: '+name
    required = [PREFIX+'_transcription.tex', PREFIX+'_changes.md', PREFIX+'_collation.tsv',
                PREFIX+'_doubts.md', PREFIX+'_inventory.csv', PREFIX+'_notes.md',
                'progress.log', PREFIX+'_workflow.md', 'CHECK_EVENTS.tsv']
    assert all((OUT/name).exists() for name in required)
    dest = OUT.parent/(PREFIX+'.zip')
    assert not dest.exists(), 'Refusing to overwrite an existing final archive'
    append('frozen SHA-256 values rechecked unchanged '+utc())
    append('final archive prepared '+utc())
    with zipfile.ZipFile(dest, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as z:
        for p in sorted(OUT.rglob('*')):
            if p.is_file() and p.suffix != '.zip' and '__pycache__' not in p.parts:
                z.write(p, p.relative_to(OUT))
    print(json.dumps({'file':str(dest),'size':dest.stat().st_size,'sha256':digest(dest)}))
else:
    raise SystemExit('Use freeze or archive')
