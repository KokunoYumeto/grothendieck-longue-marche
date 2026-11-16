#!/usr/bin/env python3
"""Read-only conservative forecast with exact savings from four PDF deltas."""
from pathlib import Path
import argparse
import hashlib
import json
import zipfile
import zlib

ROOT = Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser()
ap.add_argument('--reserve-mib',type=int,default=8)
args=ap.parse_args()
archive=ROOT.parent/'LM8_PUSH_checkpoint_15.zip'
plan_path=ROOT/'notes/checkpoint16_storage_plan.json'
plan=json.loads((plan_path if plan_path.exists() else ROOT/'notes/checkpoint15_storage_plan.json').read_text())
delta=json.loads((ROOT/'notes/checkpoint16_pdf_delta_encoding.json').read_text())
with zipfile.ZipFile(archive) as z:
    manifest=json.loads(z.read('PACKAGE_MANIFEST.json'))
    encoded_hashes={r['sha256'] for r in delta['rows']}
    replaced=[{'path':e['path'],'compressed_bytes':z.getinfo(e['path']).compress_size}
              for e in manifest['files'] if e['sha256'] in encoded_hashes]
known={e['sha256'] for e in manifest['files']}
skipped={e['original_path'] for key in ('transforms','exact_prefix_reconstructions','superseded_compression_wrappers') for e in plan.get(key,[])}
skipped.update(e['original_path'] for e in delta['transforms'])
excluded=('build/tex-cache/','__pycache__/','background/','inputs/')
metadata={'PACKAGE_MANIFEST.json','CHECKPOINT_COMPRESSION_MAP.json','ORIGINAL_PACKAGE_MANIFEST.json','RESTORE_LARGE_LOGS.py'}
rows=[]
for path in sorted(ROOT.rglob('*')):
    if not path.is_file():continue
    name=path.relative_to(ROOT).as_posix()
    if name in skipped or name in metadata or path.suffix=='.pyc' or any(name.startswith(x) or '/'+x in name for x in excluded):continue
    data=path.read_bytes();digest=hashlib.sha256(data).hexdigest()
    if digest in known:continue
    known.add(digest)
    if name.endswith(('.xz','.gz')):size=len(data)
    else:
        compressor=zlib.compressobj(9,zlib.DEFLATED,-15)
        size=len(compressor.compress(data))+len(compressor.flush())
    rows.append({'path':name,'bytes':len(data),'compressed_bytes':size,'sha256':digest})
extra=sum(r['compressed_bytes']+2*len(r['path'])+100 for r in rows)
saved=sum(r['compressed_bytes'] for r in replaced)
reserve=args.reserve_mib<<20
total=archive.stat().st_size-saved+extra+reserve
record={'scope':'Conservative read-only forecast, retaining prior archive plus new bytes and removing only four exactly verified original PDF encodings; no ZIP created.',
        'previous_archive_bytes':archive.stat().st_size,'superseded_pdf_compressed_bytes_replaced':saved,
        'replaced_pdf_entries':replaced,'new_unique_compressed_bytes_with_header_allowance':extra,
        'future_build_QA_metadata_reserve':reserve,'upper_bound_with_reserve':total,
        'headroom_below_512MiB':536870912-total,'new_unique_files':len(rows),
        'largest_additions':sorted(rows,key=lambda r:r['compressed_bytes'],reverse=True)[:20]}
(ROOT/'notes/checkpoint16_size_preflight.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
