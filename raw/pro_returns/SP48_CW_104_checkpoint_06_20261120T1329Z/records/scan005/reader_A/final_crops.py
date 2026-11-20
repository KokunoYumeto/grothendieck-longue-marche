from PIL import Image, ImageOps
from pathlib import Path
import json
root=Path('/workspace/scratch/7178efd1cfac/SP48_CW_104/records/scan005/reader_A')
src=Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans/H104-01_104_scan005.jpg')
im=Image.open(src)
manifest=json.loads((root/'crop_manifest.json').read_text())
items=[('23_b_start',[263,920,484,1002],2200,'Check small underline and F_0 at b opening'),('24_bprime_start',[274,1096,494,1182],2200,'Check small underline and F_0 at b-prime opening'),('25_bprime_membership',[510,1165,618,1266],2200,'Small F-prime_1 alphabet in vertical membership'),('26_c_wprime_membership',[1226,1309,1329,1413],2200,'Small F-prime_2 alphabet in c vertical membership'),('27_cprime_wprime_membership',[953,1555,1037,1639],2200,'Small F-prime_2 alphabet in c-prime vertical membership'),('28_cprime_w_membership',[1375,1519,1469,1613],2200,'Small F_2 alphabet in c-prime vertical membership')]
for ident,box,width,purpose in items:
 c=ImageOps.autocontrast(im.crop(box),cutoff=0)
 c=c.resize((width,round(c.height*width/c.width)),Image.Resampling.LANCZOS)
 p=root/'crops'/f'{ident}.png'; c.save(p)
 manifest.append({'id':ident,'path':str(p),'source':str(src),'bbox':box,'rotation_degrees_counterclockwise':0,'processing':['crop','no rotation','autocontrast cutoff 0','LANCZOS enlargement'],'sharpening':'none','output_size':list(c.size),'purpose':purpose,'viewed':False})
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Added six final small-glyph crops; no already-decided locus was recropped.')
