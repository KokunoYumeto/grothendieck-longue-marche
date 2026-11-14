from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,csv
ROOT=Path(__file__).resolve().parents[1]
def utc():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
log=ROOT/'progress.log';s=log.read_text()
assert 'context opened' not in s and 'transcription frozen' not in s
pages=sorted((ROOT/'pages').glob('*.tex'));assert len(pages)==43
records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan*.json'))]
assert len(records)==43 and all('second_pass_audit' in r for r in records)
assert 'notation cross-check completed' in s
assert all(r['transcribed']=='yes' for r in csv.DictReader((ROOT/'MPL_121_001-048_inventory.csv').open()))
checks=json.loads((ROOT/'records/latex_validation/compile_results.json').read_text());assert checks['passed']==checks['total']==43
assert all(sha(ROOT/r['file'])==r['sha256'] and r['returncode']==0 for r in checks['pages'])
combined=ROOT/'MPL_121_001-048_transcription.tex'
assert combined.read_text()=='\n'.join(p.read_text().rstrip()+'\n' for p in pages)
paths=pages+[combined];t=utc();manifest={'frozen_utc':t,'reader':'root','files':{str(p.relative_to(ROOT)):sha(p) for p in paths}}
(ROOT/'records/frozen_sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
with log.open('a') as f:
 for name,digest in manifest['files'].items():f.write(f'SHA-256 {digest} {name}\n')
 f.write('transcription frozen '+t+'\n')
print(t, '44 transcription hashes frozen')
