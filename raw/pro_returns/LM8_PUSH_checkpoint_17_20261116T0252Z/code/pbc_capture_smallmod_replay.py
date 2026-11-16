#!/usr/bin/env python3
"""Retain all source leaves of a CLOSED, paused native small-modulus log.

Reads the stable live file only after a valid-gzip pause acknowledgement,
makes an immutable copy outside the deliverable, and records both wrapper
and decompressed hashes. No active gzip stream is accepted.
"""
from pathlib import Path
import gzip,hashlib,json,shutil,time
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT.parent/'checkpoint11_smallmod_replay';OUT.mkdir(exist_ok=True)
ENTRY='code/pbc_native_smallmod_v2_iterated_trace.jsonl.gz'
original=ROOT/ENTRY
assert Path(str(original)+'.pause').exists()
log=(ROOT/'code/pbc_native_smallmod_v2_iterated.out').read_text()
assert log.rfind('native_checkpoint_PAUSED_valid_gzip_footer')>log.rfind('native_checkpoint_RESUMED_new_gzip_member')
snapshot=OUT/'pbc_native_smallmod_v2_capture.jsonl.gz'
if snapshot.exists():raise SystemExit('Refusing to overwrite immutable capture')
shutil.copyfile(original,snapshot)
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):h.update(b)
 return h.hexdigest()
wrapper_hash=sha(snapshot);assert wrapper_hash==sha(original)
rawpath=OUT/'pbc_smallmod_v2_original_source_lines.jsonl';rows=OUT/'pbc_smallmod_v2_identity_rows.dat'
h=hashlib.sha256();records=identities=rawcount=size=0;start=time.time()
with gzip.open(snapshot,'rb') as f,rawpath.open('wb') as out,rows.open('w') as data:
 for line in f:
  assert line.endswith(b'\n');h.update(line);size+=len(line);records+=1
  if line.startswith((b'["sub",',b'["mul",',b'["neg",')):continue
  r=json.loads(line);assert r[0] in ('source','leaf','success','failure'),r[0]
  out.write(line);rawcount+=1
  if r[0]=='leaf' and r[2]=='identity':
   identities+=1;data.write(str(len(r[3]))+' '+' '.join(map(str,r[3]))+' '+str(len(r[4]))+' '+' '.join(map(str,r[4]))+'\n')
m={'original_snapshot':str(snapshot),'original_entry':ENTRY,
 'original_sha256':wrapper_hash,'original_bytes':snapshot.stat().st_size,
 'decoded_sha256':h.hexdigest(),'decoded_bytes':size,'original_records':records,
 'identity_rows':identities,'retained_raw_records':rawcount,
 'source_lines':rawpath.name,'source_lines_sha256':sha(rawpath),'source_lines_bytes':rawpath.stat().st_size,
 'identity_data':rows.name,'identity_data_sha256':sha(rows),
 'source_dat':'code/pbc_native_smallmod_v1_iterated.dat',
 'replay_source':'code/pbc_trace_replay_smallmod.cpp','replay_executable':'code/pbc_trace_replay_smallmod',
 'capture_seconds':time.time()-start,'verified':False,
 'status':'Preparation only. Entire captured-byte replay must pass. C31 remains OPEN.'}
(OUT/'pbc_smallmod_v2_replay_manifest.json').write_text(json.dumps(m,indent=2)+'\n')
print(json.dumps(m,indent=2),flush=True)
