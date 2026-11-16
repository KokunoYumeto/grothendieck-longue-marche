#!/usr/bin/env python3
"""Compare the WHOLE paused GMP run to the immutable prefix of nativev6.

The new trace may append after the compared prefix. No hash of its growing
gzip wrapper is claimed. The entire old gzip is closed and checked to EOF.
"""
from pathlib import Path
import datetime,gzip,hashlib,json,time
B=Path(__file__).resolve().parent
old=B/'pbc_native_smallmod_v1_iterated_trace.jsonl.gz'
new=B/'pbc_native_smallmod_v2_iterated_trace.jsonl.gz'
assert Path(str(old)+'.pause').exists()
started=time.time();h=hashlib.sha256();count=records=0
with gzip.open(old,'rb') as a,gzip.open(new,'rb') as b:
 for data in iter(lambda:a.read(1<<20),b''):
  expected=b.read(len(data));assert data==expected,('mismatching prefix at or after byte',count)
  h.update(data);count+=len(data);records+=data.count(b'\n')
def sha(p):
 x=hashlib.sha256()
 with p.open('rb') as f:
  for data in iter(lambda:f.read(1<<20),b''):x.update(data)
 return x.hexdigest()
report={'PASS':True,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'paused_original':old.name,'new_append_only_trace':new.name,
 'entire_paused_payload_bytes':count,'entire_paused_payload_records':records,
 'entire_paused_payload_sha256':h.hexdigest(),'paused_gzip_sha256':sha(old),
 'paused_gzip_bytes':old.stat().st_size,'native_v5_source_sha256':sha(B/'pbc_native_modular_v5.cpp'),
 'native_v6_source_sha256':sha(B/'pbc_native_modular_v6.cpp'),
 'native_v6_executable_sha256':sha(B/'pbc_native_modular_v6'),
 'input_sha256':sha(B/'pbc_native_smallmod_v1_iterated.dat'),
 'seconds':time.time()-started,
 'scope':'Every original GMP proof byte is the corresponding nativev6 fast-path byte. This validates the arithmetic optimization on the actual source; C31 remains OPEN.'}
(B/'pbc_native_smallmod_v1_v2_prefix_validation.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2),flush=True)
