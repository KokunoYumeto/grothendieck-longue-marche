#!/usr/bin/env python3
"""Preserve an interrupted raw gzip stream and close its complete JSONL prefix.

This repairs only archival framing. It does not fabricate proof records,
complete a proof, or infer mathematical success. Every raw compressed byte
and any decoded partial record are separately retained.
"""
import argparse,gzip,hashlib,json,zlib
from pathlib import Path
ap=argparse.ArgumentParser();ap.add_argument('path',type=Path);args=ap.parse_args()
p=args.path;raw=Path(str(p)+'.incomplete_stream');partial=Path(str(p)+'.partial_record')
assert p.exists() and not raw.exists()
p.rename(raw)
decoder=zlib.decompressobj(16+zlib.MAX_WBITS)
compressed_hash=hashlib.sha256();plain_hash=hashlib.sha256();raw_bytes=0;plain_bytes=0;records=0;carry=b'';last=None
with raw.open('rb') as src,p.open('wb') as dst,gzip.GzipFile(fileobj=dst,mode='wb',compresslevel=1,mtime=0) as out:
    while chunk:=src.read(1<<20):
        raw_bytes+=len(chunk);compressed_hash.update(chunk)
        data=carry+decoder.decompress(chunk)
        cut=data.rfind(b'\n')+1
        full,carry=data[:cut],data[cut:]
        if full:
            out.write(full);plain_hash.update(full);plain_bytes+=len(full);records+=full.count(b'\n')
            last=json.loads(full.splitlines()[-1])
    rest=decoder.flush()
    if rest:carry+=rest
    cut=carry.rfind(b'\n')+1
    if cut:
        full=carry[:cut];out.write(full);plain_hash.update(full);plain_bytes+=len(full);records+=full.count(b'\n');last=json.loads(full.splitlines()[-1]);carry=carry[cut:]
partial.write_bytes(carry)
with gzip.open(p,'rb') as check:
    verify=hashlib.sha256();check_records=0
    for line in check:verify.update(line);check_records+=1
assert verify.hexdigest()==plain_hash.hexdigest() and check_records==records
report={'status':'INCOMPLETE positive-certificate search; valid archived JSONL prefix only',
        'raw_compressed_prefix':str(raw),'raw_compressed_bytes':raw_bytes,
        'raw_compressed_sha256':compressed_hash.hexdigest(),'raw_stream_had_footer':decoder.eof,
        'closed_gzip_prefix':str(p),'closed_gzip_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
        'decoded_complete_record_bytes':plain_bytes,'complete_records':records,
        'complete_record_sha256':plain_hash.hexdigest(),'partial_record':str(partial),
        'partial_record_bytes':len(carry),'partial_record_sha256':hashlib.sha256(carry).hexdigest(),
        'last_record_kind':last[0] if last else None,'last_record_id':last[1] if last else None,
        'all_raw_bytes_retained':True,'no_record_fabricated':True,'success_claimed':False}
Path(str(p)+'.archive.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
