"""Losslessly encode PNG payloads for an immutable ZIP transport copy.
The restored PNG must match its original SHA256 byte for byte, or it stays PNG.
No source images, readings, or previously written archives are changed.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
from PIL import Image
import io,os,json,hashlib,subprocess,tempfile,zipfile,sys,time
BASE=Path(__file__).resolve().parents[2]
CACHE=BASE/'archive_lossless_cache';CACHE.mkdir(exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
RESTORE=r'''from pathlib import Path
from PIL import Image
import subprocess,hashlib,io,json,sys
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'CROP_COMPRESSION_MANIFEST.json').read_text())
selected=sys.argv[1:]
for r in m['crops']:
 if r['encoding']!='JPEG XL lossless':continue
 if selected and not any(s in r['original_path'] for s in selected):continue
 out=root/r['original_path']
 if out.exists():
  assert hashlib.sha256(out.read_bytes()).hexdigest()==r['original_sha256'],out
  continue
 src=root/r['archived_path'];assert hashlib.sha256(src.read_bytes()).hexdigest()==r['archived_sha256']
 raw=subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',str(src),'-f','rawvideo','-pix_fmt',r['pixel_format'],'pipe:1'],check=True,capture_output=True).stdout
 assert hashlib.sha256(raw).hexdigest()==r['pixel_sha256'],src
 im=Image.frombytes(r['mode'],tuple(r['size']),raw);b=io.BytesIO();im.save(b,format='PNG',**r['png_save_parameters'])
 assert hashlib.sha256(b.getvalue()).hexdigest()==r['original_sha256'],out
 out.parent.mkdir(parents=True,exist_ok=True);out.write_bytes(b.getvalue())
 print(out.relative_to(root))
print('All selected PNGs restored and verified byte for byte.')
'''
README='''# Lossless crop storage\n\nThe upload service limits one file to 512 MiB. This ZIP therefore stores eligible PNG crops as lossless JPEG XL (`.jxl`). Every original crop is included; none was resized, discarded, sharpened again, or changed in colour. All text and all frozen reading TSVs are byte-for-byte unchanged. Earlier checkpoint ZIPs were not changed.\n\n`CROP_COMPRESSION_MANIFEST.json` maps each original PNG name in the contemporary records to its archived image. It records both file hashes and the decoded pixel hash. Each converted crop was decoded and its original PNG regenerated; conversion was accepted only when the regenerated PNG matched the original PNG SHA-256 exactly. Any PNG that could not be reproduced exactly was retained as PNG. Thus this archive contains all data needed to recover every original crop file without the source scans.\n\nTo restore the PNG names used in the logs, from this extracted directory run:\n\n```sh\npython scripts/restore_crops.py\n```\n\nThis requires Python, Pillow and FFmpeg with JPEG XL decoding. To restore one page or crop, append a filename fragment, for example `148_scan053`. Existing PNGs are checked and never overwritten with a different file. JPEG XL images can also be opened directly by compatible image viewers. The original PNG encodings were produced with Pillow; if another Pillow/zlib version produces different bytes, the restoration assertion deliberately stops instead of claiming a matching file. The JPEG XL pixels themselves remain exact and are independently verified.\n'''
def encode(item):
 name,data=item;h=sha(data);meta=CACHE/(h+'.json');enc=CACHE/(h+'.jxl')
 if meta.exists():
  r=json.loads(meta.read_text())
  if r['encoding']=='original PNG':return name,data,r
  if enc.exists() and sha(enc.read_bytes())==r['archived_sha256']:return name,enc.read_bytes(),r
 im=Image.open(io.BytesIO(data));im.load();mode=im.mode
 fallback={'encoding':'original PNG','original_sha256':h,'archived_sha256':h,'mode':mode,'size':list(im.size)}
 if mode not in ('RGB','RGBA','L'):
  meta.write_text(json.dumps(fallback));return name,data,fallback
 fmt={'RGB':'rgb24','RGBA':'rgba','L':'gray'}[mode]
 raw=im.tobytes();params=None
 for candidate in ({},{'optimize':True},{'compress_level':9},{'compress_level':1}):
  b=io.BytesIO();im.save(b,format='PNG',**candidate)
  if b.getvalue()==data:params=candidate;break
 if params is None:
  meta.write_text(json.dumps(fallback));return name,data,fallback
 with tempfile.TemporaryDirectory(dir=CACHE) as td:
  src=Path(td)/'source.png';dst=Path(td)/'crop.jxl';src.write_bytes(data)
  subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',str(src),'-c:v','libjxl','-distance','0','-effort','9',str(dst)],check=True,capture_output=True)
  out=dst.read_bytes()
  check=subprocess.run(['ffmpeg','-hide_banner','-loglevel','error','-i',str(dst),'-f','rawvideo','-pix_fmt',fmt,'pipe:1'],check=True,capture_output=True).stdout
  if check!=raw:raise RuntimeError('Lossless pixel verification failed: '+name)
  rebuilt=io.BytesIO();Image.frombytes(mode,im.size,check).save(rebuilt,format='PNG',**params)
  if rebuilt.getvalue()!=data:raise RuntimeError('Exact PNG recovery failed: '+name)
 if len(out)>=len(data):meta.write_text(json.dumps(fallback));return name,data,fallback
 r={'encoding':'JPEG XL lossless','original_sha256':h,'archived_sha256':sha(out),'mode':mode,'size':list(im.size),'pixel_format':fmt,'pixel_sha256':sha(raw),'png_save_parameters':params,'exact_png_reconstruction_verified':True}
 enc.write_bytes(out);meta.write_text(json.dumps(r));return name,out,r
if __name__=='__main__':
 src=Path(sys.argv[1]);dst=Path(sys.argv[2]);assert not dst.exists(),dst
 dst.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(src) as z:items=[(i.filename,z.read(i.filename)) for i in z.infolist()]
 png=[(n,b) for n,b in items if n.lower().endswith('.png')];other=[(n,b) for n,b in items if not n.lower().endswith('.png')]
 results={};start=time.monotonic()
 with ThreadPoolExecutor(max_workers=4) as ex:
  fs=[ex.submit(encode,item) for item in png]
  for i,f in enumerate(as_completed(fs),1):
   n,b,r=f.result();results[n]=(b,r)
   if i%25==0 or i==len(png):print(json.dumps({'images_encoded':i,'total':len(png),'seconds':round(time.monotonic()-start)}),flush=True)
 manifest={'source_archive':src.name,'source_archive_sha256':sha(src.read_bytes()),'purpose':'Lossless transport encoding only; original PNGs exactly recoverable','crops':[]}
 with zipfile.ZipFile(dst,'x',zipfile.ZIP_DEFLATED,compresslevel=9,allowZip64=True) as z:
  for n,b in other:z.writestr(n,b)
  for n in sorted(results):
   b,r=results[n];an=str(Path(n).with_suffix('.jxl')) if r['encoding']=='JPEG XL lossless' else n
   z.writestr(an,b);manifest['crops'].append(dict(original_path=n,archived_path=an,**r))
  z.writestr('CROP_COMPRESSION_MANIFEST.json',json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
  z.writestr('CROPS_README.md',README)
  z.writestr('scripts/restore_crops.py',RESTORE)
  if not any(n=='scripts/compact_archive.py' for n,b in other):z.writestr('scripts/compact_archive.py',Path(__file__).read_bytes())
 print(json.dumps({'path':str(dst.resolve()),'size':dst.stat().st_size,'sha256':sha(dst.read_bytes()),'original_images':len(png),'lossless_jxl':sum(r['encoding']=='JPEG XL lossless' for b,r in results.values())}),flush=True)
