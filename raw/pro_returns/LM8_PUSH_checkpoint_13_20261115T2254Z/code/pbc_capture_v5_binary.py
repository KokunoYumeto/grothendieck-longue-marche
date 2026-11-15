#!/usr/bin/env python3
"""Capture one paused valid native trace, then losslessly encode that capture.

The auxiliary local ZIP is an immutable input container, not a delivered
checkpoint. The full checkpoint assembler retains its input hash/provenance.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,zipfile
import pbc_binary_checkpoint09 as codec
BASE=Path(__file__).resolve().parents[1];name='code/pbc_native_modular_v5_iterated_trace.jsonl.gz';src=BASE/name
assert Path(str(src)+'.pause').exists(),'capture requires the acknowledged valid-footer pause'
dest=BASE.parent/'pbc_v5_capture_20261115_1938.zip'
if dest.exists():raise SystemExit('Refusing to overwrite existing capture')
outdir=BASE.parent/'checkpoint10_binary';outdir.mkdir(exist_ok=True)
h=hashlib.sha256();prefix=hashlib.sha256();count=0;prefix_length=108803164
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_STORED) as z:
 with src.open('rb') as f,z.open(name,'w',force_zip64=True) as out:
  for b in iter(lambda:f.read(1<<20),b''):
   if count<prefix_length:prefix.update(b[:prefix_length-count])
   h.update(b);count+=len(b);out.write(b)
 row={'path':name,'bytes':count,'sha256':h.hexdigest()}
 z.writestr('PACKAGE_MANIFEST.json',json.dumps({'files':[row]},indent=2)+'\n')
assert prefix.hexdigest()=='d6f6603fc702b8276587092e29539f6af9b2e75690168fe3b63bcb96f8a7deda'
provenance={'captured_utc':datetime.now(timezone.utc).isoformat(),'source':str(src),'input_container':str(dest),
 'source_bytes':count,'source_sha256':h.hexdigest(),'paused_proof_nodes':20689235,
 'previous09_compressed_prefix_bytes':prefix_length,'previous09_compressed_prefix_sha256':prefix.hexdigest(),
 'live_basis_preserved':True,'status':'C31 remains OPEN; complete proof-record snapshot, not a proof certificate.'}
(outdir/'pbc_v5_capture_manifest.json').write_text(json.dumps(provenance,indent=2)+'\n')
print(json.dumps({'CAPTURED':provenance}),flush=True)
codec.SNAPSHOT=dest;codec.OUT=outdir;codec.original={name:row}
result=codec.convert(name)
(outdir/'binary_conversion_manifest.json').write_text(json.dumps({'capture':provenance,'transforms':[result]},indent=2)+'\n')
