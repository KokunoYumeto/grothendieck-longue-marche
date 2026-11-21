from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from PIL import Image
import os,subprocess,time,json
base=Path('work/compression_engineering');source=Path('work/checkpoint06_source/crops/second/148_scan036/S36-13.png')
rgba=Image.open(source).convert('RGBA').tobytes()
def trial(item):
 name,opts=item;dest=base/('tune2_'+name+'.jxl');env=os.environ.copy();env['LD_PRELOAD']=str((base/'jxl_tune2_shim.so').resolve());env['EVIDENCE_JXL_TUNE']=opts
 t=time.time();p=subprocess.run(['ffmpeg','-v','error','-nostdin','-n','-i',str(source),'-c:v','libjxl','-distance','0','-effort','9','-frames:v','1','-threads','2',str(dest)],env=env,capture_output=True)
 if p.returncode:return dict(name=name,opts=opts,error=p.stderr.decode(),seconds=time.time()-t)
 dec=subprocess.run(['ffmpeg','-v','error','-i',str(dest),'-f','rawvideo','-pix_fmt','rgba','-threads','1','pipe:1'],capture_output=True,check=True).stdout
 out=dict(name=name,opts=opts,bytes=dest.stat().st_size,identical=dec==rgba,seconds=round(time.time()-t,2),stderr=p.stderr.decode());print(json.dumps(out),flush=True);return out
params=[('tree100_real','28:100'),('prev11_group3','29:11,26:3'),('prev11_predbest','29:11,27:15'),('prev11_tree100','29:11,28:100'),('prev11_group3_predbest','29:11,26:3,27:15')] #('tree100','28:100'),('pbest','27:15'),('group1024','26:3'),('group128','26:0'),('tree100_pbest','28:100,27:15'),('prev11','29:11'),('colorspace0','25:0'),('colorspace40','25:40')]
with ThreadPoolExecutor(max_workers=3) as pool:r=list(pool.map(trial,params))
(base/'tuning2_results.json').write_text(json.dumps(r,indent=2))
