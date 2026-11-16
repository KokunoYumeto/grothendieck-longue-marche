#!/usr/bin/env python3
"""Compare every regenerated boundary-log byte to frozen checkpoint09."""
from pathlib import Path
import hashlib,json,subprocess,time,zipfile
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT.parent/'checkpoint10_replay';p=OUT/'pbc_boundary_replay_manifest.json';m=json.loads(p.read_text());start=time.time()
args=[str(ROOT/'code/pbc_trace_replay_boundary'),str(ROOT/m['source_dat']),str(OUT/m['source_lines']),str(OUT/m['identity_data']),str(m['original_records'])]
log=(OUT/'pbc_boundary_replay_verification_native.out').open('w');proc=subprocess.Popen(args,stdout=subprocess.PIPE,stderr=log)
h=hashlib.sha256();count=0;next_progress=50000000
try:
 with zipfile.ZipFile(m['original_snapshot']) as z,z.open(m['original_entry']) as original:
  for b in iter(lambda:proc.stdout.read(1<<20),b''):
   expected=original.read(len(b))
   if b!=expected:
    j=next((j for j,(u,v) in enumerate(zip(b,expected)) if u!=v),min(len(b),len(expected)))
    raise AssertionError(('first byte mismatch',count+j,b[max(0,j-40):j+80],expected[max(0,j-40):j+80]))
   h.update(b);count+=len(b)
   if count>=next_progress:print(json.dumps({'matched_bytes':count,'seconds':time.time()-start}),flush=True);next_progress+=50000000
  assert original.read(1)==b'','replay ended too early'
 assert proc.wait()==0
 assert count==m['original_bytes'] and h.hexdigest()==m['original_sha256']
 log.close();m.update({'verified':True,'entire_original_byte_comparison':True,'replayed_sha256':h.hexdigest(),'replayed_bytes':count,'seconds':time.time()-start,'command':args,
  'replay_source_sha256':hashlib.sha256((ROOT/'code/pbc_trace_replay_boundary.cpp').read_bytes()).hexdigest(),
  'replay_executable_sha256':hashlib.sha256((ROOT/'code/pbc_trace_replay_boundary').read_bytes()).hexdigest()})
 p.write_text(json.dumps(m,indent=2)+'\n');print(json.dumps({'PASS':True,'bytes':count,'sha256':h.hexdigest(),'seconds':m['seconds']}),flush=True)
except BaseException:
 proc.kill();proc.wait();log.close();raise
