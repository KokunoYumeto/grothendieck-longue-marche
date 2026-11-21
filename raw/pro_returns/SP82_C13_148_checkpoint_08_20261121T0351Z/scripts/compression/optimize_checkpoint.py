#!/usr/bin/env python3
"""Losslessly tune crop encodings, then create a complete checkpoint06 archive.
No source, previous archive, or transcription is changed. PNG decoded RGBA
bytes must equal each candidate JPEG XL decoded RGBA before it is accepted.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image
import hashlib,json,os,shutil,subprocess,time,zipfile
ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'work/compression_engineering'
SOURCE=ROOT/'work/checkpoint06_source'
OLD=ROOT/'work/checkpoint06_jxl/stage'
DEST=ROOT/'work/checkpoint06_optimized'
CACHE=BASE/'cache_tuned'
CACHE.mkdir(exist_ok=True)
records=json.loads((OLD/'evidence_encoding.json').read_text())
ordered=sorted(records,key=lambda r:r['archive_bytes'],reverse=True)
TUNE='29:11,26:3,27:15,28:100'

def encode(r):
 start=time.time();source=SOURCE/r['source_file'];im=Image.open(source);rgba=im.convert('RGBA').tobytes();h=hashlib.sha256(rgba).hexdigest();assert h==r['rgba_sha256']
 target=CACHE/(h+'.jxl');meta=CACHE/(h+'.json')
 if not target.exists():
  env=os.environ.copy();env['LD_PRELOAD']=str(BASE/'jxl_tune2_shim.so');env['EVIDENCE_JXL_TUNE']=TUNE
  tmp=target.with_suffix('.tmp.jxl')
  proc=subprocess.run(['ffmpeg','-v','error','-nostdin','-y','-i',str(source),'-c:v','libjxl','-distance','0','-effort','9','-frames:v','1','-threads','2',str(tmp)],env=env,capture_output=True,timeout=1200)
  if proc.returncode:raise RuntimeError(proc.stderr.decode())
  if proc.stderr:raise RuntimeError('Unexpected encoder warning: '+proc.stderr.decode())
  tmp.rename(target)
 decoded=subprocess.run(['ffmpeg','-v','error','-nostdin','-i',str(target),'-f','rawvideo','-pix_fmt','rgba','-threads','1','pipe:1'],check=True,stdout=subprocess.PIPE).stdout
 assert decoded==rgba,source
 result={'source_file':r['source_file'],'archive_file':r['archive_file'],'cache':str(target),'old_bytes':r['archive_bytes'],'new_bytes':target.stat().st_size,'saving':max(0,r['archive_bytes']-target.stat().st_size),'rgba_sha256':h,'pixels_identical':True,'seconds':round(time.time()-start,2),'tune':TUNE}
 meta.write_text(json.dumps(result,indent=2)+'\n');return result

results=[];savings=0;threshold=6_100_000
# Bound the active queue so the checkpoint can be created as soon as its size is safe.
with ThreadPoolExecutor(max_workers=3) as pool:
 it=iter(ordered);pending={pool.submit(encode,next(it)) for _ in range(3)}
 while pending:
  future=next(as_completed(pending));pending.remove(future);r=future.result();results.append(r);savings+=r['saving']
  print(json.dumps({'done':len(results),'saving':savings,'result':r}),flush=True)
  (BASE/'checkpoint06_optimization_progress.json').write_text(json.dumps({'results':results,'total_savings':savings},indent=2)+'\n')
  if savings<threshold:
   try:pending.add(pool.submit(encode,next(it)))
   except StopIteration:pass
print('ENCODING_DONE savings='+str(savings),flush=True)
assert savings>5_000_000,savings
assert not DEST.exists(),DEST
stage=DEST/'stage';shutil.copytree(OLD,stage)
by_source={r['source_file']:r for r in results}
for r in records:
 new=by_source.get(r['source_file'])
 if new and new['saving']:
  shutil.copy2(new['cache'],stage/r['archive_file']);r['archive_bytes']=new['new_bytes'];r['lossless_tuning']=TUNE
(stage/'evidence_encoding.json').write_text(json.dumps(records,indent=2)+'\n')
(stage/'scripts/compression').mkdir(parents=True,exist_ok=True)
for name in ['optimize_checkpoint.py','jxl_effort_shim.c']:
 shutil.copy2(BASE/name,stage/'scripts/compression'/name)
(stage/'lossless_optimization.json').write_text(json.dumps({'basis':'checkpoint06 immutable source and validated lossless stage','options':TUNE,'results':results,'total_savings':savings},indent=2)+'\n')
with (stage/'EVIDENCE_ENCODING.md').open('a') as f:
 f.write('\n## Additional lossless coding search\n\nSelected JPEG XL crops were reencoded using the installed libjxl 0.11 expert API with modular previous-channel prediction 11, group size 1024, modular predictor selection code15, and 100% MA-tree learning. Distance remains zero. Each candidate was decoded to RGBA and compared byte for byte with the immutable source PNG; only smaller, identical candidates replaced the default lossless encoding. No image pixel, dimension, crop rectangle or transcription changed. The C shim and exact encoding workflow are included under scripts/compression; lossless_optimization.json records accepted candidates.\n')
# Assert all verbatim files and all source files continue to be represented.
for p in OLD.rglob('*'):
 if not p.is_file():continue
 q=stage/p.relative_to(OLD);assert q.is_file(),p
 if p.suffix=='.tex' or p.name.endswith(('_first.tsv','_second.tsv','_comparison.tsv','_token_differences.tsv')):assert p.read_bytes()==q.read_bytes(),p
archive=DEST/'SP82_C13_148_checkpoint_06.zip'
with zipfile.ZipFile(archive,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(stage.rglob('*')):
  if p.is_file():z.write(p,p.relative_to(stage))
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None
 assert len(z.namelist())==sum(p.is_file() for p in stage.rglob('*'))
assert archive.stat().st_size<536870912,archive.stat().st_size
receipt={'archive':str(archive),'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'all_pixels_identical':True,'source_images':len(records),'optimized_images':sum(r['saving']>0 for r in results),'total_savings':savings}
(DEST/'receipt.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt),flush=True)
