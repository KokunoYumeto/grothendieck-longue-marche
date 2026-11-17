"""Conservative actual-byte estimate for checkpoint28; creates no ZIP."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io
import json
import tarfile
import time
import zipfile
import zlib
from checkpoint_standard_tar import build_standard_tar

root=Path(__file__).resolve().parents[1]
archive=root.parent/'LM4_SUCCESSOR_checkpoint_27.zip'
prefix='LM4_SUCCESSOR/'
digest=lambda data:hashlib.sha256(data).hexdigest()

def included(f):
    r=str(f.relative_to(root))
    if r in {'verification_images.tar','historical_documents.tar'}:return False
    if r.startswith('tex_cache/'):return False
    if r.startswith('work_CE/') and f.parent==root/'work_CE' and (f.name.startswith('D_') or f.name.startswith('LM6_')):return False
    if r.startswith('work_DE/') and f.name.endswith('_source.txt'):return False
    if 'work_CE/sources/' in r and f.suffix.lower() in ['.pdf','.txt']:return False
    if r.startswith('work_DE/') and f.name not in {'B118_initial_spacing.pdf','B122_initial_layout.pdf','B128_initial_comma.pdf'} and not f.with_suffix('.tex').exists() and (f.suffix.lower()=='.pdf' or (f.suffix.lower()=='.txt' and f.with_suffix('.pdf').exists() and f.stem not in ['DE_review','B_separability_review'])):return False
    if '__pycache__' in f.parts or f.suffix in ['.aux','.toc','.blg','.bbl']:return False
    return True

def compressed_size(data,method):
    c=zlib.compressobj(6,zlib.DEFLATED,-15) if method=='deflate' else zipfile.LZMACompressor()
    return len(c.compress(data)+c.flush())

started=datetime.now(timezone.utc)
with zipfile.ZipFile(archive) as z:
    rows=list(csv.DictReader(io.StringIO(z.read(prefix+'records/checkpoint_27_contents_sha256.tsv').decode()),delimiter='\t'))
    old={r['path']:r for r in rows}
    prior={'.png':{},'.pdf':{}}
    removed={}
    for suffix,basename in [('.png','verification_images.tar'),('.pdf','historical_documents.tar')]:
        removed[basename]=z.getinfo(prefix+basename).compress_size
        with tarfile.open(fileobj=io.BytesIO(z.read(prefix+basename)),mode='r:') as tf:
            for member in tf.getmembers():
                stream=tf.extractfile(member)
                assert stream is not None
                prior[suffix][member.name[len(prefix):]]=stream.read()
    prior['.pdf']['LM4_SUCCESSOR_paper.pdf']=z.read(prefix+'LM4_SUCCESSOR_paper.pdf')

bundles={'.png':{},'.pdf':{}}
new_files=[]
for f in sorted(root.rglob('*')):
    if not f.is_file() or not included(f):continue
    rel,data=str(f.relative_to(root)),f.read_bytes()
    suffix=f.suffix.lower()
    if suffix=='.png' or (suffix=='.pdf' and rel!='LM4_SUCCESSOR_paper.pdf'):
        bundles[suffix][rel]=data
        continue
    previous=old.get(rel)
    if previous and len(data)==int(previous['bytes']) and digest(data)==previous['sha256']:continue
    method='deflate' if suffix in {'.pdf','.jpg','.jpeg','.gif','.zip','.gz','.xz','.tar'} else 'lzma'
    new_files.append((compressed_size(data,method),rel))

for suffix,files in prior.items():
    for rel,data in files.items():
        active=root/rel
        if active.is_file() and active.read_bytes()==data and rel!='LM4_SUCCESSOR_paper.pdf':
            bundles[suffix][rel]=data
        else:
            history='checkpoint_history/checkpoint_27/'+rel
            if history in bundles[suffix]:assert bundles[suffix][history]==data
            bundles[suffix][history]=data

bundle_reports={}
for suffix,kind in [('.png','images'),('.pdf','documents')]:
    bundle,metrics=build_standard_tar(sorted(bundles[suffix].items()))
    begin=time.monotonic()
    print('Compressing actual prospective',kind,'TAR',metrics,flush=True)
    size=compressed_size(bundle,'lzma')
    bundle_reports[kind]={'metrics':metrics,'compressed_bytes':size,'compression':'ZIP_LZMA','elapsed_seconds':time.monotonic()-begin}
    print('Completed',kind,'compressed bytes',size,flush=True)

added=sum(n for n,_ in new_files)
estimate=archive.stat().st_size-sum(removed.values())+sum(b['compressed_bytes'] for b in bundle_reports.values())+added
allowance=5_000_000
report={
    'started_at':started.isoformat(),'recorded_at':datetime.now(timezone.utc).isoformat(),
    'baseline_archive':archive.name,'baseline_bytes':archive.stat().st_size,
    'previous_container_compressed_bytes_removed':removed,
    'prospective_bundles':bundle_reports,
    'new_or_changed_nonbundled_files':len(new_files),
    'additional_compressed_payload_bytes':added,
    'estimated_before_allowance':estimate,
    'header_manifest_retention_and_late_text_allowance_bytes':allowance,
    'estimated_total_with_allowance':estimate+allowance,
    'delivery_cap_bytes':536870912,
    'estimated_headroom_bytes':536870912-estimate-allowance,
    'largest_new_compressed_payloads':sorted(new_files,reverse=True)[:15],
    'creates_zip':False,
    'scope':'Actual checkpoint27 baseline with both old containers removed. Complete prospective image and document standard TARs are compressed with the actual ZIP_LZMA compressor. Every earlier PNG/PDF version is retained by original or historical path. Changed nonbundled originals remain conservatively counted in the baseline; the previous main PDF is conservatively counted twice. Five MB covers headers, enlarged retention records and later text. Actual immutable size is checked after scheduled capture.'
}
(root/'records/checkpoint28_size_estimate.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2),flush=True)
assert estimate+allowance<536870912
