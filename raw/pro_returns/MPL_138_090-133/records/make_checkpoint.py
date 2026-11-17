"""Hourly all-work ZIP; never includes supplied scans/context or earlier ZIPs."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import json,zipfile,sys,time,re
root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1]); start=datetime(2026,11,17,21,48,48,tzinfo=timezone.utc)
due=start+timedelta(hours=number)
delay=(due-datetime.now(timezone.utc)).total_seconds()
if delay>60: raise SystemExit('Checkpoint is not yet due; rerun in the scheduled hour.')
if delay>0: time.sleep(delay)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
log=root/'progress.log'
with log.open('a') as f:f.write(f'checkpoint {number:02d} prepared {stamp}\n')
audits=re.findall(r'^scan (\d+) audited',log.read_text(),re.M)
state={'checkpoint':number,'prepared_utc':stamp,'first_pass_pages':43,'audited_scans':audits,'context_contents_opened': 'context opened ' in log.read_text(),'transcription_frozen': 'transcription frozen ' in log.read_text(),'next_checkpoint_due_utc':(due+timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S UTC')}
(root/'records'/'checkpoint_status.json').write_text(json.dumps(state,indent=2)+'\n')
(root/'records'/'RESUME.md').write_text('''# Recovery instructions\n\nUse the original attached prompt and scan ZIPs. Do not run first-pass write scripts over audited pages. Root has personally viewed every whole scan and both halves, in order, without OCR; all 43 first-pass page files exist. The progress log identifies the audited prefix. Complete the second visual audit, reconcile the notation/doubts, combine the fragments and freeze their SHA-256 hashes before opening context. The context contents remain sealed unless the progress log explicitly records opening after the freeze. Research leads are provisional, not mathematical checks. CHECK_EVENTS.tsv is the check ledger. The TeX compile attempt failed before page parsing because this environment lacks the format/packages; mechanical validation is distinct from successful compilation.\n\nCheckpoint ZIPs contain all current deliverables and documentation, without supplied scans/context and without earlier checkpoint ZIPs. Upload receipt is recorded in the working progress log after upload and appears in the next/final archive.\n''')
out=root.parent/f'MPL_138_090-133_checkpoint_{number:02d}.zip'
if out.exists():raise SystemExit('Refusing to overwrite checkpoint')
files=[p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.zip'}]
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for p in sorted(files):z.write(p,p.relative_to(root))
print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'files':len(files),'audited_pages':len(audits),'prepared_utc':stamp}))
