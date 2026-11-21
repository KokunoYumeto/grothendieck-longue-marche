from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json
root=Path(__file__).resolve().parent
source=root.parents[3]/'source/SP40_CW_81_scans/J81-03_81_scan026.jpg'
box=(395,1210,485,1365)
im=Image.open(source).convert('RGB').crop(box)
size=im.size
im=im.resize((2200,round(2200*im.height/im.width)),Image.Resampling.LANCZOS)
im=ImageOps.autocontrast(im)
im=im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=120,threshold=3))
dest=root/'crops/17_pale_arc.png'; im.save(dest)
rec={'path':'crops/17_pale_arc.png','bbox':list(box),'rotation':0,'crop_size':list(size),'rotated_size':list(size),'display_size':list(im.size),'resize':'PIL LANCZOS','autocontrast':True,'sharpen':{'method':'UnsharpMask','radius':1.2,'percent':120,'threshold':3},'purpose':'new pale arc target first noticed at left context boundary of crop08; complete local attachment and endpoints; settled barred formula not reopened','status_before_view':'new unresolved graphical locus with previously clipped left extent'}
arr=json.loads((root/'crop_plan.json').read_text()); arr.append(rec); (root/'crop_plan.json').write_text(json.dumps(arr,ensure_ascii=False,indent=2)+'\n')
print(rec)
