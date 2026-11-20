"""Freeze, verify and package the completed transcription. No TeX engine or OCR."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,zipfile
O=Path(__file__).resolve().parents[1]
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(1024*1024),b''):h.update(block)
 return h.hexdigest()
def log(s):
 with (O/'progress.log').open('a') as f:f.write(s+'\n')
order=json.loads((O/'page_order.json').read_text())
expected=[int(x['our_scan']) for x in order]
decisions=[json.loads(p.read_text()) for p in sorted((O/'decisions').glob('scan*.json'))]
assert len(expected)==25 and [x['scan'] for x in decisions]==expected,'All 25 pages must be decided in order.'
assert all(x.get('decided_utc') for x in decisions),'Uncommitted page.'
paths=[O/'pages'/Path(x['codex_file']).name for x in order]+[O/'SP46_CW_37_transcription.tex']
target=O/'transcription_hashes.json'
mode=sys.argv[1]
if mode=='freeze':
 assert not target.exists(),'Do not replace an existing freeze record.'
 hashes={str(p.relative_to(O)):sha(p) for p in paths}
 t=now();target.write_text(json.dumps({'frozen_utc':t,'sha256':hashes},indent=2)+'\n')
 log('transcription frozen '+t)
 for name,h in hashes.items():log('SHA-256 '+h+' '+name)
 print('Frozen SHA-256 for 25 pages and the combined fragment at',t)
elif mode in ('verify','package'):
 saved=json.loads(target.read_text());current={str(p.relative_to(O)):sha(p) for p in paths}
 assert current==saved['sha256'],'The frozen transcription has changed.'
 t=now();log('transcription hashes unchanged '+t+'; verified all 25 pages and the combined fragment')
 print('All frozen transcription hashes are unchanged at',t)
 if mode=='package':
  z=O.parent/'SP46_CW_37.zip';assert not z.exists(),'Do not overwrite an existing final ZIP.'
  log('final package SP46_CW_37.zip prepared '+t+'; excludes source attachments, witnesses, scans and earlier ZIPs')
  files=[p for p in sorted(O.rglob('*')) if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.name!='FINAL_MANIFEST.sha256']
  manifest=O/'FINAL_MANIFEST.sha256'
  manifest.write_text(''.join(sha(p)+'  '+str(p.relative_to(O))+'\n' for p in files))
  with zipfile.ZipFile(z,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as archive:
   for p in files+[manifest]:archive.write(p,p.relative_to(O))
  with zipfile.ZipFile(z) as archive:assert archive.testzip() is None
  print(json.dumps({'path':str(z),'bytes':z.stat().st_size,'sha256':sha(z),'members':len(files)+1}))
else:raise SystemExit('Use freeze, verify or package.')
