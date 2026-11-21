#!/usr/bin/env python3
"""Bind a completed full RGBA verification run to source/output byte hashes.
Usage: script SOURCE_SNAPSHOT COMPLETED_STAGE RECEIPT_JSON
"""
from pathlib import Path
import hashlib,json,sys
source,stage,receipt=map(Path,sys.argv[1:4]);info=json.loads(receipt.read_text());assert info['all_pixels_identical'] and info['under_gateway_limit']
records=json.loads((stage/'evidence_encoding.json').read_text());base=Path(__file__).resolve().parent;dest=base/'image_certificates.json'
data=json.loads(dest.read_text()) if dest.exists() else {'sources':{},'encodings':{},'origins':[]}
for r in records:
 assert r['pixels_identical'];src=source/r['source_file'];out=stage/r['archive_file']
 sh=hashlib.sha256(src.read_bytes()).hexdigest();eh=hashlib.sha256(out.read_bytes()).hexdigest();meta={'rgba_sha256':r['rgba_sha256'],'width':r['width'],'height':r['height'],'origin_archive_sha256':info['sha256']}
 data['sources'][sh]=meta
 if out.suffix=='.jxl':data['encodings'][eh]=meta
origin={'archive':info['archive'],'archive_sha256':info['sha256'],'source':str(source),'images':len(records),'basis':'The completed packaging run compared each decoded RGBA byte string with its immutable source; the unchanged source and encoded files are bound here by SHA-256.'}
if origin not in data['origins']:data['origins'].append(origin)
tmp=dest.with_suffix('.tmp');tmp.write_text(json.dumps(data,indent=2)+'\n');tmp.replace(dest)
print(json.dumps({'certificates':str(dest),'sources':len(data['sources']),'encodings':len(data['encodings'])}))
