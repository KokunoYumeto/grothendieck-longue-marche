from pathlib import Path
from PIL import Image
import hashlib,json,subprocess,time,shutil
root=Path(__file__).resolve().parents[2];base=root/'work/compression_engineering';old=root/'work/checkpoint06_source/crops';new=root/'work/SP82_C13_148/crops';cache=root/'work/jxl_evidence_cache';best=root/'work/jxl_best_evidence_cache'
records=[]
for p in sorted(new.rglob('*')):
 if not p.is_file() or p.suffix not in {'.png','.webp'} or (old/p.relative_to(new)).exists():continue
 im=Image.open(p);rgba=im.convert('RGBA').tobytes();h=hashlib.sha256(rgba).hexdigest();dest=cache/(h+'.jxl');started=time.time()
 if not dest.exists():
  tmp=cache/(h+'.prewarm.tmp.jxl')
  subprocess.run(['ffmpeg','-v','error','-nostdin','-y','-i',str(p),'-c:v','libjxl','-distance','0','-effort','9','-frames:v','1','-threads','1',str(tmp)],check=True)
  dec=subprocess.run(['ffmpeg','-v','error','-nostdin','-i',str(tmp),'-f','rawvideo','-pix_fmt','rgba','-threads','1','pipe:1'],check=True,stdout=subprocess.PIPE).stdout
  assert dec==rgba,p;tmp.rename(dest)
 candidate=best/dest.name
 if not candidate.exists() or candidate.stat().st_size>dest.stat().st_size:
  tmp=candidate.with_suffix('.tmp');shutil.copy2(dest,tmp);tmp.replace(candidate)
 records.append({'file':str(p.relative_to(root/'work/SP82_C13_148')),'source_bytes':p.stat().st_size,'jxl_bytes':dest.stat().st_size,'rgba_sha256':h,'pixels_identical':True,'seconds':time.time()-started})
 if len(records)%10==0:print(json.dumps({'new_crops':len(records),'source_bytes':sum(r['source_bytes'] for r in records),'jxl_bytes':sum(r['jxl_bytes'] for r in records)}),flush=True)
 (base/'new_crops_encoding.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps({'complete':True,'new_crops':len(records),'source_bytes':sum(r['source_bytes'] for r in records),'jxl_bytes':sum(r['jxl_bytes'] for r in records)}),flush=True)
