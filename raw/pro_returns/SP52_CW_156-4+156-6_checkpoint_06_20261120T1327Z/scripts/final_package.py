"""Final freeze/package gates. Run only after every page and notation review are complete."""
from pathlib import Path
import argparse, datetime, hashlib, json, subprocess, sys, zipfile

O=Path(__file__).resolve().parents[1]
ID='SP52_CW_156-4+156-6'
def now():return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def include_in_package(p):
 excluded_dirs={'__pycache__','packets','originals','scans','witnesses','context'}
 return p.is_file() and p.suffix.lower()!='.zip' and not excluded_dirs.intersection(p.relative_to(O).parts[:-1]) and p!=O/'PREAMBLE.tex'
def prerequisites():
 order=json.loads((O/'page_order.json').read_text())
 log=(O/'progress.log').read_text().splitlines()
 expected=[]
 for m in order:
  key=f"{m['cote']}_{int(m['our_scan']):03d}"
  dp=O/'decisions'/f'{key}.json'
  if not dp.exists():raise SystemExit(f'Undecided page: {key}')
  d=json.loads(dp.read_text());expected.append(O/'pages'/d['filename'])
  if not any(s.startswith(f"scan {int(m['our_scan']):03d} done ") and f"cote {m['cote']}" in s for s in log):raise SystemExit(f'Page not marked done: {key}')
  for r in ['R1','R2','R3']:
   for f in ['reading.tex','report.json']:
    if not (O/'readers'/key/r/f).exists():raise SystemExit(f'Missing reader return: {key}/{r}/{f}')
   if not any((O/'readers'/key/r/('inspection_log.'+ext)).is_file() for ext in ['md','txt','json']):raise SystemExit(f'Missing reader inspection log: {key}/{r}')
 if len(expected)!=29 or len(set(expected))!=29:raise SystemExit('The expected page map must contain exactly 29 distinct pages.')
 if set(expected)!=set((O/'pages').glob('*.tex')):raise SystemExit('Page file set differs from expected 29-page set.')
 review=O/'notation_consistency_review.md'
 if not review.exists():raise SystemExit('The cross-page notation review has not been recorded.')
 v=json.loads((O/'validation.json').read_text())
 if v['errors']:raise SystemExit('Structural validation has outstanding errors.')
 return expected+[O/(ID+'_transcription.tex')]

ap=argparse.ArgumentParser();ap.add_argument('operation',choices=['freeze','package']);a=ap.parse_args()
frozen=O/'transcription_sha256.json'
if a.operation=='freeze':
 if frozen.exists():raise SystemExit('Already frozen; do not overwrite the freeze record.')
 subprocess.run([sys.executable,str(O/'scripts/build_deliverables.py')],check=True)
 subprocess.run([sys.executable,str(O/'scripts/validate.py')],check=True)
 files=prerequisites();stamp=now()
 hashes={str(p.relative_to(O)):digest(p) for p in files}
 frozen.write_text(json.dumps({'frozen_utc':stamp,'sha256':hashes},indent=2)+'\n')
 with (O/'progress.log').open('a') as f:
  f.write('transcription frozen '+stamp+'\n')
  for name,h in hashes.items():f.write(h+'  '+name+'\n')
 print(json.dumps({'frozen':len(hashes),'utc':stamp}))
else:
 dest=O.parent/'deliverables'
 zpath=dest/(ID+'.zip')
 if zpath.exists():raise SystemExit('Final ZIP already exists; do not overwrite without reviewing its provenance.')
 files=prerequisites()
 if not frozen.exists():raise SystemExit('Freeze the completed transcription first.')
 fr=json.loads(frozen.read_text())
 for name,h in fr['sha256'].items():
  if digest(O/name)!=h:raise SystemExit('Frozen transcription changed: '+name)
 if set(fr['sha256'])!={str(p.relative_to(O)) for p in files}:raise SystemExit('Freeze file set mismatch.')
 packaged=[p for p in O.rglob('*') if include_in_package(p)]
 packaged_names={str(p.relative_to(O)) for p in packaged}
 records=json.loads((O/'checkpoint_records.json').read_text()) if (O/'checkpoint_records.json').exists() else []
 missing=[]
 for rec in records:
  for name in rec['files']:
   if name not in packaged_names:missing.append(name)
 if missing:raise SystemExit('Documentation named in checkpoint is missing from final package selection: '+repr(sorted(set(missing))))
 with (O/'progress.log').open('a') as f:f.write('transcription hashes unchanged '+now()+'; all 29 pages and combined fragment verified against frozen SHA-256 values\n')
 manifest=O/'final_manifest.json'
 manifest.write_text(json.dumps({'packaged_utc':now(),'pages':29,'files':[str(p.relative_to(O)) for p in sorted(packaged) if p!=manifest],'source_attachments_included':False,'frozen_transcription_verified':True},indent=2)+'\n')
 if manifest not in packaged:packaged.append(manifest)
 dest.mkdir(exist_ok=True)
 with zipfile.ZipFile(zpath,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in sorted(packaged):z.write(p,p.relative_to(O))
 with zipfile.ZipFile(zpath) as z:
  bad=z.testzip()
  if bad:raise SystemExit('ZIP CRC verification failed: '+bad)
 print(json.dumps({'file':str(zpath),'bytes':zpath.stat().st_size,'sha256':digest(zpath),'entries':len(packaged)}))
