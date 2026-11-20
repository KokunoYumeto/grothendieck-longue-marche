"""Record immutable pre-comparison readings after every first page is complete."""
from pathlib import Path
from datetime import datetime,timezone
import csv,hashlib,json,sys
E=Path(__file__).resolve().parents[1];D=E/'second'
expected=[3]+list(range(5,28))
manifest=D/'FIRST_READINGS_SHA256.tsv'
mode=sys.argv[1]
if mode=='seal':
    assert not manifest.exists(),'First-reading manifest already exists'
    assert {json.loads(p.read_text())['scan'] for p in (E/'reader_reports').glob('*_reviewed.json')}==set(expected)
    assert not list(D.glob('*_second.tsv')),'Seal before any independent reading is submitted'
    rows=[]
    for n in expected:
        p=D/f'145_scan{n:03d}_first.tsv'
        rows.append({'file':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    with manifest.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['file','sha256'],delimiter='\t');w.writeheader();w.writerows(rows)
    with (E/'progress.log').open('a') as f:f.write('first box readings sealed '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'; 24 immutable files in second/FIRST_READINGS_SHA256.tsv\n')
elif mode=='verify':
    with manifest.open() as f:rows=list(csv.DictReader(f,delimiter='\t'))
    assert len(rows)==24
    for row in rows:assert hashlib.sha256((D/row['file']).read_bytes()).hexdigest()==row['sha256'],row['file']
    print('All 24 pre-comparison first-reading files are byte-for-byte unchanged.')
else:raise SystemExit(mode)
