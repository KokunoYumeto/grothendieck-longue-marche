"""Freeze only a complete 28-page transcription, then verify its hashes separately."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
O=Path(__file__).resolve().parents[1]
def utc():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files=sorted((O/'pages').glob('*.tex'))+[O/'SP53_CW_156-6_transcription.tex']
manifest=O/'TRANSCRIPTION_SHA256.json'
mode=sys.argv[1] if len(sys.argv)>1 else 'status'
if mode=='freeze':
    assert not manifest.exists(),'Freeze already exists; do not overwrite it'
    ds=[json.loads((O/f'decisions/scan{n:03}.json').read_text()) for n in range(6,34)]
    assert all(d.get('committed') and d.get('adjudicated_all') for d in ds)
    assert len(files)==29,len(files)
    for d in ds:
        n=d['scan']
        assert all(x['transcribed']=='yes' for x in d['inventory'])
        for r in range(1,4):
            report=json.loads((O/f'readers/scan{n:03}/R{r}/report.json').read_text())
            legacy_complete=(n==6 and d.get('brief')=='v001' and report.get('finished_utc') and report.get('inventory') and report.get('notes'))
            assert report.get('status')=='complete' or legacy_complete,(n,r)
    hashes={str(p.relative_to(O)):sha(p) for p in files}
    manifest.write_text(json.dumps({'frozen_utc':utc(),'hashes':hashes},indent=2)+'\n')
    with (O/'progress.log').open('a') as f:
        f.write('transcription frozen '+utc()+'\n')
        for name,h in hashes.items():f.write(f'SHA-256 {h}  {name}\n')
    print('Frozen 28 pages and the combined transcription.')
elif mode=='verify':
    m=json.loads(manifest.read_text())
    mismatches=[name for name,h in m['hashes'].items() if not (O/name).exists() or sha(O/name)!=h]
    assert not mismatches,mismatches
    assert len(m['hashes'])==29
    with (O/'progress.log').open('a') as f:f.write('frozen hashes verified unchanged '+utc()+'; all 28 pages and combined transcription\n')
    print('All 29 frozen hashes are unchanged.')
else:
    print(json.dumps({'page_files':len(files)-1,'frozen':manifest.exists()}))
