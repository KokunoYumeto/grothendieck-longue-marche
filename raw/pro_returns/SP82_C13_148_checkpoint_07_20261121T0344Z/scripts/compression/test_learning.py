from pathlib import Path
from PIL import Image
import os,subprocess,time,json,sys
base=Path('work/compression_engineering').resolve();n=int(sys.argv[1]);source=Path('work/checkpoint06_source/crops/second/148_scan036/S36-13.png');dest=base/('learn_'+str(n)+'.jxl');env=os.environ.copy();env['LD_PRELOAD']=str(base/'jxl_tune2_shim.so');env['EVIDENCE_JXL_TUNE']='29:11,26:3,27:15,28:'+str(n)
t=time.time()
subprocess.run(['ffmpeg','-v','error','-nostdin','-n','-i',str(source),'-c:v','libjxl','-distance','0','-effort','9','-frames:v','1','-threads','2',str(dest)],check=True,env=env)
rgba=Image.open(source).convert('RGBA').tobytes();dec=subprocess.run(['ffmpeg','-v','error','-i',str(dest),'-f','rawvideo','-pix_fmt','rgba','-threads','1','pipe:1'],check=True,stdout=subprocess.PIPE).stdout;assert rgba==dec
result=dict(percent=n,bytes=dest.stat().st_size,seconds=round(time.time()-t,2),pixels_identical=True);(base/('learn_'+str(n)+'.json')).write_text(json.dumps(result));print(result,flush=True)
