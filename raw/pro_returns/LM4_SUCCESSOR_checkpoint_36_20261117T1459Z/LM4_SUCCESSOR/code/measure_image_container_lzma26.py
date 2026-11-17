"""Measure a lossless storage alternative on the actual prior TAR; create no ZIP."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib
import json
import time
import zipfile

root=Path(__file__).resolve().parents[1]
archive=root.parent/'LM4_SUCCESSOR_checkpoint_25.zip'
assert archive.stat().st_size==511112126
name='LM4_SUCCESSOR/verification_images.tar'
started=datetime.now(timezone.utc).isoformat()
t0=time.monotonic()
compressor=zipfile.LZMACompressor()
source_hash=hashlib.sha256()
compressed_hash=hashlib.sha256()
total=compressed=0
with zipfile.ZipFile(archive) as z:
    info=z.getinfo(name)
    with z.open(name) as stream:
        while block:=stream.read(1024*1024):
            total+=len(block)
            source_hash.update(block)
            result=compressor.compress(block)
            compressed+=len(result)
            compressed_hash.update(result)
    result=compressor.flush()
    compressed+=len(result)
    compressed_hash.update(result)
assert source_hash.hexdigest()=='f62d200e3950bc9db4268ca966899e903c971570195199289ff65a840d7b7680'
record={
 'started_at':started,'completed_at':datetime.now(timezone.utc).isoformat(),
 'seconds':time.monotonic()-t0,'archive':archive.name,'container':name,
 'source_bytes':total,'source_sha256':source_hash.hexdigest(),
 'current_method':info.compress_type,'current_compressed_bytes':info.compress_size,
 'alternative_method':'standard ZIP LZMA','alternative_compressed_bytes':compressed,
 'alternative_compressed_sha256':compressed_hash.hexdigest(),
 'difference_bytes':info.compress_size-compressed,
 'creates_zip':False,'modifies_prior_archive':False,
 'scope':'Exact same original standard-TAR bytes; only a stream compression-size measurement. Any adoption requires a separately preserved packager change and new immutable-capture verification.',
}
(root/'records/checkpoint26_image_compression_measurement.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
