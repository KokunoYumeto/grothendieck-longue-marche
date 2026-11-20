from PIL import Image, ImageOps
from pathlib import Path
import json
root=Path('/workspace/scratch/7178efd1cfac/SP48_CW_104/records/scan005/reader_A')
src=Path('/workspace/scratch/7178efd1cfac/source/SP48_CW_104_scans/H104-01_104_scan005.jpg')
im=Image.open(src)
manifest=json.loads((root/'crop_manifest.json').read_text())
items=[('21_a_alphabets',[249,817,795,923],2800,0,'F alphabets in first quantified condition, unresolved in half a'),('22_cprime_F',[488,1498,582,1575],2200,0,'F alphabet in c-prime, unresolved in half a')]
for ident,box,width,angle,purpose in items:
 c=ImageOps.autocontrast(im.crop(box),cutoff=0)
 c=c.resize((width,round(c.height*width/c.width)),Image.Resampling.LANCZOS)
 p=root/'crops'/f'{ident}.png'; c.save(p)
 manifest.append({'id':ident,'path':str(p),'source':str(src),'bbox':box,'rotation_degrees_counterclockwise':0,'processing':['crop','no rotation','autocontrast cutoff 0','LANCZOS enlargement'],'sharpening':'none','output_size':list(c.size),'purpose':purpose,'viewed':False})
(root/'crop_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Added 2 not-yet-viewed alphabet crops; 20 earlier crops have now been seen.')
