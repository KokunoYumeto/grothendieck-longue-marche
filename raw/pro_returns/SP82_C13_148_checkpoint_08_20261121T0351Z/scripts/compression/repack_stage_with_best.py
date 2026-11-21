#!/usr/bin/env python3
"""Repack a complete immutable stage with smaller, verified cached JXL files.
Usage: script source_snapshot existing_stage new_output_dir archive_basename
The original stage and all earlier ZIPs remain untouched.
"""
from pathlib import Path
from PIL import Image
import hashlib,json,shutil,subprocess,sys,zipfile
if len(sys.argv)!=5:raise SystemExit(__doc__)
source,old,dest=map(lambda x:Path(x).resolve(),sys.argv[1:4]);name=sys.argv[4]
assert source.is_dir() and old.is_dir() and not dest.exists() and name.endswith('.zip')
base=Path(__file__).resolve().parent;best=base.parent/'jxl_best_evidence_cache';records=json.loads((old/'evidence_encoding.json').read_text());chosen=[]
for r in records:
 candidate=best/(r['rgba_sha256']+'.jxl');current=old/r['archive_file']
 if current.suffix!='.jxl' or not candidate.is_file() or candidate.stat().st_size>=current.stat().st_size:continue
 rgba=Image.open(source/r['source_file']).convert('RGBA').tobytes();assert hashlib.sha256(rgba).hexdigest()==r['rgba_sha256']
 dec=subprocess.run(['ffmpeg','-v','error','-nostdin','-i',str(candidate),'-f','rawvideo','-pix_fmt','rgba','-threads','1','pipe:1'],check=True,stdout=subprocess.PIPE).stdout
 assert dec==rgba,r['source_file']
 chosen.append({'source_file':r['source_file'],'archive_file':r['archive_file'],'cache':str(candidate),'old_bytes':current.stat().st_size,'new_bytes':candidate.stat().st_size,'rgba_sha256':r['rgba_sha256'],'pixels_identical':True})
# The exact size is checked after packing; do not mutate any prior stage.
stage=dest/'stage';shutil.copytree(old,stage)
lookup={r['source_file']:r for r in chosen}
for r in records:
 if r['source_file'] in lookup:
  new=lookup[r['source_file']];shutil.copy2(new['cache'],stage/r['archive_file']);r['archive_bytes']=new['new_bytes'];r['lossless_tuning']=json.loads((base/'cache_tuned'/(r['rgba_sha256']+'.json')).read_text())['tune']
(stage/'evidence_encoding.json').write_text(json.dumps(records,indent=2)+'\n')
(stage/'lossless_cache_repack.json').write_text(json.dumps({'source_stage':str(old),'results':chosen,'all_pixels_identical':True},indent=2)+'\n')
extras=stage/'scripts/compression';extras.mkdir(parents=True,exist_ok=True)
for n in ['repack_stage_with_best.py','jxl_effort_shim.c','build_best_cache.py','COMPRESSION_WORKFLOW.md']:
 shutil.copy2(base/n,extras/n)
with (stage/'EVIDENCE_ENCODING.md').open('a') as f:f.write('\nSelected JPEG XL files use further lossless frame-option tuning, recorded in lossless_cache_repack.json. Every changed image was decoded and compared byte for byte against the immutable source again. All pixels and dimensions are identical. See scripts/compression/COMPRESSION_WORKFLOW.md for the exact parameter values.\n')
for p in old.rglob('*'):
 if p.is_file():
  q=stage/p.relative_to(old);assert q.is_file()
  if p.suffix=='.tex' or p.name.endswith(('_first.tsv','_second.tsv','_comparison.tsv','_token_differences.tsv')):assert p.read_bytes()==q.read_bytes(),p
archive=dest/name
with zipfile.ZipFile(archive,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(stage.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(stage))
with zipfile.ZipFile(archive) as z:assert z.testzip() is None
receipt={'archive':str(archive),'bytes':archive.stat().st_size,'under_gateway_limit':archive.stat().st_size<536870912,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'smaller_verified_images':len(chosen),'bytes_saved':sum(r['old_bytes']-r['new_bytes'] for r in chosen)}
(dest/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True)
