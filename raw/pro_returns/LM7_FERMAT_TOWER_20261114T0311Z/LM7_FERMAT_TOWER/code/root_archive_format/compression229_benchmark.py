#!/usr/bin/env python3
"""Measure lossless standard-ZIP codecs on every substantial text/data member."""
from pathlib import Path
import bz2, hashlib, json, time, zipfile

ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'LM7_FERMAT_TOWER.zip'
OUT=Path(__file__).with_suffix('.json')
SUFFIXES={'.json','.bin','.out','.tex','.md','.txt','.csv','.log','.aux','.py','.gp'}
def digest(b): return hashlib.sha256(b).hexdigest()
started=time.monotonic()
rows=[]
with zipfile.ZipFile(ARCHIVE) as z:
    infos=z.infolist()
    candidates=[i for i in infos if Path(i.filename).suffix in SUFFIXES and i.file_size>=65536]
    for j,i in enumerate(candidates):
        raw=z.read(i)
        b=bz2.compress(raw,compresslevel=9)
        assert bz2.decompress(b)==raw
        l=zipfile.LZMACompressor()
        lz=l.compress(raw)+l.flush()
        assert zipfile.LZMADecompressor().decompress(lz)==raw
        choices={'existing':i.compress_size,'bzip2':len(b),'lzma':len(lz)}
        best=min(choices,key=choices.get)
        rows.append({'member':i.filename,'bytes':len(raw),'sha256':digest(raw),
                     'original_method':i.compress_type,'compressed_bytes':choices,
                     'best':best,'savings_bytes':i.compress_size-choices[best],
                     'complete_roundtrip_byte_identity':True})
        if (j+1)%100==0: print(json.dumps({'processed':j+1,'total':len(candidates),'savings_bytes':sum(r['savings_bytes'] for r in rows)}),flush=True)
result={'status':'PASS','archive_sha256':digest(ARCHIVE.read_bytes()),
        'archive_bytes':ARCHIVE.stat().st_size,'candidate_count':len(rows),
        'candidate_raw_bytes':sum(r['bytes'] for r in rows),
        'standard_ZIP_methods':{'deflate':8,'bzip2':12,'lzma':14},
        'savings_bytes':sum(r['savings_bytes'] for r in rows),
        'projected_existing_archive_bytes':ARCHIVE.stat().st_size-sum(r['savings_bytes'] for r in rows),
        'all_new_codec_roundtrips_complete_byte_identity':True,
        'elapsed_seconds':time.monotonic()-started,'members':rows}
OUT.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='members'},indent=2))
