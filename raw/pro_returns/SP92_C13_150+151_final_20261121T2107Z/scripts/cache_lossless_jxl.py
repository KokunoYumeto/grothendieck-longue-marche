"""Cache smaller, pixel-verified JPEG XL encodings of existing evidence crops.
No crop, dimension, colour sample or reading is changed. Used only for packaging.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image
import hashlib,subprocess,json,sys
W=Path(__file__).resolve().parents[1];cache=W.parent/'deliverables'/'portable_crop_cache';cache.mkdir(exist_ok=True)
ordered=sorted((W/'crops').glob('*.png'),key=lambda p:p.stat().st_size,reverse=True)
# Identical crop bytes share one cache key: schedule each digest only once.
seen=set();items=[]
for p in ordered:
 digest=hashlib.sha256(p.read_bytes()).hexdigest()
 if digest not in seen:seen.add(digest);items.append(p)
def one(p):
 data=p.read_bytes();digest=hashlib.sha256(data).hexdigest();out=cache/(digest+'.jxl');proof=cache/(digest+'.jxl.json')
 if out.exists() and proof.exists():return json.loads(proof.read_text())
 im=Image.open(p);im.load()
 if im.mode!='RGB':return {'name':p.name,'skipped':im.mode,'saved_vs_webp':0}
 temp=cache/(digest+'.tmp.jxl')
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(p),'-c:v','libjxl','-distance','0','-effort','9','-threads','2',str(temp)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
 raw=subprocess.run(['ffmpeg','-v','error','-threads','2','-i',str(temp),'-f','rawvideo','-pix_fmt','rgb24','pipe:1'],check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE).stdout
 assert raw==im.tobytes(),p
 temp.replace(out)
 webp=cache/(digest+'.webp');baseline=min(len(data),webp.stat().st_size if webp.exists() else len(data))
 row={'name':p.name,'sha256':digest,'width':im.width,'height':im.height,'mode':'RGB','pixel_sha256':hashlib.sha256(raw).hexdigest(),'jxl_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'jxl_bytes':out.stat().st_size,'saved_vs_webp':max(0,baseline-out.stat().st_size)}
 proof.write_text(json.dumps(row)+'\n');return row
saved=0
with ThreadPoolExecutor(max_workers=4) as pool:
 for n,row in enumerate(pool.map(one,items),1):
  saved+=row['saved_vs_webp']
  if n%20==0:print(json.dumps({'verified':n,'total':len(items),'bytes_saved_vs_webp':saved}),flush=True)
print(json.dumps({'complete':True,'crops':len(items),'saved_vs_webp':saved}),flush=True)
