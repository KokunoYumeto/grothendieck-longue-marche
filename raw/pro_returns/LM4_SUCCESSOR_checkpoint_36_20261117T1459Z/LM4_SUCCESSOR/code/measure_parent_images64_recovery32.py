"""Measure the actual 64MiB ZIP-LZMA image stream without creating any ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,time
sys.path.insert(0,str(Path(__file__).resolve().parent))
from checkpoint_data_tar import DataLZMACompressor
root=Path(__file__).resolve().parents[1]
source=root/'verification_images.tar'
start=time.monotonic()
c=DataLZMACompressor(); h=hashlib.sha256(); raw_h=hashlib.sha256(); n=0; raw=0; head=b''
with source.open('rb') as stream:
 for block in iter(lambda:stream.read(4*1024*1024),b''):
  raw+=len(block);raw_h.update(block);out=c.compress(block)
  if len(head)<13:head=(head+out)[:13]
  n+=len(out);h.update(out)
 out=c.flush();n+=len(out);h.update(out)
r=dict(measured_at=datetime.now(timezone.utc).isoformat(),source='restored immutable31 image TAR',raw_bytes=raw,raw_sha256=raw_h.hexdigest(),compressed_bytes=n,compressed_stream_sha256=h.hexdigest(),stream_header_hex=head.hex(),dictionary_bytes=64*1024*1024,elapsed_seconds=time.monotonic()-start,new_zip_created=False,scope='Measured parent-image stream only; later incremental images require a conservative raw-byte allowance.')
out=root/'records/environment_recovery32/parent_images64_actual_measurement.json'
assert not out.exists();out.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r),flush=True)
