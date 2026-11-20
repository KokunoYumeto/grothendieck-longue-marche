from PIL import Image, ImageOps, ImageFilter
from pathlib import Path
import json
root=Path('/workspace/scratch/006c0e32b2af/out/readers/scan075/C')
source='/workspace/scratch/006c0e32b2af/source/SP46_CW_37_scans/H37-01_37_scan075.jpg'
item={'id':'formula_label','bbox':[190,1197,253,1261],'rotation':0,'reason':'Remaining open shape of the first displayed label: check whether its separated upper trace belongs to 1 or i.'}
im=Image.open(source).crop(item['bbox'])
im=ImageOps.autocontrast(im,cutoff=0.4)
im=im.resize((2400,round(im.height*2400/im.width)),Image.Resampling.LANCZOS)
im=im.filter(ImageFilter.UnsharpMask(radius=1.5,percent=115,threshold=3))
item['file']='crops/crop_C_075_formula_label.jpg'
item['processing']='RGB autocontrast cutoff 0.4%; LANCZOS resize to 2400 px width; UnsharpMask radius 1.5, percent 115, threshold 3; JPEG quality 96, no subsampling.'
im.save(root/item['file'],quality=96,subsampling=0)
items=json.load(open(root/'crop_log.json'))
items.append(item)
json.dump(items,open(root/'crop_log.json','w'),ensure_ascii=False,indent=2)
print(item)
