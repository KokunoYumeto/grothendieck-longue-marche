from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
PREFIX='MPL_15_195-228+18_002-017'
log=ROOT/'progress.log';assert 'transcription frozen ' not in log.read_text();assert 'context opened ' not in log.read_text()
expected=json.loads((ROOT/'records/expected_pages.json').read_text());assert len(expected)==49
entries=[];combined=b''
for e in expected:
 rel=f'pages/{PREFIX}_{e["cote"]}_scan{e["scan"]:03d}.tex';p=ROOT/rel;data=p.read_bytes();sha=hashlib.sha256(data).hexdigest();combined+=data
 a=json.loads((ROOT/'records'/f'audit_{e["cote"]}_{e["scan"]:03d}.json').read_text());assert a['page_sha256_after_audit']==sha
 entries.append({'file':rel,'sha256':sha})
rel=PREFIX+'_transcription.tex';assert (ROOT/rel).read_bytes()==combined
entries.append({'file':rel,'sha256':hashlib.sha256(combined).hexdigest()})
assert json.loads((ROOT/'records/structural_pre_freeze_report.json').read_text())['mechanical_checks_passed']
assert (ROOT/'records/notation_crosscheck.json').is_file()
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest={'frozen_utc':now,'files':entries}
(ROOT/'records/frozen_sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
with log.open('a') as f:
 for e in entries:f.write('sha256 '+e['file']+' '+e['sha256']+'\n')
 f.write('transcription frozen '+now+'\n')
for e in entries:(ROOT/e['file']).chmod(0o444)
print('transcription frozen '+now)
print('SHA-256 recorded for 49 page files and the complete fragment.')
