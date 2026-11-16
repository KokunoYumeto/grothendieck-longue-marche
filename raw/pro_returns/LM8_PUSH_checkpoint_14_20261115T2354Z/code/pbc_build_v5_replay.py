#!/usr/bin/env python3
"""Retain every leaf of the immutable 19:38 native-v5 capture.

This prepares a deterministic encoding, not an accepted archive replacement.
Every reconstructed output byte must be compared by the separate verifier.
"""
from pathlib import Path
import gzip,hashlib,json,zipfile
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT.parent/'checkpoint11_replay';OUT.mkdir(exist_ok=True)
SNAP=ROOT.parent/'pbc_v5_capture_20261115_1938.zip'
ENTRY='code/pbc_native_modular_v5_iterated_trace.jsonl.gz'
capture=json.loads((ROOT.parent/'checkpoint10_binary/binary_conversion_manifest.json').read_text())
old=capture['transforms'][0]
rawpath=OUT/'pbc_v5_original_source_lines.jsonl'
rows=OUT/'pbc_v5_identity_rows.dat'
h=hashlib.sha256();records=identities=rawcount=size=0
with zipfile.ZipFile(SNAP) as z,z.open(ENTRY) as packed,gzip.GzipFile(fileobj=packed) as f,rawpath.open('wb') as out,rows.open('w') as data:
 for line in f:
  assert line.endswith(b'\n')
  h.update(line);size+=len(line);records+=1
  if line.startswith((b'["sub",',b'["mul",',b'["neg",')):continue
  r=json.loads(line);assert r[0] in ('source','leaf'),r[0]
  out.write(line);rawcount+=1
  if r[0]=='leaf' and r[2]=='identity':
   identities+=1
   data.write(str(len(r[3]))+' '+' '.join(map(str,r[3]))+' '+str(len(r[4]))+' '+' '.join(map(str,r[4]))+'\n')
assert size==old['decoded_bytes'] and h.hexdigest()==old['decoded_sha256']
def sha(p):
 x=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1<<20),b''):x.update(b)
 return x.hexdigest()
m={'original_snapshot':str(SNAP),'original_entry':ENTRY,
 'original_sha256':old['original_sha256'],'original_bytes':old['original_bytes'],
 'decoded_sha256':h.hexdigest(),'decoded_bytes':size,'original_records':records,
 'identity_rows':identities,'retained_raw_records':rawcount,
 'source_lines':rawpath.name,'source_lines_sha256':sha(rawpath),'source_lines_bytes':rawpath.stat().st_size,
 'identity_data':rows.name,'identity_data_sha256':sha(rows),
 'source_dat':'code/pbc_native_modular_iterated.dat',
 'replay_source':'code/pbc_trace_replay_v5_crt.cpp','replay_executable':'code/pbc_trace_replay_v5_crt',
 'verified':False,'status':'Preparation only. No replay accepted until the entire original payload matches byte for byte. C31 remains OPEN.'}
(OUT/'pbc_v5_replay_manifest.json').write_text(json.dumps(m,indent=2)+'\n')
print(json.dumps(m,indent=2),flush=True)
