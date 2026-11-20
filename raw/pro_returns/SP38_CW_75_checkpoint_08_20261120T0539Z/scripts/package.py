from pathlib import Path
from datetime import datetime,timezone,timedelta
import zipfile,argparse,json,hashlib
out=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('kind',choices=['checkpoint','final']);a=p.parse_args()
dest=out.parent/'deliverables';dest.mkdir(exist_ok=True)
now=datetime.now(timezone.utc);stamp=now.strftime('%Y-%m-%d %H:%M:%S UTC')
if a.kind=='checkpoint':
 existing=list(dest.glob('SP38_CW_75_checkpoint_*.zip'))
 nums=[int(x.stem.rsplit('_',1)[1]) for x in existing]
 for saved in (out/'checkpoints').glob('checkpoint_*_*.json'):
  try:nums.append(int(saved.name.split('_')[1]))
  except (ValueError,IndexError):pass
 num=max(nums,default=0)+1
 name=f'SP38_CW_75_checkpoint_{num:02d}.zip'
 start=datetime.strptime((out/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
 due=start+timedelta(minutes=45*num)
 if now<due:raise SystemExit('Not due before '+due.strftime('%Y-%m-%d %H:%M:%S UTC'))
else:name='SP38_CW_75.zip';num=None
target=dest/name
if target.exists():raise SystemExit('Refusing to overwrite existing deliverable '+str(target))
completed=[int(p.stem[4:]) for p in sorted((out/'records').glob('scan*.json'))]
active=[p.name for p in sorted((out/'readings').glob('scan*')) if int(p.name[4:]) not in completed and any(q.is_file() for q in p.rglob('*'))]
(out/'WORK_STATE.md').write_text('# Work state\n\nUpdated '+stamp+'.\n\nCommitted scans: '+', '.join(f'{n:03d}' for n in completed)+'.\n\nCurrent uncommitted scan directories: '+(', '.join(active) or 'none')+'. Only pages/ and records/ are adjudicated. Partial reader files are preserved as work in progress, not final decisions.\n\n## Recovery and method\n\nRestore this ZIP into out/ and reacquire the original attached source ZIP. The original input is SP38_CW_75.zip, supplied with PROMPT(20261119-225751).md; the final output intentionally has the same basename but is a new file. Original scans and witness files are not copied into this archive. Run scripts/rebuild_packets.py after restoring the input source folder; it derives its workspace path and only rebuilds packets. See RECOVERY.md. Do not rerun the historical setup_work.py over restored work.\n\nProceed scan by scan through 025. Use three fresh, independent fork_turns=none readers per page with the latest brief and notation snapshot; no OCR or outside research. Main adjudicates all differences on crops, records all C doubt dispositions and S decisions, and commits before starting another page. If active reader contexts are lost, preserve their incomplete attempts and restart that uncommitted page with three fresh readers; never call incomplete reports independent completed readings.\n\nThe progress clock began 2026-11-19 23:00:18 UTC. Checkpoints are due every 45 minutes from that time, uniquely numbered, without earlier ZIPs nested. CHECK_EVENTS.tsv includes preliminary checks for uncommitted pages via pending_events/. Final work requires structural verification, all 24 page hashes plus combined-text hash, a transcription-frozen log entry, and a final hash comparison. No LaTeX compilation was requested.\n')
with (out/'progress.log').open('a') as f:f.write(f'{a.kind} packaged {stamp} {name}\n')
files=sorted(f for f in out.rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.suffix!='.pyc')
manifest={'archive':name,'snapshot_utc':stamp,'completed_scans':completed,'uncommitted':active,'files':[]}
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:
  data=f.read_bytes();rel=str(f.relative_to(out));z.writestr(rel,data)
  manifest['files'].append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
 if num is not None:
  mp=out/'checkpoints'/f'checkpoint_{num:02d}_manifest.json';mp.parent.mkdir(exist_ok=True)
  mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n');z.write(mp,mp.relative_to(out))
print(json.dumps({'path':str(target),'bytes':target.stat().st_size,'files':len(files)+(num is not None),'time':stamp}))
